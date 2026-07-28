#!/usr/bin/env python3
"""layout_check.py — the layout gate (DESIGN_DOCTRINE section 3).

Why this exists. The single largest quality defect in this repo's history is
text landing on other text or on painted art, because DOM elements were placed
by hand against coordinates the canvas drew separately. `qa.py` structurally
cannot see canvas ink, and its text-on-text gate only fires at 30 percent
overprint, so clipped, kissing and unreadable text shipped through a green
machine QA more than once. This script is the tighter net.

It reads the same `render_report.json` + PNGs `qa.py` reads, plus an OPTIONAL
zones declaration (`zones.json`, written by the storyboard before any slide
code exists) and enforces:

  1. NEAR-MISS OVERLAP   any two text line boxes overprinting by >= 6px in both
                         axes (qa.py needs 30 percent of the smaller box).
  2. GUTTER BLEED        vertically-adjacent columns whose horizontal gap falls
                         under the 16px minimum (the "column two bled into
                         column three" defect).
  3. WORST-TILE CONTRAST contrast sampled per ~24px tile under every text line
                         and reported at its MINIMUM, not its median. Text that
                         is legible on average and invisible over one bright
                         patch of art fails here and passes qa.py.
  4. SAFE AREA           a hard fail, not a warning, for primary text.
  5. ZONE CONFORMANCE    every primary text node declares data-zone, that zone
                         is declared in zones.json, and the node's box lies
                         inside it. Text inside ART needs data-knockout.
  6. VERTICAL BUDGETS    two data-block groups may not overlap in both axes.
  7. WIDOWS              a final line carrying one short word (WARN).

Usage:
  python scripts/layout_check.py --render-dir out/<date>/render \\
      [--zones out/<date>/zones.json] [--strict-zones]

Exit codes: 0 pass (warnings allowed), 1 any FAIL.
Writes <render-dir>/layout_check.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

SAFE_MARGIN = 80        # px at the 1080x1350 design size
NEAR_MISS_PX = 6        # overlap in BOTH axes that counts as a collision
MIN_GUTTER = 16         # px of clear air required between side-by-side text
TILE = 24               # contrast sampling tile, design px
CONTRAST_FAIL = 3.0     # worst-tile ratio below this fails on primary text
CONTRAST_FAIL_SMALL = 2.5   # ... and on any other non-decorative text
CONTRAST_WARN = 4.5
PRIMARY_PX = 30         # font-size at or above which text is "primary"
ZONE_TOL = 6            # px a box may sit outside its declared zone
SAFE_TOL = 8            # px of slack on the safe area before it counts
INK_DIST = 90           # sum-abs RGB distance under which a pixel is glyph ink
INK_DILATE = 2          # DESIGN px to grow the ink mask by (anti-aliased edges);
                        # scaled to device px at sample time. Under-dilating
                        # leaves the glyph halo in the "background" and reports
                        # ~1.4:1 on cream-on-black display type.
MIN_BG_FRAC = 0.25      # a tile below this much background is unmeasurable


def rel_luminance(rgb):
    def chan(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(x) for x in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def parse_css_color(s):
    m = re.match(r"rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)", s or "")
    return tuple(float(m.group(i)) for i in (1, 2, 3)) if m else None


def _boxes(node):
    return node.get("lines") or [[node["x"], node["y"], node["w"], node["h"]]]


def _inter(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return (min(ax + aw, bx + bw) - max(ax, bx),
            min(ay + ah, by + bh) - max(ay, by))


def _span(nodes):
    """Union bbox over every line box of every node."""
    xs, ys, xe, ye = 1e9, 1e9, -1e9, -1e9
    for n in nodes:
        for x, y, w, h in _boxes(n):
            xs, ys = min(xs, x), min(ys, y)
            xe, ye = max(xe, x + w), max(ye, y + h)
    return [xs, ys, xe - xs, ye - ys]


def _dilate(mask, k):
    m = mask.copy()
    for _ in range(k):
        n = m.copy()
        n[:-1] |= m[1:]; n[1:] |= m[:-1]
        n[:, :-1] |= m[:, 1:]; n[:, 1:] |= m[:, :-1]
        m = n
    return m


def _lum_arr(px):
    c = px / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def worst_tile_contrast(arr, box, color, scale):
    """Minimum contrast between text ink and background over ~TILE-px cells.

    qa.py estimates ONE ratio for a whole line box from the median background,
    which averages away exactly the failure we care about: a headline crossing
    a lit region of canvas art, readable for four words and gone for the fifth.
    Here the line box is tiled and the WORST tile is what we report.

    Background is everything OUTSIDE a dilated glyph-ink mask, never a
    percentile split: on large display type a tile can be more than half ink,
    and splitting by percentile then compares ink against ink and reports a
    ratio of 1.0 on perfectly legible text. Tiles with too little background
    left to measure are skipped rather than guessed at.
    Returns (min_ratio, (tx, ty)) or (None, None) when unmeasurable.
    """
    x, y, w, h = box
    H, W = arr.shape[:2]
    ink = np.array(color)
    lt = rel_luminance(color)
    dil = max(2, int(round(INK_DILATE * scale)))
    worst, where = None, None
    for ty in range(int(y), int(y + h), TILE):
        for tx in range(int(x), int(x + w), TILE):
            x0, y0 = max(0, int(tx * scale)), max(0, int(ty * scale))
            x1 = min(W, int(min(tx + TILE, x + w) * scale))
            y1 = min(H, int(min(ty + TILE, y + h) * scale))
            if x1 - x0 < 6 or y1 - y0 < 6:
                continue
            crop = arr[y0:y1, x0:x1, :3].astype(float)
            inkmask = _dilate(np.abs(crop - ink).sum(axis=2) < INK_DIST, dil)
            bg = ~inkmask
            if bg.mean() < MIN_BG_FRAC or bg.sum() < 12:
                continue
            lums = _lum_arr(crop)[bg]
            ratios = (np.maximum(lums, lt) + 0.05) / (np.minimum(lums, lt) + 0.05)
            r = float(np.percentile(ratios, 5))   # 5th pct, not min: ignore stray AA pixels
            if worst is None or r < worst:
                worst, where = r, (tx, ty)
    return worst, where


def check_slide(rec, arr, scale, design, zones, strict_zones):
    res = {"file": rec["file"], "fails": [], "warns": []}
    dw, dh = design
    nodes = rec.get("text_nodes", [])
    idx = list(range(len(nodes)))

    # ---- 1. near-miss overlap -------------------------------------------
    for i in idx:
        a = nodes[i]
        a_anc = set(a.get("anc") or [])
        for j in idx[i + 1:]:
            b = nodes[j]
            if i in (b.get("anc") or []) or j in a_anc:
                continue
            hit = None
            for ab in _boxes(a):
                for bb in _boxes(b):
                    ix, iy = _inter(ab, bb)
                    if ix >= NEAR_MISS_PX and iy >= NEAR_MISS_PX:
                        hit = (ix, iy, ab, bb)
            if not hit:
                continue
            ix, iy, ab, _ = hit
            msg = (f"text overprint {ix}x{iy}px: '{a['text'][:34]}' x "
                   f"'{b['text'][:34]}' near {ab[0]},{ab[1]}")
            if a.get("overlap_ok") or b.get("overlap_ok"):
                res["warns"].append(msg + " [data-overlap-ok]")
            elif a.get("decorative") and b.get("decorative"):
                res["warns"].append(msg + " [both decorative]")
            else:
                res["fails"].append(msg)

    # ---- 2. gutter bleed -------------------------------------------------
    for i in idx:
        a = nodes[i]
        if a.get("decorative"):
            continue
        a_anc = set(a.get("anc") or [])
        for j in idx[i + 1:]:
            b = nodes[j]
            if b.get("decorative") or i in (b.get("anc") or []) or j in a_anc:
                continue
            if a.get("block") and a.get("block") == b.get("block"):
                continue          # same column, stacked lines
            for ax, ay, aw, ah in _boxes(a):
                for bx, by, bw, bh in _boxes(b):
                    vov = min(ay + ah, by + bh) - max(ay, by)
                    if vov < 8:
                        continue
                    gap = max(ax, bx) - min(ax + aw, bx + bw)
                    if 0 <= gap < MIN_GUTTER:
                        res["fails"].append(
                            f"gutter {gap}px < {MIN_GUTTER}px between "
                            f"'{a['text'][:28]}' and '{b['text'][:28]}' "
                            f"near {max(ax, bx)},{max(ay, by)}")
                        break
                else:
                    continue
                break

    # ---- 3. worst-tile contrast + 4. safe area ---------------------------
    for n in nodes:
        if n.get("decorative"):
            continue
        primary = n["font_px"] >= PRIMARY_PX
        if (n["x"] < SAFE_MARGIN - SAFE_TOL or n["y"] < SAFE_MARGIN - SAFE_TOL or
                n["x"] + n["w"] > dw - SAFE_MARGIN + SAFE_TOL or
                n["y"] + n["h"] > dh - SAFE_MARGIN + SAFE_TOL):
            m = (f"outside {SAFE_MARGIN}px safe area: '{n['text'][:40]}' at "
                 f"{n['x']},{n['y']} {n['w']}x{n['h']}")
            (res["fails"] if primary else res["warns"]).append(m)
        color = parse_css_color(n.get("color"))
        if color is None or arr is None:
            continue
        for box in _boxes(n):
            if box[2] < 8 or box[3] < 8:
                continue
            r, where = worst_tile_contrast(arr, box, color, scale)
            if r is None:
                continue
            # Primary text carries the WCAG large-text floor. Small text is not
            # exempt: a 24px sourcing label is load-bearing (DESIGN_DOCTRINE
            # section 5) and at 1.5:1 over art it is simply not there, so it
            # fails too, just at the lower floor where it is unarguable.
            floor = CONTRAST_FAIL if primary else CONTRAST_FAIL_SMALL
            if r < floor:
                res["fails"].append(
                    f"worst-tile contrast {r:.1f} at {where[0]},{where[1]} under "
                    f"'{n['text'][:40]}' (floor {floor}) — art is eating the text")
                break
            if r < CONTRAST_WARN:
                res["warns"].append(
                    f"worst-tile contrast {r:.1f} at {where[0]},{where[1]} under "
                    f"'{n['text'][:40]}'")
                break

    # ---- 5. zone conformance --------------------------------------------
    zdecl = (zones or {}).get(rec["file"]) or (zones or {}).get(Path(rec["file"]).name)
    if zdecl:
        rects = {k: v for k, v in (zdecl.get("zones") or {}).items()}
        art = [rects[k] for k in rects if k.upper() == "ART"]
        art += [list(r) for r in (zdecl.get("art_rects") or [])]
        for n in nodes:
            if n.get("decorative"):
                continue
            zone = n.get("zone")
            if not zone:
                lvl = res["fails"] if strict_zones else res["warns"]
                lvl.append(f"no data-zone on '{n['text'][:40]}'")
                continue
            if zone not in rects:
                res["fails"].append(
                    f"undeclared zone '{zone}' on '{n['text'][:40]}' "
                    f"(declared: {', '.join(sorted(rects)) or 'none'})")
                continue
            zx, zy, zw, zh = rects[zone]
            if (n["x"] < zx - ZONE_TOL or n["y"] < zy - ZONE_TOL or
                    n["x"] + n["w"] > zx + zw + ZONE_TOL or
                    n["y"] + n["h"] > zy + zh + ZONE_TOL):
                res["fails"].append(
                    f"'{n['text'][:34]}' at {n['x']},{n['y']} {n['w']}x{n['h']} "
                    f"escapes zone {zone} [{zx},{zy},{zw},{zh}]")
            if zone.upper() != "ART" and not n.get("knockout"):
                for ax, ay, aw, ah in art:
                    for bx, by, bw, bh in _boxes(n):
                        ix, iy = _inter([ax, ay, aw, ah], [bx, by, bw, bh])
                        if ix > NEAR_MISS_PX and iy > NEAR_MISS_PX:
                            res["fails"].append(
                                f"'{n['text'][:34]}' sits over the ART rect "
                                f"[{ax},{ay},{aw},{ah}] with no data-knockout plate")
                            break
                    else:
                        continue
                    break

    # ---- 6. vertical budgets --------------------------------------------
    blocks = {}
    for n in nodes:
        if n.get("decorative") or not n.get("block"):
            continue
        blocks.setdefault(n["block"], []).append(n)
    names = sorted(blocks)
    for i, na in enumerate(names):
        for nb in names[i + 1:]:
            ix, iy = _inter(_span(blocks[na]), _span(blocks[nb]))
            if ix > 8 and iy > 8:
                res["fails"].append(
                    f"budget overlap {ix}x{iy}px between blocks '{na}' and '{nb}'")

    # ---- 7. widows -------------------------------------------------------
    for n in nodes:
        if n.get("decorative") or n["font_px"] < PRIMARY_PX:
            continue
        ls = _boxes(n)
        if len(ls) < 2:
            continue
        widest = max(b[2] for b in ls)
        last = ls[-1]
        words = n["text"].split()
        if last[2] < widest * 0.18 and words and len(words[-1]) <= 12:
            res["warns"].append(
                f"widow: last line of '{n['text'][:34]}' is {last[2]}px of {widest}px")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render-dir", required=True)
    ap.add_argument("--zones", help="zones.json declared by the storyboard")
    ap.add_argument("--strict-zones", action="store_true",
                    help="fail (not warn) on primary text with no data-zone")
    args = ap.parse_args()

    rdir = Path(args.render_dir)
    report = json.loads((rdir / "render_report.json").read_text())
    scale = report["canvas"]["scale"]
    design = (report["canvas"]["width"], report["canvas"]["height"])

    zones = None
    if args.zones:
        zp = Path(args.zones)
        if zp.exists():
            z = json.loads(zp.read_text())
            zones = z.get("slides", z)
        else:
            print(f"zones file not found: {zp}", file=sys.stderr)
            sys.exit(2)

    out = {"slides": [], "fails": 0, "warns": 0, "zones_declared": bool(zones)}
    for rec in report["slides"]:
        png = rdir / rec["png"]
        arr = np.asarray(Image.open(png).convert("RGB")) if png.exists() else None
        res = check_slide(rec, arr, scale, design, zones, args.strict_zones)
        out["fails"] += len(res["fails"])
        out["warns"] += len(res["warns"])
        out["slides"].append(res)

    out["verdict"] = "FAIL" if out["fails"] else ("WARN" if out["warns"] else "PASS")
    (rdir / "layout_check.json").write_text(json.dumps(out, indent=2))
    for s in out["slides"]:
        flag = "FAIL" if s["fails"] else ("warn" if s["warns"] else "ok  ")
        print(f"[{flag}] {s['file']}  fails={len(s['fails'])} warns={len(s['warns'])}")
        for f in s["fails"]:
            print(f"    FAIL: {f}")
        for w in s["warns"][:6]:
            print(f"    warn: {w}")
    print(f"verdict: {out['verdict']}  (report -> {rdir / 'layout_check.json'})")
    sys.exit(1 if out["fails"] else 0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""variety_check.py — the two variety engines (knowledge/VARIETY.md).

The maintainer's standard, stated plainly: no two slides in one run may look
like the same template with different words on them, and no run may look like
a previous run. Both are enforced here, objectively, on pixels and geometry,
so neither can be satisfied by relabelling a dossier.

ENGINE A — WITHIN-DECK (every slide in a run is custom)
  A1 pairwise layout-skeleton overlap   (same text scaffold = same template)
  A2 pairwise image correlation         (same picture, different words)
  A3 pairwise palette distance          (same colour story on every slide)
  A4 deck value arc                     (a deck at one brightness is the
                                         "uniform deck" failure)
  A5 declared per-slide signature       (mode / layout family / art system all
                                         distinct, per DESIGN_DOCTRINE 1)

ENGINE B — CROSS-RUN (no run looks like a previous run)
  B1 declared divergence table against ledger/artwork.json history
  B2 pixel divergence of every slide against every stored slide fingerprint
     from the last N runs (ledger/fingerprints.json)
  B3 render-ladder rotation (the top rung reached may not repeat every run)

Usage:
  # pre-planning: check a proposed signature before any slide is coded
  python scripts/variety_check.py --signature out/<date>/deck_signature.json --plan-only

  # quality gate: after a render pass
  python scripts/variety_check.py --render-dir out/<date>/render \\
      --signature out/<date>/deck_signature.json

  # retro: record this run so future runs must diverge from it
  python scripts/variety_check.py --render-dir out/<date>/render \\
      --signature out/<date>/deck_signature.json --record

Exit codes: 0 pass (warnings allowed), 1 any FAIL.
Writes <render-dir>/variety_check.json (or out/variety_plan.json with --plan-only)
"""

import argparse
import base64
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[1]
ARTWORK = REPO / "ledger" / "artwork.json"
FINGERPRINTS = REPO / "ledger" / "fingerprints.json"

MODES = ["SCENE", "OBJECT", "DOCUMENT", "DIAGRAM", "DATA", "FIELD"]
MODE_CAP = 3            # DESIGN_DOCTRINE 1: no mode more than three times

# --- within-deck thresholds (calibrated against the run-2 deck, the one the
#     maintainer called cookie-cutter; see knowledge/VARIETY.md for the numbers)
LAYOUT_IOU_FAIL = 0.55
LAYOUT_IOU_WARN = 0.42
IMAGE_CORR_FAIL = 0.86
IMAGE_CORR_WARN = 0.74
PALETTE_SIM_FAIL = 0.94
VALUE_ARC_FAIL = 0.12   # max minus min mean luminance across the deck
VALUE_ARC_WARN = 0.22
# Deck-level sameness, the single most honest number in this file. Measured on
# the deck the maintainer rejected as cookie-cutter (2026-07-25, 10 slides):
# median pairwise image correlation 0.978, median layout IoU 0.565, value arc
# 0.059. A deck with genuinely custom slides lands far below all three.
DECK_CORR_FAIL = 0.70
DECK_CORR_WARN = 0.55
DECK_IOU_FAIL = 0.50
DECK_IOU_WARN = 0.38
# a pair fails when it is too close on BOTH structure and picture; either one
# alone is a warning, because a shared scaffold with genuinely different art is
# a legitimate series device and identical art with different scaffolds is not
# a template.

# --- cross-run thresholds
XRUN_CORR_FAIL = 0.90
XRUN_CORR_WARN = 0.80
XRUN_LOOKBACK = 4       # runs of pixel history a new deck must diverge from

# --- declared-field divergence: field -> how many previous runs it must differ
#     from. Mirrors the sibling studio's law, extended for the new doctrine.
DIVERGENCE = {
    "hero_structure": 4,
    "atmosphere": 3,
    "depth_technique": 3,
    "continuity_device": 2,
    "hook_archetype": 3,
    "palette_family": 3,
    "type_pairing": 2,
    "narrative_structure": 2,
    "render_ladder_top": 2,
    "line_voice": 2,
}

GRID_W, GRID_H = 12, 15     # layout-skeleton cells
FP_W, FP_H = 16, 20         # stored image fingerprint


# ---------------------------------------------------------------- fingerprints
def layout_skeleton(rec, design):
    """Coarse occupancy grid of every text line box on the slide.

    This is the slide's SCAFFOLD with the words and the art removed. Two slides
    built from one template light up the same cells no matter what they say.
    """
    dw, dh = design
    g = np.zeros((GRID_H, GRID_W), dtype=bool)
    for n in rec.get("text_nodes", []):
        for x, y, w, h in (n.get("lines") or [[n["x"], n["y"], n["w"], n["h"]]]):
            c0 = max(0, int(x / dw * GRID_W)); c1 = min(GRID_W, int(math.ceil((x + w) / dw * GRID_W)))
            r0 = max(0, int(y / dh * GRID_H)); r1 = min(GRID_H, int(math.ceil((y + h) / dh * GRID_H)))
            g[r0:r1, c0:c1] = True
    return g


def image_fp(png):
    im = Image.open(png).convert("L").resize((FP_W, FP_H), Image.LANCZOS)
    a = np.asarray(im, dtype=float) / 255.0
    return a


def norm_fp(a):
    v = a - a.mean()
    s = v.std()
    return v / s if s > 1e-6 else v


def palette_fp(png):
    im = Image.open(png).convert("RGB").resize((64, 80), Image.LANCZOS)
    a = np.asarray(im).reshape(-1, 3) // 64          # 4 bins per channel
    idx = a[:, 0] * 16 + a[:, 1] * 4 + a[:, 2]
    h = np.bincount(idx, minlength=64).astype(float)
    return h / h.sum()


def iou(a, b):
    u = (a | b).sum()
    return float((a & b).sum() / u) if u else 0.0


def corr(a, b):
    return float((norm_fp(a) * norm_fp(b)).mean())


def hist_sim(a, b):
    return float(np.minimum(a, b).sum())


def b64(a):
    return base64.b64encode((a * 255).astype(np.uint8).tobytes()).decode()


def unb64(s):
    return np.frombuffer(base64.b64decode(s), dtype=np.uint8).reshape(FP_H, FP_W).astype(float) / 255.0


# ------------------------------------------------------------ engine A: deck
def check_signature(sig, n_slides, out):
    """A5 + the plan-time half of the doctrine. Runs with or without renders."""
    slides = sig.get("slides") or []
    if n_slides and len(slides) != n_slides:
        out["fails"].append(
            f"signature declares {len(slides)} slides, deck has {n_slides}")
    if not slides:
        out["fails"].append("deck_signature.json declares no slides")
        return

    counts = {}
    for s in slides:
        m = (s.get("mode") or "").upper()
        if m not in MODES:
            out["fails"].append(
                f"slide {s.get('n')} mode '{s.get('mode')}' is not one of {', '.join(MODES)}")
        counts[m] = counts.get(m, 0) + 1
    for m, c in sorted(counts.items()):
        if c > MODE_CAP:
            out["fails"].append(
                f"compositional mode {m} used {c} times (cap {MODE_CAP}) — "
                "this is the uniform-deck failure")
    for a, b in zip(slides, slides[1:]):
        if (a.get("mode") or "").upper() == (b.get("mode") or "").upper():
            out["warns"].append(
                f"slides {a.get('n')} and {b.get('n')} are both {a.get('mode')} back to back")

    # every slide must be its own thing: no repeated (mode, layout_family) and
    # no repeated art_system anywhere in the deck.
    seen_pairs, seen_art = {}, {}
    for s in slides:
        key = ((s.get("mode") or "").upper(), (s.get("layout_family") or "").strip().lower())
        if not key[1]:
            out["fails"].append(f"slide {s.get('n')} declares no layout_family")
        elif key in seen_pairs:
            out["fails"].append(
                f"slides {seen_pairs[key]} and {s.get('n')} share mode+layout_family "
                f"{key[0]}/{key[1]} — that is a template, not two custom slides")
        else:
            seen_pairs[key] = s.get("n")
        art = (s.get("art_system") or "").strip().lower()
        if not art:
            out["fails"].append(f"slide {s.get('n')} declares no art_system")
        elif art in seen_art:
            out["warns"].append(
                f"slides {seen_art[art]} and {s.get('n')} reuse art_system '{art}'")
        else:
            seen_art[art] = s.get("n")
        if len((s.get("custom_note") or "").split()) < 6:
            out["fails"].append(
                f"slide {s.get('n')} has no custom_note — one sentence naming what "
                "makes this slide unlike every other slide in the deck is required")

    fams = {(s.get("layout_family") or "").strip().lower() for s in slides if s.get("layout_family")}
    need = math.ceil(len(slides) * 0.7)
    if len(fams) < need:
        out["fails"].append(
            f"{len(fams)} distinct layout families across {len(slides)} slides "
            f"(floor {need})")

    vals = [(s.get("value") or "").strip().lower() for s in slides]
    if len(set(v for v in vals if v)) < 2:
        out["fails"].append("declared value arc is flat — the deck is one brightness")

    ladder = (sig.get("deck") or {}).get("render_ladder_top", "").strip().lower()
    if ladder not in ("akthree", "aksdf"):
        out["fails"].append(
            f"render_ladder_top is '{ladder or 'unset'}' — DESIGN_DOCTRINE 2 requires at "
            "least one slide reaching akthree or aksdf")


def check_within_deck(slides, out):
    """A1-A4. `slides` is a list of dicts with fp/skeleton/palette/lum."""
    for i in range(len(slides)):
        for j in range(i + 1, len(slides)):
            a, b = slides[i], slides[j]
            li = iou(a["skel"], b["skel"])
            ci = corr(a["fp"], b["fp"])
            pi = hist_sim(a["pal"], b["pal"])
            pair = f"{a['name']} x {b['name']}"
            detail = f"layout IoU {li:.2f}, image corr {ci:.2f}, palette {pi:.2f}"
            if li >= LAYOUT_IOU_FAIL and ci >= IMAGE_CORR_FAIL:
                out["fails"].append(
                    f"{pair}: same template ({detail}) — every slide in a run is custom")
            elif li >= LAYOUT_IOU_FAIL:
                out["warns"].append(f"{pair}: shared text scaffold ({detail})")
            elif ci >= IMAGE_CORR_FAIL:
                out["warns"].append(f"{pair}: near-identical picture ({detail})")
            elif li >= LAYOUT_IOU_WARN and ci >= IMAGE_CORR_WARN:
                out["warns"].append(f"{pair}: drifting toward one template ({detail})")
            if pi >= PALETTE_SIM_FAIL and ci >= IMAGE_CORR_WARN:
                out["warns"].append(f"{pair}: one palette and one picture ({detail})")
            out["pairs"].append({"pair": pair, "layout_iou": round(li, 3),
                                 "image_corr": round(ci, 3), "palette_sim": round(pi, 3)})

    lums = [s["lum"] for s in slides]
    arc = max(lums) - min(lums)
    out["value_arc"] = round(arc, 3)
    if arc < VALUE_ARC_FAIL:
        out["fails"].append(
            f"value arc {arc:.3f} < {VALUE_ARC_FAIL} — every slide is the same brightness "
            "(the uniform deck)")
    elif arc < VALUE_ARC_WARN:
        out["warns"].append(f"shallow value arc {arc:.3f} (aim above {VALUE_ARC_WARN})")

    # Deck sameness: one number for "does the contact sheet read as one image
    # repeated". Pair rules can be dodged by making one outlier slide; the
    # median cannot.
    med_c = float(np.median([p["image_corr"] for p in out["pairs"]]))
    med_i = float(np.median([p["layout_iou"] for p in out["pairs"]]))
    out["deck_median_image_corr"] = round(med_c, 3)
    out["deck_median_layout_iou"] = round(med_i, 3)

    # The retro (VARIETY.md, "the closest pair, by eye") has to look at the two
    # most similar slides. Until 2026-08-15 that number was printed to the
    # console and never persisted, so the 2026-08-15 retro was handed the wrong
    # pair from a hand read of pairs[]. Persist the ranking the console already
    # computes, so the retro reads a number instead of scanning a matrix.
    ranked = sorted(out["pairs"], key=lambda p: -(p["layout_iou"] + p["image_corr"]))
    out["closest_pairs"] = ranked[:5]
    out["closest_pair"] = ranked[0]["pair"] if ranked else None
    if med_c >= DECK_CORR_FAIL:
        out["fails"].append(
            f"deck median image correlation {med_c:.2f} >= {DECK_CORR_FAIL} — the contact "
            "sheet reads as one image repeated")
    elif med_c >= DECK_CORR_WARN:
        out["warns"].append(f"deck median image correlation {med_c:.2f} is high")
    if med_i >= DECK_IOU_FAIL:
        out["fails"].append(
            f"deck median layout IoU {med_i:.2f} >= {DECK_IOU_FAIL} — one text scaffold "
            "is carrying the whole deck")
    elif med_i >= DECK_IOU_WARN:
        out["warns"].append(f"deck median layout IoU {med_i:.2f} is high")


# --------------------------------------------------------- engine B: history
def check_cross_run(sig, slides, artwork, fps, out, run_date):
    deck = sig.get("deck") or {}
    entries = [e for e in (artwork.get("entries") or []) if e.get("run_date") != run_date]
    for field, look in DIVERGENCE.items():
        val = (deck.get(field) or "").strip().lower()
        if not val:
            out["warns"].append(f"deck signature declares no {field}")
            continue
        for e in entries[-look:]:
            if (e.get(field) or "").strip().lower() == val:
                out["fails"].append(
                    f"{field} '{deck.get(field)}' repeats run {e.get('run_date')} "
                    f"(must differ from the last {look})")
                break

    hist = [r for r in (fps.get("runs") or []) if r.get("run_date") != run_date][-XRUN_LOOKBACK:]
    for r in hist:
        for pv in r.get("slides", []):
            try:
                prev = unb64(pv["fp"])
            except Exception:
                continue
            for s in slides:
                c = corr(s["fp"], prev)
                if c >= XRUN_CORR_FAIL:
                    out["fails"].append(
                        f"{s['name']} is a near copy of {r.get('run_date')} "
                        f"{pv.get('name')} (corr {c:.2f}) — no run looks like a previous run")
                elif c >= XRUN_CORR_WARN:
                    out["warns"].append(
                        f"{s['name']} resembles {r.get('run_date')} {pv.get('name')} "
                        f"(corr {c:.2f})")


# ------------------------------------------------------------------ main
def load_deck(render_dir):
    rdir = Path(render_dir)
    report = json.loads((rdir / "render_report.json").read_text())
    design = (report["canvas"]["width"], report["canvas"]["height"])
    slides = []
    for rec in report["slides"]:
        png = rdir / rec["png"]
        if not png.exists():
            continue
        fp = image_fp(png)
        slides.append({
            "name": rec["file"],
            "png": str(png),
            "fp": fp,
            "skel": layout_skeleton(rec, design),
            "pal": palette_fp(png),
            "lum": float(fp.mean()),
        })
    return slides


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render-dir")
    ap.add_argument("--signature", required=True)
    ap.add_argument("--plan-only", action="store_true",
                    help="check the declared signature before any slide exists")
    ap.add_argument("--record", action="store_true",
                    help="append this run's fingerprints to ledger/fingerprints.json")
    ap.add_argument("--artwork", default=str(ARTWORK))
    ap.add_argument("--fingerprints", default=str(FINGERPRINTS))
    args = ap.parse_args()

    sig = json.loads(Path(args.signature).read_text())
    run_date = sig.get("run_date", "")
    artwork = json.loads(Path(args.artwork).read_text()) if Path(args.artwork).exists() else {}
    fps = json.loads(Path(args.fingerprints).read_text()) if Path(args.fingerprints).exists() \
        else {"_doc": "Per-run per-slide image fingerprints. Engine B of the variety "
                      "system reads this so a new deck must diverge from what shipped, "
                      "in pixels and not only in labels.", "runs": []}

    out = {"run_date": run_date, "fails": [], "warns": [], "pairs": []}

    slides = []
    if not args.plan_only:
        if not args.render_dir:
            print("--render-dir is required unless --plan-only", file=sys.stderr)
            sys.exit(2)
        slides = load_deck(args.render_dir)
        if not slides:
            print("no rendered slides found", file=sys.stderr)
            sys.exit(2)

    check_signature(sig, len(slides), out)
    if slides:
        check_within_deck(slides, out)
    check_cross_run(sig, slides, artwork, fps, out, run_date)

    out["verdict"] = "FAIL" if out["fails"] else ("WARN" if out["warns"] else "PASS")

    if args.record:
        if not slides:
            print("--record needs rendered slides", file=sys.stderr)
            sys.exit(2)
        runs = [r for r in fps.get("runs", []) if r.get("run_date") != run_date]
        runs.append({
            "run_date": run_date,
            "case_file_no": sig.get("case_file_no"),
            "slides": [{"name": s["name"], "mode": None, "fp": b64(s["fp"])} for s in slides],
        })
        fps["runs"] = runs[-12:]     # a year of history is plenty; keep the file small
        Path(args.fingerprints).write_text(json.dumps(fps, indent=1))
        out["recorded"] = True

    dest = (Path(args.render_dir) / "variety_check.json") if args.render_dir \
        else Path(args.signature).with_name("variety_plan.json")
    dest.write_text(json.dumps(out, indent=2))

    for f in out["fails"]:
        print(f"FAIL: {f}")
    for w in out["warns"]:
        print(f"warn: {w}")
    if out["pairs"]:
        worst = out.get("closest_pairs") or []
        print("closest pairs:")
        for p in worst:
            print(f"    {p['pair']}  IoU {p['layout_iou']}  corr {p['image_corr']}  "
                  f"palette {p['palette_sim']}")
        print(f"value arc: {out.get('value_arc')}")
    print(f"verdict: {out['verdict']}  (report -> {dest})")
    sys.exit(1 if out["fails"] else 0)


if __name__ == "__main__":
    main()

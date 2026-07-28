#!/usr/bin/env python3
"""coherence_check.py — the narrative coherence gate (knowledge/NARRATIVE_COHERENCE.md).

The maintainer's observation, which the last run's own score report confirms:
the editing loops chop the story up. A collision fix deletes a body paragraph
to make room, a word-count trim drops the clause that named the ladder rung,
and the deck ships as ten correct slides that no longer carry one idea. Every
individual edit passed its gate. The story died between them.

So the authored copy record is the STORY OF RECORD, and slide code is only its
rendering. This script enforces that, mechanically:

  1. CONTRACT      out/<date>/coherence.json declares the deck's one thesis and,
                   per slide, its role, the open loop it opens, and which
                   earlier slide it pays off. Every loop must close.
  2. FIDELITY      every authored string in copy.json.slides must actually be
                   on its rendered slide. A sentence that vanished in an edit
                   round is a FAIL, not a diff nobody reads.
  3. BODY PRESENT  a slide the copy record says has a body must render one.
                   (2026-07-25: slide 6 lost its entire body paragraph in a
                   collision fix and shipped as statistics with no prose.)
  4. DRIFT         against a snapshot from the previous render pass: every
                   sentence removed since, and every slide whose word count
                   collapsed. Removals are legal only when the copy record
                   removed them too.
  5. UNAUTHORED    rendered prose that traces to no authored string.
  6. NUMBERS       every numeral on a slide traces to claims.json.
  7. OPENERS       a slide body that opens on a bare demonstrative or pronoun
                   is a dangling reference once the deck gets reordered (WARN).

Usage:
  # after every render pass, including every fix pass
  python scripts/coherence_check.py --render-dir out/<date>/render \\
      --copy out/<date>/copy.json --contract out/<date>/coherence.json \\
      --claims out/<date>/claims.json --baseline out/<date>/coherence_snapshot.json

  # write the snapshot the NEXT pass will diff against
  python scripts/coherence_check.py ... --snapshot out/<date>/coherence_snapshot.json

Exit codes: 0 pass (warnings allowed), 1 any FAIL.
Writes <render-dir>/coherence_check.json
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# CASE_CRAFT grammar. The three that can never be cut are enforced here so a
# late trim cannot quietly drop the slides that make this a case file.
ROLES = ["COVER", "THE COMPANY", "THE BOTTLENECK", "THE BUILD", "THE RECEIPTS",
         "WHAT IT TOOK", "YOUR VERSION", "CLOSE"]
REQUIRED_ROLES = ["THE RECEIPTS", "WHAT IT TOOK", "YOUR VERSION"]

BODY_MIN_WORDS = 12
DRIFT_WORD_DROP = 0.25          # a slide losing this share of its words
OPENERS = {"this", "that", "these", "those", "it", "they", "them", "there",
           "such", "both", "either", "which"}


def norm(s):
    """Collapse to a comparable form: fold case, strip accents and punctuation
    variants, squeeze whitespace. Rendered text loses soft hyphens and gains
    line-break joins, so a raw equality test false-fails constantly."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"[\s­]+", " ", s)
    return re.sub(r"[^a-z0-9'\" .,%$/-]+", " ", s.lower()).strip()


def squash(s):
    """norm() with every space removed. Rendered slides join lines without a
    space ('a visit.The study'), so containment must ignore spacing entirely."""
    return re.sub(r"[^a-z0-9%$./-]", "", norm(s))


def sentences(s):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", (s or "").strip()) if x.strip()]


def slide_text(rec):
    """Non-decorative rendered text on a slide, in DOM order, deduped by
    containment. Decorative furniture (crop marks, axis ticks, scale numerals)
    is outside the copy record's authority and is excluded here so it neither
    reads as unauthored prose nor as an untraceable number."""
    out = []
    for n in rec.get("text_nodes", []):
        if n.get("decorative"):
            continue
        t = (n.get("text") or "").strip()
        if t and not any(squash(t) and squash(t) in squash(o) for o in out):
            out.append(t)
    return out


def numerals(s):
    return {m.rstrip(",.") for m in
            re.findall(r"\d[\d,]*(?:\.\d+)?", s or "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render-dir", required=True)
    ap.add_argument("--copy", required=True)
    ap.add_argument("--contract")
    ap.add_argument("--claims")
    ap.add_argument("--baseline")
    ap.add_argument("--snapshot")
    args = ap.parse_args()

    rdir = Path(args.render_dir)
    report = json.loads((rdir / "render_report.json").read_text())
    copy = json.loads(Path(args.copy).read_text())
    out = {"fails": [], "warns": [], "slides": []}

    authored = {}
    for s in (copy.get("slides") or []):
        authored[int(s["n"])] = s
    if not authored:
        out["fails"].append(
            "copy.json declares no per-slide strings — the copy record is the story of "
            "record and slide code renders it; without it nothing downstream is checkable")

    rendered = {}
    for i, rec in enumerate(report["slides"], start=1):
        rendered[i] = {"file": rec["file"], "text": slide_text(rec)}

    # ---- 1. contract ----------------------------------------------------
    contract = None
    if args.contract and Path(args.contract).exists():
        contract = json.loads(Path(args.contract).read_text())
        if not (contract.get("thesis") or "").strip():
            out["fails"].append("coherence.json declares no thesis")
        elif len(sentences(contract["thesis"])) > 1:
            out["fails"].append("thesis must be ONE sentence the whole deck argues")
        cslides = {int(c["n"]): c for c in (contract.get("slides") or [])}
        if set(cslides) != set(rendered):
            out["fails"].append(
                f"contract covers slides {sorted(cslides)} but the deck has {sorted(rendered)}")
        roles = [(c.get("role") or "").upper() for c in cslides.values()]
        for r in REQUIRED_ROLES:
            if r not in roles:
                out["fails"].append(f"required slide role {r} is missing from the deck")
        for n, c in sorted(cslides.items()):
            role = (c.get("role") or "").upper()
            if role and role not in ROLES:
                out["warns"].append(f"slide {n} role '{c.get('role')}' is outside the grammar")
            pays = c.get("pays")
            if n > 1 and pays is None:
                out["fails"].append(
                    f"slide {n} pays off nothing — every slide after the cover answers "
                    "something an earlier slide opened")
            elif pays is not None and not (1 <= int(pays) < n):
                out["fails"].append(f"slide {n} pays off slide {pays}, which is not earlier")
            if n < max(cslides) and not (c.get("promise") or "").strip():
                out["fails"].append(
                    f"slide {n} opens no loop — it gives the reader no reason to swipe")
        for n in sorted(cslides):
            if n == max(cslides) or not (cslides[n].get("promise") or "").strip():
                continue
            if not any(int(c.get("pays") or 0) == n for m, c in cslides.items() if m > n):
                out["fails"].append(
                    f"slide {n} opens a loop no later slide closes: "
                    f"'{cslides[n]['promise'][:70]}'")
    elif args.contract:
        out["fails"].append(f"coherence contract not found: {args.contract}")

    # ---- 2/3/5/6/7. per-slide -------------------------------------------
    claim_nums = set()
    if args.claims and Path(args.claims).exists():
        claim_nums = numerals(Path(args.claims).read_text())

    for n, r in sorted(rendered.items()):
        srec = {"n": n, "file": r["file"], "fails": [], "warns": []}
        joined = " ".join(r["text"])
        blob = squash(joined)
        a = authored.get(n)
        if a:
            fields = [("kicker", a.get("kicker")), ("headline", a.get("headline")),
                      ("body", a.get("body"))]
            fields += [("label", x) for x in (a.get("labels") or [])]
            fields += [("source", x) for x in (a.get("source_labels") or [])]
            for kind, val in fields:
                if not val:
                    continue
                for sent in sentences(val) or [val]:
                    if squash(sent) and squash(sent) not in blob:
                        srec["fails"].append(
                            f"authored {kind} missing from the render: '{sent[:70]}'")
            body = (a.get("body") or "").strip()
            authored_words = sum(len(str(v).split()) for _, v in fields if v)
            rendered_words = len(joined.split())
            if authored_words >= BODY_MIN_WORDS and rendered_words < authored_words * 0.6:
                srec["fails"].append(
                    f"copy record authors {authored_words} words for this slide; "
                    f"{rendered_words} rendered — copy was cut to make room for layout "
                    "instead of the layout being fixed")
            # unauthored prose
            auth_blob = squash(" ".join(str(v) for _, v in fields if v))
            for t in r["text"]:
                if len(t.split()) >= 8 and squash(t) not in auth_blob:
                    srec["warns"].append(f"unauthored prose on the slide: '{t[:70]}'")
        elif authored:
            srec["fails"].append("no entry in copy.json.slides for this slide")

        if claim_nums:
            for num in numerals(joined):
                if num not in claim_nums and len(num) > 1 and num not in {str(n), f"{n:02d}"}:
                    srec["warns"].append(
                        f"numeral {num} on the slide traces to no claim in claims.json")

        if a and (a.get("body") or "").strip():
            first = norm(a["body"]).split()
            if first and first[0].strip(".,") in OPENERS:
                srec["warns"].append(
                    f"body opens on a bare '{first[0]}' — a dangling reference the moment "
                    "the deck is reordered; name the thing")

        out["slides"].append(srec)
        out["fails"] += [f"slide {n}: {x}" for x in srec["fails"]]
        out["warns"] += [f"slide {n}: {x}" for x in srec["warns"]]

    # ---- 4. drift against the previous pass ------------------------------
    snap = {str(n): {"text": r["text"], "words": len(" ".join(r["text"]).split())}
            for n, r in rendered.items()}
    if args.baseline and Path(args.baseline).exists():
        base = json.loads(Path(args.baseline).read_text())
        authored_blob = squash(json.dumps(copy.get("slides") or []))
        for k, prev in base.items():
            cur = snap.get(k)
            if not cur:
                out["fails"].append(f"slide {k} existed last pass and is gone now")
                continue
            curblob = squash(" ".join(cur["text"]))
            for t in prev["text"]:
                for sent in sentences(t):
                    sq = squash(sent)
                    if len(sent.split()) >= 5 and sq and sq not in curblob:
                        lvl = out["warns"] if sq not in authored_blob else out["fails"]
                        lvl.append(
                            f"slide {k}: sentence removed since the last pass "
                            f"{'(and it is still in the copy record)' if sq in authored_blob else '(also removed from the copy record)'}"
                            f": '{sent[:70]}'")
            if prev["words"] and cur["words"] < prev["words"] * (1 - DRIFT_WORD_DROP):
                out["warns"].append(
                    f"slide {k}: word count fell {prev['words']} -> {cur['words']} in one pass")

    if args.snapshot:
        Path(args.snapshot).write_text(json.dumps(snap, indent=1))

    out["verdict"] = "FAIL" if out["fails"] else ("WARN" if out["warns"] else "PASS")
    (rdir / "coherence_check.json").write_text(json.dumps(out, indent=2))
    for f in out["fails"]:
        print(f"FAIL: {f}")
    for w in out["warns"][:40]:
        print(f"warn: {w}")
    print(f"verdict: {out['verdict']}  fails={len(out['fails'])} warns={len(out['warns'])}"
          f"  (report -> {rdir / 'coherence_check.json'})")
    sys.exit(1 if out["fails"] else 0)


if __name__ == "__main__":
    main()

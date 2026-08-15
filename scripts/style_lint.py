#!/usr/bin/env python3
"""style_lint.py — pre-flight house-style lint for authored copy and rendered slides.

Purpose: the SHIP-time gate in scripts/site_build.py (`prose_colon_gate`)
refuses prose colons on every emitted page, because house style bans them
(clock times like 4:30 and URLs are exempt, they are not prose). That gate is
correct and must never weaken, but it only fires at ship, AFTER the docket
note (Phase 3.5) and copy.json (Phase 6) are written -- so runs 2026-07-09 and
2026-07-10 each tripped it TWICE and had to rephrase under ship-time pressure
(a docket history note, then copy.json's first_comment lead line). This helper
runs the SAME rule EARLY, where the text is authored, so the fix happens before
ship. It moves the catch earlier; it does not replace or loosen the gate.

The colon transform below is a byte-for-byte replica of
site_build.prose_colon_gate (strip script/style, tags -> newlines, drop URLs
and clock times, then any remaining ':' on a line is a violation). Keep the two
in sync; if site_build's rule changes, mirror it here.

SECOND RULE, added 2026-08-15: banned glyphs. config/brand.yaml
on_slide_text_rules says "No em dashes or en dashes in ANY on-slide string. Zero
exceptions." and "Straight quotes." caption_check.py has enforced exactly that on
the CAPTION since 2026-07-21, but nothing enforced it on the SLIDES or on
copy.json, so the 2026-08-15 deck carried mixed straight and curly apostrophes
until a pixel critic caught them by eye. Eyes are not a gate. The glyph list here
is deliberately identical to caption_check.BANNED_PUNCT minus the semicolon
(semicolons are banned in post copy, not on slides).

THIRD MODE, same date: --render-dir lints the RENDERED text nodes out of
render_report.json rather than the HTML source, so an entity (&rsquo;) or an
escape (\\u2019) is caught in the form the reader actually sees.

Usage:
  echo "Sources for today's deck:" | python scripts/style_lint.py
  python scripts/style_lint.py --file out/<date>/docket_note.txt
  python scripts/style_lint.py --file out/<date>/copy.json --json-field first_comment
  python scripts/style_lint.py --file copy.json --json-field .   # lint every string
  python scripts/style_lint.py --render-dir out/<date>/render    # every on-slide string

Exit 0 = clean, 1 = at least one violation (offending lines printed to stderr),
2 = usage error.
"""
import argparse
import json
import re
import sys
from pathlib import Path

# Mirrors caption_check.BANNED_PUNCT minus ';' (a post-copy rule, not a slide rule).
BANNED_GLYPHS = {"—": "em dash", "–": "en dash",
                 "“": "curly quote", "”": "curly quote",
                 "‘": "curly apostrophe", "’": "curly apostrophe"}


def glyph_violations(text):
    """Return [(glyph_name, offending_excerpt)] for every banned glyph present."""
    out = []
    for i, ch in enumerate(text):
        name = BANNED_GLYPHS.get(ch)
        if name:
            out.append((name, text[max(0, i - 30):i + 30].replace("\n", " ").strip()))
    return out


def colon_violations(text):
    """Return the list of offending (stripped) lines, replicating exactly
    scripts/site_build.py::prose_colon_gate."""
    txt = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", text)
    txt = re.sub(r"<[^>]+>", "\n", txt)
    txt = re.sub(r"https?://\S+", " ", txt)
    txt = re.sub(r"\d{1,2}:\d{2}", " ", txt)
    return [line.strip() for line in txt.split("\n") if ":" in line]


def collect_strings(node):
    """Yield every string in a JSON subtree (field values, list items, nested)."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from collect_strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from collect_strings(v)


def navigate(obj, dotpath):
    if dotpath in ("", "."):
        return obj
    cur = obj
    for key in dotpath.strip(".").split("."):
        if not isinstance(cur, dict) or key not in cur:
            print(f"FAIL: --json-field {dotpath!r}: no key {key!r}", file=sys.stderr)
            sys.exit(2)
        cur = cur[key]
    return cur


def lint_render_dir(render_dir):
    """Lint every rendered on-slide string. Exits; never returns."""
    report = Path(render_dir) / "render_report.json"
    if not report.exists():
        print(f"FAIL: no render_report.json in {render_dir}", file=sys.stderr)
        sys.exit(2)
    doc = json.loads(report.read_text(encoding="utf-8"))
    bad, nodes = [], 0
    for slide in doc.get("slides", []):
        name = slide.get("file", "?")
        for node in slide.get("text_nodes", []):
            text = node.get("text") or ""
            if not text.strip():
                continue
            nodes += 1
            for glyph_name, excerpt in glyph_violations(text):
                bad.append(f"{name}: {glyph_name} in {excerpt[:70]!r}")
            for line in colon_violations(text):
                bad.append(f"{name}: prose colon in {line[:70]!r}")
    if bad:
        for line in bad:
            print(f"FAIL: {line}", file=sys.stderr)
        print(f"{len(bad)} on-slide house-style violation(s) across {nodes} text nodes "
              f"(brand.yaml on_slide_text_rules). Fix the slide source, not the report.",
              file=sys.stderr)
        sys.exit(1)
    print(f"style_lint: clean ({nodes} on-slide text nodes, no banned glyphs, no colons)")
    sys.exit(0)


def main():
    ap = argparse.ArgumentParser(
        description="pre-flight house-style lint (prose colons + banned glyphs)")
    ap.add_argument("--file", help="text or .json file to lint; omit to read stdin")
    ap.add_argument("--json-field", help="dot-path into a .json file; '.' lints every string")
    ap.add_argument("--render-dir",
                    help="lint every rendered on-slide text node in <dir>/render_report.json")
    args = ap.parse_args()

    if args.render_dir:
        return lint_render_dir(args.render_dir)

    strings = []
    if args.json_field is not None:
        if not args.file:
            print("FAIL: --json-field requires --file <json>", file=sys.stderr)
            sys.exit(2)
        obj = json.loads(open(args.file, encoding="utf-8").read())
        strings = list(collect_strings(navigate(obj, args.json_field)))
    elif args.file:
        strings = [open(args.file, encoding="utf-8").read()]
    else:
        strings = [sys.stdin.read()]

    colons, glyphs = [], []
    for s in strings:
        colons.extend(colon_violations(s))
        glyphs.extend(glyph_violations(s))
    if colons or glyphs:
        for line in colons:
            print(f"FAIL: prose colon in {line[:80]!r}", file=sys.stderr)
        for name, excerpt in glyphs:
            print(f"FAIL: {name} in {excerpt[:80]!r}", file=sys.stderr)
        print(f"{len(colons)} prose-colon and {len(glyphs)} banned-glyph violation(s); "
              f"fix before ship (brand.yaml on_slide_text_rules, and site_build's "
              f"ship gate will otherwise block the colons).", file=sys.stderr)
        sys.exit(1)
    print("style_lint: clean (no prose colons, no banned glyphs)")
    sys.exit(0)


if __name__ == "__main__":
    main()

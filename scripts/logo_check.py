#!/usr/bin/env python3
"""logo_check.py — objective gate, the brand logo must appear in every deck.

Maintainer rule (2026-07-21): every carousel this routine ships carries the
Alaska Ai logo somewhere in the deck, default the close slide brand row.
This gate makes the rule machine-enforced, it scans the slide HTML for a
reference to the configured logo asset and fails the deck when none exists
or when the asset file itself is missing.

  python scripts/logo_check.py --slides-dir out/<date>/slides
Exit 0 = at least one slide references the logo and the asset exists.
Exit 1 = FAIL (no reference, or asset missing).
"""
import argparse
import re
import sys
from pathlib import Path

DEFAULT_ASSET = "assets/alaskaaipic.png"


def configured_asset(repo_root: Path) -> str:
    brand = repo_root / "config" / "brand.yaml"
    if brand.exists():
        m = re.search(r'logo_asset:\s*"([^"]+)"', brand.read_text())
        if m:
            return m.group(1)
    return DEFAULT_ASSET


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slides-dir", required=True)
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args()

    root = Path(args.repo_root)
    asset_rel = configured_asset(root)
    asset = root / asset_rel
    basename = Path(asset_rel).name

    if not asset.exists():
        print(f"FAIL: logo asset {asset_rel} does not exist in the repo", file=sys.stderr)
        sys.exit(1)

    slides = sorted(Path(args.slides_dir).glob("slide-*.html"))
    if not slides:
        print(f"FAIL: no slides found under {args.slides_dir}", file=sys.stderr)
        sys.exit(1)

    carriers = [s.name for s in slides if basename in s.read_text()]
    if not carriers:
        print(f"FAIL: no slide references {basename}. The logo must appear in "
              f"every deck (default, the close slide brand row).", file=sys.stderr)
        sys.exit(1)

    print(f"PASS: logo {basename} referenced by {', '.join(carriers)} "
          f"({len(slides)} slides scanned)")


if __name__ == "__main__":
    main()

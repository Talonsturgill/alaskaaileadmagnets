#!/usr/bin/env python3
"""fetch_pdf_text.py, open a PDF from the web and read it as text.

Why this exists. Conference decks are the only venue the 2026-08-08 restock
found that carried a real itemised cost slide (Peckham Industries, AGC Tech
Con, roughly $3,000/yr). Those decks are PDFs, and in this sandbox a scout has
no way to read one:

  * WebFetch on a .pdf returns raw binary and silently drops the file into the
    tool-results directory
  * `Read` cannot rasterise it, because poppler / pdftoppm is not installed
  * `r.jina.ai` works but has a hard quota and starts returning 401 after a
    handful of calls, then recovers minutes later

pypdf IS installed (it is a bootstrap dependency for the vector PDF path), so
this script closes the gap with zero new runtime dependencies.

Usage
-----
  python3 scripts/fetch_pdf_text.py <url>
  python3 scripts/fetch_pdf_text.py <url> --money
  python3 scripts/fetch_pdf_text.py <url> --pages 1-12 --out out/deck.txt
  python3 scripts/fetch_pdf_text.py --local path/to/file.pdf --money

  --money   print ONLY lines carrying a dollar amount or a duration. This is
            the hard intake gate (cost AND decision-to-working timeline) run
            as a single command against a deck. Use it first. If it prints
            nothing, the deck does not close the gate and you move on.
  --pages   1-based inclusive range, e.g. 3-9 or 12.
  --out     also write the extracted text to a file.

Exit codes
----------
  0  text extracted
  3  fetched fine but the PDF has NO text layer (an image-only export).
     That is a dead end, not a retry. Do not burn budget re-fetching it.
  4  the URL did not return a PDF (403 / 404 / HTML wall).
  5  --money found no dollar amount and no duration in the document.

Nothing here posts, writes to the network beyond a GET, or touches ledger
state. It is a read tool.
"""

from __future__ import annotations

import argparse
import io
import re
import sys

MONEY = re.compile(
    r"""(
        \$\s?\d[\d,]*(?:\.\d+)?(?:\s?[KkMm]\b|\s?(?:million|billion|thousand))?
      | \b\d[\d,]*(?:\.\d+)?\s?(?:dollars|USD|EUR|euros)\b
      | \b(?:USD|EUR)\s?\d[\d,]*
    )""",
    re.VERBOSE,
)

DURATION = re.compile(
    r"""\b(
        (?:\d+|a|an|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)
        [\s-]*(?:to|-|through)?[\s-]*(?:\d+)?[\s-]*
        (?:minute|hour|day|week|weekend|month|quarter|year)s?
      | (?:same|next)[\s-]day
      | overnight
      | go[\s-]?live
      | went[\s-]live
      | (?:in|within|over|after|took)\s+(?:about\s+)?\d+\s+
        (?:minute|hour|day|week|month|year)s?
    )\b""",
    re.VERBOSE | re.IGNORECASE,
)

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)


def parse_pages(spec: str, total: int) -> list[int]:
    if not spec:
        return list(range(total))
    out: list[int] = []
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            lo, hi = chunk.split("-", 1)
            out.extend(range(int(lo) - 1, min(int(hi), total)))
        else:
            out.append(int(chunk) - 1)
    return [p for p in out if 0 <= p < total]


def get_bytes(url: str, timeout: int) -> tuple[bytes, str]:
    import requests  # stdlib-adjacent, already present for the engine

    resp = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": UA, "Accept": "application/pdf,*/*"},
        allow_redirects=True,
    )
    return resp.content, f"HTTP {resp.status_code} {resp.headers.get('content-type', '?')}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="URL of the PDF")
    ap.add_argument("--local", help="read a PDF already on disk instead of fetching")
    ap.add_argument("--pages", default="", help="1-based page range, e.g. 3-9")
    ap.add_argument("--money", action="store_true", help="print only lines with a dollar amount or a duration")
    ap.add_argument("--out", help="also write extracted text here")
    ap.add_argument("--timeout", type=int, default=60)
    args = ap.parse_args()

    if not args.url and not args.local:
        ap.error("give a URL or --local")

    if args.local:
        with open(args.local, "rb") as fh:
            raw = fh.read()
        where = args.local
        status = "local file"
    else:
        try:
            raw, status = get_bytes(args.url, args.timeout)
        except Exception as exc:  # noqa: BLE001
            print(f"FETCH FAILED  {args.url}\n  {type(exc).__name__}: {exc}", file=sys.stderr)
            return 4
        where = args.url

    if not raw[:5].startswith(b"%PDF"):
        head = raw[:200].decode("utf-8", "replace").replace("\n", " ")
        print(
            f"NOT A PDF  {where}\n  {status}\n  first bytes: {head}\n"
            "  A wall or a redirect to HTML. Do not retry the same URL.",
            file=sys.stderr,
        )
        return 4

    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(raw))
    total = len(reader.pages)
    wanted = parse_pages(args.pages, total)

    chunks: list[str] = []
    for i in wanted:
        try:
            text = reader.pages[i].extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            text = f"[page {i + 1} extraction error: {type(exc).__name__}]"
        chunks.append(f"\n===== page {i + 1} of {total} =====\n{text.strip()}")

    body = "\n".join(chunks)
    stripped = re.sub(r"=====.*?=====", "", body).strip()

    if len(stripped) < 40:
        print(
            f"IMAGE-ONLY PDF  {where}\n  {total} pages, no text layer.\n"
            "  poppler is not installed, so there is no OCR path here.\n"
            "  DEAD END, not a retry. Move to the next deck.",
            file=sys.stderr,
        )
        return 3

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(body)

    if args.money:
        hits: list[str] = []
        page = "?"
        for line in body.splitlines():
            m = re.match(r"===== page (\d+) of", line)
            if m:
                page = m.group(1)
                continue
            s = line.strip()
            if not s:
                continue
            if MONEY.search(s) or DURATION.search(s):
                hits.append(f"p{page}: {s}")
        print(f"# {where}\n# {total} pages, {len(hits)} lines carrying a dollar amount or a duration\n")
        for h in hits:
            print(h)
        if not hits:
            print(
                "NO COST AND NO TIMELINE IN THIS DECK. The hard gate does not close here.",
                file=sys.stderr,
            )
            return 5
        return 0

    print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())

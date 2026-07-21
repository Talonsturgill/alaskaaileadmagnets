#!/usr/bin/env python3
"""gmail_draft.py — builds the Case Files delivery email payload.

Reads the run artifacts and emits {subject, to, html_body} JSON for the
Gmail MCP create_draft tool. The email body this script emits is the email
body, VERBATIM — the routine never hand-composes or restyles it.

Contract:
- POST block carries ONLY the caption (it is the paste target). This script
  hard-fails if a URL or a sources line leaked into it.
- FIRST-COMMENT block is plain text with full raw URLs visible.
- All artifact links are COMMIT-PINNED via --raw-base (an immutable
  raw.githubusercontent.com/<owner>/<repo>/<sha> base), so delivery never
  depends on a merge.

  python scripts/gmail_draft.py --run-dir out/<date> --run-date <date> \
      --case-no N --raw-base https://raw.githubusercontent.com/o/r/<sha> \
      --branch claude/case-file-<date> --payload-out out/<date>/gmail_payload.json
"""
import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path

URLISH = re.compile(r"https?://|www\.", re.I)


def die(msg):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def load_json(path, required=False):
    p = Path(path)
    if not p.exists():
        if required:
            die(f"missing required artifact {p}")
        return None
    return json.loads(p.read_text())


def esc(s):
    return html.escape(s or "", quote=False)


def pre_block(text):
    return (f'<pre style="white-space:pre-wrap;font-family:Menlo,Consolas,monospace;'
            f'font-size:13px;background:#f5f7fa;border:1px solid #d8dee8;'
            f'border-radius:6px;padding:14px;margin:6px 0 18px 0;">{esc(text)}</pre>')


def section(title, body):
    return (f'<h2 style="font-family:Georgia,serif;font-size:17px;margin:26px 0 6px 0;'
            f'color:#0E2138;">{esc(title)}</h2>{body}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--run-date", required=True)
    ap.add_argument("--case-no", required=True, type=int)
    ap.add_argument("--raw-base", required=True,
                    help="commit-pinned raw base, .../<owner>/<repo>/<sha>")
    ap.add_argument("--branch", required=True)
    ap.add_argument("--payload-out", required=True)
    ap.add_argument("--to", default="me")
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args()

    run = Path(args.run_dir)
    root = Path(args.repo_root)
    copy = load_json(run / "copy.json", required=True)
    score = load_json(run / "score_report.json")
    honesty = load_json(run / "honesty_report.json")
    assemble = load_json(run / "final" / "assemble_report.json") or load_json(run / "assemble_report.json")
    bank = load_json(root / "ledger" / "bank.json")
    upgrades = load_json(root / "ledger" / "upgrades.json")

    post = copy.get("post_copy") or die("copy.json has no post_copy")
    first_comment = copy.get("first_comment") or die("copy.json has no first_comment")
    title = copy.get("document_title") or die("copy.json has no document_title")
    aftercare = copy.get("aftercare") or []

    # The paste contract: nothing linkish and no sources block in the post.
    if URLISH.search(post):
        die("post_copy contains a URL; sources belong in the first comment only")
    if re.search(r"^\s*sources\b", post, re.I | re.M):
        die("post_copy contains a sources block; move it to the first comment")

    renders = sorted((run / "render").glob("slide-*.png"))
    if not renders:
        die(f"no renders found under {run}/render")
    thumbs = sorted((run / "final" / "thumbs").glob("*-thumb.png"))

    date_path = f"runs/{args.run_date}"
    link = lambda rel: f"{args.raw_base}/{date_path}/{rel}"

    body = []
    body.append(
        f'<div style="font-family:Georgia,serif;font-size:15px;color:#1a2433;'
        f'max-width:680px;line-height:1.5;">'
        f'<h1 style="font-size:21px;margin:0 0 2px 0;color:#0E2138;">'
        f'Alaska.Ai — Case File No. {args.case_no}</h1>'
        f'<p style="margin:0 0 18px 0;color:#5b6b80;">{esc(args.run_date)} · '
        f'branch {esc(args.branch)} · links pinned to the pushed commit</p>')

    steps = (f"1. Download the PDF and post it as a LinkedIn document post.\n"
             f"2. Document title, {title}\n"
             f"3. Paste the POST block as the caption. Nothing else goes in the post.\n"
             f"4. Paste the FIRST COMMENT block as your first comment right after posting.")
    body.append(section("How to post this", pre_block(steps)))
    body.append(section("The PDF",
                        f'<p style="margin:6px 0 18px 0;"><a href="{link("carousel.pdf")}">carousel.pdf</a>'
                        f'{" · " + str(assemble.get("pdf_mb")) + " MB, " + esc(str(assemble.get("pdf_mode"))) + " text" if assemble else ""}</p>'))
    body.append(section("POST (paste as the caption, whole block)", pre_block(post)))
    body.append(section("FIRST COMMENT (paste right after posting)", pre_block(first_comment)))

    if thumbs:
        cells = []
        for t in thumbs:
            b64 = base64.b64encode(t.read_bytes()).decode()
            cells.append(f'<img src="data:image/png;base64,{b64}" width="150" '
                         f'style="margin:0 6px 6px 0;border:1px solid #d8dee8;border-radius:4px;"/>')
        body.append(section("Preview", f'<div>{"".join(cells)}</div>'))

    links = [f'<a href="{link("slide-%02d.png" % (i + 1))}">slide {i + 1:02d}</a>'
             for i in range(len(renders))]
    links.append(f'<a href="{link("contact_sheet.png")}">contact sheet</a>')
    body.append(section("Full-size artifacts", f'<p style="margin:6px 0 18px 0;">{" · ".join(links)}</p>'))

    if score:
        rows = "".join(
            f'<tr><td style="padding:3px 10px 3px 0;color:#5b6b80;">{esc(c.get("name", ""))}</td>'
            f'<td style="padding:3px 0;">{c.get("score", "")}</td></tr>'
            for c in score.get("criteria", []))
        verdict = "SHIP" if score.get("ship") else "BELOW THRESHOLD, read the notes"
        body.append(section(
            f'Report card — {score.get("weighted_total", "?")} / threshold {score.get("threshold", "?")} — {verdict}',
            f'<table style="font-size:13px;border-collapse:collapse;margin:0 0 6px 0;">{rows}</table>'
            f'<p style="margin:4px 0 18px 0;color:#5b6b80;">{esc(score.get("editor_notes_for_email", ""))}</p>'))

    if honesty:
        hr = honesty.get("hostile_reply_test", {})
        body.append(section("Honesty gate",
                            f'<p style="margin:6px 0 18px 0;">Verdict {esc(honesty.get("verdict", "?"))}. '
                            f'Weakest sentence under a hostile reply, "{esc(hr.get("weakest_sentence", ""))}" '
                            f'(survives, {hr.get("survives", "?")}).</p>'))

    if bank:
        ready = [c for c in bank.get("cases", [])
                 if c.get("status") in ("candidate", "verified")
                 and c.get("evidence_strength") in ("strong", "medium")]
        body.append(section("Bank health",
                            f'<p style="margin:6px 0 18px 0;">{len(ready)} ship-ready cases in the bank.</p>'))

    ups = [u for u in (upgrades or {}).get("entries", []) if u.get("run_date") == args.run_date]
    if ups:
        items = "".join(f'<li>{esc(u.get("kind", ""))} · {esc(u.get("area", ""))} · {esc(u.get("change", ""))}</li>'
                        for u in ups)
        body.append(section("Automation changes this run", f'<ul style="margin:6px 0 18px 18px;">{items}</ul>'))
    else:
        body.append(section("Automation changes this run",
                            '<p style="margin:6px 0 18px 0;">No changes.</p>'))

    if aftercare:
        body.append(section("Aftercare",
                            '<ul style="margin:6px 0 18px 18px;">' +
                            "".join(f"<li>{esc(a)}</li>" for a in aftercare) + "</ul>"))

    body.append("</div>")

    payload = {
        "subject": f"Alaska.Ai — Case File No. {args.case_no} — {args.run_date} — {title}",
        "to": args.to,
        "html_body": "".join(body),
    }
    out = Path(args.payload_out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2))
    print(f"payload -> {out}  (subject: {payload['subject']})")


if __name__ == "__main__":
    main()

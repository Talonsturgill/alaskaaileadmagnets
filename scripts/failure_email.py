#!/usr/bin/env python3
"""failure_email.py — builds the Gmail payload for a run that shipped nothing.

The failure protocol in prompts/routine_instructions.md requires a draft even
when no case can responsibly ship: subject "Alaska.Ai - Case Files run failed
- <date>", carrying the post-mortem and what exists. gmail_draft.py cannot be
used, because it hard-requires copy.json, renders and an assemble report, none
of which exist on a run that never reached Phase 6.

  python scripts/failure_email.py --run-date 2026-08-08 --case-no 2 \
      --raw-base https://raw.githubusercontent.com/o/r/<sha> \
      --branch <branch> --pr <url> --payload-out out/<date>/gmail_payload.json
"""
import argparse
import base64
import html
import json
from pathlib import Path


def esc(s):
    return html.escape(s or "", quote=False)


def h2(t):
    return (f'<h2 style="font-family:Georgia,serif;font-size:17px;'
            f'margin:26px 0 6px 0;color:#0E2138;">{esc(t)}</h2>')


def p(t):
    return f'<p style="margin:6px 0 12px 0;">{t}</p>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-date", required=True)
    ap.add_argument("--case-no", required=True, type=int)
    ap.add_argument("--raw-base", required=True)
    ap.add_argument("--branch", required=True)
    ap.add_argument("--pr", required=True)
    ap.add_argument("--payload-out", required=True)
    ap.add_argument("--to", default="docket@alaskaaihq.com")
    ap.add_argument("--repo-root", default=".")
    a = ap.parse_args()

    root = Path(a.repo_root)
    link = lambda rel: f"{a.raw_base}/runs/{a.run_date}/{rel}"

    logo_html = ""
    logo = root / "assets" / "alaskaaipic.png"
    if logo.exists():
        b64 = base64.b64encode(logo.read_bytes()).decode()
        logo_html = (f'<img src="data:image/png;base64,{b64}" width="54" '
                     f'style="border-radius:6px;vertical-align:middle;margin-right:12px;"/>')

    b = []
    b.append('<div style="font-family:Georgia,serif;font-size:15px;color:#1a2433;'
             'max-width:680px;line-height:1.55;">')
    b.append(f'<h1 style="font-size:21px;margin:0 0 2px 0;color:#0E2138;">'
             f'{logo_html}Alaska.Ai - Case Files run failed</h1>')
    b.append(f'<p style="margin:0 0 20px 0;color:#5b6b80;">{esc(a.run_date)} - '
             f'Case File No. {a.case_no} - branch {esc(a.branch)}</p>')

    b.append('<div style="background:#fff8e6;border-left:4px solid #FFC72C;'
             'padding:14px 16px;margin:0 0 20px 0;">'
             '<b>Nothing shipped, and there is no draft post today.</b><br>'
             'Ten scouts, three waves, roughly 250 queries and 85 pages read in '
             'full returned zero qualifying cases. Every single lead died on the '
             'same two facts, no disclosed cost and no disclosed timeline. The '
             'routine refused to lower the bar. Below is what it found instead, '
             'and it is worth reading, because one decision from you unblocks '
             'the next several runs.</div>')

    b.append(h2("The finding, in one paragraph"))
    b.append(p('<b>Cost is the payoff of a build-it-cheap talk.</b> The one real '
               'itemised price anyone found all day came from a family paving '
               'contractor presenting to a conference room, roughly $3,000 a year '
               'broken out line by line, and they disclosed it precisely because '
               'the punchline was "we built this ourselves and we are not data '
               'scientists". A company that <i>bought</i> from a vendor has an NDA '
               'or simply no reason to put the number on a slide. Our filter '
               'requires both a disclosed cost <i>and</i> a bought-not-built '
               'solution, and in published sources that intersection is close to '
               'empty. That is a structural property of what gets published, not '
               'a scouting failure, and it will reproduce every run until '
               'something changes.'))

    b.append(h2("The decision this puts in front of you"))
    b.append('<ol style="margin:6px 0 12px 20px;padding:0;">'
             '<li style="margin-bottom:10px;"><b>Grant the scout agent shell '
             'access.</b> The cheapest and highest-leverage item. The retro '
             'measured that <b>six hosts this run wrote off as blocked are '
             'blocked to our fetcher only</b> - a plain browser request returns '
             '200 from achrnews.com, mcaa.org, cfma.org, mmh.com, '
             'constructionexec.com and abc.org. Wave 1 called losing achrnews '
             '"severe"; half of that was a tool artefact. The fetcher is built '
             'and parked, because giving an agent a shell is your call, not '
             'the routine\'s.</li>'
             '<li style="margin-bottom:10px;"><b>Fund one phone call.</b> Four '
             'leads are missing only the price and have a named executive '
             'already talking publicly about the deployment. Any one call '
             'converts a lead into a shippable case.</li>'
             '<li style="margin-bottom:10px;"><b>Or split the hard gate.</b> Keep '
             'cost-and-timeline for a full case file, but allow a second, '
             'clearly labelled format where the price genuinely is not public and '
             'we say so out loud. That would have shipped four times today. It is '
             'a doctrine change and it is yours to make, not the routine\'s.</li>'
             '</ol>')

    b.append(h2("What the run banked instead"))
    b.append('<ul style="margin:6px 0 12px 20px;padding:0;">'
             '<li>Eight fully formed leads in the bank (bank-017 to bank-024), '
             'each naming exactly which filter parts hold and exactly what is '
             'missing</li>'
             '<li>Two new open venues: <b>64 downloadable contractor decks</b> at '
             'necaconvention.org, about 50 of them unwalked, plus the AGC archive</li>'
             '<li>A tool that reads those decks. <code>fetch_pdf_text.py --money</code> '
             'runs the cost-and-timeline gate against a deck in one command, '
             'verified live against a NECA deck</li>'
             '<li>Dead craft retired: searching for cost phrases now returns only '
             'AI-pricing SEO farms. Four scouts proved it; the instruction telling '
             'them to do it has been rewritten</li>'
             '<li>Five kills worth remembering, including a vendor stat card that '
             'would have inflated a baseline about 2x, and a case study that is '
             'almost certainly synthetic</li></ul>')

    b.append(h2("Read the full write-ups"))
    b.append(p(f'<a href="{link("postmortem.md")}">post-mortem</a> (the argument, '
               f'and the three options) &middot; '
               f'<a href="{link("automation_retro.md")}">automation retro</a> '
               f'(what changed in the machine and how it was verified) &middot; '
               f'<a href="{link("restock_notes.md")}">restock notes</a> (the full '
               f'access map) &middot; <a href="{a.pr}">the PR</a>'))

    b.append(h2("Automation changes this run"))
    ups = json.loads((root / "ledger" / "upgrades.json").read_text())
    items = "".join(
        f'<li style="margin-bottom:6px;"><b>{esc(u.get("area",""))}</b> &middot; '
        f'{esc(str(u.get("change",""))[:260])}</li>'
        for u in ups.get("entries", []) if u.get("run_date") == a.run_date)
    b.append(f'<ul style="margin:6px 0 12px 20px;padding:0;">{items}</ul>'
             if items else p("No changes."))

    b.append(h2("Bank health"))
    bank = json.loads((root / "ledger" / "bank.json").read_text())
    ready = [c for c in bank.get("cases", [])
             if c.get("status") in ("candidate", "verified")]
    b.append(p(f'<b>{len(ready)} ship-ready</b> against a par of 8. '
               f'{len(bank.get("cases", []))} entries total, all leads. '
               f'The bank is the constraint, and stocking it is what the three '
               f'options above are about.'))

    b.append('<p style="margin:22px 0 0 0;color:#5b6b80;font-size:13px;">'
             'Nothing was published anywhere. This routine drafts and never posts.'
             '</p></div>')

    payload = {
        "subject": f"Alaska.Ai - Case Files run failed - {a.run_date}",
        "to": a.to,
        "html_body": "".join(b),
    }
    out = Path(a.payload_out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2))
    print(f"payload -> {out}  (subject: {payload['subject']})")


if __name__ == "__main__":
    main()

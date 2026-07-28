# Field Notes

Living lessons for the Case Files studio. Dated entries, newest first. The
retro phase appends, the wake phase reads.

## 2026-07-21b (Case File No. 1, the first live run)

- The fact-check killed the story's intended payoff (the camera did NOT
  keep the Redoubt count going) and the honest version was a better story.
  Bank intake must always mark proposal vs deployed, the case-scout
  definition requires it.
- The honesty gate caught the caption outrunning its own deck (the hook
  claimed more than c23 supports). The caption must never claim more than
  the most-hedged slide.
- DOM chips and labels collide with canvas data marks that QA cannot see.
  Plan canvas element rects IN the dossier next to the DOM budgets, and
  eyeball every art-zone chip against them. Parked as a future gate.
- The flow critic's forward-plant fix (one tease line at the predicted
  bail slide) is cheap and repeatable. Any keepable slide should plant the
  next slide.
- Agent deaths from infra blips are real, respawn-by-cause worked, check
  liveness via the task registry instead of waiting on notifications.
- The logo is now law and machine-enforced (logo_check.py), default home
  the close slide brand row, keep it at 66px or smaller until a higher
  resolution export exists.

## 2026-07-21 (pre launch, from the build session)

- Engine proof shipped, three slides rendered and QA green in this repo with
  the vendored engine, vector PDF at 1.96 MB. The pipeline works end to end
  before the first real run.
- QA caught exactly the defect classes the sibling studio's ledger predicted,
  a hand sized hook wrapping into the block below, a bottom anchored note
  colliding with a stat stack, unmarked micro text. All three are now
  instincts (ledger/instincts.json i-001 to i-003).
- The evidence base (research/EVIDENCE.md) says documents and carousels are
  the top organic LinkedIn format in 2025 to 2026 on both pages and profiles,
  personal profiles carry roughly 2x page reach, links in body suppress
  reach, and comment gated lead magnets increasingly read as bait. The
  series' mechanics are built on those findings, revisit quarterly.
- The case bank's weakest coverage is aviation and Alaska specific private
  company stories. The standing fix is the interview lead (Saltwater Inc,
  Anchorage) and the Phase 1 restock hunting bizjournals and NIST MEP for
  named mid market operators.
- Voice discipline note for case posts, the vendor label reads cleanest as a
  plain attribution mid sentence, "per Samsara's case study, insurance costs
  fell 36 percent," which satisfies the honesty rule without a footnote.

## 2026-07-28 — the Gmail account was repointed

The Gmail connector on this account now authenticates as
**docket@alaskaaihq.com**, a Google Workspace mailbox on our own domain,
replacing the personal Gmail it used before. This is account level, so it
applies to every run from here.

What it means in practice:

- Drafts land in docket@alaskaaihq.com. That is the mailbox to check, not a
  personal inbox. It is freshly repointed, so it holds nothing from earlier
  runs and an empty history there means nothing at all. Never infer run state
  from mailbox contents; `runs/<date>/gmail_draft_id.txt` and the run PR are
  the record.
- Drafts are already from the right address, DKIM signed by alaskaaihq.com.
  **There is no From address to set and no send-as alias to configure.** Any
  step that changes the sender is obsolete, and following one now would be
  wrong.
- `scripts/gmail_draft.py --to` now defaults to the real address rather than
  the Gmail API's `me` shorthand, because the MCP `create_draft` tool rejects
  `me` with "At least one recipient must be specified". On 2026-07-25 that
  error was worked around by typing an address at the tool call, which is
  exactly the kind of hand substitution that goes stale. The payload is now
  correct as emitted and gets passed through unmodified.

Unchanged: this routine drafts and never sends.

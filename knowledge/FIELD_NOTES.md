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

## 2026-08-15 — Case File 002, The Wilson Companies

**The bank woke empty.** Sixteen entries, zero ship-ready, not one with a
disclosed cost. Two restock waves and seven scouts were needed before a case
existed. That is the single biggest schedule risk this routine carries and it
is structural, not an accident of lazy past runs.

**Every hunting ground carries exactly one half of what the filter needs, and
never the same half.** Trade press names the operator and omits the price.
Public record names the price and omits the deployment. Vendor libraries
describe the build and omit both. The one ground that delivered BOTH was an
operator-to-operator podcast, where peers disclose casually because the
audience would smell a dodge.

**Four scouts independently surfaced the same company and independently killed
it for the same reason.** CJB Industries' disclosed 300,000 dollars bought a
data historian and a quality system, and the actual AI was still in future
tense on a page updated April 2026. Convergent kills raise confidence. Read the
verbs, "expects to" is not a result.

**The runner-up died on the cost gate and there was no fallback.** Grand Island
Express was excellent on every other axis. The most cost-candid format in
trucking contains the words cost, price, paid and dollar exactly zero times.
The run proceeded on one case with no safety net, which was survivable this
time and should not be relied on again.

**The fact-checker killed the briefed hero numbers and the case got better.**
The operator refuses the AI attribution on his own headcount drop twice, naming
a compensation change. What survived is smaller and more copyable: the cut came
out of overnight and weekend coverage while his people still answer nine calls
in ten inside seven seconds. A confound volunteered by the person who did the
project is more credible than a clean number.

**The honesty gate earned its position before the art.** It caught a quantified
Anchorage weather claim ("eleven nights a year") that was our analysis wearing
the clothes of a fetched fact, in front of the one audience with personal
counter-evidence. That number was already hard-coded into the slide 8 art spec.
Had the gate run after the build, the fix would have been a retrofit.

**A gate that cannot see cannot judge.** render.py truncated every reported text
node to 80 characters, so coherence_check could not verify any authored sentence
longer than that and failed 58 fidelity checks on correct copy. Fixed to 600.
When a gate fails loudly on work you believe is right, suspect the gate's
instrument before you suspect the work.

**Layout yields to copy, and it costs something.** A pixel critic called slide
8's covered particle field the deck's worst craft defect and proposed opening a
full-bleed band. That would have meant deleting the honest limit, the rung 1
answer, or the Monday action. The copy stayed and the weaker art shipped,
recorded here rather than hidden.

# Launch Plan, the first 15 runs

Sequenced from the actual bank so the first three weeks cover the whole
Anchorage ICP map, obey the rotation rules from run one, and build trust
before asking for anything. The routine proposes, the maintainer disposes,
swap freely, the rotation gates will keep any order honest.

Launch order logic. Open with the local flag planted (fish), then the most
relatable Outside case (trucking), then prove range fast, and put the first
Reality Check inside week one so the honesty brand lands early.

| Run | Flavor | Case | Why here |
|----|--------|------|----------|
| 1 | Translation | SalmonVision and the counting weir (local flagship) | Plant the flag, the most Alaska story in the bank, engine proof already prototypes it |
| 2 | Case File | Fraley and Schilling, trucking (bank-001) | The most relatable everyday company win, sample already drafted |
| 3 | Case File | Hardie's Fresh Foods, route optimization (bank-002) | Boring optimization pays, rhymes with plow routes |
| 4 | Capability File | Fine tuning small models, Checkr + NOAA (bank-003, 016) | The model tuning explainer, ownership story, strong evidence |
| 5 | Case File | Verst Logistics, CV safety (bank-004) | Runs on cameras you already own, low lift entry |
| 6 | Reality Check | The 95 percent, and what the 5 percent do | The trust builder, base rates together, winner behaviors |
| 7 | Case File | Great Lakes Credit Union, voice service (bank-008) | Exact local size class, congressional testimony signal |
| 8 | Case File | BC Machining, predictive maintenance (bank-005) | Small shop, per machine arithmetic, lights out |
| 9 | Case File | Carbon Health, ambient documentation (bank-007) | Healthcare ROI where it actually lives |
| 10 | Capability File | RAG over your own documents, Gilbane + Rogers-O'Brien (bank-011, 010) | Strong numbers plus mid market size profile, size caveats said plainly |
| 11 | Case File | Peppermill Resort, voice operations (bank-009) | Tourism anchor, voice spaced three runs from run 7 |
| 12 | Translation | Plow route optimization, Indiana and Iowa to Anchorage | Winter city native, muni plow map is live local context |
| 13 | Case File | Afresh grocers, demand forecasting (bank-012) | Alaska freshness math, vendor aggregate labeled |
| 14 | Reality Check | Agent washing and the compounding error math | Kills the hype the audience is being sold right now |
| 15 | Case File | NY Power Authority, CV inspection (bank-013) | Railbelt rhyme, government sourced |

Held back deliberately. NEB Medical (bank-006) and Aire Serv (bank-014) are
weak evidence, they appear inside later capability files with explicit
vendor framing or after corroboration. Kvaroy (bank-015) rides a fisheries
capability file with the regulatory acceptance angle.

Rotation check against the gates. No company repeats. Industries never
repeat within any 3 run window. Voice capability appears at runs 7 and 11,
spaced. CV appears at 5 and 15 as safety then inspection, distinct
capability tags. Flavors run 4-ish case files per 6 runs with no two
non-case flavors adjacent.

## Phase 1.5, the compounding assets (after the series has legs)

- The case library page on alaskaaihq.com. Every shipped case file at a
  stable URL. Built by the site machinery in the carousels repo, which this
  routine never touches, wire it in a development session there.
- The Anchorage bottleneck map goes public once it holds 15 plus proven
  rows (knowledge/ALASKA_TRANSLATION.md grows it every run).
- The quarterly compiled playbook PDF, offered as a plain link, never
  comment gated.
- The Saltwater Inc interview, the first first-party Alaska case file.

## Phase 2, the video flagship

The week's best case as a 60 second Dispatch style video using the
alaska-ai-weekly machinery, weekly at most, only once the daily series is
proven. Not part of the initial build.

## Wiring the trigger (the one manual step)

At claude.ai/code/routines create a daily Routine on this repo:
- Prompt, the contents of prompts/ROUTINE_PROMPT.txt.
- Schedule, daily, a morning Alaska hour so drafts are ready before 8am
  posting windows.
- Connectors, Gmail (draft scope is enough, the routine only drafts). The
  connector authenticates as docket@alaskaaihq.com, a Workspace mailbox on
  our own domain. Drafts land there, and would send from there, DKIM signed
  by alaskaaihq.com. There is no send-as alias to configure and no From
  address to set.
- Network, standard web research access.
The first run creates a Gmail draft in docket@alaskaaihq.com titled
"Alaska.Ai — Case File No. 1 — <date> — <title>". Check that mailbox, not a
personal inbox. It is freshly repointed, so it holds no drafts from earlier
runs and an empty history there means nothing. Don't post a draft you
haven't read.

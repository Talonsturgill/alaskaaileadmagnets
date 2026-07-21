# Automation Blueprint (design rationale, superseded)

STATUS 2026-07-21. This blueprint was built the same session. The living
contract is prompts/routine_instructions.md, which refines the phase map
below (the honesty gate moved before the art build, delivery links became
commit-pinned, the merge policy lives in CLAUDE.md). Kept as the design
rationale, when the two disagree, the routine file wins.

The proposed daily routine for the lead magnet series. It adapts the proven
alaskaaicarousels studio architecture (14 phase showrunner, bounded subagents,
ledger enforced variety, machine QA plus taste critics, script built Gmail
draft) to an evergreen case study series instead of a news series. Nothing here
runs yet. This document exists so the build phase starts from a decision, not a
blank page.

## The one structural difference from the news carousel

News is perishable, case studies are evergreen. So this routine feeds from a
BANK instead of a news window. A bank refresh phase keeps verified cases
stocked, a selection phase picks by rotation rules, and the day's production
verifies and ships one case. Research amortizes across runs, the daily cost
stays low, and the series never has an empty news day problem.

## Deliverable per run

One Gmail draft for the maintainer containing, in paste ready blocks, the post
copy, the first comment source block, the document title, and links to the
rendered carousel PDF plus slide PNGs. The maintainer posts by hand on the
chosen surface. DRAFT, NEVER POST is law.

## Proposed phase map

- P0 WAKE. Bootstrap engine, read ledgers (cases shipped, artwork variety,
  instincts), compute case_file_no, derive variety constraints and variance
  dials, note seasonal Alaska context.
- P1 BANK REFRESH (bounded). If the bank holds fewer than 10 ship ready cases,
  spawn case-scout agents (one per hunting ground, trade press, government and
  academic writeups, business journals, vendor libraries with skepticism
  labels) to restock. Each candidate lands in the bank with sources, numbers,
  evidence strength, and a proposed Alaska translation. Skipped when the bank
  is full.
- P2 SELECTION. Pick the day's case by rotation rules from the ledger, company
  never repeats, industry differs from the last 3, capability differs from the
  last 3, evidence strength at least medium with 2 plus sources (or one
  primary). Record decision and runner up.
- P3 VERIFICATION. Fact-checker re-fetches every source of the chosen case
  fresh and returns claims.json, the only thing downstream may cite. A case
  that fails verification is killed in the bank with a reason and the runner up
  takes its place. Kill means not this case, never no post today.
- P3.5 TRANSLATION ROOM. The differentiator phase. A translator agent maps the
  verified case to Anchorage, which local industry twin it speaks to, what the
  equivalent build honestly looks like on the feasibility ladder (rules first,
  then retrieval, then a single call, then a workflow, agent last), what it
  roughly costs at mid-market scale, where the case does NOT translate, and the
  honest do-you-even-need-AI note. Output is the translation dossier with every
  claim either sourced or labeled as our assessment.
- P4 DIRECTORS ROOM. Three treatment-director agents with rotating lenses pitch
  the deck, showrunner synthesizes, then writes the full storyboard with per
  slide dossiers (copy verbatim with claim ids, layout, technique stack,
  acceptance checklist).
- P5 COPY CHAMBER. Copywriter drafts caption and slide copy corrections, then
  caption lint and style lint until PASS. Voice per config, no em or en dashes,
  no colons, no emojis, ends on a real question, sources only in the first
  comment block.
- P6 ART BUILD. Bespoke HTML slides against the carousel-engine contract
  (1080x1350, offline assets, seeded, text in DOM or SVG), render.py then qa.py
  until exit 0.
- P7 PIXEL REVIEW. Pixel-critic per 1 to 2 slides in parallel, apply fixes,
  re-render changed slides, then flow-critic on the sequence. Loop until ship
  verdicts.
- P8 FINAL ASSEMBLY. assemble.py, vector text PDF, contact sheet, thumbs,
  verify the assembly report.
- P9 SCORING AND HONESTY GATE. Scorer grades against the rubric. A case-critic
  (adapted from leadflow's study-critic) audits against the anti hype tables,
  vendor numbers labeled, ranges not hero numbers, failure stats cited together
  never alone, the translation's feasibility call defensible, nothing that
  reads as AI slop or marketer cheese. Default is reject, loop until it ships.
- P10 SHIP. Copy artifacts to runs/<date>/, append ledgers, branch, commit,
  push, PR. Merge policy is an open decision (siblings merge autonomously
  because the Gmail draft gates the POST, not the merge, same logic applies
  here once the routine is trusted).
- P11 AUTOMATION RETRO AND UPGRADE. Upgrade-engineer diffs the run against this
  spec, implements 0 to 3 bounded verified upgrades, logs to the upgrades
  ledger, separate commit.
- P12 GMAIL DRAFT. Script built body, verbatim, paste ready blocks (post copy,
  first comment sources, document title), inline previews, raw links, report
  card, the standing offer line per config. Draft only.
- P13 RETRO. Ledger appends (instincts, field notes), run summary, run_state
  complete.

## Ledgers (committed state, the memory between runs)

- ledger/cases.json. Every shipped case file, company, industry, capability,
  angle, evidence strength, sources, outcome notes. Enforces the rotation
  rules and the company never repeats rule.
- ledger/bank.json. The case bank itself, statuses fresh, verified, shipped,
  killed (with reason). Restocked by P1, consumed by P2.
- ledger/artwork.json. The variety engine, same schema and enforcement as the
  carousel sibling, no two decks visually alike.
- ledger/instincts.json. Confidence scored lessons injected into subagent
  prompts.
- ledger/upgrades.json. The automation change trail.

## Agents (bounded set, showrunner only spawning, no agent spawns agents)

Reused patterns from siblings, case-scout (per hunting ground), fact-checker,
treatment-director x3, copywriter, pixel-critic per 1 to 2 slides, flow-critic,
scorer, upgrade-engineer. New to this series, translator (the Alaska mapping
specialist) and case-critic (the honesty gate, carries the anti hype tables
and the feasibility ladder from the method knowledge).

## Knowledge base to port (public safe digests, written at build time)

- CASE_CRAFT.md, what makes a case file post land (adapted CAROUSEL_CRAFT plus
  the case story grammar, problem, mechanism, numbers, what it took, what would
  break, the Alaska translation).
- HONEST_AI.md, the public safe digest of the feasibility ladder, the anti hype
  tables, the compounding error math, capacity vs cash, ranges not hero
  numbers. Sourced from the same public research the private method files cite,
  never copied from the private repo's prospect work.
- ALASKA_TRANSLATION.md, the industry twin map, which Outside industries rhyme
  with which Anchorage segments, plus the local proof stories from
  research/ALASKA_GROUND.md.

## Engine and delivery

Copy the carousel-engine skill, fonts, and needed asset libraries into this
repo at build time so the sibling stays self contained, same pattern the
siblings use. Reuse the gmail_draft.py pattern with this repo's config. The
Gmail connector, schedule, model, and network policy live on the routine
trigger at claude.ai/code/routines, and prompts/ROUTINE_PROMPT.txt stays a thin
pointer at prompts/routine_instructions.md, exactly like the siblings.

## Phase two option, the video flagship

The weekly best case becomes a 60 second Dispatch style video using the
alaska-ai-weekly machinery (Gemini VO, forced aligned captions, minus 14 LUFS
mix gate, 4x5 master). Heavy, roughly 10x the production weight of a carousel
run, so it earns its slot weekly at most, and only after the daily series has
legs. Not part of the initial build.

## Open decisions (the maintainer's, not the machine's)

1. Direction pick from BRAINSTORM.md (this blueprint assumes the Case File
   core).
2. Posting surface. Evidence says the founder's personal profile, with the
   Alaska.Ai page as archive, also avoids two dailies on one surface.
3. Cadence. The machine drafts daily, the human owns posting cadence. Platform
   evidence favors 3 to 5 posts per week on one surface, a daily draft supply
   supports either.
4. Merge policy for routine runs, autonomous merge like the siblings, or
   review first during a trust building period.
5. The standing offer line wording and where it points (see BRAINSTORM.md,
   lead magnet mechanics).
6. Series name.

# RUN PLAN — 2026-08-15 — Case File No. 2

## Wake state

- Engine bootstrap: **ok** (playwright, pypdf repaired, chromium ok).
- `case_file_no` = `ledger/cases.json` entries (1) + 1 = **2**.
- Shipped so far: case file 1, 2026-07-21, fisheries / computer_vision_counting
  (translation flavor). Industry and capability for this run must differ.
- `ledger/fingerprints.json` also holds a 2026-07-25 run at case_file_no 2, ten
  slides, the deck the maintainer rejected. Its pixels are in the divergence
  set even though it never reached `cases.json`.

## Bank health at wake

**Ship-ready count: 0.** Par is 8.

All 16 bank entries are status `lead`. Not one carries a cost figure. Several
also lack a named human and a timeline. Under the hard intake gate (cost class
AND timeline, `knowledge/CASE_CRAFT.md` filter 5) **nothing in the bank
qualifies to ship**, so Phase 1 restock is mandatory and is the critical path
of this run.

Bank companies that must never be re-surfaced by a scout this run: Fraley and
Schilling, Hardie's Fresh Foods, Checkr, Verst Logistics, BC Machining, NEB
Medical, Carbon Health, Great Lakes Credit Union, Peppermill Resort,
Rogers-O'Brien, Gilbane, Cub Foods / Bashas / Heinens via Afresh, New York
Power Authority, Aire Serv of Sevierville, Kvaroy Fiskeoppdrett, NOAA AFSC /
Ai.Fish.

## Restock assignment (four parallel case-scouts)

| Scout | Ground | Sector lean |
|---|---|---|
| A | Cost-disclosure grounds: conference talks, operator panels, podcasts with transcripts, trade association case libraries, award submissions | construction, trades, field service, freight, warehousing |
| B | Public record: procurement, grant reporting, NIST/state MEP, extension programs, DOT repositories | manufacturing, processing, utilities, ports, engineering |
| C | Regional business journals and sector trade press | clinics, professional services, distribution, hospitality, specialty manufacturing |
| D | The agentic frontier at mid-market scale, vendor libraries as leads only | anything non-tech at 50 to 1,000 people, rungs 4 and 5 |

Every scout carries the seven-part filter, the snippet rule, the ladder bias,
the do-not-resurface list, and the top instincts.

## Top instincts injected this run (confidence >= 0.7)

1. **i-001 (0.80)** — fit display headlines with `AK.fitText` inside
   `renderReady`, never hand-tuned sizes.
2. **i-005 (0.80)** — vendor numbers carry their label in the same breath as
   the number, never a footnote.
3. **i-007 (0.80)** — the caption never claims more than the most hedged slide
   supports. Write the hook FROM the verified claim text.
4. **i-006 (0.75)** — DOM chips and labels in the art zone must be checked
   against canvas coordinates at plan time. Machine QA cannot see canvas.
5. **i-002 (0.70)** — every absolutely positioned text block gets an explicit
   vertical budget.

(i-003, 0.70, also carried into the art build: decorative micro-type must
declare `data-decorative`.)

## Variety constraints derived from `ledger/artwork.json`

The directors room works INSIDE this forbidden list. `variety_check.py
--plan-only` runs before any art code exists.

| Field | Must differ from last | FORBIDDEN values this run |
|---|---|---|
| hero_structure | 4 runs | "underwater data baseline panorama", "typographic cover over night gradient" |
| atmosphere | 3 | "turbid glacial silt water with sonar scan banding", "aurora ribbon and star field over deep night" |
| depth_technique | 3 | "multiplane silt layers with one sharp focal plane", "none, flat layered 2D" |
| hook_archetype | 3 | "status quo exposure", "narrative reversal" |
| palette_family | 3 | "glacial river and sonar screen", "house dark arctic with gold" |
| continuity_device | 2 | "count baseline panorama spine with tally mark states, plus provenance stamp chips", "gold kicker rail and counter" |
| type_pairing | 2 | "Instrument Serif display with Archivo body and JetBrains Mono telemetry", "Fraunces display with Space Grotesk body and JetBrains Mono telemetry" |
| narrative_structure | 2 | "status quo, identification, arrival, reality check, receipts, catch, translation fork, seal", "proof, receipts, translation" |
| line_voice | 2 | "instrument editorial with phantom dash proposal grammar", "thin telemetry rules" |
| render_ladder_top | 2 | none recorded, but must be `akthree` or `aksdf` |

Pixel divergence also runs against the 10 stored slide fingerprints of the
2026-07-25 run. At or above 0.90 correlation is a FAIL.

Consequences the directors room should absorb early: this deck cannot lead
with a full-bleed underwater panorama or a plain typographic night cover, it
cannot use Instrument Serif or Fraunces as the display voice, and its
continuity device cannot be a panorama spine or a gold kicker rail. The
palette must come from the chosen case's own material world, not from the
house arctic default.

## Seasonal Anchorage context for the translation

Mid-August in Southcentral is the closing stretch, not the opening one.

- Construction and civil work are in the last six to eight weeks before
  freeze-up. Everything is "can we get it buttoned up before the ground goes".
- Tourism operators are running out the season, with cruise and lodge staffing
  falling off through September. Season-close accounting and seasonal-labor
  churn are live problems right now.
- Seafood is past the Bristol Bay sockeye peak and into silvers, so processors
  are unwinding a triple-headcount summer.
- School year restarting pulls part-time labor out of service businesses.
- Heating and boiler season prep starts now for mechanical contractors.
- The PFD lands in October, which shifts consumer-facing cash flow.

A translation that lands in this window should prefer a bottleneck that bites
at season close or at freeze-up rather than one that bites in May.

## Route through the rest of the run

Restock -> selection with a runner-up -> fact-check -> translation ->
three-director room inside the forbidden list -> plan-time variety gate ->
storyboard -> copy -> honesty gate BEFORE art -> art build -> four machine
gates plus pixel critics every pass -> coherence gate and the re-read ->
assemble -> score -> ship on branch `tsturg/wonderful-bell-oy73k4` (the
harness-designated branch for this session) with commit-pinned raw URLs ->
upgrade-engineer -> Gmail draft to docket@alaskaaihq.com -> retro.

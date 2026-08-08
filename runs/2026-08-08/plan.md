# RUN PLAN — 2026-08-08 — Case File No. 2

## Wake state

- **Run date:** 2026-08-08
- **Case file no:** 2 (`ledger/cases.json` has 1 entry)
- **Engine bootstrap:** green after a repair. `bootstrap.sh` died on the
  cryptography step with a pip read timeout to files.pythonhosted.org; a manual
  retry of `pip install --user --upgrade cryptography` succeeded and
  `from pypdf import PdfReader, PdfWriter` now imports. **Vector PDF path is
  available.** Logged as an incident in `run_state.json`.
- **Chromium:** present at `/opt/pw-browsers`.

## Ledger state

- `cases.json` — 1 shipped entry (2026-07-21, case 1, fisheries /
  computer_vision_counting, translation flavor).
- `artwork.json` — 2 entries (case 0 engine proof, case 1).
- `fingerprints.json` — holds run 2 (2026-07-25, 10 slides), the deck the
  maintainer **rejected as cookie-cutter**. It never reached `cases.json` or
  `artwork.json`, so it constrains this run on PIXELS only. That is the point
  of it being there.
- `bank.json` — **16 entries, all status `lead`, ship_ready_count 0, par 8.**
  Every seeded case was demoted on 2026-07-28 when the cost-and-timeline hard
  gate landed. **Phase 1 is a full restock and it is not optional.**

## Rotation constraints (from cases.json)

- Industry must differ from the last 3 shipped: **not fisheries.**
- Capability must differ from the last 3 shipped: **not computer_vision_counting.**
- Company never repeats.

## Variety constraints — the forbidden list (Engine B, from artwork.json)

The directors room works INSIDE this list. Nothing here may be re-declared.

| Field | Lookback | Forbidden values |
|---|---|---|
| hero_structure | 4 runs | `typographic cover over night gradient`, `underwater data baseline panorama` |
| atmosphere | 3 | `aurora ribbon and star field over deep night`, `turbid glacial silt water with sonar scan banding` |
| depth_technique | 3 | `none, flat layered 2D`, `multiplane silt layers with one sharp focal plane` |
| hook_archetype | 3 | `narrative reversal`, `status quo exposure` |
| palette_family | 3 | `house dark arctic with gold`, `glacial river and sonar screen` |
| continuity_device | 2 | `gold kicker rail and counter`, `count baseline panorama spine with tally mark states, plus provenance stamp chips` |
| type_pairing | 2 | `Fraunces display with Space Grotesk body and JetBrains Mono telemetry`, `Instrument Serif display with Archivo body and JetBrains Mono telemetry` |
| narrative_structure | 2 | `proof, receipts, translation`, `status quo, identification, arrival, reality check, receipts, catch, translation fork, seal` |
| render_ladder_top | 2 | (no prior entry declares one; free, but must still be `akthree` or `aksdf`) |
| line_voice | 2 | `thin telemetry rules`, `instrument editorial with phantom dash proposal grammar` |

**Pixel divergence (Engine B, B2):** every slide correlated against all 10
stored fingerprints from the rejected 2026-07-25 deck. At or above 0.90 fails.
That deck was dark, centre-weighted, one brightness (value arc 0.059). The
cheapest structural way to clear it is a genuinely different value arc and
genuinely different compositional anchors per slide.

**Within-deck (Engine A):** mode cap 3, no repeated mode+layout_family pair,
70 percent distinct layout families, no reused art system, a custom note per
slide of at least six words, value arc at or above 0.12, render ladder top at
`akthree` or `aksdf`.

## Top instincts injected into every subagent this run

From `ledger/instincts.json`, confidence >= 0.7, top 5 by confidence:

1. **i-001 (0.8)** — Fit display headlines with `AK.fitText` inside
   renderReady, never hand-tuned font sizes. Hand-sized hooks wrap an extra
   line and collide with the block below.
2. **i-005 (0.8)** — Vendor-sourced numbers carry the label in the same breath
   as the number, never in a footnote. Trust is the product.
3. **i-007 (0.8)** — The caption must never claim more than the most hedged
   slide supports. Write the hook FROM the verified claim text, not from the
   story's vibe.
4. **i-006 (0.75)** — DOM chips and labels in the art zone must be checked
   against canvas data-mark coordinates at plan time. Machine QA cannot see
   canvas, so these collisions survive to the pixel critics or the reader.
5. **i-002 (0.7)** — Every absolutely positioned text block gets an explicit
   vertical budget. A bottom-anchored block under a top-anchored stack collides
   the moment content grows a line.

(Also carried, below the top-5 cut but cheap to honour: i-003, micro text in
the constellation carries `data-decorative`; i-004, lead with the ordinary
company detail before any technology word; i-008, plant the next slide on the
keepable receipts slide.)

## Seasonal Anchorage context, 2026-08-08

Early August. This is the top of the operating year for most of Dana's
segments, which is exactly when a bottleneck is felt hardest:

- **Tourism and hospitality at peak.** Cruise season runs through September;
  staffing, dispatch and front-desk load are at maximum right now, and the
  season's cash has to be made before the boats stop.
- **Seafood processing at peak headcount.** Bristol Bay sockeye has come off
  its late-July peak, Southcentral and Southeast silvers are running; plants
  are still at triple headcount and burning admin hours.
- **Construction and civil at the crunch.** The paving and site season closes
  at freeze-up around October. August is when a permitting or estimating
  backlog turns into work that does not happen this year.
- **Air cargo and freight** running summer volume into the fall barge and
  freeze-up push.
- **Fire season** on the road system.
- **PFD** applications closed in March; the payout lands in early October,
  which is when retail and services see the bump. Not an August lever.
- School restarts mid-August; workforce churn as seasonal staff leave.

**The translation should land in season where it honestly can.** A bottleneck
that is worst in August lands harder in August. This is the translator's call,
not a licence to force it.

## Phase 1 plan — full restock, four scouts in parallel

Bank is at 0 of par 8, so all four grounds run. Each scout gets: its ground,
the full 16-company do-not-resurface list, the coverage gaps, the top
instincts, and the hard gate stated first (cost AND timeline, checked early).

| Scout | Hunting ground | Sector priority |
|---|---|---|
| S1 | Cost-disclosure grounds: conference talks, operator panels, podcasts with transcripts, award submissions, trade association case libraries | Construction, trades, field service, mechanical and electrical contracting |
| S2 | Regional business journals + sector trade press (Supply Chain Dive, Transport Topics, FreightWaves, Manufacturing Dive) | Logistics, freight, distribution, warehousing, manufacturing |
| S3 | Government, academic, procurement and grant records + state MEP centers | Utilities, public works, municipal, healthcare operations, manufacturing |
| S4 | Vendor libraries used strictly as LEADS, then go around the vendor for an independent account | Professional services, clinic groups, hospitality and tourism, food processing and distribution |

**Do-not-resurface (already in the bank):** Fraley and Schilling, Hardie's
Fresh Foods, Checkr, Verst Logistics, BC Machining, NEB Medical, Carbon Health,
Great Lakes Credit Union, Peppermill Resort Spa Casino, Rogers-O'Brien
Construction, Gilbane Building Co, Cub Foods / Bashas / Heinens (Afresh), New
York Power Authority, Aire Serv of Sevierville, Kvaroy Fiskeoppdrett / Seloy
Sjofarm, NOAA AFSC / Ai.Fish. Also excluded: the shipped case 1 material
(SalmonVision, ADF&G).

**Coverage gaps to prioritise:** anything that is NOT fisheries and NOT
computer-vision counting; ladder rungs 4 and 5 (multi-step workflows, tool use,
human-in-the-loop checkpoints) over rung 2 and 3 chatbots; a named human with a
verbatim quote; and above all a page that says what it cost and how long it
took.

## The bar this run has to clear

Run 1 shipped a translation-flavour post about a state agency counting fish.
Run 2 was rejected as a cookie-cutter deck. **This run needs an actual company
Dana can be**, with a bought-and-configured build, a disclosed price and a
disclosed timeline, and eight slides that were each composed once. The one
sentence we are engineering, still: *"Huh. I could do that."*

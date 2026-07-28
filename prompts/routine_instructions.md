# ALASKA AI — CASE FILES, the run contract

## ROLE

You are the showrunner. One run produces ONE post-ready LinkedIn carousel
breaking down a verified story of an ordinary midsized company that pointed AI
at one named bottleneck and got a measurable result, translated honestly to
Anchorage, delivered as a Gmail draft.

`CLAUDE.md` is the law above this file and never bends. This file is how a run
executes.

**The whole run has one job: produce the sentence "Huh. I could do that." in
the head of one specific person.** Everything below serves that.

---

## NON-NEGOTIABLES (the contract)

1. **THIS ROUTINE DRAFTS. IT NEVER POSTS.** Every run ends with a Gmail draft.
   Nothing is published to any platform by the machine, ever. No tool that
   posts is given to this routine and none is ever added.
2. **THE PRIVACY WALL.** The private sibling repo `alaska-ai-leadflow` and its
   database do not exist to this routine. No lead, no dossier, no prospect
   fact is read, referenced, or hinted at. Segments, never targets.
3. **NEVER INVENT.** Every fact traces to a page fetched THIS RUN. Not from
   memory, not from the knowledge base, not from a search snippet. A
   fabricated company, number, quote, person or outcome is the single
   unforgivable failure.
4. **THE KNOWLEDGE BASE IS PRIORS, NEVER A CITATION.** `knowledge/kb/` tells
   you where to look and what to expect. It never tells you what is true about
   a specific company, number, or product. When it disagrees with a fetched
   page, the page wins and the disagreement gets logged.
5. **COST AND TIMELINE ARE A HARD INTAKE GATE.** If we cannot tell the reader
   roughly what it cost and roughly how long it took, the case does not
   qualify. Not "we ship without that slide." It does not qualify.
6. **LAYOUT YIELDS TO COPY.** Copy is never deleted to fix a layout problem.
   The copy record is the story of record.
7. **EVERY SLIDE IN A RUN IS CUSTOM, AND NO RUN LOOKS LIKE A PREVIOUS RUN.**
   Both variety engines are enforced, at plan time and on pixels.
8. **THE ITERATION LAW.** Every artifact facing a critic loops until it meets
   the standard. The standard never bends, the artifact bends. A KILL verdict
   disqualifies the CASE, not the run: swap to the runner-up and continue.
9. **BOUNDED SPAWNING.** Subagents run in parallel where the contract says so.
   A failed subagent is respawned at most ~3 times, then you execute its role
   yourself at the same bar.
10. **SCOPE GUARD.** Sibling checkouts are reference only. Never write to them.

---

## CONTEXT (read before starting, in this order)

**The doctrine, in dependency order:**
1. `knowledge/THE_READER.md` — who Dana is, the six questions. Everything else
   is downstream of this file.
2. `knowledge/AGENTIC_LITERACY.md` — the ladder, the curriculum
3. `knowledge/CASE_CRAFT.md` — the qualifying filter and the story grammar
4. `knowledge/NARRATIVE_COHERENCE.md` — one idea, eight slides, no chop
5. `knowledge/VARIETY.md` — the two variety engines
6. `knowledge/DESIGN_DOCTRINE.md` — the visual bar
7. `knowledge/ALASKA_TRANSLATION.md` — the landing
8. `knowledge/CAROUSEL_CRAFT.md`, `SLIDE_DOSSIER_SPEC.md`,
   `TECHNIQUE_LIBRARY.md`, `FIELD_NOTES.md`

**The standing knowledge** (`knowledge/kb/`): `README.md` first for the
handling law, then `DEPLOYMENT_PATTERNS.md`, `EVIDENCE.md`, `ECONOMICS.md`,
`AI_LANDSCAPE.md`, `HUNTING_GROUNDS.md`, `VENDOR_MAP.md`, `ANCHORAGE.md`.

**Config:** `config/brand.yaml`, `config/sources.yaml`,
`config/scoring_rubric.yaml`.

**Ledgers:** `ledger/bank.json`, `cases.json`, `artwork.json`,
`fingerprints.json`, `instincts.json`, `upgrades.json`.

**The engine:** `.claude/skills/carousel-engine/SKILL.md` is the slide
contract.

---

## RUN STATE (crash-resilient checklist)

At wake, create `out/<date>/run_state.json`:
```json
{"run_date": "...", "case_file_no": N, "bank_id": "...",
 "phases": {"wake": "pending", "restock": "pending", "selection": "pending",
  "verification": "pending", "translation": "pending",
  "directors_room": "pending", "storyboard": "pending", "copy": "pending",
  "honesty_gate": "pending", "art_build": "pending", "review_loop": "pending",
  "coherence_gate": "pending", "assemble": "pending", "scoring": "pending",
  "ship": "pending", "upgrade": "pending", "gmail": "pending",
  "retro": "pending"}}
```
Update each phase to "done" WITH artifact paths as you complete it. The
COMPLETION GATE (before ship) requires every phase done and every artifact
existing. If the session restarts, resume from run_state.

---

## PHASE 0 — WAKE

1. `bash .claude/skills/carousel-engine/bootstrap.sh`
2. Read the doctrine, the knowledge base, the config and the ledgers above.
3. `case_file_no` = `ledger/cases.json` entries + 1.
4. Extract the TOP 5 instincts (confidence >= 0.7) from
   `ledger/instincts.json`. Inject them into every subagent prompt this run.
5. **Derive the variety constraints.** From `ledger/artwork.json`, list the
   forbidden values per the divergence table in `knowledge/VARIETY.md`
   (hero_structure last 4, atmosphere last 3, depth_technique last 3,
   hook_archetype last 3, palette_family last 3, continuity_device last 2,
   type_pairing last 2, narrative_structure last 2, render_ladder_top last 2,
   line_voice last 2). Write the forbidden list into the plan. The directors
   room works inside it.
6. Note the seasonal Anchorage context (fishing openers, freeze-up, PFD,
   tourism season, boiler season) so the translation lands in season when it
   can.
7. Write `out/<date>/plan.md` with all of the above.

## PHASE 1 — BANK RESTOCK (conditional, bounded)

Count ship-ready cases in `ledger/bank.json`: status candidate or verified,
**cost AND timeline disclosed**, company not already in `cases.json`.

If fewer than 8, spawn up to FOUR `case-scout` agents in parallel, one per
hunting ground from `config/sources.yaml`, each with: the ground, the current
bank company list (never re-surface), the coverage gaps, and the top instincts.

The scouts hunt operator language, not AI language. They check cost and
timeline EARLY. They read full pages before citing anything, and a company
name never enters the bank from a search snippet.

Merge their JSON into the bank with skepticism labels intact. Near misses go
in as LEADS with what is missing named. Write `out/<date>/restock_notes.md`.
Log any cross-scout contradiction as an incident, resolved in favour of the
agent that read the page.

## PHASE 2 — SELECTION

Apply the seven-part qualifying filter from `knowledge/CASE_CRAFT.md` to the
bank. **All seven must hold.** Then apply the preference order: the more
agentic build, then the more ordinary company, then the better documented cost
and timeline, then the sector that maps hardest onto Anchorage.

Pick a case AND a runner-up. Write `out/<date>/selection.md` with the six
questions answered for the chosen case, in writing, honestly.

**If nothing in the bank qualifies, restock rather than lowering the bar.**
A run that ships a case Dana cannot be has failed more expensively than a run
that ships late.

## PHASE 3 — VERIFICATION

Spawn `fact-checker` with the chosen case and every URL. It re-fetches
everything fresh this run, verifies every number and quote verbatim in the
page, finds the baseline, the denominator, who measured it, the date, one
limit the source names itself, the cost, the timeline, and a named human. It
tries to break the case. It drops what cannot be proven.

Output: `out/<date>/claims.json`. **This is the only source of truth copy and
slides may draw from.** Nothing reaches a slide that is not in it.

**If verification kills the cost or the timeline, the case is dead.** Swap to
the runner-up and re-run this phase. That is what the bank is for.

## PHASE 3.5 — TRANSLATION ROOM

Spawn `translator` with the verified case. It produces
`out/<date>/translation.md`: which Anchorage segments carry this exact
bottleneck, the local version of the build, the honest ladder rung, a cost
class as a range, where it does NOT translate, and the local proof pairing.

Segments, never a named local company as a target.

## PHASE 4 — DIRECTORS ROOM (the planning phase, and the cheapest place to fix
anything)

Spawn THREE `treatment-director` agents in parallel with different creative
lenses, each given the verified case, the translation, the forbidden variety
list from Phase 0, and the doctrine. Each pitches ONE complete deck treatment.

Synthesize the winner, grafting the best ideas from the runners-up. Then
produce THREE planning artifacts before any slide code exists:

**a. `out/<date>/deck_signature.json`** — the variety declaration. Deck level
fields plus, per slide: `mode`, `layout_family`, `art_system`, `value`,
`temperature`, and a `custom_note` naming what makes that slide unlike every
other slide in the deck.

**b. `out/<date>/coherence.json`** — the through-line contract. The deck's ONE
thesis sentence, and per slide the `role`, the `promise` it opens, and which
earlier slide it `pays`.

**c. `out/<date>/zones.json`** — per slide, the named rectangles (`HEAD`,
`BODY`, `ART`, `DATA`, `FOOTER`, `BRAND`), any knockout plates, and the art
rectangles in canvas coordinates. Every text element will declare its zone.

Then run the plan-time gate:

```
python scripts/variety_check.py --signature out/<date>/deck_signature.json --plan-only
```

**Green before any art gets written.** A template caught here costs minutes.
The same template caught after a render costs the run.

Write `out/<date>/storyboard.md` with the per-slide dossiers per
`SLIDE_DOSSIER_SPEC.md`, including the explicit vertical budgets.

## PHASE 5 — COPY CHAMBER

Spawn `copywriter` with the claims, the translation, the storyboard and the
brand config. It writes `out/<date>/copy.json` containing:

- `slides[]` with per slide `n`, `role`, `kicker`, `headline`, `body`,
  `labels[]`, `source_labels[]` — **the story of record**
- `post_copy` (the caption), `first_comment` (sources, full URLs, labels),
  `document_title`, `aftercare`, `claims_used`

Every factual string carries a claim id. Vendor numbers carry their label in
the same breath. The offer line appears exactly once, exactly as configured.

Then:
```
python scripts/caption_check.py ...
python scripts/style_lint.py ...
```

## PHASE 5.5 — HONESTY GATE (BEFORE the art, not after)

Spawn `case-critic` with the storyboard, the copy record, the claims and the
translation. It defaults to reject.

**This phase runs before Phase 6. It is sequenced here on purpose:** in the
2026-07-25 run it ran after the art was built, every fix it issued had to be
retrofitted into live slide code, and the gate was never re-run. Do not repeat
that.

Apply every fix to the storyboard and the copy record. Re-run the critic until
it passes. Only then build art.

## PHASE 6 — ART BUILD

Build the slides per the storyboard, the dossiers and `DESIGN_DOCTRINE.md`.

**The rules that are not optional:**
- Every text element declares `data-zone`, and `data-block` where it shares a
  vertical budget. Text in ART carries `data-knockout` on an explicit plate.
- One source of truth for coordinates. If the canvas draws at x, the DOM label
  reads that same x from a shared constants object. Never retype a number that
  already exists in the art code.
- Every display headline fitted with `AK.fitText` after
  `await document.fonts.ready`. Never hand-tune a display size.
- The rendered ladder is climbed: at least one slide reaches `akthree` or
  `aksdf`, with its Canvas fallback designed in the dossier, never improvised.
- Finish every art canvas with `AKPOST.grade`. Build every ramp in OKLCH.
- **Machine QA cannot see canvas.** Anything placed relative to painted art is
  invisible to it. That is why the zones are declared.

Render:
```
python .claude/skills/carousel-engine/render.py --slides-dir out/<date>/slides --out-dir out/<date>/render
```

## PHASE 7 — THE REVIEW LOOP (all four gates, every pass)

This is the loop that produced the last run's defects, so it is now specified
exactly. **After EVERY render, including every fix pass, run all four:**

```
python .claude/skills/carousel-engine/qa.py       --render-dir out/<date>/render
python scripts/layout_check.py --render-dir out/<date>/render --zones out/<date>/zones.json
python scripts/variety_check.py --render-dir out/<date>/render --signature out/<date>/deck_signature.json
python scripts/coherence_check.py --render-dir out/<date>/render --copy out/<date>/copy.json \
    --contract out/<date>/coherence.json --claims out/<date>/claims.json \
    --baseline out/<date>/coherence_snapshot.json --snapshot out/<date>/coherence_snapshot.json
```

Then spawn `pixel-critic` agents in parallel across slides. They read the full
size PNG and the 432px thumb, transcribe every visible word, and judge against
the dossier checklist and the doctrine.

**How to fix, in this order, and the order is the point:**

1. Re-lay the slide. Give the text more room. Move the art.
2. Change the composition. A different mode may hold this copy better.
3. Split across two slides, and update the copy record AND the contract.
4. **Only then**, and only via the copywriter, shorten the copy while
   preserving every load-bearing element, and update the record.

**Never delete a sentence inline in the HTML because a box overflowed.** That
edit is invisible to everything except the coherence gate, which will fail the
build, correctly.

Loop until all four gates are green and the pixel critics pass. A variety
failure is fixed by recomposing, never by recolouring.

## PHASE 7.5 — THE COHERENCE GATE

Spawn `flow-critic` with the contact sheet, the thumbs, the copy record, the
through-line contract, and the machine reports from `coherence_check.json` and
`variety_check.json`.

It judges the deck as ONE DOCUMENT. It defaults to revise. It may not pass a
deck where the thesis it reads differs from the contract's thesis, where any
loop goes unpaid, or where any slide is removable with no loss.

**Every fix it issues sends the deck back through Phase 7, all four gates.**
That is the loop, and it is the whole point of having one.

**Then the re-read, and it is not optional.** After the FINAL fix pass, read
the deck start to finish as one document, from the contact sheet and the PDF,
as Dana. Answer out loud: what is this deck's one sentence, where does it
stutter, and what would be lost if slide N were removed. A deck that passes
every machine gate and fails the re-read does not ship.

## PHASE 8 — FINAL ASSEMBLY

Re-run `assemble.py` for the final artifacts: `out/<date>/final/carousel.pdf`
(vector expected; raster fallback only if the vector path breaks, and noted in
the email), `contact_sheet.png`, `thumbs/`. Verify `assemble_report.json`:
slide count correct, `pdf_mode` vector, `pdf_mb` in 2 to 25.

## PHASE 9 — SCORING

Spawn `scorer` with everything: renders, thumbs, contact sheet, storyboard,
copy record, claims, translation, and **all four machine gate reports**.
Persist to `out/<date>/score_report.json`.

A green score over a red gate is a scoring failure. Report every gate verdict.

- Below threshold: apply the one sentence fix and the weakest criterion
  repairs, then back through Phase 7. Max 2 scoring cycles, then the iteration
  ladder governs.
- Any HARD FAIL: fix it no matter what. If unfixable this run, fall back to
  the runner-up ONLY if before Phase 6; otherwise ship nothing, write the
  post-mortem email per the failure protocol, and commit the evidence.
- **Never report a score that was not recomputed after the last fix.** If a
  fix pass followed the last scoring, either re-score or say plainly in the
  email that the number predates the fixes.

## PHASE 10 — SHIP (commit, push, PR; merge policy in CLAUDE.md)

1. Copy shippable artifacts to `runs/<date>/`: slide PNGs, carousel.pdf,
   contact_sheet.png, thumbs/, storyboard.md, claims.json, translation.md,
   copy.json, coherence.json, deck_signature.json, zones.json, caption.txt +
   caption_report.json, honesty_report.json, score_report.json,
   machine_qa.json, layout_check.json, variety_check.json,
   coherence_check.json, assemble_report.json, selection.md, plan.md,
   run_state.json.
2. Append this run's entries to `ledger/cases.json` and `ledger/artwork.json`
   (full schemas), update the shipped case in `ledger/bank.json` (status
   shipped), add 1 to 3 new instincts (confidence scored, bump or decay old
   ones), append the retro bullets to `knowledge/FIELD_NOTES.md`, and merge
   the translator's bottleneck map row into `knowledge/ALASKA_TRANSLATION.md`
   when it adds one.
3. **Record the variety fingerprints**, which is what makes the NEXT run have
   to diverge from this one:
   ```
   python scripts/variety_check.py --render-dir out/<date>/render \
       --signature out/<date>/deck_signature.json --record
   ```
   A run that does not record has broken the engine for every future run.
4. COMPLETION GATE: verify `run_state.json` shows every prior phase done and
   every file in (1) exists and is non-trivial.
5. Branch `claude/case-file-<date>`; commit everything (runs/, ledger/,
   knowledge/ changes); push with retries (2s/4s/8s/16s backoff). Record the
   pushed commit SHA.
6. Open a PR per the CLAUDE.md delivery policy (ready, not draft). The email's
   links are COMMIT-PINNED
   (`https://raw.githubusercontent.com/<owner>/<repo>/<sha>/runs/<date>/...`)
   so delivery never depends on a merge.
7. Verify two spot URLs resolve at the pinned SHA (WebFetch a slide PNG raw
   URL and the PDF URL). If they 404, wait 30s and retry once; if still
   broken, say so loudly in the email instead of shipping dead links.

## PHASE 11 — AUTOMATION RETRO + UPGRADE

Spawn `upgrade-engineer` (Opus pinned) with the run date, the run_state path,
and your incident notes. It executes its retro, its frontier scan, and 0 to 3
bounded verified upgrades, and logs to `ledger/upgrades.json`. The upgrade set
is its own `upgrade(<date>):` commit.

**Two things it owns that a run is not complete without:**

**a. The knowledge base append.** Everything this run CONFIRMED or
CONTRADICTED goes into the relevant `knowledge/kb/*.md` file under
`## CONFIRMED BY RUNS`, dated, **naming the URL that established it**. A
pattern seen for the first time, a cost band corrected by a real disclosed
figure, a source that turned out to launder a press release, a search query
that worked, anything a fetched page proved wrong. An entry with no source URL
is an opinion and does not belong there.

**b. The variety retro evaluation**, per `knowledge/VARIETY.md`: the numbers
and their trend, the closest pair judged by eye, which previous run this one
most resembles and on what measure, the reuse honesty question, and whether
any threshold fired on something fine or passed something lazy.

Zero upgrades is acceptable. Unverified upgrades are not.

## PHASE 12 — GMAIL DRAFT

```
python scripts/gmail_draft.py --run-dir out/<date> --run-date <date> \
  --case-no <N> --raw-base https://raw.githubusercontent.com/<owner>/<repo>/<sha> \
  --branch claude/case-file-<date> --payload-out out/<date>/gmail_payload.json
```
Create the draft via the Gmail MCP `create_draft` tool with the payload
(subject, `to` the maintainer, html_body). Save the returned draft id to
`runs/<date>/gmail_draft_id.txt` (a follow-up commit is fine).

**THE EMAIL BODY IS THE SCRIPT'S OUTPUT, VERBATIM.** Never hand compose or
restyle it. The paste-ready blocks are a copy/paste contract:
- The POST block contains ONLY the caption (hook, body, offer line, question,
  hashtags). No sources, no URLs, nothing else.
- The FIRST-COMMENT block is plain text, one source per line with its full raw
  URL visible and vendor labels where due.

FALLBACK if Gmail MCP is unavailable: commit `gmail_payload.json` under
`runs/<date>/` and make the run summary very loud about where it lives.

## PHASE 13 — RETRO

End with a summary: the case, the score, what the critics caught, all four
gate verdicts, the variety numbers, bank health (ship-ready count with cost
and timeline), what was learned, and the one thing to improve next run. Mark
run_state complete.

---

## FAILURE PROTOCOL

- A subagent that FAILS is handled by CAUSE. Respawn only the SAME failed
  agent, cap ~3 attempts, then treat that agent as unavailable and execute its
  role yourself at the same quality bar. A retry REPLACES the failed agent.
- **ONLY IF the failure is an account usage limit of any kind:** do NOT degrade
  to a solo run, do NOT ship a reduced deck, do NOT abandon. (1) read the reset
  time from the error (poll with backoff if unstated), (2) WAIT until reset,
  however long, (3) RESUME from run_state exactly where it stopped. Waiting is
  only for the usage-limit case.
- Engine breakage unfixable in ~3 attempts: ship a REDUCED deck (fewer slides,
  simpler technique) rather than nothing. The quality bar still applies to what
  ships, including both variety engines and the coherence gate.
- A dead case (verification, cost gate, or honesty kill) is never a dead run:
  swap to the runner-up, and if the runner-up dies too, take the next best bank
  entry. The bank exists so the run never starves.
- **A case that cannot produce a cost and a timeline is dead, not thin.** It
  goes back to the bank as a lead. This is the rule the 2026-07-25 run got
  backwards, and it is the most important single change in this contract.
- Total failure (nothing can responsibly ship): still create the Gmail draft,
  subject "Alaska.Ai — Case Files run failed — <date>", with the post-mortem
  and what exists. Commit the evidence to the run branch.
- Never fabricate. A thin true post beats a rich invented one. A missed day
  beats a wrong day.

## SUCCESS CRITERIA (all must hold)

1. Gmail draft exists: post copy with the offer line once, first-comment
   sources with labels, document title, inline previews, working commit-pinned
   URLs for every slide PNG and the PDF, report card, all four gate verdicts,
   aftercare checklist, automation-changes section (even if "no changes"),
   bank health line.
2. `runs/<date>/` committed and pushed with all artifacts; ledgers updated
   (cases, artwork, bank, **fingerprints**, instincts, upgrades); knowledge
   updated (field notes, the knowledge base appends, bottleneck map when
   earned); PR opened per CLAUDE.md policy; run_state complete.
3. All four machine gates green: `machine_qa`, `layout_check`,
   `variety_check`, `coherence_check`.
4. `score_report.json` at or above threshold, recomputed after the last fix,
   OR an explicit honest shortfall note in the email saying so.
5. `carousel.pdf` has vector text (or the noted fallback), correct page count,
   4:5 1080x1350 pages.
6. The case had a disclosed cost and a disclosed timeline, and the deck says
   both.
7. **The final read as Dana produces "I could do that," not "that was well
   made."** If it produces the second one, it did not ship.

Now begin Phase 0.

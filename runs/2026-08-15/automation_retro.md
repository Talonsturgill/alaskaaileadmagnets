# AUTOMATION RETRO, 2026-08-15, Case File No. 002

Upgrade engineer, run after ship (SHA 4add2b7, PR #6) and before the Gmail
draft. Scope: what deviated from `prompts/routine_instructions.md`, what the
frontier scan found, what changed in the machine, and the variety evaluation
required by `knowledge/VARIETY.md`.

---

## 1. REACTIVE RETRO, phase by phase against the spec

| Phase | Verdict | Evidence |
|---|---|---|
| 0 wake | deviation, structural | Bank held 16 entries and **0 ship-ready**, against a par of 8. Not one entry carried a disclosed cost (`ledger/bank.json` `_doc`, triaged 2026-07-28). |
| 1 restock | ran, over budget | Two waves, seven scouts, before ONE case existed. Wave one returned zero bankable candidates across four grounds (`runs/2026-08-15/restock_notes.md`). Restock became the critical path of the run. |
| 2 selection | shipped with **no runner-up** | Grand Island Express died on the cost gate after a dedicated chase (`ledger/bank.json` bank-018 skepticism field). The spec's premise, "the bank exists so the run never starves", did not hold. A KILL at any later phase would have ended the run with nothing. |
| 3 verification | worked, and killed the brief | The fact-checker killed the briefed hero numbers (the 18-to-10 headcount cut) because the operator refuses the AI attribution twice, naming a compensation change. Correct behaviour, and the surviving claim is better. Also logged: ZERO independent corroboration, six routes attempted. |
| 3.5 translation | clean | no deviation |
| 4 directors room | clean | no deviation |
| 5 copy | clean | no deviation |
| 5.5 honesty gate | worked, and earned its position | Caught a quantified Anchorage weather claim ("eleven nights a year") that was our analysis wearing the clothes of a fetched fact, BEFORE it was built into slide 8 art. Under the old ordering this would have been a retrofit. |
| 6 art build | clean | no deviation |
| 7 review loop | **gate instrument was blind** | `render.py` truncated every reported text node to 80 chars, so `coherence_check` could not verify any authored sentence longer than that and failed 58 fidelity checks on correct copy. Fixed in commit 4f76952 (limit raised to 600). Verified still in force this retro: longest reported node in a fresh engine-proof render is 188 chars. |
| 7 variety | passed on the **second** recomposition | Median layout IoU went 0.52 (FAIL) then 0.51 (FAIL) then 0.477 (pass, 0.023 under the 0.50 hard line). Slides 5, 7, 8 recomposed. |
| 7.5 coherence gate | passed with 5 warns | Two of the five are the deck's own case-file counter ("002 traces to no claim"), i.e. gate noise. Two more are the modeled Anchorage dollar range, which the slide labels correctly as our analysis. See PARKED below. |
| 8 assembly | clean | no deviation |
| 9 scoring | clean | 8.16 weighted against a threshold of 8.0, SHIP, zero hard fails. |
| 10 ship | shipped, but the **completion gate could not have passed as written** | `runs/2026-08-15/run_state.json` still reads `review_loop: in_progress`, `coherence_gate: pending`, `scoring: pending`, `ship: pending` while all of those completed and the gate verdicts are recorded in the same file. Phase 10 step 4 requires "run_state.json shows every prior phase done". It was judged by hand instead. Everything else in step 1's artifact list is present, `ledger/fingerprints.json` carries the 2026-08-15 record, and `cases.json` / `artwork.json` / `bank.json` were all updated. |
| retro inputs | one wrong number reached the retro | The showrunner's notes name the closest slide pair as 08 x 09 at IoU 0.545. The actual closest pair is **07 x 08** (IoU 0.657, corr 0.423, palette 0.982). The number was printed to the console and never persisted to `variety_check.json`, so the retro had to hand-scan a 36-row matrix. Fixed this retro (upgrade 2). |

### Process collision, worth naming

The showrunner committed three more times DURING this retro (8956c6b, d8713c4,
e587431, flow-critic fix, cover invoice, score and honesty report reshape). Two
of those commits swept my in-progress working-tree edits into themselves:
`scripts/style_lint.py` landed inside d8713c4 and `scripts/variety_check.py` plus
`prompts/routine_instructions.md` inside e587431. **The upgrade set therefore
does not revert as one commit this run, which is a spec deviation
(`prompts/routine_instructions.md` Phase 11).** The rollback instructions in
`ledger/upgrades.json` are written per file so the changes can still be undone by
hand. Two fixes for next time, both cheap: run Phase 11 strictly after the
showrunner's last commit, and have the upgrade engineer work on a scratch branch
or stage-and-commit each change as it is verified.

Consequence for verification: the deck changed after my first verification pass
(slide 01 and slide 03 were re-rendered by those commits). Everything below was
re-verified against the FINAL `runs/2026-08-15/slides`: render 9/9 OK, QA
identical, style_lint clean on 85 nodes, variety numbers unchanged.

### Environment and fetch layer

- **HAZARD, the most serious incident of the run.** The fetch layer FABRICATED
  roughly eighty bullet points on one long page, including invented statistics,
  in fluent form. It nearly reached a slide. The mitigation that worked, now
  standing practice and appended to `knowledge/kb/EVIDENCE.md`: narrow
  enumerated prompts ("quote the full sentence containing each of these words,
  say NOT PRESENT if absent") plus cross-checking every quoted string across two
  independent renderings before trusting it.
- **403 wall.** Thirteen domains blocked outright, including the best
  cost-disclosure format in trucking. `r.jina.ai/<url>` defeats it on
  Randall-Reilly properties. Both the blocklist and the workaround are now in
  `knowledge/kb/HUNTING_GROUNDS.md`.
- **SEO poisoning.** Reproduced independently in this retro's own frontier scan:
  every generic operator-cost query returned vendor listicles.

### Bank intake skepticism notes, checked against what died

The intake notes were right, not wrong. CJB Industries was banked with its
future-tense problem named at intake and it died at intake, four times over,
independently. Grand Island Express was banked as "cost unknown" and died on
exactly that. **No entry died at fact-check because its skepticism note was
wrong.** The bank's failure mode this run was volume of qualified entries, not
quality of labelling.

---

## 2. FRONTIER SCAN

**Focus:** voice AI in field service, and where the honest rung-4 versus rung-5
line sits in that category right now. Rotated in because the last scan_log entry
(2026-07-21) was skipped, and because the shipped case is in this category.
Six searches, three substantive fetches, about 25 minutes.

**What was established, each with the page that established it:**

1. **Almost every published number in voice AI is a containment number, and
   containment is not resolution.** Stated plainly on a vendor CEO's own blog,
   which is where the honest version of this distinction currently lives:
   "A call is contained if the customer hangs up. It's resolved if their problem
   is fixed", and "Many vendors quote 'containment rate' ... rather than
   resolution rate ... These are not the same number."
   https://irisagent.com/blog/voice-ai-customer-service-2026-benchmarks/
   The page cites no survey with a sample size, and its author sells the
   category. Recorded in `EVIDENCE.md` as a smell test, with the question to
   demand of any case in this pattern: how many contained calls called back.
2. **Adoption in the trades is broad, shallow and size-blind.** A Housecall Pro
   survey of over 400 US home service contractors: "over 70% have tried AI
   tools", "about 40% are now using AI actively", and "From solo owner-operators
   to 50+-person companies, small shops are embracing AI nearly as much as large
   ones." https://www.pmmag.com/articles/106575-70-of-home-service-professionals-now-use-ai-to-cut-admin-work-not-field-jobs-housecall-pro-report-finds
   Vendor-run survey of its own base; labelled as such in `AI_LANDSCAPE.md`.
   Useful only as orientation, never as a fear line.
3. **A platform-data number for any after-hours story:** "Across jobs booked
   online on Housecall Pro, 41% come in after hours when many businesses aren't
   responding actively."
   https://www.housecallpro.com/resources/field-home-service-industry-trends/
4. **pmmag.com is fetchable while its BNP Media sibling achrnews.com is
   blocked.** Publisher-level blocking is not a rule. Test the domain.
5. **Nothing fetched described a rung 5 deployment in field service.** Every
   product in the category runs fixed steps into one system of record with a
   designed human handoff. The rung 4 line held.

---

## 3. UPGRADES (2 applied, 1 logged as already done, 3 parked)

### U1, on-slide house-style lint (`scripts/style_lint.py`)

`config/brand.yaml` on_slide_text_rules says "No em dashes or en dashes in ANY
on-slide string" and "Straight quotes." `caption_check.py` has enforced exactly
that on the caption since 2026-07-21. **Nothing enforced it on the slides or on
copy.json**, so this deck carried mixed apostrophe characters until a pixel
critic caught them by eye, and asked for a lint that did not exist. Eyes are not
a gate.

- `style_lint.py` now also refuses the banned glyphs (curly quotes, curly
  apostrophes, em dash, en dash), in every mode, using a list identical to
  `caption_check.BANNED_PUNCT` minus the semicolon.
- New `--render-dir` mode lints the RENDERED text nodes out of
  `render_report.json` rather than HTML source, so an entity (`&rsquo;`) or an
  escape is caught in the form the reader actually sees. It also applies the
  existing prose-colon rule to on-slide strings, which brand.yaml already bans
  and no gate checked.
- Wired into Phase 5 and Phase 7 of the run contract.

**Verification.** Clean on this run's 85 on-slide text nodes, clean on the
committed regression deck's 36, clean on `copy.json`. FAILS a reconstruction of
the exact defect: a planted `didn’t` and `-` in a rendered node produced
`FAIL: slide-02.html: curly apostrophe` + `FAIL: slide-02.html: em dash`, exit 1.
Pre-existing colon behaviour unchanged (fires on a prose colon, still exempts
`4:30` and URLs).

### U2, `variety_check.py` persists the closest pair

The retro is required to name the closest pair. The ranking was printed to the
console and thrown away, so the number reaching this retro was wrong. The JSON
report now carries `closest_pair` and `closest_pairs` (top five), using the same
`layout_iou + image_corr` ranking the console already computed. Report-only. No
threshold, rule or verdict changed.

**Verification.** Re-ran on this run's render: two new keys, `closest_pair` =
`slide-07.html x slide-08.html`, and **every pre-existing field byte-identical**
to the pre-change report, verdict WARN, exit 0. Re-ran on a fresh render of the
whole deck with identical output.

### U3, logged, not redone: the coherence gate's 80-char blind spot

Fixed by the showrunner mid-run in commit 4f76952 (`render.py` text-node report
limit 80 to 600). Logged in `ledger/upgrades.json` for the trail. Confirmed
still in force by a fresh engine-proof render this retro.

### Engine regression evidence (required before any of the above counts)

```
render.py samples/engine-proof/slides  -> 3/3 OK, warnings=0 errors=0
qa.py     samples/engine-proof         -> verdict PASS, 0 fails 0 warns
render.py out/2026-08-15/slides        -> 9/9 OK, warnings=0 errors=0
qa.py     out/2026-08-15/render        -> WARN, per-slide fails/warns identical
                                          to the shipped machine_qa.json
```

### PARKED (dated candidates, not implemented)

- **2026-08-15, tighten the variety pair rule.** A pair currently fails only on
  IoU >= 0.55 AND corr >= 0.86. Slide 07 x 08 sits at IoU 0.657, corr 0.423,
  **palette 0.982** and passes. Proposal for the maintainer, because it is a
  gate tightening and would retroactively fail a shipped deck: add a third fail
  condition on shared scaffold plus shared palette plus moderate correlation.
  Numbers to test it against are in `runs/2026-08-15/variety_check.json`.
- **2026-08-15, coherence numeral noise.** The numeral check warns on the deck's
  own case-file counter ("002") twice per deck, and on correctly-labelled
  modeled figures. Both are noise that trains the crew to skim warnings.
  Candidate: exempt the counter string, and accept an explicit
  "our analysis, not fetched figures" label on the same slide as satisfying the
  numeral. Needs a design decision, not a patch.
- **2026-08-15, typography finding, no code.** The house rule "straight quotes"
  cannot be judged by eye. The body face draws U+0027 as a curved typographic
  apostrophe while the mono face draws it straight, so one slide shows both
  shapes with identical source bytes (verified: `slide-08.html` contains
  `winter's`, `Wilson's`, `owner's` all as U+0027, zero curly characters).
  A pixel critic must report a suspected curly quote as a question, and
  `style_lint --render-dir` is the answer.

**Not attempted, and the honest reason.** The run's biggest schedule risk is the
bank's cost-gate starvation, and no bounded script fixes it. What actually
mitigates it is knowing which grounds disclose price, which is why the whole of
section 4 went into the knowledge base instead of into code.

---

## 4. KNOWLEDGE BASE APPENDS (every entry names its URL)

- `kb/HUNTING_GROUNDS.md` gets the one-half-each structural finding; the operator
  podcast promoted to first stop for cost-gated restocks; domain-constrained
  search as the only technique that produced leads; `r.jina.ai` past the 403
  wall; the NIST MEP faceted search and the finding that the ground is barren
  (3 AI stories in 1,067, none from 2026); the association-then-local-news
  two-step proven on Coldwater; EDGAR full-text as JSON; the blocklist and the
  confirmed-working list; the grounds to stop funding.
- `kb/EVIDENCE.md` gets the fetch-layer fabrication hazard and the mitigation that
  worked; SEO poisoning of operator cost language; read the verbs; the inverse
  relationship between the agentic label and the presence of a measured number;
  containment versus resolution in voice AI.
- `kb/ECONOMICS.md` carries 8,000 dollars a month for the displaced answering service
  (and the scouting rule it implies: hunt the price of what the AI replaced);
  248,000 dollars over five years for a municipal computer-vision inspection
  contract; the corrected yield order for where cost gets disclosed.
- `kb/AI_LANDSCAPE.md` gets the trades adoption numbers, the 41 percent
  after-hours booking figure, and where the rung 4 / rung 5 line sits in voice.
- `kb/DEPLOYMENT_PATTERNS.md` gets the after-hours front office as a named pattern,
  with the number to demand from it; and the operator-volunteered confound as a
  quality signal.

---

## 5. VARIETY RETRO EVALUATION

### The numbers, and the trend

| Measure | Rejected deck (the reason the engine exists) | 2026-08-15 | Gate |
|---|---|---|---|
| Median image correlation | 0.978 | **-0.005** | fail at 0.70 |
| Median layout IoU | 0.565 | **0.477** | fail at 0.50, warn at 0.38 |
| Value arc | 0.059 | **0.756** | fail under 0.12, warn under 0.22 |
| Closest pair | every pair | **07 x 08**, IoU 0.657 / corr 0.423 / palette 0.982 | fail at IoU 0.55 AND corr 0.86 |

Image sameness is solved and not close: -0.005 median is nine slides that share
no picture at all. The value arc is enormous. **Layout is the measure still
under strain**: 0.477 is only 0.023 under a hard fail, eleven pairs warn for a
shared text scaffold, and it took two rounds of recomposition to get there.

### The closest pair, by eye

Slide 07 (WHAT IT TOOK) and slide 08 (YOUR VERSION), viewed full size. They are
**genuinely two ideas**: 07 is a two-column head-and-body split over a hardware
panel diagram with three unlit dials; 08 is a single centred plate over a
particle field with a dashed rule at the foot. Neither was built from the other.
What they share is real, though, and the numbers see it: both are the deck's
most copy-dense slides, both stack a plate over art, and their palettes are 0.98
alike. The honest name for the similarity is **copy volume dictating layout**,
not template reuse. It is also where the deck's worst craft defect sits, already
recorded in FIELD_NOTES: on slide 08 the plate covers most of the particle
field, and the copy was kept rather than the art, deliberately.

### Cross-run drift

Measured against the stored fingerprints of 2026-07-25 (the rejected deck, the
only prior run with fingerprints): **maximum correlation 0.504, median 0.278**,
against a warn line of 0.80. The single closest resemblance is this deck's
slide 01 against that deck's slides 03, 04 and 09, all around 0.50, and the
measure it resembles them on is the dark full-bleed hero with type knocked into
the shadow. Worth naming early: **the dark hero opener is becoming the house
opener.** Two runs is not a rut, three is. The next run should open somewhere
else.

### The reuse honesty question, answered plainly

**No slide in this deck was built by copying another slide in this deck.** But
slides 5, 7 and 8 were recomposed specifically to move the median, across two
rounds, and that deserves a straight answer rather than a green tick.

The recompositions were real work, not recolours: the headline moved to the
bottom on 5, the body moved to a right-hand column on 7, the centre column was
narrowed on 8. Those are different compositions and the pixels agree. So the
result is **genuine variety, produced under gate pressure rather than by
authorial intent**, which is the gate working exactly as designed, and is not
the same thing as a deck that was various because the story asked for it.

The tell that it was pressure and not intent: the recompositions moved the
MEDIAN (0.52 to 0.477) without separating the actual nearest neighbours. 07 and
08, both recomposed, remain the closest pair in the deck. A deck varied by
intent would have pulled its closest pair apart. This one pulled the middle of
the distribution down.

### Threshold check

- **Nothing fired on something fine.** The 0.50 median-IoU line caught a deck
  that was genuinely leaning on one scaffold, twice, and the fix improved it.
- **Something lazy passed at the pair level.** 07 x 08 at IoU 0.657 with a 0.982
  palette match is the deck's weakest variety spot and no rule touched it,
  because the corr-0.86 arm of the pair rule is built for identical pictures.
  Parked as a maintainer decision above rather than changed here, because
  tightening a fail rule after ship would fail the deck we just shipped.
- **A reporting hole, now closed.** The closest pair was never persisted, and
  the wrong pair reached this retro as a result. Fixed in U2.

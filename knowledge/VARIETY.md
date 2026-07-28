# VARIETY — two engines, and neither one is optional

Read `knowledge/THE_READER.md` first. `DESIGN_DOCTRINE.md` owns the visual
standard. This file owns the standard the maintainer stated in one line:

> **No two run slides should look too similar, no cookie cutter templates.
> Even the slides within one run should each be custom.**

Two engines enforce it. Both are used in pre-planning, both are enforced as
quality gates, and both are evaluated in the retro. The gate is
`scripts/variety_check.py`.

---

## WHY THIS IS A LAW AND NOT A PREFERENCE

Measured on the deck the maintainer rejected, ten slides, all machine gates
green:

| Measure | That deck | What it means |
|---|---|---|
| Median pairwise image correlation | **0.978** | Every slide is the same picture |
| Median layout skeleton overlap | **0.565** | One text scaffold, ten times |
| Value arc (brightest minus darkest) | **0.059** | One brightness end to end |

The reason is easy to name and easy to repeat: a beautiful chassis got built
on slide 1 and then reused, because reusing it was cheaper than composing
again. Every slide was individually good. The deck was a template.

**A chassis is a tool for making one slide. It is not a deck.**

---

## ENGINE A — WITHIN THE DECK

**Every slide in a run is its own composition.** Not a variant. Not the same
plane with different ink.

### Declared at pre-planning, in `out/<date>/deck_signature.json`

Written by the treatment-director and showrunner BEFORE any slide code, and
checked with `variety_check.py --plan-only` before a single line of art gets
written. Cheap to fix here, expensive to fix after a render.

```json
{
  "run_date": "2026-08-04", "case_file_no": 3,
  "deck": {
    "hero_structure": "...", "atmosphere": "...", "depth_technique": "...",
    "line_voice": "...", "continuity_device": "...", "hook_archetype": "...",
    "palette_family": "...", "type_pairing": "...", "narrative_structure": "...",
    "render_ladder_top": "akthree"
  },
  "slides": [
    {"n": 1, "mode": "OBJECT", "layout_family": "full-bleed hero, type knocked into the shadow",
     "art_system": "akthree PBR dispatch board", "value": "dark", "temperature": "warm",
     "custom_note": "one sentence naming what makes this slide unlike every other slide here"}
  ]
}
```

### The rules, all machine-enforced

1. **Mode cap.** Six compositional modes (SCENE, OBJECT, DOCUMENT, DIAGRAM,
   DATA, FIELD). None used more than three times. Adjacent repeats warn.
2. **No repeated mode + layout family pair.** Two slides sharing both are the
   same template with different words, by definition.
3. **Distinct layout families** for at least 70 percent of slides.
4. **No reused art system.** Each slide's art is built for that slide.
5. **A custom note per slide.** One sentence, at least six words, naming what
   makes this slide unlike the others. Writing it is the point. If it cannot
   be written, the slide is not custom.
6. **A declared value arc.** More than one brightness in the deck.
7. **The render ladder is climbed.** `render_ladder_top` must be `akthree` or
   `aksdf` (DESIGN_DOCTRINE section 2).

### The rules, measured on pixels after every render

Labels can be gamed. Pixels cannot.

- **Pairwise:** a pair fails on layout-skeleton overlap at or above 0.55 AND
  image correlation at or above 0.86. Either alone warns, because a shared
  scaffold with genuinely different art is a legitimate series device and
  identical art under different scaffolds is not a template.
- **Deck sameness:** median image correlation must stay under 0.70 and median
  layout overlap under 0.50. A median cannot be fixed by making one outlier
  slide, which is exactly why it is the number that matters.
- **Value arc:** brightest minus darkest mean luminance of at least 0.12, and
  under 0.22 warns. A deck at one brightness is the uniform deck.

---

## ENGINE B — ACROSS RUNS

**No run looks like a previous run.** The series should read as one voice and
never as one layout.

### Declared divergence, against `ledger/artwork.json`

Each field must differ from the last N runs:

| Field | Must differ from last |
|---|---|
| hero_structure | 4 runs |
| atmosphere | 3 |
| depth_technique | 3 |
| hook_archetype | 3 |
| palette_family | 3 |
| continuity_device | 2 |
| type_pairing | 2 |
| narrative_structure | 2 |
| render_ladder_top | 2 |
| line_voice | 2 |

### Pixel divergence, against `ledger/fingerprints.json`

Every slide of the new deck is correlated against every stored slide
fingerprint from the last four runs. At or above 0.90 is a FAIL, at or above
0.80 a warning. This is the backstop that cannot be satisfied by writing
different words in the signature.

The retro records the run with `variety_check.py --record`, which is what
makes the NEXT run have to diverge from this one. **A run that does not record
its fingerprints has broken the engine for every future run.**

---

## WHERE THE ENGINES RUN

| Phase | Command | On failure |
|---|---|---|
| Pre-planning, after the directors room | `--plan-only` | Re-pitch the deck before writing art. Cheapest possible fix. |
| After every render pass | full check | Recompose the offending slides. Not a recolour. |
| Before ship | full check, must be green | No override exists. |
| Retro | `--record` plus the evaluation below | Findings go to `knowledge/FIELD_NOTES.md` |

---

## THE RETRO EVALUATION

Every run's retro answers these in writing, in the run report:

1. **The numbers.** Deck median image correlation, median layout overlap,
   value arc, and the closest pair. Trend them against previous runs.
2. **The closest pair, by eye.** Look at the two most similar slides on the
   contact sheet. Were they genuinely two ideas, or one idea rendered twice?
3. **Cross-run drift.** Which previous run does this one most resemble, and on
   which measure? Naming it early is how a house style stops becoming a rut.
4. **The reuse honesty question.** Was any slide built by copying another
   slide in this deck? If yes, that is the finding, whatever the numbers said.
5. **Threshold check.** Did any threshold in `variety_check.py` fire on
   something that was genuinely fine, or pass something that was genuinely
   lazy? Tune it, log the change in `ledger/upgrades.json`.

---

## WHAT VARIETY IS NOT

- **Not inconsistency.** The brand marks, the counter, the voice and the
  honesty grammar are constant. Composition is what varies.
- **Not novelty for its own sake.** A weird slide that serves no story point
  is a different failure with the same cost.
- **Not a licence to abandon a good idea mid-deck.** Continuity devices are
  required (DESIGN_DOCTRINE section 10). A motif that evolves across slides is
  variety. A plane that repeats across slides is a template.

The line between them: **does slide N exist because the story needed this
composition, or because slide N-1 already had one that worked?**

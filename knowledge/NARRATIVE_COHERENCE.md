# NARRATIVE COHERENCE — one idea, eight slides, no chop

Read `knowledge/THE_READER.md` first. `CASE_CRAFT.md` owns the story grammar.
This file owns whether the story SURVIVES the build.

The gate is `scripts/coherence_check.py` and the `flow-critic` agent. Both run
after **every** render pass, not once at the end.

---

## THE FAILURE THIS EXISTS TO STOP

The deck is written once and then edited fifteen times. A collision fix needs
40px, so a body paragraph gets cut. A headline runs four lines, so a clause
gets trimmed, and the clause happened to be the one naming the ladder rung. A
label overlaps, so it moves to another slide. Every one of those edits passed
the gate it was made for.

Then the deck ships and it is ten correct slides that no longer carry one
thought.

This is documented, not hypothetical. From the last run's own score report:
*"slide 6 lost its entire body paragraph in the collision fix and now carries
statistics with no prose."* Slide 4 lost the phrase "On the feasibility
ladder" to a word-count trim, which is the entire curriculum payload of that
slide, removed to fix a layout problem.

**Layout problems are never solved by deleting copy.** That is the law this
whole file exists to state.

---

## THE FOUR RULES

### 1. The copy record is the story of record

`copy.json` holds every authored string, per slide, with the slide number on
it. Slide HTML is a *rendering* of that record. The record is the truth.

If a string is on a slide, it is in the record. If a string leaves a slide, it
leaves the record too, deliberately, by the copywriter, with a reason. Nothing
disappears because a div was in the way.

`coherence_check.py` diffs the render against the record every pass. A missing
authored sentence is a FAIL.

### 2. When copy and layout collide, layout yields

The permitted moves, in order:

1. Re-lay the slide. Give the text more room. Move the art.
2. Change the composition. A different mode may hold this copy better.
3. Split across two slides, and update the record and the contract.
4. **Only then**, and only by the copywriter, rewrite the copy to be shorter
   while preserving every load-bearing element, and update the record.

The forbidden move is deleting a sentence inline in the HTML because the box
overflowed. That edit is invisible to everything except this gate.

### 3. Every slide opens a loop and pays one

`out/<date>/coherence.json` is the deck's through-line contract, written at
storyboard time, before any slide code:

```json
{
  "thesis": "One sentence the entire deck argues.",
  "slides": [
    {"n": 1, "role": "COVER", "promise": "what this makes the reader want to know",
     "pays": null},
    {"n": 2, "role": "THE COMPANY", "promise": "...", "pays": 1}
  ]
}
```

Enforced mechanically: every slide after the cover names an earlier slide it
pays off, every loop a slide opens is closed by a later slide, and the three
uncuttable roles (RECEIPTS, WHAT IT TOOK, YOUR VERSION) are present.

The contract is not paperwork. It is the object the flow-critic reviews the
deck against, and the reason a reordered deck cannot silently break.

### 4. The through-line is one sentence, and it is the same sentence at the end

The thesis is written before the deck and re-read after the last fix pass. If
the finished deck argues something narrower, wider, or simply different from
the sentence written at storyboard time, the deck changed under the crew
without anyone deciding to change it. Either update the thesis deliberately or
put the deck back.

---

## WHAT MAKES A DECK CHOPPY (the flow-critic's list)

Machines catch removals. These need eyes.

- **Dangling reference.** A slide that opens on "this", "that number", "they",
  "as we saw". Fine when the previous slide is right there in the reader's
  head, fatal after a reorder, and a coin flip in between. Name the thing.
- **Orphaned setup.** Slide 3 says "there were three problems" and the deck
  only ever addresses two.
- **Restated payoff.** The same number lands twice with the same framing. The
  second landing steals the first one's weight.
- **Tonal jump.** Six slides of dry operator voice and then one slide of
  marketing. The seam is visible even when the sentence is fine.
- **Vocabulary drift.** The bottleneck is "the bid queue" on slide 3, "the
  estimating backlog" on slide 5, "quoting" on slide 7. Pick one name and hold
  it for the whole deck.
- **Unit drift.** Hours on one slide, minutes on the next, per week here and
  per visit there. This is how the last run turned into a methods seminar.
- **A slide that could be removed with no loss.** If the deck reads exactly as
  well without it, it was decoration.
- **A slide that could be reordered with no loss.** Sequence should be load
  bearing. If slides 4 and 6 swap freely, neither is doing narrative work.

---

## THE RE-READ, and it is not optional

After the FINAL fix pass, someone reads the deck start to finish as one
document, out of the slide editor, from the contact sheet and the PDF.

Not "does each slide pass its checklist." **Does this still say one thing.**

Three questions, answered out loud:

1. What is this deck's one sentence, read from the deck alone, without looking
   at the contract? Does it match the contract?
2. Where does it stutter? Name the exact seam.
3. If I removed slide N, what would be lost? If the answer is "nothing" for
   any N, that slide is not finished.

A deck that passes every machine gate and fails the re-read does not ship.

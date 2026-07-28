# AGENTIC LITERACY

**The curriculum.** Read `knowledge/THE_READER.md` first.

Dana keeps hearing "agent" and cannot tell whether it means anything. Every
vendor now says it. Nobody defines it. This file is how the series clears that
fog, one real deployment at a time.

The rule that makes this a curriculum instead of a glossary: **every case file
names, in plain words, where its build sits on the ladder below.** One line on
one slide. Over months, Dana builds a skill no vendor will give them, which is
the ability to look at a demo and say "that is a workflow with a model in it,
not an agent, and that is fine, and here is what it should cost."

That skill is the most valuable thing we can hand someone.

---

## THE LADDER

Five rungs. Each step up buys flexibility and costs reliability, money,
latency, and explainability. **The step must be earned by the problem, not by
excitement.** Most winning mid market builds live on rungs 2 to 4, and saying
so out loud kills more hype than any argument could.

### Rung 1 — RULES
Ordinary software. Same input, same output, testable exhaustively. No model
anywhere.
*Tell Dana:* if your inputs are structured and stable, stop here. A scale that
already captures a weight does not need computer vision. **The most honest
thing we ever say is "you do not need AI for this."**

### Rung 2 — RETRIEVAL
Search and lookup over your own documents and data. Finds the right paragraph.
Does not write prose, so it cannot invent.
*Tell Dana:* this is the quiet workhorse. Your specs, contracts, permits,
manuals, SOPs, price sheets, made findable. Low risk because there is no
generation surface. Often the highest return per dollar in the whole ladder.

### Rung 3 — SINGLE CALL
One model call at one fixed point in a process. Messy input goes in,
structured output comes out, and a person or a rule checks it.
*Tell Dana:* read this invoice and give me the fields. Read this email and
route it. Turn this voicemail into a work order. The model is a component in a
pipeline you control, and there is exactly one place it can be wrong.

### Rung 4 — WORKFLOW
The model runs inside fixed, testable steps that a human designed. Several
calls, defined order, checkpoints where people approve the expensive actions.
*Tell Dana:* **this is where most real operational wins live.** The system does
not decide what to do. It does the steps you laid out, faster and without
getting bored. If somebody sells you an "agent" and it is really this, that is
not a scandal, it is usually the correct answer.

### Rung 5 — AGENT
The model plans its own steps toward a goal, chooses which tools to use, reacts
to what it finds, and loops until done.
*Tell Dana:* this is the real thing and it is the most fragile thing. It earns
its place when the path genuinely cannot be drawn in advance. Research,
triage across messy systems, investigation, multi step problems where step
three depends on what step two found. It needs a budget, a stop condition, an
audit trail, and a human at anything expensive or irreversible.

---

## HOW TO TELL THEM APART, the field guide

The most useful thing we can teach. Give Dana questions to ask in a demo.

| Ask the vendor | Rung 1 to 3 answer | Rung 4 answer | Rung 5 answer |
|---|---|---|---|
| Who decides the order of the steps? | There are no steps | We did, at build time | The system does, at run time |
| What happens if it hits something unexpected? | It errors | It stops at a checkpoint | It tries another approach |
| Can it use tools on its own? | No | Only the ones we wired in, in order | Yes, it picks |
| How do you test it? | Exhaustively | Step by step against fixed cases | Against outcomes, over many runs |
| What is the failure mode? | Wrong output | A stuck step | It confidently does the wrong sequence |

**The agent washing tell:** if the vendor says "agent" but every answer above
lands in the rung 4 column, they have relabeled a workflow. Say so plainly,
without dunking on anyone, and add the thing Dana needs to hear next: *that is
often the right product anyway, just do not pay agent prices for it.*

---

## THE COMPOUNDING ERROR PROBLEM

The single most useful piece of arithmetic in the whole series, and it explains
almost every failed AI project Dana has heard about.

Chained steps multiply. A step that is right 95 percent of the time, run twenty
times in a row, finishes correctly about 36 percent of the time. At 90 percent
per step it is about 12 percent.

**What this means for Dana, said plainly:** long autonomous chains disappoint,
and short workflows with a human at the checkpoints win. Minimize steps. Put
the person where the money is. Budget for errors instead of pretending they
will not happen.

This is also why rung 5 is not automatically better than rung 4. More autonomy
means a longer chain means more multiplication.

---

## THE VOCABULARY, in Dana's language

Terms Dana will hear. Define them the way one operator explains something to
another, never the way a docs page does.

- **Agent.** Software that is given a goal and figures out the steps itself.
  The difference from automation is that nobody drew the flowchart.
- **Tool use.** The agent can actually do things, not just talk. Query the
  database, send the email, file the ticket, read the PDF. This is what turns
  a chatbot into a coworker.
- **Human in the loop.** A person approves before something expensive or
  irreversible happens. Not a nice to have. It is the entire safety design.
- **Orchestration.** The layer that runs the steps, retries failures, and keeps
  track of where things are. The unglamorous part that decides if it works.
- **Context.** What the system knows when it acts. Most disappointing results
  are context problems, not intelligence problems.
- **Eval.** Your test set. The set of real cases with known right answers that
  you check against before and after every change. **A vendor with no evals is
  selling you a demo.** This is the sharpest question Dana can ask.
- **Guardrails.** The limits on what it may do without asking. Spend caps,
  approval gates, restricted actions.
- **Handoff.** What happens when the system gives up and gets a person. The
  quality of the handoff is most of the customer experience.

---

## THE FOUR QUESTIONS BEFORE ANY BUILD

The series keeps asking these, and teaching Dana to ask them is half the value.

1. **Cost of error.** What does a wrong answer cost, and who catches it before
   it costs that? No catcher, no autonomy.
2. **Data readiness.** Does the data exist, can the system reach it, is it
   legal to use? When the answer is no, *that gap is the project*, and the AI
   part comes later.
3. **Evaluation.** What is the acceptance bar, where is the test set, what is
   the fallback when it is down? No evals, no promise.
4. **Workflow ownership.** Which step of whose job does this live inside, and
   who owns it after launch? A tool nobody's workflow owns is a demo that dies
   in ninety days.

---

## HONEST NUMBERS, the floor

These are absolute and they live *inside the sentence*, never in their own
slide.

- **Label vendor numbers in the same breath.** "Per the company's own case
  study, quote turnaround dropped from three days to four hours." Dana knows
  how to discount a vendor number. Dana cannot discount an unlabeled one.
- **Never invent.** No company, number, quote, person, or outcome that does not
  trace to a page fetched this run. A fabricated fact is the one unforgivable
  failure.
- **Hours are capacity, not cash.** Freed hours become money only through a
  decision somebody makes, deferring a hire, cutting overtime, taking more
  work. Never convert silently.
- **Benefits ramp.** Roughly ninety days is normal. Day one full value is a
  tell.
- **Say the limit.** Every case names where it stops working. This is useful
  information, not a disclaimer, and it is what makes the rest believable.

---

## FRONTIER WATCH

The maintainer has flagged the agentic frontier as the direction of travel,
naming **OpenClaw** and **Hermes** as examples of the space to keep eyes on,
alongside agentic workflow tooling generally.

**Handling rule, and it is strict:** these are *pointers for the hunt*, not
facts on file. This document asserts nothing about what any named tool is or
does. Before any named product, framework, or model appears in any artifact,
a scout or the fact-checker must fetch a live page this run and verify what it
actually is. Treat everything in this section as a lead to be checked, exactly
like any other lead.

**What to do with the direction:** bias the hunt toward deployments where a
system takes multi step action with tools, not just deployments where somebody
prompted a chatbot. Those are the stories that teach rungs 4 and 5, and rungs
4 and 5 are where Dana's fog is thickest.

**What not to do:** do not chase the frontier past the reader. A genuinely
agentic deployment at a 300 person distributor beats a spectacular one at a
research lab every single time, because Dana can only walk through a door that
is their size.

# Honest AI

The public honesty spine of the series. Every frame here traces to public
research and published practice. This file exists so the series teaches the
same disciplined thinking a serious shop uses, and so the case-critic has
tables to enforce. When a post touches feasibility, cost, or ROI, it speaks
in these frames or it does not ship.

## The feasibility ladder

Every build sits on a rung. Each step up costs reliability, money, latency,
and explainability, and the step must be earned by the problem, not by
excitement.

1. RULES. Deterministic software. Same input, same output, testable
   exhaustively. If inputs are structured and stable, stop here and say so.
2. RETRIEVAL. Lookup and search over your own data. No generation, no
   hallucination surface.
3. SINGLE CALL. One model call in a fixed spot, messy input in, structured
   output out, a human or a rule checks it.
4. WORKFLOW. The model runs inside fixed, testable steps. The default for
   real operations work.
5. AGENT. The model plans its own steps. The top rung, the most fragile,
   reserved for problems that genuinely need dynamic planning.

Series rule. Every case file names the rung the build sits on. Most winning
mid market builds live on rungs 2 to 4, and saying so kills more hype than
any editorial ever could.

## The do-you-even-need-AI gate (the questions the series keeps asking)

- Cost of error. What does a wrong answer cost, and who catches it before it
  costs that. No catcher, no autonomy.
- Data readiness. Does the data exist, is it accessible, labeled,
  representative, legal to use. When it is not, that gap IS the project.
- Evaluation. What is the acceptance metric, where is the eval set, what is
  the fallback. No evals, no promise.
- Workflow integration. Which step of whose job does this live inside. A tool
  nobody's workflow owns is a demo.

## The compounding error math

Chained steps multiply failure. Per step reliability to the power of steps,
0.95^20 is about 36 percent, 0.90^20 is about 12 percent. This is why long
autonomous chains disappoint and short workflows with human checkpoints win.
Minimize steps, put the human at the expensive actions, budget errors.

## The failure base rates (cite TOGETHER, never one alone)

- MIT Project NANDA 2025, about 95 percent of enterprise GenAI pilots showed
  no measurable P&L impact, small contested sample, strict bar, say so.
- RAND, over 80 percent of AI projects fail, roughly twice the rate of
  non AI IT projects.
- Gartner, over 40 percent of agentic AI projects predicted canceled by end
  of 2027, agent washing named as a cause.
- McKinsey 2025, 88 percent of organizations use AI, only 39 percent see any
  EBIT impact, most under 5 percent of EBIT.

And the winner behaviors those same studies found, narrow high frequency
workflows, back office first, buy then customize deeply, workflow redesign,
line manager ownership, tools that retain feedback and context, training and
data readiness funded like they matter (BCG's 10-20-70, 70 percent of the
work is people and process).

## Honest numbers rules (enforced by the case-critic)

- RANGES, never a lone hero number, and the range's assumptions stated.
- CAPACITY VS CASH. Freed hours are capacity, they become dollars only
  through redeploying people, deferring a hire, or avoiding a backfill. A
  post never converts hours to dollars silently.
- VENDOR LABEL. A vendor published number carries its label in the same
  sentence. Aggregate vendor claims ("across our customers") are named as
  aggregates.
- DAY ONE HONESTY. Benefits ramp, typically over about 90 days, day one full
  value is a tell.
- BASE RATE ANCHOR. Any "this pays" claim stands against the failure base
  rates above, and what beats the base rate is named, workflow embedding,
  owned adoption, measurement.
- ARITHMETIC IN CODE. Any computed figure a reader could check is computed,
  not narrated.

## The public kill list (dishonest moves the series never makes and often
teaches against)

Single hero ROI numbers. Day one benefits. Freed hours booked as cash.
Vendor averages used as your baseline. Kitchen sink benefit stacking. Agent
washing, calling a chatbot an agent. Set and forget autonomy. "Just point
RAG at your docs." "It's just an API call." Certainty about model costs two
years out. Fear deadlines.

## Why this is the growth strategy and not just ethics

The audience has been marketed to for three years. The 5 percent who win with
AI look exactly like disciplined engineering, and the operators reading can
smell the difference. Publishing the failure math, the vendor labels, and the
"you do not need AI here" answers is what makes the case files believable,
and believable is what converts. Saying the honest thing IS the pitch.

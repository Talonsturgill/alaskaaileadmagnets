# AI LANDSCAPE — what the technology actually is, in capability tiers

Read `README.md` in this directory first. Everything here is a PRIOR, written
from model training and past runs, and this is the file in the knowledge base
that goes stale fastest. **No product, model, capability or price statement
here may appear in an artifact without a page fetched this run.**

Written in capability tiers rather than brand names on purpose. Brands change
quarterly. The tiers have been stable for years and they are what actually
determines whether a build works.

---

## THE SHAPE OF THE FIELD, for an agent that has to reason about it

**Frontier models** are general-purpose systems from a small number of labs,
sold through APIs and through chat products. They are the substrate almost
everything else sits on. Capability rises and per-token price falls on a
cadence measured in months, which is why any cost or capability claim older
than about a year is untrustworthy for planning.

**Small and open-weight models** run cheaply, sometimes locally, and are
genuinely good enough for narrow, well-defined tasks. They matter to Dana for
two reasons: cost at volume, and data residency when the data cannot leave the
building.

**The application layer** is where Dana actually buys. Vertical software that
embeds a model into a specific job — the scribe, the estimator, the dispatch
assistant. Dana almost never buys a model. Dana buys a product with a model
inside it, and that is the correct thing to do.

**The plumbing layer** is orchestration, retrieval, evaluation, observability,
and tool-connection standards. Invisible to Dana and it determines whether the
product works. When a deployment succeeds or fails for reasons the story
cannot explain, the answer is usually here.

---

## WHAT THESE SYSTEMS ARE ACTUALLY GOOD AT

Stated as capabilities, because this is what maps onto bottlenecks.

**Reliably good, at production quality:**
- Turning messy unstructured input into structured fields
- Summarising and rewriting text between registers
- Classification and routing against a defined taxonomy
- Retrieval over a corpus with citation back to the source
- Drafting a first pass that a knowledgeable person edits
- Transcription, and translation between major languages
- Writing and modifying code against a test suite

**Good with a human at the checkpoint:**
- Multi-step tasks with a fixed, designed sequence
- Extraction where the cost of an error is real money
- Anything customer-facing where tone carries risk
- Ranked triage that decides what a person looks at first

**Genuinely hard, and where projects break:**
- Long autonomous chains. Arithmetic, not opinion: twenty steps at 95 percent
  each finishes correctly about 36 percent of the time.
- Anything requiring facts not in the context. Most disappointing results are
  context problems, not intelligence problems.
- Precise numerical work without a tool doing the actual computation
- Domain judgement with no examples to learn from
- Knowing what it does not know. Confident wrongness is the default failure
  mode and it is why the human-in-the-loop design exists.

**The practical rule this yields:** put the model where messy input becomes
structured output, and put a person where money or commitment happens.

---

## THE VOCABULARY THAT MATTERS, and what is underneath it

`knowledge/AGENTIC_LITERACY.md` owns how to explain these to Dana. This is the
engineering reality behind them, so the crew is not explaining something it
does not understand.

- **Context window.** How much the system can hold at once. It got large
  enough that "it cannot see the whole document" stopped being the usual
  constraint. Retrieving the *right* material is still the constraint.
- **Retrieval.** Fetching relevant material into the context before answering.
  Cheap, low risk, and the highest return per dollar in most mid-market
  deployments, because there is no generation surface to invent from.
- **Tool use / function calling.** The model calls software: query the
  database, send the email, file the ticket. This is the capability that turns
  a chat product into something that does work. Everything at rungs 4 and 5
  depends on it.
- **Tool-connection standards.** There is now an ecosystem of standard ways to
  expose a company's systems to a model rather than hand-wiring each one. This
  is why "connect it to our systems" got cheaper. It is also where security
  review belongs, because a connected tool can act.
- **Orchestration.** The layer running the steps, retrying, and tracking
  state. Unglamorous and decisive.
- **Evaluation.** A held-out set of real cases with known right answers,
  checked before and after every change. **A vendor with no evals is selling a
  demo.** This is the sharpest single question Dana can ask.
- **Guardrails.** Spend caps, approval gates, restricted actions, stop
  conditions. For anything autonomous these are the design, not a feature.
- **Fine-tuning.** Adapting a model on your own examples. Much less often the
  answer than vendors imply. Retrieval plus a good prompt usually beats it,
  costs less, and is easier to change.
- **Multimodality.** Images, audio and documents in, not only text. This is
  what made inspection, field-report-from-voice, and document intake work
  outside of pilots.

---

## WHAT ACTUALLY CHANGED RECENTLY, and what did not

**Changed.** Tool use got reliable enough for production. Cost per unit of
capability kept falling fast. Small models got good enough for narrow jobs.
Connecting a model to a company's systems stopped being custom engineering
every time. Genuinely agentic products shipped in real categories, coding
being the best evidenced.

**Did not change.** Compounding error still punishes long chains. Data
readiness is still the hidden project. Change management still decides
outcomes. A tool nobody's workflow owns still dies in ninety days. The four
questions in `AGENTIC_LITERACY.md` still separate the projects that work from
the ones that do not.

**Why this matters for the hunt:** the durable teaching is in the second list.
The first list is why 2024-or-later evidence is required — economics from
before then would misprice a decision made now.

---

## FRONTIER WATCH, and the handling rule

The maintainer has flagged the agentic frontier as the direction of travel,
naming **OpenClaw** and **Hermes** as examples of the space to watch, along
with agentic workflow tooling generally.

**The rule is strict and it is the same rule as everything else in this
directory.** These are pointers for the hunt, not facts on file. This document
asserts nothing about what any named tool is or does. Before any named
product, framework, or model appears in any artifact, a scout or the
fact-checker fetches a live page this run and verifies what it actually is.

**What to do with the direction.** Bias the hunt toward deployments where a
system takes multi-step action with tools, not toward deployments where
somebody prompted a chatbot. Those teach rungs 4 and 5, and that is where
Dana's fog is thickest.

**What not to do.** Do not chase the frontier past the reader. A genuinely
agentic deployment at a 300 person distributor beats a spectacular one at a
research lab every time, because Dana can only walk through a door their size.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro, with the URL that established
each entry. This file goes stale fastest, so corrections here are worth more
than anywhere else in the knowledge base.)*

- 2026-08-15 (case file 2, retro scan): **adoption in the trades is broad and
  shallow, and it is size-blind.** A Housecall Pro survey of over 400 US home
  service contractors found "over 70% have tried AI tools" with "about 40% now
  using AI actively in their businesses", and, the line that matters for our
  reader, "From solo owner-operators to 50+-person companies, small shops are
  embracing AI nearly as much as large ones." The named uses are "automating
  marketing, customer service, scheduling and paperwork", not field work.
  Source: https://www.pmmag.com/articles/106575-70-of-home-service-professionals-now-use-ai-to-cut-admin-work-not-field-jobs-housecall-pro-report-finds
  (Housecall Pro's own page states it as "In 2025, over 70% of Pros in Housecall
  Pro's survey reported using AI tools, with nearly 40% actively using AI in
  their business",
  https://www.housecallpro.com/resources/field-home-service-industry-trends/ ).
  Vendor-run survey of its own customer base, so label it that way and never use
  it as a fear line. It is useful as scale-orientation: Dana is not late.
- 2026-08-15 (case file 2, retro scan): a platform-data number worth holding for
  any after-hours story, from Housecall Pro's own booking data: "Across jobs
  booked online on Housecall Pro, 41% come in after hours when many businesses
  aren't responding actively." Source:
  https://www.housecallpro.com/resources/field-home-service-industry-trends/
  Platform-owner data about its own platform. Verify fresh before it ships.
- 2026-08-15 (case file 2, retro scan): **the voice AI category is where
  agent-washing is thickest right now.** Vendors market "always-on agents" and
  an "AI workforce"; the shipped case's own vendor co-founder is on record that
  the human-in-the-loop hybrid books better than full autonomy, which is a rung 4
  answer. The honest line to teach: a voice system running fixed steps, wired
  into ONE system of record, that stops and hands to a person when a caller gets
  frustrated, is rung 4 and is usually the right buy. Rung 5 would mean the
  system chooses its own steps and tools at run time, and nothing fetched this
  run described that in field service. Source:
  https://www.ownedandoperated.com/post/owned-and-operated-173-we-booked-400-calls-a-week-how-avoca-ai-is-shaping-home-services

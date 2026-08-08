# VENDOR MAP — market structure, and how to reason about a vendor claim

Read `README.md` in this directory first. Everything here is a PRIOR.

**This file deliberately names no vendors.** Not out of caution, but because a
vendor list written from training would be wrong within a quarter and would be
exactly the kind of unverified assertion the whole series exists not to make.
Vendors get named in artifacts only after a scout or the fact-checker fetched
a live page this run and confirmed what the product actually is.

What this file gives an agent instead is durable: the CATEGORIES the market
organises into, what each category tends to be true about, and the questions
that separate a real product from a demo.

---

## THE THREE LAYERS DANA COULD BUY FROM

**1. Vertical applications.** Software built for one industry's one job. The
scribe for clinics, the estimating tool for contractors, the dispatch
assistant for service fleets.
*Tends to be:* the right answer for Dana. Fastest to value, least integration
work, and the vendor already knows the workflow.
*Watch for:* thin wrappers whose entire product is a prompt, and lock-in on
data you will want back.

**2. Horizontal platforms.** General tools configured to a job. Document
processing, workflow automation with model steps, retrieval over a corpus.
*Tends to be:* more work to stand up, more flexible, and cheaper at scale.
Usually needs somebody internal to own it.
*Watch for:* a platform sold as a solution. The platform is real; the solution
is the six weeks of configuration nobody quoted.

**3. Model APIs direct.** Building on a frontier or open model.
*Tends to be:* disqualifying for this series. If the answer required engineers,
Dana cannot copy it. Legal as a labelled mechanism case only.

**The series preference is unambiguous:** bought or configured, not built. That
is what makes a case copyable, and copyable is the whole product.

---

## WHAT A CATEGORY TELLS YOU BEFORE YOU RESEARCH THE VENDOR

Useful priors for orienting fast. Each is a hypothesis to check, not a fact.

- **A category with an obvious system of record** (accounting, EHR, ERP, CRM)
  tends to have both an incumbent shipping an AI feature and startups shipping
  a better standalone version. The incumbent's version integrates and is
  usually weaker; the startup's is stronger and has to integrate. This
  trade-off is worth explaining to Dana, because it is the actual decision.
- **A category where the output is testable** (code, extraction, transcription)
  has better evidence and more honest claims, because customers can measure.
- **A category where the output is subjective** (content, strategy,
  recommendations) has worse evidence and looser claims.
- **A category priced per outcome** has thought harder about what the outcome
  is than one priced per seat. Then check how the outcome is defined.
- **A category with heavy regulation** (health, safety, finance, hiring) moves
  slower, discloses more, and has a real audit trail. Good hunting for
  verifiable stories.

---

## THE QUESTIONS THAT SEPARATE A PRODUCT FROM A DEMO

These are the questions the fact-checker asks of a story and that Dana should
ask in a room. They are also the most valuable thing we can teach.

1. **What are your evals?** A held-out set of real cases with known right
   answers, checked before and after every change. **No evals means a demo.**
   This is the single sharpest question in the file.
2. **Who decides the order of the steps, you at build time or the system at
   run time?** This is the rung 4 versus rung 5 question, and it is how agent
   washing gets caught. See the field guide in `AGENTIC_LITERACY.md`.
3. **What happens when it hits something unexpected?** Error, checkpoint, or
   another approach. The answer names the rung.
4. **What is the failure mode, and who catches it before it costs money?**
   No catcher, no autonomy.
5. **What does it need from our systems, and who does that integration?**
   The answer is where the unquoted cost lives.
6. **How does it handle our data, where does it live, and can we get it back?**
7. **Show me a customer my size in my industry.** If every reference is an
   enterprise, Dana is buying an enterprise product.
8. **What does month three look like, not day one?** Benefits ramp over
   roughly ninety days. Day-one full value is a tell.
9. **What is it bad at?** A vendor with no answer has not deployed enough to
   know, or is not telling you. The good ones answer this well and it is a
   strong positive signal.

---

## AGENT WASHING, and how to correct it without dunking

Everything is called an agent now. Most of it is a workflow with a model in
it, which is frequently the correct product.

**The tell:** the vendor says agent, and every answer to the questions above
lands in the rung 4 column. Fixed steps, designed at build time, stops at a
checkpoint, tested step by step.

**The correction, in the house voice:** name the rung plainly, then
immediately say the useful thing. *"This is a workflow with a model in it, not
an agent. That is usually the right answer for this job. Just do not pay agent
prices for it."*

That sentence does three things at once: it is honest, it is useful, and it
teaches Dana a distinction they can use in the next demo without us. That is
the whole curriculum in one line.

---

## HOW A VENDOR ENTERS AN ARTIFACT

The full path, and there is no shortcut:

1. The vendor appears in a story that passed the qualifying filter
2. A live page is fetched this run confirming what the product is
3. What it actually does is described in plain operator words, not marketing
4. Its ladder rung is named honestly, correcting the vendor if needed
5. Every number attributed to it carries its label in the same breath
6. We name it without fear and without endorsement. We do not sell it, we do
   not compete with it, and saying what it is costs us nothing.

**We are not afraid of naming tools we do not sell.** Refusing to name the
product is how a case file becomes useless: Dana cannot go look at a thing we
would not name.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro, with the URL that established
each entry. Category-level findings belong here. Specific vendor facts do not
live in this file at all: they live in the run's claims.json, verified that
run, which is the only place a vendor fact is ever true.)*

### 2026-08-08 (case file 2, shipped nothing)

**"Who built it" is now the FIRST question, ahead of cost and timeline.**
This is a change to the order of the intake filter and it was earned. Filter 3
kills faster and kills more candidates than filter 5 does, and it kills them
before a scout has fallen in love with the story.

The mechanism, and it is a property of a whole category. **Case study libraries
for self-hostable open-source tools systematically omit who did the building**,
because the vendor's interest is in making it look effortless. The customer is
presented as having configured a product when the actual artefact is a software
project. Field Aerospace self-hosted an open-source workflow engine, then built
a custom React front end and a Node.js backend over it and wired an API
integration to a third-party data service. **No page names who did that work.**
If it took an internal software team, Dana cannot copy it and the case is dead
regardless of what the price turns out to be. One question converts the lead:
*who built the front end, and how long did it take them?*
Source: the n8n case study and the n8n case-study index, fetched by scouts S4
and W2-A on 2026-08-08.

The same category note applies to layer 2 in this file: a horizontal platform
plus a custom front end is layer 3 wearing layer 2's label.

**Two verified agent-washing exemplars, both worth a teaching slide.** These
are the concrete instances the file's agent-washing section has been describing
in the abstract:

- **Choco** brands what the page itself describes as a rung 3 extraction step,
  turning messy inbound orders into structured ones, "OrderAgent" and "AI
  agents". Source: `choco.com`, fetched by scout S4.
- **Kay.ai** brands what reads as rung 4 workflow execution the "first fully
  autonomous AI agent". Source: the Kay.ai / JMG Insurance release, fetched by
  scout S4.

Neither page answers a single field-guide question in the rung 5 column. The
house correction applies unchanged: name the rung plainly, then say the useful
thing. It is usually the right product. Just do not pay agent prices for it.

**A category note on the honest ones.** n8n's own case study for Field
Aerospace calls the build "automation" rather than "agent", which is accurate
and rare. Vendor honesty on the rung is a real positive signal about the vendor
and it costs nothing to notice.

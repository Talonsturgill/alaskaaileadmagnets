# DEPLOYMENT PATTERNS — the shapes real mid-market AI wins come in

Read `README.md` in this directory first. Everything here is a PRIOR. Nothing
here is citable. Verify before it touches an artifact.

This is the most useful file in the knowledge base for the hunt. It converts a
vague brief ("go find an AI win") into a concrete one ("go find one of these
shapes, at 50 to 1,000 employees, with a disclosed cost and a named human").

Each pattern carries: the bottleneck in operator language, the honest ladder
rung, the shape of the build, what it typically costs and how long it takes,
the failure mode, and **what to verify** before it can ship. The cost and time
bands are priors for orientation and for smelling a wrong number. They are
never a figure that goes on a slide.

Ladder rungs are defined in `knowledge/AGENTIC_LITERACY.md`: 1 RULES,
2 RETRIEVAL, 3 SINGLE CALL, 4 WORKFLOW, 5 AGENT.

---

## HOW TO USE THIS FILE

**Scouts:** these are search targets, not a checklist. Search the pattern's
operator language, not "AI case study." An estimator who cut bid turnaround
does not describe themselves as an AI adoption success story.

**Fact-checkers:** when a claim lands outside the band here, that is a flag to
dig, not a reason to reject. Ask what the number includes. Most wild figures
are real numbers measuring something narrower than the sentence implies.

**Translators:** the "Anchorage read" line on each pattern is the fastest route
from a lower 48 win to a local segment. Segments, never named targets.

**Everyone:** the highest-value patterns for this series are the ones at rungs
4 and 5, because that is where Dana's fog is thickest and where the curriculum
does the most work. A rung 2 win is still shippable when it is a great story,
and saying "this is retrieval, not an agent, and it still paid for itself in
four months" teaches as much as anything.

---

# DOCUMENT AND INTAKE PATTERNS

## P1 — Invoice and AP document intake
**Bottleneck.** Someone keys hundreds of invoices a month by hand, and the
month-end close waits on them.
**Rung.** 3 (single call), often wrapped in a 4 (workflow) for approvals.
**Shape.** Documents land in a queue, a model extracts fields, a rules layer
validates against the PO and the vendor master, exceptions route to a person.
**Typical band.** Low five figures a year at mid-market volume; weeks to
months to working, dominated by ERP integration, not by the model.
**Failure mode.** Extraction accuracy is fine and the exception queue is
unstaffed, so the backlog moves rather than shrinking.
**Verify.** Documents per month before and after, touch time per document,
what share still needs a human, and who works the exception queue.
**Anchorage read.** Any multi-entity operation with a small back office:
contractors, distributors, freight, ANCSA subsidiaries with shared services.

## P2 — Contract, spec and submittal review
**Bottleneck.** A person reads a 200 page spec looking for the clauses that
change the price or the risk.
**Rung.** 2 (retrieval) at the useful floor, 4 when it drafts a summary and
routes it.
**Shape.** The corpus is indexed, questions are asked against it, answers cite
the page. The citation is the whole product.
**Typical band.** Often the cheapest genuinely valuable build in this file.
**Failure mode.** Answers with no page citation. Once a reviewer has to check
every answer manually, the tool costs time instead of saving it.
**Verify.** Review hours per document before and after, and whether the output
cites a locatable page.
**Anchorage read.** Engineering firms, general contractors, anyone bidding
federal or state work with heavy submittal requirements.

## P3 — RFP and bid response drafting
**Bottleneck.** Every RFP re-answers questions the company has already
answered thirty times, and the proposal team works nights before a deadline.
**Rung.** 4 (workflow). A genuine 5 exists when the system decides which past
answers to hunt for and iterates.
**Shape.** A library of past answers, retrieval against the new questions, a
drafted first pass, human editing, and a feedback loop that improves the
library.
**Typical band.** Weeks to stand up on top of an existing answer library;
months when the library has to be built first, and building it is the project.
**Failure mode.** Nobody owns the answer library, it goes stale in two
quarters, and the drafts get worse than writing from scratch.
**Verify.** Proposals per quarter, hours per proposal, win rate if claimed
(and be sceptical of win-rate claims, see `EVIDENCE.md`).
**Anchorage read.** ANCSA subsidiaries, engineering firms, anyone with a
federal contracting practice.

## P4 — Inbound mail, quote request and order triage
**Bottleneck.** A shared inbox where orders, quote requests, complaints and
spam arrive together, and somebody sorts them by hand every morning.
**Rung.** 3 to 4.
**Shape.** Classify, extract the fields, create the record in the system of
record, route the exception. The value is in the record creation, not the
classification.
**Typical band.** Fast to working, and one of the most common genuinely
successful small builds.
**Failure mode.** It handles the 80 percent that was already easy and the hard
20 percent still eats the same person's morning.
**Verify.** Messages per day, time to first response before and after, and
what share auto-completed without a human touch.
**Anchorage read.** Distributors, parts counters, marine and aviation service
outfits, anyone with a quote desk.

---

# FIELD AND OPERATIONS PATTERNS

## P5 — Dispatch and scheduling assistance
**Bottleneck.** A dispatcher holds the whole board in their head, and when
they are on vacation the week goes badly.
**Rung.** 4, occasionally 5 when it re-plans in response to live disruption.
**Shape.** Constraints, skills, locations and priorities in one place;
proposed assignments; the dispatcher approves or overrides. The override data
is the training signal and the political problem at once.
**Typical band.** Longer than people expect. Data readiness (who is certified
for what, which truck has which gear) is usually the real project.
**Failure mode.** The dispatcher does not trust it, overrides everything, and
the tool becomes a screen nobody looks at. This is a change-management
failure, and it is the most common failure in this whole file.
**Verify.** Jobs per day, travel time, overtime hours, and specifically the
override rate. An unreported override rate is the tell.
**Anchorage read.** Mechanical and electrical contractors, service fleets,
home health, anyone with techs in trucks and a whiteboard that matters.

## P6 — Field report and daily log generation
**Bottleneck.** A supervisor writes the same report at 5am, or does not write
it, and the office reconstructs the week on Friday.
**Rung.** 3.
**Shape.** Voice or photo in, structured report out, human confirms and
signs. The signature is what makes it legally usable and operationally
trusted.
**Typical band.** Among the cheapest and fastest wins in this file, and one
that field crews genuinely like, which is rare and worth saying out loud.
**Failure mode.** The report reads generic, so the office stops trusting it
and asks for the old one too.
**Verify.** Reports completed on time before and after, minutes per report,
and whether the office actually stopped chasing.
**Anchorage read.** Construction, utilities, remote site operations, marine
maintenance, anything where the crew is not near a desk.

## P7 — Visual inspection and defect detection
**Bottleneck.** A person looks at every part, weld, panel or fish and decides
pass or fail, and they get tired.
**Rung.** 3, with a rules layer around it.
**Shape.** Camera, model, threshold, and a human on everything near the
boundary. Almost always deployed as a triage that ranks what a human looks at
first, not as a replacement for looking.
**Typical band.** Capital cost in the hardware more than the model. Timeline
dominated by collecting enough labelled examples of the defect, which is hard
precisely because good operations produce few defects.
**Failure mode.** The model is trained on last year's defects and the new
failure mode walks straight past it.
**Verify.** Escape rate, false-reject rate, throughput, and how the model gets
retrained when a new defect appears.
**Anchorage read.** Seafood processing, fabrication shops, aviation
maintenance, utility line inspection.

## P8 — Maintenance triage and work order generation
**Bottleneck.** A machine goes down and the diagnosis lives in one person's
memory and a filing cabinet of manuals.
**Rung.** 2 to 4.
**Shape.** Manuals, past work orders and sensor history made searchable; a
symptom description in; likely causes, the relevant manual pages and a drafted
work order out.
**Typical band.** Cheap when the manuals are already digital. Expensive when
"digitise thirty years of paper" turns out to be step one.
**Failure mode.** Sold as predictive maintenance when it is retrieval over
manuals. Useful either way. Priced very differently.
**Verify.** Mean time to repair, first-time fix rate, and whether the sensor
history is actually being used or is just in the pitch.
**Anchorage read.** Processors, mines, utilities, fleet maintenance shops.

---

# CUSTOMER AND FRONT-OFFICE PATTERNS

## P9 — Call handling and after-hours coverage
**Bottleneck.** Calls come in after hours, or all at once at 7am, and either
an answering service takes bad messages or the phone rings out.
**Rung.** 4, sometimes 5 for genuine multi-step handling.
**Shape.** Voice in, intent classified, routine requests completed end to end,
everything else warm-transferred with context attached. The handoff quality is
most of the customer experience.
**Typical band.** Usage priced, so the bill scales with call volume in a way
seat pricing does not. Model this before signing.
**Failure mode.** Containment rate is reported as a success metric while
customer satisfaction on contained calls goes unmeasured. A call that ends
without resolution counts as contained.
**Verify.** Containment rate AND resolution rate AND what happens on transfer.
Insist on all three.
**Anchorage read.** Service contractors, clinics, property management, tour
operators with a seasonal call spike.

## P10 — Quote and estimate generation
**Bottleneck.** Estimators are the constraint on how much work the company can
bid, and turnaround time loses jobs that were winnable.
**Rung.** 3 to 4.
**Shape.** Requirements in, historical pricing and catalogue retrieved, draft
quote out, estimator reviews and sends. The estimator's edit is the product,
not an inconvenience.
**Typical band.** Highly variable, driven by how clean the pricing data is.
**Failure mode.** Fast wrong quotes. A quote is a commitment; the cost of an
error here is real money, which pins the human firmly in the loop.
**Verify.** Turnaround time, quotes per estimator per week, and the margin on
AI-drafted quotes versus hand-built ones. The margin question is the one
nobody asks and the one that matters.
**Anchorage read.** Mechanical contractors, fabricators, freight and logistics
pricing desks. This is close to the ideal pattern for this series: everyone
recognises the bottleneck instantly.

## P11 — Knowledge assistant for staff
**Bottleneck.** New hires ask the same forty questions, and the person who
knows the answers is the person with the least time.
**Rung.** 2.
**Shape.** SOPs, policies, price sheets and manuals indexed, asked in plain
language, answers citing the source document.
**Typical band.** Usually the highest return per dollar in this file, and the
least exciting to write about, which is a craft problem and not a reason to
skip it.
**Failure mode.** The corpus is out of date, so it confidently quotes a policy
that changed in March. Content ownership is the entire project.
**Verify.** Question volume to the expert before and after, time to competence
for a new hire, and who owns updating the corpus.
**Anchorage read.** Every segment. Especially operations with heavy seasonal
hiring, where the same onboarding happens every single spring.

---

# BACK-OFFICE AND PLANNING PATTERNS

## P12 — Demand and inventory forecasting
**Bottleneck.** Ordering is done on feel, so there is too much of the wrong
thing and not enough of the right thing.
**Rung.** 1 or 2 far more often than anyone admits. Classical statistics
frequently beats a model here, and saying so is exactly the honest teaching
this series exists to do.
**Shape.** History plus signals in, forecast out, a planner adjusts.
**Typical band.** Modest, if the data is clean. It usually is not.
**Failure mode.** A forecast nobody acts on because the planner does not trust
it and has no way to interrogate why it said what it said.
**Verify.** Forecast error before and after, and whether inventory turns or
stockouts actually moved. A better forecast that changed no decision is worth
nothing.
**Anchorage read.** Distributors, retail groups, parts operations, seafood
with brutal seasonality and a shipping lead time that punishes being wrong.

## P13 — Compliance, safety and incident reporting
**Bottleneck.** Reports get written late and badly because writing them is
nobody's favourite hour.
**Rung.** 3 to 4.
**Shape.** Narrative in, structured incident record out, classification
against the regulatory taxonomy, human sign-off. Sign-off is mandatory.
**Typical band.** Moderate. The compliance review of the tool is often longer
than the build.
**Failure mode.** Misclassification that creates a regulatory problem rather
than solving an administrative one. High cost of error means low autonomy.
**Verify.** Reporting lag, completeness, and the classification accuracy
against a human-labelled sample.
**Anchorage read.** Processors, construction, marine, aviation, mining.

## P14 — Recruiting and workforce screening
**Bottleneck.** Six hundred applications for the summer season and two people
to read them.
**Rung.** 2 to 3.
**Shape.** Parse, extract, rank against explicit criteria, human decides.
**Typical band.** Cheap to run and legally the most loaded pattern in this
file.
**Failure mode.** Discriminatory ranking, and a defensibility problem the day
somebody asks how a decision was made.
**Verify.** Time to fill, screening hours, and specifically what audit trail
exists on why a candidate was ranked where they were.
**Anchorage read.** Seasonal operations that triple headcount. Handle with
care and name the legal limit out loud.

---

# THE AGENTIC PATTERNS (rung 5, where the curriculum earns most)

These are the shapes where a system genuinely plans its own steps. They are
rarer, harder to verify, and worth disproportionate hunting effort, because a
verified rung 5 win at 300 employees is the single most valuable story this
series can tell.

## P15 — Investigation and reconciliation agents
**Bottleneck.** Something does not tie out, and finding out why means chasing
across four systems in an order nobody can specify in advance.
**Why it is genuinely rung 5.** Step three depends on what step two found.
That is the actual definition, and it is why this shape cannot be a workflow.
**Shape.** A goal, a set of tools that read the systems, a budget, a stop
condition, and an audit trail of what it checked and concluded.
**Failure mode.** Confident wrong sequences, and a trail nobody can follow to
see where it went wrong. No audit trail, no deployment.
**Verify.** Cases resolved without escalation, time per case, AND the error
rate on a human-audited sample. The third one is the one that gets skipped.

## P16 — Research and monitoring agents
**Bottleneck.** Somebody is supposed to watch competitors, permits, tenders,
regulations or prices and never has time.
**Why it is rung 5.** The path through the sources is discovered, not drawn.
**Shape.** A standing question, tool access to search and fetch, a schedule,
and a written brief with links a human reads.
**Failure mode.** Plausible summaries of pages it did not actually read. Every
claim must carry a link, for the same reason ours do.
**Verify.** What a human does differently because of the brief. If nothing,
it is an expensive newsletter.

## P17 — Multi-system order and case orchestration
**Bottleneck.** One customer request touches five systems and a person is the
integration layer.
**Rung.** 4 when the path is fixed, 5 when it is not. Most vendors call this
5 and most of it is 4, which makes it the best teaching example of agent
washing in the whole file.
**Shape.** Tool use across systems, checkpoints at anything expensive or
irreversible, and a human who can see the whole trail.
**Failure mode.** Compounding error. Twenty chained steps at 95 percent each
finish correctly about 36 percent of the time.
**Verify.** End-to-end completion rate without human touch, and the cost of
the errors that got through.

## P18 — Coding and internal tooling agents
**Bottleneck.** A small IT team, a backlog of small internal tools nobody has
time to build, and a business that routes around the gap with spreadsheets.
**Rung.** 5, and unusually well evidenced because the output is testable.
**Shape.** A goal, a repository, tests, and a human reviewing every change.
**Failure mode.** Volume of unreviewed change. The bottleneck moves to review,
and if review is not staffed the quality falls quietly.
**Verify.** Cycle time on small internal requests, and the review load created.
**Anchorage read.** Any company with two IT people and a hundred spreadsheets.
Dana probably recognises this one instantly.

---

## THE PATTERNS THAT DISAPPOINT (hunt these knowing what you will find)

Worth knowing so a run does not get spent on them, and worth naming to Dana
because knowing what does not work is half of what they came for.

- **The general assistant rollout.** Seats deployed company-wide with no
  workflow attached. Usage looks fine and no operational number moves,
  because no specific job was pointed at.
- **The chatbot on the website with no path to a human.** Deflection metrics
  up, customer satisfaction down, and only one of the two is on the dashboard.
- **The unfocused data lake project** that has to finish before the AI part
  starts. It is a data project. That is fine, and it should be sold as one.
- **The pilot with no owner.** Ninety days of enthusiasm, then the champion
  changes jobs. Look for a named owner in every case, and be suspicious when
  the story cannot produce one.
- **The demo that never left the demo.** If the story cannot name production
  volume, it never reached production.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro. Every entry names the URL that
established it. See `README.md`.)*

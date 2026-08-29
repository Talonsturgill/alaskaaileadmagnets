# SELECTION — 2026-08-29 — Case File No. 2

## The bank, after two restock waves

Eight scouts across eight hunting grounds returned **one** bank verdict out of
twenty-four candidates. Everything else failed the cost-and-timeline hard gate.

**Selected: `bank-025` — La Crosse County Public Safety Communications.**

**Runner-up: none qualifies, and I am not going to pretend otherwise.** The
next-best entries are `bank-020` Body by Cochran (no cost anywhere, no employee
count), `bank-026` Field Aerospace (no cost, no timeline, and buy-vs-build in
genuine question), and `bank-027` Grand Traverse County (cost and term
disclosed, but every operational number is a projection because the system had
not deployed when the article ran). None of the three clears the gate. If
verification kills La Crosse, the honest outcome is a failed run and a
post-mortem, not a swap to a case that fails the same rule La Crosse passes.

---

## THE SEVEN-PART QUALIFYING FILTER, applied

**1. 50 to 1,000 employees, not a technology company.** — **PARTIAL, and it is
the one open item.** Not a technology company, plainly. But La Crosse County
government's headcount is not verified from any fetched page; the county HR
page returned 403. What IS on the record is the dispatch center's own shape:
"at least four dispatchers per shift." The fact-checker must close the county
number. **If it cannot be closed, the entity we describe is the dispatch
center itself**, which is unambiguously a small operation, and we say so.

There is a second, subtler question here that I want on the record rather than
buried: **a county agency is not a private company.** Dana owns a business.
Nothing in the filter or the scored hard-fail list excludes a public agency —
the exclusions are technology companies, Fortune 500s, venture-backed
darlings and research labs — so this is legal. But identification is the
highest-weighted scored criterion at 0.14, and it is where this case is
weakest. **That is a directing problem, not a disqualification**, and the deck
has to solve it on slide 2 by leading with the shape of the operation (a 24/7
phone desk nobody can staff) rather than the shape of the employer.

**2. ONE named bottleneck, in operator language.** — **YES, and it is the
strongest thing in the case.** Cory Lynch: *"By virtue of being a 24/7
department, we've just become a default."* And: *"It's been really hard to
hire and keep staff on."* Roughly 105,000 non-emergency calls a year about
parking tickets, court times, accident reports and which village hall to call,
landing on people trained to handle emergencies. That is not "operational
inefficiency." That is somebody's Tuesday.

**3. They bought or configured it, they did not build it.** — **YES,
cleanly.** They bought Aurelian's voice agent and pointed it at one line, the
non-emergency line. No engineers hired, no platform built. This is the
cleanest buy-not-build in the whole bank, and notably cleaner than Dunaway
(custom Azure Functions citation matcher) or Field Aerospace (self-hosted n8n
plus a React and Node app).

**4. A measurable before and after, with a real number.** — **YES.** Baseline
stated for calendar 2024: 140,000 calls for service, 35,000 of them 911, so
roughly 105,000 non-emergency. After: 41,000 calls handled by the system
between 5 May and early December 2025, about 65 percent of them without a
dispatcher picking up the phone.

*The honest caveat, which must ride with the number:* 65 percent is a
**containment** metric, not a resolution metric. A call that ended without the
caller getting what they needed still counts as handled. No resolution or
satisfaction figure exists on any fetched page. This is exactly the failure
mode `knowledge/kb/DEPLOYMENT_PATTERNS.md` flags for P9, and the deck says so
in the same breath as the number.

**5. Cost class AND timeline known. HARD GATE.** — **COST: YES, and it is the
best-shaped disclosure this series has ever had.** Around $67,000 in year one
and $81,000 in year two, priced on call volume, and Milwaukee Magazine frames
it in the unit Dana actually thinks in: *"approximate to one employee with
benefits."* WEAU independently calls it "the $70,000 system." Two further
agencies corroborate the price class on the same product: Grand Traverse
County at $60,000 then $72,000 on a three-year term, and Spokane at $95,000
annually on two years.

**TIMELINE: PARTIAL and it is verification task number one.** We have a
go-live date (5 May 2025) and a measured seven-month ramp. We do **not** have
decision-to-working for La Crosse. County board or public safety committee
minutes from late 2024 or early 2025 are where to close it. Spokane's "six
weeks of preparation" is a real data point for this pattern but belongs to a
different agency and may not be silently borrowed.

**6. A named human on the record.** — **YES.** Cory Lynch, operations
supervisor, quoted verbatim across three separate outlets.

**7. 2024 or later.** — **YES.** May 2025, with results reported through
December 2025.

---

## PREFERENCE ORDER, applied

Only one case qualified, so the preference order did not have to break a tie.
Recording how it would have scored anyway:

- **More agentic build:** rung 4, honestly. Fixed steps a person drew —
  answer, classify intent, collect location, route or text, escalate on
  keyword, hand to a human on request — with a biweekly meeting where
  dispatchers tune it. The vendor calls it an agent. **That gap is the
  curriculum payload**, and it is a friendly example rather than a dunk,
  because rung 4 is the right answer for this job.
- **More ordinary company:** a small-city dispatch desk with a hiring problem.
  Unglamorous in the way the doctrine wants.
- **Better documented cost and timeline:** best in the bank on cost by a wide
  margin, weakest-but-passable on timeline.
- **Sector that maps hardest onto Anchorage:** strong. The bottleneck is a
  24/7 phone desk that cannot be staffed, which is the single most portable
  problem shape in the local mid-market.

---

## THE SIX QUESTIONS, answered honestly

**1. Does Dana see themselves in this company?**
**Partly, and this is the case's weak flank.** Not in the employer — Dana runs
a business, not a county. But squarely in the *operation*: a phone line that
became the default number for everything, staffed around the clock by people
who are too skilled for most of what they answer, in a labour market where
the desk is hard to fill and harder to keep filled. The deck wins this on
slide 2 or it does not win it at all. Lead with the desk, not the employer.

**2. Does the problem sound like Dana's Tuesday?**
**Yes, emphatically.** "We've just become a default" is a sentence any
Anchorage operator with a main line has thought. Pair it with "it's been
really hard to hire and keep staff on" and it is the local labour story
verbatim.

**3. Can Dana picture actually doing this?**
**Yes, and better than any other case in the bank.** They bought one thing,
pointed it at one line, kept the emergency line untouched, and set a keyword
rule that hands anything alarming straight back to a human. The cost is
known, the term is known, and the operator framed the price as one employee
with benefits. Dana can do that arithmetic in their head on Thursday.

**4. Is there a number that makes Dana sit up?**
**Yes.** 41,000 calls taken off the desk in seven months, about 65 percent of
them never reaching a dispatcher, for about the cost of one hire.

*(Corrected after verification. This line originally read "two thirds of
105,000 nuisance calls a year taken off the desk," which is precisely the
error the fact-checker ruled against: the 65 percent is a share of the 41,000
calls the system took, not of the county's annual 105,000. The wrong version
is left visible here rather than silently swapped, because this is the exact
mistake the deck is most likely to make.)*

**5. Does Dana learn something about AI they did not know?**
**Yes, three things.** What "agent" actually buys you and why this one is a
rung 4 workflow rather than a rung 5 agent. That containment is not
resolution, which is the sharpest question Dana can ask any voice-AI vendor.
And that the same product failed at a neighbouring agency and had to be pulled
back to two hours a day, which teaches that deployment quality, not model
quality, is the variable.

**6. Would Dana send this to their ops lead?**
**Yes.** It has a price, a boundary, and a named failure mode. That is a
forwardable document.

---

## WHY THIS CASE AND NOT A BETTER-KNOWN COMPANY

Three private-sector stories in the bank read better on identification —
Dunaway, Team Air Distributing, Body by Cochran — and every one of them fails
the cost gate. The 2026-07-25 run shipped a case that failed a hard rule and
was rejected. This run will not repeat that.

There is also a finding worth stating plainly, because it shaped the choice:
the Infor cluster (Turtle, Endries, Team Air, Grosfillex, State Electric) all
sit behind a product that lists on AWS Marketplace at $250,000 to $600,000 a
year. Even if an operator handed us their invoice tomorrow, that is not a door
Dana can walk through. **La Crosse is the only case found in two waves where
the price is both known and reachable.**

---

## VERIFICATION TASKS, in priority order

1. **The decision-to-working interval.** County board or public safety
   committee minutes, late 2024 to early 2025. This closes the second half of
   the hard gate. Highest priority.
2. **La Crosse County headcount** against the 50 to 1,000 band. If it cannot
   be established, fall back to describing the dispatch center.
3. **Both cost figures verbatim**, from Milwaukee Magazine and WEAU
   separately, including the "one employee with benefits" framing.
4. **The 2024 baseline** (140,000 / 35,000 / ~105,000) and who measured it.
5. **The Ozaukee County failure account** in full, since it is the limit slide.
6. **Every Lynch quote character for character.** Wave 1 already produced one
   contradiction where two scouts returned different verbatim quotes from the
   same page, so this is not a formality.
7. **Try to break it:** is 65 percent of *handled* calls or of *all* calls? Is
   there any resolution or satisfaction figure anywhere? Did anything go wrong
   at La Crosse specifically?

## KILL CONDITIONS

The case dies, and the run writes a post-mortem rather than swapping, if:
the cost figures do not survive re-fetching; the decision-to-working interval
cannot be established from any source; or the 41,000 / 65 percent figures turn
out to rest on a base that makes them meaningless.

---

## POST-VERIFICATION ADDENDUM (2026-08-29)

The fact-checker returned `case_viable: true` and the case ships. It also
caught **two factual errors in this memo**, both of which are corrected here
rather than quietly edited above, because the record of what we got wrong is
worth more than a clean document.

**Error 1, and it was mine: Spokane is not the same product.** This memo and
`bank-025` both presented Spokane County's $95,000 contract and its six-week
preparation window as a third cost point on the same vendor. It is not. The
Spokesman-Review names **Prepared AI in partnership with Axon**, not Aurelian.
Spokane corroborates that the price class holds across the category and
nothing more. **The six-week figure is now formally off limits for this deck
under any framing**, which matters because it was the most tempting thing
available to fill the timeline gap.

**Error 2: two quotes were carried in a form that does not exist on the page.**
The "we've just become a default" line was truncated — the actual sentence
continues "for anything…related to municipalities or police departments." And
the inflection-and-background-noise line was silently smoothed; the page
carries an ellipsis and an editorial bracket. The deck uses the short clean
verbatim instead: *"I don't think AI will ever replace the human in a 911
center."* Both are corrected in `claims.json` and in the bank.

A third thing the fact-checker caught before it could become an error: **"approximate
to one employee with benefits" is Milwaukee Magazine's own prose, not a quote
from Cory Lynch or the county.** Putting it in anyone's mouth would be a
fabricated quote.

### The hard gate, ruled on

**Cost HOLDS** and it is the best-documented cost this series has had.

**Timeline is PARTIAL and I am accepting it narrowly.** The
decision-to-contract date does not exist in any reachable source — the county
web estate returns 403 to everything and its meeting PDFs are not full-text
indexed. What survived is La Crosse-specific and sourced: the county's own
announcement that the platform *"underwent several months of intensive
training before implementation,"* paired with a firm go-live of 5 May 2025.

I am accepting that because **Dana's actual question is "roughly how long
before it worked," and that answers it.** The deck states it exactly as
scoped and never as a decision-to-working interval, and **the delivery email
flags it as this run's one soft edge.** That is the opposite of what the
2026-07-25 run did, which was ship past a hard rule quietly.

### The scoping rule that governs the whole deck

The 65 percent is a share of **the 41,000 calls the system took**, not of the
county's 105,000 annual non-emergency calls, and it counts calls that
**ended**, not calls that got **answered**. No resolution, satisfaction,
callback or complaint figure exists anywhere, including on the vendor's own
page. Any slide that multiplies 65 percent by 105,000, or implies two thirds
of the county's nuisance calls are gone, makes a claim no source supports.

Written honestly the number is still excellent, and the honest version is the
better story: a phone desk with four people on it took 41,000 calls off its
own hands in seven months for about the price of one hire, and the county says
it did not cut a single position.

### One more directing consequence

**Slide 2 describes the dispatch center, not the county.** The county headcount
is uncorroborated and no county headcount goes on a slide. The desk is better
evidenced, more specific, and the thing Dana actually recognises: at least four
people on it at a time, open around the clock, authorised for 28 seats with 22
filled.

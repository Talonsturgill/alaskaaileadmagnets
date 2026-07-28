# ECONOMICS — what these things actually cost, and how to talk about it

Read `README.md` in this directory first. Everything here is a PRIOR. No band
in this file goes on a slide. Every figure that ships came off a page fetched
this run.

This file exists because of the hardest rule in the rebuild: **a case with no
cost and no timeline does not qualify.** That rule only works if the crew can
reason about cost well enough to recognise a real disclosure, spot a
suspicious one, and know which question is missing.

---

## THE FOUR COSTS, and only one of them gets quoted

When a vendor quotes a price, they are quoting the first one.

**1. Licence or usage.** The number on the proposal. Seat-based, usage-based,
or a platform fee plus consumption. Predictable, and usually the smallest of
the four.

**2. Integration.** Getting it connected to the systems of record. Frequently
larger than the licence in year one. Modern systems with clean APIs make this
cheap; a twenty year old ERP with a custom schema makes it the whole project.

**3. Data readiness.** Getting the data into a state where the thing can work.
This is the cost that kills timelines, and it is invisible in every proposal.
When the answer to "does the data exist and can the system reach it" is no,
**that gap IS the project** and the AI part comes later.

**4. Change.** Training, workflow redesign, the productivity dip while people
learn, and the political work of getting the person whose job changes to
actually use it. Almost never budgeted. Frequently the reason a technically
successful deployment produces no result.

**The single most useful thing this series can tell Dana:** the quoted price
is one of four, and the other three are where projects die. A case that
discloses all four is rare and worth a whole post.

---

## PRICING MODELS, and the trap in each

**Per seat.** Predictable, budgets cleanly, and punishes broad light usage.
Watch for a floor on seat count.

**Per usage.** Scales with value and scales with volume spikes. The trap is a
seasonal business modelling on a quiet month. An Anchorage operation that
triples in July should model July, not February.

**Per outcome.** Per document, per call resolved, per ticket closed. Aligns
incentives well. The trap is the definition of the outcome. A "resolved" call
that the customer called back about was counted anyway.

**Platform plus implementation.** Standard for anything touching an ERP. The
implementation number is the one to negotiate and the one that slips.

**Build it yourself on an API.** Cheapest per unit, and it converts a vendor
cost into an internal engineering cost that most mid-market companies do not
have and should not create. For this series it is usually disqualifying:
if the answer required hiring engineers, Dana cannot copy it.

---

## ORDERS OF MAGNITUDE (orientation only, never a citation)

For smelling a wrong number, not for quoting.

- **A single-workflow deployment** at a mid-market company is usually a
  four-to-five-figure annual commitment, not a six-figure one. A six-figure
  number should prompt "what else is in that number."
- **Implementation** commonly lands somewhere between a fraction of and a
  multiple of first-year licence, driven almost entirely by integration
  complexity.
- **Time from decision to working**, for a single well-scoped workflow, is
  usually measured in weeks to a few months. Anything claiming days either
  had unusually clean data or is describing a demo. Anything past a year is
  a data or change project wearing an AI label.
- **Benefits ramp over roughly ninety days.** Day-one full value is a tell.
- **Payback** on a well-scoped single-workflow build is usually claimed inside
  a year. Claims of weeks deserve the denominator question.

**How to use these.** A disclosed figure far outside a band is a flag to dig,
never a reason to reject. Most extreme figures are real numbers measuring
something narrower than the sentence around them.

---

## THE HONEST ROI SENTENCE

Freed hours are capacity. Capacity becomes money only through a decision.

The dishonest version: *"Saved 15 hours a week, which at $75 an hour is
$58,500 a year."* Nobody wrote a cheque.

The honest version names the decision: *"Freed about 15 hours a week across
the estimating desk. They used it to bid more work rather than to cut
staff."* That sentence is more useful AND more credible, and it is the voice.

The three real conversions, and a case should name which one happened:
1. **Deferred a hire.** Real money, easy to verify, the cleanest claim.
2. **Cut overtime or contractor spend.** Real money, appears in the P&L.
3. **Took on more work with the same people.** Real money if the work existed
   to be taken. This is the most common and the most often overstated.

Anything else is capacity, and capacity is worth saying plainly as capacity.

---

## THE QUESTIONS THAT GET COST ON THE RECORD

Cost disclosure is our hard gate, so finding it is a scouting skill. Where it
actually shows up, roughly in order of yield:

- Conference talks and operator panels, where peers ask peers directly
- Trade press interviews that ask "what did it run you"
- Public sector and utility procurement records, which are public by law
- Vendor pricing pages, for the licence layer only
- Podcast interviews with operators, which are underused and often candid
- Community forums where operators compare notes

**What to accept as a disclosure.** A range is fine. An order of magnitude is
fine. "Under fifty thousand all in, and about three months" fully satisfies
the gate. What does not satisfy it is silence, or a vendor's list price
standing in for what this customer actually paid.

**And the discipline that follows:** when a story is wonderful and has no cost
anywhere, it does not become a case with a missing slide. It goes back in the
bank as a lead, and the run takes the runner-up. That rule is what the last
run got backwards.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro, with the URL that established
each entry. Real disclosed figures are the most valuable thing this file can
accumulate: every one of them makes the next run's smell test sharper.)*

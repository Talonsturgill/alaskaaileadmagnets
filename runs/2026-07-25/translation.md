# TRANSLATION DOSSIER
## Case File No. 2, 2026-07-25
### Ambient clinical documentation, translated to Anchorage and Southcentral

### SHOWRUNNER HEADER, read before using this file

The translator returned TWO new factual assertions that were not verified this
run. Both are DROPPED from everything the deck may use. Neither is load
bearing and neither justified a second fact-check round.

1. DROPPED. 42 CFR Part 2, the federal confidentiality rule for substance use
   disorder records. Plausible and probably right, not fetched, so the
   behavioral health segment ships without any regulatory citation.
2. DROPPED. A 2025 AI in Alaska Native Health Care Systems symposium carried
   over from research/ALASKA_GROUND.md. Not fetched this run. It must not
   appear in any artifact.

VERIFIED BY THE SHOWRUNNER against
out/2026-07-25/source_uw_chws_alaska_physicians_2021.txt, the three table
figures the translator pulled that the brief had not already quoted, urban
300.4 per 100,000, isolated small rural 85.9, and 43.3 percent age 55 or
older. All three appear in the extract. Cleared for use.

Everything else below is claim-cited, quoted from the UW extract, or labeled
ANALYSIS.

---

Source of every Alaska figure used here, Dahal A, Skillman SM. "Alaska's
Physician Workforce in 2021." Seattle, WA: Center for Health Workforce
Studies, University of Washington, July 2022, revised January 29 2025, HRSA
funded. Referred to below as the UW report.

---

## 1. SEGMENTS

Segments only. No named Alaska business appears here as a target.

**Rank 1. Independent primary care and urgent care practices, Anchorage and
Mat-Su.** Same bottleneck physics as the case. A clinician sits in a room with
a patient, and a note has to exist afterward in an EHR. The case's own build
drafts both the chart and a plain language patient summary (c08). This segment
ranks first not because Anchorage is short of doctors, because the UW report
says the opposite, but because it already owns every input the build needs and
needs no new data collection.

**Rank 2. Anchorage-based clinicians who travel to rural sites or run
telehealth from town.** The UW report names this pattern directly, "it is not
uncommon for providers to travel to rural sites for short periods of practice,
and/or to provide telemedicine to more remote sites while based in urban
locations." ANALYSIS, this is where the after-hours note problem is worst,
because travel days and clinic days compete for the same evening. It is also
where the build translates least cleanly, see section 5.

**Rank 3. Behavioral health practices.** Same document stream, a session and a
note. Different physics. Sessions are longer, the transcript is more
sensitive, and the consent conversation is heavier. ANALYSIS, a behavioral
health pilot is a legal review before it is a software evaluation.

**Rank 4. Veterinary practices.** ANALYSIS, the lowest-regulation twin of the
case, and therefore the cheapest place in Southcentral to learn whether
ambient drafting actually changes an operator's evening.

**Rank 5. Dental and physical therapy practices.** ANALYSIS, the note is
shorter and more templated, which pushes the honest answer down the ladder
toward templates and macros. Listed for completeness, not recommended first.

Deliberately excluded. Large integrated systems and tribal health
organizations, outside the 20 to 2000 person band, and their decision is a
system-level procurement rather than a mid-market one.

## 2. THE HONEST RUNG

**The build in the case sits on rung 4, workflow.** Fixed steps in a fixed
order. Consent, record, transcribe, draft, clinician reviews and signs. The
stack is on the record, AWS Transcribe Medical and GPT-4 hosted on Microsoft
Azure (c06, vendor sourced). Consent is obtained before recording (c09, vendor
sourced). Nothing plans its own steps, so this is not an agent, and calling it
one would be agent washing.

**The honest rung for the Anchorage twin is the same rung 4 shape, bought and
configured, not built.** The case company deployed to 600 plus clinicians
(c05, vendor sourced) inside its OWN EHR (c06, vendor sourced). ANALYSIS, a 6
to 40 provider Anchorage practice does not own its EHR, so the equivalent
project is a vendor selection, an integration, a consent workflow, and an
adoption program. It is a configuration and change management project wearing
an AI label. This matches what the independent literature actually studied, a
commercial product, Abridge from Abridge AI, Inc (c24, independent), across 6
academic and community-based health care systems (c15, independent).

**The rungs underneath, which most practices have not exhausted.** ANALYSIS.
Part of the charting load is rung 1 rules work, note templates, order sets,
macros, smart phrases. Part is rung 2 retrieval, pulling the last visit
forward instead of retyping it. If a practice has not done those, an ambient
system will be paying a subscription to paper over a template problem.

**What the human catcher buys.** The clinician reviews and edits before the
note is signed. The vendor's own framing implies the review step, "88 percent
of the AI-generated text is accepted by the provider without edits" (c02,
vendor sourced). ANALYSIS, that review is the whole safety case. It bounds the
cost of error at the drafting stage and keeps the clinician the author of
record. It also has an obvious failure mode. Acceptance is not accuracy. A
high acceptance rate is equally consistent with a careful clinician and with a
review that has become a signature. The catcher only pays for itself while it
is still a real read.

## 3. COST CLASS

**No price for this category was verified this run, and no dollar figure
appears below, because an invented one would be worse than none.** The case
company built its own system rather than buying one, so the case contains no
purchase price at all.

The **shape of the cost**, in four components.

1. **A recurring per clinician software subscription.** The visible line, and
   the one a vendor quote leads with. It scales with headcount, which means
   the pilot decision is a headcount decision.
2. **Integration into the EHR you already run.** Either inside the contract or
   scoped as a connector project. ANALYSIS, ask which in the first call,
   because it moves the number more than the seat price does.
3. **Internal work that never appears on the quote.** Security and privacy
   review, a business associate agreement, a written consent script and room
   signage, note template configuration, and supervision through the first
   quarter. ANALYSIS, MODELED PLANNING RANGE, for a single site practice on
   one EHR with a vendor supplied integration and no custom connector, plan
   roughly 2 to 6 staff weeks of internal effort spread across a 90 day ramp,
   with one named clinic owner. Assumptions, one EHR, no custom build,
   existing compliance capacity, no multi site rollout. A planning range for
   scoping conversations, not a verified price.
4. **The custom build path is out of class for mid market.** The case's build
   presumes owning the EHR (c05, c06). ANALYSIS, without that, "build our own"
   means rebuilding the system of record.

**Capacity versus cash.** The independent result is 0.90 hours per week of
self-reported after-hours documentation (c22, independent), which the same
authors restate as the equivalent of 10.8 minutes saved per workday (c23,
independent). Those are the SAME finding expressed two ways, not two results.
ANALYSIS, at that magnitude the return is an evening, not a line on a P&L. It
becomes money only through a decision an owner actually makes, deferring a
hire, cutting locum spend, or keeping a clinician who was going to leave.

## 4. WHAT IT TAKES

**Data readiness.** Unusually good, and this is the rare AI project where the
data gap is not the project. The segment already holds every input, an EHR
with structured encounter records, a schedule, existing note templates, an
existing consent and privacy process, and a BAA process already used with
other vendors. The model input is the conversation in the room, generated
fresh at every visit. Nothing has to be labeled, migrated, or cleaned first.

**People.** ANALYSIS. Not IT, and not the owner by title. The clinic manager
or medical director, whoever runs the daily schedule, owns this or it dies.
Line manager ownership per HONEST_AI.md, and the same file's 10-20-70 framing
applies, roughly 70 percent of the work is people and process. Where a large
share of clinicians are late career, adoption is a training and respect
problem before it is a licensing problem.

**A realistic ramp.** Benefits ramp over roughly 90 days and day one full
value is a tell. The case's own "in just ten days" refers to ROLLOUT across an
already-existing 600 plus clinician network on a company-owned EHR (c04, c05),
and no build duration appears on any fetched page. ANALYSIS, plan a pilot with
a handful of willing clinicians, a written acceptance standard, a weekly read
of EDITED notes rather than accepted notes, and a stop rule.

**Evaluation.** ANALYSIS. What is the acceptance metric, who reads a sample of
signed notes against the recording, and what is the fallback on the day the
connection or the vendor is down. A practice that cannot answer the fallback
question has not finished the evaluation.

## 5. WHERE IT DOES NOT TRANSLATE

**Limit 1. Per capita supply is not Alaska's constraint, so a shortage pitch
is simply wrong.** The UW report states, "Alaska's physician supply, on a per
100,000 population basis, is similar to the national number." In 2021 there
were "240 physicians per 100,000 population providing direct patient care in
the state, and 95 primary care physicians per 100,000 population. Nationally,
in 2021 there were 248 physicians per 100,000 providing direct patient care,
and 94 primary care physicians per 100,000 population." Supply also grew, "The
estimated supply of physicians providing direct patient care in Alaska grew
19% from 1,474 in 2014 to 1,751 in 2021." ANALYSIS, any Alaska framing of this
build as filling a headcount gap fails against its own source material.

**Limit 2. Distribution. An ambient scribe does nothing where there is no
clinician.** "In 2021, 7 of the 29 Alaskan boroughs/census areas had no
practicing physicians and another 9 boroughs/census areas had physician supply
rates of fewer than 100 physicians per 100,000 population." Urban areas run
300.4 physicians per 100,000 against isolated small rural at 85.9. ANALYSIS,
any per-clinician efficiency gain multiplied by zero clinicians is zero. This
build is an Anchorage, Mat-Su, and Kenai clinic tool. It is not a rural access
tool, and selling it as one would be dishonest.

**Limit 3. Age, and what it does and does not imply.** "The mean age of
Alaska's practicing physicians was 52 years" and 43.3 percent were age 55 or
older. "More than 50% of all primary care physicians providing direct patient
care in eight of 29 Alaska boroughs/census areas were age 55 or older in
2021." ANALYSIS, this is a retention question rather than a recruitment one.
The limit is equally honest, nothing in the verified evidence shows that an
ambient documentation system changes a retirement decision. That is a
hypothesis a practice could test on itself, not a finding anyone can cite.

**Limit 4. The independent evidence is modest, and it is about a different
system.** The study measured Abridge, not the case company's in-house build
(c24). It is a quality improvement study with pre and 30-day post surveys
(c14), not a randomized trial. 451 enrolled, 272 completed both surveys at
60.3 percent, 263 analyzed (c17, c18, c19). The authors state there was no
control group (c25), that findings were subjective self-reports not paired
with EHR data (c26), and that recruitment may have been biased toward people
favorable to new technologies (c27). The result is 0.90 hours per week (c22).
The vendor's figures are per visit, self-reported, unaudited, under 4 minutes
versus 16 (c01), 88 percent accepted without edits (c02), 2.5 times more
detailed (c03). ANALYSIS, the vendor measured the TASK and the independent
study measured the WEEK, and the week barely moved. An Anchorage practice
should budget against the week.

**Limit 5. Connectivity, and the itinerant pattern.** The stack is cloud
transcription and a cloud model (c06). ANALYSIS, offline and low bandwidth
behavior is the single most important question for any Southcentral practice
that also runs village clinic rotations or telehealth into the Bush, and the
UW report is explicit that the pattern exists. A per seat subscription priced
for a fixed exam room with stable bandwidth fits a travel rotation badly. No
Alaska bandwidth figure was verified this run, so this is the question to ask
a vendor, not a claim about Alaska's networks.

**Limit 6. Economics. Nothing here promises more patients.** The case
company's own engineering blog makes no claim about more patients or more
visits per day (c10, verified by absence). A 30 percent increase in patients
appears only in the company's own press release, one San Francisco pilot
clinic, no control, no baseline (c12), and that press release is a paid wire
distribution, not independent reporting (c11). ANALYSIS, a practice that buys
this expecting throughput is buying against a claim the company itself did not
repeat on its own technical blog.

## 6. LOCAL PROOF PAIRING

The line that makes this land as an Alaska fact is not a shortage line, it is
a distribution and age line. These two together are the pairing.

> "Alaska's physician supply, on a per 100,000 population basis, is similar to
> the national number."

> "In 2021, 7 of the 29 Alaskan boroughs/census areas had no practicing
> physicians and another 9 boroughs/census areas had physician supply rates of
> fewer than 100 physicians per 100,000 population."

And the age line, for the retention frame.

> "The mean age of Alaska's practicing physicians was 52 years."

ANALYSIS, the Anchorage-specific texture is in the report's Table 6, which
ranks the top 15 boroughs and census areas by supply per 100,000. Anchorage
ranks 1 for number of overall physicians and 11 for number of primary care
physicians, with the table's own footnote that "Lower number reflects higher
rank." Anchorage is where the specialists are, and it is not the top of the
state for primary care density. That is the honest local hook, and it is a
distribution story, not a shortage story.

## 7. WHY NOW, AND THE SEASONAL ANGLE

**Why now, on verified ground only.** The standing labor frame in
ALASKA_TRANSLATION.md runs on out-migration years and nonresident workforce
share. NEITHER WAS VERIFIED THIS RUN, so neither is used, and no artifact may
quote them. The verifiable why-now is different and better. Alaska's physician
count grew 19 percent from 1,474 in 2014 to 1,751 in 2021, supply per 100,000
is similar to the national number, and 43.3 percent of physicians were age 55
or older at a mean age of 52. ANALYSIS, that combination says the pressure
point in Southcentral is holding onto the clinicians already here, and
after-hours documentation is one of the few pressures on that group a practice
owner can act on this quarter.

**In season, and it is thin. Say so.** Late July in Southcentral is peak
visitor load, salmon season, fire season, and the summer when clinic staff
take deferred leave. Nothing in this claim set or in the UW report measures
Southcentral clinic volume by season, so any seasonal number would be
invented. The one honest seasonal note is operational. ANALYSIS, late July is
a poor month to START an adoption program, because the person who would own it
is covering someone else's leave. The realistic move is to run vendor
evaluation and the security review now and start the clinician pilot after the
season, so the 90 day ramp lands in a quarter with full staffing. If the deck
needs a seasonal beat, that is the only one the evidence supports.

## BOTTLENECK MAP CHANGE

**This REPLACES the existing "Independent clinics" row in
knowledge/ALASKA_TRANSLATION.md.** The current row reads "charting burnout"
with the answer "ambient scribes (buyable)," which is directionally right and
operationally empty. The replacement names the rung, names the catcher, names
which number to plan against, and carries the Alaska proof that keeps anyone
from writing a shortage pitch.

| Independent clinics and practices | Fax intake, and the note that gets written after hours | Document intake (single call to workflow). Ambient documentation is rung 4 workflow with the clinician as the catcher, and mid market buys and configures it rather than building it, the case build presumed owning the EHR. Exhaust templates and macros (rung 1) first. Plan against the independent per week result, not the vendor per visit one | 006, 007, Case File 002 (2026-07-25), UW CHWS Alaska Physician Workforce 2021 |

A second row is a candidate for a future run and is NOT proposed today,
Anchorage-based itinerant and telehealth clinicians, where the bottleneck is
charting stacked behind travel days and the limiting factor is connectivity.
It needs its own verified Alaska proof before it earns a row.

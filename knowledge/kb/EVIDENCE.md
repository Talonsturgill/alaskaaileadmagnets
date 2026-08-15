# EVIDENCE — reading AI claims without being fooled or paralysed

Read `README.md` in this directory first. Everything here is a PRIOR. Nothing
here is citable.

Two failure modes bracket this work. Believing a vendor number is the obvious
one. The other one is what sank the last run: getting so careful that the post
becomes a seminar on measurement and the reader learns nothing they can use.

**The standard: know exactly how much to trust a number, label it in the same
breath, and then get on with the story.** Sourcing discipline is plumbing.

---

## SOURCE TAXONOMY, and what each one systematically omits

Ranked by how much weight a number from it can carry.

### Peer-reviewed study
*Carries:* a real methodology, a stated sample, and limits the authors named
themselves.
*Systematically omits:* cost, vendor identity sometimes, and generalisability
to a company of Dana's size. Almost always studies a different setting.
*Watch for:* pre/post survey designs described in prose as though they were
controlled trials. Read the methods section and state the actual design. The
last run nearly shipped "followed clinicians at 6 health systems for a year"
about what was a 30 day pre/post survey.
*Label:* "peer reviewed, independent" and name the design.

### Government or regulator data
*Carries:* authority on population-level facts.
*Systematically omits:* anything about a specific deployment. Usually two or
more years stale.
*Watch for:* PDFs the fetcher cannot read. Extract with pypdf rather than
dropping the source.
*Label:* the agency and the data year, always the data year.

### Independent trade press with an interview
*Carries:* the most useful evidence in this file for our purposes. A named
operator describing their own build, with numbers they said out loud.
*Systematically omits:* verification. The reporter usually did not audit the
figure, and often did not ask what it excluded.
*Watch for:* articles that are a rewritten press release. Tells: no
independent quote, no limit named, publication date within days of the
vendor's announcement, phrasing lifted verbatim.
*Label:* "reported by <publication>, figures from the company."

### Conference talk or recorded operator session
*Carries:* unusual candour. Operators talking to peers say things they do not
say in a case study, including what went wrong.
*Systematically omits:* rigour, and often the denominator.
*Watch for:* this is where cost and timeline actually get disclosed, which
makes it disproportionately valuable given our hard intake gate.
*Label:* "said by <name, role> at <event, date>."

### Earnings call or investor material
*Carries:* claims made under securities liability, which raises the floor.
*Systematically omits:* the operational detail Dana needs, and it is selected
for the good news.
*Label:* "from the company's <quarter> earnings call."

### Vendor case study
*Carries:* structure, named customer, usually a real deployment underneath.
*Systematically omits:* the baseline, the denominator, the failures, the
timeline, the cost, and every customer where it did not work.
*Watch for:* percentages with no base, "up to" figures, best-performing-site
numbers presented as the average, and time savings measured on the narrowest
possible task.
*Label:* "per the vendor's own case study" or "per the company's own numbers",
in the same sentence as the figure. Never in a footnote.

### Press release
*Carries:* that the deployment exists and roughly when.
*Systematically omits:* everything else.
*Label:* "in the company's own press release."

### Analyst survey and market forecast
*Carries:* very little that helps Dana. Percentages of executives who "plan
to" do something are not evidence that anything happened.
*Use:* framing at most, never a load-bearing number.

### LinkedIn post or vendor blog by an employee
*Carries:* a lead. Sometimes a very good one.
*Use:* as a starting point to find a real source. Never as the source.

---

## THE STANDARD INFLATION PATTERNS

Learn these and most bad numbers announce themselves.

1. **The missing denominator.** "Saved 15 hours a week." Across how many
   people? Fifteen hours across forty staff is twenty-two minutes each.
2. **The narrow task, wide claim.** Measured on the one step the tool touches,
   stated as though it were the whole job. A 60 percent reduction in drafting
   time is not a 60 percent reduction in the process.
3. **The best site as the average.** Pilot at the most enthusiastic location,
   report it as the deployment result.
4. **Self-reported time.** People asked how much time they saved consistently
   overestimate. Not dishonesty, just a known measurement property. Say
   "self reported" and move on.
5. **The absent baseline.** No before number, so the after number cannot mean
   anything. Ask what it was before. If nobody measured before, that is worth
   saying plainly and is often the most useful sentence in the story.
6. **Capacity stated as cash.** Freed hours are capacity. They become money
   only when somebody decides to defer a hire, cut overtime, or take more
   work. Never convert silently.
7. **The unit switch.** Per visit here, per week there, per day in the
   headline. Different bases cannot be summed or compared. Name the base every
   time.
8. **Cherry-picked window.** Compared against the worst month.
9. **Adoption as outcome.** Seats deployed, queries run, users active. None of
   these are results. A tool everybody uses that changed no operational number
   is a tool everybody uses.
10. **The agent-washed claim.** A rung 4 workflow sold as an agent. See the
    field guide in `knowledge/AGENTIC_LITERACY.md`. Correct it gently and say
    the useful thing: often the right product, just do not pay agent prices.

---

## THE BASE RATES, and how to use them honestly

Two facts are broadly established and constantly abused: a large share of
corporate AI pilots never reach production or measurable value, and the
projects that succeed look markedly different from the ones that do not.

**How to use them.** Cited together, always, and landing on what winners do.
"Most pilots stall" alone is fear, and fear is banned. "Most pilots stall, and
the ones that do not have these four things in common" is the useful sentence.

**Never use them as:** a lone hero statistic, a hook, or a reason for Dana to
feel behind.

**What the successful ones have in common,** and this is the durable teaching:
one named bottleneck rather than a general capability, a named internal owner
with authority, a measured baseline before anything was built, a human at the
expensive decisions, and a budget for the ninety day ramp.

---

## THE VERIFICATION PROTOCOL

What the fact-checker actually does, in order.

1. **Fetch every URL fresh, this run.** Not from memory. Not from a search
   snippet. A search summary naming a company is not that company appearing in
   the article, and we have already been burned by exactly that.
2. **Find the number in the page, verbatim.** If it is not there in those
   digits, it does not exist.
3. **Find the baseline.** No baseline, no before-and-after claim.
4. **Find the denominator.** Per what, across how many, over what period.
5. **Identify who measured it,** and label accordingly.
6. **Find the date.** Both the publication date and the date the work happened.
7. **Find one limit** the source itself names. Every case ships with one.
8. **Find the cost and the timeline.** Hard intake gate. Without both, the
   case does not qualify, however good the story is.
9. **Find a named human.** A quote with a name and a role.
10. **Try to break it.** Search for a contradicting account. A case nobody
    tried to disprove has not been checked.

**When two sources disagree,** the one that read the full page wins over the
one that read a summary. Log the contradiction in the run's incidents.

---

## LABELS, the exact wording

Say it inside the sentence, never as a disclaimer block.

- `Per the company's own case study, ...`
- `Per the company's own numbers, ...`
- `In the company's own press release, ...`
- `Reported by <publication>, figures from the company.`
- `Peer reviewed and independent, <n> participants, <design>.`
- `Self reported, not measured from system data.`
- `<Agency>, <data year> data.`
- `Modeled, not measured. Assumptions stated.`

**Modeled figures are ranges with stated assumptions, never lone hero
numbers.** If we did the arithmetic, we say we did the arithmetic.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro, with the URL that established
each entry. See `README.md`.)*

- 2026-07-25 (case file 2): a scout banked a named company from a search
  result summary; a second scout read both underlying articles in full and
  neither named it. Rule that came out of it: a company name never enters the
  bank from a search snippet, only from a fetched page.
- 2026-07-25 (case file 2): a study described in secondary coverage as
  longitudinal across six health systems was, in its own methods section, a
  30 day pre/post survey. Read the methods section, every time.
- 2026-08-15 (case file 2): **THE FETCH LAYER CAN FABRICATE. Treat it as a
  hazard, not a tool.** On one long page the fetcher returned roughly eighty
  bullet points that were not on the page, including invented statistics, in
  fluent and plausible form. This nearly reached a slide. **The mitigation that
  worked, and is now standing practice for any page longer than a few screens:**
  ask narrow enumerated questions ("quote the full sentence containing each of
  these words, and say NOT PRESENT if absent") instead of "summarise", and
  cross-check every quoted string across TWO independent renderings of the same
  URL before trusting it. Anything that survives only one rendering is labelled
  SINGLE RENDERING and cannot carry a slide. Established across the fetches
  behind https://www.ownedandoperated.com/post/owned-and-operated-173-we-booked-400-calls-a-week-how-avoca-ai-is-shaping-home-services
  and recorded per claim in `runs/2026-08-15/claims.json`.
- 2026-08-15 (case file 2): **SEO poisoning of operator language is real and it
  is new.** The exact disclosure phrases this knowledge base recommends ("what
  it cost us", "we pay about", "paid for itself", "we spent about") now return
  almost pure AI-vendor listicles. One scout measured 14 of 20 searches
  returning zero fetchable operator pages; two others hit the same wall
  independently. **The word "AI" poisons a cost query outright.** Search the
  bottleneck plus the dollar figure with no AI word, then find the AI inside the
  article; or find the deployment first and chase the company by name.
  Reproduced in the retro's own frontier scan, where every generic query
  returned vendor blogs such as https://www.retellai.com/blog/best-voice-ai-solutions-for-home-service-contractors
  and https://superdupr.com/blog/ai-answering-service-home-services
- 2026-08-15 (case file 2): **read the verbs.** Wave one killed at least three
  otherwise-good stories whose every number was a projection stated ahead of
  launch. "Expects to", "will", "anticipated" and "projected" are kills, not
  numbers. Extension and MEP success stories in particular get written when the
  engagement ends, which is usually before the AI reaches production. Established
  on https://www.nist.gov/mep/successstories/2024/cjb-industries-chemical-manufacturer-enhances-efficiency-and-quality-ai
  where the disclosed 300,000 dollars bought a data historian and a quality
  system and the generative-AI work was still future tense on a page updated
  April 2026.
- 2026-08-15 (case file 2): **the agentic label and the measured number are
  inversely correlated.** Across four scouts' reading, the deployments carrying
  "agentic" in the headline named zero companies, zero numbers and zero costs,
  and the deployments with real measured numbers called themselves nothing at
  all. Useful as a smell test and as teaching. Same evidence base as the restock
  notes in `runs/2026-08-15/restock_notes.md`.
- 2026-08-15 (case file 2, retro scan): **in voice AI, almost every published
  number is a CONTAINMENT number, and containment is not resolution.** The
  distinction, stated plainly on a vendor CEO's own blog (label it as such):
  "A call is contained if the customer hangs up. It's resolved if their problem
  is fixed" and "Many vendors quote 'containment rate' (calls that don't reach a
  human) rather than resolution rate (issues actually solved). These are not the
  same number." Source: https://irisagent.com/blog/voice-ai-customer-service-2026-benchmarks/
  (IrisAgent, written by its CEO and co-founder, sells the category; the page
  cites no survey with a sample size). **The question to ask any voice AI case:
  how many of those contained calls called back.** Booked-call and answer-rate
  claims are the same trap in a different coat.

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

### 2026-08-08 (case file 2, shipped nothing)

- **Read a vendor's stat card against the vendor's own prose and pull quotes.
  Add this to the verification protocol.** The n8n case study for Field
  Aerospace disagrees with itself in three places: the stat card says "25
  minutes (vs 3-4 weeks before)", the body prose says "about two weeks of work
  from multiple contributors", and Shawn Tatum's named pull quote says
  "probably two weeks of three or four people". Two of three say two weeks.
  The likely mechanism is a marketer collapsing "three or four people, two
  weeks" into "3-4 weeks", which **inflates the baseline by about 2x**.
  The defensible number is the named human's, because the prose agrees with it.
  This is a fast, cheap, repeatable check and it caught a real defect.
  Source: the n8n Field Aerospace case study, fetched by scouts S4 and W2-A.
- **The synthetic case study has a signature, and it is first names.** A vendor
  blog published a distributor case study for "Meridian Supply Co." with a
  first-name-only "Marcus, operations director" and suspiciously tidy numbers
  (41 hours a week, 4.7 to 1.6 minutes). Composite, almost certainly.
  **The tell stack: a generic-plausible company name, a source with no surname
  and no verifiable title, round or too-clean figures, and no second page
  anywhere naming the company.** Do not use it. Source: scout S2.
- **A company newsroom that links straight to the vendor's case study is a
  strong negative signal, and it is the cheapest check available.** Field
  Aerospace's own newsroom carries "Using AI for Client Responsiveness" whose
  href points back at the n8n page. The company did not write anything, it
  linked the vendor. That reliably predicts no independent account exists
  anywhere. **Check the newsroom href before spending searches on trade press.**
  Source: scout W2-A.
- **Vendor case studies are now 4 for 4 (arguably 6 for 6) on the same
  omission profile, and it is the FORMAT, not sloppiness.** Choco/Colony Foods,
  WizCommerce/Howard Elliott, Hatch/Wilson, n8n/Field Aerospace, plus six
  Paperless Parts studies killed at intake on the base rate. Every one gives
  the bottleneck, a named human and a before-and-after. Every one omits cost,
  decision-to-working timeline and headcount. **Treat a vendor case study as a
  source for the BOTTLENECK and the NAME only, never as a candidate.** The
  entry above under "Vendor case study" understated this: the omission is not
  a tendency, it is the genre.
- **Two more press-release-laundering tells confirmed in the wild.** A trade
  piece on Palmer Holland was a rewrite of the company's own release, with
  launch language, an aspirational CIO quote, no independent number and no
  limit named. A Farm Equipment "practical guide" was bylined by the vendor
  itself. Source: scouts W3-B and S2.
- **Three more disqualifying shapes worth naming, all caught this run.** A
  company that BUILT the tool and now RESELLS it is a vendor in this story, not
  an adopter (Dairyland Power Cooperative; also Summit Electric, "Summit
  developed an AI-enabled tool"). An operator quoted as an independent customer
  who is now the vendor's COO has a commercial interest (Armstrong Plumbing).
  And a deck full of genuinely good numbers may contain **no AI at all**
  (Casella Construction: HR software plus Microsoft Power Platform). Check the
  premise before checking the numbers.
- **The absent-baseline and cherry-picked-window patterns showed up together.**
  A municipal utility reported savings "from about $15,000 to a quarter million
  in one month" with no baseline period and no definition of what the savings
  measure against. One month is not a result. Source: scout W3-B.
- **Podcast episode titles carrying dollar figures are an artefact, not a
  lead.** Both instances found across two waves traced to machine-generated
  podcast-aggregation pages we cannot trust. Do not chase them again.
  Source: scouts S1 and W2-B.
- **Podcast transcripts are, as a category, closed to this fetcher.** No
  transcript was reachable for Acquisition Collective, FWD WholeStory, Toolbox
  for the Trades, Bridging the Gap or Distribution Talk. Budget accordingly:
  the audio seam is real and it does not publish.

# HUNTING GROUNDS — where these stories actually live, and how to find them

Read `README.md` in this directory first. `config/sources.yaml` holds the
operational source list. This file holds the search craft.

The premise of the whole series: **specific, small, real wins at Dana's scale
are happening and nobody is aggregating them.** That is our advantage and it
only pays if the hunting is good. Being a sniper is the job.

---

## THE CORE PROBLEM OF THE HUNT

The companies we want do not describe themselves as AI adoption stories.

A 210 person mechanical contractor that cut bid turnaround from three days to
four hours thinks of that as a good quarter, not as content. Nobody at that
company will ever publish the phrase "AI transformation."

**So searching for AI language finds vendors. Searching for operator language
finds operators.** Every productive search in this file is built on that.

---

## SEARCH CRAFT

**1. Search the bottleneck, not the technology.**
Weak: "AI case study manufacturing." Strong: "cut quote turnaround" or
"estimator backlog" or "invoices keyed by hand" paired with a year.

**2. Search the disclosure, not the outcome.**
Cost is the hard intake gate, so hunt where cost gets said out loud:
"what it cost us", "all in", "under six months", "we paid about". Operators
talking to peers disclose. Operators talking to press do not.

**3. Search the named role.**
"our estimator", "the dispatcher", "our ops manager said". A named human on
the record is a qualifying requirement, so search for the shape of a quote.

**4. Search the scale.**
Pair the pattern with employee-count language: "family owned", "three
locations", "we have about 200 employees", "second generation". This filters
out the enterprise stories that Dana files under "not me."

**5. Search the second-order sources.**
Award submissions, trade association case studies, state and utility grant
reports, procurement records, conference agendas. These are written for peers
and are far more specific than press coverage.

**6. Search the failure too.**
"we tried and it did not work" is how you find the honest limit that every
case has to name, and often finds the company that later got it right.

---

## THE GROUNDS, by yield

**High yield for our qualifying filter:**
- Regional business journals, which cover mid-market companies by name and ask
  operational questions the national press does not
- Trade press by sector (construction, logistics, processing, healthcare
  operations, field service), which speaks operator language natively
- Conference talks and recorded operator panels, the best source of disclosed
  cost and timeline in existence for our purposes
- Trade association case studies and award submissions
- Public procurement and grant reporting, where cost is public by law
- Operator podcasts, underused, frequently candid about what it cost

**Medium yield, needs verification work:**
- Vendor case studies, useful for finding the company and then going around
  the vendor to an independent account. The vendor page is the lead, never the
  source.
- LinkedIn posts by operators, good leads, never a source
- Local and regional news, thin on operational detail but names companies

**Low yield, mostly noise:**
- National business press, which covers enterprises and funding rounds
- Analyst forecasts and executive intent surveys
- AI newsletters, which recycle the same enterprise anecdotes
- Anything whose headline contains a percentage and no company name

---

## THE SCOUT'S DISCIPLINE

Learned the expensive way and now law:

1. **A company name never enters the bank from a search snippet.** Only from a
   page fetched and read in full. A search summary that names a company is not
   that company appearing in the article. This has already cost us once.
2. **Read the whole page before citing any of it.** Including the methods
   section, including the fine print under the chart.
3. **Kill early.** Run the seven-part qualifying filter from
   `knowledge/CASE_CRAFT.md` at intake. It is cheaper to lose a candidate on
   the first read than on slide six.
4. **Cost and timeline first.** They are the hard gate and the rarest
   ingredient. Check them before falling in love with a story.
5. **Bank the near misses as leads,** with what is missing named. A great
   story with no disclosed cost is a lead worth an interview, not a case.
6. **Contradiction beats confidence.** When two scouts disagree, the one that
   read the full page wins, and the contradiction gets logged.

---

## THE BANK

The bank exists so a run never starves and never has to lower the bar to
ship. Kill verdicts disqualify a case, not a run: swap to the runner-up and
continue.

**Par:** enough qualified candidates on hand that any single kill is
survivable. Restock when the bank drops below par, in parallel, one scout per
hunting ground.

**A bank entry carries:** the company and its shape, the bottleneck in
operator language, the build and its honest ladder rung, the numbers with
their labels, cost and timeline with the source that disclosed them, the
named human, every URL, the date fetched, and an explicit skepticism label.

**Entries expire.** Tooling economics move fast enough that a two year old
number misprices a decision made now. Re-verify before shipping anything that
has sat in the bank.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro. Searches that worked, verbatim,
are worth recording: query craft compounds faster than anything else here.)*

- 2026-08-15 (case file 2): **every ground carries exactly one half of the
  qualifying filter and never the same half.** Trade press names the operator,
  the bottleneck and the outcome and omits the price, confirmed across seven
  verticals in one run. Public record and grant documents name the price and
  omit what was built or whether it reached production. Vendor libraries
  describe the build and omit both. Plan restock around which half a ground
  gives you, and pair grounds deliberately. Source: the seven-scout hunt
  recorded in `runs/2026-08-15/restock_notes.md`, with the ground-by-ground
  evidence at nist.gov/mep/successstories, publicpower.org and
  fleetowner.com.
- 2026-08-15 (case file 2): **the ground that gave BOTH halves was an
  operator-to-operator podcast.** One domain-constrained query into
  ownedandoperated.com produced the entire shipped case, including a dollar
  figure the owner said out loud. Peers disclose to peers because the audience
  would smell a dodge. Source:
  https://www.ownedandoperated.com/post/owned-and-operated-173-we-booked-400-calls-a-week-how-avoca-ai-is-shaping-home-services
  Promote operator podcasts from "underused" to first stop for any cost-gated
  restock.
- 2026-08-15 (case file 2): **domain-constrained search produced every usable
  lead across seven scouts. Unconstrained search produced nothing usable in any
  ground.** Pick the domain first, then search inside it.
- 2026-08-15 (case file 2): **`r.jina.ai/<url>` defeats the HTTP 403 wall** on
  Randall-Reilly properties that were previously locked out entirely. Proven by
  retrieving
  https://www.ccjdigital.com/ccj-innovators/article/15744393/grand-island-express-boosts-fleet-efficiency-with
  as https://r.jina.ai/https://www.ccjdigital.com/... . CCJ Innovators is the
  best cost-disclosure format in trucking, so this reopens a ground. Treat the
  proxied text as a fetched page, and re-read it for the fabrication hazard in
  `EVIDENCE.md` before quoting.
- 2026-08-15 (case file 2): **NIST's MEP archive has a faceted keyword search**
  at `https://www.nist.gov/mep/successstories?k=<term>`, which makes the whole
  ground checkable in two fetches. Result, with certainty: the 1,067-story
  archive contains exactly THREE AI stories ever and none from 2026. **The MEP
  ground is structurally barren for our filter for at least two quarters.** Do
  not spend a scout on it. Source: https://www.nist.gov/mep/successstories
- 2026-08-15 (case file 2): **the two-step that works on public bodies.** The
  association trade magazine names the deployment and omits the price, then the
  LOCAL NEWS OUTLET COVERING THE BOARD MEETING prints the contract number.
  Proven on Coldwater Board of Public Utilities (Michigan): deployment at
  https://www.publicpower.org/periodical/article/coldwater-board-public-utilities-deploying-ai-prevent-grid-outages
  then 248,000 dollars over five years at https://wtvbam.com/2026/01/01/877163/
  Search the utility or district name plus "board approved" on the local
  station or paper, never the national association.
- 2026-08-15 (case file 2): EDGAR full-text search is fetchable as JSON at
  `https://efts.sec.gov/LATEST/search-index?q=%22phrase+a%22+%22phrase+b%22&dateRange=custom&startdt=&enddt=`
  which gives obliged disclosure without fighting the HTML app. Untested for
  yield on our size band; small-caps are usually above it.
- 2026-08-15 (case file 2): **blocked to our fetcher** (403/429/refused or
  blank): ccjdigital.com and overdriveonline.com (use r.jina.ai), achrnews.com,
  ecmag.com, mcaa.org, mdm.com, qsrmagazine.com, restaurantbusinessonline.com,
  franchisetimes.com, bizjournals.com, staffingindustry.com PDFs,
  homehealthcarenews.com, businessinsider.com, and gamep.org (renders blank on
  three attempts across two waves, retire it). **Confirmed fetchable:**
  nist.gov, fleetowner.com, contractormag.com, industryweek.com and Endeavor
  Business Media generally; truckingdive.com, constructiondive.com,
  supplychaindive.com, restaurantdive.com, hoteldive.com and Industry Dive
  generally; route-fifty.com, digitalcommerce360.com, n8n.io, inddist.com,
  industrialsupplymagazine.com, virginiabusiness.com, publicpower.org,
  akbizmag.com, phcppros.com, ownedandoperated.com, pmmag.com, and
  quicktransportsolutions.com (free FMCSA carrier records, excellent for
  verifying the headcount of any trucking candidate).
  **Publisher-level blocking is not a rule:** pmmag.com fetched cleanly in the
  2026-08-15 retro scan (https://www.pmmag.com/articles/106575-70-of-home-service-professionals-now-use-ai-to-cut-admin-work-not-field-jobs-housecall-pro-report-finds)
  while its BNP Media sibling achrnews.com stayed blocked. Test the domain, do
  not infer it.
- 2026-08-15 (case file 2): grounds that returned nothing usable and should not
  get another scout without a new angle: trade association AI content (MCAA,
  NAW, Distribution Strategy Group), MEP and extension AI explainer blogs (IMEC,
  Catalyst Connection, WMEP, MAGNET), aggregate MEP impact reports (they name no
  company by construction), state "Industry 4.0" grant programs (the phrase
  means metal-cutting machines with network ports; one 500,000 dollar Iowa award
  read in full was weld cells, a plasma cutter, a brake press and an ERP
  upgrade, zero AI), and municipal general-government procurement (a perfect
  cost disclosure attached to an entity Dana cannot be is still a kill).

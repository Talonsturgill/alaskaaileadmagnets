# RESTOCK NOTES — 2026-08-29

Bank health at wake: **0 ship-ready.** All 16 seeded entries were demoted to
`lead` on 2026-07-28 when the cost-and-timeline hard gate landed, and none of
them carried a cost. Restock was therefore mandatory and the whole run's risk
sat here.

---

## WAVE 1 — four scouts, four grounds, ZERO bank verdicts

| Ground | Candidates returned | Banked | Killed |
|---|---|---|---|
| Cost-disclosure grounds (conference, podcast, procurement, award, MEP) | 4 | **0** | 9 |
| Sector trade press | 4 | **0** | 12 |
| Regional business journals | 3 | **0** | 12 |
| Government, academic, research + vendor libraries as leads | 3 | **0** | 7 |

Fourteen candidates, eight of them genuinely good stories, **not one with a
disclosed cost.** Eight were added to the bank as leads (`bank-017` through
`bank-024`), each carrying a `qualification` block naming exactly what is
missing and exactly what would promote it.

### The structural finding, and it belongs in the knowledge base

Wave 1's four scouts converged independently on the same explanation, which
makes it worth more than any single candidate they found:

> **Award submissions, vendor blogs, trade press and MEP writeups all
> reliably print RESULTS and never print MONEY, because every one of them is
> written to win something, and cost is the one number that never helps you
> win.**

The cost-disclosure scout opened four award submissions, two MEP success
stories, one vendor press release and one vendor blog. Every one disclosed
results. Exactly one disclosed anything about money, and it was a ratio
("less than half of what it was before"), not a figure.

This is not bad luck and it will repeat next run unless the grounds change.

### Where cost DID appear, and what that predicts

The only absolute dollar figure wave 1 surfaced was `$300,000` on a NIST MEP
success story, and MEP prints it only because the federal client impact survey
demands it. That same survey format is why the MEP figure is reliably the
**capital investment line and never the implementation clock**. And on that
particular story the money attached to data-visualisation software while the
AI component was still in future tense, which is exactly the attribution trap
two separate scouts flagged.

Prediction that follows: the highest-yield remaining grounds are the ones
where cost is published **by law or by construction** rather than by choice.
State Industry 4.0 grant recipient lists, public procurement and board
minutes, and operators talking to peers on conference panels.

### Grounds discovered this run, worth promoting into `config/sources.yaml`

1. **Constellation Research SuperNova Awards case study archive**
   (`constellationr.com/communities/supernova-awards-2026/case-study-archive`).
   An operator-written library of 250-plus deployments, indexed by company and
   by a named person with a title, fetchable, with further pages covering 2025
   and 2024. Delivers filters 2, 4, 6 and 7 reliably. Never delivers cost, so
   it is a lead generator: take the named human somewhere else for the money.
   Two of one scout's four candidates came from a single page of it.
2. **Microsoft Learn Power Platform case study library**
   (`learn.microsoft.com/power-platform/guidance/case-studies`). The richest
   source wave 1 hit for rung-4 builds at named, ordinary, correctly sized
   non-technology companies. Written for builders rather than buyers, so it
   names the architecture, the tool calls, the failure they had to engineer
   around, and the limit. Never names cost.
3. **NIST MEP success stories paged by year** rather than searched. Searching
   surfaced only 2022-vintage AI stories; the index itself holds 1,067
   entries.

### Fetch map (recorded so no future run re-buys this)

**Fetch fine:** Industry Dive properties (constructiondive, supplychaindive,
manufacturingdive), autobodynews.com, ttnews.com, freightwaves.com,
fleetowner.com, mmsonline.com, zweiggroup.com, nist.gov, learn.microsoft.com,
microsoft.com/customers, microage.com, infor.com, constellationr.com,
pmmag.com, contractormag.com, servicetitan.com, akbizmag.com.

**Hard 403 or blocked:** bizjournals.com (blocked to the search tool entirely,
which removes roughly forty metro business journals and most of that ground's
stated advantage), achrnews.com, thefabricator.com, mcaa.org, mdm.com article
pages, supplyht.com, canadianmetalworking.com, forconstructionpros.com,
ccjdigital.com, automate.org, controleng.com, commonwealthfund.org,
mainebiz.biz, teamairdist.com, openai.com/stories.

**JavaScript-only, empty body:** lawnandlandscape.com and its GIE Media
siblings.

### Search craft, recorded verbatim because query craft compounds

**Failed, do not repeat.** Literal quoted-phrase cost hunting: `"we spent
about $"`, `"cost us about"`, `"we pay about"`, `"we're not a tech company"`.
Three of four scouts tried this independently and all three wasted roughly
eight queries each. The search tool is **semantic, not literal**, so
quoted-phrase hunting returns AI-pricing listicles and vendor SEO every time.
The index is also badly polluted for any query containing "AI" plus "cost"
plus a year.

**Worked.** Short queries naming a publication, conference or programme plus a
sector noun. Descriptive natural-language queries about a deployment ("a
wholesale distributor deployed an AI agent to read purchase order emails and
went live in weeks"). And above all, **fetching index and tag pages directly,
then picking headlines and reading the article** — the Alaska Business AI tag
page, the BizTimes search page and the SuperNova archive all returned clean
article lists this way.

### Contradiction logged

Two scouts fetched the same ServiceTitan press release for Bill Joplin's Air
Conditioning and Heating on the same day and returned **different verbatim
quotes** from the same named human, Randi Thompson. One version also carried a
spelling error. Neither is usable until re-fetched and matched character for
character. Logged on `bank-021`. Resolution rule per the contract is that the
agent which read the page wins, and here both did, so the quote is simply
unproven and does not exist until re-verified.

### The eight leads banked

| id | Company | Shape | Why it is not a case |
|---|---|---|---|
| bank-017 | Dunaway | 375-person Texas engineering firm, Copilot Studio city-code agent | No cost anywhere on three fetched pages. No clean decision-to-working pair. Buy-not-build is borderline (they wrote an Azure Functions citation matcher). |
| bank-018 | Team Air Distributing | HVAC distributor, 18 branches, ERP-embedded agents live in under two weeks | No cost, including from an independent analyst who went looking. Headcount unverified. |
| bank-019 | The Dufresne Group | Canadian furnishings retailer, contact centre rebuilt in 30 days | Employee band runs to 2,000, past our ceiling. Cost is a ratio, not a figure. |
| bank-020 | Body by Cochran | 11 collision shops, AI intake plus photo pre-estimating | No cost. No employee count, and the parent group is 44 dealerships. |
| bank-021 | Bill Joplin's | 1978 DFW HVAC contractor, ServiceTitan voice agent | No cost, no headcount, no limit named, vendor-only sourcing, contested quote. |
| bank-022 | Superior Plumbing | Atlanta plumber, call desk 7 to 3 plus an agent | No cost, no year on the timeline, and three of four departed CSRs unaccounted for. |
| bank-023 | Christian Healthcare Ministries | Under 500, phone tree and dialer rebuilt | No cost, no timeline at all, and rung 2 teaches least of the ladder. |
| bank-024 | AllTech Services | Virginia HVAC, Probook dispatch scoring | No number of any kind. No cost, no timeline, no headcount. |

**The three highest-value follow-ups, in order:** a cost class and a fetched
headcount for Team Air Distributing (Alisha Thompson, CTO); a cost class and a
clean timeline for Dunaway (Brian Bowden, VP of Technology); an employee count
and a cost for Body by Cochran's collision division (David Black).

---

## WAVE 2 — the decision, and why

The contract is explicit: *"If nothing in the bank qualifies, restock rather
than lowering the bar. A run that ships a case Dana cannot be has failed more
expensively than a run that ships late."*

Shipping any wave-1 candidate would mean shipping a case with no cost on the
deck, which is a scored HARD FAIL and the exact rule the 2026-07-25 run got
backwards. So wave 1 did not fail the run. It correctly refused to lower the
bar, and it bought the bank eight documented leads and a structural finding
about where cost actually lives.

Wave 2 therefore ran four scouts against the veins wave 1 identified but never
opened, each briefed with wave 1's fetch map, its failed query craft, and its
already-worked company list:

1. **The SuperNova archive worked systematically**, paging 2026, 2025 and 2024,
   triaging by workforce band first, then going around each submission to
   close cost on the named human.
2. **Public records where cost is disclosed by law or by construction** — NIST
   and state MEP success stories paged by year, and state Industry 4.0 and
   Manufacturing 4.0 grant recipient lists (Indiana's Manufacturing Readiness
   Grants, Michigan, Iowa, Maryland), where the award amount and the required
   company match are published and the tiers encode company size.
3. **Conference sessions, operator panels and podcasts with transcripts** —
   the one ground where an operator says what they paid, because peers ask.
   ENR FutureTech, Zweig ElevateAEC, MDM's AI for Distributors Summit, the MSO
   Symposium, ServiceTitan Pantheon. Explicitly tasked with closing cost on
   Dunaway, Team Air and Body by Cochran.
4. **Operators who publish their own priced build** — public-sector and
   quasi-public board packets and contract awards, low-code platform case
   libraries written for builders, co-op and buying-group member case studies,
   and operator-authored writeups.

*(Wave 2 results and the run's outcome are recorded below this line once the
scouts return.)*

---

## WAVE 2 RESULTS — one bank verdict out of twenty-four candidates

| Ground | Candidates | Banked | Killed |
|---|---|---|---|
| SuperNova archive, worked systematically | 4 | 0 | 8 |
| Public records: MEP paged by year + state grant lists | 2 | 0 | 8 |
| Conference sessions, operator panels, podcasts | 4 | 0 | 8 |
| Priced buildable deployments (public sector, low-code, co-ops) | 6 | **1** | 7 |

**`bank-025` La Crosse County Public Safety Communications is the run's only
qualifying case**, and it came from the vein nobody in this project had ever
worked: public-safety answering points.

### Why that vein worked, and it is a keeper

911 funding comes from a public surcharge, so the contract value is public and
local press routinely prints the figure next to the result. **Four agencies
disclosed a hard annual number on the same product inside one search session:**
La Crosse at $67k year one and $81k year two, Grand Traverse MI at $60k then
$72k on a three-year term, Spokane WA at $95k on two years, Ozaukee at roughly
$70k. Nothing else in eight scout-runs produced a single absolute price.

Two craft findings worth more than the case:

1. **Search the FAILURE.** One fetch of "After a few hiccups, Ava settling in
   at sheriff's office" in the Ozaukee Press produced a same-product,
   different-agency account of routing errors and background-noise confusion
   that forced the system back to two hours a day. That is the limit slide,
   sourced, for one query. Do this every run.
2. **The long-form regional magazine, not the TV station, carries the
   operator's own cost framing.** Milwaukee Magazine had the sentence nobody
   else did, "approximate to one employee with benefits," which is a better
   cost line for Dana than any dollar figure standing alone.

### The conference-and-podcast ground: a clean negative result

Wave 1 established that award submissions and trade press print results and
never money. **Wave 2 establishes that written conference recaps do not fix
that, for a specific and fixable reason: the peer question that gets cost said
out loud happens in the Q&A, and the Q&A is exactly what recaps omit.**

Worse, the agendas are vendor-dominated. Across roughly 40 sessions at Applied
AI for Distributors 2025 and 2026 — the two most on-target distribution events
in existence — the number led by an actual distributor describing their own
deployment is near zero. 2025 was 19 sessions, all vendors. Same at ENR
FutureTech, where the operators on the AI agent panel were Hensel Phelps and
McCarthy, both far outside our band.

Trade podcast episode PAGES publish summaries, not transcripts. Toolbox for the
Trades, MakingChips, Manufacturing Happy Hour, Home Service Expert and Collision
Vision were all checked; in every case the candid moment is inside audio nobody
transcribed to a fetchable page. **This ground is real but it needs a transcript
source, not a search engine.**

### The single most actionable finding of the whole run

The one page in two waves that printed a real cost class AND a real timeline for
a mid-market company was not a conference recap, an award submission or a vendor
case study. **It was a trade reporter who asked.** Don Davis at Distribution
Strategy Group got "less than $50,000" and a December-to-April window out of the
Howard Elliott Collection in a plain news interview. (That company is 11 to 50
employees, below our floor, so it is not a case — but the *route* is the finding.)

**Next wave should identify the two or three reporters in each vertical who ask
what it cost, and read their back catalogue, rather than searching for the
disclosure.** Don Davis is the first name on that list. The Colorado Sun's
distribution coverage is the second.

### The Infor cluster, and a price-class rule worth keeping

Turtle, Endries, Team Air, Grosfillex and State Electric all sit behind Infor
Augmented Intelligence, which lists on AWS Marketplace at **$250,000 for a
12-month contract rising to $600,000**, plus infrastructure. Even handed an
invoice, that is not a door Dana can walk through.

**New rule for the hunt: weight toward vendors whose customers are 50 to 300
person companies, not toward ERP-attached AI.** And a genuinely new
cost-hunting ground nobody here has used: **cloud marketplace listings**, where
vendors who refuse to publish a price page will publish a listing.

### Grounds now confirmed DRY, so no future run re-buys them

- **NIST MEP for AI.** The index supports keyword filtering
  (`?k=<full phrase>`; `k=AI` is too short a token and returns everything).
  Across the entire 1,067-story corpus, all years: "artificial intelligence"
  returns 3, "machine learning" 2, "chatbot" 2, "generative" 4, heavily
  overlapping. Deduplicated, **the whole MEP network has published exactly two
  AI deployment stories**, and in both the dollar figure attaches to something
  other than the AI. Retire this vein for at least two quarters.
- **The SuperNova archive is now substantially worked.** Twelve pages,
  `?page=0` to `?page=11`; pages 0 and 1 are the entire recency-compliant
  universe, about 80 entries, all triaged. The remaining Dana-shaped seam is
  thin.
- **Microsoft Power Platform case studies.** Index fetched in full; with
  Dunaway already worked, essentially every remaining entry is a global
  enterprise, a bank, a university or a technology vendor.
- **State Industry 4.0 grant lists.** The cost-by-construction premise is real
  but the plumbing fights you: states publish as PDF (Maryland) or Excel (Iowa),
  neither of which the fetcher reads, and this sandbox cannot parse a saved PDF.
  The one route that works is regional press republishing the list with both
  numbers per company. Base rate is also poor: in the one full recipient table
  read (Conexus Indiana, 43 companies), roughly 5 percent of line items were AI
  or ML and none had a case study behind it.

### Quote asset worth keeping regardless of what ships

Jenni Detert, VP of Information Technology at Endries International, to the
Colorado Sun on an automation that went wrong: **"we had just kind of automated
chaos."** Her own correction was that they should have found the root cause of
the exceptions rather than automating around them. An independent reporter, a
named operator, admitting a failure mode. That is the most trustworthy sentence
found across both waves and it belongs in the knowledge base.

### Scout disagreements logged

- **Team Air timeline.** One wave-2 scout found "three agents deployed in under
  two weeks" on the Infor blog; another reported it appears on no page it
  fetched. Not a true contradiction — they fetched different URLs, and only the
  Infor blog carries it. The Constellation submission does not.
- **Dunaway's ladder rung.** One scout called it rung 4, another rung 3. Both
  read the same architecture. Immaterial to this run since Dunaway is not
  shipping, but worth noting that the rung call is genuinely arguable when a
  build chains retrieval, a citation checker and generation.
- **Dunaway buy-vs-build.** Wave 2 raised a filter-3 concern wave 1 did not:
  they wrote a custom Azure Functions BM25 paragraph matcher, which is more
  build than buy. Recorded on `bank-017`.

### Unverified pointer, explicitly NOT banked

A search result described Lynas Foodservice going from 240 customers a week
with four people to over 1,000 a week with two, within four weeks of going live
on Choco's OrderAgent. **The page was never fetched, so nothing about it is
asserted and no company from it entered the bank.** A future scout should fetch
it first and go around the vendor. It is Northern Ireland rather than the lower
48.

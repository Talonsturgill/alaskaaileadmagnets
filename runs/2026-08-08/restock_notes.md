# PHASE 1 — BANK RESTOCK, 2026-08-08

Bank opened this run at **0 ship-ready against a par of 8**. Every one of the 16
seeded cases had been demoted to `lead` on 2026-07-28 when the cost-and-timeline
hard gate landed. So Phase 1 was a full restock, not a top-up.

---

## WAVE 1 — four scouts, four hunting grounds

| Scout | Ground | Sectors | Banks | Leads |
|---|---|---|---|---|
| S1 | Cost-disclosure grounds (conference talks, operator panels, podcasts, award submissions, association libraries) | Construction, mechanical and electrical contracting, trades, field service | **0** | 6 |
| S2 | Regional business journals + sector trade press | Logistics, freight, distribution, warehousing, manufacturing | **0** | 4 |
| S3 | Government, academic, procurement, state MEP | Manufacturing, utilities, public works, healthcare ops | **0** | 1 |
| S4 | Vendor libraries used strictly as leads, then corroborated | Professional services, clinics, hospitality, food processing and distribution | **0** | 4 |

**Wave 1 total: 0 qualifying cases, 15 leads, ~150 distinct queries, ~40 pages
fetched and read in full.**

Every single lead died on the same thing. Not on the story, not on the size, not
on the named human. On **cost and timeline.**

---

## THE FINDING, and it is the most valuable thing this run produced

All four scouts converged independently on one sentence:

> **Trade press reports outcomes and never asks what it ran. Cost gets said out
> loud only operator-to-operator: podcasts, independent newsletters, webinars,
> member forums, conference sessions.**

Three corollaries, each paid for with real budget this run:

1. **Literal cost-phrase searching is dead craft.** "we paid about", "what it
   cost us", "$3,000 a month", "under $50,000", "how much did it cost" — run
   dozens of times across three scouts, and they now return almost nothing but
   "Best AI Software 2026" SEO spam farms. S1 recorded it failing nine times out
   of nine. `knowledge/kb/HUNTING_GROUNDS.md` search craft rule 2 says to hunt
   these phrases. **That rule was true a year ago and is not true now.** It
   should be rewritten to say: hunt the VENUE, not the phrase.
2. **Reading a case-study or session INDEX page beats searching for cases.** One
   fetch of n8n's index returned 31 companies with industry and headline result,
   and the best lead of the whole run fell straight out of it.
3. **Asking the fetcher directly for "every verbatim sentence containing a time
   period or a dollar amount"** closes the hard gate on a suspect page in a
   single call.

---

## THE ACCESS MAP (this is now standing operational knowledge)

**Blocked or 403 to our fetcher. Do not spend budget again without a workaround:**

| Host | Status | Cost of losing it |
|---|---|---|
| `bizjournals.com` | hard 400 on the search API, whole regional network unreachable | **Severe.** This was supposed to be the single best mid-market-by-name source. Losing it is most of why S2's yield was poor. |
| `achrnews.com` and all BNP Media | 403 | Severe for trades. Carries the Leonard Splaine / UpSmith story with a named COO and a 25 percent number. |
| `forconstructionpros.com` | 403 | High for construction |
| `www.mcaa.org` | 403 | **Workaround found: `dev.mcaa.org` is a readable mirror** serving the full Smart Solutions case index |
| `thefabricator.com` | 403 | Medium |
| `mmh.com` | 403 | Medium, blocks the Productivity Achievement Awards |
| `naw.org` | 403 | Medium |
| `biztimes.com` | fetches, article paywalled | Low |

**Fetched clean and productive:** truckingdive.com, freightwaves.com,
fleetowner.com, truckinginfo.com, distributionstrategy.com, phcppros.com,
farm-equipment.com, precisionfarmingdealer.com, homepros.news,
hvac-blog.acca.org, constructiondive.com, nist.gov, n8n.io, choco.com,
numeo.ai, upsmith.com, and company-owned .com newsrooms generally.

**A decision the maintainer should make:** whether a bizjournals workaround is
worth building. It changes what an entire hunting ground is worth.

---

## THE LEADS, ranked by how close they are to being a case

**Tier 1 — missing exactly one or two facts, worth chasing:**

1. **Field Aerospace** (Oklahoma City, ~250 employees, aircraft modification for
   DoD). A government solicitation proposal took "about two weeks of work from
   multiple contributors"; now an 80 percent draft in about 25 minutes. Named
   humans with real titles (Shawn Tatum, Senior Program Manager; Jim Webster,
   CIO). Honest rung 4 that teaches the agent-washing lesson. **Missing: cost
   and timeline, both.** Also needs a filter-3 test, because they put a
   React/Node front end on self-hosted n8n.
2. **Colony Foods** (Massachusetts, 100+ employees, 25 trucks, family run since
   1988). The 3pm order cut-off: "I'd feel anxiety levels rise every day around
   3pm as my team worked to manually key in bulk orders before a cut-off time."
   CEO Joey Barbagallo confirmed on his own company newsroom. **Missing: cost,
   and a Colony-specific timeline.** Also a 70 vs 75 percent discrepancy to
   resolve.
3. **Capital Heating, Cooling, Electric and Plumbing** (Wisconsin, ~49 to 70).
   Owner Jason Fox on record: 3,000+ calls handled, about $397,000 revenue,
   61.61 percent booking on lead nurturing. **Missing: cost, timeline, and even
   which vendor.** Media-active owner, so one podcast away.
4. **Summit Electric Supply** (electrical distributor). President Dwayne Roberts
   in a Distribution Strategy Group Q&A, with a real before-and-after, a 76
   percent BOM match rate, and an unprompted admission of their own mistake
   ("We made it too wide open"). **Missing: cost, timeline, headcount.** Also a
   Sonepar operating company, which hurts identification.

**Tier 2 — structurally compromised:**

5. **Armstrong Plumbing** — the cleanest price comparison found all run
   ($5,000/mo for humans vs ~$950/mo for the agent) but **the named operator is
   now the vendor's COO**, and size is likely under 50.
6. **Lynas Foodservice** — has a timeline ("within four weeks of going live")
   and a great shape (240 customers/week with four people to 1,000+ with two)
   but **the load-bearing number is attributed to initials, "EJ"**, no cost, no
   verified headcount, and Northern Ireland weakens identification.
7. **Leonard Splaine Co.** — named COO and a 25 percent number, but **the only
   page carrying them returns 403** and the snippet rule forbids using them.
8. **CJB Industries** — has cost ($300,000) and timeline, but **the dollar
   figures belong to a data historian and quality project, not to the AI**, the
   AI was still in testing, and the work is from 2022.

**Tier 3 — kept for parts, not as cases:**
R.E. Garrison Trucking, Ward Transport, Four Ways Cargo, Five Star Home
Services, Roland Black, JMG Insurance, Genz-Ryan.

Genz-Ryan is worth a specific note: **no case, but CEO Jon Ryan is on record
with the most Dana-shaped sentence anyone found this run** — "You can go broke
spending all of your money on technology enhancements, so you have to be very
clear upfront about what you're expecting from it" — plus a copyable 60-to-90-day
evaluation rule. Keep it as sourced framing for a future case.

---

## SYNTHETIC-CONTENT WARNING

S2 caught a vendor blog publishing a distributor case study for **"Meridian
Supply Co."** with a first-name-only "Marcus, operations director" and
suspiciously tidy numbers (41 hours a week, 4.7 to 1.6 minutes). It has the
signature of an illustrative composite, not a real customer. **Do not use it.**
The snippet rule earned its keep more than once this run.

---

## WAVE 2 — four scouts, re-aimed at the gap

Wave 1 proved the bottleneck is not "find a good story", it is "find the price".
So wave 2 stops hunting grounds and starts hunting the two missing facts.

| Scout | Mission |
|---|---|
| W2-A | **Gap-close Field Aerospace.** One company, two facts. n8n community forum and webinars, YouTube transcripts, fieldaero.com newsroom, Oklahoma business press, govcon press, conference agendas. Plus the baseline discrepancy and the bought-vs-built test. Spare budget goes to Summit Electric. |
| W2-B | **The operator-audio seam.** FWD "WholeStory" episode "Digitise or Drift" with Andrew Lynas and Choco's CEO; Colony Foods' own newsletter archive; Jason Fox's podcast appearances; Distribution Strategy Group's podcast; and homepros.news mined archive-first rather than by query. Hunt episode TITLES, because the dollar figure is often in the title even when the audio is unreachable. |
| W2-C | **Award submissions and operator-written case libraries** — the one format where cost is present because the format demands it. DOE Better Plants "Better Project" awards, Supply and Demand Chain Executive Top Supply Chain Projects, CFMA Building Profits, dev.mcaa.org, IndustryWeek Best Plants, grant CLOSE-OUT reports (never announcements), state MEP impact PDFs. |
| W2-D | **Software user conferences and owner-authored writing** — the ground nobody touched. At a user conference the presenter is the CUSTOMER, and they tell a room of peers what it cost. ServiceTitan Pantheon, Acumatica Summit, Epicor Insights, SuiteWorld, Deltek Insight, Procore Groundbreak, Sage Transform, IFDA, ISA. Plus owner-written Substacks and company operations blogs at non-technology firms. |

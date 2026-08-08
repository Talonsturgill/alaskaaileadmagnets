# SCOUT S4 — vendor libraries used as leads (returned 2026-08-08)

**Result: zero banks, four leads.** Across ~33 searches and 12 full page fetches,
**zero customer-side cost disclosures.** Every path to a dollar figure ended in a
vendor list price, an SEO listicle, or a consultancy build-cost band.

## Leads returned

| Company | Size | Bottleneck | Rung | Missing |
|---|---|---|---|---|
| **Field Aerospace** (Oklahoma City, aircraft mod / DoD) | ~250 employees (stated on the fetched page) | A government solicitation proposal took "about two weeks of work from multiple contributors"; 50+ page solicitations; opportunities missed because nobody could read them all | 4 (self-hosted n8n workflow, human drew every step; vendor calls it "automation", honestly) | **COST and TIMELINE, both absent.** Everything else is strong. |
| **Colony Foods** (Massachusetts foodservice distributor, family run since 1988) | 100+ employees, 25 trucks | The 3pm order cut-off. "I'd feel anxiety levels rise every day around 3pm as my team worked to manually key in bulk orders before a cut-off time" | 3 (Choco OrderAgent, messy input to structured order; vendor brands it "agent") | **COST.** Timeline only partial (one year of use, generic vendor-wide 2 to 4 week claim). Also 70 vs 75 percent discrepancy across two vendor pages for what reads as the same metric. |
| **Lynas Foodservice** (Coleraine, Northern Ireland, foodservice wholesale) | not established from any fetched page | 240 customers a week all through email, order desk of four "couldn't cope anymore" | 3 (Choco OrderAgent) | **COST**, employee count, and the named human — the load-bearing 240-to-1,000 number is attributed to initials "EJ" with no surname or role. Timeline present ("within four weeks of going live"). |
| **JMG Insurance Corp** (US insurance brokerage) | not disclosed | Retraining the same back-office workflows across teams | 4, flagged as agent-washing (vendor says "first fully autonomous AI agent"; nothing in the release answers a field-guide question in the rung 5 column) | **COST, a measurable before and after, employee count.** Press release only. |

## Kills
Canary Technologies hotel voice (enterprises only, no operator named); Eve Legal
(technology company, no customer firm named); Valley Diabetes and Obesity (under
50 employees, vendor blog only); Delivery Hero / Vodafone / Stepstone / Trendyol
/ Seguros Bolivar from the n8n library (all over 1,000 employees); Boston Bone
and Joint Institute and O'Connor Insurance and Zero Zone (all snippet-rule
violations, never fetched).

## Craft that worked, for the next run
- **Read a vendor's case-study INDEX page instead of searching for cases.** n8n's
  index returned 31 companies with industry and headline result in one fetch, and
  Field Aerospace fell straight out of it. Do this first for any vendor.
- **A company's own newsletter or newsroom is a genuinely independent
  corroborating source** and is easier to find than trade press.
  `colonyfoods.com/about/news/2025/august` confirmed the deployment and gave a
  better CEO quote than the vendor page did.
- **Ask the fetcher directly for "every verbatim sentence containing a time
  period or a dollar amount."** One call proved Field Aerospace has neither.
- **Skip without fetching** any page whose title contains "cost" and a year. It
  is vendor SEO every time.

## Agent-washing exemplars found (worth a future teaching slide)
Choco brands a rung 3 extraction step "OrderAgent" and "AI agents". Kay.ai brands
what reads as rung 4 workflow execution the "first fully autonomous AI agent".
Neither page answers a single field-guide question in the rung 5 column.

## Where to hunt next in these sectors
Stop searching for cost. Search for venues where operators talk to operators.
(1) The FWD "WholeStory" podcast episode "Digitise or Drift" with Andrew Lynas of
Lynas Foodservice and Choco's CEO — audio, not indexed, and podcasts are the
single most likely place a wholesaler says a number out loud. (2) IFDA and NAW
conference sessions. (3) Direct outreach to Jim Webster or Shawn Tatum at Field
Aerospace, which is the best story found and needs exactly two facts. (4) The
Grocer's piece on The Menu Partners, surfaced but never fetched.

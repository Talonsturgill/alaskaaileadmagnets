# SCOUT W2-A — gap-close Field Aerospace (returned 2026-08-08)

**Result: clean negative on Field Aerospace, and Summit Electric Supply KILLED.**

## Field Aerospace — still a lead, and the blocker is not the one we thought

Venues checked and what each returned:
- `community.n8n.io` search for "Field Aerospace" — **zero topics**
- n8n YouTube channel — JS-rendered, fetcher saw only footer nav. **Genuinely unchecked rather than empty. The single remaining venue, and a long shot.**
- NAVAIR OSBP — **HTTP 403**
- Oklahoma business press, govcon press, Deltek customer content, aerospace trade press — **nothing on this deployment at all**
- AviationPros — directory profile only, but worth the fetch because it **corrected the headcount**

**Cost: still absent.** What exists and must NOT stand in for it: Field runs
self-hosted n8n on the Business plan, and n8n's public pricing page lists
Business at 667 EUR/mo billed annually — a vendor list price, not what Field
paid. The $30K of eliminated annual software cost is money that stopped going
out, not money that went in. Entirely unknown: **the internal developer hours
for the React/Node application**, the Deltek GovWin API subscription, hosting,
model spend.

**Timeline: nothing, anywhere.** No start date, no go-live, no build duration,
not even a publication date on the case study.

**Headcount, resolved:** n8n says ~250; AviationPros says "more than 600 people"
company-wide across 4 locations and separately "more than 250 employees from the
Oklahoma City area". n8n's 250 is almost certainly the OKC site. Both readings
stay inside the 50 to 1,000 band.

## THE BASELINE CONTRADICTION, now pinned

The vendor page disagrees with itself in three places:
- **stat card:** "25 minutes (vs 3-4 weeks before)"
- **body prose:** "about two weeks of work from multiple contributors"
- **Shawn Tatum's quote:** "probably two weeks of three or four people"

Two of three say two weeks. **The stat card is the outlier**, and the likely
explanation is that a marketer collapsed "three or four people, two weeks" into
"3-4 weeks". Shipping the stat card would have **inflated the baseline by about
2x on a vendor's arithmetic error.** The defensible number is Tatum's, because
it is on a named human's record and the prose agrees with it.

## THE REAL BLOCKER — filter 3, not cost

They self-hosted an open-source engine, **built a custom React front end and
Node.js backend over it**, and wired an API integration to Deltek GovWin. No
page names who did that work. If it took an internal software team, **Dana
cannot copy it and the case is dead regardless of what the cost turns out to
be.**

> To convert this from lead to case, exactly one question needs answering and it
> is not the cost question: **"Who built the React app and how long did it take
> them?"** If the answer is one internal IT person over a few weeks, this becomes
> a very strong case and the cost gate can likely be closed in the same
> conversation. If the answer is a dev team or an outside agency, kill it.

## SUMMIT ELECTRIC SUPPLY — KILLED, strike from the target list

Fetched the Distribution Strategy Group interview (Mark Brohan, 28 April 2026)
in full. It states plainly that **"Summit developed an AI-enabled tool"** — built
in house, not bought or configured. **Filter 3 fail.** It also establishes Summit
is a **Sonepar operating company** with access to enterprise tools and SAP-based
systems, making it a subsidiary of a global multi-billion-euro distributor
rather than a company Dana can be. **Filter 1 fail.** No cost, no timeline, no
employee count, no locations, no revenue anywhere in the article. There is no
embedded podcast or video on the page, so the wave 1 hypothesis that a spoken
version would leak a price never gets tested — the case is disqualified on
structure before cost matters.

## THREE CRAFT FINDINGS WORTH CARRYING FORWARD

1. **A company's own newsroom linking straight to the vendor page is a strong
   negative signal, and it is cheap to check early.** Field Aerospace's newsroom
   carries an item titled "Using AI for Client Responsiveness" whose href points
   straight back at the n8n case study. The company did not write anything, it
   linked the vendor. That reliably predicts no independent account exists
   anywhere. **Check the newsroom href before spending searches on trade press.**
2. **Read vendor stat cards against the vendor's own body prose and pull
   quotes.** The Field Aerospace stat card was wrong by 2x. This is a fast,
   repeatable check and **it belongs in the fact-checker's protocol.**
3. **The real gate on self-hosted open-source case studies is not cost, it is
   filter 3.** Self-hosted plus a custom front end plus an API integration is a
   software project wearing an automation label. Vendor case studies for
   self-hostable tools systematically omit who did the building, because the
   vendor's interest is in making it look effortless. **Future scouts working any
   open-source-tool case library should ask "who built it" FIRST, before cost
   and before timeline, because it kills faster and it kills more of them.**

## Where the scout would go next
"The venue class that has not yet been genuinely worked is the one ECONOMICS.md
ranks highest and that no scout has touched: **public procurement and grant
records, where cost is public by law**, and state MEP center project write-ups,
which publish engagement cost and duration as a matter of course because they
are federally funded and have to report it."

(Note: W2-C is currently working the award-submission and grant-close-out half
of exactly this recommendation.)

# SCOUT S2 — regional business journals + sector trade press (returned 2026-08-08)

**Result: zero banks, four leads.** Blunt finding, consistent across 12 outlets:
trade press reliably delivers the company name, the bottleneck in operator
language, one before-and-after number and a named human with a title, and
reliably delivers **no cost and no timeline**. The scout never once found both
on a fetched trade page.

## Leads returned

| Company | Size | Bottleneck | Rung | Missing |
|---|---|---|---|---|
| **Summit Electric Supply** (electrical distributor, a Sonepar operating company) | not disclosed on the page | Quoting. Turning a bill of materials into a quote took "hours or days". President: "the first person to respond with a quality quotation that includes accurate information has the lead" | 4 (ingest BOM, resolve SKUs, check inventory, flag gaps, hand to a human) | **COST, TIMELINE, headcount.** Best page read all run otherwise: named human, named bottleneck, real before and after, a 76 percent BOM match rate, and an unprompted admission of their own mistake ("We made it too wide open"). |
| **R.E. Garrison Trucking** (Alabama carrier with a brokerage arm) | not disclosed | Booking delivery appointments by hand, by phone, email and separate portals | 4 (Qued scheduling into McLeod TMS) | **COST**, its own timeline, size, and any named limit. ~60 hours saved in the first two months, no denominator. July 2024, at the edge of the date rule. |
| **Ward Transport and Logistics** (LTL carrier) | not disclosed | Rating LTL shipments, "slow, manual and error-prone" | 2 — and the AI label looks unearned against what the page describes | **COST, TIMELINE, size, baseline, limit.** Low or negative agentic teaching value. Keep only as a possible rules-engine-vs-AI contrast. |
| **Four Ways Cargo** (150 trucks, 15 dispatchers) | plausibly in band but no headcount | Dispatchers working DAT and Truckstop load boards by hand | 4 (vendor calls it "agent") | **COST, TIMELINE, and a named human — there is none at all.** Entirely vendor-sourced. A revenue-per-truck lift attributed to software in a market where rates move on their own, with no control. |

## Access map (worth keeping)
**Blocked or 403 to our fetcher — do not spend budget again without a
workaround:** bizjournals.com (search API returns a hard 400; the whole regional
network is out of reach), thefabricator.com (403), mmh.com (403), naw.org (403).
biztimes.com fetches but the substantive AI article is paywalled.
**Fetched clean and read in full:** truckingdive.com, freightwaves.com,
fleetowner.com, truckinginfo.com, distributionstrategy.com, phcppros.com,
farm-equipment.com, precisionfarmingdealer.com, numeo.ai.

Losing the entire bizjournals network removes the single best
mid-market-by-name source this ground was supposed to provide, and is most of
why the yield was poor. **Someone should decide whether a workaround is worth
building, because it changes what this ground is worth.**

## What did NOT work — do not repeat
Literal cost-phrase searches ("we paid about", "we spent about $", "cost us
about", "how much did it cost", "five figures", "$3,000 a month") are now almost
pure vendor-SEO bait. Every one returned AI-agent pricing listicles from
consultancies, not operators. **That craft note in HUNTING_GROUNDS may have been
true a year ago; on this run it failed nine times out of nine.** Pairing an
outlet name with operator language worked better for finding stories, it just
never found price.

## The vein to mine next
The operator Q&A run by a sector analyst firm (Distribution Strategy Group's
Summit Electric interview) had every ingredient except the two that gate us.
DSG, MDM and NAW all run **podcasts alongside these written interviews, and the
spoken version is where a price usually slips out.** Next run: find the audio or
transcript companion to a written operator interview rather than hunting the
written piece alone.

Two untouched seams that structurally contain cost because the format demands
it: **award submissions** (Supply and Demand Chain Executive "Top Supply Chain
Projects", Modern Materials Handling "Productivity Achievement Awards") and
MDM's paywalled case study library. MMH is 403 and MDM is paywalled, so both
need an access route decided first.

## Warning
This ground is dense with vendor content wearing trade-press clothing. A Farm
Equipment "practical guide" was bylined by the vendor itself. A vendor blog
produced a distributor case study ("Meridian Supply Co.", a "Marcus, operations
director", 41 hours a week, 4.7 to 1.6 minutes) detailed enough to look real and
almost certainly synthetic. **Do not use "Meridian Supply Co."** The snippet rule
earned its keep more than once this run.

## Kills
Danfoss, C.H. Robinson, XPO, ArcBest, Schneider National, Saia (all enterprise);
Western Express (no bottleneck, no numbers, no human); Gulf Relay (in-house
model, Dana cannot copy); Rectangle (vendor, customer unnamed); Ryan
Transportation (no before/after of its own); Messick's Equipment / DIS Corp
"Dex" and visorPRO (vendor content in trade dress); MKE Tech Hub "Synapse" (a
program, not a deployment); FleetWorks, Hey Bubba / TruckX (no customer named);
Ludwig Meister / LINC Systems / Watsco (MDM paywall, never fetched).

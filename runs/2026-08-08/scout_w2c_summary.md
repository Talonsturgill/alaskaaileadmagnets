# SCOUT W2-C — award submissions and operator-written case libraries (returned 2026-08-08)

**Result: zero banks, four leads.** The ground's thesis was never disproved. It
could not be executed, for a specific and recordable reason.

## THE BLOCKER — a transport failure, not a thesis failure

**`betterbuildingssolutioncenter.energy.gov` returned HTTP 503 on every attempt,
four times across the run, on three different paths.** `www.energy.gov/eere/iedo/
better-plants` fetches fine and links straight into the dead host.

The single most promising library on this ground — operator-written DOE Better
Project submissions, where **project cost and payback are part of the entry
format** — was unreachable today. **Independently re-confirmed by the showrunner
after the scout returned: still 503.** This is an outage on DOE's side, not a
block against us.

**This is the first thing the next run should retry.** If it is still 503, try
the PDF attachments under `/sites/default/files/attachments/`, served from the
same host on a different path, and extract with pypdf.

## NEW FETCH WALLS — add to the standing list
- `cfma.org` **403, and its chapter mirrors `mass.cfma.org` and `grcinn.cfma.org`
  are also 403.** CFMA Building Profits is fully walled. Wave 1's hope that a
  chapter mirror would work is dead.
- `sdcexec.com` 403 — Endeavor Business Media, same family as the known walls.
  **Treat ALL Endeavor properties as walled, including IndustryWeek.**
- `b2bea.org` 403.
- `betterbuildingssolutioncenter.energy.gov` 503.

## WHAT WORKED AND SHOULD BE REPEATED

**1. `nucleusresearch.com/roi-case-studies` is the best-shaped library found all
run, and it is fetchable.** A new ROI case study lands most months, each with a
named company, a payback period in months and an average annual benefit. Their
stated method counts software subscription, personnel time to implement,
training time and consulting over three years — **that is exactly the four-cost
structure `ECONOMICS.md` asks for, in a standing format.** The free abstracts
withhold the cost figures and the named humans, so the play is: use the index to
FIND a 50-to-1,000 non-technology company, then go around Nucleus to the vendor's
own case study and the company's local press for the name and the quote.

**2. Conference AGENDA pages are a gold seam for operator identification and
nobody is guarding them.** `appliedaifordistributors.com/agenda` yielded seven
named operators at named distributors describing their own deployments, in one
fetch, for free. Then `distributionstrategy.com` publishes a companion article
per panelist. **The pattern generalises: find the 2026 sector conference, fetch
/agenda and /speakers, harvest the operator names, then search each name for the
recap or the podcast. Do this BEFORE searching for cases, not after.**

**3. `nrucfc.coop` and `cooperative.com` (NRECA) are fetchable and genuinely
peer-to-peer.** Electric cooperatives are a strong structural fit for this
series — member-owned, 50 to 1,000 employees, deeply ordinary, and **Anchorage
has three of them, so the translation writes itself.** The AI supply is real and
growing. What is missing is price, every time.

## STOP DOING
- **Any query pairing a sector noun with "AI" and "cost" or "per month" or
  "pricing".** Five variants across dental, veterinary, contractor answering
  services and distributor order entry returned **100 percent SEO listicle
  farms.** Wave 1 said this. It is worse than wave 1 said: **the vertical-AI-
  pricing SEO farm has now fully colonised every operator noun.**
- Vendor case studies as anything but a lead.
- Award pages that aggregate winners with vendor-supplied blurbs (FreightWaves AI
  Excellence). One fetch produced 20 vendors and zero operator baselines.

## Leads
| Company | Why it is only a lead |
|---|---|
| **Mountain View Electric Association** (Colorado co-op, 58,000 members, 5,000 sq mi, 3,600+ miles of line) | Vegetation management planning with satellite and LiDAR. Planning cycle months to 2 weeks; 56 miles trimmed in 136 days against a 336 day projection. **But the 40 percent cost figure compares two different contractors, not before-and-after AI. No MVEA employee is quoted at all — the only named human is the tree contractor. No cost. Rung 3.** |
| **New Horizon Electric Cooperative** (South Carolina) | Three sentences inside a roundup. **Two bottlenecks, not one. No cost, no timeline, no headcount, no vendor, no baseline.** Has the rarest ingredient though: CEO Bobby Smith on the record by name and title. |
| **The Howard Elliott Collection** | Pure vendor case study. **No headcount, no cost, no exception rate.** Also a unit switch flag: "several hours to 15 minutes per order" on the case study versus "4 hours a day" in the vendor's press material — different bases. |
| **FORUM Credit Union** (Indianapolis, six-person accounting dept) | Cleanest capacity-to-cash conversion seen all run (department carries ~3x the balance sheet without hiring, two hires avoided). **But no named human at all, no disclosed deployment cost, and AI involvement is unestablished — I will not call something AI because the vendor category is trending.** |

## Notable kills
- **Summit Electric Supply — killed again, independently.** "They BUILT their
  AI-enabled quoting and account analysis internally and draw enterprise tooling
  through parent company Sonepar." Filter 3. (W2-A reached the same verdict from
  the same article. Two scouts, same kill.)
- **Dairyland Power Cooperative** — built the platform themselves and now resell
  it to other co-ops, making them a technology vendor in this story, not an
  adopter.
- **Helm Mechanical** (MCAA Smart Solutions via the dev.mcaa.org mirror) — no AI
  anywhere in it, a digital field-sketch tool. Good number (a day to five
  minutes), which is why it hurt to kill.
- **Sauder Woodworking, NFI, Flexport, Uber Freight, Grainger, Graybar, ADI
  Global** — all over the ceiling.

## The scout's closing line, which is now the run's central question
> "At some point the cheapest path to a qualifying case is not another search,
> it is one email."

# SCOUT W3-B — association deck indexes and co-op governance documents (returned 2026-08-08)

**Result: clean negative. Zero qualifying cases.** 29 searches, 14 pages fetched
in full. The hard gate killed every candidate on the same two facts as the
previous eight scouts.

## THE MOST IMPORTANT FINDING — it corrects the brief

> **`r.jina.ai` is DEAD in this environment. It returned HTTP 401 on every
> attempt** (cooperative.com PDF, mvea.coop page, mvea.coop PDF). Do not budget
> time for it.
>
> **But WebFetch now reads PDFs natively.** It pulled the full text of the NRECA
> January 2026 advisory PDF straight from the `.pdf` URL and saved the binary
> locally.

The one PDF it could not read was an 8.2 MB scanned board packet with no text
layer. For those, WebFetch saves the binary to the tool-results directory and
**the local Read tool with a `pages` range is the next move** — untested this
run.

**Net effect: the PDF seam is OPEN, just through a different door than wave 2
reported.** (Wave 2's W2-D reported Jina working on four AGC decks; it has since
started 401ing. Either way, WebFetch native is the route now.)

## SEAM A — association deck indexes outside construction: nothing, for a
## structural reason worth logging

**The deck indexes themselves are behind 403s.**
- `publicpower.org/national-conference-presentations` — 403
- `cooperative.com` — serves article pages, but **401s its member-area PDFs**
- `cmtc.com` — now 301s to `roadmap4innovation.com`, which 404s the case-study index
- `mvea.coop` — 403 on both the page and the PDF

> **The pattern: an association will let you read its magazine but not its
> handouts.** AGC worked because AGC leaves its handouts on an open path.

**Next scout should hunt for OPEN handout PATHS, not handout index pages** — try
guessing `/wp-content/uploads/` and `/sites/default/files/` patterns from a known
filename, which is how the mvea and owenelectric PDF URLs surfaced in search
results in the first place.

## SEAM B — co-op governance documents: structurally sound, blocked on discovery

The blocker is discovery, not disclosure. Search engines cannot find a dollar
amount inside a co-op's board minutes because **the query "board minutes
artificial intelligence approved" is now fully colonised by AI-minutes-drafting
software SEO** (Diligent, OnBoard, Convene).

**Add to the proven-dead-craft list.** Two other query families died the same way
this run: "AI scribe per provider per month" returns nine vendor pricing-guide
pages and zero named practices; "AI dispatch cost trucking" returns one vendor's
content farm exclusively.

## WHAT TO TRY NEXT, in the scout's priority order

1. **Invert the co-op search.** Do not search minutes for AI. Search minutes for
   the ordinary governance verb and read them for what turns up. Fetch
   `owenelectric.com/sites/default/files/YYYY-MM/*-web-posting.pdf` month by
   month — a known-open path with a predictable filename pattern. If those
   minutes itemise vendor contracts by dollar amount, the seam is proven and it
   becomes a mechanical crawl.
2. **IRS Form 990, Part VII Section B.** Nonprofits — including many electric
   co-ops and every nonprofit health system — **must list their five highest-paid
   independent contractors over $100,000 with vendor name, exact amount and a
   description of services. That is a cost disclosure public by law and nobody is
   mining it.** It gives no timeline and no before/after, so it is a pairing
   source, not a standalone.
3. **Chase the underlying decks, not the panel writeups.** The APPA piece was a
   summary of a June 2025 panel; the slides behind it are where a cost would be,
   and both named operators are reachable and clearly willing to talk.
4. **Distribution Strategy Group is a live vein and is not walled.** It publishes
   operator-first pieces on genuinely Dana-sized distributors and its Applied AI
   for Distributors speaker roster is a clean list of named operators at named
   distributors. It has produced four bank entries across runs. **It reliably
   omits cost — which now looks less like a DSG failing and more like the central
   fact of this whole hunt.**

## Leads
| Company | Missing |
|---|---|
| **Building Products Inc.** (Watertown SD, building materials distributor, ~30 sales reps) | Reps spent only ~30 percent of time selling; Pronto (free add-on to their existing Proton CRM) writes call notes and drafts follow-ups. 10 to 15 min saved per stop. **Total headcount unverified, no before-and-after operational number, "free add-on" is not a cost class, no decision-to-working span.** Rung 3. |
| **CDE Lightband** (municipal utility, 86,000 customers) and **City of Santa Clara, Utah** | Board records back to 1938 made searchable; load forecasting at 92 percent accuracy, savings "from about $15,000 to a quarter million in one month". **Single month, no baseline period, no definition of what savings measure against — cherry-picked-window and absent-baseline pattern. Public bodies. Probably built, not bought.** |
| **Palmer Holland** (employee-owned specialty chemical distributor, Ohio) | **No result at all.** The piece reads as a rewrite of the company's own press release — launch language, aspirational CIO quote, no independent number, no limit. Press-release-laundering tell. |

## Kills
Horry Electric Cooperative (2022 pilot, fails recency); Magellan Aerospace and
zBeats (no numbers, and zBeats is a technology company); Uptool (vendor profile,
names no customer shop); six Paperless Parts case studies (killed at intake on
the known base rate — **vendor case study libraries are now 4 for 4 on omitting
cost, headcount and timeline**); Graybar, Grainger, ADI Global (over the ceiling).

## THE STRUCTURAL CONCLUSION
> "Across roughly 230 queries and 85 pages by nine scouts, **the joint
> distribution of 'bought from a vendor' and 'disclosed what we paid' is close to
> empty in published sources.** The one hit, Peckham, disclosed precisely because
> it had built something almost free. **The gate may not be reachable by search
> alone.** If the bank has to be stocked, the highest-expected-value move is
> probably not a tenth scout — it is picking two or three of the nineteen leads
> with a named, reachable operator and asking them the two missing questions
> directly."

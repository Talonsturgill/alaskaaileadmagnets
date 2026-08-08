# CASE FILES - RUN POST-MORTEM, 2026-08-08

**No case shipped. The routine did not lower the bar, and that was the correct
call.** This document is the run's actual product, and it is worth more than a
weak deck would have been.

---

## WHAT HAPPENED, in one paragraph

The bank opened at **0 ship-ready against a par of 8** - every one of the 16
seeded cases had been demoted to `lead` on 2026-07-28 when the cost-and-timeline
hard gate landed. Phase 1 ran a full restock. **Ten scouts across three waves,
roughly 250 queries and 85 pages fetched and read in full, returned zero
qualifying cases.** Every single failure was the same two facts: no disclosed
cost, no disclosed decision-to-working timeline. The stories are out there, in
quantity, at exactly the right size, with named humans and real before-and-after
numbers. **The price is not on the page.**

Phases 2 through 9 never ran. There is no deck, no copy, no gate result and no
score, because there was nothing honest to build one from.

---

## THE FINDING, which is the reason this run was worth running

Four independent scouts in wave 1, working four different hunting grounds,
converged on the same sentence without conferring:

> **Trade press reports outcomes and never asks what it ran. Cost gets said out
> loud only operator-to-operator.**

Wave 2 confirmed it and found where operator-to-operator actually lives. Wave 3
tested that seam directly. Three things came out of it that change how this
series hunts:

### 1. Operator conference DECKS carry cost slides. Abstracts never do.

A deck from **Peckham Industries** (family-owned paving and materials
contractor, 100 years old) presented at the AGC Technology Conference carries a
literal itemised annual cost slide: **$19.70 in tokens, $840 vector store,
$2,760 Azure App Service, about $3,000 a year**, framed as "the equivalent of a
$3,000 home-improvement budget." They even disclosed the failed experiment -
nearly $1,000 in one day on fine-tuning before deciding they did not need it.

Nothing else across ~250 searches produced a disclosure like that. The reason is
structural: **when an operator presents to a room of peers, they put the invoice
on the slide, because the room will ask.**

### 2. The conference seam publishes almost nothing, and that is provable

The full agenda for **Applied AI for Distributors 2026** names seven operating
distributors who stood on stage and described their own deployments - including
one on an 18-month journey and a leader panel *explicitly about how they
evaluate ROI*. **None of it is recorded, transcribed or recapped on the open
web. The disclosure happens in the room and dies there.**

### 3. The tension inside our own filter

This is the part that needs a decision, and it is the deepest thing the run
found. Wave 3 went looking specifically to test it and came back with it
sharpened rather than softened:

> **Cost is the payoff of a build-it-cheap talk.**
>
> Peckham put its $3,000 on a slide precisely *because* the punchline was "we
> built this for three thousand dollars and we are not data scientists" - and
> that same fact fails them on filter 3, because Dana cannot copy a Python
> build. When a company **bought** from a vendor, the price is usually under an
> NDA or simply not the point of the talk, so it never goes on the slide at all.

**Our filter requires both a disclosed cost AND a bought-not-built solution. In
published sources, that intersection is close to empty.** Wave 3 opened twelve
operator decks specifically hunting it. Six were vendors or consultants, three
were companies over the ceiling, and the three genuine operator-told segments
disclosed neither price nor go-live. The only dollar figure found in an AI
context all day was a published $20 a month list price on a teaching slide.

The cleanest single illustration of the whole problem is the ACEC report on AI
in engineering: **twenty named firms, twenty CTO-level quotes, and not one cost,
timeline, employee count or before-and-after number in the entire document.** It
is a posture survey, not a deployment record, and most of what the web publishes
about mid-market AI is the same thing wearing different clothes.

That is not a scouting failure. It is a structural property of what gets
published, and it will reproduce every run until something changes.

---

## THE DECISION THIS PUTS IN FRONT OF THE MAINTAINER

Three options. They are not mutually exclusive and the first is by far the
cheapest.

**A. Fund one phone call.** Four leads are missing only the price and have a
named executive already on the record talking publicly about the deployment.
Any one of these calls converts a lead into a shippable case:

| Who | Company | Why they will talk |
|---|---|---|
| **Joey Barbagallo** | Colony Foods (MA foodservice distributor, 100+ employees, 25 trucks, family run since 1988) | Publishes a **monthly newsletter under his own byline** on his own domain, already wrote about this exact deployment, has sat for panel interviews |
| **Colleen Daly** | The Howard Elliott Collection (home decor wholesaler) | Already **presented the 18-month journey on stage** in June 2026, including where vendor expectations were not met |
| **Dan Decker / Russell Bradshaw** | Peckham Industries | Already put their **itemised cost slide** in front of a conference room |
| **Rob Spencer** | CAMP Facility Services (Houston) | Presented at AGC Tech Con 2025; no deck posted |

The scout's own conclusion, and I agree with it: *"At some point the cheapest
path to a qualifying case is not another search, it is one email."*

**B. Split the hard gate.** Keep cost-and-timeline as the bar for a full case
file, but allow a second, clearly-labelled format for a verified deployment with
a great before-and-after where the price genuinely is not public - with the
missing number named out loud as the thing we could not get. That is honest, it
is still useful to Dana, and it would have shipped four times today. **This is a
doctrine change and it is the maintainer's call, not the routine's.**

**C. Accept a slower cadence.** Ship when a case clears all seven, and bank
leads on the days it does not. Today's run produced a materially better bank and
a much sharper hunting method. That is a real output, just not a post.

---

## WHAT THE RUN BANKED

`ledger/bank.json` gained **bank-017 to bank-024**, eight fully-formed leads,
each carrying the whole entry plus a `qualification` block naming exactly which
filter parts hold and exactly what a scout must go find. Highlights:

- **Field Aerospace** (~250 employees, Oklahoma City, DoD aircraft modification).
  Proposals took "about two weeks of work from multiple contributors"; now an
  80 percent draft in about 25 minutes. **Blocked on filter 3, not cost:** they
  built a custom React/Node app over self-hosted n8n and no page says who did
  that work. One question converts it: *who built the React app and how long did
  it take them?*
- **Colony Foods.** The 3pm order cut-off, in the owner's own words. Corroborated
  on his own newsroom. Missing only price and a company-specific timeline.
- **Capital Heating.** 3,000+ calls, ~$397,000 revenue, owner on record.
  **Recommend retiring** - two waves failed to find where he says the price.

---

## THINGS THE RUN CAUGHT THAT WOULD HAVE SHIPPED AS ERRORS

Worth recording, because these are the honesty machine working:

1. **A vendor stat card inflating its own baseline by ~2x.** The Field Aerospace
   page says "25 minutes (vs 3-4 weeks before)" on a stat card while the body
   prose and the named human's pull quote both say **two weeks**. The likely
   cause is a marketer collapsing "three or four people, two weeks" into "3-4
   weeks". **Reading stat cards against the vendor's own pull quotes belongs in
   the fact-checker's protocol.**
2. **A synthetic case study.** A vendor blog published "Meridian Supply Co." with
   a first-name-only "Marcus, operations director" and suspiciously tidy numbers.
   It has the signature of an illustrative composite. **Do not use it.**
3. **Two companies that build and resell, presented as adopters.** Summit
   Electric ("Summit developed an AI-enabled tool", plus a Sonepar subsidiary)
   and Dairyland Power (built the platform and now sells it to other co-ops).
4. **A deck with no AI in it.** Casella Construction's numbers were real and
   good; the technology was HR software and Power Platform.
5. **An operator who is now the vendor's COO**, quoted as an independent customer.

---

## OPERATIONAL INTELLIGENCE FOR THE NEXT RUN

**Reading PDFs, and the two scouts disagreed so both accounts are recorded.**
`https://r.jina.ai/<pdf-url>` converts a PDF to text and opened the conference
deck seam. One scout hit consistent 401s and concluded it was dead; a later
scout established it has a **rate quota** that recovers after roughly fifteen
minutes, so **a 401 means wait, not blocked** - pace it one call at a time,
never two in parallel. Separately, WebFetch read at least one PDF natively from
its `.pdf` URL. What is certain: **poppler is not installed in this sandbox**,
so a subagent with no Bash tool has no local PDF path at all, and image-only
decks with no text layer are a dead end rather than a retry. Anything read
through Jina mixes verbatim strings with paraphrase and **must be re-extracted
before it ships**.

**The venues, both newly found and both open:**
- `https://www.necaconvention.org/presentations/` - a public, unauthenticated
  index of **64 downloadable decks** from the NECA 2025 convention, electrical
  contractors presenting to electrical contractors, with direct PDF links. NECA
  posts within days of the event. **Roughly 50 of those decks are unwalked, and
  the Peckham precedent says the cost slide hides in the session that is not
  titled about AI.**
- `archive.tech-con.agc.org/2025-session-presentations/` - the same shape for
  general contractors, ~25 decks a year, roughly 3 in 25 being genuine
  operator-told deployments. **Only 2024 and 2025 exist.** The 2026 conference
  ran 4 to 6 August 2026, two days before this run, and its index still returns
  404. **Check again in two to four weeks** - that is the freshest possible batch
  and it is exactly our sector.

**Unmined and fetchable, for the next run:** `abc.org/Technology/AI-Resource-Guide`,
`constructionexec.com` and its Top Tech Product List, `smacna.org`, and IFMA
**chapter** presentation pages (chapter pages are far more open than national
bodies). Plus two structural cost sources nobody is touching: **IRS Form 990
Part VII Section B**, where nonprofits must list their five highest-paid
contractors over $100,000 by name and exact amount, and **cooperative board
minutes on known-open paths** (search the ordinary governance verb, never "AI",
because "board minutes artificial intelligence approved" is now fully colonised
by minutes-drafting-software SEO).

**Dead craft, confirmed by three independent scouts:** literal cost-phrase
searching ("we paid about", "what it cost us", "$3,000 a month"). The
vertical-AI-pricing SEO farm has fully colonised every operator noun. One scout
logged it failing nine times out of nine. **`knowledge/kb/HUNTING_GROUNDS.md`
search craft rule 2 currently instructs scouts to hunt exactly these phrases and
must be rewritten to hunt the VENUE instead.**

**The access map** (now standing operational knowledge):

| Host | Status |
|---|---|
| `bizjournals.com` | **hard 400 on search - the whole regional network is unreachable.** This was our best mid-market-by-name source; losing it materially reduces what an entire hunting ground is worth |
| all BNP Media (`achrnews.com`) | 403 |
| all Endeavor Business Media (`sdcexec.com`, IndustryWeek) | 403 |
| `cfma.org` **and its chapter mirrors** | 403 - fully walled |
| `forconstructionpros.com`, `thefabricator.com`, `mmh.com`, `naw.org`, `b2bea.org`, `whattheythink.com`, `printweek.com` | 403 |
| `www.mcaa.org` | 403. `dev.mcaa.org` mirrors the Smart Solutions case index but **NOT the news paths, whose article URLs 404** (a wave-1 finding that wave 3 partially retracted) |
| `tech-con.agc.org`, `mepconference.com` | Salesforce Lightning / 403. **Use the `archive.` subdomain for AGC** |
| `betterbuildingssolutioncenter.energy.gov` | **503 today, independently re-confirmed.** A DOE outage, not a block. This is the best award library in existence for cost and payback and it was unreachable. **Retry first next run.** |

**Fetchable and productive:** truckingdive.com, freightwaves.com, fleetowner.com,
distributionstrategy.com, homepros.news, hvac-blog.acca.org, constructiondive.com,
nist.gov, nrucfc.coop, cooperative.com, nucleusresearch.com,
appliedaifordistributors.com, archive.tech-con.agc.org, and company-owned
newsrooms generally.

**Two source types worth promoting to standing craft:**
- **A company's own owner-written newsletter.** `colonyfoods.com/about/news/` is
  a monthly archive under the owner's byline that independently corroborated a
  vendor's account in his own voice. It is the only source type in three waves
  that gave us an operator describing his own deployment without a vendor
  holding the pen.
- **Conference agenda pages as operator-identification maps.** One fetch of
  `appliedaifordistributors.com/agenda` yielded seven named operators at named
  companies. Harvest names first, then hunt each name. Do this *before* searching
  for cases.

**A negative signal worth checking early and cheaply:** if a company's own
newsroom links straight to the vendor's case study rather than telling the story
itself, no independent account exists anywhere. Check the newsroom href before
spending searches on trade press.

---

## THE ONE THING TO CHANGE NEXT RUN

Stop opening with an open-ended hunt. **Open by walking conference deck indexes
through the PDF reader**, because that is the only venue in three waves that
produced a real itemised cost. Then, if the deck seam is dry, spend the run's
budget on one outreach email to a named executive who has already talked
publicly - rather than on a fourth wave of searching for a number the web does
not contain.

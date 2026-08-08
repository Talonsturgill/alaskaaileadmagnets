# SCOUT W2-D — software user conferences and owner-authored writing (returned 2026-08-08)

**Result: zero banks, one genuinely good lead, two thin ones.** And the single
most useful craft discovery of either wave.

## THE UNLOCK

> **Operator conference DECKS carry cost slides. Session abstracts never do.**

The **Peckham Industries** deck (family-owned paving and materials contractor,
100 years old, New York and New England) presented at the AGC Technology
Conference on 6 August 2025 carries a **literal itemised annual cost slide**:

| Line | Amount |
|---|---|
| Tokens, year to date | $19.70 |
| Vector store database, annualised | $840 |
| Azure App Service, annualised | $2,760 |
| **Total** | **~$3,000/yr**, framed on the deck as "the equivalent of a $3,000 home-improvement budget" |

They also disclosed the cost of the experiment they abandoned: **nearly $1,000
in one day** on fine-tuning, before concluding they did not need it.

**No trade article, no vendor case study and no press release produced anything
like that across roughly 200 searches and 70 fetches.** The reason is
structural: when an IT director stands in front of a room of other IT
directors, they put the invoice on the slide, because the room will ask.

**Hunt the DECK, not the agenda.**

## THE TOOL — `https://r.jina.ai/<pdf-url>`

Converts a PDF to readable text. The normal fetcher returns raw binary for PDFs
and the Read tool fails without poppler installed. **Prefixing the PDF URL with
the Jina reader worked every time, across four separate decks.** This reopens
the entire universe of conference handouts, association white papers and
government PDFs. It also partially defeats 403 walls, though not real paywalls.

**Caveat for the fact-checker:** the reader returns a mix of verbatim strings
and paraphrase across calls. The Peckham dollar figures were consistent across
two separate calls, but **anything read through Jina must be re-extracted from
the PDF directly before it ships.**

## THE VENUE — `archive.tech-con.agc.org/2025-session-presentations/`

A public index of downloadable contractor decks from the AGC Technology
Conference. One fetch returns ~25 sessions with title, presenter and direct PDF
link. **Roughly 3 in 25 are genuine operator-told deployments**; the rest are
vendors and consultants. The live `tech-con.agc.org` 301-redirects to a
Salesforce Lightning portal that renders as a loading error — **always use the
`archive.` subdomain.**

**Highest-probability next target:** the 2026 AGC Technology Conference ran
4 to 6 August 2026 in Minneapolis, **two days ago**.
`archive.tech-con.agc.org/2026-session-presentations/` returns 404 today.
**Check again in two to four weeks.** That is the freshest possible batch of
contractor-authored decks and it is exactly our sector.

## WHY PECKHAM STILL IS NOT A CASE
Fails three of seven. **(3)** They built it in Python — Chainlit, Azure OpenAI
GPT-4o, LangGraph, NLP-to-SQL — so Dana cannot copy the move. **(4)** No
measurable before and after anywhere in the deck; nobody says how many ad hoc
reports stopped or how much time came back. **(5)** Cost is disclosed
beautifully but **the timeline is not**, and that is the hard gate on its own.
Employee count also unverified from any fetched page.

The $3,000 is real and thrilling and **it is measuring an input, not an
outcome.**

## THE STRUCTURAL OBSERVATION — and this is the run's central finding

> **Cost gets disclosed by people who BUILT something cheap, and stays hidden by
> people who BOUGHT something.**
>
> Peckham put its $3,000 on a slide precisely because the punchline was "this
> was almost free and we are not data scientists." A company that signed a
> licence has a procurement reason not to say the number.
>
> **If the run keeps requiring both a disclosed cost AND a bought-not-built
> solution, the intersection is genuinely thin on the open web**, and the
> realistic route to it is a fifteen minute call with a named presenter rather
> than another sixty searches.

That is a real tension inside the qualifying filter and it needs a maintainer
decision, not another scout.

## Other leads
- **The Howard Elliott Collection** — 18-month journey, VP Colleen Daly
  presenting at Applied AI for Distributors, June 2026. Session abstract only;
  no bottleneck in operator language, no verbatim quote, no cost, no headcount.
  The abstract says she will discuss **where expectations were met or exceeded
  and what vendor evaluation criteria distributors should demand before
  signing** — that is exactly the honest-limit material, and it is behind the
  session, not on the web.
- **CAMP Facility Services** (Houston, facility and construction management) —
  Rob Spencer presented "AI: Keys to Real World Application and Success" at AGC
  Tech Con 2025, but **no deck was posted**. Worth one outreach email, not a
  research hour.

## Notable kills
- **Casella Construction** — read the full deck. Genuinely good numbers (payroll
  from 2 FTE to 1 while headcount grew, AP automation saving 40+ hours a month,
  onboarding from days to hours) but **the deck names no AI anywhere.** It is HR
  software plus Microsoft Power Platform. Fails the premise.
- **Border States** — 976 percent ROI, $21M inventory reduction, 1.3 month
  payback, all disclosed. Far over 1,000 employees. The disclosure exists at
  enterprise scale and not at Dana's.
- **HSO** — a Microsoft partner pitching Power Platform, not an operator.
- **Benike Construction** — session is upcoming 9 September 2026, nothing exists
  yet. Worth a look after that date.

## New fetch walls
`whattheythink.com` (403 direct; Jina gets the paywall stub only),
`printweek.com` (403), `b2bea.org` (403), `tech-con.agc.org` live site
(Salesforce Lightning, unrenderable — use the `archive.` subdomain),
`agc-community.agc.org` (same).

## Confirmed dead
**Owner-authored writing via search is completely SEO-poisoned.** Any query
mixing first-person operator language ("our shop", "we rolled out", "family
owned") with AI returns tool listicles and consultancy pricing guides, three
deep, every time. Do not run it again without a hard domain restriction to a
known operator's site.

**Vendor user-conference marketing** (Acumatica, ServiceTitan, Deltek, Global
Shop) publishes only its own product announcements. The customer sessions exist
but their content is never on the open web. Four fetches, zero customer names
with numbers.

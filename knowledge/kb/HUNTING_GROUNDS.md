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

**2. Hunt the VENUE, not the cost phrase. The phrase craft is dead.**

This rule used to say: search "what it cost us", "all in", "we paid about".
**Do not do that.** On 2026-08-08 four independent scouts ran that craft across
six sector framings and it failed every time. S1 logged nine failures out of
nine attempts. The vertical-AI-pricing SEO farm has fully colonised every
operator noun, so any query pairing a trade noun with AI and a cost word
returns "Best AI Software 2026" listicles and consultancy pricing guides,
three results deep, every time. W3-B found the same colonisation on a fourth
family of queries ("board minutes artificial intelligence approved" now
returns AI-minutes-drafting vendors).

**What replaced it.** Cost is a property of the VENUE a story was told in, not
of the words in it. Go to the venue first and read what is there:

- **Operator conference DECKS, not agendas and not recaps.** When an operator
  presents to a room of peers they put the invoice on the slide, because the
  room will ask. This is the only venue in ~250 queries that produced a real
  itemised cost. Decks are PDFs: use `scripts/fetch_pdf_text.py --money`,
  which prints every line carrying a dollar amount or a duration.
- **The non-AI-titled session.** The cost slide hides in the session about
  service, prefab, systems integration or labour, presented by an operator.
  The session titled about AI is usually a vendor or a consultant.
- **Conference AGENDA and SPEAKER pages, used as operator-identification
  maps.** Harvest the named operators at named companies FIRST, then hunt each
  name. Do this before searching for cases, not after.
- **A company's own owner-written newsletter or newsroom.** The one source
  type that gave us an operator describing his own deployment with no vendor
  holding the pen.
- **Records where cost is public by law.** Procurement files, grant
  close-outs (never announcements), and nonprofit filings.

**And know what the venue costs you.** Cost gets disclosed by people who BUILT
something cheap, and stays hidden behind people who BOUGHT something. See
`ECONOMICS.md`. Budget for that: a deck seam is rich in price and thin in
copyability, which is the opposite of what filter 3 wants.

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

## THE ACCESS MAP

**Read this before you spend a single fetch.** On 2026-08-08 ten scouts
independently rediscovered the same walls. Nobody should ever pay for that
again. Status is stated per TOOL, because the tool matters more than the site.

**Two different fetchers exist in this pipeline and they get different
answers:**

- **WebFetch** is what a `case-scout` has. Many sites return 403 to it
  specifically.
- **A plain browser-UA GET from Bash** (what `scripts/fetch_pdf_text.py` does,
  and what the showrunner and fact-checker can run) gets through several of
  those. **A "403" in a scout report means 403 to WebFetch. It does not mean
  the site is walled.**

| Host | WebFetch | Browser-UA GET from Bash | Note |
|---|---|---|---|
| `achrnews.com` and BNP Media | 403 | **200, deep article paths too** | recorded as a severe loss on 2026-08-08; it was not one |
| `www.mcaa.org` | 403 | **200** | `dev.mcaa.org` mirrors the Smart Solutions case index ONLY; its article URLs 404 |
| `cfma.org` | 403 (chapters too) | **200** | CFMA Building Profits is written by contractor CFOs |
| `mmh.com` | 403 | **200** | Productivity Achievement Awards |
| `constructionexec.com` | 403 | **200** at `/topic/technology/` | |
| `abc.org` | 403 | **200** at `/Technology/AI-Resource-Guide` | |
| `bizjournals.com` | 400 on search | **403, Cloudflare JS challenge** | genuinely walled to both. Real loss. |
| `forconstructionpros.com` | 403 | **403, Cloudflare JS challenge** | genuinely walled |
| `thefabricator.com` | 403 | **403, Cloudflare JS challenge** | genuinely walled |
| `sdcexec.com` and all Endeavor | 403 | **403, Cloudflare JS challenge** | genuinely walled, incl. IndustryWeek |
| `naw.org` | 403 | **403, Cloudflare JS challenge** | genuinely walled |
| `publicpower.org/national-conference-presentations` | 403 | 403 but serves ~84 KB of real HTML | soft block, worth a second look |
| `betterbuildingssolutioncenter.energy.gov` | 503 | TLS handshake failure | DOE-side outage, not a block. **Retry first next run.** |
| `tech-con.agc.org` live | Salesforce Lightning, unrenderable | same | always use the `archive.` subdomain |
| `mepconference.com`, `b2bea.org`, `whattheythink.com`, `printweek.com`, `mvea.coop`, `ifmaseattle.org` | 403 / JS challenge | untested | |

**Fetchable and productive to WebFetch:** truckingdive.com, freightwaves.com,
fleetowner.com, truckinginfo.com, distributionstrategy.com, phcppros.com,
farm-equipment.com, homepros.news (exact article slugs only), hvac-blog.acca.org,
constructiondive.com, nist.gov, nrucfc.coop, cooperative.com,
nucleusresearch.com, appliedaifordistributors.com,
archive.tech-con.agc.org, necaconvention.org, and company-owned newsrooms
generally.

**PDFs, and this is settled.** A scout has NO working PDF path.
`WebFetch` on a `.pdf` returns raw FlateDecode binary it cannot decode and
silently saves the file; `Read` on that saved file errors with "pdftoppm is not
installed"; `r.jina.ai` works but has a hard quota, 401s for roughly fifteen
minutes after about four calls, then recovers, so treat a 401 as **wait**, not
**blocked**. The working path is `scripts/fetch_pdf_text.py` from Bash, which
needs no network service and no new dependency. Both accounts in the
2026-08-08 scout reports were partly right: W3-A was right that WebFetch cannot
read a compressed deck, W3-B was wrong that Jina is permanently dead.

---

## CONFIRMED BY RUNS

*(Appended by the upgrade-engineer each retro. Searches that worked, verbatim,
are worth recording: query craft compounds faster than anything else here.)*

- 2026-08-08 (case file 2, shipped nothing): **cost-phrase searching is dead
  craft.** Four scouts, six sector framings, nine logged failures out of nine
  for S1 alone. Every variant returned vertical-AI-pricing SEO farms. Search
  craft rule 2 above was rewritten because of this. Evidence: scout reports
  S1, S2, W2-B, W2-C, W2-D and W3-B in `out/2026-08-08/`.
- 2026-08-08: **`https://www.necaconvention.org/presentations/` is a public,
  unauthenticated index of 64 downloadable convention decks** from NECA 2025
  (September 2025), each with title, presenter names and a direct PDF link on
  an open `/wp-content/uploads/2025/09/` path. Verified live in the retro: the
  index returns 200 and 64 `.pdf` hrefs. Electrical contractors presenting to
  electrical contractors. The uploads DIRECTORY itself is 403, so you must
  harvest hrefs from the index page. NECA posts decks within days of the show.
  **~50 of the 64 are non-AI titles and nobody has walked them.**
- 2026-08-08: the NECA decks carry a footer reading "FOR REFERENCE OF NECA 2025
  CHICAGO CONVENTION ATTENDEES ONLY". They are published on an open,
  unauthenticated path, and that is where we read them, but prefer a second
  on-the-record source before a number from one of these goes on a slide.
  Source: `https://www.necaconvention.org/wp-content/uploads/2025/09/NECA-2025_Tradeshow-Ed_Innovation-in-Action_Barnard-Joe_Adamson-Tom_Lazarian-Sean.pdf`
- 2026-08-08: **the non-AI-titled deck is where the numbers are.** The NECA
  session titled "The Impact of Artificial Intelligence on Electrical
  Estimating" is two Trimble employees, a vendor, with zero cost. The session
  titled "Innovation in Action" is three contractors, one of whom puts his own
  company on a slide ("Custom Electric Inc, in business since 1982, $25-$30
  Million Annual Sales, 50 to 65 Field Workers, 10 Full-time Office Workers")
  and then itemises what tools cost, $20 to $600 a line. Same index, opposite
  yield. Both URLs under
  `https://www.necaconvention.org/wp-content/uploads/2025/09/`.
- 2026-08-08: **`archive.tech-con.agc.org/2025-session-presentations/`** is a
  public index of ~25 downloadable AGC Technology Conference contractor decks,
  roughly 3 in 25 genuinely operator-told. It carried the only real itemised
  cost disclosure of the entire run. `/2023-` and `/2026-session-presentations/`
  both 404, the 2026 one still 404 two days after that conference ended.
  **Retry the 2026 index in two to four weeks.**
- 2026-08-08: **`appliedaifordistributors.com/agenda`** yielded seven named
  operators at named distributors describing their own deployments in ONE
  fetch. None of those sessions is recorded, transcribed or recapped anywhere
  on the open web. Use agenda pages as identification maps, never as sources.
- 2026-08-08: **`nucleusresearch.com/roi-case-studies`** is fetchable and the
  best-shaped library found. A new ROI case study most months, each with a
  named company, a payback in months and an average annual benefit, costed
  over three years across software, personnel time, training and consulting.
  The free abstracts withhold the figures and the named human, so use the index
  to FIND a 50-to-1,000 non-technology company, then go around Nucleus.
- 2026-08-08: **`colonyfoods.com/about/news/`** is a monthly archive under the
  owner's own byline going back to May 2024, and it independently corroborated
  a vendor's account of the same deployment in the owner's own voice. The shape
  to hunt: a non-technology mid-market company that publishes an owner-written
  newsletter on its own domain.
- 2026-08-08: `nrucfc.coop` and `cooperative.com` (NRECA) are fetchable and
  peer-to-peer. Electric co-ops are a strong structural fit (member-owned,
  50 to 1,000 employees, ordinary, and Anchorage has three). Supply is real.
  Price is missing every time.
- 2026-08-08: **an association will let you read its magazine but not its
  handouts.** Deck INDEX pages are commonly walled (`publicpower.org` 403,
  `cooperative.com` 401s member PDFs, `mvea.coop` 403). AGC and NECA work
  because they leave handouts on an open path. When the index is walled, hunt
  the open handout PATH instead: `/wp-content/uploads/YYYY/MM/` and
  `/sites/default/files/` patterns, guessed from a filename that showed up in
  a search result.

**Candidate venues, named by a scout this run but NOT yet fetched. Untested,
so they are leads about grounds, not confirmed grounds:**

- IRS Form 990 Part VII Section B, which requires a nonprofit to list its five
  highest-paid independent contractors over $100,000 with vendor name, exact
  amount and a description of services. Cost public by law, and no timeline or
  before-and-after, so it is a pairing source, never a standalone. Recommended
  by W3-B, no filing fetched.
- `owenelectric.com/sites/default/files/YYYY-MM/*-web-posting.pdf`, a co-op
  posting board minutes on a predictable open path. Recommended by W3-B.
- SMACNA's annual convention schedule page (`smacna.org` fetches; the
  `/education-events/annual-convention` path 404s, so the real path still needs
  finding), `mheda.org/resources/` (200), and IFMA chapter presentation pages.

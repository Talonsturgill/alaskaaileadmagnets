# Phase 1 restock notes, 2026-07-25

Four case-scouts ran in parallel, one per hunting ground. Six candidates
merged into ledger/bank.json (bank-017 through bank-022) and eleven new
interview leads appended.

## The honest read on this restock

The hunt was not the bottleneck. The SOURCING BAR is. Of six new candidates,
exactly one (bank-017, CJB Industries, NIST MEP) clears the ship-ready gate.
The other five are single-source vendor case studies, which is the same wall
eleven of the original sixteen entries are stuck behind.

Ship-ready count moved from 5 to 6 against a par of 10. The bank is not
starving for stories, it is starving for CORROBORATION. The maintainer should
know that another four-scout sweep is unlikely to move this number much. What
would move it is either (a) promoting the government and awards-based grounds
below, or (b) the interview leads, which is the only channel that can produce
an Alaska-specific case the series can actually own.

## Cross-scout contradiction, resolved

The business-journals scout banked "Troiano Waste Services" as a named case.
The trade-press scout independently read BOTH underlying articles (Waste Dive
and Transport Topics) in full and confirmed neither names the company, only
"a Maine-based waste hauler". The name came from a search-engine summary, not
a fetched page. Resolved in favour of the scout that read the pages. Troiano
is an interview lead, not a bank entry. This is the no-snippet-citation rule
working exactly as designed, and it is worth keeping as a standing cross-check.

## Operational findings for the maintainer

1. **bizjournals.com is effectively dead to this machine.** Every WebFetch
   attempt failed this run and WebSearch surfaces almost no article text.
   config/sources.yaml rates it "the best source for named mid-market
   operators with named owners", and it is currently returning nothing. Either
   find a fetch path that renders it or downgrade its billing in the config.
2. **PDF text extraction was missing and it cost us the Alaska proof.** The
   fact-checker downloaded two government and academic PDFs successfully and
   could not read either, because poppler-utils is not installed. The
   showrunner recovered one of them with pypdf, which was already installed.
   Government sources are exactly the tier the bank needs most and they are
   disproportionately PDFs. This is the single highest-value upgrade available
   and is handed to the upgrade engineer.
3. **403s are systematic on several named grounds.** Becker's Hospital Review,
   RAND, HousingWire, America's Credit Unions, Pharmacy Times, and North of 60
   Mining News all returned 403 to at least one agent this run. Corroboration
   attempts are failing on access, not on absence.

## new_sources_to_consider

Recorded for the maintainer to promote into config/sources.yaml.

| Source | Why |
|---|---|
| https://www.nist.gov/mep/successstories (paginate directly) | The full MEP index runs 128 plus entries when searched for artificial intelligence and is only lightly indexed by search. Government sourced, named small and mid manufacturers, exactly our band. Paginate with WebFetch, not WebSearch. |
| https://www.freightwaves.com/news/2026-ai-excellence-in-supply-chain-awards-winners | An independent juried awards program naming real companies with specific verified savings. Independent tier, not vendor self reporting. Feeds logistics, aviation, waste, marine. |
| https://www.cooperative.com/programs-services/bts | NRECA's Business and Technology Strategies publishes member facing tech surveillance on rural electric co-op deployments. Strong vein for the energy gap given Alaska's many small co-ops. |
| https://alaskaseagrant.org/our-work/seafood-processing/ | A NOAA affiliated state federal partnership. Any AI or automation case here carries primary sourcing AND direct Alaska relevance. Not yet explored. |
| https://www.globalseafood.org/advocate/ and https://www.nationalfisherman.com | Independent and trade coverage of AI in fishing, aquaculture, and seafood processing. Fills the seafood processing gap. Currently skews pilot stage, so expect interview leads before cases. |
| https://www.nyserda.ny.gov | Runs a qualified vendor program for AI driven building energy management and publishes its own performance data independent of the vendor. Could supply the government corroboration bank-020 lacks. |
| https://www.cutoday.info | Fetchable trade press for credit unions and community banks. Useful against vendor blogs for the financial services gap. |
| https://www.qualia.com/case-studies | The only channel producing named 12 to 30 employee professional services firms with hard numbers. Vendor by default, so always pair with a trade fetch attempt before banking. |
| https://www.waste360.com and https://www.wastetodaymagazine.com | More operator level detail on regional and independent haulers than Waste Dive's enterprise focus. |
| https://extension.org/tools/extbot/ | A RAG chatbot over 360,000 plus USDA and land grant Extension publications. Not a company, but a clean government mechanism example for the regulatory document search capability. |
| State economic development agencies (Michigan LEO, JobsOhio) | Beginning to publish named small manufacturer AI stories tied to public funding. Thin today, worth periodic re-checking. |
| https://www.cpapracticeadvisor.com | Covers the accounting gap directly, but most 2025 coverage traces to vendor press releases. Bankable only with a non vendor second source. |

## Coverage still thin after this restock

Aviation and air cargo (still zero cases), mining (zero), marine and vessel
operations (zero), agriculture (zero), veterinary and pharmacy (zero),
education (zero), tribal and rural health (leads only). Workforce scheduling
and shift optimization remains the largest untouched capability.

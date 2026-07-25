# Field Notes

Living lessons for the Case Files studio. Dated entries, newest first. The
retro phase appends, the wake phase reads.

## 2026-07-25 (Case File No. 2, "Two Rulers, One Exam Room")

- The fact-check overturned the BANK'S OWN skepticism note. The bank said the
  "30 percent more visits" claim was not in the primary source. It is, verbatim,
  in the company's press release, just not on its engineering blog. Bank notes
  are hypotheses, not findings, and the fact-checker outranks them.
- The independent study measured a DIFFERENT PRODUCT (Abridge) than the case
  company built. That is category evidence, not company evidence, and it took
  the case-critic to notice the deck never said so at the climax slide where
  the reader forms the conclusion. When a deck pairs a vendor claim with
  independent literature, name the product in both places.
- ART CAN COMMIT THE ERROR THE COPY IS CORRECTING. Two instances this run. The
  discounted claim was struck with an UPWARD line that read as a growth trend,
  and the magnified bar was drawn as a huge gold slab that made the magnified
  view the loudest object on the slide built to stop that misreading. Now
  instinct i-011.
- MACHINE QA CANNOT SEE THE PAPER. Text placed below the drawn sheet renders on
  the dark desk at 2 to 3 to 1 and qa.py passes it clean. Four separate
  versions shipped this defect. Now instinct i-009.
- A continuity device carried by COLOUR ALONE is invisible. The unit chips ran
  five slides as plain coloured text and three pixel critics independently
  reported the device as missing. State changes must be SHAPE changes. Now
  instinct i-010.
- Two scouts contradicted each other on a company name. The one that READ BOTH
  ARTICLES IN FULL was right, and the other had taken the name from a search
  summary. The no-snippet-citation rule earned its keep. Cross-check scouts.
- PDF EXTRACTION WAS MISSING AND IT COST US THE ALASKA PROOF. The fact-checker
  downloaded two government and academic PDFs and could read neither, because
  poppler-utils is absent. pypdf was already installed and recovered it in one
  command. Government sources are the tier the bank needs most and they are
  disproportionately PDFs.
- bizjournals.com, rated in sources.yaml as the best ground for named
  mid-market operators, is unreachable by WebFetch. So are Becker's, RAND,
  HousingWire, Pharmacy Times and North of 60. Corroboration is failing on
  ACCESS, not on absence, and that is what keeps the bank's ship-ready count low.
- The honest Alaska angle was the opposite of the obvious one. Alaska's
  physicians per 100,000 essentially match the national rate. The real story is
  distribution and age. Reading the source instead of the vibe produced a
  better and more defensible slide.

## 2026-07-21b (Case File No. 1, the first live run)

- The fact-check killed the story's intended payoff (the camera did NOT
  keep the Redoubt count going) and the honest version was a better story.
  Bank intake must always mark proposal vs deployed, the case-scout
  definition requires it.
- The honesty gate caught the caption outrunning its own deck (the hook
  claimed more than c23 supports). The caption must never claim more than
  the most-hedged slide.
- DOM chips and labels collide with canvas data marks that QA cannot see.
  Plan canvas element rects IN the dossier next to the DOM budgets, and
  eyeball every art-zone chip against them. Parked as a future gate.
- The flow critic's forward-plant fix (one tease line at the predicted
  bail slide) is cheap and repeatable. Any keepable slide should plant the
  next slide.
- Agent deaths from infra blips are real, respawn-by-cause worked, check
  liveness via the task registry instead of waiting on notifications.
- The logo is now law and machine-enforced (logo_check.py), default home
  the close slide brand row, keep it at 66px or smaller until a higher
  resolution export exists.

## 2026-07-21 (pre launch, from the build session)

- Engine proof shipped, three slides rendered and QA green in this repo with
  the vendored engine, vector PDF at 1.96 MB. The pipeline works end to end
  before the first real run.
- QA caught exactly the defect classes the sibling studio's ledger predicted,
  a hand sized hook wrapping into the block below, a bottom anchored note
  colliding with a stat stack, unmarked micro text. All three are now
  instincts (ledger/instincts.json i-001 to i-003).
- The evidence base (research/EVIDENCE.md) says documents and carousels are
  the top organic LinkedIn format in 2025 to 2026 on both pages and profiles,
  personal profiles carry roughly 2x page reach, links in body suppress
  reach, and comment gated lead magnets increasingly read as bait. The
  series' mechanics are built on those findings, revisit quarterly.
- The case bank's weakest coverage is aviation and Alaska specific private
  company stories. The standing fix is the interview lead (Saltwater Inc,
  Anchorage) and the Phase 1 restock hunting bizjournals and NIST MEP for
  named mid market operators.
- Voice discipline note for case posts, the vendor label reads cleanest as a
  plain attribution mid sentence, "per Samsara's case study, insurance costs
  fell 36 percent," which satisfies the honesty rule without a footnote.

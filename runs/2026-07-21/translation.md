# Translation Dossier, Case File No. 1, 2026-07-21

Case in one breath. Computer vision that counts salmon from underwater camera
and weir video (SalmonVision, sixteen sites across Alaska and BC in the 2025
season, c09, over 20 monitoring projects now, c10), told honest against the
government anchor that technicians still watch DIDSON and ARIS video and
count fish by eye today, labor and time intensive (c23), and against the
Redoubt Lake reality check, where a funded tribal proposal for AI video (a
200,000 dollar grant, c18) did not replace the 2025 count, which ran through
the physical US Forest Service weir, 8,111 sockeye by June 29 (c19).

The core move is watch and count. A person at a fixed point, watching product
or traffic go by and tallying or grading it, is a universal operations
bottleneck. If a conservation nonprofit and a tribe can field a camera
counting rig the program reports fell from about 50,000 dollars to about
10,000 dollars with edge processing, about 5,000 dollars video only (program
reported costs relayed by an independent outlet, c14, c15), then the same
class of small vision build is within reach of a mid market operation.

Note on labeling. Sections 1 through 5 (the segment ranking, the rung calls,
the cost shape, the ramp, the limits) are analysis grounded on the cited
claims. Claim ids mark the verified facts. Nothing here names a private
Alaska business as a target, only public record sector anchors appear.

## 1. Segments

Rank 1. Seafood intake and processing QC. The literal twin. Same object,
fish, and the same physics, a person watching product move past a fixed
point and tallying or grading it. Processors already count and grade on
intake and on the line, and that counting peaks in the exact summer weeks
the runs do, so the labor crunch and the seasonality both rhyme one to one
with the case. The document stream rhymes too, fish tickets, intake counts,
and grades are already recorded, which means a trusted baseline for an eval
already exists. Bank proof, Norway aquaculture CV counting (015) and NOAA's
fisheries small model (016), plus SalmonVision itself. This is the strongest
rhyme the twin map offers.

Rank 2. Cargo and warehouse counting. Air cargo is a real Anchorage mid
market segment with public sector anchors on the record (Corporate 100,
https://digital.akbizmag.com/issue/april-2025/2025-corporate-100/). Same
physics, count discrete units, ULDs, pallets, parcels, moving past a dock
camera, and the document stream, manifests and waybills, is already digital.
Seasonality is flatter than seafood but has peaks, fish freight out in
summer and retail in for winter. Honest caveat carried up front, if the
units are already barcode or RFID scanned, the count already exists and the
answer drops to plain software, no CV. Bank proof, the 3PL that put CV on
cameras it already owned (004). Candidate new bottleneck map row.

Rank 3. Gate and yard traffic. Freight yards, port and terminal gates, fuel
terminals, distribution yards. Same watch and count physics at a chokepoint,
vehicles and containers in and out. This is the segment where the honest
answer is most often not AI at all. A beam break, an inductive loop, or
license plate reading is rules level and cheaper, and CV earns its place
only when you need to classify, vehicle type, container id, or damage. A
good place to prove the discipline, count the cost of a wrong count first,
and if a sensor solves it, buy the sensor.

Rank 4. Inspection footage review for utilities and contractors. Railbelt
co-ops and pipeline and facility inspection contractors. Not counting, but
the same underlying bottleneck, a human watching hours of footage for
events, defects, encroachments, corrosion. This rhymes with the NOAA bycatch
review in the case, models that process fishing tows in hours where humans
need days to weeks (c25, c26), more than with the counting story itself. The
move is CV flags candidate events and a human confirms, and the human stays
on the expensive call. Bank proof, the utility that ran CV over inspection
imagery (013). A weaker rhyme to counting specifically, a strong one to
review footage for events.

## 2. The honest rung

Most of these sit on rung 4, workflow, the model runs inside fixed, testable
steps, camera in, detection and count out, tally recorded, a human checks it
against the baseline. That is where the case lives and where the bank's
seafood row already sits, small custom CV models, workflow.

Two honest moves down the ladder, and saying them is the brand working.
- Cargo and warehouse counting drops to rung 1, rules, whenever the count is
  already captured by a scale, a barcode, or an RFID read. If the number
  already exists in a scan, you do not need a model to see it. Say that
  first.
- Gate and yard traffic is often rung 1 too, a sensor, not a camera model,
  unless classification is genuinely required.

And one move nobody should make, none of these is an agent (rung 5). A
counting or review build that plans its own steps is fragile and unearned
here. The winning shape is a short workflow with the human at the count that
matters.

## 3. Cost class

Grounded shape, the hardware. The program reports its per site rig fell from
about 50,000 dollars to about 10,000 dollars with edge processing, about
5,000 dollars for video only (program reported, relayed by an independent
outlet, c14, c15). Read that as hardware in the low thousands to about ten
thousand dollars per camera position, and mid market operators often already
own usable cameras on the floor, the dock, or the gate.

Cost shape, not dollars, for the model and integration, because claims.json
does not ground a mid market build price and inventing one would break the
honesty rule. Two paths.
- Buy a vision counting or video review tool. The cost shows up as a per
  camera per month subscription. Faster to stand up, less control, and you
  must test the vendor's own accuracy claim against your data before you
  trust it, never against the vendor's average.
- Build a custom small model. The cost shows up as an engineering build
  measured in weeks, and the bulk of it is labeling a representative set and
  standing up an eval harness against your existing manual count, plus
  ongoing monitoring for drift across seasons and lighting.

The honest cost driver is labeling and evaluation, not the camera. The
program's model trained on over 5 million annotated frames (c13) shows how
heavy the data side can run, though a narrow mid market count needs far less
than that.

## 4. What it takes

Data readiness in local terms. The segments that translate already hold the
two things a build needs. First, a camera position, floors, docks, gates,
and inspection archives already have cameras or can add one cheaply. Second,
and more important, a trusted baseline to grade against, the manual count or
the manifest the operation already records. That baseline is the eval set.
The whole salmon method is machine count measured against a human or weir
count, and the Bristol Bay drone project makes the pattern explicit, it
plans to test its models against ADF&G tower counts in a next phase (c29).
No baseline, no eval, no promise.

People, who owns adoption. The line manager who owns the count today, the
intake lead, the yard supervisor, the QC lead, the inspection foreman, owns
the adoption, not IT. Line manager ownership is one of the behaviors the
failure studies found on the winning side, alongside a narrow high frequency
workflow and buying before building. A tool no supervisor's workflow owns is
a demo.

Ramp, realistic. Benefits ramp, plan for roughly 90 days, not day one. Run
the model alongside the human count for a full cycle to build the eval and
the trust, then move the human to spot checking where it pays. This is
exactly the case, humans still count today (c23), the machine assists, and
the trusted baseline is what earns the handoff.

## 5. Where it does not translate

- Low volume a person clears in minutes. If a person counts it in a couple
  of minutes a few times a day, a vision build never pays. The economics
  need high frequency, high volume, or long hours of footage.
- Safety or regulation critical counts with no human check. If a wrong count
  carries a safety or compliance cost and no one catches it before it lands,
  you cannot run it autonomously (the cost of error gate). The salmon world
  keeps humans on the count and validates against weirs and towers for
  exactly this reason.
- Hard imagery. Clear weir video is where the program reports its high
  accuracy (a self report, c05). Sonar echograms are where a February 2025
  arXiv preprint reported about a 23 percent count error on Kenai River
  data, framed as feasibility, not a solved problem, and it is not peer
  reviewed (c24), and it should never be inverted into an accuracy figure.
  Clear, well lit, unobstructed camera positions translate. Murky water,
  overlapping units, occluded scenes, and sonar style imagery are much
  harder and stay that way for now.
- Alaska frictions. Bandwidth in the Bush. A remote plant, yard, or weir
  with no connectivity cannot stream video to the cloud, which is why the
  program moved to edge processing (c14), plan for edge or plan for nothing.
  And seasonality cuts both ways, a summer count build has to be stood up
  and validated before the season opens, because there is no time to train a
  model during a three week sockeye crush.
- Proposal is not deployment. The honest Redoubt lesson. A funded grant to
  add AI video (c18) did not replace the 2025 physical weir count (c19).
  Budget for the gap between buying a camera and trusting it enough to
  retire the manual count, and expect that gap to run a season or more.

## 6. Local proof pairing

This case is itself the flagship Alaska local proof (ALASKA_GROUND section
1), so the pairing is internal. For the counting segments, SalmonVision and
the honest Redoubt reality check carry it, real, still imperfect, honestly
told. For the inspection footage review segment, pair NOAA's Alaska
Fisheries Science Center customizing YOLOv11 to flag pollock and salmon in
nets, processing tows in hours where human review needs days to weeks (c25,
c26), the cleanest review footage for events twin in the case. And for the
what it takes section, the Bristol Bay drone's plan to validate against
ADF&G tower counts (c29) is the local proof that every operator build needs
an eval against a trusted baseline.

## 7. The why-now

It is sockeye season right now, the weir count is live and the sonar
technicians are counting by eye this month (c19, c23), so the watch and
count crunch this case describes is not a future Alaska problem, it is a
summer that lands its whole counting labor in a few short weeks, which is
exactly when a mid market operator most needs the workers it cannot always
staff.

## bottleneck_map_row

```json
{
  "action": "strengthen",
  "segment": "Seafood",
  "recurring_bottleneck": "Watch and count labor, manual counting and grading on intake and hours of line and sonar video reviewed by eye",
  "honest_answer": "Small custom CV counting and grading model inside a fixed workflow that assists the human and is validated against the existing manual count, rung 4 workflow. Where a scale or a scan already captures the count the honest answer drops to rung 1 rules with no CV. Sonar and murky imagery stay harder than clear video.",
  "rung": 4,
  "proof_id": ["015", "016", "SalmonVision"],
  "case_claim_backing": ["c09", "c10", "c14", "c15", "c18", "c19", "c23", "c24", "c25", "c26"],
  "whats_new": "Adds the ADF&G government anchor that technicians still count by eye today (c23), the Redoubt reality check that a funded 200k dollar AI video proposal (c18) did not replace the 2025 physical weir count of 8,111 sockeye by June 29 (c19), the program reported edge rig cost of about 10k dollars down from 50k (c14, c15), and the honest counterweight of about 23 percent sonar count error in a non peer reviewed 2025 preprint (c24)."
}
```

# Alaska Ground Truth

Compiled 2026-07-21 from fetched pages. This is the local proof layer for the
series, the stories that make "AI winning in the real world" land as an Alaska
fact instead of an Outside rumor. Figures that could not be fully verified are
marked uncertain. Re-verify every claim through the pipeline's fact-check gate
before it ships in a post.

## 1. Fish counting, the flagship local-proof story

How salmon get counted today. In clear narrow streams ADF&G still uses weirs and
counting towers, people counting fish by eye. Wide glacial rivers get imaging
sonar. DIDSON replaced older Bendix systems across sites between 2002 and 2011,
ARIS arrived in Alaska in 2012. The counting is still largely manual review of
sonar video, tedious and labor heavy. That labor is exactly what the AI work
below targets.
- https://www.adfg.alaska.gov/index.cfm?adfg=sonar.main
- https://www.adfg.alaska.gov/index.cfm?adfg=sonar.didson

The real AI deployments and pilots.
- SalmonVision. Pacific Salmon Foundation, Wild Salmon Center, and Lumax
  Ecological Analytics with Simon Fraser University, DFO, ADF&G, and Indigenous
  nations including the Sitka Tribe of Alaska. Computer vision on underwater
  camera and weir video. Reported roughly 90 percent accuracy, 80.2 percent mean
  average precision in later runs (67.6 percent in an earlier combined-dataset
  run), trained on 5 million plus annotated frames, deployed at about 16 sites
  across Alaska and BC, goal of 100 watersheds by 2028. Processes an hour of
  video in about a minute. Hardware cost fell from about 50k dollars to 10k
  (5k video only). CORRECTED BY FACT-CHECK 2026-07-21. The lake is Redoubt
  Lake (an ADF&G release confirms the spelling), it supports ONE OF the
  largest sockeye subsistence fisheries in Southeast Alaska, and the camera
  did NOT simply keep the count going. The Forest Service said in February
  2024 it lacked funds to run the weir, the Sitka Tribe stepped in to support
  management with a 200,000 dollar tribal wildlife grant proposing AI video
  with the Wild Salmon Center and USFS, and the 2025 count still ran through
  the USFS operated physical weir, 8,111 sockeye by June 29 2025. The AI
  handoff is being built, not done. See runs/2026-07-21 claims c16 to c19.
  https://salmonvision.org/
  https://www.currentflowstate.com/salmon-vision-the-ai-revolution-comes-to-salmon-conservation/
- NOAA Alaska Fisheries Science Center customized YOLOv11 to detect pollock and
  salmon in fishing nets, cutting bycatch video review from days or weeks down
  to hours.
  https://www.fisheries.noaa.gov/feature-story/faster-analysis-data-evaluate-bycatch-reduction-efforts-pollock-fishery
- Alaska Longline Fishermen's Association won a 485,000 dollar NFWF grant to
  test FishVue AI cameras (Archipelago Marine Research) counting sablefish and
  halibut at sea, with the Pacific States Marine Fisheries Commission.
  https://www.eweek.com/news/alaskas-fishing-industry-ai-observers/
- Bristol Bay drones. UW Fisheries Research Institute flies an autonomous drone
  daily over the Wood River, hand labeling footage to train a counting model
  against ADF&G tower counts. Early, no accuracy figures yet.
  https://alaskapublic.org/news/environment/2026-07-08/ai-drones-and-salmon-what-new-technology-could-mean-for-bristol-bay-sockeye-counts
- The honest counterweight. A February 2025 arXiv preprint (not peer
  reviewed) counting fish from echograms of sonar video (ResNet-18) reported
  a 23 percent count error on Kenai River data, framed as feasibility.
  A DOE Fish Detection AI project trained Faster R-CNN on ADF&G sonar images.
  This problem is advancing, not solved, and saying so is on brand.
  https://arxiv.org/abs/2502.05129
  https://catalog.data.gov/dataset/fish-detection-ai-sonar-image-trained-detection-counting-tracking-models
- UAF used ML on Chinook tagging data to model where Chinook swim so trawlers
  can cut bycatch, published in Animal Biotelemetry.
  https://www.newsminer.com/news/alaska_news/salmon-tagging-data-could-help-trawlers-reduce-bycatch/article_62b94d4f-4aad-4843-a08e-8c815aff394d.html

The mature end state, for contrast only. Norway's Aquabyte estimates salmon
group weight within 0.8 percent of truth 95 percent of the time, has detected
100,000 plus sea lice (about a 1 billion dollar per year problem in Norway), and
projects 20 to 30 percent feed cost reduction. Alaska law effectively bans
finfish farming, so this is an analogy for what mature fisheries CV looks like,
never a local play.
- https://aquaculturemag.com/2018/02/16/aquabyte-is-using-computer-vision-and-machine-learning-to-optimise-fish-farming/

## 2. Snow operations

Anchorage today. Winter maintenance runs from muni.org/plow with a public ArcGIS
plow tracking map. Crews clear arterials and collectors after 4 plus inches,
around the clock October through March. A recent low snow winter shifted road
money from plowing to potholes, a real local hook about budget swings. Mat-Su
rolled out borough-wide live plow tracking. No hard data was found quantifying
Anchorage plowing complaints, treat that angle as anecdotal.
- https://www.muni.org/Departments/operations/streets/WinterMaintenance/Pages/default.aspx
- https://experience.arcgis.com/experience/76746e478f7942e2ab98c4a0e483b77b
- https://www.matsusentinel.com/snowplow-live-tracking-now-available-throughout-mat-su/

Route optimization elsewhere, with results.
- Indiana DOT's CASPER route optimization cut fleet size about 10 percent,
  savings conservatively estimated at 5 million dollars, projected to exceed 14
  million over 10 years statewide.
- Iowa DOT District 3 cut deadhead distance 13.2 percent.
- Perth County Ontario retired 3 depots and 8 trucks through depot sharing while
  still meeting service law.
- Newer reinforcement learning work partitions road networks for multi-depot
  balance. The clean narrative, boring optimization pays for itself in a winter
  city.
- https://prosper.intrans.iastate.edu/news/snowplow-route-optimization-offers-big-potential/
- https://rosap.ntl.bts.gov/view/dot/31681/dot_31681_DS1.pdf

## 3. The Anchorage mid-market map

Alaska Business Magazine's Corporate 100 is the authoritative employer list. The
biggest names exceed the 50 to 1000 employee band, use them as sector anchors,
not as "mid-sized."
- https://digital.akbizmag.com/issue/april-2025/2025-corporate-100/

- Healthcare. Providence Alaska (about 5,000, largest private employer), ANTHC
  and Southcentral Foundation in Alaska Native health. Genuinely mid-sized
  clinic groups live beneath these, and they are the ICP target, not the
  systems.
- Seafood. Trident Seafoods (3,641 Alaska employees). Seven seafood firms in the
  Corporate 100.
- Retail and distribution. Carrs Safeway (2,507).
- Alaska Native corporations. NANA, ASRC, CIRI, BBNC, Doyon, Calista, Ahtna,
  with many subsidiaries that land squarely in the 50 to 1000 band.
- Air cargo and logistics, strong mid-market fit. Lynden Air Cargo (about 140
  employees), Northern Air Cargo (largest intra-Alaska by tonnage), Everts Air
  Cargo.
- Construction, utilities (Chugach Electric, Enstar, MEA), tourism operators,
  and credit unions (Global Credit Union, Credit Union 1) are natural 50 to
  1000 segments. Specific headcounts not verified, segment guidance only.

Alaska organizations already talking about AI in public. The 2025 AI in Alaska
Native Health Care Systems symposium (ANTHC, Southcentral Foundation, Maniilaq,
Stanford). UAA launched a Master's in AI in Fall 2025 plus a Business Analytics
and AI certificate. Alaska won 272.2 million dollars in Rural Health
Transformation funding, second largest nationally. A 2026 Alaska AI Pitch
Competition targets small businesses.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13202658/
- https://www.nucamp.co/blog/coding-bootcamp-anchorage-ak-getting-a-job-in-tech-in-anchorage-in-2025-the-complete-guide

## 4. How the brand presents publicly today

alaskaaihq.com presents as a daily publication and an AI studio in Anchorage,
tagline "AI is coming north." Nav is HOME, THE DOCKET, ARCHIVE, SERVICES, ABOUT.
13 decks live as of 2026-07-21, six daily beats, content on LinkedIn and TikTok.
The Docket tracks 8 live AI infrastructure decisions (AKLNG tax bill, AIDEA
Mat-Su Data Center Park, STAK Energy North Slope campus lease, Air Force
enhanced-use leases, GVEA turbine vote, HB 259, Enstar gas storage denial,
Anchorage data center zoning AO 2026-27). Services listed are voice agents,
custom AI assistants trained on company files, paperwork automation, and digital
employees. The editorial promise, every number and quote re-fetched from a
primary source, artwork drawn fresh from code.

Series takeaway. The brand already owns the verified, Alaska specific, receipts
first voice. The fisheries story is the sharpest local proof, real, still
imperfect, honestly told. Snow ops route optimization is the cleanest "boring AI
that saves money" case for a winter city. This series extends the publication
from covering the AI beat to teaching the AI playbook, and the mid-market map in
section 3 is who it teaches.

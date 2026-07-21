# Case Craft

The story grammar for the Case Files series. This sits ON TOP of the ported
studio doctrine. CAROUSEL_CRAFT.md owns platform physics, DESIGN_DOCTRINE.md
owns the visual standard, SLIDE_DOSSIER_SPEC.md owns planning format,
TECHNIQUE_LIBRARY.md owns the art. This file owns what makes a CASE post land
with an operator who could be a customer.

## The reader

An Anchorage area owner, GM, or ops lead at a company of roughly 20 to 2000
people. Practical, busy, allergic to Outside slickness and to AI hype in equal
measure. They have used ChatGPT. They do not believe it matters to their
business yet. The post exists to close that gap with proof, not persuasion.
The reaction we are engineering, in order, is "that company looks like mine,"
then "oh, that is HOW," then "these Alaska AI people talk straight."

## The four flavors

- CASE FILE (the core, most runs). One real company's win, told whole.
- CAPABILITY FILE (about weekly). One capability demystified through the
  companies using it, fine tuning, RAG, vision counting, forecasting, route
  optimization, document intake. What it is in plain talk, what it costs now,
  who used it, when you need it, when you absolutely do not.
- REALITY CHECK (every week or two). The anti hype desk. What the failure
  research actually says, why pilots die, what the winners do differently.
  Cite the failure stats TOGETHER (MIT, RAND, Gartner, McKinsey), never one
  alone as a scare number.
- TRANSLATION (occasional). An Alaska ground story promoted to a full post,
  fish counting, plow routes, always framed honestly as analysis, never as a
  claim that we built it.

## The Case File grammar (9 slide default, 6 to 12 legal)

1. COVER. The hook in 12 words or fewer, a number or a reversal, huge type.
   The company may be unnamed here if the tension is stronger without it.
2. THE COMPANY. Who, where, size, age. Deliberately ordinary. Family owned,
   founded 1955, 160 trucks. This slide does the identification work, the
   reader must see themselves before anything else happens.
3. THE BOTTLENECK. The specific pocket in operational terms, the thing that
   ate hours or leaked money. Quote the operator when a fetched quote exists.
   Never "they needed to innovate." Always "referrals arrived as faxes and
   took 15 minutes each."
4. THE BUILD. What they actually built or bought, mechanism in plain talk.
   Name the ladder rung (HONEST_AI.md), rules, retrieval, single call,
   workflow, agent. Name vendors when known, we are not afraid of naming
   tools we do not sell.
5. THE RECEIPTS. The numbers slide. Keepable, tabular, sourced, claim-ids on
   every figure. Sourcing labels live here in the same breath, "per Samsara's
   case study" sits next to the 36 percent, not in a footnote.
6. WHAT IT TOOK. Time, data readiness, people, rough cost class. The
   implementation reality every other AI post skips. This is the bridge from
   capability to implementation and the slide that makes the series useful
   instead of entertaining.
7. THE CATCH. What would break, where the approach stops working, what the
   vendor number probably flatters, when you do not need this at all. The
   honesty slide. Never skipped, never softened. This slide is the brand.
8. THE TRANSLATION. Which Anchorage segment this speaks to and what the
   equivalent build honestly looks like here, per ALASKA_TRANSLATION.md.
   Speak to segments, never call out a named local business as a target.
9. CLOSE. One ask only. The standing offer line from config/brand.yaml, the
   site small in mono, the constellation marks, and the Alaska Ai logo
   (required on every deck, scripts/logo_check.py enforces it, default home
   is this slide's brand row). Educational close, zero pressure.

The grammar is bones, not a template. Slides may merge (bottleneck and build,
receipts and what it took) when the story is tight, the count may stretch when
the story is rich. The DOSSIER decides and defends the count. But no case file
ever ships without RECEIPTS, THE CATCH, and THE TRANSLATION. Those three are
the series.

## The Capability File grammar

1. Cover, the capability as a plain promise or a myth to kill.
2. What it actually is, one metaphor, zero jargon.
3. Who used it, 2 to 3 bank cases compressed to one line each with numbers.
4. What it costs now, honest ranges, what moved the price recently.
5. When you need it, the ladder position and the tells.
6. When you do NOT, the plain software answer said with a straight face.
7. What it takes to start, data, weeks, people.
8. Close, offer line.

## The Reality Check grammar

Hook on the uncomfortable number, then what the research actually measured,
then the winner behaviors as practical moves, then the honest local
implication, then close. Reality checks NEVER dunk on a named company and
NEVER use fear as the ask. The point is that the reader trusts the case files
more because we publish the failure math too.

## Caption craft (adds to the ported caption rules, all still binding)

- Hook patterns that fit this series, the reversal ("The weir lost its
  funding. The camera kept counting."), the ordinary company number ("A 160
  truck produce hauler cut a fifth of its miles."), the cost flip ("GPT-4 was
  the expensive way to do this job.").
- The caption tells the story in miniature but keeps one load bearing number
  for the deck, the caption teases, the deck delivers.
- Identification before information, company shape before technology name.
- The standing offer line appears ONCE, near the close, exactly as configured
  in brand.yaml, never improvised, never repeated.
- First comment carries sources (primary first, vendor labeled as vendor),
  one light site line, and one line inviting readers to add their own war
  stories. War story invitations out-engage generic questions for an operator
  audience.

## What kills a case post (the series kill list, on top of house rules)

- Enterprise worship. A Fortune 500 logo where an ordinary company should be.
  Big firm mechanism cases are legal ONLY with the size caveat said plainly.
- Product pitching. Our services never appear by name inside the teaching.
  The offer line is the only commercial sentence and it is configured, not
  written fresh.
- Unlabeled vendor numbers. The label rides with the number, every time.
- A sweeping transformation arc. The series thesis is targeted builds on
  specific bottlenecks. "They transformed their business with AI" is banned
  energy, "they fixed the fax queue" is the voice.
- Hype verbs, dashes, colons, emojis, AI tells, per the house lists, enforced
  by lint and critics.
- A missing catch. If we cannot find the honest limitation, we have not
  researched enough to ship.

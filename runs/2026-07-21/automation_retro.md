# Automation retro, 2026-07-21, Case File No. 1 (manual test run)

Phase 11 executed by the showrunner under the contract's fallback (agent
infrastructure dropped two subagents mid-run this session, and the run's
upgrade budget was already consumed by a verified maintainer-requested
change).

## Deviations observed, with evidence

1. Two subagents (flow-critic, pixel-critic 1-4) died silently during a
   server disconnect and produced no notifications. Respawn-by-cause worked
   on the first retry. Lesson recorded, liveness can be checked via the
   task registry rather than waiting on notifications.
2. The engine-proof deck's cover premise ("the camera kept counting") was
   KILLED by fresh verification (claims c19 and c31). Root cause, the bank
   digest did not distinguish deployed from proposed. Fixed in the moment
   (research/ALASKA_GROUND.md corrected, engine-proof README frozen as a
   fixture), and the case-scout definition already requires the
   distinction going forward.
3. A DOM-over-canvas regression class appeared twice, the S3 chip row
   covering dashed series nodes, and the S5 footer tease wrapping into the
   canvas cost stair. Machine QA cannot see canvas art, so these survive
   to the pixel critics. PARKED as a future gate candidate, a
   dom-canvas collision pre-check helper that reads declared canvas
   element rects from the slide dossier.
4. The shell working directory reset twice between calls, breaking
   relative-path commands. Mechanical, absolute paths or a leading cd are
   the fix, noted for the routine's Bash discipline.
5. Copy fidelity worked as designed, the copywriter's corrections, the
   case-critic's six catches, and the pixel critics' honesty-mark checks
   all landed before ship, and the record-sync note kept the storyboard
   honest about it.

## Upgrades this run, 1 (reactive, maintainer requested)

- kind improvement, area gates. scripts/logo_check.py, every deck must
  carry the brand logo (assets/alaskaaipic.png), enforced objectively in
  the art build phase and via a scorer hard fail. VERIFIED, PASS on the
  live deck, FAIL on a reconstruction without the logo, and the full deck
  renders green with the logo present. Wired into brand.yaml
  (logo_required), scoring_rubric.yaml, routine_instructions.md (storyboard
  gate + art build), CASE_CRAFT.md.

## Frontier scan

Skipped this run (manual test run driven interactively, timebox spent on
the live iteration loops). scan_log entry records the skip. Next run picks
a rotation focus per the upgrade-engineer definition.

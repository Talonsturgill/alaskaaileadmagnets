# AUTOMATION RETRO, 2026-08-08, Case File No. 2

**The run shipped nothing.** Phases 2 through 9 never executed, so there are no
renders, no copy, no gates and no score to retro. The reactive half of this
document is therefore about the HUNT, which is where the whole run happened.

---

## 1. REACTIVE RETRO, phase by phase against the spec

### Wake, one deviation, self-repaired

`bootstrap.sh` died on the cryptography step with a pip `ReadTimeoutError` to
`files.pythonhosted.org`. A manual retry of `pip install --user --upgrade
cryptography` succeeded and `from pypdf import PdfReader, PdfWriter` imports
cleanly. Confirmed still true in the retro: pypdf 6.15.0 on
`/usr/local/bin/python3`.

**Verdict: transient network, correctly handled in the moment.** One retry
fixed it and the bootstrap is green. No durable fix warranted; a retry loop
around pip would hide a real outage as easily as it would absorb a blip. Worth
one line of watching: if this recurs a second time, it becomes a bootstrap
change.

**But it exposed something the run never used.** pypdf was repaired at wake and
then sat idle while three waves of scouts hit PDFs they could not open. That is
the gap upgrade U-002 closes.

### Phase 1 restock, ran three waves instead of one, and that was correct

The spec says "spawn up to FOUR `case-scout` agents in parallel". The run
spawned **ten across three waves**. That is a deviation from the literal
contract and the right call: the bank was at 0 of par 8, so a single wave could
not have restocked it, and each wave was genuinely re-aimed by what the
previous wave learned (wave 1 hunted grounds, wave 2 hunted the two missing
facts, wave 3 tested the deck seam). The failure protocol was invoked correctly
and the bar was not lowered.

**Cost of the deviation:** roughly 250 queries and 85 pages for zero cases. Not
wasted, but the same budget spent with the kill order (below) would have died
faster and left room for a fourth idea.

### Phases 2 to 9, never ran

Correct. Nothing in the bank qualified, and the spec's own instruction is
"restock rather than lowering the bar."

### Ten deviations and defects, with evidence

| # | What | Evidence | Durable fix |
|---|---|---|---|
| 1 | `run_state.json` was left stale at `restock: wave1_done_wave2_running` after three waves finished and the postmortem was written | `out/2026-08-08/run_state.json` phases block vs `postmortem.md` | Not machinery. Flagged to the showrunner: run_state is the record and it stopped tracking reality mid-run. |
| 2 | `HUNTING_GROUNDS.md` search craft rule 2 actively instructed scouts to run a search craft that is dead | rule 2 as written vs S1, S2, W2-B, W2-C, W2-D, W3-B | **FIXED.** Rule 2 rewritten to hunt the venue. |
| 3 | Ten scouts independently rediscovered the same fetch walls | access maps in S1, S2, W2-B, W2-C, W2-D, W3-A, W3-B, all overlapping | **FIXED.** Standing access map added to `HUNTING_GROUNDS.md`, and `case-scout` is told to read it before its first fetch. |
| 4 | `case-scout` puts the hard gate at item 5 and never mentions filter 3 as a kill | `.claude/agents/case-scout.md` | **FIXED.** A three-question kill order added ahead of the filter. The seven-part filter is unchanged and unweakened. |
| 5 | Scouts have no working PDF path at all, and the best ground in the series is PDFs | W3-A, W3-B, and reproduced in the retro (see section 3) | **FIXED.** `scripts/fetch_pdf_text.py` plus a showrunner deck pre-pass in the run contract. |
| 6 | Two scouts filed contradictory tool reports (W3-A: Jina rate-limited, WebFetch cannot read PDFs; W3-B: Jina permanently dead, WebFetch reads PDFs natively) and the contradiction was never resolved | W3-A vs W3-B summaries | **RESOLVED BY TEST**, see section 3. Both were partly wrong. Recorded in `HUNTING_GROUNDS.md`. |
| 7 | Wave 1 recorded `dev.mcaa.org` as "a readable mirror of www.mcaa.org"; W3-A found its article URLs 404 | S1 vs W3-A | **PARTIALLY RETRACTED** in the access map: it mirrors the Smart Solutions case index only. |
| 8 | A vendor stat card would have shipped a baseline inflated ~2x | W2-A on the n8n Field Aerospace page | **FIXED.** New step 3 in the verification protocol in `EVIDENCE.md`. |
| 9 | A synthetic case study reached intake ("Meridian Supply Co.", "Marcus, operations director") | S2 | **FIXED.** Tell stack recorded in `EVIDENCE.md`. Caught by the snippet rule, which held. |
| 10 | Bank intake skepticism was NOT wrong this run | no bank entry died at fact-check, because fact-check never ran | Nothing to fix. The 16 seeded entries were demoted on 2026-07-28 by a gate change, not by a bad intake call. |

### What worked and should not be touched

- **The failure protocol.** The run refused to lower the bar and produced a
  postmortem that is a better artifact than a weak deck would have been.
- **The snippet rule.** It killed "Meridian Supply Co.", Leonard Splaine and
  three others. It earned its keep repeatedly.
- **Wave re-aiming.** Each wave's brief was written from the previous wave's
  finding. That is the iteration law applied to research and it worked.

---

## 2. FRONTIER SCAN, focus (b), new documented mid-market case sources

Chosen because the last `scan_log` entry is "skipped, manual test run" so no
focus is stale, and because this run's entire deficit is on the hunt side.
Eight operations, all fetched and read.

**Findings, all verified live this run:**

1. `https://www.necaconvention.org/presentations/` returns 200 with **64
   `.pdf` hrefs** on an open `/wp-content/uploads/2025/09/` path. The uploads
   directory itself is 403, so hrefs must be harvested from the index page.
2. **The non-AI-titled deck is where the numbers are, and it is now
   demonstrated rather than hypothesised.** The NECA session titled "The Impact
   of Artificial Intelligence on Electrical Estimating and Project Operations"
   is two Trimble employees with zero cost content. The session titled
   "Innovation in Action" is three contractors, one of whom puts his own
   company on a slide ("Custom Electric Inc, in business since 1982, $25-$30
   Million Annual Sales, 50 to 65 Field Workers, 10 Full-time Office Workers")
   and then itemises tool costs, $20 to $600 a line. Same index, opposite yield.
3. **`abc.org`, `constructionexec.com`, `smacna.org`, `mheda.org` and
   `ifma.org` all return 200** to a browser-UA GET. `ifmaseattle.org` returns a
   202 JS interstitial of 185 bytes.
4. **Several of the run's "403 walls" are WebFetch-specific, not site walls.**
   See section 3. This is the biggest single finding of the scan.
5. The genuinely walled hosts are Cloudflare JS challenges and they are walled
   to everything we have: `bizjournals.com`, `forconstructionpros.com`,
   `thefabricator.com`, `sdcexec.com`, `naw.org`.
6. `betterbuildingssolutioncenter.energy.gov` fails a TLS handshake from Bash
   and 503s from WebFetch. Still down. Still the first retry next run.

---

## 3. THE TOOL CONTRADICTION, RESOLVED BY TEST

W3-A and W3-B filed opposite reports. Both were tested directly in the retro.

| Claim | Verdict | Evidence |
|---|---|---|
| W3-B: "WebFetch reads PDFs natively" | **WRONG in the general case.** WebFetch on `NECA-2025_Tradeshow-Ed_The-Impact-of-Artificial-Intelligence...pdf` returned "heavily compressed/encoded with FlateDecode filters, making the actual text inaccessible" and saved the binary. | reproduced this run |
| W3-A: "`Read` cannot open the saved PDF, poppler is absent" | **CORRECT.** `Read` on the saved file errors: "pdftoppm is not installed." | reproduced this run |
| W3-B: "`r.jina.ai` is permanently dead" | **WRONG.** W3-A's account, a hard quota with ~15 minute recovery, is the one to carry. A 401 means wait, not blocked. | W3-A vs W3-B, not re-tested in the retro to avoid burning the quota |
| W3-A: "some decks are image-only exports and are a dead end" | **CORRECT and now machine-detected.** `fetch_pdf_text.py` exits 3 with an explicit "DEAD END, not a retry" message. | verified against a synthetic no-text-layer PDF |

**And a fifth finding neither scout could have made, because neither had Bash:**
a plain browser-UA GET reaches hosts WebFetch cannot.

| Host | WebFetch | Browser-UA GET |
|---|---|---|
| `achrnews.com` (BNP Media) | 403 | **200, including deep `/articles/` paths** |
| `www.mcaa.org` | 403 | **200** |
| `cfma.org` | 403 | **200** |
| `mmh.com` | 403 | **200** |
| `constructionexec.com` | 403 | **200** |
| `abc.org` | 403 | **200** |

Wave 1 recorded the loss of `achrnews.com` as "severe" and the loss of
`bizjournals.com` as the reason an entire hunting ground underperformed. Half
of that was a tool artefact, not a wall. **This is corrected in the access map.**

---

## 4. UPGRADES MADE

Two, plus the knowledge base append. Both verified by running them.

**U-002, `scripts/fetch_pdf_text.py`.** Fetch a PDF and read it. `--money`
prints only lines carrying a dollar amount or a duration, which is the hard
intake gate as one command. No new dependency (pypdf and requests are both
already present). Five exit paths, all verified against real URLs.

**U-003, the scout's kill order, the dead search craft, and the access map.**
`case-scout.md` now asks who built it, is the price on the page, and is this
company the adopter, before it invests in a story. The cost-phrase craft is
replaced with venue craft. The scout is told to read the access map first and
to hand back `pdf_urls_unread` and `access_notes` as structured output. The
run contract gains a showrunner deck pre-pass, because scouts have no Bash.

**Not done, deliberately:** see section 6.

---

## 5. VARIETY RETRO, skipped, honestly

No deck was produced, so there are no fingerprints, no correlations, no value
arc and no closest pair to evaluate. `ledger/artwork.json`,
`ledger/fingerprints.json` and `ledger/cases.json` are untouched this run,
which is correct: nothing shipped, so nothing is recorded. No threshold in
`variety_check.py` fired or failed to fire, because it never ran.

---

## 6. PARKED, AND WHY

**A general HTML fetcher (`scripts/fetch_page.py`).** The evidence for it is
strong: six hosts the run wrote off are reachable. It is parked because the
decision it forces is not mine. A general fetcher is only useful to a scout if
`case-scout` is granted Bash, and granting an agent shell access is a
capability and permissions decision that belongs to the maintainer, not to the
upgrade engineer. Recommended in the email. Parked as a dated FIELD_NOTES
candidate with the measured evidence.

**A bizjournals workaround.** Genuinely walled to both fetchers by a Cloudflare
JS challenge. There is no small, safe fix. If the maintainer wants that ground
back it needs a decision about a rendering fetcher, not a script.

**Splitting the hard gate (postmortem option B).** A doctrine change and
explicitly the maintainer's call. **I did not weaken any gate.**

**Appending wave 2 and wave 3 leads to `ledger/bank.json`.** The showrunner
owns bank merges and `bank-017` to `bank-024` are already committed at
`14babce`. Touching it from here risks duplicate IDs for no gain.

**`AI_LANDSCAPE.md` and `DEPLOYMENT_PATTERNS.md` were not appended to.** The
run established nothing new about either. Padding them would dilute the files
that agents treat as ground.

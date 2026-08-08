# SCOUT W3-A — operator conference decks, construction and trades (returned 2026-08-08)

**Result: zero banks, two thin leads.** Opened 12 decks across AGC Tech Con 2024
and 2025, NECA 2025, plus the ACEC AI report.

## THE FIND — a brand new hunting ground

> **`https://www.necaconvention.org/presentations/` is a public,
> unauthenticated index of 64 downloadable decks** from the NECA 2025
> convention (September 2025), each with title, presenter names and a direct PDF
> link. Electrical contractors presenting to electrical contractors. NECA posts
> the decks on the open web within days.

**Nobody has walked the ~50 non-AI decks on that index, and the Peckham
precedent says the cost slide hides in the session that is not titled about AI.**
NECA 2026 runs in Las Vegas and its decks should land at the same path pattern.

## THE YIELD, and what it means
Of 12 decks opened: **6 were vendors or consultants** presenting their own
product, **3 were companies well over 1,000 employees**, and **3 were genuine
operator-told segments — none of which disclosed what they paid a vendor or how
long it took to go live.** The single dollar figure found in an AI context all
day was a published **$20/month ChatGPT Plus list price on a teaching slide**.

## THIS SHARPENS THE PECKHAM LESSON RATHER THAN CONFIRMING IT

> Peckham disclosed an itemised annual cost because the punchline was "we built
> this for three thousand dollars and we are not data scientists."
> **Cost is the payoff of a build-it-cheap talk.**
>
> When a contractor bought from a vendor, the price is usually under NDA or
> simply not the point of the talk, so it never goes on the slide.
> **The intersection the series needs — bought from a vendor AND priced AND
> timelined — may be structurally rare in conference decks specifically.** Its
> likelier home is a procurement record, an interview where a reporter actually
> asked, or a direct conversation.

## TOOL CRAFT, hard-won — and it corrects W3-B
- **`r.jina.ai` has a real quota, it is not dead.** It worked for ~4 fetches,
  then 401'd on everything including the same URLs for ~15 minutes, then
  recovered. **Pace it one call at a time, never two in parallel, and treat a
  401 as "wait", not "blocked."** (W3-B concluded it was permanently dead from
  consistent 401s. That conclusion was wrong.)
- **A scout with no Bash tool has NO other PDF path.** WebFetch on a PDF returns
  raw binary and silently saves the file to the tool-results directory, but
  `Read` cannot open it because **poppler/pdftoppm is not installed.**
- Some decks are image-only exports and Jina returns nothing from them. Dead
  end, not a retry.

## WALLS CONFIRMED
- `archive.tech-con.agc.org` has **only** 2024 and 2025 session indexes.
  `/2023-` and `/2026-session-presentations/` both 404 — the latter **still 404
  two days after the 2026 conference ended.**
- `mepconference.com` 403 across the site.
- **`dev.mcaa.org` does NOT mirror `www.mcaa.org` news paths — its article URLs
  404.** This partially retracts wave 1's finding, which held only for the Smart
  Solutions case index.
- `smacna.org`, `constructionexec.com` and `abc.org` all fetch fine and are
  **unmined**.

## Leads
| Company | Note |
|---|---|
| **Sidney Electric Company** (electrical contractor, refineries, food processing, hospitals) | **~225 employees (~25 office, 200 field), $60M+** — a perfect size read, and the bottleneck language is excellent: "Managing our backlog", "Deciding on what to bid", "Low margin or low success rate Bids". **But there is no AI in it at all** — BI dashboards over their own bid history. No cost, no timeline, no before-and-after. |
| **Big State Electric** (San Antonio) | ChatGPT Plus with custom pre-prompting for NEC code lookup, meeting summarisation, spec review. **The deck is unusually good on limits — it names hallucinations, reward hacking, prompt injection and unintended training associations directly.** Real curriculum value, no deployment story, no headcount, and the interesting parts are built (Cursor, Pinecone, N8N). |

## Notable kills
**Custom Electric Inc** hurt most: perfect size (50 to 65 field plus 10 office,
$25 to $30M), partner Tom Adamson on the record — **but there is no AI in the
segment.** It is prefabrication strategy and gadget pricing (AirTags at $20, a
Stream Deck at $150).

**The ACEC AI report** is the cleanest illustration of the whole problem:
**twenty named engineering firms, twenty CTO-level quotes, and not one cost,
timeline, employee count or before-and-after number in the entire report.** It is
a posture survey, not a deployment record.

Also killed: Kraus Anderson / Hensel Phelps (three-page title deck); Burns &
McDonnell, PCL, Rosendin, Milwaukee Tool (all over the ceiling); Trimble,
OpenSpace, SALUS, HSO (vendor decks); Placer Solutions, IKERD, Dodge
(consultants); ERMCO / Westphal with RIVET (right pattern, no numbers).

## Next-run priorities from this scout
1. **Walk the remaining ~50 NECA 2025 decks**, especially the non-AI titles about
   service, prefab, systems integration and labour.
2. `abc.org/Technology/AI-Resource-Guide` — fetchable, unopened.
3. `constructionexec.com` and its Top Tech Product List — fetchable, unmined.
4. **IFMA chapter presentation pages** (`ifmaseattle.org/presentations/`
   confirmed to exist, unopened). **Chapter pages are far more open than national
   bodies.**
5. SMACNA's 2025 annual convention schedule page, to see whether it links speaker
   materials the way NECA does.

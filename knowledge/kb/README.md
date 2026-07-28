# THE KNOWLEDGE BASE — what every agent knows before it starts

Until now every agent woke up knowing HOW to work (the doctrine) and nothing
about the FIELD it works in. A scout hunting mid-market AI wins had to
rediscover, every run, where those stories get published, what a real
deployment looks like, what it plausibly costs, and which claims are
systematically inflated. That is a slow, shallow agent.

This directory is the standing knowledge. It exists so that an agent starts a
run already holding the priors a good analyst would hold, and spends its
budget on what is genuinely new instead of on rediscovering the obvious.

---

## THE HANDLING LAW (read this before you use anything here)

**Nothing in this knowledge base is a fact you may put in an artifact.**

Everything here is a PRIOR. It tells you what to expect, what to look for,
what to ask, and what is probably true. It never tells you what IS true about
a specific company, number, product, or price.

Three rules, and they do not bend:

1. **Every claim in a shipped artifact traces to a page fetched THIS RUN.**
   The knowledge base is never a citation. Not for a number, not for a price
   band, not for what a product does. If it is on a slide, somebody fetched it
   today.
2. **The knowledge base is stale by construction.** It is written from model
   training plus what past runs confirmed. This field moves in months. Treat
   every capability, price, and product statement here as "was probably true
   at some point recently, verify before use."
3. **When the knowledge base and a fetched page disagree, the page wins, and
   the disagreement gets logged.** That is how this directory gets better.

What the knowledge base IS for: knowing where to look, knowing what question
to ask next, recognising a pattern fast, spotting a claim that does not smell
right, and not wasting a run on a shape of story that has never worked.

---

## THE FILES

| File | Owns | Who must read it |
|---|---|---|
| `AI_LANDSCAPE.md` | What the technology actually is and does, in capability tiers rather than brand names. What changed recently and what did not. | every agent |
| `DEPLOYMENT_PATTERNS.md` | The recurring shapes of real mid-market AI deployments. The single most useful file for the hunt. | case-scout, fact-checker, translator, treatment-director, copywriter |
| `ECONOMICS.md` | How to reason about cost, payback, and the parts nobody quotes. | case-scout, fact-checker, translator, scorer |
| `EVIDENCE.md` | Source taxonomy, what each source type systematically omits, the standard inflation patterns, honest base rates. | case-scout, fact-checker, case-critic, scorer |
| `VENDOR_MAP.md` | Market structure by category, and how to reason about a vendor claim without asserting vendor facts. | case-scout, fact-checker |
| `ANCHORAGE.md` | The local operating context the translation lands in. | translator, copywriter, case-critic |
| `HUNTING_GROUNDS.md` | Where these stories actually live, and the search craft that finds them. | case-scout |

`config/sources.yaml` holds the operational source list. This directory holds
the reasoning about it.

---

## HOW THIS GETS SMARTER

The knowledge base is not a document somebody wrote once. It is the compounding
asset of the series.

**Every retro, the upgrade-engineer appends what the run confirmed or
contradicted**, dated, with the URL that established it:

- a deployment pattern seen in the wild for the first time
- a cost band confirmed or corrected by a real disclosed figure
- a source that turned out to be reliable, or to be laundering a press release
- a vendor category that turned out to be agent-washed
- a search that worked, and the exact query
- anything in here that a fetched page proved wrong

Format for an appended entry, at the bottom of the relevant file under
`## CONFIRMED BY RUNS`:

```
- 2026-08-04 (case file 3): mid-market quote generation deployments cluster at
  8 to 14 weeks decision-to-working, not the 4 to 6 this file assumed.
  Source: <url fetched that run>. Corrected the band above.
```

Two runs from now that entry is worth more than anything written from priors,
because it was measured rather than remembered.

**The rule that keeps it honest:** an appended entry names the URL that
established it. An entry with no source is an opinion, and opinions do not
belong in the file agents treat as ground.

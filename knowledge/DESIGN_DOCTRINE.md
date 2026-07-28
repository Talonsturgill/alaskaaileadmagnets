# DESIGN DOCTRINE — the visual standard

Read `knowledge/THE_READER.md` first. Companions: `TECHNIQUE_LIBRARY.md` (the
how), `SLIDE_DOSSIER_SPEC.md` (the plan format), `CAROUSEL_CRAFT.md` (platform
physics).

The pixel critics grade against this document. Every rule here is codifiable
and checkable.

---

## 0. THE BAR (read this before you write a line of art code)

Dana is scrolling past professional design all day. Our slides do not compete
with other AI newsletters. They compete with everything on the feed.

**The standard is: this looks like a magazine commissioned it.** Not "clean."
Not "on brand." Commissioned. If a slide could have been made in twenty minutes
in a presentation tool, it is not finished.

Three failures we have actually shipped, named so they never repeat:

1. **The uniform deck.** Ten slides of the same object with different text on
   it. The contact sheet read as one image repeated. **A deck must have visual
   RHYTHM** (section 1).
2. **The flat deck.** Every slide drawn in flat Canvas 2D while a GPU PBR bench
   and a raymarcher sat unused in `assets/js/`. **Every deck now climbs the
   rendered ladder somewhere** (section 2).
3. **The collision deck.** DOM labels positioned by hand against canvas art,
   producing clipped and overlapping text that machine QA structurally could
   not see. **Layout is now a system, not a per-slide guess** (section 3).

---

## 1. DECK RHYTHM (new, mandatory)

`knowledge/VARIETY.md` owns the full law here, both engines, with the measured
numbers and the thresholds. `scripts/variety_check.py` enforces it at
pre-planning, at every render, before ship, and in the retro. This section is
the design half of it.

A deck is a filmstrip. Judge it on the contact sheet, not slide by slide.

**No deck may use the same compositional mode more than three times.** Assign
every slide one of these modes in the dossier header, and vary them:

- **SCENE** — a rendered or deeply layered space with real depth. Atmosphere,
  focal plane, foreground occlusion.
- **OBJECT** — one hero thing, lit, centred, large. A machine, a form, a
  device, a sculpted mass.
- **DOCUMENT** — flat ink on a surface. Tables, ledgers, forms, receipts.
- **DIAGRAM** — a mechanism drawn. Flows, systems, ladders, before and after.
- **DATA** — a chart that is actually a chart, drawn to editorial standard.
- **FIELD** — a generative texture carrying a quantity. Stipple, particles,
  contours, ISOTYPE.

A legal 8 slide rhythm: `OBJECT, SCENE, DOCUMENT, DIAGRAM, DATA, DOCUMENT,
FIELD, OBJECT`. An illegal one: six DOCUMENTs in a row, which is what shipped
last time.

**And the rule underneath the rhythm rule:** no two slides in a deck may share
a mode AND a layout family, no art system is reused across slides, and every
slide carries a written sentence naming what makes it unlike the others. A
chassis is a tool for making one slide. It is not a deck.

**Tonal rhythm too.** The deck must not be one temperature and one value
throughout. Plan a value arc (dark, dark, light, dark...) and a temperature arc
in the dossier header, and verify both on the contact sheet.

---

## 2. THE RENDERED LADDER (mandatory)

`assets/js/` contains a GPU PBR bench, a CPU raymarcher, a software 3D
renderer, a film grade pass and an OKLCH colour engine. **Using none of them is
now a defect, not a stylistic choice.**

Every deck must satisfy BOTH:

- **At least one slide reaches rung 1 or 2 of the rendered ladder** below.
- **The hero slide is never flat unless the dossier argues flat deliberately
  and the pixel critic agrees the argument holds.**

**The ladder:**
1. **akthree (GPU PBR, technique #87).** Real materials, soft shadow maps, IBL
   reflections, ACES. The default for object heroes and dimensional systems.
   Roughly 3 to 9 seconds a slide. Rules are absolute: `setPixelRatio` BEFORE
   `setSize`; `await AKT.snapshot(R)` and check `.ok`; use `AKT.objectHero` for
   silhouette separation; render offscreen and `drawImage` when compositing;
   **design the Canvas fallback in the dossier, never improvise it.**
2. **aksdf (CPU raymarch, #88).** Sculpted organic masses meshes are bad at.
   One hero panel per deck, 5 to 15 seconds, cache by seed.
3. **AK3D / Zdog / CSS 3D.** The zero-dependency bench and the mandatory
   fallback design for any akthree slide.

**Finish every art canvas** with the film grade (`AKPOST.grade`, #89) and build
every ramp in OKLCH (`AKC.*`, #90). IGN dither is always on when there is a
large soft gradient anywhere in frame.

---

## 3. LAYOUT IS A SYSTEM (the root-cause fix)

The single largest quality defect in this repo's history is text landing on
other text or on art, because DOM elements were positioned by hand against
coordinates the canvas drew separately.

**The rules, and they are not optional:**

1. **Declare zones first.** Every slide's dossier declares named rectangles:
   `HEAD`, `BODY`, `ART`, `DATA`, `FOOTER`, `BRAND`. Every element belongs to
   exactly one zone. Nothing is placed outside a declared zone.
2. **One source of truth for coordinates.** If the canvas draws at x, the DOM
   label reads that same x from a shared constants object. Never retype a
   number that already exists in the art code.
3. **Text never enters the ART zone** unless it sits on an explicit knockout
   plate declared in the dossier.
4. **Every text block gets an explicit vertical budget**, and a slide's budgets
   may not overlap. Write them in the dossier before writing code.
5. **Run `python scripts/layout_check.py --render-dir ...` after every render.**
   It fails the build on text over text, text outside its declared safe area,
   and text over busy art. It catches what `qa.py` structurally cannot.

**Machine QA cannot see canvas.** It cannot see the drawn sheet, the rendered
object, or the painted field. Anything you place relative to art is invisible
to it. That is precisely why the layout gate exists, and why the dossier
declares art rectangles in canvas coordinates next to the DOM budgets.

---

## 4. THE GRID

- **12 col x 8 row module grid**, 80px outer margins, 24px gutters, all sizes
  and spacing on an 8px base unit.
- **Asymmetric composition on the symmetric grid.** Never default to centred
  stacks. Place mass off axis, counterweight with a small element.
- Restraint budget per slide: **max 2 type families, 3 type sizes, 1 accent
  colour, 1 loud visual device.** One deliberate grid violation maximum, and it
  must be argued in the dossier.
- **Negative space is the price of premium**, but empty is not the same as
  quiet. A large blank region with nothing happening in it is a hole. A quiet
  zone has texture, light falloff, or a subtle field in it, and it makes the
  loud thing louder.
- Optical over mechanical alignment. Pull display left edges out so stems
  align. Hang punctuation outside the margin.

## 5. TYPOGRAPHY

- Library: Fraunces (editorial serif), JetBrains Mono (telemetry), Space
  Grotesk, Archivo (width axis 62 to 125), Manrope (body workhorse), Instrument
  Serif, Bricolage Grotesque, Unbounded (wide statement, sparingly).
- One display voice plus one support voice per deck. Mono is always allowed as
  the third instrument voice for data and labels.
- Modular scale, 1.25 dense or 1.333 to 1.5 dramatic. Display leading 0.95 to
  1.05, body 1.3 to 1.45. Display tracking -1 to -3 percent.
- Line length 28 to 42 characters. Headlines wrap 3 lines maximum, broken at
  sense boundaries, never orphaning a preposition.
- Data uses tabular lining numerals.
- **Fit every display headline with `AK.fitText`** inside renderReady after
  `await document.fonts.ready`. Never hand-tune a display size.
- Type crimes, auto-fail: faux bold or italic, fake small caps, full
  justification, hyphenation, all-caps paragraphs, more than two families, two
  similar sans faces together.

**Type floors.** Body 32px or more. Absolute floor 24px. Any load-bearing
sourcing label is 24px or larger and is NEVER marked `data-decorative`. Only
true furniture (coordinates, crop marks, scale numerals) may go below 24 and
must carry `data-decorative`.

## 6. COLOUR

- **Dark-arctic-first.** Base is never pure black. Layered dark surfaces from
  the brand register, 2 to 3 elevation steps apart.
- Brand anchors present somewhere: flag gold `#FFC72C`, aurora family, snow.
- **Rotate the supporting palette per deck from the story's material world.**
  Sodium-lamp amber for a night warehouse, hot-metal orange for a fab shop,
  chart-paper cream for a back office. Palettes derive from the subject, never
  from a mood board.
- 60/30/10 hierarchy, most saturated colour on the smallest area.
- Gradients interpolate in OKLCH. Grain over every large gradient.
- Text contrast 4.5:1 or better at the worst point, earned by composition
  before reaching for scrims.
- **AI-slop ban list, auto-fail:** indigo-to-purple SaaS gradients, three
  evenly-rounded glass cards, thin-line icon decoration, Inter-everywhere
  sameness, unmotivated glassmorphism.

## 7. DEPTH

Flat is a choice, not a default. Compose with at least **four** depth cues:
atmospheric perspective (lerp toward sky by (i/n)^1.4), overlap and occlusion,
scale gradient, depth of field with ONE tack-sharp focal plane, fog in the
palette's sky colour, one key light at 4:1 to 8:1 with shadows sharing a single
global direction and coloured as darkened background hue, and volumetric shafts
for drama beats.

**Quantities are always parallel projection.** Never perspective on a number.
No 3D pies. Grids and labels stay flat 2D.

## 8. GENUINE DETAIL (the anti-lazy standard)

Every slide survives the zoom test. At 100 percent there is craft in every
region: texture in large fills, deliberate edges, micro-typography, annotation
furniture (leader lines, ticks, scale bars), and 2 to 4 distinct line weights
carrying meaning. Uniform line weight is the number one amateur tell.

Detail must be MOTIVATED by the story. Ornament for its own sake is also a
fail.

## 9. ART SERVES THE STORY

1. Extract the story's **geometry** (route, grid, network, floor plan), its
   **quantity** (hours, dollars, units, trucks), and its **place**.
2. Map concept to a drawable system: connectivity to networks, decline to
   ridgelines, risk to fracture, scale to ISOTYPE repetition, energy to
   particle density, regulation to grid lines interrupting a field.
3. **The field carries the data.** Parameters of the generative system ARE
   numbers from the story. State the mapping in the dossier so the critic can
   verify it.
4. **One literal anchor plus one annotation** per abstract composition. Two
   anchors maximum. Zero anchors is wallpaper and is a fail.
5. Diagram, do not decorate.

**And the reader test, above all of it:** the art exists to make Dana feel the
problem and picture the fix. A beautiful abstraction that leaves Dana unable to
picture the thing running in their building has failed, however well crafted.

## 10. CONTINUITY

Choose at least TWO per deck: panorama spine, edge tease, motif evolution
(a glyph that changes STATE, never merely brightness, with the state change
being a SHAPE change), camera move through one scene, or a palette arc.

The contact sheet review judges the deck as a filmstrip. Continuity devices
must read left to right as one composed sequence.

## 11. THE FEED TEST

Every slide is reviewed at 432px thumb width. The cover must stop a scroll at
that size. Every body slide must have one readable takeaway at that size. If a
slide only works at full size, it fails.

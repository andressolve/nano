# Style Guide — The Name of the Rose, Book Two: The Fire

**This is a DELTA against Book One's style guide.** Read [`~/Documents/nano/name-of-the-rose/01-STYLE-GUIDE.md`](../name-of-the-rose/01-STYLE-GUIDE.md) **first**. Everything in the Book One style guide carries forward into Book Two unless explicitly overridden here. This document lists only what is new or changed.

## Carry forward verbatim (do NOT redefine)

The following Book One style-guide sections apply unchanged to Book Two:

- **The Style Block** (oil-painting realism + register block + anti-drift directive). Pasted verbatim into every Book Two page prompt.
- **Period accuracy rules** (Romanesque only, no Gothic; riveted-leather spectacles; vellum codices; no firearms; no clocks; snow on every exterior; visible breath in the cold).
- **The lettering treatment** ("ivory parchment with serif ink, slightly worn at edges" caption boxes; off-white parchment-feel speech bubbles; full-width T5 hero bands; `LETTERING — verbatim, render exactly:` trigger phrase; the restrictions block closing every prompt).
- **The illuminated chapter-break style** template (gold-leaf border, fox-in-monk's-habit drollery, gilt-and-lapis historiated initial, central painted miniature, Latin tag in Gothic blackletter + English helper caption + old-Adso setup line).
- **The in-image Latin English helper canonical rule** (all four treatment types: single-line tag, Latin speech bubble, Latin column / paragraph, in-scene signage).
- **The hybrid layouts template** (3:2 page divided vertically by clean painted edge, half painting + half parchment-textured panel with decorated initial).
- **The restrictions block** (close every prompt verbatim, period accuracy clauses included).
- **The canonical six-block prompt order.**
- **The character-lock-locks-the-visual-not-the-name rule** (most acute again here for Bernard Gui on P3, P5, P6).
- **The per-page template scaffold** (paste from style guide, fill in lock blocks / setting / composition / lettering).
- **The pre-flight check** before every `edit_image` call (Glob refs, confirm ref file exists, confirm age phase if applicable — though for Book Two, like Book One, the seven days span no significant aging of any character).

## DELTA 1 — Two new illuminated tag types

Book One had four illuminated chapter-break pages, all of the same shape: a Latin daily tag (*Dies primus / secundus / tertius / quartus*) plus an old-Adso setup line. Book Two adds two new tag types in the same illuminated register:

### *Continuatio Manuscripti* — P1 frame opener

Same full illuminated-page treatment as Book One's frame opener (P1) and Day chapter breaks. The central miniature shows Old Adso again at his writing desk in Melk, but slightly older / more weighed-down than at the start of Book One (his task in this volume is to write the hardest part). The Latin tag in Gothic blackletter, centered below the miniature:

```
Continuatio Manuscripti
```

English helper caption directly below, ivory parchment, dark serif:

```
The Manuscript Continues — Days Five Through Seven.
```

Old-Adso setup-line caption box below the helper: full-paragraph recap of where Book One ended (Bernard Gui has arrived, three monks dead, the village girl in his hands), then forward-pointing into the worst days.

### *Epilogus* — P21 epilogue chapter break

Same illuminated treatment, with one variant from the four daily chapter breaks: the central miniature does NOT show "a scene of the day to come." Instead it shows **the two riders moving AWAY from the abbey on the snowy road** — a visual inverse of Book One's cover (which showed two riders moving TOWARD the abbey). Same fox-in-monk's-habit marginalia. Latin tag:

```
Epilogus
```

English helper caption:

```
Epilogue — Decades Later.
```

Old-Adso setup-line caption box: short paragraph naming the year (old Adso is writing now, ~60 years after the events), the death of William of a plague years before, and Old Adso's intent to ride back to the ruins one last time before he dies.

### *Stat Rosa Pristina Nomine* — P24 closing illuminated page

This is the volume's closing-as-invention page (parallel to Honda Vol 1 P24, da Vinci Vol 1 P22, Newton Vol 2 P23). Full illuminated-manuscript treatment, but **the whole composition reads as the final folio of Adso's manuscript** — the central artifact this time is the Latin tag itself, given more visual weight than any other text element on any page in either volume:

```
Stat rosa pristina nomine, nomina nuda tenemus.
```

Set in larger Gothic blackletter than the other tags, centered, the prominent text on the page. English helper caption directly below, slightly larger than the daily-tag helpers:

```
The rose of old remains only in its name; we hold only naked names.
— the final line of Adso's manuscript.
```

The historiated initial encloses the same Old Adso writing-cell scene used inside Book One P1 — closing the frame. The central miniature shows the burned abbey ruins from a distance, decades later, snow on the broken walls. Fox-in-monk's-habit marginalia held one last time. The old-Adso voice closing caption (~150 words) is the volume's final paragraph: Adso is dying, the library is gone, William is gone, the village girl is gone, and what remains is this manuscript and the name *rose* that no one now knows for certain refers to what.

## DELTA 2 — Dream-sequence register variant (P12 only)

P12 visualizes Adso's *Coena Cypriani* dream — a real 9th-c. medieval Latin parody of the Last Supper as a wedding feast where biblical figures (Adam, Eve, Christ, the apostles, John the Baptist) behave in deliberately grotesque or comic ways. It is exactly the kind of "blasphemous laughter" Jorge spent the seven days killing to suppress. The dream is rendered as a swirling vision **above** the sleeping Adso, visible to the reader but not to the other characters.

**Register variant — paste this into the P12 prompt in addition to the standard Style Block:**

```
DREAM REGISTER (this page only): Same oil-painting realism, same painted brushwork, same muted period palette as the rest of the volume — BUT tilted: slight skewed perspective in the dream-content area, colors more saturated than the volume default (deeper reds, brighter golds, more luminous candleflames), faces of the dream-figures slightly distorted (eyes a touch too large, mouths a touch too wide, gestures a touch too theatrical). NOT a comic. NOT a cartoon. NOT a children's-book illustration. Still oil-painting realism — but oil-painting realism of an uneasy dream. The waking foreground (sleeping Adso in the cold chapel) stays in the volume's normal palette and perspective; the contrast between the two is the point.
```

The dream-content and the waking-Adso foreground share the same painted brushwork but are visually distinct enough that the reader can tell at a glance which is the world and which is the dream. Single page, single use. Do not apply this register to any other page.

## DELTA 3 — Fire palette (P19, P20, cover)

Three pages in Book Two are fire pages: the interior of the library taking the flame (P19), the exterior of the abbey engulfed at night (P20), and the cover (the abbey at night with a single library window glowing warm-amber — pre-fire, foreshadowing only).

**Fire palette block — paste this into the P19, P20, and cover prompts in addition to the standard Style Block:**

```
FIRE PALETTE (this page): Deep orange and red-gold flame glow contrasted against the cold stone-grey and snow-white of the volume's default palette. Ember-black and acrid grey smoke against snow. Backlit silhouettes of figures and architecture — figures rendered as cinematic silhouettes against firelight where appropriate. The fire is the only warm light source in the scene; everything not lit by fire is in cold deep shadow. Painted brushwork — NO digital glow effects, NO lens flare, NO halftone. Heavy chiaroscuro, the orange of the fire and the blue-grey of the winter night fighting for the frame.
```

The fire palette is a sub-register, not a register replacement. The Style Block (oil-painting realism, period accuracy, etc.) still applies on top of it.

For the **cover** specifically, the fire palette is restrained — only one high library window is lit warm-amber, the rest of the abbey and the surrounding mountain still in the cold-dawn / cold-night palette of Book One's cover. The single glowing window is the volume's foreshadowing of the fire to come without spoiling the act itself.

## DELTA 4 — Composite reference plate protocol — applied from production day one

Book One built composite reference plates only after the audit pass forced the fix. Book Two builds them **before** any page generation, per RULE 1 of the Book One retrospective. The protocol:

1. **Identify every page with 3+ named cast members from the project's locked cast.** For Book Two: P3 (William + Abbot + Gui), P5 (Gui + Remigio + Salvatore + village girl), P6 (Gui + Remigio + Salvatore + village girl + Adso watching), P17 (William + Adso + Jorge), P19 (William + Adso + Jorge + the fire). Five candidate pages clustered into three scene groups.
2. **Build one composite per scene group, not per page.** Compositing per page wastes calls; compositing per scene gives you a reusable single image:
   - `refs/composite_chapter_house_disputation.png` — William + Abbot + Gui (P3, optionally P14 Abbot's chamber if the Abbot's lock is helpful there).
   - `refs/composite_condemnation.png` — Gui + Remigio + Salvatore + village girl (P5 interrogation, P6 condemnation). Four characters on one canvas.
   - `refs/composite_finis_africae.png` — William + Adso + Jorge (P17 confrontation, P19 fire begins).
3. **Build each composite with all component refs when the current image tool supports multi-reference editing.** In this Codex session, the bundled imagegen CLI supports repeated `--image` inputs for `gpt-image-2`; use that. If a later production path only accepts one reference image, anchor on the visually-trickiest single character ref so at least that face is preserved verbatim. Per the Book One retrospective: building composites with no reference input lets every face drift simultaneously, defeating the purpose.
   - For `composite_chapter_house_disputation.png`: anchor on `ref_gui.png` (real-historical figure risk, easiest to drift).
   - For `composite_condemnation.png`: anchor on `ref_gui.png` (same reason).
   - For `composite_finis_africae.png`: anchor on `ref_william.png` (near-bald tonsure + rope-belted Franciscan habit hardest to describe in prose; Jorge's milky blind eyes and Adso's blond tonsure are described-in-prose features that the model handles reliably given a strong anchor).
4. **Re-Read every involved character ref BEFORE writing the composite prompt.** Write a one-line verbatim observation per character into the working notes. RULE 2 of the Book One retrospective applies most stringently here — the composite is the most-load-bearing image in the volume after the cover, and if its prose is wrong every downstream page poisons.
5. **Composite format: horizontal landscape triptych (or quadtych for the four-character `composite_condemnation`)**, each character full-length, same painter / same light / same scale, plain warm-toned neutral background, thin painted name label below each figure. Use the per-character ref's height/build accurately — Jorge taller and bent; Adso slight; Salvatore short and hunched; Gui tall and very straight-backed; Remigio heavy-set and broad; village girl small and thin.
6. **Pass the composite as the single `imagePath` for every page in its scene group.** The prompt prose for each downstream page only describes pose, placement, costume detail, and per-page action. Every face is already locked by the composite.

## DELTA 5 — Cover register

Book One cover: Aedificium at cold dawn, two tiny riders ascending the snow road, gilt-with-red-inner-shadow title block.

Book Two cover: **same Aedificium ref, same composition**, but shifted to night. One small change with large effect — a single high library window in the tower glowing warm-amber, suggesting candlelight from within. The road is empty (or shows two tiny riders DESCENDING — direction flipped from Book One). Heavy snow on the roofs and surroundings, full night, a pale moon behind clouds. The title block uses the same gilt-with-red-inner-shadow display serif as Book One.

Title block:

```
THE NAME OF THE ROSE
Book Two: The Fire
after the novel by Umberto Eco
```

The glowing window is the volume's single foreshadowing element — restrained enough not to spoil the fire as the climax, deliberate enough to mark Book Two as the volume *about* the fire. If during prototype generation the glowing window reads as ambiguous (just a bedroom candle, no menace), brighten it slightly and add a faint trace of smoke at the window mouth. Do not make the cover the burning-abbey itself — that beat is reserved for P20.

## DELTA 6 — Old Adso continuity check protocol

The new `ref_old_adso.png` must be visually consistent with Old Adso as glimpsed inside Book One P1's historiated initial (a small painted scene inside the bowl of the illuminated "I"). Procedure:

1. Before writing the Old Adso ref prompt, **Read `~/Documents/nano/name-of-the-rose/pages/page-01.png` and look at the historiated initial in the upper-left.** Describe verbatim into the working notes what Old Adso looks like there: beard length, beard color, hair (or baldness) on the crown, habit color, hands, posture, the writing desk and quill.
2. The new ref must show the same person, at the same age, in the same kind of cell, with the same desk and quill, in the same black Benedictine habit. The ref is a *larger view* of the same Old Adso, not a different Old Adso.
3. The ref's full-body view will be used as a `composite` partner for any downstream multi-character scene in the epilogue — though for Book Two the epilogue pages (P22 William + Adso ride away; P23 Old Adso alone at the ruins; P24 closing illuminated page) feature Old Adso either alone or with William, never in three-character scenes, so no composite is needed for the epilogue.
4. The casting check at the ref gate: does the ref's Old Adso match the Old Adso inside Book One P1's historiated initial? If no, regenerate before passing the gate.

This is the only continuity check in Book Two that depends on an existing rendered page rather than on a fresh ref. Treat the existing page as authoritative source material — Old Adso is one of the volume's repeating characters and his look must remain stable.

## DELTA 7 — Reader hours-strip footer ships from Day One

Book One bolted the persistent prayer-hours-strip footer ("Prayer hours of the Benedictine day", Matins → Compline, current page's hour highlighted in gold) onto the reader at audit time after the user flagged the period-vocabulary problem. Book Two ships this footer from the first commit of the reader, not later. The reader's HTML template is copied from `~/Documents/nano/name-of-the-rose/index.html`; preserve the footer block, the highlighting logic, the page-info label position above the footer, and the hide-on-quiz behavior verbatim.

When mapping pages to canonical hours for the highlighting logic:
- **P1 Continuatio** — no hour (frame opener, hide the highlight or default to Matins).
- **P2 Dies Quintus, P3–P8** — Day 5 hours run from Sext (P2 / P3 chapter house disputation) through Vespers (P8 cloister conversation).
- **P9 Dies Sextus, P10–P14** — Day 6 hours run from Matins (P10 Malachi collapses) through Vespers (P14 hidden door found).
- **P15 Dies Septimus, P16–P20** — Day 7 hours run from Compline-of-Day-6 / Matins-of-Day-7 (P16 climbing into finis Africae) through what the bells would have called Lauds if anyone were ringing them by the time the abbey burned. The seventh day ends without canonical hours because the bells stop ringing.
- **P21 Epilogus, P22–P24** — no hours (epilogue is decades later, secular framing). Default-hide or fade the strip on these pages, or fade it to a thin line — UX call to make at reader-build time.

## DELTA 8 — No new restrictions block

Use Book One's restrictions block verbatim. No additions.

## DELTA 9 — Per-page prompt template

Use Book One's per-page template scaffold (Style Block → character locks → setting → composition → lettering verbatim → restrictions block). No structural change. The only new elements you may insert between the Style Block and the character locks, **only on the pages that need them**, are:

- The **DREAM REGISTER** block (P12 only).
- The **FIRE PALETTE** block (P19, P20, cover only).

Neither replaces the Style Block. Both stack additively on top of it.

## Casting checks — gate before any page generation

For each of the 5 new single refs (Old Adso, Remigio, Malachi, Severinus, Aristotle codex) AND the 3 composite refs (chapter_house_disputation, condemnation, finis_africae), before passing the gate:

- [ ] **Single refs:** Age right? Habit color right? Distinctive marker visible? Register matches Book One refs and Newton / Honda / da Vinci (oil-painting realism, NOT comic, NOT children's book, NOT digital-painting / concept-art)? Period-accurate (no modern artifacts)?
- [ ] **Old Adso continuity:** Matches Book One P1 historiated initial Old Adso?
- [ ] **Composite refs:** All named characters present and recognizable against their single refs? Same painter / same light / same scale across the composite? Faces oriented forward (three-quarter view, not in profile)? Plain neutral background? Name labels readable (thin painted serif, not modern type)?
- [ ] If any ref fails, regenerate before proceeding. A drifted ref poisons every page generated from it. A drifted composite poisons every page generated from the entire scene group.

This gate matches Book One's gate, extended for the composite-ref protocol.

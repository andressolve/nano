# 01 — STYLE GUIDE · "The Pea Square"

## Register
**Botanical-plate continuity** — the book should feel like *Mendel's own notebook, opened up and annotated for you*. A 19th-century naturalist's study-plate: aged cream paper, pea plants in fine ink line + soft watercolour wash, hand-ruled pencil/chalk grids, the contrasting traits laid out like a careful field study. Warm, period, hand-made — NOT a glossy modern infographic, NOT a comic. This deliberately matches the Mendel biography (`../mendel/`) so the two read as shelf-companions; the difference is this book is **diagrammatic and explanatory** where the bio was cinematic.

This is an **explainer**, not a narrative — there is no protagonist, no drama, no speech bubbles (except possibly one small Mendel cameo). The "scenes" are teaching plates: a grid, a pair of plants, a row of peas, a tally. Clarity of the math is the first priority; warmth of the plate is the second.

## STYLE BLOCK — paste verbatim into every page prompt
> 19th-century botanical study-plate in oil-and-watercolour realism, like a naturalist's notebook page opened up. Aged cream paper ground, fine ink linework with soft watercolour washes, hand-ruled pencil and chalk grids, period serif and handwritten labels. Warm, patient, hand-made — pea-plant green and pea-blossom violet as the living accents against cream paper and soft sepia. Painterly, tactile, visible paper grain and pencil texture. NOT a glossy modern infographic, NOT a photograph. Calm even daylight, the look of a careful field study.

## REGISTER BLOCK — paste verbatim into every page prompt
> Botanical-plate illustration, ink-and-watercolour realism on aged paper. NOT a comic, NO halftones, NO cel shading, NO hard ink-outline cartoon look, NO glossy vector-infographic flatness. Hand-painted naturalist's plate with pencil-ruled diagrams.

## ANTI-DRIFT DIRECTIVE — paste verbatim into every page prompt
> NOT a children's book. A serious, beautiful science plate for a thoughtful reader. Realistic plant rendering, clean legible diagrams, calm composition. NOT cute, NOT cartoonish, NO mascots, NO oversized features.

## Palette
- **Base:** aged cream / ivory paper, soft sepia ink, warm graphite-pencil grey, chalk white.
- **The two living accents (the through-line):** **pea-plant green** (`~#6fa86b` family — leaves, vines, pods) and **pea-blossom violet** (`#9176c4` — the flower, and the reader's accent colour). These two carry continuity with the Mendel biography. Yellow vs green peas add a warm gold where the seed-colour trait is shown.
- **The grid:** always rendered as **hand-ruled pencil/chalk on the cream paper**, never as a crisp modern printed table. The Punnett square is *Mendel's own working*, not a textbook diagram.

## The factor notation (lock this — used on almost every page)
- A dominant factor = a **capital letter card** (e.g. **T** for tall); a recessive factor = the **same letter, lowercase** (e.g. **t** for short). Rendered as little **handwritten cards / tiles** on the paper, so a non-reader still sees "big letter / small letter = two versions of one thing."
- Default worked example through the book = **Tall (T) vs short (t)** for the single-trait pages, because it's the bio's example (tall × short). For colour where helpful: **Yellow seed (Y) vs green seed (y)**, **Round (R) vs wrinkled (r)**.
- **Always gloss the letters in plain words on first use:** "T stands for the tall factor; little t for the short one." Never assume the reader knows what T/t mean.

## Grid-rendering discipline (the geometry risk — load-bearing)
The Punnett square is the hero object and the model's biggest failure mode. Rules:
- Keep grids **small and clean**: a **2×2** for single-trait pages, a **4×4** only on the P11 dihybrid POSTER. Never more.
- **Parents' factor cards sit along the top edge and the left edge**; each inner cell shows the **combination** (two letter-cards) and a tiny painted plant/pea showing what it looks like.
- State the exact cell contents in the LETTERING block so the model fills them correctly (don't let it improvise letters).
- If a grid renders with wrong/duplicated letters after 2 tries, **build the grid with PIL locally and composite it onto the painted plate**, OR generate the painted plate with an empty ruled grid and overlay clean letter-cards. Do not burn >2 regens fighting the model's handwriting — switch to the composite approach (validated technique, see skill).
- Consider `thinking=true` on P5 and P11 only (geometry-critical), opt-in.

## In-image text → always clear to a first-time reader (CAPTION CLARITY RULE)
- Every caption/label stands alone. Gloss every symbol and term on first use: "allele (one version of a factor)," "dominant (the version that shows)," "recessive (the version that hides)," "genotype (which factors it carries)," "phenotype (what it looks like)." Use the plain-word gloss *first*, the technical word *second* and sparingly.
- Numbers are the point: render **3 : 1**, **1 : 2 : 1**, **9 : 3 : 3 : 1** as bold, clean, hand-lettered ratios — these are the emotional artwork of their pages.
- Keep caption boxes few and short per page; this is a teaching plate, not a wall of text. If a page needs more than ~3 short text zones + the diagram, split it.

## Caption / label style (hold all volume)
- **Caption boxes:** aged-cream paper insets with soft sepia serif text — like a notebook annotation. Readable, calm.
- **Diagram labels:** handwritten-pencil style, short, pointing with thin painted leader-lines to the thing they name.
- **Ratios:** large period serif or confident chalk, the focal artwork of the page.

## Restrictions block — close every prompt with this
> All words and letters spelled and rendered correctly. Do not duplicate text. Do not invent extra labels or captions. Render every grid cell exactly as specified. NO modern logos, NO watermarks, NO QR codes, NO modern UI, NO photographic sheen.

## The POSTER / cutaway page (explainer template, used on P5 & P11)
A single big central diagram (the grid machine) on the cream plate, with 3–5 short labelled callouts pointing to its parts with thin leader-lines, a title strip at the top, and one summary line at the bottom. Same scaffold the mil-tech explainers used for POSTER pages, re-skinned to the botanical-plate register (pencil leader-lines, cream paper, no dark schematic background).

## Footer concept-strip (reader)
A persistent strip showing the **grid growing up**: factor → 2×2 → 3:1 → 1:2:1 → 4×4 → 9:3:3:1, highlighting the stage the current page is on (the explainer-mode footer device, like the KILL-CHAIN / IRON-TRIANGLE strips). Reinforces the "one machine, built up" spine.

## Anti-drift watchlist
- Keep it a **botanical plate**, never sliding into (a) glossy modern infographic flatness or (b) children's-book cartooning. The register block guards both.
- **Grids stay hand-ruled pencil/chalk** on cream paper — if a crisp printed table appears, regen.
- **Letters must be correct** (T/t, R/r, Y/y) and match the cell math — the #1 thing to check on every grid page.
- The two accents (pea-green + violet) mark *life*; don't flood the cream plate with colour — it's mostly paper, ink, and pencil, with green/violet as the living spots.
- No cells, no chromosomes, no DNA, no double helix — the depth ceiling is the arithmetic (see brief). If the model adds a helix or a cell, regen.

# 00 — PROJECT BRIEF · "The Pea Square"

## Title
**The Pea Square — How to Predict a Living Thing**

(Landing-card subtitle: *Mendel found a hidden three-to-one in his garden. This is the machine underneath it — a grid you can fill in yourself.*)

## What this is
An illustrated **explainer** (explainer mode of the graphic-novel skill — concept spine, no human protagonist arc) on **how heredity actually adds up**: alleles, dominant/recessive, the Punnett square, and where the 3:1, 1:2:1, and 9:3:3:1 ratios come from. **14 pages + cover + dark-flipper reader + 5-question WHY-quiz + landing card.**

It is the **companion to the Mendel biography** (`../mendel/`). The biography told the life and *glossed* the science; this book *fully explains* the science the biography pointed at. The two snap together: the bio ends on the 3:1 as a mystery; this book opens on the 3:1 and derives it.

## Why
The user asked to expand on Mendel-related science as a deliberate **bio + math** pairing, with the objective to **FULLY explain, not gloss**. Mendelian inheritance is the rare big idea where "fully explain" and "a kid can re-enact it with paper and pencil" are the same thing — a Punnett square is arithmetic on a 2×2 grid. This is the strongest agency hook in the collection (per the skill's "can the kid DO it?" rubric).

## Audience standard
Honor the CRITICAL FRAMING RULE: write so any first-time reader can follow — no age-pitching, clear but **not dumbed down**. The whole point of this volume is that it does NOT gloss: every ratio is *derived on the page*, not asserted.

## The organizing idea (the concept spine)
**The grid, built up one layer at a time.** Each page adds exactly one idea and the reader can fill in the next grid themselves. The 2×2 Punnett square is the recurring "machine"; by the end it scales to a 4×4 and the reader sees the same machine produce every Mendelian ratio. Heredity = counting outcomes on a grid.

## The depth ceiling (LOAD-BEARING — do not violate)
**Level 1: classical Mendelian / transmission genetics ONLY.** The "factor" (allele) is a **black box**, exactly as Mendel treated it.
- **YES:** allele, dominant/recessive, genotype vs phenotype (in plain words), pure lines, the Punnett square, 3:1, the hidden 1:2:1, probability as counting outcomes, the test cross, two-trait independent assortment, 9:3:3:1, the honest caveat that not all traits are clean either/or (incomplete dominance, multiple versions).
- **NO — out of scope, do not open:** cells, chromosomes, meiosis, DNA, genes-as-molecules, proteins, mutation-as-sequence-change. We never explain *why* the factors come in pairs or separate — we just establish that they do (as Mendel did) and do the arithmetic. Going further would require half-explaining cell biology, which breaks the "fully explain" promise at this level.
- This ceiling keeps the book 100% re-enactable and historically honest. If a later companion wants the cell/DNA layer, that is a *separate* book (Level 2/3).

## Scope decisions
- **Math only.** No ethics thread, no eugenics detour (a real historical shadow of genetics, but out of scope for a Level-1 arithmetic explainer for this audience; do not raise it).
- **Mendel appears only as a small framing cameo** (P1 open, P14 close) to bridge to the biography — he is NOT a protagonist here. The "characters" are objects: the factor tiles, the pea plant, the pea/blossom, and the grid.
- **Honesty caveat page (P12):** explicitly tell the reader the clean either/or rules are Mendel's *chosen* simple case — some traits blend (red × white snapdragon → pink), some come in more than two versions. This prevents the book from over-promising. Still Level 1 (no cells needed to say "some traits mix").
- **Frame device:** P1 (Mendel's 3:1 as an unexplained number) is re-read and *answered* on P6, then fully closed on P13/P14.

## Visual register (see 01-STYLE-GUIDE)
**Botanical-plate continuity** — "Mendel's notebook, opened up." Aged cream paper, 19th-century naturalist's ink-and-watercolour pea illustration, Punnett grids hand-ruled in pencil/chalk as if in Mendel's own hand, the factors as little handwritten cards. Violet (`#9176c4`) + pea-green accents, matching the biography so the two read as shelf-companions. This is a *deliberate* departure from the freed glossy/gritty register of the mil-tech explainers — chosen for continuity with the Mendel bio.

## Spine (14 pages)
P1 hook (Mendel's 3:1 — why exactly?) → P2 the factor (pairs, one from each parent) → P3 dominant & recessive (what shows vs what's carried) → P4 pure lines → all hybrids (the "vanishing" trait) → **P5 POSTER: the Punnett square explained (the machine)** → P6 3:1 derived (Tt × Tt, fill the grid) → P7 the hidden 1:2:1 → P8 probability = counting squares (coin-flip re-enactment) → P9 the test cross (TT or Tt? cross and count) → P10 two traits at once (independent assortment) → **P11 POSTER: the 4×4 dihybrid grid → 9:3:3:1** → P12 when the clean rules bend (honest caveat) → P13 the same arithmetic everywhere (re-read the opening) → P14 DO IT YOURSELF (breed paper peas / coin-flip toward 3:1).

## POSTER pages (the explainer-mode cutaway template)
- **P5** — the Punnett square as a labelled "machine": how to draw it, parents' factors along the edges, how each cell is filled. The tool page.
- **P11** — the 4×4 dihybrid grid producing 9:3:3:1, the big scaled-up payoff.
(These two are the geometry/text-dense pages — prototype first.)

## Production plan
1. **Refs** (botanical-plate register): factor tiles (T/t cards), pea plant (tall vs short), pea (round/wrinkled + yellow/green) & blossom (violet/white), the blank Punnett-grid device, small Mendel cameo. → `refs/`. **Check in with user before generating (first money step).**
2. **Prototype 3 pages** spanning format/density: **P5 (POSTER, the grid machine)**, **P6 (3:1 derived — the core payoff)**, **P11 (POSTER, 4×4 → 9:3:3:1, most text-dense)**. Validate register + grid legibility before bulk.
3. **Bulk-generate** remaining ~11 pages + cover in parallel waves.
4. **Reader** (dark flipper cloned from `mendel/index.html`, **violet `#9176c4` accent** for shelf-continuity, footer concept-strip showing the grid stages) + 5-question WHY-quiz (length-matched distractors, shuffled positions) + landing card + footer entry in root `index.html`.
5. User QA → audit regens → commit `pea-square/` + `index.html` only when asked.

## Cost envelope
~15 pages + cover + ~6 object refs (+ maybe 1 PIL composite) on gpt-image-2 standard 1536×1024 ≈ **$4.0–4.5**. Grid/text-dense POSTER pages may need a regen or two; budget for it.

## Tooling note
Session scoped to nano → `mcp__openai-image-2__*` available. The grid pages are geometry+text critical; if a Punnett grid won't render cleanly on standard, consider `thinking=true` on that page only (opt-in, higher cost) before falling back to a PIL-built grid overlay.

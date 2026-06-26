# 02 — CHARACTERS · "The Pea Square"

This is an **explainer** — there is no human protagonist. The "characters" are **objects**: the factor tiles, the pea plant, the pea/blossom, the Punnett-grid device, and a single small Mendel cameo for the P1/P14 frame. Each gets a lock block + a reference-sheet prompt, exactly as a biographical mode locks a face — because object drift (a grid that re-rules itself, a tile that changes its handwriting, a pea that turns photographic) breaks continuity just as visibly as a drifting face.

All refs are generated against the **botanical-plate register** (paste STYLE + REGISTER + ANTI-DRIFT from `01-STYLE-GUIDE.md` ahead of every ref prompt). Landscape-ish framing on a plain aged-cream ground, no extra labels. `refs/ref_<name>.png`.

---

## OBJECT 1 — The factor tiles (THE hero object, on almost every page)
**Lock:** Small **hand-cut cards / wooden tiles** resting on cream paper, each bearing **one hand-inked serif letter**. A **dominant** factor = a **CAPITAL** letter (e.g. **T**); a **recessive** factor = the **same letter lowercase** (e.g. **t**). The capital tile is faintly warmer / firmer in ink weight; the lowercase tile a touch lighter — but they are obviously *the same letter, two sizes*. Tiles are plain, period, hand-made: slightly irregular edges, soft drop-shadow on the paper, visible paper or woodgrain. NOT printed Scrabble tiles, NOT modern flashcards, NO rounded cartoon bubbles.
**Default letters through the book:** **T / t** (tall / short). Secondary sets only where the script calls them: **Y / y** (yellow / green seed), **R / r** (round / wrinkled seed).
**Ref-sheet prompt:** a reference row on aged cream paper showing six hand-inked tiles — **T t**, **Y y**, **R r** — each a small hand-cut card with one serif letter, capitals slightly bolder than lowercase, soft pencil shadow, visible paper grain. Period naturalist's hand-lettering. No other text, no labels, plain cream ground.

## OBJECT 2 — The pea plant (tall vs short)
**Lock:** A garden pea plant (*Pisum sativum*) in fine ink line + soft watercolour wash. **Tall** = a tall climbing vine on a thin cane, reaching up, more internode length. **Short** = a low compact bushy plant, same leaf and tendril forms, clearly stunted in height. Same species, same green (`~#6fa86b`), same blossom — **only height differs**, so the contrast reads instantly. Botanical-plate accuracy: pinnate leaves, curling tendrils, pods. NOT a cartoon sprout, NO face, NO mascot.
**Ref-sheet prompt:** botanical study-plate showing the same pea plant in two heights side by side — a tall climbing vine on a cane at left, a short compact bush at right — fine ink line and soft green watercolour wash on aged cream paper, pinnate leaves and curling tendrils, identical species and colour, differing only in height. No text, no labels.

## OBJECT 3 — The pea seeds (round/wrinkled, yellow/green)
**Lock:** Individual pea seeds painted as botanical specimens. **Round** = smooth full sphere; **wrinkled** = shrivelled, dimpled. **Yellow** = warm gold; **green** = soft pea-green. Used on the seed-colour / seed-shape trait pages and inside grid cells as the "what it looks like" token. Tactile watercolour, NOT glossy 3D render.
**Ref-sheet prompt:** botanical specimen row on cream paper — four pea seeds: a smooth round yellow pea, a smooth round green pea, a wrinkled yellow pea, a wrinkled green pea — soft watercolour and fine ink, visible paper grain. No text.

## OBJECT 4 — The pea blossom (violet vs white)
**Lock:** The pea flower — the book's **violet accent** (`#9176c4`) and the continuity link to the biography. The signature bloom is **violet-purple**; a **white** variant appears where the flower-colour trait is shown. Botanical-plate rendering: standard pea-flower form (banner, wings, keel). The violet blossom is the single most saturated spot of colour on most plates.
**Ref-sheet prompt:** botanical study of a garden-pea blossom — one violet-purple flower and one white flower of the same pea plant, fine ink line and watercolour on aged cream paper, accurate pea-flower form. No text, no labels.

## OBJECT 5 — The Punnett-grid device (the recurring "machine")
**Lock:** A **hand-ruled square grid** drawn in **pencil/chalk on the cream paper**, as if in Mendel's own hand — slightly imperfect rules, soft graphite texture, NEVER a crisp modern printed table. Default form = **2×2**; the scaled-up form on P11 = **4×4**. Parents' factor tiles sit **along the top edge and the left edge**; each inner cell holds the **combination** (two letter-tiles) plus a tiny painted plant/pea showing the phenotype. The grid is the hero — keep it clean, square, legible.
**Ref-sheet prompt:** a blank 2×2 grid hand-ruled in pencil on aged cream paper, slightly imperfect hand-drawn lines, soft graphite texture, room along the top edge and left edge for letter-cards, empty cells. Naturalist's notebook working, NOT a printed table. No text inside the cells.

## OBJECT 6 — The ratio numerals (the emotional artwork)
**Lock:** The ratios **3 : 1**, **1 : 2 : 1**, **9 : 3 : 3 : 1** rendered as **bold confident hand-lettering** — large period serif or chalk — the focal artwork of their pages. Pea-green / violet / sepia ink. These are deliberately the most "designed" text on the page. NOT a modern infographic font, NOT neon.
**Ref-sheet prompt:** (no separate ref needed — specify directly in each page's LETTERING block; this entry exists so the numerals stay consistent in weight and style across pages.)

## CAMEO — Mendel (P1 open, P14 close only)
**Lock (reuse from the biography, mid phase):** a stout, **clean-shaven** man (~38–50), round face, **gold-oval spectacles**, **black Augustinian habit**, kindly patient expression. On P14 the **silver pectoral cross** of the abbot may show. He appears small and framing — a hand entering frame to set down a tile, or a half-figure at the edge of the plate bending over the peas — NEVER a full dramatic portrait. **Always clean-shaven** (the model loves to add 19th-c. facial hair — state "NO beard, NO moustache" every cameo prompt). He is a *bridge to the bio*, not a protagonist.
**Ref-sheet prompt:** reuse `../mendel/refs/` mid-phase Mendel ref if available; otherwise — a stout clean-shaven man about 45 in a black Augustinian habit, round face, gold oval spectacles, kindly patient expression, half-length, painted oil-and-watercolour realism on a plain warm ground, NO beard, NO moustache, no text.

---

## Anti-drift watchlist for objects
- **Tiles:** capital vs lowercase must stay legibly *the same letter at two sizes* — the whole notation rests on it. Wrong/duplicated letters in cells = regen (the #1 grid failure).
- **Grid:** stays **hand-ruled pencil/chalk**; if a crisp printed table appears, regen. 2×2 default, 4×4 only on P11.
- **Plant/seed/blossom:** botanical-plate realism, never cartoon, never a face. Violet blossom carries the accent — don't let it wash out to blue or pink (pink is reserved for the P12 incomplete-dominance snapdragon).
- **Mendel cameo:** clean-shaven, small, framing only.

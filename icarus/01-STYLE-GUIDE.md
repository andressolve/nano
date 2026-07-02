# 01 — STYLE GUIDE

## Register B — ink-line + flat color (series signature)

This volume launches the Myth & Epic shelf's look. Match the exemplars in `refs/` exactly:
`icarus_B_inkflat.png` (the cover-energy frame) and `page_daedalus_icarus_v1.png` (the approved 3-panel page).

### Style Block — paste verbatim into every page prompt (blocks 1–2)

> Bold ink-line comic-book art with FLAT vivid color, in the tradition of modern mythology graphic novels (the George O'Connor *Olympians* idiom). Clean confident black linework, flat saturated color fills, minimal soft rendering, dynamic heroic energy. Warm Aegean palette: golden sun, deep sea-blue, sun-bleached stone, terracotta and cream tunics. Strong directional light, high skies. Cinematic comic composition.

### Anti-drift directive — paste verbatim (block 3)

> NOT a children's book. Serious mythic tone, realistic heroic proportions. Clean adult graphic-novel linework, NOT cute, NOT chibi, NO oversized eyes, NO soft pastel storybook look.

### Palette

- **Sky/sun:** golden-white sun core, radiating warm yellow-orange, thin ray lines. The sun is the volume's antagonist — it grows larger and hotter across P9→P12.
- **Sea:** deep saturated blue with flat lighter-blue highlight bands. Whitecaps as clean white flecks.
- **Stone:** sun-bleached cream/tan (Cretan cliffs, tower, Knossos walls).
- **Tunics:** Daedalus terracotta-brown; Icarus cream/white; Minos royal (deep red + gold).
- **Wings:** white-and-tan feathers, gold-tinged in sunlight; loosening feathers drawn as clean individual shapes.
- **Accent of dread:** as the sun grows, warm color floods the top of the frame; the sea-blue shrinks. On the fall page the palette goes hot-white and empty.

## Lettering treatment

- **Speech bubbles:** clean white ovals, black comic lettering, solid black tail pointing to the speaker. NO quotation marks inside bubbles — the bubble is the quote.
- **Caption boxes:** small rectangular boxes, cream/parchment fill, dark serif or clean sans lettering, anchored to a top or bottom corner. These carry narration.
- **Density:** do NOT hold back. Multiple bubbles + a caption box per page is the norm (the approved test page ran 8 elements / ~75 words cleanly). Keep each individual element legible — no single 40-word bubble — but let the story breathe.
- Every text element quoted verbatim from 04-SCRIPT in the `LETTERING — verbatim, render exactly:` block.

## Layout rules

- **3:2 landscape, 1536×1024.**
- **3–4 panels per page**, layout stated explicitly (e.g. "TWO equal panels across the top, ONE wide panel across the bottom"). Reading order named.
- **Clean solid-black panel borders, clear white gutters.**
- Cover and the final meditation page may be single full-bleed images (no panel grid).

## One-shot whole-page bake

Generate the entire multi-panel page — all panels + all lettering — in a single call. Do NOT composite panels or add text via code. gpt-image-2 holds the recurring cast across panels and renders the lettering in-image (validated on the test page).

## Moderation

- The fall (P11–P12) is rendered as **flight failing**: wings coming apart, feathers scattering on the wind, Icarus small and high in silhouette against the sun. Never a body plummeting toward death (trips the self-harm filter).
- The grief (P13) is **aftermath**: empty sea, feathers on the water, Daedalus circling above. No corpse.
- The Minotaur (P2–P3) is a monster in shadow / mid-lunge, not gore. Theseus's kill is implied (spear raised, or the beast falling in shadow), not butchery.

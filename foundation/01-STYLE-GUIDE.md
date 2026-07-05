# Style Guide — Foundation: The Plan

## STYLE BLOCK (paste verbatim into every prompt, first)

> 1970s British science-fiction paperback cover art, smooth airbrushed gradients, hazy atmospheric depth, monumental scale. Saturated teal, magenta, amber and deep space-black palette with glowing horizon light. Chrome and candy-colored machinery with crisp airbrush highlights; soft-edged atmospheric haze behind. Painterly period airbrush rendering — NOT modern digital concept art, NOT cel shading, NOT halftones, NOT ink linework.

## REGISTER / ANTI-DRIFT (paste verbatim, second)

> NOT a children's book. Serious mature science-fiction graphic novel, realistic proportions, cinematic composition, natural dramatic lighting.

## Page geometry

- 3:2 landscape, 1536×1024, quality high.
- 3–4 panels per page, layout stated explicitly every time (e.g. "THREE panels: two equal panels across the TOP, one WIDE panel across the BOTTOM. Reading order: top-left, top-right, wide bottom.").
- "Clean solid-black borders and clear white gutters between all panels." — verbatim in every prompt.

## Lettering conventions (observed on the two validated prototypes)

- **Caption boxes:** cream/ivory rectangular boxes, dark serif-style lettering, corner-anchored or full-width band. State the corner explicitly.
- **Speech bubbles:** white rounded bubbles, dark lettering, tail explicitly described ("tail pointing to the old man in the dock").
- **Ship/signage text** renders reliably when described as a physical object with quoted text ("IMPERIAL LINER 88" on the hull).

## LETTERING RULEBOOK (evolved v1→v4 on the trial prototype — LAW)

1. **Stage speakers left-to-right in speaking order.** First speaker at frame-left, reply speaker at frame-right. This is THE root fix for bubble attribution. Never fix attribution by amputating composition (no rows of static talking heads).
2. Every bubble spatially anchored: position in panel + "tail pointing to <visible description>" — never just "bubble from X".
3. **≤ ~8 words per bubble.** Exchanges longer than 2 beats move to close-up chains. (A signature line may run to ~11 words if it owns its panel.)
4. No quotation marks inside speech bubbles — the bubble IS the quote. Add to lettering block: "DO NOT include any quotation marks inside speech bubbles."
5. Open the text section with `LETTERING — verbatim, render exactly:` and close every prompt with the restrictions block:
   > All words spelled correctly. Do not duplicate text. Do not invent extra captions, extra bubbles, or extra signage. Render ONLY the quoted text. NO modern logos, NO watermarks.
6. Attribution problems are designed out at script level (staging), never chased in QA.

## Palette anchors per act

- **Act 1 Trantor:** deep space blacks + teal-and-bronze metal world + amber interior light shafts (trial hall: dark green-black marble, gold imperial starship emblem, dusty amber god-rays).
- **Act 2 Terminus:** warmer and barer — ochre plains, pale sky, white low colony architecture; interiors in muted slate + amber lamplight. Anacreon/imperial visitors bring saturated maroon-and-gold pomp.
- **Time Vault:** near-dark neutral chamber; the hologram is the light source — pale luminous blue-white with a faint glow halo.
- **Finale:** full '70s cosmic — galaxy spiral in teal/magenta, Terminus a hot amber spark at the rim.

## Non-English / archaic text

None planned. Lord Dorwin's dropped r's appear in exactly ONE bubble ("Empiah") — deliberately, once, and the caption on that page frames his affected speech so it reads as characterization, not a typo.

## Hard ops constraints

- `edit_image` takes ONE `imagePath` — composite plates for 2+ locked characters (see 02-CHARACTERS).
- `thinking=true` broken in this MCP build — standard mode only.
- A "falling body" trips the self-harm output filter — no such beat in this volume, but keep it in mind for spacecraft/crowd scenes.

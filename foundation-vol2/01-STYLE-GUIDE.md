# Style Guide — Foundation: Book Two — The Priests

Inherited verbatim from Vol 1 (`../foundation/01-STYLE-GUIDE.md`). Vol 1's finished pages are the register anchors — when in doubt, look at them, not at prose.

## STYLE BLOCK (paste verbatim into every prompt, first)

> 1970s British science-fiction paperback cover art, smooth airbrushed gradients, hazy atmospheric depth, monumental scale. Saturated teal, magenta, amber and deep space-black palette with glowing horizon light. Chrome and candy-colored machinery with crisp airbrush highlights; soft-edged atmospheric haze behind. Painterly period airbrush rendering — NOT modern digital concept art, NOT cel shading, NOT halftones, NOT ink linework.

## REGISTER / ANTI-DRIFT (paste verbatim, second)

> NOT a children's book. Serious mature science-fiction graphic novel, realistic proportions, cinematic composition, natural dramatic lighting.

## Page geometry

- 3:2 landscape, 1536×1024, quality high.
- 3–4 panels per page, layout stated explicitly every time (e.g. "THREE panels: two equal panels across the TOP, one WIDE panel across the BOTTOM. Reading order: top-left, top-right, wide bottom.").
- "Clean solid-black borders and clear white gutters between all panels." — verbatim in every prompt.

## Lettering conventions

- **Caption boxes:** cream/ivory rectangular boxes, dark serif-style lettering, corner-anchored or full-width band. State the corner explicitly.
- **Speech bubbles:** white rounded bubbles, dark lettering, tail explicitly described ("tail pointing to the heavy man in the green-and-gold uniform").
- **Ship/signage text** renders reliably when described as a physical object with quoted text.

## LETTERING RULEBOOK (v4 — LAW, unchanged from Vol 1)

1. **Stage speakers left-to-right in speaking order.** First speaker at frame-left, reply speaker at frame-right. THE root fix for bubble attribution. Never fix attribution by amputating composition.
2. Every bubble spatially anchored: position in panel + "tail pointing to <visible description>" — never just "bubble from X".
3. **≤ ~8 words per bubble.** Exchanges longer than 2 beats move to close-up chains. (A signature line may run to ~12 words if it owns its panel.)
4. No quotation marks inside speech bubbles — the bubble IS the quote. Add to lettering block: "DO NOT include any quotation marks inside speech bubbles."
5. Open the text section with `LETTERING — verbatim, render exactly:` and close every prompt with the restrictions block:
   > All words spelled correctly. Do not duplicate text. Do not invent extra captions, extra bubbles, or extra signage. Render ONLY the quoted text. NO modern logos, NO watermarks.
6. Attribution problems are designed out at script level (staging), never chased in QA.

## Palette anchors per act

- **Act 1 Terminus (P1–P4, P6):** the Vol 1 Terminus palette matured — ochre plains, pale sky, white architecture now taller and denser; interiors muted slate + amber lamplight. Thirty years of growth visible: more towers, air traffic, green belts.
- **Temple pages (P1 f2, P3 f2):** soaring dim interior, gold vestments, and ONE dominant light source — the reactor-altar's cool atomic blue-white glow (the same blue-white family as Seldon's hologram: the light of science).
- **Anacreon court (P5, P8, P9, P12, P13):** saturated maroon-and-gold pomp (Vol 1's Rodric palette, scaled to a whole kingdom), heavy Viceroy-era architecture, torch-warm interiors.
- **The flagship *Wienis* (P4, P7, P10):** '70s chrome hero hardware — cold steel-teal hull, cathedral-scale bridge; when the curse lands, banks of light die to near-black with single cream emergency accents.
- **Midnight blackout (P11–P13):** city glitter extinguished to deep blue-black; the only warm light is TORCH FIRE (the oldest light) flooding the streets.
- **Time Vault (P15):** near-dark neutral chamber; the hologram is the light source — pale luminous blue-white, faint glow halo (identical to Vol 1 P13–P14).
- **Finale (P16):** full '70s cosmic — the Terminus spark now a radiant amber-gold LAMP at the galaxy's rim, four small cold crowns circling it like moths.

## Non-English / archaic text

None planned. "Interdict" and "temporal/spiritual power" get inline caption glosses on first use (caption-clarity rule), not foreign-text treatment.

## Hard ops constraints

- **Multi-ref `edit_image`:** the wrapper now supports `imagePaths` (1–16 refs) — **but verify the reconnected MCP schema actually exposes `imagePaths` before any production call** (this session initially loaded the stale one-ref schema). If unavailable, fall back to Vol 1's PIL composite plates (method A local stitch).
- `thinking=true` broken in this MCP build — standard mode only.
- **Moderation:** a falling body trips the self-harm filter; Wienis's suicide is NEVER depicted or named — off-page, caption-implied only (see script P13). The blaster shot at Hardin is framed as the beam breaking harmlessly on the shield (no wounds, no casualties anywhere in the volume). The Nyak hunt shows pursuit only — nothing living is shot.

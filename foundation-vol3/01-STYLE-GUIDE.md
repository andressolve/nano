# Style Guide — Foundation: Book Three — The Merchants

Inherited verbatim from Vol 1 (`../foundation/01-STYLE-GUIDE.md`) via Vol 2. Vol 1/Vol 2 finished pages are the register anchors — when in doubt, look at them, not at prose.

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
- **Speech bubbles:** white rounded bubbles, dark lettering, tail explicitly described ("tail pointing to the broad-shouldered man in the copper-brown jacket").
- **Ship/signage text** renders reliably when described as a physical object with quoted text.

## LETTERING RULEBOOK (v4 — LAW, unchanged from Vols 1–2)

1. **Stage speakers left-to-right in speaking order.** First speaker at frame-left, reply speaker at frame-right. THE root fix for bubble attribution. Never fix attribution by amputating composition.
2. Every bubble spatially anchored: position in panel + "tail pointing to <visible description>" — never just "bubble from X".
3. **≤ ~8 words per bubble.** Exchanges longer than 2 beats move to close-up chains. (A signature line may run to ~12 words if it owns its panel.)
4. No quotation marks inside speech bubbles — the bubble IS the quote. Add to lettering block: "DO NOT include any quotation marks inside speech bubbles."
5. Open the text section with `LETTERING — verbatim, render exactly:` and close every prompt with the restrictions block:
   > All words spelled correctly. Do not duplicate text. Do not invent extra captions, extra bubbles, or extra signage. Render ONLY the quoted text. NO modern logos, NO watermarks.
6. Attribution problems are designed out at script level (staging), never chased in QA.

## Palette anchors per act

- **P1 bridge:** Vault near-dark + pale blue-white hologram glow (Vol 2 P15 palette) opening out onto warm amber trade-port light — the volume's handover of light: blue-white (science-as-religion) → amber-gold (trade).
- **Prologue, Askone (P2–P3):** cold ice-world exterior light, austere stone council interiors in slate and bone-white; the transmuter scene lit by the warm impossible glow of new gold — the first strike of the volume's trade-gold.
- **Terminus, 155 F.E. (P4, P10–P13, P15):** Vol 2's Terminus grown into a true trade capital — taller white towers, freight lanes, golden cargo-ship running lights; interiors slate + amber lamplight (Hardin's old office room continuity on P12/P15).
- **Korell (P5–P7, P14):** deliberate drabness — olive, dust-grey, faded brick, weak yellowed daylight; the Commdor's "palace" austere and mean. Against it, Foundation gadgets glow candy-bright (the necklace, the tools) — the only saturated objects in frame. In P14 those glows die one by one and Korell goes cold grey-blue.
- **Siwenna (P8–P9):** dead Imperial grandeur — cold marble colonnades, dusty violet dusk, the huge power plant a dim cathedral of gunmetal with sparse cream indicator lights; Barr's ruined estate in long amber shadows.
- **The war (P13):** deep space; a wall of dark Imperial dreadnoughts with cold magenta running lights vs. small bright Foundation traders withdrawing into the teal.
- **Finale (P16):** full '70s cosmic — the galaxy rim threaded with a WEB of amber-gold trade routes, ship-sparks strung along the lines; the Imperial core dim and reddened far away.

## Non-English / archaic text

None planned. First-use glosses required in caption (caption-clarity rule): *transmuter* (machine that turns one metal into another), *embargo* (a total stop of trade), *Commdor* (Korell's ruler title), *patrician* (nobleman of the old Empire), *dreadnought* (giant battleship).

## Hard ops constraints

- **Multi-ref `edit_image`:** the wrapper supports `imagePaths` (1–16 refs) — **verify the live MCP schema actually exposes `imagePaths` before any production call.** If unavailable, fall back to PIL composite plates (method A local stitch).
- `thinking=true` broken in this MCP build — standard mode only.
- **Moderation:** no violence depicted anywhere. The missionary is escorted out the airlock, mob visible only as distant torchlit crowd through the viewport — his fate stated in caption, never shown. The war shows dreadnoughts looming and traders withdrawing — no ship fired upon or destroyed on-page. No falling bodies. Every multi-ref prompt includes the different-characters-never-merge clause.

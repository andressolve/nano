# Style Guide - Expanded Earthsea Part Two

## Style Block

> Bold ink-line graphic-novel art with clean, confident black linework and flat muted color. Fine etched crosshatching in faces, cloth, wet slate, old stone, carved wood, sea spray, and weather, exactly matching the finished `../earthsea-wizard-part1/pages/` artwork. Serious mythic realism, cinematic staging, realistic heroic proportions. Cold maritime palette: sea-grey, slate blue, fog-white, moss-black green, weathered brown wood, dark wet stone, muted grey wool. Low saturation throughout. Warm gold appears only as candlelight, hearth fire, festival lanterns, werelight, or spell-glow. Rain, wind, spray, moving cloud, and island weather are active parts of outdoor scenes.

## Character and Canon Rules

- Unscarred Ged has unmistakable red-brown copper skin, straight rough black hair, sharp hawk-like features, and no facial scars.
- Scarred Ged retains the same identity and skin tone. Four pale healed claw marks run down the left side of his face from beside the eye to the jaw.
- Vetch has deep black skin, short tightly curled black hair, a broad sturdy build, and an open, warm face.
- Jasper has light-brown skin, fine dark hair, elegant features, a silver cloak clasp, and controlled superior poise.
- Nemmerle is extremely old, thin, and driftwood-white in hair, beard, robe, and staff; his raven is matte black.
- Roke students and masters are ethnically varied Archipelagans. Do not default crowds to pale skin.
- Magic is physical and restrained: silver-white werelight, subtle transformations, changes in air and shadow. No neon effects.
- The shadow is absolute flat matte black: no texture, no reflected light, no glow, no visible face.

## Page Construction

- 3:2 landscape, exactly 1536x1024.
- Usually 3 panels; 4 for intimate exchanges or measured montage.
- Solid black borders and clear off-white gutters.
- Reading order must be unambiguous left-to-right, top-to-bottom.
- Caption boxes use weathered parchment and dark serif text.
- Speech bubbles use off-white fill and dark serif text.
- All lettering is baked into the generated page.
- No page should require zoom at a 1200-pixel display width.

## Lettering Restrictions

Render every supplied line exactly. Spell all words correctly. Do not duplicate, omit, paraphrase, or invent text. No quotation marks inside speech bubbles. No labels, signage, page numbers, watermarks, modern objects, school crests, decorative pseudo-writing, or extra runes unless specified.

## Dialogue Blocking

- Solve attribution before generation. Treat it as character blocking and reading order, not as a tail repair.
- For an A-B exchange, stage A on the left and B on the right whenever possible.
- For A-B-A in one panel, use two tiers: A upper-left, B upper-right, A lower-left.
- Define each balloon by ordinal, speaker, verbatim text, balloon position, speaker position, and tail endpoint.
- State exact balloon counts and explicitly name silent characters.
- Keep mouths visible and leave clear corridors between balloons and faces.
- Use one visible speaker and one balloon per panel when the exchange is high-risk.
- Inspect every page at full resolution for wrong tails, torso-pointing tails, orphan fragments, duplicate balloons, silent-character violations, and canvas drift.
- If attribution fails, regenerate the full page with revised staging. Never crop-patch a tail.

See `../earthsea-wizard-part1/05-SPEECH-ATTRIBUTION-STUDY.md` for the controlled tests and canonical attribution block.

# Style Guide - Expanded Earthsea Pilot

## Style Block

> Bold ink-line graphic-novel art with clean, confident black linework and flat muted color. Fine etched crosshatching in faces, cloth, stone, wet wood, and weather, matching the shipped `../earthsea/pages/` artwork. Serious mythic realism, cinematic staging, realistic heroic proportions. Cold maritime palette: sea-grey, slate blue, fog-white, cold green water, weathered brown wood, blackened iron, dark wet stone. Low saturation throughout. Warm gold appears only as forge fire, hearth fire, candlelight, werelight, or spell-glow. Mist, rain, wind, and mountain weather are active parts of outdoor scenes.

## Character and Canon Rules

- Duny/Ged has unmistakable red-brown copper skin and straight black hair.
- Ogion has dark copper-brown skin, tied-back grey hair, and an utterly still bearing.
- The Kargish raiders alone are pale white-skinned and yellow-haired.
- Young Serret is exceptionally pale with long straight black hair.
- Magic is physical and restrained. No neon fantasy effects.
- The shadow is absolute flat matte black: no texture, no reflected light, no glow.

## Page Construction

- 3:2 landscape, 1536x1024.
- Usually 3 panels; 4 only for intimate exchanges or measured montage.
- Solid black borders and clear off-white gutters.
- Reading order must be unambiguous left-to-right, top-to-bottom.
- Put the speaker on the same side as the bubble whenever possible. Every tail must visibly terminate at the correct mouth.
- Caption boxes use weathered parchment and dark serif text.
- Speech bubbles use off-white fill and dark serif text.
- All lettering is baked into the generated page.
- No page should require zoom at a 1200-pixel display width.

## Lettering Restrictions

Render every supplied line exactly. Spell all words correctly. Do not duplicate, omit, paraphrase, or invent text. No quotation marks inside speech bubbles. No labels, signage, page numbers, watermarks, modern objects, or decorative pseudo-writing unless specified.

## Dialogue Blocking

- Solve attribution before generating the page. Treat it as character blocking and reading order, not as a tail repair.
- For an A-B exchange, stage A on the left and B on the right whenever possible.
- For A-B-A in one panel, use two tiers: A upper-left, B upper-right, A lower-left.
- Define each balloon by ordinal, speaker, verbatim text, balloon position, speaker position, and tail endpoint.
- State the exact balloon count for every speaker and explicitly name silent characters.
- Keep mouths visible and leave a clear corridor between balloon and face. Do not place hands, staffs, animals, or bystanders in that corridor.
- A prompt that says "tail ends at the mouth" can still produce a tail that stops short, hits a torso, or leaves an orphan fragment. Full-resolution visual QA is mandatory.
- Use one speaker per panel when attribution remains high-risk.
- If attribution fails, regenerate the full page with revised staging. Never crop-patch a tail.

See `05-SPEECH-ATTRIBUTION-STUDY.md` for the tests, raw outputs, canonical prompt block, and QA checklist.

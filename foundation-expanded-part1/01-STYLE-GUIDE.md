# Style Guide - Foundation, Part One

## Fixed Style Block

Paste this near the beginning of every image prompt:

> 1970s British science-fiction paperback airbrush graphic novel, smooth painterly gradients and hazy atmospheric depth, monumental scale, saturated teal, magenta, amber and deep space-black palette. Chrome and candy-colored machinery with crisp airbrush highlights; serious realistic human anatomy and expressive natural faces. Period paperback illustration, not modern digital concept art, not cel shading, not halftones, not flat vector art.

## Register and Anti-Drift

> Match the attached shipped Foundation page as the visual-register source: cinematic multi-panel storytelling, clean solid-black panel borders, clear off-white gutters, cream rectangular caption boxes with dark hand-lettered serif text, off-white rounded speech balloons, natural dramatic lighting. Serious science fiction for intelligent young readers, never cute, never mascot-like, never parody.

The actual shipped pixels in `../foundation/pages/page-01.png`, `../foundation/pages/page-05.png`, `../foundation/refs/ref_gaal.png`, and `../foundation/refs/ref_seldon.png` are the source of truth.

## Page Geometry

- Exactly 1536x1024, 3:2 landscape.
- Usually three panels: two across the top and one wide across the bottom, or one wide top and two across the bottom.
- Use four panels only when the progression genuinely needs four distinct beats.
- State panel layout and reading order explicitly.
- Maintain clean solid-black borders and off-white gutters.
- Do not render a production heading, page number, script label, or prompt instruction.

## Lettering

- All text must be baked into the generated page image.
- Captions: cream/ivory rectangular boxes, dark readable serif or hand-lettered text.
- Dialogue: off-white rounded balloons with dark text and short triangular tails.
- Render only the supplied text, verbatim, once each.
- No quotation marks inside speech balloons.
- No empty balloons, empty caption boxes, pseudo-writing, decorative equations posing as dialogue, watermarks, or extra signage.
- Prefer short bubbles. A long idea should own its panel or be divided across panels.
- Preserve capitalization and punctuation from `04-SCRIPT.md`.

Close every page prompt with:

> All words spelled correctly. Do not duplicate, omit, paraphrase, or invent text. Render only the quoted captions and dialogue. No modern logos, no watermarks, no page number, no title heading, no blank balloons, and no decorative pseudo-writing.

## Speech Attribution

Speech attribution is designed through blocking:

1. Stage speakers left-to-right in speaking order whenever possible.
2. Map every balloon by ordinal, speaker, verbatim text, balloon position, character position, and tail endpoint.
3. Keep mouths visible and a clear tail corridor.
4. Name silent characters and give them no balloons.
5. For A-B-A in one panel, use upper-left A, upper-right B, lower-left A.
6. If an exchange remains risky, show one visible speaker and one balloon per panel.
7. Reject wrong speakers, orphan tail fragments, and tails pointing to torsos, hands, props, or empty space.

## Act Palettes

- **View-room and orbit:** deep space-black, chrome silver, navy uniforms, red/blue liner details, amber consoles.
- **Trantor public world:** bronze-teal metal, artificial amber suns, immense enclosed depth, tiny crowds, no visible nature.
- **Streeling University:** ivory architecture, warm daylight, rare real sky; Seldon's office is spare and calm.
- **Psychohistory projection:** teal probability threads and amber system nodes; failure progresses into magenta warning tones and deep black. It must look analytical, not mystical.
- **Commission spaces:** dark green-black marble, scarlet-and-gold authority, severe shafts of amber light.
- **Departure:** cold chrome ships above the still-bright bronze world, with one distant amber point on the galactic rim.

## Projection Rules

The Pages 10-11 projection must remain legible as a model:

- Frame it through Gaal's calculator/projection apparatus.
- Use repeated maps, route lines, fleet icons, food convoys, power grids, and probability numerals.
- A human-scale ruin may appear only inside the declared projected future.
- Do not show Gaal literally transported into the future.
- No magical aura, prophecy eyes, visions emanating from a forehead, or supernatural ghosts.

## Reference Roles

Every generation prompt labels its inputs:

- identity reference;
- environment/object reference;
- finished-page visual-register reference.

Reference sheets are not layouts. Prompts must say to create one new unified scene and not reproduce split-sheet arrangements or labels.

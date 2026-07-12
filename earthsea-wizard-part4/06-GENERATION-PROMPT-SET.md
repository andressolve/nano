# Generation Prompt Set - Part Four

This file records the production prompt system. It is not an alternate script.

## Billing path

Use the built-in Codex image-generation path under the user's ChatGPT/Codex subscription entitlement. Do not use `OPENAI_API_KEY`, the bundled image-generation CLI, or any direct Image API request unless the user explicitly authorizes separate API billing in that conversation.

## Fixed page prompt

> Use case: illustration-story. Asset type: finished Expanded Earthsea graphic-novel page. Create one finished 3:2 landscape graphic-novel page at exactly 1536x1024. Match the attached finished Expanded Earthsea Part Three page exactly: bold confident black ink line, fine etched crosshatching, flat muted maritime and winter color, realistic anatomy, cold sea-grey/slate/wet-wood/frost palette, restrained warm light, solid black panel borders, and clean off-white gutters. Use the exact panel count and generous composition in the supplied page script. Preserve every attached identity exactly, including canonical skin tone, age, clothing, Ged's left-cheek scars, Hoeg's large-rat/tiny-cat scale, Skiorh's peaked hood, and the north ship or Terrenon keep design. Render only the supplied captions and dialogue, verbatim, in weathered parchment caption boxes and off-white serif speech balloons. Bake all lettering into the image. Follow the supplied balloon ordinal, speaker position, balloon position, reading order, and tail endpoint. Every declared silent character must remain silent. No extra text, labels, signs, runes, page numbers, headings, watermarks, duplicate figures, duplicate balloons, orphan tails, modern objects, neon magic, decorative pseudo-writing, or post-generation lettering. The shadow and gebbeth hood interior are absolute flat matte black with no face, eyes, bones, texture, reflected light, smoke detail, or glow.

Append the complete panel-by-panel page block and attribution map from `04-SCRIPT.md` without shortening or paraphrasing it.

## Reference order

1. Attach every identity and environment sheet listed for the page.
2. Attach at least one finished page from `../earthsea-wizard-part3/pages/` as the primary visual-register reference.
3. For Low Torning continuity, prefer the closest finished Part Three page.
4. After prototypes pass, attach the closest approved Part Four page when it materially helps recurring ship, snow, Skiorh, or gate continuity.
5. Never substitute prose descriptions for an available identity or environment sheet.

## Page reference matrix

| Page | Required Part Four refs |
|---|---|
| Cover | `ref_ged_scarred.png`, `ref_skiorh_gebbeth.png`, `ref_terrenon_exterior.png` |
| 1-2 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_pechvarry.png`, `ref_low_torning_people.png` |
| 3-7 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_southern_sailors.png` |
| 8-9 | `ref_ged_scarred.png`, `ref_hoeg.png` |
| 10-12 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_grey_stranger.png`, `ref_southern_sailors.png` |
| 13 | `ref_ged_scarred.png`, `ref_north_ship_crew.png`, `ref_north_ship.png` |
| 14-15 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_north_ship_crew.png`, `ref_north_ship.png`, `ref_osskil_people.png` |
| 16-19 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_north_ship_crew.png`, `ref_north_ship.png` |
| 20 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_north_ship_crew.png`, `ref_osskil_people.png` |
| 21-24 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_north_ship_crew.png`, `ref_terrenon_exterior.png` |
| 25-28 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_skiorh_gebbeth.png`, `ref_terrenon_exterior.png` |
| 29-30 | `ref_ged_scarred.png`, `ref_skiorh_gebbeth.png`, `ref_terrenon_exterior.png` |

## Prototype order

1. Page 6 - the Roke-wind reversal.
2. Page 25 - the empty-hood reveal.
3. Page 29 - the gate chase.

Inspect and approve each before generating the next. A passing prototype becomes the active final page; do not generate disposable alternate art.

## Full-page correction prompt

When QA fails, repeat the complete fixed prompt, page script, attribution map, and reference attachments. Add a short correction block naming the observed failure and required staging change. The replacement must be a newly generated full 1536x1024 page.

Example correction block:

> Correction required: the previous page drew eyes inside the empty hood and made Hoeg cat-sized. Regenerate the entire page. Preserve the script exactly. The hood opening is featureless flat matte black with no eyes, face, bones, smoke, or texture. Hoeg is silent and no larger than a large rat inside Ged's cloak.

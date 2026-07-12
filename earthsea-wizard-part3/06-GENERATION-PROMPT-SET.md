# Generation Prompt Set - Part Three

This file records the production prompt system. It is not an alternate script.

## Billing path

Use the built-in Codex image-generation path under the user's ChatGPT/Codex subscription entitlement. Do not use `OPENAI_API_KEY`, the bundled image-generation CLI, or any direct Image API request unless the user explicitly authorizes separate API billing in that conversation.

## Fixed page prompt

> Create one finished 3:2 landscape graphic-novel page at exactly 1536x1024. Match the attached finished Expanded Earthsea Part Two page exactly: bold confident black ink line, fine etched crosshatching, flat muted maritime color, realistic anatomy, cold sea-grey/slate/salt-grass/wood palette, restrained warm light, solid black panel borders, and clean off-white gutters. Use the exact panel count and generous composition in the supplied page script. Preserve every attached identity exactly, including canonical brown or black skin tone, age, clothing, Ged's left-cheek scars, Hoeg's large-rat/tiny-cat scale, and dragon anatomy and scale. Render only the supplied captions and dialogue, verbatim, in weathered parchment caption boxes and off-white serif speech balloons. Bake all lettering into the image. Follow the supplied balloon ordinal, speaker position, balloon position, reading order, and tail endpoint. Every declared silent character must remain silent. No extra text, labels, signs, runes, page numbers, headings, watermarks, duplicate figures, duplicate balloons, orphan tails, modern objects, neon magic, decorative pseudo-writing, or post-generation lettering. The shadow is absolute flat matte black with no face, eyes, texture, reflected light, smoke detail, or glow.

Append the complete panel-by-panel page block and attribution map from `04-SCRIPT.md` without shortening or paraphrasing it.

## Reference order

1. Attach every identity sheet listed for the page.
2. Attach at least one finished page from `../earthsea-wizard-part2/pages/` as the primary visual-register reference.
3. When Low Torning maritime construction is central, optionally attach a compatible finished page from `../earthsea-wizard-part1/pages/`.
4. After prototypes pass, attach the closest approved Part Three page when it materially helps recurring setting or light continuity.
5. Never substitute prose descriptions for an available identity sheet.

## Page reference matrix

| Page | Required Part Three identity refs |
|---|---|
| Cover | `ref_ged_scarred.png`, `ref_yevaud.png`, `ref_young_dragons.png` |
| 1-2 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_low_torning_people.png` |
| 3 | `ref_ged_scarred.png`, `ref_low_torning_people.png`, `ref_young_dragons.png` |
| 4 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_people.png`, `ref_low_torning_family.png` |
| 5 | `ref_ged_scarred.png`, `ref_pechvarry.png` |
| 6 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_pechvarry.png` |
| 7 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_family.png`, `ref_young_dragons.png` |
| 8 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_pechvarry.png` |
| 9-10 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_family.png` |
| 11 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_family.png` |
| 12-15 | `ref_ged_scarred.png` |
| 16-17 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_family.png` |
| 18 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_low_torning_family.png` |
| 19 | `ref_ged_scarred.png`, `ref_pechvarry.png` |
| 20 | `ref_ged_scarred.png`, `ref_hoeg.png` |
| 21 | `ref_ged_scarred.png`, `ref_hoeg.png`, `ref_young_dragons.png` |
| 22 | `ref_ged_scarred.png`, `ref_low_torning_people.png` |
| 23 | `ref_ged_scarred.png`, `ref_pechvarry.png`, `ref_low_torning_people.png` |
| 24 | `ref_ged_scarred.png`, `ref_yevaud.png` |
| 25-27 | `ref_ged_scarred.png`, `ref_young_dragons.png` |
| 28-32 | `ref_ged_scarred.png`, `ref_yevaud.png` |

## Prototype order

1. Page 15 - Dry Land threshold.
2. Page 27 - dragon change.
3. Page 30 - Yevaud temptation.

Inspect and approve each before generating the next. The prototype is the eventual final page if it passes; do not generate disposable alternate art.

## Full-page correction prompt

When QA fails, repeat the complete fixed prompt, page script, attribution map, and reference attachments. Add a short correction block naming the observed failure and the required staging change. The replacement must be a newly generated full 1536x1024 page.

Example correction block:

> Correction required: the previous page assigned the second balloon to the silent character and drew Hoeg at dog scale. Regenerate the entire page. Preserve the script exactly. The second balloon belongs to Pechvarry on the RIGHT with a short tail ending at his mouth. Hoeg is silent and no larger than a large rat beside Ged's boot.

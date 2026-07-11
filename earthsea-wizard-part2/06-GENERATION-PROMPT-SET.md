# Generation Prompt Set - Part Two

This file records the production prompt system. It is not an alternate script. For any regeneration, combine the relevant page block in `04-SCRIPT.md` with the following fixed prompt and reference rules.

## Fixed page prompt

> Create one finished 3:2 landscape graphic-novel page at exactly 1536x1024. Match the attached finished Part One page exactly: bold confident black ink line, fine etched crosshatching, flat muted maritime color, realistic anatomy, cold sea-grey/slate/moss/wood palette, restrained warm light, solid black panel borders, and clean off-white gutters. Use three or four generous panels exactly as scripted. Preserve the attached character identities exactly, including canonical skin tones, age, clothing, scar side, and animal scale. Render only the supplied captions and dialogue, verbatim, in weathered parchment caption boxes and off-white serif speech balloons. Bake all lettering into the image. Follow the supplied balloon ordinal, speaker position, balloon position, reading order, and tail endpoint. Every declared silent character must remain silent. No extra text, labels, signs, runes, page numbers, headings, watermarks, duplicate figures, duplicate balloons, orphan tails, modern objects, neon magic, or decorative pseudo-writing. The shadow is absolute flat matte black with no face, texture, reflected light, or glow.

Append the complete panel-by-panel page block and attribution map from `04-SCRIPT.md` without shortening or paraphrasing it.

## Reference order

1. Attach every identity sheet listed for the page below.
2. Attach at least one finished page from `../earthsea-wizard-part1/pages/` as the visual-register reference.
3. After the prototype gate, attach the closest approved Part Two page when it materially helps a recurring location or exchange.
4. Never substitute prose descriptions for an available identity sheet.

## Page reference matrix

| Page | Required Part Two identity refs |
|---|---|
| Cover | `ref_ged_roke.png`, `ref_jasper.png`, `ref_roke_masters.png` |
| 1-4 | `ref_ged_roke.png` |
| 5-6 | `ref_ged_roke.png`, `ref_roke_masters.png` |
| 7-8 | `ref_ged_roke.png`, `ref_nemmerle.png` |
| 9-12 | `ref_ged_roke.png`, `ref_vetch.png`, `ref_jasper.png` |
| 13-14 | `ref_ged_roke.png`, `ref_roke_masters.png` |
| 15-16 | `ref_ged_roke.png`, `ref_roke_masters.png` |
| 17 | `ref_ged_roke.png`, `ref_hoeg.png` |
| 18-20 | `ref_ged_roke.png`, `ref_vetch.png`, `ref_jasper.png`, `ref_hoeg.png` |
| 21 | `ref_ged_roke.png`, `ref_roke_masters.png` |
| 22-25 | `ref_ged_roke.png`, `ref_vetch.png`, `ref_jasper.png`, `ref_hoeg.png` where visible |
| 26 | `ref_ged_roke.png`, `ref_vetch.png`, `ref_jasper.png`, `ref_nemmerle.png` |
| 27 | `ref_ged_scarred.png`, `ref_vetch.png`, `ref_nemmerle.png` |
| 28 | `ref_ged_scarred.png`, `ref_roke_masters.png` |
| 29 | `ref_ged_scarred.png`, `ref_vetch.png` |
| 30 | `ref_ged_scarred.png`, `ref_roke_masters.png` |

## Full-page correction prompt

When QA fails, repeat the complete fixed prompt, page script, attribution map, and reference attachments. Add a short correction block that names the observed failure and the required staging change. Do not ask for an edit to a crop or a local patch. The replacement must be a newly generated full 1536x1024 page.

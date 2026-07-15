# Generation Prompt Set - Foundation, Part One

This file records the fixed production prompt and reference matrix. It does not replace `04-SCRIPT.md`.

## Fixed Page Prompt

> Use case: illustration-story. Create one finished 3:2 landscape graphic-novel page at exactly 1536x1024. Match the attached shipped Foundation page as the visual-register source: 1970s British science-fiction paperback airbrush, smooth painterly gradients, hazy atmospheric depth, monumental scale, saturated teal, magenta, amber and deep space-black, chrome machinery, serious realistic anatomy and natural expressive faces. Use the scripted panel layout exactly, with clean solid-black borders and clear off-white gutters. Preserve every attached recurring identity exactly, including face, age, skin tone, hair, costume, and body build. Render only the supplied captions and dialogue, verbatim, in cream rectangular caption boxes and off-white rounded speech balloons with dark readable hand-lettered serif text. Bake all lettering into the image. Follow every balloon ordinal, speaker position, balloon position, reading order, and tail endpoint. Every declared silent character must remain silent. No extra text, empty balloons, pseudo-writing, page numbers, headings, watermarks, duplicated figures, duplicated balloons, orphan tails, modern objects, Apple-series characters or technology, or supernatural presentation of psychohistory.

Append the complete page block and balloon map from `04-SCRIPT.md` without shortening or paraphrasing it.

Close with the lettering restriction block from `01-STYLE-GUIDE.md`.

## Reference Semantics

Label every input in the prompt:

- `Image N: identity reference`;
- `Image N: environment/object reference`;
- `Image N: finished-page visual-register reference`.

State:

> Reference sheets are identity and design sources, not layouts. Paint one new unified page using their locked features. Do not reproduce any split-sheet arrangement or labels.

## Production Reference Files

### Existing refs copied from shipped edition

- `refs/ref_gaal.png`
- `refs/ref_seldon.png`

### New identity refs

- `refs/ref_jerril.png`
- `refs/ref_advocate.png`
- `refs/ref_linge_chen.png`
- `refs/ref_commissioners.png`
- `refs/ref_commission_guards.png`

### New environment and object refs

- `refs/ref_trantor_city.png`
- `refs/ref_seldon_office.png`
- `refs/ref_psychohistory_projection.png`
- `refs/ref_commission_spaces.png`
- `refs/ref_departure.png`

### Register references

- `../foundation/pages/page-01.png`
- `../foundation/pages/page-05.png`
- after prototype approval, the nearest accepted Part One prototype or finished page.

## Page Reference Matrix

| Page | Required identity refs | Required environment/object refs | Register anchor |
| --- | --- | --- | --- |
| Cover | Gaal, Seldon | Trantor city, projection, departure | shipped P1 |
| 1 | Gaal | departure/liner cues | shipped P1 |
| 2 | Gaal, Jerril | Trantor city | shipped P1 |
| 3 | Gaal | Trantor city | shipped P1 |
| 4-5 | Gaal, Jerril | Trantor city | shipped P1 |
| 6 | Gaal, Seldon | Seldon office for register cues only; script controls hotel | shipped P5 |
| 7-9 | Gaal, Seldon | Seldon office, projection | shipped P5 |
| 10-11 | none required when humans are partial only | Trantor city, projection | shipped P1 |
| 12 | Gaal, Seldon | Seldon office, projection | shipped P5 |
| 13 | Gaal, Seldon, Guards | Commission spaces | shipped P5 |
| 14 | Gaal, Advocate | Commission spaces | shipped P5 |
| 15 | Gaal, Seldon | Commission spaces | shipped P5 |
| 16 | Gaal, Seldon, Advocate, Commissioners | trial hall from shipped P5 | shipped P5 |
| 17 | reused finished shipped page | none | shipped P5 itself |
| 18 | Seldon, Advocate, Commissioners | trial hall from shipped P5 | shipped P5 |
| 19 | Gaal, Seldon, Advocate, Commissioners | projection, trial hall | shipped P5 |
| 20 | Gaal, Seldon, Linge Chen, Commissioners | Commission spaces/trial hall | shipped P5 |
| 21-22 | Gaal, Seldon, Linge Chen, Commissioners | Commission spaces, projection on P22 | shipped P5 |
| 23 | Gaal, Seldon, Guards | Seldon office, departure | shipped P5 |
| 24 | Gaal, Seldon | Seldon office, projection, departure | shipped P1 |

## Prototype Prompts

Use the fixed page prompt and exact script blocks for:

1. Page 1 - cinematic hook, scale, and A-B-A attribution.
2. Page 11 - analytical destruction projection.
3. Page 18 - trial logic with six exact balloons.

No other page generation begins until the three outputs pass `05-PRODUCTION-QA.md` together.

## Full-Page Correction Prompt

When QA fails, repeat the fixed prompt, complete page script, balloon map, and all references. Add one short correction block naming the observed failure and the required staging change. The replacement must be a complete new 1536x1024 page. Never request a crop edit, tail patch, text swap, or HTML/SVG repair.

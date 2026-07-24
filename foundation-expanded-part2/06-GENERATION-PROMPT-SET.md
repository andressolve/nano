# Generation Prompt Set - Foundation, Part Two

This file records the fixed reference/page prompts and attachment matrix. It
does not replace the exact locks in `02-CHARACTERS.md`, `03-SETTINGS.md`, or the
verbatim lettering and blocking in `04-SCRIPT.md`.

## Production Path

Use the built-in subscription-backed Codex image-generation tool only. Generate
one final asset per tool call. Do not use the imagegen CLI, `OPENAI_API_KEY`, or
another directly billed API route.

All accepted project assets must be copied from the built-in generation output
location into this folder. Never leave a project-referenced final only under a
Codex-generated-images directory.

## Fixed Reference Prompt

> Use case: illustration-story. Create one production reference image at exactly 1536x1024, 3:2 landscape. Match the attached finished Foundation Part One page as the visual-register source: serious cinematic mid-century science-fiction graphic-novel realism descended from 1970s British SF paperback airbrush, controlled dark inked contours, smooth painterly airbrush and cel-shaded color, atmospheric depth, realistic anatomy, and natural expressive faces. Render the exact character, group, environment, or object lock supplied below. This is a design reference, not a story page. Neutral uncluttered presentation, no story panels unless the supplied group/environment specification requires separated views. No captions, speech balloons, labels, names, pseudo-writing, page numbers, title, watermark, duplicated figure, modern logo, or Apple-series design.

Append the complete relevant lock from `02-CHARACTERS.md` or
`03-SETTINGS.md`. For character refs, require a large portrait plus a full-body
standing view on a warm neutral background. For group refs, require distinct
non-cloned faces and silhouettes. For environment/object refs, require one
unified wide design plate or the explicitly declared comparison states.

## Seldon Recording Composition Prompt

Load `../foundation-expanded-part1/refs/ref_seldon.png` as the exact identity
source and `../foundation/refs/ref_seldon_hologram.png` as the seated
apparatus/projection source. This two-source composition was the successful
subscription-backed generation path after direct identity-edit phrasing caused
a moderation false positive.

> Create a new 1536x1024 production reference for Hari Seldon's timed Vault recording. Image 1 is the exact expanded Part One face, age, hair, skin tone, lined features, gentle expression, and pale-grey scholar's robe; preserve that identity exactly. Image 2 supplies only the seated chair, closed book, and mechanical-projection presentation. Compose one complete seated figure in the practical powered chair, with the closed undecorated book on his lap, rendered as a crisp translucent pale blue-white projection against a near-black neutral background. No halo, magic, standing duplicate, text, labels, Apple Vault, null field, or floating polyhedron.

## Fixed Page Prompt

> Use case: illustration-story. Create one finished 3:2 landscape graphic-novel page at exactly 1536x1024. Match the attached finished Foundation Part One page as the visual-register source: serious cinematic mid-century science-fiction graphic-novel realism descended from 1970s British SF paperback airbrush, controlled dark inked contours, smooth painterly airbrush and cel-shaded color, hazy atmospheric depth, monumental but readable environments, realistic anatomy, and natural expressive faces. Use the scripted panel layout exactly, with clean solid-black borders and clear off-white gutters. Preserve every attached recurring identity exactly, including face, age, skin tone, hair, costume, and body build. Render only the supplied captions and dialogue, verbatim, in cream rectangular caption boxes and off-white rounded speech balloons with dark readable hand-lettered serif text. Bake all lettering into the raster. Follow every balloon ordinal, speaker position, balloon position, reading order, and tail endpoint. Every declared silent character must remain silent. No extra text, empty balloons, pseudo-writing, page numbers, headings, watermarks, duplicated figures, duplicated balloons, orphan tails, modern objects, Apple-series characters or technology, or supernatural psychohistory/Vault effects.

Append the complete page block and balloon map from `04-SCRIPT.md` without
shortening, summarizing, or paraphrasing it. Append any page-specific ref roles
and anti-drift notes from the matrix below. Close with the lettering restriction
block from `01-STYLE-GUIDE.md`.

## Reference Semantics

Label every attached image explicitly in each prompt:

- `Image N: identity reference`;
- `Image N: group identity reference`;
- `Image N: environment/object reference`;
- `Image N: finished-page visual-register reference`.

State:

> Reference sheets define identity and design, not layout. Paint one new unified page using their locked features. Do not reproduce a portrait/full-body split, comparison plate, label zone, or source-page composition.

The built-in generator accepts at most five image attachments. When a page's
matrix names more than five refs, attach the composite group sheet instead of
its constituent solo refs, then prioritize the setting/object lock and nearest
accepted page register. Preserve every omitted solo identity through the group
lock and repeat its written design constraints in the prompt.

## Production Reference Files

### Identity and group refs

- `refs/ref_hardin.png`
- `refs/ref_pirenne.png`
- `refs/ref_rodric.png`
- `refs/ref_dorwin.png`
- `refs/ref_fara.png`
- `refs/ref_yohan_lee.png`
- `refs/ref_seldon_recording.png`
- `refs/ref_board.png`
- `refs/ref_civic_wardens.png`
- `refs/ref_anacreon_group.png`
- `refs/ref_three_kingdom_envoys.png`

### Environment and object refs

- `refs/ref_terminus_city.png`
- `refs/ref_encyclopedia_building.png`
- `refs/ref_four_kingdoms_model.png`
- `refs/ref_anacreon_arrival.png`
- `refs/ref_atomic_contrast.png`
- `refs/ref_board_and_city_hall.png`
- `refs/ref_dorwin_and_logic_room.png`
- `refs/ref_anacreon_base.png`
- `refs/ref_time_vault.png`

### Finished-page register refs

- `../foundation-expanded-part1/pages/page-24.png` - series transition and
  frontier departure continuity;
- `../foundation-expanded-part1/pages/page-06.png` - two-person dialogue;
- `../foundation-expanded-part1/pages/page-11.png` - analytical system;
- `../foundation-expanded-part1/pages/page-18.png` - political dialogue;
- after prototype approval, the nearest accepted Part Two prototype or final.

## Page Reference Matrix

| Page | Required identity/group refs | Required environment/object refs | Register anchor |
| --- | --- | --- | --- |
| Cover | Hardin, Pirenne, Seldon recording | Terminus city, Four Kingdoms model | Part One P24 |
| 1 | Hardin, Lee | Terminus city | Part One P24 |
| 2 | Hardin, Lee | freight cues from Terminus city, Board/City Hall | Part One P6 |
| 3 | Hardin, Pirenne | Encyclopedia Building, Four Kingdoms model | Part One P12 |
| 4 | Hardin, Pirenne | Encyclopedia Building | Part One P18 |
| 5 | Hardin, Rodric, Anacreon group | Anacreon arrival, Terminus city | Part One P1 |
| 6 | Hardin, Pirenne, Rodric | Encyclopedia Building | Part One P19 |
| 7 | Hardin, Pirenne, Rodric, Board | Anacreon arrival/state-dinner cues | Part One P18 |
| 8 | Hardin, Pirenne, Rodric | Anacreon arrival/state-dinner cues, Terminus city | Part One P18 |
| 9 | Hardin, Pirenne, Rodric | Atomic contrast, state-dinner cues | Part One P12 |
| 10 | Hardin, Pirenne | Atomic contrast, Four Kingdoms model | Part One P11 |
| 11 | Hardin, Lee, Pirenne, Board | Board/City Hall | Part One P6 |
| 12 | Hardin, Pirenne, Fara, Board | Board/City Hall, Four Kingdoms model | Part One P18 |
| 13 | Hardin, Pirenne, Dorwin | Dorwin/logic room, Anacreon arrival for ship contrast | Part One P1 |
| 14 | Hardin, Dorwin | Dorwin/logic room | Part One P7 |
| 15 | Hardin, Dorwin | Atomic contrast, Dorwin/logic room | Part One P11 |
| 16 | Hardin, Lee | Dorwin/logic room, Four Kingdoms model | Part One P11 |
| 17 | Hardin, Lee, Rodric, Board, Anacreon group | Board/City Hall, Four Kingdoms model, Anacreon base | Part One P18 |
| 18 | Hardin, Pirenne, Fara, Board | Board/City Hall, Four Kingdoms model | Part One P18 |
| 19 | Hardin, Pirenne, Fara, Board | Board/City Hall, Four Kingdoms model | Part One P8 |
| 20 | Hardin, Lee | Board/City Hall, Four Kingdoms model | Part One P12 |
| 21 | Hardin, Lee, civic wardens | Board/City Hall | Part One P23 |
| 22 | Hardin, Lee, Board, civic wardens, Anacreon group | Board/City Hall, Anacreon base, Time Vault entrance | Part One P24 |
| 23 | Hardin, Pirenne, Fara, Board, Seldon recording | Time Vault | Part One P18 |
| 24 | Hardin, Pirenne, Board, Seldon recording | Time Vault, Terminus city | Part One P24 |
| 25 | Seldon recording | Time Vault, Four Kingdoms model | Part One P11 |
| 26 | Hardin, Pirenne, Fara, Lee, Board, Seldon recording | Time Vault, Four Kingdoms model | Part One P18 |
| 27 | Hardin, Lee, three kingdom envoys | Four Kingdoms model, Board/City Hall | Part One P11 |
| 28 | Hardin, Lee, Pirenne, Anacreon group, three kingdom envoys | Terminus city, Anacreon base, atomic contrast, Four Kingdoms model | Part One P24 |

The freight port and state-dinner spaces are sub-designs within their declared
environment plates; do not invent separate refs unless prototype/full-page QA
shows that those rooms drift.

## Prototype Prompts

Use the fixed page prompt and exact complete script blocks for:

1. Page 1 - fifty-year settlement reveal, generation handoff, and new viewpoint.
2. Page 12 - three-panel Board exchange with six exact balloons.
3. Page 23 - Time Vault geography, Seldon identity, and recording ownership.

No other page generation begins until the three outputs pass
`05-PRODUCTION-QA.md` together.

## Full-Page Correction Prompt

When QA fails, repeat the fixed prompt, complete page script, balloon map, and
all original references. Add one concise correction block:

> Observed failure: [state only the concrete failure]. Required correction: [state the single staging, density, identity, text, or composition change]. Preserve every other scripted and visual invariant. Generate a complete new 1536x1024 page; do not edit, crop, patch, or overlay the previous page.

Reinspect the entire replacement. A corrected detail does not excuse a new
error elsewhere.

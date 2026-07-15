# Production QA - Foundation, Part One

## Status

**Production complete and browser-verified, 2026-07-13.**

The deliverable is a cover, 24 finished story pages, a responsive reader, an afterword, a spoiler-light Book/Screen note, a five-question causal-comprehension quiz, and root-catalog integration.

## Final Inventory

- [x] Cover and Pages 1-24 in `pages/`.
- [x] Every cover/final page is exactly 1536x1024.
- [x] Gaal and Seldon production refs copied locally.
- [x] Jerril, Advocate, Linge Chen, five Commissioners, and Commission Guards locked refs.
- [x] Trantor, Seldon office, psychohistory projection, Commission spaces, and departure refs.
- [x] Accepted hard-page prototypes for Pages 1, 11, and 18 under `research/prototypes/`.
- [x] Responsive reader with zoom, route strip, afterword, Book/Screen note, and five-question WHY-quiz.
- [x] Root catalog entry added; earlier compressed `foundation/` entry retained on disk and marked superseded.
- [x] No HTML, SVG, or post-production lettering on story pages.

## Generation Path

All new raster production used the built-in subscription-backed Codex image-generation path. No `OPENAI_API_KEY`, bundled imagegen CLI, or separately billed direct API path was used.

## Reference Gate

All twelve production refs passed full-resolution inspection:

1. Exact 1536x1024 canvas.
2. Visual register compatible with the shipped Foundation pages.
3. Face, age, skin tone, hair, and costume consistent with `02-CHARACTERS.md`.
4. Recurring identities legible across later page generations.
5. Group sheets contain distinct recurring faces and costumes.
6. No contaminating labels or pseudo-writing.
7. Environment/object sheets establish reusable geometry.

Locked refs:

- `refs/ref_gaal.png`
- `refs/ref_seldon.png`
- `refs/ref_jerril.png`
- `refs/ref_advocate.png`
- `refs/ref_linge_chen.png`
- `refs/ref_commissioners.png`
- `refs/ref_commission_guards.png`
- `refs/ref_trantor_city.png`
- `refs/ref_seldon_office.png`
- `refs/ref_psychohistory_projection.png`
- `refs/ref_commission_spaces.png`
- `refs/ref_departure.png`

## Prototype Gate

### Page 1 - Cinematic hook

- [x] Trantor's scale is promised before it appears.
- [x] The view-room and dangerous sunward approach read clearly.
- [x] Officer/Gaal/officer exchange has correct attribution.
- [x] All four text blocks render exactly once.
- [x] Canvas is 1536x1024.

### Page 11 - Technical projection

- [x] Projection is visibly produced by the calculator.
- [x] Route failure, blackout, unheeded orders, and future ruin read sequentially.
- [x] Ruin is mathematical probability, not supernatural vision or present event.
- [x] No Star Bridge, bombs, gore, or Apple-series imagery.
- [x] All five captions render exactly once.
- [x] Canvas is 1536x1024.

### Page 18 - Trial logic

- [x] Advocate remains left and Seldon right in all three panels.
- [x] Exactly six balloons, two per panel.
- [x] Every tail reaches the correct speaker.
- [x] Commissioners and Gaal stay silent.
- [x] Trial hall matches the shipped Foundation register.
- [x] Canvas is 1536x1024.

The three prototypes passed as a set before the full run began. Their accepted images were copied into the final `pages/` directory.

## Full-Page QA

The cover and all 24 final pages were inspected during generation and in reading order against `04-SCRIPT.md` for:

- [x] panel number, shape, and order;
- [x] exact story text, punctuation, spelling, and capitalization;
- [x] no invented, omitted, duplicate, or paraphrased text;
- [x] intended balloon count and speaker;
- [x] reading order, staging, and tail endpoint;
- [x] silent-character discipline;
- [x] no blank balloons or orphan tails;
- [x] recurring character and costume continuity;
- [x] stable environment and analytical-projection language;
- [x] no Apple-only story object, character, or event;
- [x] no production heading, prompt fragment, watermark, or fake label;
- [x] exact 1536x1024 dimensions.

Page 17 deliberately reuses the already accepted shipped trial image from `../foundation/pages/page-05.png`, as specified in the script.

## Accepted Full-Page Regenerations

All corrections were full-page regenerations; no crop patch, lettering overlay, or tail repair was used.

| Page | Retained draft | Failure found | Final correction |
| --- | --- | --- | --- |
| 3 | `pages/page-03-v1.png` | Driver's left-side reply read visually before Gaal's right-side question. | Regenerated with the questions at the highest tier and replies clearly lower. |
| 4 | `pages/page-04-v1.png` | The anonymous attendant inherited Jerril's face and coat, weakening his later entrance. | Regenerated with a distinct older woman in a silver-gray facility uniform; Jerril appears only in Panel 3. |

All other cover/page generations passed their first full-page inspection.

## Narrative Pass

- [x] Gaal's question or desire carries every major scene.
- [x] Places and scene changes are visually oriented for a young reader.
- [x] Abstract claims receive a visible system or consequence.
- [x] Psychohistory remains probabilistic and population-scale.
- [x] Page 11 delivers visible destruction as a calculator-generated future projection.
- [x] The trial develops as a contest of evidence, legitimacy, and political risk.
- [x] Chen's sentence is clearly the outcome Seldon prepared to exploit.
- [x] Page 24 completes Gaal's understanding while opening the thousand-year story.
- [x] Intact Trantor at the end answers the central theme: early action matters before damage makes belief easy.

## Reader QA

Browser checks ran against a local HTTP server in the Codex in-app browser on 2026-07-13.

- [x] Cover, Pages 1-24, afterword, Book/Screen note, and quiz are reachable.
- [x] Every page loaded as a 1536x1024 image during a complete sequential browser walk.
- [x] Previous/next navigation, page counter, progress bar, and disabled end states work.
- [x] Keyboard bindings are present for left/right navigation and Escape-to-close zoom.
- [x] Active route moves through Liner, Spaceport, Surface, Luxor, Streeling, Commission, and Departure.
- [x] Click zoom opens with the current image, locks body scroll, and closes cleanly.
- [x] Mobile viewport 390x844 has no body-level horizontal overflow.
- [x] Mobile route bar fits inside the viewport.
- [x] Mobile navigation buttons do not overlap the centered page counter after correction.
- [x] Book/Screen comparison cards collapse to one column at the mobile breakpoint.
- [x] All five quiz answers lock, show causal feedback, and score `5 of 5`.
- [x] No browser console errors were reported during reader and catalog testing.
- [x] Root homepage shows the expanded volume as the newest story with the correct cover/link.
- [x] Archive shows one expanded-volume link and zero links to the superseded compressed Book One.

## Catalog Decision

`stories.js` now contains:

- active slug: `foundation-expanded-part1`;
- title: *Foundation — Part One: The Man Who Saw the End*;
- publication date: `2026-07-13`;
- earlier `foundation` entry marked `status: "superseded"` with `replacedBy: "foundation-expanded-part1"`.

No shipped Foundation folder or page was deleted or overwritten.

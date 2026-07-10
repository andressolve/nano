# Handoff - Expanded Earthsea Part One Pilot

## Status

**Pilot complete, 2026-07-09.** Cover, 24 finished pages, six character/family refs, expanded script, responsive reader, zoom view, and five-question comprehension check are all present. The shipped `../earthsea/` project remains unchanged.

Open the local reader at `http://127.0.0.1:8765/earthsea-wizard-part1/` while the workspace server is running.

## Production Path

- All new raster art was generated with the built-in Codex image-generation path under the user's subscription entitlement.
- No `OPENAI_API_KEY`, imagegen CLI, or direct API billing was used.
- Native multi-reference prompts attached the relevant identity refs plus an approved finished page as the visual-register reference.
- All lettering is baked into the page images.

## Speech Attribution Study

- `05-SPEECH-ATTRIBUTION-STUDY.md` records four GPT Image 2 prompt tests with their raw outputs under `research/speech-attribution/`.
- Explicit balloon geometry improves attribution but does not make tail endpoints deterministic; a repeated prompt produced a torso-pointing tail and an orphan tail fragment.
- The production rule is to make speaker identity clear through character placement and reading order first, then use tails as confirmation.
- For difficult dialogue, one speaker per panel is the most reliable fallback.
- Full-resolution QA must check attribution, orphan fragments, exact balloon counts, silent characters, and the 1536x1024 canvas.

## Accepted Full-Page Regenerations

- Page 2: restaged the final-panel exchange so the aunt's question, Duny's reply, and the aunt's follow-up read unambiguously in that order; all tails now identify the intended speaker.
- Pages 6 and 7: removed the aunt after page 5 established that she fled.
- Page 11: restaged panel 4 in left-to-right speaking order so the father's line points to the father and Ogion's reply points to Ogion; Duny remains silent.
- Page 12: removed an accidentally rendered production heading.
- Page 15: replaced an incorrect image of humans riding giant birds with an unambiguous imagined pair of hawks.
- Page 16: restored Ogion's omitted line about the seed being alive.
- Page 22: removed an invented explanatory caption.
- Page 24: separated the harbourmaster from Ogion, removed duplicate figures, and aligned the farewell's speaker placement with left-to-right reading order.

No crop patches or local composite repairs were used.

## Reader QA

- All 25 PNGs exist: cover + pages 1-24.
- Every finished page is 1536x1024.
- Desktop reader checked at the default in-app browser viewport.
- Mobile reader checked at 390x844 with no body-level horizontal overflow.
- Tap-to-zoom opens a pannable image at roughly 3x mobile viewport width.
- Previous/next navigation reaches all 24 pages, afterword, and quiz.
- Active location strip changes across Ten Alders, the road, Re Albi, and Great Port.
- Quiz answer locking and feedback were exercised successfully.
- Browser console reported no errors or warnings.

## Non-Negotiables

- Preserve the shipped visual style.
- Use the built-in Codex image-generation path, not API-key or CLI billing.
- Bake all lettering into each page image.
- Attach the listed character refs to every page.
- Inspect pages in reading order, not as isolated illustrations.
- Regenerate a full page when lettering, identity, staging, or reading order fails. Do not crop-patch.

## Narrative QA

After each batch, ask:

1. Can a reader identify every recurring speaker without outside notes?
2. Is the location and time transition clear?
3. Does the page show the event, or merely report that it happened?
4. Does the emotional reaction survive into the next page?
5. Is every bubble unambiguously attached and read in order?

## Approval Gate

User approved the expanded pilot on 2026-07-09. It replaces the compressed `../earthsea/` edition in the root collection index. Do not begin Part Two until its scope and source coverage are chosen explicitly.

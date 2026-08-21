# Page 32 — Frame A builder packet

## Assignment

Create exactly one fresh canonical production candidate from `qa/production/page-32/frames/frame-a-prompt.md`. This is an owner-authorized component round, not a prototype and not permission for a second candidate.

Use only subscription-backed built-in in-app image generation. Do not use `OPENAI_API_KEY`, the imagegen CLI, a direct API, or separately billed generation. Generation inputs are limited to:

1. `refs/approved/19-set-chamber.png` — architecture/material reference.
2. `pages/page-31.png` — canonical hall, daylight, palette, crowd, and finish continuity.

Do not open, attach, edit, crop, imitate, or otherwise use any rejected Page 32 candidate or proof as a generation input. Do not use any additional reference.

## Exact outputs

- Fresh candidate: `qa/production/page-32/frames/candidates/frame-a-v1.png`
- Builder audit: `qa/production/page-32/frames/audits/frame-a-v1.md`
- Assembled-scale proof: `qa/production/page-32/frames/proofs/frame-a-v1-600x263.png`
- Larger proof: `qa/production/page-32/frames/proofs/frame-a-v1-768x336.png`
- Independent critic report target: `qa/production/page-32/frames/critic-frame-a-v1.md`
- If approved, byte-for-byte promotion target: `qa/production/page-32/frames/approved/frame-a.png`

Save the built-in result from its subscription-backed generated-images location to the fresh candidate path. The candidate must be a flattened RGB PNG at exactly 1024 × 448. Wrong canvas/aspect ratio, corrupt or truncated output, or gross anatomical breakage is failed generation; stop and report it rather than silently repairing or creating another candidate.

Derive the two proofs from the untouched candidate by whole-image scaling only. Do not crop, repaint, patch, extend, selectively recolor, add/remove figures, alter gaze, or add text.

## Audit and handoff

Record one compact practical audit covering: canvas/mode; zero strings; crowd only; unanimous literal screen-right eye/nose/chin vector including the right edge; absence of door and focal figure; Page 31 hall/palette/medium continuity; anatomy/integrity; proof paths. The audit is a report, never a gate. Except for the narrow failed-generation conditions above, submit the candidate to the independent critic regardless of audit findings. Do not regenerate before the verdict.

The critic alone returns `APPROVED` or `REVISE`. Do not promote or assemble before approval. Promotion must copy the approved candidate byte-for-byte.

Assembly warning: code may only place, uniformly scale if required, and flatten approved panel rasters. It may never crop for reframing, paint, patch, heal, extend, add/remove objects or figures, change gaze, or add lettering.

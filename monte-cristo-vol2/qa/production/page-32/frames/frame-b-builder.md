# Page 32 — Frame B builder packet

## Assignment

Create exactly one fresh canonical production candidate from `qa/production/page-32/frames/frame-b-prompt.md`. This is an owner-authorized component round, not a prototype and not permission for a second candidate.

Use only subscription-backed built-in in-app image generation. Do not use `OPENAI_API_KEY`, the imagegen CLI, a direct API, or separately billed generation. Generation inputs are limited to:

1. `refs/approved/05-haydee.png` — Haydée identity/costume reference.
2. `refs/approved/03-fernand-1838.png` — Fernand identity/silhouette reference.
3. `refs/approved/19-set-chamber.png` — architecture/material reference.
4. `refs/approved/21-objects.png` — folded document/red wax seal reference.
5. `pages/page-31.png` — canonical hall, daylight, palette, bar, and finish continuity.

Do not open, attach, edit, crop, imitate, or otherwise use any rejected Page 32 candidate or proof as a generation input. Do not use any additional reference.

## Exact outputs

- Fresh candidate: `qa/production/page-32/frames/candidates/frame-b-v1.png`
- Builder audit: `qa/production/page-32/frames/audits/frame-b-v1.md`
- Assembled-scale proof: `qa/production/page-32/frames/proofs/frame-b-v1-600x628.png`
- Larger proof: `qa/production/page-32/frames/proofs/frame-b-v1-768x804.png`
- Independent critic report target: `qa/production/page-32/frames/critic-frame-b-v1.md`
- If approved, byte-for-byte promotion target: `qa/production/page-32/frames/approved/frame-b.png`

Save the built-in result from its subscription-backed generated-images location to the fresh candidate path. The candidate must be a flattened RGB PNG at exactly 1024 × 1072. Wrong canvas/aspect ratio, corrupt or truncated output, or gross anatomical breakage is failed generation; stop and report it rather than silently repairing or creating another candidate.

Derive the two proofs from the untouched candidate by whole-image scaling only. Do not crop, repaint, patch, extend, selectively recolor, add/remove figures or objects, enlarge Haydée/document/seal, alter architecture, or add text.

## Audit and handoff

Record one compact practical audit covering: canvas/mode; zero strings; exact two-human count; one remote small full-figure Haydée enclosed by the complete doorway; one tiny far-end bar-occluded Fernand; no other human vertical or Count-like black figure; document/isolated red seal readability at the 600 × 628 proof without enlarged Haydée; Page 31 hall/palette/medium continuity; anatomy/integrity; proof paths. The audit is a report, never a gate. Except for the narrow failed-generation conditions above, submit the candidate to the independent critic regardless of audit findings. Do not regenerate before the verdict.

The critic alone returns `APPROVED` or `REVISE`. Do not promote or assemble before approval. Promotion must copy the approved candidate byte-for-byte.

Assembly warning: code may only place, uniformly scale if required, and flatten approved panel rasters. It may never crop for reframing, paint, patch, heal, extend, add/remove objects or figures, enlarge the seal or Haydée, alter architecture, or add lettering.

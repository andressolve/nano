# Page 32 — Frame B square-safe builder packet

## Assignment and isolation

Create exactly one fresh canonical square production candidate from `qa/production/page-32/frames/frame-b-square-prompt.md`. This is an owner-authorized component round, not a prototype and not permission for an additional candidate.

Use only subscription-backed built-in in-app image generation. Do not use `OPENAI_API_KEY`, the imagegen CLI, a direct API, or separately billed generation. Generation inputs are limited to:

1. `refs/approved/05-haydee.png`
2. `refs/approved/03-fernand-1838.png`
3. `refs/approved/19-set-chamber.png`
4. `refs/approved/21-objects.png`
5. `pages/page-31.png`

Do not open, inspect, attach, edit, crop, imitate, or otherwise use `qa/production/page-32/frames/candidates/frame-b-v1.png`, its proofs, any rejected Page 32 image, or any additional reference as a generation input. The known 1254 × 1254 result is evidence of the tool's square-output behavior only.

The builder and critic are isolated roles. The builder generates, normalizes by the permitted whole-image operation if necessary, records one audit, derives proofs, and hands the candidate to the independent critic. The builder does not decide approval.

## Exact outputs

- Untouched built-in result: `qa/production/page-32/frames/candidates/frame-b-square-v1-raw.png`
- Exact normalized square candidate: `qa/production/page-32/frames/candidates/frame-b-square-v1.png`
- Builder audit: `qa/production/page-32/frames/audits/frame-b-square-v1.md`
- Isolated assembled-scale proof: `qa/production/page-32/frames/proofs/frame-b-square-v1-600x600.png`
- Larger isolated proof: `qa/production/page-32/frames/proofs/frame-b-square-v1-768x768.png`
- Independent critic report target: `qa/production/page-32/frames/critic-frame-b-square-v1.md`
- If approved, byte-for-byte promotion target: `qa/production/page-32/frames/approved/frame-b-square.png`

Save the built-in result untouched to the raw path. It must be a flattened RGB square PNG. A non-square canvas, corrupt or truncated output, or gross anatomical breakage is failed generation; stop and report it rather than repairing it or creating another candidate.

If the raw result is already 1024 × 1024 RGB, copy it byte-for-byte to the normalized candidate path. If it is another exact square size, including 1254 × 1254, uniformly resample the complete image once to exactly 1024 × 1024 RGB and save it at the normalized candidate path. This one whole-image square-to-square normalization is the only permitted pixel transformation. Do not crop, stretch nonuniformly, repaint, patch, extend, selectively recolor, sharpen, add or remove figures or objects, enlarge Haydée/document/seal, alter architecture, add mattes, or add text.

Derive both isolated proofs from the untouched normalized 1024 × 1024 candidate by whole-image scaling only. The 600 × 600 proof exactly represents Frame B's story-art width in the 600 × 900 assembled-page proof. The 768 × 768 proof exactly represents its story-art width in the 768 × 1152 assembled-page proof.

## Audit and handoff

Record one compact practical audit covering:

- raw canvas dimensions/mode and normalized canvas dimensions/mode;
- confirmation that normalization, if used, was uniform whole-image scaling only;
- zero strings;
- exactly two live humans total;
- one remote small full-figure Haydée fully enclosed by the complete open doorway;
- one tiny far-end bar-occluded Fernand;
- no other human vertical or Count-like black figure;
- unmistakable pale folded document and attached saturated red seal at the 600 × 600 proof without enlarged Haydée;
- Page 31 hall, palette, daylight, and Velvet Cinema continuity;
- anatomy and raster integrity;
- raw, normalized candidate, and proof paths.

The audit is a report, never a gate. Except for the narrow failed-generation conditions above, submit the normalized square candidate to the independent critic regardless of audit findings. Do not regenerate before the verdict. The critic alone returns `APPROVED` or `REVISE`. Do not promote or assemble before approval. Promotion must copy `frame-b-square-v1.png` byte-for-byte to `approved/frame-b-square.png`; never promote the raw file in its place.

## Assembly boundary

The builder does not create the 24-pixel mattes and does not assemble Page 32. After isolated approval, assembly may place the approved 1024 × 1024 square unchanged at `(0, 488)` in the final page and draw only the two fixed matte rectangles defined by `qa/production/page-32/frames/assembly-spec-square.md`. No generated story pixel may be cropped, covered, repainted, patched, or altered.

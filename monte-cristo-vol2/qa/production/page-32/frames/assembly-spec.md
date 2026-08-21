# Page 32 — locked two-component assembly spec

## Final geometry

Final page: exactly 1024 × 1536 pixels, RGB, flattened PNG.

| Element | Rectangle `(x, y, width, height)` | Share of image area excluding gutter |
|---|---:|---:|
| Frame A, top | `(0, 0, 1024, 448)` | 29.47% |
| Fixed gutter | `(0, 448, 1024, 16)` | — |
| Frame B, lower dominant | `(0, 464, 1024, 1072)` | 70.53% |

The gutter is a solid neutral page white: RGB `(255, 255, 255)`. There is no outer border, padding, overlap, bleed, or additional divider.

## Approved inputs and exact outputs

- Required approved Frame A input: `qa/production/page-32/frames/approved/frame-a.png` — exact 1024 × 448 RGB PNG.
- Required approved Frame B input: `qa/production/page-32/frames/approved/frame-b.png` — exact 1024 × 1072 RGB PNG.
- Fresh assembled candidate: `qa/production/page-32/candidates/page-32-components-v1.png`.
- Assembly audit: `qa/production/page-32/audits/page-32-components-v1.md`.
- 600 × 900 whole-page proof: `qa/production/page-32/proofs/page-32-components-v1-600x900.png`.
- 768 × 1152 whole-page proof: `qa/production/page-32/proofs/page-32-components-v1-768x1152.png`.
- Fresh whole-page critic report: `qa/production/page-32/critic-components-v1.md`.
- Canonical promotion target only after whole-page approval: `pages/page-32.png`.

## Assembly limits

Both component rasters must first receive isolated-frame `APPROVED` verdicts and byte-for-byte promotion to the approved input paths. Assembly code may only verify dimensions/mode, place the complete approved Frame A raster in its rectangle, place the complete approved Frame B raster in its rectangle, draw the fixed white gutter, flatten, convert/export as RGB PNG, and derive whole-page proofs by whole-image scaling.

No crop or reframing is permitted. No painting, patching, healing, generative fill, compositing within either panel, content-aware extension, selective recoloring, retouching, sharpening that changes content, object or figure insertion/removal, gaze correction, seal enlargement, architecture alteration, or lettering is permitted. If an approved input does not match its locked rectangle exactly, stop; do not repair it during assembly.

The assembled candidate must receive a fresh independent whole-page critic after assembly, reviewing the 600 × 900 proof first for zero-text transcription, the unanimous screen-right crowd, one small doorway Haydée, one tiny far-end bar-occluded Fernand, exact live-figure counts per panel, document/seal readability, absence of Count-like false positives, 30/70 hierarchy, fixed gutter, and cross-panel cohesion of Velvet Cinema medium, cold high daylight, crimson value, dark oak, gilded plaster, black coats, and charcoal/ink edges. Neither component approval nor the assembly audit can substitute for this whole-page verdict. Only an `APPROVED` whole-page report permits byte-for-byte canonical promotion.

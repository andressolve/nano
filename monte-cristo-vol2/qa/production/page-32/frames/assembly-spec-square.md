# Page 32 — locked square-safe two-component assembly spec

## Final geometry

Final page: exactly 1024 × 1536 pixels, RGB, flattened PNG.

| Element | Rectangle `(x, y, width, height)` | Rule |
|---|---:|---|
| Frame A, top | `(0, 0, 1024, 448)` | Place complete approved raster unchanged. |
| Fixed gutter | `(0, 448, 1024, 16)` | Solid page white, RGB `(255, 255, 255)`. |
| Frame B top matte | `(0, 464, 1024, 24)` | Solid dark-oak/oxblood, RGB `(38, 24, 25)`. |
| Frame B square story art | `(0, 488, 1024, 1024)` | Place complete approved square unchanged. |
| Frame B bottom matte | `(0, 1512, 1024, 24)` | Solid dark-oak/oxblood, RGB `(38, 24, 25)`. |

The lower Frame B rectangle remains exactly `(0, 464, 1024, 1072)`. The two equal 24-pixel matte bands center the 1024 × 1024 art vertically and consume the otherwise unsupported 48 pixels without cropping, stretching, outpainting, or inventing story content. The flat RGB `(38, 24, 25)` value is a deterministic near-black dark-oak with a restrained oxblood cast suited to the approved dark-oak/crimson page treatment. The mattes contain no texture, gradient, line, ornament, object, figure, or lettering.

There is no outer border, padding outside the listed rectangles, overlap, bleed, or additional divider. The white gutter remains visually and geometrically separate from the top matte.

## Approved inputs and exact outputs

- Required approved Frame A input: `qa/production/page-32/frames/approved/frame-a.png` — exact 1024 × 448 RGB PNG.
- Required approved Frame B square input: `qa/production/page-32/frames/approved/frame-b-square.png` — exact 1024 × 1024 RGB PNG, byte-for-byte promoted after isolated approval.
- Fresh assembled candidate: `qa/production/page-32/candidates/page-32-square-components-v1.png`.
- Assembly audit: `qa/production/page-32/audits/page-32-square-components-v1.md`.
- Whole-page desktop proof: `qa/production/page-32/proofs/page-32-square-components-v1-600x900.png`.
- Whole-page tablet proof: `qa/production/page-32/proofs/page-32-square-components-v1-768x1152.png`.
- Fresh whole-page critic packet: `qa/production/page-32/critic-square-components-packet.md`.
- Fresh whole-page critic report: `qa/production/page-32/critic-square-components-v1.md`.
- Canonical promotion target only after whole-page approval: `pages/page-32.png`.

At the 600 × 900 whole-page proof, the Frame B story art is represented at exactly 600 × 600 before final whole-page rasterization; each 24-pixel matte is approximately 14.06 proof pixels high. At the 768 × 1152 proof, the story art is exactly 768 × 768 and each matte is exactly 18 pixels high. Derive both proofs by scaling the complete assembled page only; do not independently resize or reassemble regions for proof production.

## Prerequisites and deterministic assembly rule

Both component rasters must first receive isolated-frame `APPROVED` verdicts and byte-for-byte promotion to the exact approved input paths. Stop if Frame A is not exactly 1024 × 448 RGB or Frame B is not exactly 1024 × 1024 RGB. Do not repair either input during assembly.

Starting from a new 1024 × 1536 RGB canvas, assembly may perform only these operations:

1. Fill the page white RGB `(255, 255, 255)`.
2. Place the complete approved Frame A raster at `(0, 0)` with no scaling.
3. Preserve the white gutter at `(0, 448, 1024, 16)`.
4. Fill the top matte rectangle `(0, 464, 1024, 24)` with RGB `(38, 24, 25)`.
5. Place the complete approved Frame B square raster at `(0, 488)` with no scaling.
6. Fill the bottom matte rectangle `(0, 1512, 1024, 24)` with RGB `(38, 24, 25)`.
7. Flatten and export as an exact 1024 × 1536 RGB PNG.
8. Derive the two whole-page proofs by uniform whole-image scaling only.

No crop, reframing, nonuniform stretch, painting, patching, healing, generative fill, compositing within either approved panel, content-aware extension, selective recoloring, retouching, content-changing sharpening, object or figure insertion/removal, gaze correction, seal enlargement, architecture alteration, or lettering is permitted. The deterministic matte fills are the only assembly-added pixels beyond the existing white gutter and are outside the approved square story art.

## Assembly audit

The assembly audit must record:

- exact input paths, dimensions, and RGB mode;
- exact output path, 1024 × 1536 dimensions, and RGB mode;
- Frame A, gutter, both matte, and Frame B coordinates;
- exact gutter and matte RGB values;
- confirmation that Frame B is complete, centered, unscaled, uncropped, and unobscured;
- confirmation that no operation beyond the eight listed assembly steps occurred;
- both whole-page proof paths.

The assembly audit is a report, never an approval gate.

## Fresh whole-page critic contract

The assembled candidate must receive a fresh independent whole-page critic after assembly. The critic must not rely on either isolated approval or the assembly audit as a verdict and must not edit, repair, promote, or generate anything.

Review `qa/production/page-32/proofs/page-32-square-components-v1-600x900.png` first and blind-transcribe all visible strings. The required result is zero strings. At that proof, verify the exact Page 32 story and hierarchy: unanimous literal screen-right crowd in Frame A; one small solitary full-figure Haydée completely inside the distant open doorway in Frame B; one tiny far-end bar-occluded Fernand; exact live-figure counts per panel; no other human vertical or Count-like black figure; unmistakable pale folded document and attached saturated red wax seal; vast-hall dominance; and a clear approximately 30/70 top/lower hierarchy.

Then review the 768 × 1152 proof and full 1024 × 1536 candidate for anatomy, integrity, fixed 16-pixel white gutter, equal 24-pixel matte bands, clean centering, and cross-panel cohesion of Velvet Cinema medium, cold high daylight, crimson value, dark oak, gilded plaster, black coats, and charcoal/ink edges. The mattes must read as quiet page treatment, not extra story panels or content, and must contain no marks or lettering.

Save a concise report to `qa/production/page-32/critic-square-components-v1.md` with transcription first, mandatory findings only, geometry/integrity findings, and one final line exactly `APPROVED` or `REVISE`. Only `APPROVED` permits byte-for-byte promotion of the 1024 × 1536 assembled candidate to `pages/page-32.png`. Component approval and the assembly audit cannot substitute for this fresh whole-page verdict.

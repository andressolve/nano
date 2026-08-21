# Builder audit — Sheet 23 v1

## Outcome

**PASS TO INDEPENDENT CRITIC**

This is the builder's one practical-essentials audit of the first deterministic production artifact. It is not an approval or promotion.

## Candidate and method

- Candidate: `monte-cristo-vol2/refs/23-page-33-chamber-objects-carrier.png`
- SHA-256: `b5d48cac4e21741053a29bded5055d89ecdf7b08360c09835b65752dd483e649`
- File validation: 1536 × 1024, 8-bit/color RGB, non-interlaced PNG.
- Reproducible builder: `qa/references/sheet-23/build-carrier.py`.
- Manifest: `qa/references/sheet-23/manifest-v1.json`.
- No image generation, API, image-generation CLI, repainting, relighting, retouching, or invented content was used.

## Practical essentials

- PASS — The approved Sheet 19 source appears in the left half and the approved Sheet 21 source appears in the right half.
- PASS — Both complete 1536 × 1024 source rasters are reduced directly to 759 × 506 by the exact aspect-preserving scale 253/512 using Pillow LANCZOS resampling.
- PASS — The full source rectangle `[0, 0, 1536, 1024]` is retained for each source. All three Chamber views and all seven object groups remain present; no view or object is cropped away.
- PASS — The left placement is `[0, 259]`; the right placement is `[777, 259]`. The 18-pixel neutral gutter between them is the only separator.
- PASS — The unused upper and lower canvas areas and the gutter use one unlettered neutral RGB ground `(215, 211, 201)`. There are no labels, captions, dividers, outlines, borders, or added visual content.
- PASS — Source pixels are changed only by the recorded deterministic reduction. Composition, palette, lighting, object design, and architectural design remain source-derived.
- PASS — The manifest records both approved source paths and SHA-256 values, the no-crop source rectangles, resampling method, exact and decimal scales, resized dimensions, placements, gutter geometry, output path, and output SHA-256.
- PASS — Original-resolution visual inspection shows clean, complete transport of both plates with no clipping, overlap, distortion, interpolation artifact, or unintended mark.

The first deterministic artifact is plausible and is submitted without cosmetic iteration. Nothing was written to `refs/approved/`, and no other sheet, carrier, or story page was built.

# Builder audit — Sheet 10 v1

## Outcome

**PASS TO INDEPENDENT CRITIC**

This is the first plausible deterministic production candidate. This audit is not an approval or promotion.

## Method and provenance

- PASS — Built only by the reproducible script `qa/references/sheet-10/build-head-board.py`.
- PASS — No image generation, API, CLI image generation, repainting, relighting, retouching, facial interpolation, or identity alteration was used.
- PASS — Inputs are exactly the approved sheets 01–08. The builder validates every source against its fixed SHA-256 before producing output.
- PASS — `manifest-v1.json` records the required fixed order, source paths, source SHA-256 values, source dimensions/mode, crop boxes, normalization landmarks, scales, resized sizes, placements, cells, matte method, and output SHA-256.
- PASS — The exact approved three-quarter head-and-shoulders crops are retained; only deterministic LANCZOS reduction and soft crop-edge alpha placement onto a neutral ground are applied.

## Required board checks

- PASS — Output is a 1536 × 1024, 3:2 landscape, 8-bit/color RGB PNG.
- PASS — Eight heads appear in one even row in fixed 01→08 order: Count, Mercédès, Fernand, Albert, Haydée, Danglars, Beauchamp, Villefort.
- PASS — Hairline-to-chin height is normalized to 250 pixels for all eight crops, with the hairline aligned to y=330.
- PASS — Each crop stays within its 192-pixel cell; no face overlaps another.
- PASS — The board has one neutral unlettered ground and contains no text, labels, name plates, drawn dividers, or borders.
- PASS — No costume or body content was invented; only clothing already present in each approved head-and-shoulders crop remains.
- PASS — All eight identities remain visibly distinct at board scale, including the critical Count/Albert and Danglars/Villefort lanes.

## Candidate identity

- Output: `monte-cristo-vol2/refs/10-head-board.png`
- SHA-256: `626c2ee6a2d0e6e240cd571c9225ee1e97ef03fa258d1f591b769484089b52f6`

No file was written to `refs/approved/`, and no other sheet, board, plate, or story page was built.

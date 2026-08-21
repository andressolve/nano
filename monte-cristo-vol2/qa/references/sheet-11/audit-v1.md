# Builder audit — Sheet 11 v1

## Outcome

**STOP — PRACTICAL ESSENTIALS FAILURE; NOT SUBMITTED TO CRITIC**

The deterministic render was visually inspected at original resolution. It is not a plausible production candidate and is not approved or promoted.

## Checks that passed

- PASS — Built deterministically from approved sheets 01–08 with fixed SHA-256 gates; no image generation, repainting, relighting, pose correction, or identity redesign.
- PASS — Fixed 01→08 order in one row.
- PASS — All figures use the same 370-pixel body-height normalization and y=697 floor target.
- PASS — One flat dark silhouette value on one light neutral ground, with no source colour, interior detail, text, labels, dividers, or borders.
- PASS — Output validates as a 1536 × 1024, 8-bit/color RGB PNG.
- PASS — `manifest-v1.json` records source paths/hashes, extraction method, crop boxes, seeds, scales, placements, and output hash.

## Consequential failures

1. **Danglars (#6) has a materially missing upper head/face contour.** The silhouette carries a large open notch through the upper-right head mass. This is not the approved full-length contour and violates the prohibition on identity reshaping.
2. **Source ground shadows remain fused to several feet**, most visibly on the Count, Fernand, Albert, Danglars, and Beauchamp. These are ground pixels rather than figure pixels, so the required “isolate only that figure from its plain ground” condition is not met.

Correcting these failures would require a different source-contour extraction method. Continuing with manual contour invention would risk prohibited redrawing or pose correction, so the builder stopped rather than submitting or privately polishing.

## Evidence

- Working output: `monte-cristo-vol2/refs/11-silhouette-board.png`
- Preserved failed render: `monte-cristo-vol2/qa/references/sheet-11/candidate-builder-failed-v1.png`
- SHA-256: `5894a3eb660e47f98e9ac87695f5e0ed6a9fd005e8ead775890e2cfbd3958b0f`
- Reproducible script: `monte-cristo-vol2/qa/references/sheet-11/build-silhouette-board.py`
- Manifest: `monte-cristo-vol2/qa/references/sheet-11/manifest-v1.json`

No file was written to `refs/approved/`, and no other sheet, board, plate, or story page was built.

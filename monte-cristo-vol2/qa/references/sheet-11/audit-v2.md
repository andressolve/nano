# Builder audit — Sheet 11 v2

## Outcome

**PASS TO INDEPENDENT CRITIC**

This is the builder's single practical-essentials audit, not an approval or promotion.

## Candidate and execution evidence

- Candidate: `monte-cristo-vol2/refs/11-silhouette-board.png`
- SHA-256: `46c9a8a05c6556dcaeeb64b8209db3609de01ef9cfcea56787be2bf477d3b24d`
- File validation: 1536 × 1024, 8-bit/color RGB, non-interlaced PNG.
- The production lead ran `run-v2-in-terminal.command`; `terminal-v2.log` records status 0.
- Extraction remained the authorized deterministic local method: macOS Vision `VNGeneratePersonInstanceMaskRequest`, revision 1, on the exact approved full-length crops, with the fixed `>=128` binary cutoff and the recorded floor/body-height normalization.
- No image generation, network/API call, hand tracing, polygon drawing, contour painting, reshaping, pose correction, relighting, or invented pixels were used.

## Practical essentials audit

- PASS — Eight upright, complete source-derived full-body contours are present in the fixed order 01 Count, 02 Mercédès, 03 Fernand, 04 Albert, 05 Haydée, 06 Danglars, 07 Beauchamp, 08 Villefort.
- PASS — The approved source postures and distinguishing outer contours remain recognizable, including Mercédès's gown, Fernand's military breadth, Haydée's robe, Danglars's heavier build, and Beauchamp's stoop.
- PASS — All eight use the unchanged recorded head-top and floor landmarks to normalize to a 370 px body height and common target floor y=697. Their visible feet and hems resolve consistently around that floor without a fused ground strip.
- PASS — Silhouettes are one flat dark value on one light neutral ground, with no interior color/detail and no grey mask haze or streaking.
- PASS — No retained source ground shadows are fused to the contours.
- PASS — No text, labels, dividers, or borders are present.

### Haydée floor-mark determination

The small detached dark mark below Haydée's left side is her source-derived forward shoe, not a ground artifact. In the approved full-length source, that shoe is visibly separated from the robe hem by light ground; the automatically selected binary Vision mask preserves the same shoe-shaped component in the same relative position. The diffuse grey floor shadow visible farther beneath and around the source feet is absent. The mark is therefore a legitimate part of the complete source contour.

## Preserved failure evidence

- Failed v2 orientation/haze render: `qa/references/sheet-11/candidate-builder-failed-v2.png`
- Failed v2 SHA-256: `53c0c1bff509f78f7d9ae3a68f89ca21d36a5badc856ae0ed21eb29e523eceea`
- Its log and manifest are preserved as `terminal-v2-orientation-failure.log` and `manifest-v2-orientation-failure.json`.
- Failed v1 render: `qa/references/sheet-11/candidate-builder-failed-v1.png`
- Failed v1 SHA-256: `5894a3eb660e47f98e9ac87695f5e0ed6a9fd005e8ead775890e2cfbd3958b0f`

No file was written to `refs/approved/`, and no other sheet, board, plate, or story page was built.

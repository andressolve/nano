# 02 — CHARACTERS

Rule: the lock is the VISUAL. Never write "Kepler", "Tycho Brahe" etc. in any image prompt — names live in
this doc, the script, and ref filenames only. Re-Read the actual ref PNG before writing any page prompt.

## KEPLER — 4 age phases

### Phase K1 — child, ~6 (P1) — `refs/ref_kepler_child.png`
Small thin pale boy of six, short dark brown hair, large alert dark eyes, narrow face, a few faint pox marks,
slightly awkward hands. Plain 1570s German wool tunic in dull brown, simple hose, worn leather shoes.
Realistic child anatomy. NOT cute, NOT mascot proportions, NOT oversized eyes.

### Phase K2 — Graz, 22–28 (P2–P4) — `refs/ref_kepler_graz.png`
Slight, wiry young man in his mid-twenties. Dark brown hair, very high forehead, long narrow face, large
alert dark eyes with a slight squint (poor eyesight), sparse young dark pointed beard and mustache. White
ruff collar, plain dark scholar's doublet, ink-stained fingers. Restless, forward-leaning posture.

### Phase K3 — Prague, 29–40 (P5–P13) — `refs/ref_kepler_prague.png`
The standard likeness (1610 portrait): man in his thirties, dark hair receding from a very high forehead,
long face, trim dark pointed beard and mustache, large intelligent dark eyes with a slight squint, sallow
scholar's complexion. White ruff collar, dark doublet. Slight wiry build, shoulders a little hunched from
desk work, ink-stained fingers.

### Phase K4 — older, 45–58 (P14–P18) — `refs/ref_kepler_older.png`
Same long face aged into the fifties: hair and pointed beard heavily grey-streaked to grey, forehead lines,
hollower cheeks, tired eyes still alert. Plain white falling collar (flat, post-1620 fashion — NOT a ruff),
worn dark coat. Thin, slightly stooped.

Phase discipline: NEVER feed a wrong-phase ref. P14–P18 = K4 (state "grey-streaked beard, flat falling
collar, no ruff" in every prompt). Watch the model's urge to de-age him or restore the ruff.

## TYCHO BRAHE — 53 (P5–P7) — `refs/ref_tycho.png`
Corpulent, powerful Danish nobleman in his fifties. Reddish-blond hair receding from a high bald pate,
ENORMOUS handlebar mustache sweeping past the jaw, small pointed chin-beard. Across the bridge of his nose,
a visible BRASS prosthetic plate with a thin seam (duel scar) — subtle metallic glint, not a cartoon nose.
Rich dress: black doublet with gold embroidery, fur-trimmed robe, white ruff, heavy gold chain with a small
elephant medallion. Commanding, expansive posture.

## KATHARINA KEPLER — early 70s (P16) — `refs/ref_katharina.png`
Very small, thin old woman in her early seventies. Deeply lined, weathered narrow face, sharp dark eyes
(the same alert eyes as her son), wisps of grey hair under a plain white linen cap. Coarse dark wool dress,
grey shawl. Stands very upright despite her size — unbowed. No portrait survives; this is our invention,
documented as such.

## BARBARA KEPLER — 24–37 (P4, P13 memory) — `refs/ref_barbara.png`
Prosperous Styrian burgher wife in her twenties. Round gentle face, fair-brown hair pulled back under a
white bonnet, small ruff, dark bodice with russet wool skirt, keys at her belt. No authenticated likeness;
invented, documented as such.

## Prose-only (no refs — described fresh, never 3+ named faces on a page)
- **Mästlin** (P2): astronomy professor ~45, full dark beard, black scholar's gown, kindly heavy-lidded eyes.
- **Susanna** (P14): young woman of 24, simple clean dress, calm steady face.
- Students, examiners, magistrates, printers, courtiers: generic period figures.

## Reference-sheet generation prompt (template)
Landscape 1536×1024, oil-painting register (Style Block + register + anti-drift verbatim). Left half:
chest-up portrait, neutral expression, eyes toward viewer. Right half: full-body standing figure. Plain
warm-toned neutral background, soft studio-like north light. NO text, NO labels, NO props unless specified
in the lock. One character per sheet.

## Page-by-page face count (Strategy 1 audit)
Max 2 named faces on any page: P5 (K3+Tycho), P7 (K3+Tycho), P4 (K2+Barbara), P16 (K4+Katharina).
All other pages: 1 named face + unnamed figures. No composite plate needed.

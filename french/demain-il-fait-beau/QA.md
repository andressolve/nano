# DEMAIN, IL FAIT BEAU ! — QA ledger

## Production state

- Script: APPROVED by user on 2026-08-13
- Supplemental reference: APPROVED
- Page 1: APPROVED
- Page 2: APPROVED
- Two-page sequence gate: APPROVED
- Reader: APPROVED by static and asset validation
- Catalog: ADDED locally; not committed or published

## Required evidence

For each page keep:

- exact generation prompt in `01-IMAGE-PROMPTS.md`;
- original candidate in `qa/`;
- concise essentials audit in this ledger;
- reduced reader proof in `qa/` when available;
- canonical page in `pages/` only after approval;
- SHA-256 confirmation that canonical bytes match the approved candidate.

## Supplemental reference audit

- File: `refs/ref-rain-cafe-football.png`
- Dimensions: 1536×1024
- SHA-256: `ef6ef11986b031c252d29e7eb7527e4e8f76092d37dadec71f23da67d5418cf4`
- Hugo identity, age, base clothing, navy rain layer, and red trainers: PASS
- Léo identity, age, base hoodie, teal rain layer, and rain boots: PASS
- Café worker distinct, consistent, and production-usable: PASS
- Football, hot chocolate, croissant, counter, pastry display, and table: PASS
- No labels, menu writing, prices, logos, balloons, or watermarks: PASS
- Verdict: APPROVED without regeneration

## Page 1 essentials audit

- Candidate: `qa/page-01-candidate.png`
- Reader proof: `qa/page-01-reader-proof.png` (512×768)
- Canonical page: `pages/page-01.png`
- Canvas: 1024×1536 (exact 2:3 portrait)
- Candidate and canonical SHA-256: `02b0ab92fb4fef79d370c9544edab9d80009f896f40e53118af940f42c4218c7`
- Exactly four large panels in a clear 2×2 reading order: PASS
- Exactly four balloons, one per panel, with no captions or additional visible text: PASS
- Script, including accents and punctuation: PASS
  1. Hugo: `Il pleut.`
  2. Hugo: `Bonjour ! Je voudrais un chocolat chaud, s’il vous plaît.`
  3. Server: `Et avec ça ?`
  4. Léo: `Un croissant, s’il vous plaît.`
- Speaker attribution and visible tails: PASS
- Rain-to-café transition, ordering action, and croissant choice: PASS
- Hugo, Léo, server, café, and single-football continuity: PASS
- Generation converged Hugo and Léo's rain shells toward the same teal family and
  gave both practical rain boots. Their faces, hair, skin tone, staging, and
  base-clothing cues remain distinct, so this is a nonblocking rain-scene color
  variation rather than an identity or story failure.
- Verdict: APPROVED; candidate promoted byte-for-byte without regeneration

## Page 2 essentials audit

- Candidate: `qa/page-02-candidate.png`
- Reader proof: `qa/page-02-reader-proof.png` (512×768)
- Canonical page: `pages/page-02.png`
- Canvas: 1024×1536 (exact 2:3 portrait)
- Candidate and canonical SHA-256: `bf570125a47321cb21e19a5273789b044ea8bd16b195c8007e4609d02ca5aeb0`
- Exactly four large panels in a clear 2×2 reading order: PASS
- Exactly four balloons, one per panel, with no captions or additional visible text: PASS
- Script, including accents and punctuation: PASS
  1. Hugo: `C’est tout, merci.`
  2. Hugo: `Tu veux jouer demain ?`
  3. Léo: `Oui, avec plaisir !`
  4. Léo: `Il fait beau !`
- Speaker attribution and visibly connected tails: PASS
- Counter handoff, invitation, acceptance, and next-day payoff: PASS
- Café, food, clothing, and single-football continuity: PASS
- Final panel is unmistakably a dry, sunny next day and restores Hugo and Léo's
  approved everyday outfits: PASS
- Verdict: APPROVED; candidate promoted byte-for-byte without regeneration

## Two-page sequence gate

- Proof: `qa/two-page-sequence-proof.png` (512×1560), with the two reduced
  reader proofs stacked in true reading order
- Eight panels and eight exact balloons read continuously without explanation:
  PASS
- Causal spine—rain → café stop → order → invitation → sunny next day: PASS
- Hugo, Léo, server, café, food, and football remain recognizable and coherent:
  PASS
- Page turn preserves the café scene before the final dry, sunny transition:
  PASS
- Lettering remains comfortable in the 512-pixel-wide reduced proof: PASS
- Verdict: APPROVED

## Reader audit

- Reader: `index.html`
- Comic appears before lesson notes and optional questions: PASS
- Page 1 and Page 2 are in explicit order with page labels and descriptive alt
  text: PASS
- Three optional recognition questions use only lines from the comic: PASS
- Responsive sizing retains the full 2:3 pages without cropping: PASS by CSS
  inspection; both source pages are exact 2:3 canvases
- HTML audit found two page images, three questions, nine choices, and all local
  targets present: PASS
- `catalog.js` and `home.js` JavaScript syntax: PASS
- Live browser viewport screenshots were unavailable because no browser was
  connected to this session. The canonical pages and reduced uninterrupted
  proof were visually inspected; this is a tooling limitation, not an observed
  reader defect.
- Verdict: APPROVED for the local collection; no commit or publication was
  requested

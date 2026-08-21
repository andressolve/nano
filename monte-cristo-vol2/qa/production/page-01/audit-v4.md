# Builder practical-essentials audit — Page 01 v4

## Outcome

**SUBMITTED TO INDEPENDENT CRITIC WITH A MANDATORY FINDING**

This is the builder's single practical audit of the sole v4 production candidate and the final attempt permitted under the existing composition. It is not an approval or promotion, and the candidate has not been written to `pages/`. The brief prohibits a private reroll, so the candidate is submitted despite the finding below.

## Candidate and generation record

- Candidate: `qa/production/page-01/candidates/page-01-v4.png`
- SHA-256: `e2758dd361ae7110f4b7abb01d63c8644f4341e70e7ea02a56f447db241af41a`
- File validation: 1024 × 1536, 8-bit/color RGB, non-interlaced PNG.
- Exact corrective prompt: `qa/production/page-01/prompts/page-01-v4.md`. Its base matches the verified §5 Page 1 prompt exactly; the only appended language is the named v4 final mandatory correction.
- Attached inputs, and no others:
  1. `refs/approved/01-count-1838.png` — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`.
  2. `refs/approved/17-set-count-house.png` — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`.
- Generated once as a complete whole-page redraw with the built-in Codex in-app image-generation path under the ChatGPT subscription. Rejected v1–v3 were preserved and were not attached. No API, API key, CLI fallback, predecessor, patching, or second generation was used.

## Script transcription

All four required prose blocks appear exactly once, in the correct order, with correct spelling, punctuation, capitalization, apostrophes, and the accent in `Champs-Élysées`:

1. `Nine years after a shipowner in Marseille walked down to the harbour and found a ship he had lost sitting at anchor, a stranger bought the house at number thirty, Champs-Élysées.`
2. `He paid in gold, he paid at once, and he furnished it the way a man furnishes a room he does not mean to live in. Within a month Paris had decided he was the most interesting person in France. Nobody could say where the money came from. Nobody asked twice.`
3. `From that window he could see three roofs.`
4. `He had chosen the house for that.`

No pseudo-text, title, signature, page number, quotation marks, speaker label, speech balloon, or tail is visible. Tail ownership is therefore not applicable.

## Visual essentials

- PASS — The page retains exactly two panels with one unmistakably dominant upper room/window panel and a wide horizontal rooftop band below.
- PASS — Exactly one human being appears: a small rear-view man at the glass. No woman, servant, crowd, second figure, duplicate, or face appears.
- PASS — The figure reads as the locked Count through tall slim columnar proportions, swept-back dark head, still posture, and unrelieved black evening silhouette. With no other figure present, there is no identity collision.
- PASS — His visible back-view anatomy, shoulders, arms, coat, legs, stance, and reflection are coherent; no exposed hand or finger is malformed.
- PASS — The dominant room is enormous, cold, unlit, and deliberately empty. The architectural fireplace is dark; there is no fire, family object, portrait, or furniture clutter.
- PASS — Both fixed parchment fields are enlarged and remain wholly clear of the Count and window glass. The upper field is in uninterrupted blank wall; the lower field is in the dark-sky lane.
- PASS — The window and lower band establish the roof cues: copper gutter at left, central flagpole, and the right-hand house with its visible windows lit.
- PASS — The palette and matte gouache/opaque-watercolor Velvet Cinema register remain intact, with no obvious generation artifact, crop mark, or outer decorative frame.
- **MANDATORY FINDING — V4 materially enlarges the prose, but the required 40–44 px actual lowercase black x-height remains unmet. At the 1024 × 1536 source, dark-glyph row-run measurement finds visible letterform extents approximately 25–27 px high in both fields; lowercase x-height is smaller still. This is substantially above v1–v3 but materially below the mandated minimum. The final mandatory correction therefore remains unresolved.**

## Derived proofs

- `proofs/page-01-v4-600.png` — exact 600 × 900 RGB PNG, SHA-256 `92eb68a0b230adab316c10d57adb16a32bedd5ff40368a2b27acd1c470ddb9f3`.
- `proofs/page-01-v4-768.png` — exact 768 × 1152 RGB PNG, SHA-256 `2e348567f39e535e212a2e87ca1120ec2fe915fe0d9c924451ef4649c56f9788`.
- Both proofs are direct Pillow LANCZOS reductions of the unchanged v4 candidate. The 600 × 900 proof is comfortably readable, but visible glyphs measure roughly 15–16 px rather than the mandated 24–26 px, corroborating the source finding.

The content and composition are otherwise practically plausible. This sole v4 candidate is submitted with the mandatory lettering finding and without private reroll; the independent critic owns the verdict. No fifth incremental attempt is authorized under the existing composition.

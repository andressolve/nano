# Builder practical-essentials audit — Page 01 v2

## Outcome

**SUBMITTED TO INDEPENDENT CRITIC WITH A MANDATORY FINDING**

This is the builder's single practical audit of the sole v2 production candidate. It is not an approval or promotion, and the candidate has not been written to `pages/`. The brief prohibits a private reroll, so the candidate is submitted despite the finding below.

## Candidate and generation record

- Candidate: `qa/production/page-01/candidates/page-01-v2.png`
- SHA-256: `2dc238725c3fd06f404635f664869487c71edb70e2309f34cd17595b98a18714`
- File validation: 1024 × 1536, 8-bit/color RGB, non-interlaced PNG.
- Exact corrective prompt: `qa/production/page-01/prompts/page-01-v2.md`. Its base matches the verified §5 Page 1 prompt exactly; the only appended language is the named v2 mandatory correction.
- Attached inputs, and no others:
  1. `refs/approved/01-count-1838.png` — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`.
  2. `refs/approved/17-set-count-house.png` — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`.
- Generated once as a complete whole-page redraw with the built-in Codex in-app image-generation path under the ChatGPT subscription. Rejected v1 was preserved and was not attached. No API, API key, CLI fallback, predecessor, patching, or second generation was used.

## Script transcription

All four required prose blocks appear exactly once, in the correct order, with correct spelling, punctuation, capitalization, apostrophes, and the accent in `Champs-Élysées`:

1. `Nine years after a shipowner in Marseille walked down to the harbour and found a ship he had lost sitting at anchor, a stranger bought the house at number thirty, Champs-Élysées.`
2. `He paid in gold, he paid at once, and he furnished it the way a man furnishes a room he does not mean to live in. Within a month Paris had decided he was the most interesting person in France. Nobody could say where the money came from. Nobody asked twice.`
3. `From that window he could see three roofs.`
4. `He had chosen the house for that.`

No pseudo-text, title, signature, page number, quotation marks, speaker label, speech balloon, or tail is visible. Tail ownership is therefore not applicable.

## Visual essentials

- PASS — The page has two panels and a clearly dominant upper room/window panel occupying roughly 65%, over a wide rooftop band occupying roughly 35%.
- PASS — Exactly one human being appears: a small rear-view man at the glass. No woman, servant, crowd, second figure, duplicate, or face appears.
- PASS — The figure reads as the locked Count through tall slim columnar proportions, swept-back dark head, still posture, and unrelieved black evening silhouette. With no other figure present, there is no identity collision.
- PASS — His visible back-view anatomy, shoulders, arms, coat, legs, stance, and reflection are coherent; no exposed hand or finger is malformed.
- PASS — The dominant room is enormous, cold, unlit, and deliberately empty. The architectural fireplace is dark; there is no fire, family object, portrait, or furniture clutter.
- PASS — The window and lower band establish the roof cues: copper gutter at left, central flagpole, and the right-hand house with its visible windows lit.
- PASS — The palette and matte gouache/opaque-watercolor Velvet Cinema register remain intact, with no obvious generation artifact, crop mark, or outer decorative frame.
- **MANDATORY FINDING — Although v2 lettering is visibly larger and more generously led than v1, source-raster inspection does not support the required true 40–42 px visible letterform height. Dark glyph row runs in both prose fields measure approximately 21–23 px high at the 1024 × 1536 source. Even allowing for antialiased edge pixels, this is materially below 40 px. The named v2 correction therefore appears unresolved.**

## Derived proofs

- `proofs/page-01-v2-600.png` — exact 600 × 900 RGB PNG, SHA-256 `534832984cb6e25abcf32c62e91374bd2f659cf0b39b467facdc25f16e41b851`.
- `proofs/page-01-v2-768.png` — exact 768 × 1152 RGB PNG, SHA-256 `e8a7fddae37f49ee98c321ff6db12471f71a0080c1c8d5b8be3121fee1e4f6db`.
- Both proofs are direct Pillow LANCZOS reductions of the unchanged v2 candidate. The 600 × 900 proof is readable, but proof readability does not satisfy or supersede the mandatory 40–42 px source-letterform requirement.

The content and composition are otherwise practically plausible. This sole v2 candidate is submitted with the mandatory lettering finding and without private reroll; the independent critic owns the verdict.

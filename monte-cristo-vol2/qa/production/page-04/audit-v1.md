# Builder practical-essentials audit — Page 04 v1

## Outcome

**STOP — NOT PLAUSIBLE FOR INDEPENDENT-CRITIC SUBMISSION**

This is the builder's single practical audit of the one permitted v1 production candidate. It is not an approval or promotion, and the candidate has not been written to `pages/`. No private reroll was made.

## Candidate and generation record

- Candidate: `qa/production/page-04/candidates/page-04-v1.png`
- SHA-256: `08b227f028a866fd9c302bfe646ebb6be55bcd8f10657acf5ce7f33caf2d9e4f`
- File validation: exact 1024 × 1536, 8-bit/color RGB, non-interlaced PNG.
- Exact prompt: `qa/production/page-04/prompts/page-04-v1.md`, SHA-256 `ae3b5f38b954c9a7db39f6d6a0bece4fb976a42d54e3b4fc6c0f04c187d85e58`; diff-verified against the current §5 Page 4 prompt immediately before generation.
- Attached inputs, and no others:
  1. `refs/approved/01-count-1838.png` — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`.
  2. `refs/approved/05-haydee.png` — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`.
  3. `refs/approved/17-set-count-house.png` — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`.
  4. `pages/page-03.png` — SHA-256 `326061f3ccc54a364bc7f9f6db524d1703accfb9495133c12cb2b54510e8e5a3`.
- Generated once with the built-in Codex in-app image-generation path under the ChatGPT subscription. No API, API key, CLI fallback, rejected candidate, prototype, patch, post-hoc lettering, redesign, or second generation was used.

## Mandatory practical failure

- FAIL — The page contains **eight** balloons instead of the required seven. `You are not listening to me.` appears correctly in Panel 2, then appears a second time as an unrequested extra balloon at the lower right of Panel 3.
- FAIL — `That is enough.` is present, but its balloon is placed on Haydée's left side and its tail points to Haydée. The line belongs to the Count and was required at the lower right beneath her three statements.
- CONSEQUENCE — The extra repeated line corrupts the exact seven-string sequence, and the misplaced `That is enough.` reverses ownership of the decisive shutdown beat. These are script and attribution failures, not cosmetic deviations.

The exact required strings are otherwise legible, but the candidate cannot satisfy the literal script/ownership gate in its flattened form. Post-hoc lettering or balloon repair is prohibited, so correction would require a separately authorized complete whole-page redraw from the approved inputs.

## Other practical observations

- PASS — The page has four panels with a single dominant central confrontation panel.
- PASS — Haydée remains left and the Count right throughout; the two approved identities are distinct and anatomically coherent.
- PASS — The final panel shows Haydée half through the left door, not looking back, with the Count small and dark to the right.
- PASS — The absent woman is not depicted; no third figure, portrait, locket, flashback, Marseille scene, daylight, or crowd appears.
- PASS — Count-house continuity, cold palette, restrained crimson-gold Epirote costume, and painterly Velvet Cinema register remain plausible.

## Derived proofs

- `proofs/page-04-v1-600.png` — exact 600 × 900 RGB PNG, SHA-256 `cf9e9267b9eb54a81f331cb6a59f0a012c8b76ff4c688b9109790e9ffe8f7d5b`.
- `proofs/page-04-v1-768.png` — exact 768 × 1152 RGB PNG, SHA-256 `2bc28d8ac729a6079a4402836b6359a7598e70b7d7987510d7b7248b38341e1d`.
- Both proofs are direct Pillow LANCZOS reductions of the unchanged candidate.

The first candidate is preserved as required evidence. Work stops here without critic submission, reroll, promotion, later-page preparation, or `pages/` write.

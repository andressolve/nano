# Builder practical-essentials audit — Page 04 v2

## Outcome

**PASS TO INDEPENDENT CRITIC**

This is the builder's single practical audit of the first v2 production candidate. It is not an approval or promotion, and the candidate has not been written to `pages/`.

## Candidate and generation record

- Candidate: `qa/production/page-04/candidates/page-04-v2.png`
- SHA-256: `a9cc846b2387e37b71024c03ef3f06b747524af8b6c039a9b7a22accf5bd5e7f`
- File validation: exact 1024 × 1536, 8-bit/color RGB, non-interlaced PNG.
- Exact issued prompt: `qa/production/page-04/prompts/page-04-v2.md`, SHA-256 `dd11eee8e15fa9a6bffe7220631972e0157e00f7cd608bc980b7f2b3a63bd2ba`; its base diff-matches the verbatim current §5 Page 4 prompt, followed only by the authorized seven-balloon correction.
- Attached inputs, and no others:
  1. `refs/approved/01-count-1838.png` — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`.
  2. `refs/approved/05-haydee.png` — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`.
  3. `refs/approved/17-set-count-house.png` — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`.
  4. `pages/page-03.png` — SHA-256 `326061f3ccc54a364bc7f9f6db524d1703accfb9495133c12cb2b54510e8e5a3`.
- Rejected v1 remains preserved at `qa/production/page-04/candidates/page-04-v1.png` and was not attached.
- Generated once as a complete whole-page redraw with the built-in Codex in-app image-generation path under the ChatGPT subscription. No API, API key, CLI fallback, prototype, flattened-page patch, post-hoc lettering, redesign, or second generation was used.

## Mandatory v2 lettering and ownership gate

- PASS — The page contains **exactly seven** balloons, no more and no less.
- PASS — The exact order and map are:
  1. Panel 1, Count: `The Morcerf house is difficult. There are more people in it.`
  2. Panel 2, Haydée: `There is one more person in it.`
  3. Panel 3 upper left, Haydée: `I have lived in your house four years and you have never once said her name to me.`
  4. Panel 3 middle left, Haydée: `You say Mondego. You say the banker, the attorney.`
  5. Panel 3 lower left, Haydée: `You say the woman.`
  6. Panel 3 lower right, Count: `That is enough.`
  7. Panel 4 left, Haydée: `I am not the one who is afraid of a house.`
- PASS — Haydée owns exactly five balloons; the Count owns exactly two.
- PASS — `You are not listening to me.` does not appear. No unlisted string, duplicate balloon, caption, prose field, quotation mark, speaker label, page number, title, signature, or pseudo-text appears.
- PASS — All strings have exact wording, spelling, punctuation, capitalization, and apostrophes. The third Panel 3 string is plain upright mixed-case with no emphasis.

## Attribution and tails

- PASS — Panel 1's upper-right balloon points to the Count; Haydée's dark left edge is silent and receives no fragment.
- PASS — Panel 2's upper-left balloon points to Haydée.
- PASS — Panel 3's three left balloons align with and point toward Haydée; the sole lower-right balloon points to the Count.
- PASS — Panel 4's left balloon points down toward Haydée at the door. Every balloon remains on its owner's side and no ownership is ambiguous.

## Visual essentials

- PASS — The page contains four panels: the two-part top tier, one full-width central confrontation panel, and one full-width shallow ending panel. The central face-to-face panel is the single largest and visually dominant panel.
- PASS — Panel 1 shows the Count on the right with his hand lowered and a reasonable, recovering expression; Haydée is only a dark silent edge at left.
- PASS — Panel 2 shows Haydée left, unmoved and looking across the gutter.
- PASS — Panel 3 stages Haydée left and level against the Count right and visibly less composed, in close three-quarter opposition.
- PASS — Panel 4 shows Haydée left with one hand on the door frame, already half through and not looking back; the Count is small and dark on the right.
- PASS — Haydée remains twenty-seven, olive-gold, long-unbound-haired, and loose-silhouetted in crimson-and-gold Epirote dress. She does not drift toward a French comtesse.
- PASS — The Count remains clean-shaven, pallid, swept-back dark-haired, columnar, and unrelieved black. The identities remain distinct and anatomy is coherent.
- PASS — The woman under discussion is not shown or named. No third figure, servant, crowd, Fernand, Albert, Mercédès, portrait, miniature, locket, silhouette, flashback, Marseille image, daylight, or memory vignette appears.
- PASS — The cold Count-house room, three roof cues, doorway, cup/table continuity, costumes, hour, and painterly Velvet Cinema register remain intact.

## Derived proofs

- `proofs/page-04-v2-600.png` — exact 600 × 900 RGB PNG, SHA-256 `5d90ebb77462cc5d955b3f0b9d47bd6a0505391f4fc965a9b44dedfbcb7209a3`; the seven strings and ownership remain comfortable at reading scale.
- `proofs/page-04-v2-768.png` — exact 768 × 1152 RGB PNG, SHA-256 `6bd377d842ef81ed85b12e8daf23c4f7a4abb3c3c48cb0ac91a40f78a129be30`.
- Both proofs are direct Pillow LANCZOS reductions of the unchanged candidate.

The first v2 candidate is practically plausible and is submitted without private cosmetic reroll. Independent criticism remains required before any promotion.

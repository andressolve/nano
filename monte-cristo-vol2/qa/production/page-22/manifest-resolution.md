# Page 22 v1 — manifest resolution

**Status: PROMOTED — Page 22 v3 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-22/prompts/page-22-v1.md`
- Source: current `qa/_plan/page-22.md` §5, Page 22 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `48e6abf8ffba4a35894ad67da3d40c765adafe7b9038f1b9b63d2a31419c67f8`

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/05-haydee.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`
4. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

All four permanent references resolve under `refs/approved/`. They bind the Count, Haydée, the black Count-house room/table/lamp, and the large folded document with its broken red wax seal and unreadable ink marks.

The approved-reference gate is satisfied for every visible character. The Count and Haydée are the only permitted figures, and both have approved permanent locks.

## Continuous-scene input and sequential hold

5. `pages/page-18.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `393c903f9528ca59cadbc6e25d35ceea8b8574f51540d02594ca65681287f652` — required fifth generation input.

- Prompt-specific binding: Page 22 is continuous from promoted Page 18. Attach Page 18 to bind the same evening, table, chairs, single lamp, clothes, character positions, and document appearance/state. Pages 19–21 are narration and took no time in this room.
- `pages/page-21.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `9e537aee926d78eca16b7b304f6e84b043958d701683a186d363e3fb48721350`; sequence release only, and **must not be attached** to Page 22.
- The four approved permanent references plus promoted Page 18 exactly fill the five-input cap. Promoted Page 21, once it exists, remains sequence status only and not an image input.
- Never substitute Page 18 candidate evidence, any Page 21 candidate, any rejected art, any other page image, or prose description for the required promoted Page 18 continuity input.
- Every other character sheet and every page image other than promoted Page 18 are prohibited generation inputs. No extra setting, object, cast-board, or adversarial-board image may be attached.
- The prompt's content prohibitions remain binding: no Mercédès, Fernand, Albert, Danglars, Villefort, Beauchamp, servant, clerk, Janina, daylight, third figure, second document, fire, clutter, legible document writing, or identity collision.

Page 21 v1 is unconditionally approved and promoted. Page 22 generation is released with exactly the five listed Page 22 inputs and must not attach Page 21.

No image, proof, candidate, audit, critic report, Page 23 material, promotion, `pages/` write, or story-document edit was created during this preparation step.

## Page 22 v1 execution record

- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call.
- Attached inputs: exactly the five Page 22 files listed above—four approved permanent references and promoted Page 18. Promoted Page 21, every rejected candidate, and every unlisted image were excluded. No API, API key, or CLI path was used.
- Issued prompt: `qa/production/page-22/prompts/page-22-v1.md` — exact per-page §5 prompt — SHA-256 `48e6abf8ffba4a35894ad67da3d40c765adafe7b9038f1b9b63d2a31419c67f8`.
- Candidate: `qa/production/page-22/candidates/page-22-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `3f353b277b961afe63df9a00cf33daedd7423f6bf7ee528c4a7d2a8d9fa830d6`.
- 600 proof: `qa/production/page-22/proofs/page-22-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `4fdfa5447ce20bef8fbc36821370733fdf22fb2091fe253c8b1193672df80cde`.
- 768 proof: `qa/production/page-22/proofs/page-22-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `fc23e2a701139434bf6a7919c88a680db442ce7c51bc15863ecf073385457088`.
- Practical audit: `qa/production/page-22/audit-v1.md` — non-gating builder report; candidate submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 23 work, or story-document edit was performed.

## Page 22 v2 execution record

- Redraw basis: full authoritative Page 22 prompt plus only the independent critic's named Panel 1 reading-order correction. Rejected Page 22 v1 was preserved and excluded from generation inputs.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, or post-hoc lettering path was used.
- Attached inputs: exactly the same five authorized files listed above—approved Count, approved Haydée, approved Count-house, approved objects, and promoted Page 18. Page 21, Page 22 v1, every other rejected candidate, and every unlisted image were excluded.
- Issued prompt: `qa/production/page-22/prompts/page-22-v2.md` — full v1 prompt exact-prefix verified, with only the named v2 correction appended — SHA-256 `d092aa27c299a3c0002a9b58e9689698fba5052b26375d1ab74e3d4f5ccc4ae0`.
- Candidate: `qa/production/page-22/candidates/page-22-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `4317a1280f983b1423762c5d67133b1490ca7c979990cce344d5e06fb0a2cf58`.
- 600 proof: `qa/production/page-22/proofs/page-22-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `3b063710636ae590f17dcac4df884d618c84b4c1d79c7cdb9a096692297e0420`.
- 768 proof: `qa/production/page-22/proofs/page-22-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `3db1bc0867dd959db1c62143a5bad443aacc9b3d12ec003539354c6d9cdd91f9`.
- Practical audit: `qa/production/page-22/audit-v2.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 23 generation, Page 24 preparation, or story-document edit was performed.

## Promotion

- Independent verdict: `qa/production/page-22/critic-v3.md` — APPROVED
- Promoted candidate: `pages/page-22.png`
- Promoted version: v3
- SHA-256: `17cbabdaa6403bdd05b5ee3f2b9c68576e49ee7539ee0cc56c155e5038fafa98`

## Page 22 v3 execution record

- Redraw basis: full authoritative Page 22 prompt plus only the independent critic's named document-layout continuity correction. Rejected Page 22 v1/v2 evidence was preserved and excluded from generation inputs.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, or post-hoc lettering path was used.
- Attached inputs: exactly the same five authorized files listed above—approved Count, approved Haydée, approved Count-house, approved objects, and promoted Page 18. Page 21, every Page 22 rejected candidate, and every unlisted image were excluded.
- Issued prompt: `qa/production/page-22/prompts/page-22-v3.md` — full authoritative prompt exact-prefix verified, with only the named v3 correction appended — SHA-256 `ea5a1b2e55ebeebc6eb8e6d2115b8c5e0a2d162d5a32def1b99eff4cc0448b5e`.
- Candidate: `qa/production/page-22/candidates/page-22-v3.png` — 1024 × 1536 RGB PNG — SHA-256 `17cbabdaa6403bdd05b5ee3f2b9c68576e49ee7539ee0cc56c155e5038fafa98`.
- 600 proof: `qa/production/page-22/proofs/page-22-v3-600.png` — 600 × 900 RGB PNG — SHA-256 `8d0e599b7602f4444f872ae7c95d3b4d99f0a854ea99c99a5f023b4ebe859bc7`.
- 768 proof: `qa/production/page-22/proofs/page-22-v3-768.png` — 768 × 1152 RGB PNG — SHA-256 `8edb8546ce570a4783075725e0b85cf8dc030b0cca17b146eee965d6dd492b0c`.
- Practical audit: `qa/production/page-22/audit-v3.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 23 generation, Page 24 preparation, or story-document edit was performed.

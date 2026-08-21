# Page 24 v1 — manifest resolution

**Status: PROMOTED — Page 24 v2 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-24/prompts/page-24-v1.md`
- Source: current `qa/_plan/page-24.md` §5, Page 24 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `1d1fe6a6b1c3640c5837e0d2c64c7eb3e279b24a2a4579127e416f7822e9bfd6`

## Approved permanent generation inputs

1. `refs/approved/06-danglars-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `626f71c601069032624654958a24b06dfc33974d290d6c9d09d627f3f1e4beb9`
2. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`

Both permanent references resolve under `refs/approved/`. They bind the only visible characters: Baron Danglars, with full side whiskers and no moustache, and the clean-shaven Count in unrelieved black. The approved-character reference gate is satisfied.

The prompt authorizes exactly these two visual inputs, below the five-input cap. No setting, object, cast-board, adversarial-board, or page image is authorized.

## Predecessor status and prompt-specific prohibition

- `pages/page-23.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `37b9a4d7acdb2f34f5e15679c986f63a26162a022805fd948f960e702d456703`; sequence release only.
- Page 23 v2 is unconditionally approved and promoted. Page 24 generation is released.
- Even after promotion, **do not attach Page 23**. The prompt explicitly changes to a different house on a different day and requires a hard palette break from the Count's black room to Danglars' bottle-green, brass, ledger-calf and gaslight study.
- The only carried continuity is the Count's unrelieved black clothing, already bound by `refs/approved/01-count-1838.png`.
- Never substitute Page 23 candidate evidence, rejected art, any other page, or prose description as an image input.

## Content and input prohibitions

- Every other character sheet is prohibited. Do not attach Haydée, Mercédès, Fernand, Albert, Villefort, Beauchamp, any servant, clerk, woman, or crowd reference.
- Do not attach the Count-house setting, the Page 22/23 document continuity, the objects sheet, or any other setting/object sheet. Page 24 creates Danglars' study from the exact prose design in the prompt.
- The page may show only Danglars and the Count. No clerk, servant, woman, daylight, Haydée document, broken red wax seal, or legible ledger/letter/label writing is permitted.
- The Panel 5 letter is a fresh clean sheet, unsealed, with unreadable ink marks only; no red wax is present.

No image, proof, candidate, audit, critic report, Page 25 material, promotion, `pages/` write, or story-document edit was created during this preparation step.

## Page 24 v1 execution record

- Prompt verification: `qa/production/page-24/prompts/page-24-v1.md` was exact-diff verified against the current §5 Page 24 prompt before generation — SHA-256 `1d1fe6a6b1c3640c5837e0d2c64c7eb3e279b24a2a4579127e416f7822e9bfd6`.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, or post-hoc lettering path was used.
- Attached inputs: exactly the two authorized files listed above—approved Danglars and approved Count. Promoted Page 23, every setting/object sheet, every rejected candidate, and every unlisted image were excluded.
- Candidate: `qa/production/page-24/candidates/page-24-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `816195a2d2f209c64c58f151890b8c93f8d852d7f1b6947bc0603e460f333a91`.
- 600 proof: `qa/production/page-24/proofs/page-24-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `c4a48e635a88239aa25a7c6d0bfba357f1024fbcdfb906dc0576d25746266179`.
- 768 proof: `qa/production/page-24/proofs/page-24-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `86cf662fa90a6a17159f28cd19889211c77d457bf6ca2cf14654a4d8bae7a281`.
- Practical audit: `qa/production/page-24/audit-v1.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 25 work, or story-document edit was performed.

## Page 24 v2 execution record

- Redraw basis: full authoritative Page 24 prompt plus only the independent critic's named Panel 1/2 Count-first reading-order correction. Rejected Page 24 v1 evidence was preserved and excluded from generation inputs.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, or post-hoc lettering path was used.
- Attached inputs: exactly the same two authorized files—approved Danglars and approved Count. Page 24 v1, promoted Page 23, every setting/object sheet, and every unlisted image were excluded.
- Issued prompt: `qa/production/page-24/prompts/page-24-v2.md` — full authoritative prompt exact-prefix verified, with only the named v2 correction appended — SHA-256 `0418f9f350d9ac5b8960acdec2f1b7cc074efb82c556d5156441a0a1c399b232`.
- Candidate: `qa/production/page-24/candidates/page-24-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `3f71e2faeb724956cfca7880c5825b86052fc092da311c24cb2197437f9857f1`.
- 600 proof: `qa/production/page-24/proofs/page-24-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `5d4a5726f0738d3c5933b3a0928e980db238056e28219eff8c5454c6c8f6e54c`.
- 768 proof: `qa/production/page-24/proofs/page-24-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `f69a17489ab962e67d58cbcd43c31ee847ec3a84494b043030da825a0ca179d1`.
- Practical audit: `qa/production/page-24/audit-v2.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 25 generation, Page 26 preparation, or story-document edit was performed.

## Promotion

- Independent verdict: `qa/production/page-24/critic-v2.md` — APPROVED
- Promoted candidate: `pages/page-24.png`
- Promoted version: v2
- SHA-256: `3f71e2faeb724956cfca7880c5825b86052fc092da311c24cb2197437f9857f1`

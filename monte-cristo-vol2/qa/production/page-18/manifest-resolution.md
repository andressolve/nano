# Page 18 v1 — manifest resolution

**Status: PROMOTED — Page 18 v2 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-18/prompts/page-18-v1.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 18 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `d3fca803e8643b243281ba9d8917edd2c4706aeb2c5c0fdf12d036c9c31faa61`

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/05-haydee.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`
4. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

All four permanent references resolve under `refs/approved/`. They bind the two characters, the black room and lamp, and the travelling case/document with the broken red wax seal.

## Sequence predecessor and attachment binding

5. `pages/page-17.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `17bdbda7b699365d41156e16dd4d6ee2722fa2a3c84af1d9c78c06a266b2f197` — required fifth image input.

- Prompt binding: attach promoted Page 17 because Page 18 retains the same Count-house room and the same two faces/builds while moving from morning to evening.
- Do not substitute the unapproved Page 17 candidate, any rejected page art, or any other page for `pages/page-17.png`.
- The five listed inputs exactly fill the five-input cap. Every other character sheet, page image, and unlisted reference is prohibited.

Page 17 v2 is unconditionally approved and promoted byte-for-byte. Page 18 generation is released with exactly the five listed inputs.

No image, proof, candidate, audit, critic report, Page 19 material, promotion, or `pages/` write was created during this preparation step.

## Page 18 v1 execution record

- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call.
- Attached inputs: exactly the five files listed above; no rejected candidate, unlisted page, extra character sheet, API, API key, or CLI path was used.
- Issued prompt: `qa/production/page-18/prompts/page-18-v1.md` — SHA-256 `d3fca803e8643b243281ba9d8917edd2c4706aeb2c5c0fdf12d036c9c31faa61`.
- Candidate: `qa/production/page-18/candidates/page-18-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `d5692a44b6f44dda62402090a413b194fe9dbb035e01544951e4119453771c76`.
- 600 proof: `qa/production/page-18/proofs/page-18-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `a2b3444b92f79e3d73103304283caabe62a7c144d4e4315d41321f2df934a133`.
- 768 proof: `qa/production/page-18/proofs/page-18-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `bc20f609d4a98883553b445f5b7fa10d87c16a4e38a049d334448a1b7a02872b`.
- Practical audit: `qa/production/page-18/audit-v1.md` — non-gating builder report; candidate submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 19 work, or story-document edit was performed.

## Page 18 v2 execution record

- Independent v1 verdict: `REVISE` for the sole Panel 2 reading-order and speech-ownership defect recorded in `qa/production/page-18/critic-v1.md`.
- Generation route: one fresh built-in Codex/ChatGPT subscription-backed image-generation call.
- Attached inputs: exactly the same five files listed above; rejected v1 and every unlisted image were excluded. No API, API key, or CLI path was used.
- Issued prompt: `qa/production/page-18/prompts/page-18-v2.md` — full v1 prompt byte-for-byte first, followed only by the named v2 correction — SHA-256 `00b918d35d6576eb126944195ab795fdf9a8b010816b2a11143ed30c6a16a3fe`.
- Candidate: `qa/production/page-18/candidates/page-18-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `393c903f9528ca59cadbc6e25d35ceea8b8574f51540d02594ca65681287f652`.
- 600 proof: `qa/production/page-18/proofs/page-18-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `953386586a039142eab47ee938951381e390ae8e4d75b19c4bd8acb8d6d4b2c8`.
- 768 proof: `qa/production/page-18/proofs/page-18-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `81b969e60a71c429a4be31858aa50347658ee5b8100b593c0e859ce96287834f`.
- Practical audit: `qa/production/page-18/audit-v2.md` — non-gating builder report; candidate submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 19 generation, Page 20 preparation, or story-document edit was performed.

## Promotion

- Independent verdict: `qa/production/page-18/critic-v2.md` — APPROVED
- Promoted candidate: `pages/page-18.png`
- Promoted version: v2
- SHA-256: `393c903f9528ca59cadbc6e25d35ceea8b8574f51540d02594ca65681287f652`

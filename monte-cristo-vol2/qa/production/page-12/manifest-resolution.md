# Page 12 v2 — manifest resolution

**Status: PROMOTED — Page 12 v2 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-12/prompts/page-12-v2.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 12 generation prompt
- Verification: the full §5 Page 12 prompt remains byte-identical to `prompts/page-12-v1.md`, followed only by the authorized v2 Count-tail correction and preservation of critic-cleared v1 essentials
- Prompt SHA-256: `8f5ffd9117d860455b9e4d6139809712fc12b15adf59a245259d904a189a8082`

## Authorized inputs — resolved

1. `refs/approved/02-mercedes-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821`
2. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
3. `refs/approved/18-set-morcerf-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `f69809a0cc54174ed7706af8ef3c83c9dbf0b5dcf763398953f477c412971e96`
4. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`
5. `pages/page-11.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `c57e76a161c30227f120d3c3abe8a2613ecce45f860fd45ac9eb12dcc59a58fa`

## Gate result

- Approved permanent references: PASS; all four exist under `refs/approved/` with exact recorded hashes.
- Required predecessor: PASS; promoted Page 11 exists byte-for-byte with the production-lead hash.
- Input cap: PASS; exactly five image inputs, at the allowed maximum.
- Prohibited inputs: all other character sheets, rejected candidates, and unlisted images.

Page 12 v2 generation is released with exactly these five inputs through built-in Codex/ChatGPT subscription-backed image generation. Rejected Page 12 v1 and every unlisted image are prohibited generation inputs.

## Rejected v1 evidence retained

- Prompt SHA-256: `f702a125556e271b8ced572d76401160a38a4dfc78384fbb7b8578b47c2ec01e`
- Candidate: `candidates/page-12-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `db990ccb3f7f64abc20b70084eadcaa859ccf71f0fa668c1cf0becb477f611d6`
- 600 × 900 proof: `proofs/page-12-v1-600.png` — SHA-256 `6f7bc601b131baf1654cdda052abd1e19c1be954943a8955d08688551b50b448`
- 768 × 1152 proof: `proofs/page-12-v1-768.png` — SHA-256 `5ec985e274904cdb9d139a7f0bc01209b14d80fa9045ee23a3ad986d5e3ab54b`

Page 13 generation remains held.

## V2 production output evidence

- Generation: one fresh whole-page built-in subscription-backed call with exactly the five authorized inputs; rejected v1 and all unlisted images were not attached.
- Candidate: `candidates/page-12-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `179ff4a8b08b70e6985773efbbd2c1eecf27a10eb0a4c91c2e5b0b8c8e901455`
- 600 × 900 proof: `proofs/page-12-v2-600.png` — SHA-256 `206adeb31c433272b6cb66f5c95546bdbb2813ff528d9fc813e3953b9fa3df7f`
- 768 × 1152 proof: `proofs/page-12-v2-768.png` — SHA-256 `8fd6b5430f8db42c8bea030ab9fce3555026ec3fd1370ec35541462f135bf033`

## Promotion

- Independent verdict: `qa/production/page-12/critic-v2.md` — APPROVED
- Promoted candidate: `pages/page-12.png`
- Promoted version: v2
- SHA-256: `179ff4a8b08b70e6985773efbbd2c1eecf27a10eb0a4c91c2e5b0b8c8e901455`

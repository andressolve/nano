# Page 17 v1 — manifest resolution

**Status: PROMOTED — Page 17 v2 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-17/prompts/page-17-v1.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 17 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `50bcf299644365c727e7e8b7360909329c4eb93d672dd91e5dce43e7c218d5d0`

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/05-haydee.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`

All three permanent references resolve under `refs/approved/`. The permanent-reference gate is clear.

## Required earlier promoted page input

4. `pages/page-15.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `1623f14dfea5d1f173589913621014432d207d222946f8e62402ecd041a997b4`

Prompt binding: attach promoted Page 15 because Page 17 returns to the Count's house in the same flat-grey morning and requires the room's emptiness, scale, tall uncurtained windows, and cold. The resolved generation manifest therefore contains exactly four image inputs and remains within the five-input cap.

## Sequence predecessor and prohibition binding

- `pages/page-16.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `34288c500eee35dd5950ec193bd835cb4060a77401b63a8f1a2268ee05930e99` — required for sequence release only.
- Do not attach Page 16. The Page 17 prompt names Page 15 as its visual predecessor and its manifest does not authorize Page 16, which is a different house and a return to the prior party night.
- Do not substitute the Page 16 candidate, any rejected page art, or any other page for promoted Page 15.
- All other character sheets and all unlisted images are prohibited generation inputs.

Page 16 v1 is unconditionally approved and promoted byte-for-byte. Page 17 is released, but generation must still use only the three approved permanent references plus promoted Page 15; promoted Page 16 remains excluded from the image call.

## Page 17 v1 execution record

- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached inputs: exactly approved Count, approved Haydée, approved Count-house, and promoted `pages/page-15.png`.
- Excluded inputs: promoted `pages/page-16.png`, every rejected candidate, and every unlisted image.
- Issued prompt: `qa/production/page-17/prompts/page-17-v1.md` — SHA-256 `50bcf299644365c727e7e8b7360909329c4eb93d672dd91e5dce43e7c218d5d0`
- Candidate: `qa/production/page-17/candidates/page-17-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `0f89658609dc330e469a383612883966ca20ad5a00da244a7b2634ac9a20fe58`
- 600 proof: `qa/production/page-17/proofs/page-17-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `3c02e4afcf053ad842aa961651b0942ff12b6518c51f85423c7946d17e266eb9`
- 768 proof: `qa/production/page-17/proofs/page-17-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `e913b7e7f95b7a61e3e8a3699a1a34b7f894bc66a9255a1aff5e2b6bd6737890`
- Builder audit: `qa/production/page-17/audit-v1.md` — non-gating; candidate submitted unchanged to the independent critic.

No Page 18 material, promotion, or `pages/` write was created during Page 17 execution.

## Page 17 v2 execution record

- Trigger: independent critic v1 `REVISE`, correcting only the disappearance of the low black table and heavy cloak after Panel 2.
- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached inputs: exactly approved Count, approved Haydée, approved Count-house, and promoted `pages/page-15.png`.
- Excluded inputs: rejected Page 17 v1, promoted `pages/page-16.png`, every other page image, and every unlisted reference.
- Issued prompt: `qa/production/page-17/prompts/page-17-v2.md` — SHA-256 `2a597ab585aaf97c6e462f7c6878248afe04c3bc5c59679fbd48a51aea3ee4c6`
- Candidate: `qa/production/page-17/candidates/page-17-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `17bdbda7b699365d41156e16dd4d6ee2722fa2a3c84af1d9c78c06a266b2f197`
- 600 proof: `qa/production/page-17/proofs/page-17-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `9a8ce201a3670c08bfae8ec174cf20eeaa751e1b850c8512436fc0f9d9a2011d`
- 768 proof: `qa/production/page-17/proofs/page-17-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `eaa01240c709bca853a8695b9ed93fa24d2693df84cdb1645bd335308647945c`
- Builder audit: `qa/production/page-17/audit-v2.md` — non-gating; candidate submitted unchanged to the independent critic.

## Promotion

- Independent verdict: `qa/production/page-17/critic-v2.md` — APPROVED
- Promoted candidate: `pages/page-17.png`
- Promoted version: v2
- SHA-256: `17bdbda7b699365d41156e16dd4d6ee2722fa2a3c84af1d9c78c06a266b2f197`

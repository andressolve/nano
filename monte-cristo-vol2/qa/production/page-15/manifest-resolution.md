# Page 15 v1 — manifest resolution

**Status: PROMOTED — Page 15 v1 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-15/prompts/page-15-v1.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 15 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`
3. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

All three permanent references resolve under `refs/approved/`. The permanent-reference gate is clear, and the manifest remains within the five-input cap.

## Sequence predecessor and attachment binding

- `pages/page-14.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `c21649575a5148ca52510a29284dc5b7e739e4ff361d407a4a39b39998f18a6e` — required fourth image input.
- Prompt binding: attach promoted Page 14 because it carries the same Count-house room, scale, cold, and tall uncurtained windows from near dawn into full morning.
- Do not substitute the unapproved Page 14 candidate or any rejected page art for `pages/page-14.png`.
- All other character sheets and all unlisted images are prohibited generation inputs.

Page 14 v3 is unconditionally approved and promoted byte-for-byte. Page 15 generation is released with exactly the three approved permanent references and promoted Page 14.

## Page 15 v1 execution record

- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached inputs: exactly the three approved permanent references listed above plus promoted `pages/page-14.png`.
- Excluded inputs: every rejected candidate, unlisted page, and unlisted reference.
- Issued prompt: `qa/production/page-15/prompts/page-15-v1.md` — SHA-256 `ba0276aa80a725a352b79c2f57d72fdc7341977b82366f57cf726dce478d9a63`
- Candidate: `qa/production/page-15/candidates/page-15-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `1623f14dfea5d1f173589913621014432d207d222946f8e62402ecd041a997b4`
- 600 proof: `qa/production/page-15/proofs/page-15-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `977690f7a041f4f8817a990387e4c5031dc4c32558c2d036cb09b768b17c2e3e`
- 768 proof: `qa/production/page-15/proofs/page-15-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `f578368b4e70b145ec828aee24b1bf2000e140642a363fcf19a14dca55248fb6`
- Builder audit: `qa/production/page-15/audit-v1.md` — non-gating; candidate submitted unchanged to the independent critic.

## Promotion

- Independent verdict: `qa/production/page-15/critic-v1.md` — APPROVED
- Promoted candidate: `pages/page-15.png`
- Promoted version: v1
- SHA-256: `1623f14dfea5d1f173589913621014432d207d222946f8e62402ecd041a997b4`

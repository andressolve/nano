# Page 16 v1 — manifest resolution

**Status: PROMOTED — Page 16 v1 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-16/prompts/page-16-v1.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 16 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `81c235482b170c93d987b6d99b60a204e9d44e95bd5e2eb704eb1295b2bd7f43`

## Approved permanent generation inputs

1. `refs/approved/03-fernand-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `487f21e1de98136ddc16fcd7aa44d69d0fd659178de417ed282dd30486ea0a40`
2. `refs/approved/02-mercedes-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821`
3. `refs/approved/18-set-morcerf-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `f69809a0cc54174ed7706af8ef3c83c9dbf0b5dcf763398953f477c412971e96`

All three permanent references resolve under `refs/approved/`. The permanent-reference gate is clear.

## Required non-predecessor page input

4. `pages/page-13.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `d0e539deaeb6ec0300529dd7fdfc60241aa952e5cb320cc44685ffcf52d6bfca`

Prompt binding: attach promoted Page 13 because Page 16 returns to the same Morcerf-house party night and requires Mercédès' gown, dressed hair, house, and dying candle amber. The resolved generation manifest therefore contains exactly four image inputs and remains within the five-input cap.

## Sequence predecessor and explicit prohibition

- `pages/page-15.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `1623f14dfea5d1f173589913621014432d207d222946f8e62402ecd041a997b4` — required for sequence release only.
- **Do not attach Page 15.** It is a different house on a different morning and is explicitly prohibited as a Page 16 visual input.
- Do not substitute the Page 15 candidate, any rejected page art, or any other page for the required promoted Page 13 input.
- All other character sheets and all unlisted images are prohibited generation inputs.

Page 15 v1 is unconditionally approved and promoted byte-for-byte. Page 16 is released, but generation must still use only the three approved permanent references plus promoted Page 13; promoted Page 15 remains excluded from the image call.

## Page 16 v1 execution record

- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached inputs: exactly approved Fernand, approved Mercédès, approved Morcerf-house, and promoted `pages/page-13.png`.
- Excluded inputs: promoted `pages/page-15.png`, every rejected candidate, and every unlisted image.
- Issued prompt: `qa/production/page-16/prompts/page-16-v1.md` — SHA-256 `81c235482b170c93d987b6d99b60a204e9d44e95bd5e2eb704eb1295b2bd7f43`
- Candidate: `qa/production/page-16/candidates/page-16-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `34288c500eee35dd5950ec193bd835cb4060a77401b63a8f1a2268ee05930e99`
- 600 proof: `qa/production/page-16/proofs/page-16-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `dd0e6a2d2a11b54628b061eb597589cae900b130463d883dfe74a46de0867fe1`
- 768 proof: `qa/production/page-16/proofs/page-16-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `989283663a87f42c360b05cad3c8877bd1368053de26d348e8a4d980261319ff`
- Builder audit: `qa/production/page-16/audit-v1.md` — non-gating; candidate submitted unchanged to the independent critic.

## Promotion

- Independent verdict: `qa/production/page-16/critic-v1.md` — APPROVED
- Promoted candidate: `pages/page-16.png`
- Promoted version: v1
- SHA-256: `34288c500eee35dd5950ec193bd835cb4060a77401b63a8f1a2268ee05930e99`

# Page 14 v1 — manifest resolution

**Status: PROMOTED — Page 14 v3 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-14/prompts/page-14-v1.md`
- Source: current `12-PRODUCTION-PLAN.md` §5, Page 14 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/05-haydee.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`

All three permanent references resolve under `refs/approved/`. No other character, setting, object, or page image is an authorized Page 14 generation input.

## Sequence predecessor status

- `pages/page-13.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `d0e539deaeb6ec0300529dd7fdfc60241aa952e5cb320cc44685ffcf52d6bfca`

Page 13 v1 is unconditionally approved and promoted. Page 14 is released.

**Important execution binding:** do **not attach Page 13** because it is the wrong house and palette. The promoted file is a sequence-release prerequisite only, not a generation input. Use exactly the three approved permanent images above.

## Page 14 v1 execution record

- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached image inputs: exactly the three approved permanent images listed above.
- Excluded inputs: `pages/page-13.png` and every rejected candidate or unlisted reference.
- Issued prompt SHA-256: `c496219dd79adb42887ef8d42014f41fa3e66aabc231930df371670ba34ab0b2`
- Candidate: `qa/production/page-14/candidates/page-14-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `86181f92b913514511c2d76da50f048b3a92c2bdb603e849a242d2cc41e91bbc`
- 600 proof: `qa/production/page-14/proofs/page-14-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `c116a30feccfdf8fd0b9907c24828a97d1681c295ace9f8a50a981da12c9fbdb`
- 768 proof: `qa/production/page-14/proofs/page-14-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `024ad63d965011f838bcfc2e1f2ddf07c35d92417141e77e3c929479d496e4d5`
- Builder audit: `qa/production/page-14/audit-v1.md` — non-gating; candidate submitted unchanged to the independent critic.

## Page 14 v2 execution record

- Trigger: independent critic v1 `REVISE`, correcting only the Count-house fireplace orientation and locked three-roof/window exterior aspect.
- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached image inputs: exactly approved `refs/approved/01-count-1838.png`, `refs/approved/05-haydee.png`, and `refs/approved/17-set-count-house.png`.
- Excluded inputs: rejected Page 14 v1, `pages/page-13.png`, every other page image, and every unlisted reference.
- Issued prompt: `qa/production/page-14/prompts/page-14-v2.md` — SHA-256 `0822109ce5c286492c4031df13ce2357684d617939f2e1fe2295ea88b4502ed6`
- Candidate: `qa/production/page-14/candidates/page-14-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `eae59545e3a7fc98d86482106d9926346edea03d2ffa2bef7c1b945183adf68d`
- 600 proof: `qa/production/page-14/proofs/page-14-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `9c77148dc0e2a872e2cebab7d9b20403df7e0d0102e5cfc70a0d5c299b2a00e7`
- 768 proof: `qa/production/page-14/proofs/page-14-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `8bc0148bd939578117c45b4c1a9240aa2d8310028ce8788faa726df5697d7a7b`
- Builder audit: `qa/production/page-14/audit-v2.md` — non-gating; candidate submitted unchanged to the independent critic.

## Page 14 v3 execution record

- Trigger: independent critic v2 `REVISE`, correcting only the missing third warm exterior cue and the premature complete back-turn in Panel 3.
- Generation path: one built-in Codex/ChatGPT subscription-backed image-generation call; no API, CLI, API key, prototype, patch, or post-hoc lettering.
- Attached image inputs: exactly approved `refs/approved/01-count-1838.png`, `refs/approved/05-haydee.png`, and `refs/approved/17-set-count-house.png`.
- Excluded inputs: rejected Page 14 v1/v2, every page image, and every unlisted reference.
- Issued prompt: `qa/production/page-14/prompts/page-14-v3.md` — SHA-256 `269c2068e2ef4bb5f34c4b1ac672331e5bd899991edc570dc54855aea4439370`
- Candidate: `qa/production/page-14/candidates/page-14-v3.png` — 1024 × 1536 RGB PNG — SHA-256 `c21649575a5148ca52510a29284dc5b7e739e4ff361d407a4a39b39998f18a6e`
- 600 proof: `qa/production/page-14/proofs/page-14-v3-600.png` — 600 × 900 RGB PNG — SHA-256 `818ae4e66b5366df17ab2bfd0fa7f6c0a48dfb4e0390c5d2532a425e428248a4`
- 768 proof: `qa/production/page-14/proofs/page-14-v3-768.png` — 768 × 1152 RGB PNG — SHA-256 `6a63024e287b4fd030a40568ec219693540a0aac73233470af9b36bc0aac8c8e`
- Builder audit: `qa/production/page-14/audit-v3.md` — non-gating; candidate submitted unchanged to the independent critic.

## Promotion

- Independent verdict: `qa/production/page-14/critic-v3.md` — APPROVED
- Promoted candidate: `pages/page-14.png`
- Promoted version: v3
- SHA-256: `c21649575a5148ca52510a29284dc5b7e739e4ff361d407a4a39b39998f18a6e`

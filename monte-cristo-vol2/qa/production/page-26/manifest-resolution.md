# Page 26 v1 — manifest resolution

**Status: PROMOTED — Page 26 v2 independently approved**

## Prompt verification

- Prepared prompt: `qa/production/page-26/prompts/page-26-v1.md`
- Source: current `qa/_plan/page-26.md` §5, Page 26 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `34dc576cc3b309b652d2e15834aadb9714e25469a0ad2e7ee1066783ccc4a7d6`

## Approved permanent generation inputs

1. `refs/approved/01-count-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0`
2. `refs/approved/04-albert.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `3ff9d03308e7f79d5b217f90e8437067a8e407c0f3347902a87db4fb0f54dbee`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`
4. `refs/approved/18-set-morcerf-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `f69809a0cc54174ed7706af8ef3c83c9dbf0b5dcf763398953f477c412971e96`
5. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

The approved-reference gate is satisfied for both visible named characters: the Count is bound by approved Sheet 01 and Albert by approved Sheet 04. The Count-house and Morcerf-house settings and the folded 1838 Paris newspaper are likewise bound by approved permanent references. These five files exactly fill the five-input cap.

## Required predecessor and sequential hold

- `pages/page-25.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `f56bd2e1d087d54638456d38391a08b3434f530b4060a76dde4e222bfdbe484d` — sequence-status prerequisite only.
- Page 25 v1 is unconditionally approved and promoted. Page 26 generation is released.
- Page 25 is a sequence-status prerequisite only, not a Page 26 generation input. The current Page 26 manifest authorizes exactly the five approved permanent inputs above and already fills the input cap. Even after promotion, **do not attach `pages/page-25.png`**.
- The prompt explicitly says **do not attach Page 24**. Do not attach `pages/page-24.png`, Page 25 candidate evidence, any rejected art, any other page image, or a prose substitute for an approved image input.

## Attach and prohibit bindings

- Attach exactly the five approved files listed above, in that order, if Page 26 is later released.
- All other character sheets and character-bearing boards are prohibited generation inputs. Do not attach Danglars, Haydée, Mercédès, Fernand, Villefort, Beauchamp, a clerk, a servant, a crowd, the head board, silhouette board, live-pair proof, or any adversarial board.
- Do not attach any unlisted setting, object, Janina, Chamber, carrier, page, candidate, proof, or rejected image.
- The Count is the only figure in Panel 1; Albert is the only figure in Panel 3; they never share a panel. Panel 2 contains no figure. No servant, clerk, crowd, or additional person may appear.
- The same physical folded newspaper must recur across all three panels with the same fold, crease, and column layout. The approved objects sheet is the sole object reference.
- Text is limited to the exact Panel 1 Count balloon and the exact single readable newspaper paragraph in Panel 2. Panel 3 is silent. No readable headline, masthead, dateline, byline, price, adjoining article, room label, or other pseudo-text is allowed.
- The Count-house dawn palette and Morcerf breakfast-room palette must remain distinct. Do not import Danglars' green-and-brass Page 25 palette or Page 24 palette.

No image, proof, candidate, audit, critic report, Page 27 material, promotion, `pages/` write, or story-document edit was created during this preparation step.

## Page 26 v1 execution record

- Prompt verification: `qa/production/page-26/prompts/page-26-v1.md` was exact-diff verified against the current §5 Page 26 prompt before generation — SHA-256 `34dc576cc3b309b652d2e15834aadb9714e25469a0ad2e7ee1066783ccc4a7d6`.
- Sequence release: promoted `pages/page-25.png` exists as a sequence prerequisite — 1024 × 1536 RGB PNG — SHA-256 `f56bd2e1d087d54638456d38391a08b3434f530b4060a76dde4e222bfdbe484d`. It was not attached.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or rejected candidate was used.
- Attached inputs: exactly the five authorized approved permanent files listed above, in manifest order. Neither Page 25 nor Page 24 nor any other image was attached.
- Candidate: `qa/production/page-26/candidates/page-26-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `2098463328babe194b85faf16591e481846dd334810883746c33e2bcf52d1c4b`.
- 600 proof: `qa/production/page-26/proofs/page-26-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `9f1a2ed8b78c782a25b81165304c7e347432323c539cf6b98cd84119c29afc31`.
- 768 proof: `qa/production/page-26/proofs/page-26-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `6db48547fd05d4e2c467a0acf3847d415542c53bae2df48a6cf997796378ef45`.
- Practical audit: `qa/production/page-26/audit-v1.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 27 work, or story-document edit was performed.

## Page 26 v2 execution record

- Critic basis: `qa/production/page-26/critic-v1.md` returned `REVISE` for Albert's incorrect light morning coat in Panel 3 and named no other mandatory defect.
- Issued prompt: `qa/production/page-26/prompts/page-26-v2.md` contains the full exact Page 26 prompt plus only the named dark-navy-tailcoat correction and preservation clause — SHA-256 `9eea2130c5fbd7f95dc766e378e58e123543222925b52871d4f8403cc4feb851`.
- Generation route: one fresh built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or edit operation was used.
- Attached inputs: exactly the same five authorized approved permanent files listed above, in manifest order. Rejected v1, Pages 24–25, and every other image were excluded.
- Rejected v1 remains preserved byte-for-byte at `qa/production/page-26/candidates/page-26-v1.png` — SHA-256 `2098463328babe194b85faf16591e481846dd334810883746c33e2bcf52d1c4b`.
- Candidate: `qa/production/page-26/candidates/page-26-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `8308e7499b2eb076c2f1837d58afd77e71651885f8f888bd19bedf3c59e4bf2f`.
- 600 proof: `qa/production/page-26/proofs/page-26-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `88dd720570c0e0cca2875f52cf771fa20732cf265e74061a27fb263c330f1a97`.
- 768 proof: `qa/production/page-26/proofs/page-26-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `efbf6d4a4c4baa96be7d42809aec38f65e5dfce659f6d759af2651ebab6a08e5`.
- Practical audit: `qa/production/page-26/audit-v2.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 27 generation, Page 28 preparation, or story-document edit was performed.

## Promotion

- Independent verdict: `qa/production/page-26/critic-v2.md` — APPROVED
- Promoted candidate: `pages/page-26.png`
- Promoted version: v2
- SHA-256: `8308e7499b2eb076c2f1837d58afd77e71651885f8f888bd19bedf3c59e4bf2f`

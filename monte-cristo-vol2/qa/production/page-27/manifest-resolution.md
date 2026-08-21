# Page 27 v1 — manifest resolution

**Status: PROMOTED — Page 27 v4 unconditionally approved and promoted byte-for-byte**

## Prompt verification

- Prepared prompt: `qa/production/page-27/prompts/page-27-v1.md`
- Source: current `qa/_plan/page-27.md` §5, Page 27 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `bfe046ff4acdb7b84c7349bfba1ea1dbb48b143d2ba40f49ad4f1c58a59d36e3`

## Approved permanent generation inputs

1. `refs/approved/04-albert.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `3ff9d03308e7f79d5b217f90e8437067a8e407c0f3347902a87db4fb0f54dbee`
2. `refs/approved/07-beauchamp.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `58ba63bf5b77fdf31c585da888461c143474c750d0fa8b2bf7cdab218f38d834`

The approved-reference gate is satisfied for both visible named characters. Albert is bound by approved Sheet 04 and Beauchamp by approved Sheet 07. Their four required collision separators are explicit in both the prompt and approved locks: chestnut versus sandy hair; no spectacles versus small oval spectacles; bright pale versus dull dark costume values; upright versus stooped posture.

## Required predecessor and sequential hold

3. `pages/page-26.png` — PROMOTED — 1024 × 1536 RGB PNG — SHA-256 `8308e7499b2eb076c2f1837d58afd77e71651885f8f888bd19bedf3c59e4bf2f` — required third input.

- Page 26 v2 is unconditionally approved and promoted. Page 27 generation is released.
- After release, attach the promoted `pages/page-26.png` as the required third input. It binds Albert's unchanged, now-creased previous-evening clothing and the same edition of the newspaper, including its fold and crease.
- Before generation, resolve and record the promoted Page 26 dimensions and SHA-256. Never substitute Page 26 candidate evidence, a rejected candidate, another page, or prose description for the required promoted predecessor.
- The two approved character sheets plus promoted Page 26 will use three inputs, below the five-input cap.

## Attach and prohibit bindings

- If released, attach exactly these three files in manifest order: approved Albert, approved Beauchamp, and promoted Page 26. Attach no other image.
- All other character sheets and character-bearing boards are prohibited generation inputs. Do not attach the Count, Haydée, Mercédès, Fernand, Danglars, Villefort, any woman, servant, printer, clerk, crowd, head board, silhouette board, live-pair proof, or adversarial board.
- Do not attach any setting, object, newspaper, carrier, candidate, proof, rejected art, Page 25, or other page image. The approved predecessor alone supplies the newspaper and clothing continuity.
- Albert remains on the left of every panel and Beauchamp on the right. The two are the only named figures and must remain separated by hair color, spectacles, costume value, and posture in every panel. Beauchamp's spectacles come off only in Panel 3 and remain visible in his hand.
- Optional far printers are prose-constrained background shapes only, with no faces or balloons, and receive no reference image. They may be omitted.
- The same Page 26 newspaper remains on the table with the same fold and crease, but it and every proof or paper in the room carry no legible print.
- The press room stays the volume's uniquely poor room: ink black, newsprint grey, tallow, bare board, dirty-window light, paper, press furniture, and worn wool. No gilt, burgundy, polish, candle amber, lacquer, or imported luxury setting palette.
- Exactly four panels and thirteen balloons are specified. Preserve the exact order, ownership, left/right staging, Panel 3's genuine offer, and dominant Panel 4 refusal with Albert standing and both hands flat on the table.

No image, proof, candidate, audit, critic report, Page 28 material, promotion, `pages/` write, or story-document edit was created during this preparation step.

## Page 27 v1 execution record

- Prompt verification: `qa/production/page-27/prompts/page-27-v1.md` was exact-diff verified against the current §5 Page 27 prompt before generation — SHA-256 `bfe046ff4acdb7b84c7349bfba1ea1dbb48b143d2ba40f49ad4f1c58a59d36e3`.
- Sequence release: promoted `pages/page-26.png` exists and matches the released predecessor — 1024 × 1536 RGB PNG — SHA-256 `8308e7499b2eb076c2f1837d58afd77e71651885f8f888bd19bedf3c59e4bf2f`.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or rejected candidate was used.
- Attached inputs: exactly the three authorized files in manifest order—approved Albert, approved Beauchamp, and promoted Page 26. No setting, object, extra character, other page, candidate, proof, or rejected image was attached.
- Candidate: `qa/production/page-27/candidates/page-27-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `2dcf74a518fe64cb501a806152d0120a90b277aaf1625efc6270da8a9ee0458b`.
- 600 proof: `qa/production/page-27/proofs/page-27-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `2f8cdcfcbaf9a4d5dab8fe7ebddc40eb70a7090bbc5d05cdcaf353b187667c04`.
- 768 proof: `qa/production/page-27/proofs/page-27-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `43f511fdd611af48973353dd9d6b7204e433d317982e424197fd116c5bbed05c`.
- Practical audit: `qa/production/page-27/audit-v1.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 28 work, or story-document edit was performed.

## Page 27 v2 execution record

- Critic basis: `qa/production/page-27/critic-v1.md` returned `REVISE` solely for the unauthorized duplicate `You may not like what I bring back.` balloon in dominant Panel 4.
- Issued prompt: `qa/production/page-27/prompts/page-27-v2.md` contains the full exact Page 27 prompt plus only the named thirteen-balloon/single-Beauchamp-line correction and preservation clause — SHA-256 `6f641b03c60776746247e1fa612bd2075cebb874238bf867b7c6607fa594eee5`.
- Generation route: one fresh built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or edit operation was used.
- Attached inputs: exactly the same three authorized files—approved Albert, approved Beauchamp, and promoted Page 26. Rejected v1 and every other image were excluded.
- Rejected v1 remains preserved byte-for-byte at `qa/production/page-27/candidates/page-27-v1.png` — SHA-256 `2dcf74a518fe64cb501a806152d0120a90b277aaf1625efc6270da8a9ee0458b`.
- Candidate: `qa/production/page-27/candidates/page-27-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `272a879bf8b5bbcb7fbdaba4b6087fae1e577a147eac70ffb31d2bd405cfdaea`.
- 600 proof: `qa/production/page-27/proofs/page-27-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `37131f0aa4e36c19160705bc7c9258fe69608162fa97f8d8c8afbf4e9326ab53`.
- 768 proof: `qa/production/page-27/proofs/page-27-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `086a77679d56a63505374cb14bcba7de2f7806cdca249581bc01fc61d7b47115`.
- Practical audit: `qa/production/page-27/audit-v2.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 28 generation, Page 29 preparation, or story-document edit was performed.

## Page 27 v4 execution record

- Critic basis: `qa/production/page-27/critic-v3.md` returned `REVISE` solely because Beauchamp wore one pair of spectacles while holding a duplicate pair in Panel 3, with the duplicated state continuing into Panel 4.
- Attempt ceiling: v4 is the final authorized existing-composition attempt. No v5, redesign, or split was performed; a later v4 `REVISE` requires an owner stop.
- Issued prompt: `qa/production/page-27/prompts/page-27-v4.md` contains the full exact Page 27 prompt plus only the named bare-face/sole-held-pair correction and preservation clause — SHA-256 `b8d12319eff38d931fb9e658190f5659046a4871e3e2095530247f617231535c`.
- Generation route: one fresh built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or edit operation was used.
- Attached inputs: exactly the same three authorized files—approved Albert, approved Beauchamp, and promoted Page 26. Rejected v1–v3 and every other image were excluded.
- Rejected v1 remains preserved at `qa/production/page-27/candidates/page-27-v1.png` — SHA-256 `2dcf74a518fe64cb501a806152d0120a90b277aaf1625efc6270da8a9ee0458b`.
- Rejected v2 remains preserved at `qa/production/page-27/candidates/page-27-v2.png` — SHA-256 `272a879bf8b5bbcb7fbdaba4b6087fae1e577a147eac70ffb31d2bd405cfdaea`.
- Rejected v3 remains preserved at `qa/production/page-27/candidates/page-27-v3.png` — SHA-256 `9041fe8e2a693cdc5e9790af42743a593a4141ef8b068dc44c229bd8c1f4f509`.
- Candidate: `qa/production/page-27/candidates/page-27-v4.png` — 1024 × 1536 RGB PNG — SHA-256 `dcd32558ed34b372e578865c12f8d2aa51610c61c9def8ae4abd1ae3ecbba030`.
- 600 proof: `qa/production/page-27/proofs/page-27-v4-600.png` — 600 × 900 RGB PNG — SHA-256 `c555c32afa0b1e0e6a686c94ed7307479a65f59823e2737c5f4eaaf96cad5811`.
- 768 proof: `qa/production/page-27/proofs/page-27-v4-768.png` — 768 × 1152 RGB PNG — SHA-256 `7581e4337a3a7afcfaee98e4a8196251ab14844570f61e20fc084b1b59659aa7`.
- Practical audit: `qa/production/page-27/audit-v4.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 28 generation, Page 29 preparation, story-document edit, v5, redesign, or split was performed.

## Page 27 promotion record

- Independent critic: `qa/production/page-27/critic-v4.md` — `APPROVED` after blind transcription of all thirteen strings and named verification of the sole held spectacles pair, corrected reading order, identity separation, newspaper/room continuity, anatomy, register, and canvas.
- Promoted candidate: `pages/page-27.png` — byte-for-byte copy of `qa/production/page-27/candidates/page-27-v4.png` — 1024 × 1536 RGB PNG — SHA-256 `dcd32558ed34b372e578865c12f8d2aa51610c61c9def8ae4abd1ae3ecbba030`.
- Promoted 600 proof: `qa/production/page-27/proofs/page-27-promoted-600.png` — byte-for-byte copy of `qa/production/page-27/proofs/page-27-v4-600.png` — SHA-256 `c555c32afa0b1e0e6a686c94ed7307479a65f59823e2737c5f4eaaf96cad5811`.
- Promoted 768 proof: `qa/production/page-27/proofs/page-27-promoted-768.png` — byte-for-byte copy of `qa/production/page-27/proofs/page-27-v4-768.png` — SHA-256 `7581e4337a3a7afcfaee98e4a8196251ab14844570f61e20fc084b1b59659aa7`.
- Page 28 sequence hold is cleared. Page 27 remains a sequence-status prerequisite only and must not be attached to Page 28 generation.

## Page 27 v3 execution record

- Critic basis: `qa/production/page-27/critic-v2.md` returned `REVISE` solely because dominant Panel 4 placed Beauchamp's warning before Albert's `Go and find out.` at first read.
- Issued prompt: `qa/production/page-27/prompts/page-27-v3.md` contains the full exact Page 27 prompt plus only the named dominant-panel reading-order correction and preservation clause — SHA-256 `bbbfe6e9adfcf73737a6fab45700cafd8c3b5c581419cdd593a01c9563f763e3`.
- Generation route: one fresh built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or edit operation was used.
- Attached inputs: exactly the same three authorized files—approved Albert, approved Beauchamp, and promoted Page 26. Rejected v1/v2 and every other image were excluded.
- Rejected v1 remains preserved at `qa/production/page-27/candidates/page-27-v1.png` — SHA-256 `2dcf74a518fe64cb501a806152d0120a90b277aaf1625efc6270da8a9ee0458b`.
- Rejected v2 remains preserved at `qa/production/page-27/candidates/page-27-v2.png` — SHA-256 `272a879bf8b5bbcb7fbdaba4b6087fae1e577a147eac70ffb31d2bd405cfdaea`.
- Candidate: `qa/production/page-27/candidates/page-27-v3.png` — 1024 × 1536 RGB PNG — SHA-256 `9041fe8e2a693cdc5e9790af42743a593a4141ef8b068dc44c229bd8c1f4f509`.
- 600 proof: `qa/production/page-27/proofs/page-27-v3-600.png` — 600 × 900 RGB PNG — SHA-256 `d5f48643db7400930e7781bca1ab4cc1970d844a92f72e7aaf0581740faddce7`.
- 768 proof: `qa/production/page-27/proofs/page-27-v3-768.png` — 768 × 1152 RGB PNG — SHA-256 `7b61da78fe23f75b37516e78da900a586126b6a5ba63a2fca7841aea55b58c52`.
- Practical audit: `qa/production/page-27/audit-v3.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 28 generation, Page 29 preparation, or story-document edit was performed.

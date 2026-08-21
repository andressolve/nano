# Page 29 v1 — manifest resolution

**Status: PROMOTED — Page 29 v3 independently approved and supersedes promoted v1**

## Prompt verification

- Prepared prompt: `qa/production/page-29/prompts/page-29-v1.md`
- Source: current `qa/_plan/page-29.md` §5, Page 29 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `461f1e02f74570d68c86bdc8742c5fd792e03bb930e94ee844f2e349679ca45d`

## Approved permanent generation inputs

1. `refs/approved/07-beauchamp.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `58ba63bf5b77fdf31c585da888461c143474c750d0fa8b2bf7cdab218f38d834`
2. `refs/approved/20-set-janina.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `131af9dc496660cdaee9dbded4bfe85a09e81d8b1fb39a1b45da543fc6a3c77f`
3. `refs/approved/17-set-count-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `7e1c690b5772a8607589b62ac57e7e8de10026bf59cca4c34260065a0c800c93`
4. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

The approved-reference gate is satisfied for Beauchamp, the only visible named character, by approved Sheet 07. The old Greek man is an explicitly fresh, prose-constrained minor character with no reference sheet. Panel 3 contains no face or visible named character—only two pale hands, the recurring newspaper, lamp, table, and locked Count-house setting—so no Count character sheet is authorized or required. The four approved permanent inputs remain below the five-input cap.

## Required predecessor and sequential hold

- `pages/page-28.png` — **PROMOTED** — 1024 × 1536 RGB PNG — SHA-256 `fa80a1f71f5f0796c6f0d6f93a897541529d8e45504d3750e0f5706985d77318`.
- Page 28 v1 is unconditionally approved and promoted byte-for-byte. Page 29 generation is explicitly released.
- Page 28 is sequence status only, never a Page 29 image input. The Page 29 prompt specifies a hard cut to a different room and country and explicitly says **do not attach the previous page**. After Page 28 is promoted, record its canonical path and SHA-256 here for release verification, but still do not attach it.
- Do not substitute Page 28 candidate evidence, rejected art, Page 26, or any other page for an authorized permanent reference.

## Attach and prohibit bindings

- On release, attach exactly the four approved permanent files listed above, in that order. Attach no predecessor or other page image.
- All other character sheets are prohibited generation inputs. In particular, do not attach the Count, Albert, Mercédès, Fernand, Haydée, Danglars, Villefort, any adversarial/cast board, an invented old-man reference, or any crowd reference.
- Do not attach any unlisted setting, object, carrier, candidate, proof, rejected image, or prose substitute. Approved Sheet 20 binds Janina, approved Sheet 17 binds the Count's black room, and approved Sheet 21 binds the newspaper.
- Panels 1–2 are unmistakably Janina under hard high southern light, with no Paris architecture, fire, soldiers, weapons, or crowd. Beauchamp retains his stoop, same Paris coat, notebook, and small oval spectacles in every panel where he appears.
- The old Greek man is approximately seventy, locally dressed, fresh and prose-constrained, and must not collide with any principal identity. The surrounding men remain only the few indifferent local men specified by the prompt, never a crowd.
- Panel 3 shows no face at all: only two long pale hands, damp newspaper, lamp, low black table, and the locked airless black room. `JANINA` may appear once as the newspaper headline; all other print is unreadable type texture. No sky or fire appears in Panel 3.
- Exactly three panels and seven text blocks are specified: two prose fields carrying three paragraphs total, followed by four balloons in the exact scripted order and ownership. Preserve all exact strings, attribution, panel hierarchy, and the Janina-to-Paris palette collision.

No Page 29 image, proof, candidate, audit, critic report, promotion, `pages/` write, Page 30 material, or story-document edit was created during preparation. On release, Page 29 must use exactly the four approved permanent inputs listed above and must not attach promoted Page 28.

## Page 29 v1 execution record

- Prompt verification: `qa/production/page-29/prompts/page-29-v1.md` was exact-diff verified against the current `qa/_plan/page-29.md` §5 prompt after blockquote stripping immediately before generation — SHA-256 `461f1e02f74570d68c86bdc8742c5fd792e03bb930e94ee844f2e349679ca45d`.
- Sequence release: promoted `pages/page-28.png` exists and matches the released predecessor — 1024 × 1536 RGB PNG — SHA-256 `fa80a1f71f5f0796c6f0d6f93a897541529d8e45504d3750e0f5706985d77318`. It was not attached.
- Generation route: exactly one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or rejected candidate was used.
- Attached inputs: exactly the four approved permanent files listed above, in manifest order. Page 28, the Count character sheet, an invented old-man reference, and every other image were excluded.
- Candidate: `qa/production/page-29/candidates/page-29-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `844f78b72d9b6437bac6b2c1accf0dd84fd5fa8165929d70c908ecb20ea218c2`.
- 600 proof: `qa/production/page-29/proofs/page-29-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `a10f41fb4227a9ebd5a58f56ec84314f709e6d68e85942d14d69daea763b07fc`.
- 768 proof: `qa/production/page-29/proofs/page-29-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `df1fb290ec5a2f2d7ebc0dcea5ae207837e1d0c6c8f3ffddfaee9936eed80d96`.
- Practical audit: `qa/production/page-29/audit-v1.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 30 preparation or generation, or story-document edit was performed.

## Page 29 v2 batch-correction execution record

- Batch correction authority: `qa/batches/batch-21-30.md` returned `REVISE` because promoted Page 29 replaced Page 26's transparent-chimney lamp with a black-shaded lamp and introduced an unscheduled decanter/tumbler. `qa/batches/batch-21-30-owner-tolerance.md` explicitly left this Page 29 defect mandatory while resolving only the separate rhythm finding.
- Issued prompt: `qa/production/page-29/prompts/page-29-v2.md` — the complete exact Page 29 prompt plus only the lamp/vessel correction and explicit Page29 critic-v1 preservation clause — SHA-256 `b4d80a4cdfeaeeab7e015dd62c8fd121d9a5850f910d9c94f29c8a678e7e25c7`.
- Generation route: exactly one fresh whole-page built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, patch, post-hoc lettering, or rejected/promoted candidate was used.
- Attached inputs: exactly the same four approved permanent files listed above, in manifest order. Page 26, promoted/rejected v1, Pages 28/30, and every other image were excluded.
- Preserved v1 evidence and canonical page: `qa/production/page-29/candidates/page-29-v1.png` and `pages/page-29.png` both remain byte-for-byte SHA-256 `844f78b72d9b6437bac6b2c1accf0dd84fd5fa8165929d70c908ecb20ea218c2`. Canonical Page 29 is not replaced unless v2 receives independent unconditional approval and the production lead promotes it.
- V2 candidate: `qa/production/page-29/candidates/page-29-v2.png` — 1024 × 1536 RGB PNG — SHA-256 `877342d0afa7ef3cf5099bec4fbdbc88b5e27198e5039ad5cac6c7c293e7b73d`.
- 600 proof: `qa/production/page-29/proofs/page-29-v2-600.png` — 600 × 900 RGB PNG — SHA-256 `3ccf56125de74975cf9b802fcdbf6bb631abcb2ce212ef7a73fa9bfca99aaf88`.
- 768 proof: `qa/production/page-29/proofs/page-29-v2-768.png` — 768 × 1152 RGB PNG — SHA-256 `28dd0504a5b7b4bf5f8a274bec26d3fee0e9a8b2681e58208940dea502a11812`.
- Practical audit: `qa/production/page-29/audit-v2.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, canonical `pages/` replacement, Page 31 generation, or story-document edit was performed.

## Page 29 v3 critic-correction execution record

- Independent correction authority: `qa/production/page-29/critic-v2.md` returned `REVISE` for one defect only: Panel 2 did not enforce the required old man / Beauchamp / old man first-read order without a backward crossing.
- Issued prompt: `qa/production/page-29/prompts/page-29-v3.md` — the complete exact Page 29 prompt plus only the Panel 2 descending-tier correction and explicit preservation clause — SHA-256 `c975bd590fc0b05b34209954bcd53637f697e785645897b6757afa20850d8696`.
- Generation route: exactly one fresh whole-page built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, patch, post-hoc lettering, or rejected/promoted candidate was used.
- Attached inputs: exactly the same four approved permanent files listed above, in manifest order. Page 26, Page 29 v1/v2, every page image, and every other reference were excluded.
- Preserved evidence and canonical page: v1 remains at SHA-256 `844f78b72d9b6437bac6b2c1accf0dd84fd5fa8165929d70c908ecb20ea218c2`; v2 remains at SHA-256 `877342d0afa7ef3cf5099bec4fbdbc88b5e27198e5039ad5cac6c7c293e7b73d`. Canonical `pages/page-29.png` remains the promoted v1 byte sequence unless v3 receives independent unconditional approval and the production lead promotes it.
- V3 candidate: `qa/production/page-29/candidates/page-29-v3.png` — 1024 × 1536 RGB PNG — SHA-256 `8232916ad3d850a9ebfe53ceb4cbdbdf4884966d2e202a43dcc65be66931d413`.
- 600 proof: `qa/production/page-29/proofs/page-29-v3-600.png` — 600 × 900 RGB PNG — SHA-256 `d28218186cbcae6e6b83eea32fad587846ff088f83da43133ad003dab7fa28c2`.
- 768 proof: `qa/production/page-29/proofs/page-29-v3-768.png` — 768 × 1152 RGB PNG — SHA-256 `5b9311fa553e5cdeb9c8ac11d5e466497788c5db76276c72b6c46505ff11e85a`.
- Practical audit: `qa/production/page-29/audit-v3.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, canonical `pages/` replacement, Page 31 generation, or story-document edit was performed.

## Page 29 promotion record

- Independent critic: `qa/production/page-29/critic-v1.md` — `APPROVED` after blind transcription of all seven text blocks and verification of the Janina/Paris cut, unburned town, Beauchamp lock, old-man separation, faceless black-room coda, prose-field count, and newspaper print limits.
- Promoted candidate: `pages/page-29.png` — byte-for-byte copy of `qa/production/page-29/candidates/page-29-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `844f78b72d9b6437bac6b2c1accf0dd84fd5fa8165929d70c908ecb20ea218c2`.
- Promoted 600 proof: `qa/production/page-29/proofs/page-29-promoted-600.png` — byte-for-byte copy of `qa/production/page-29/proofs/page-29-v1-600.png` — SHA-256 `a10f41fb4227a9ebd5a58f56ec84314f709e6d68e85942d14d69daea763b07fc`.
- Promoted 768 proof: `qa/production/page-29/proofs/page-29-promoted-768.png` — byte-for-byte copy of `qa/production/page-29/proofs/page-29-v1-768.png` — SHA-256 `df1fb290ec5a2f2d7ebc0dcea5ae207837e1d0c6c8f3ffddfaee9936eed80d96`.
- Page 30 clears the sequence prerequisite but remains on pre-generation HOLD for the unresolved internal speaker-count contradiction recorded in its manifest.

## Pages 21–30 batch correction authority

- Batch report: `qa/batches/batch-21-30.md` returned `REVISE` for Page 29's Count-house coda continuity. The coda substituted a black-shaded desk lamp for Page 26's transparent-chimney oil lamp and added an unscheduled decanter/tumbler.
- Authorized v2 correction: one fresh whole-page redraw from the exact v1 manifest inputs. In Panel 3 restore the simple transparent-glass-chimney oil lamp beside the hands/newspaper and remove every decanter, bottle, tumbler, wine glass, or drinking vessel.
- Preservation: all critic-v1-passed text, Janina fields, Beauchamp/old-man identities, old-man–Beauchamp–old-man ownership, faceless reader, `JANINA` print limit, palette collision, anatomy, register, and canvas remain mandatory.
- V1 and Page 26 are evidence only and must not be attached. The v2 call must use exactly the same four approved permanent references as v1.
- Page 29 v1 remains the current promoted byte sequence until an independently approved v2 supersedes it. Page 31 and milestone release remain held.

## Page 29 v3 superseding promotion record

- Independent critic: `qa/production/page-29/critic-v3.md` — `APPROVED` after blind transcription and verification of the old man / Beauchamp / old man order, restored transparent-chimney Page 26 lamp rhyme, absent drinkware, all Page 29 appendix items, anatomy, register, and canvas.
- Superseded canonical v1 remains preserved at `qa/production/page-29/candidates/page-29-v1.png` — SHA-256 `844f78b72d9b6437bac6b2c1accf0dd84fd5fa8165929d70c908ecb20ea218c2`.
- Promoted replacement: `pages/page-29.png` — byte-for-byte copy of `qa/production/page-29/candidates/page-29-v3.png` — 1024 × 1536 RGB PNG — SHA-256 `8232916ad3d850a9ebfe53ceb4cbdbdf4884966d2e202a43dcc65be66931d413`.
- Promoted 600 proof: `qa/production/page-29/proofs/page-29-promoted-600.png` — byte-for-byte copy of `qa/production/page-29/proofs/page-29-v3-600.png` — SHA-256 `d28218186cbcae6e6b83eea32fad587846ff088f83da43133ad003dab7fa28c2`.
- Promoted 768 proof: `qa/production/page-29/proofs/page-29-promoted-768.png` — byte-for-byte copy of `qa/production/page-29/proofs/page-29-v3-768.png` — SHA-256 `5b9311fa553e5cdeb9c8ac11d5e466497788c5db76276c72b6c46505ff11e85a`.
- Page 30 remains canonical and unchanged because Page 29 was sequence-only and explicitly excluded from Page 30's generation inputs. Pages 21–30 milestone gates must rerun before Page 31 release.

# Page 28 v1 — manifest resolution

**Status: PROMOTED — Page 28 v1 unconditionally approved and promoted byte-for-byte**

## Prompt verification

- Prepared prompt: `qa/production/page-28/prompts/page-28-v1.md`
- Source: current `qa/_plan/page-28.md` §5, Page 28 generation prompt
- Verification: exact diff match after removing Markdown blockquote markers only
- Prompt SHA-256: `602c3450f862011c15dabe92f4f972afaf8a502202d2242ecb8ca0d9921d4dc6`

## Approved permanent generation inputs

1. `refs/approved/03-fernand-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `487f21e1de98136ddc16fcd7aa44d69d0fd659178de417ed282dd30486ea0a40`
2. `refs/approved/02-mercedes-1838.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821`
3. `refs/approved/18-set-morcerf-house.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `f69809a0cc54174ed7706af8ef3c83c9dbf0b5dcf763398953f477c412971e96`
4. `refs/approved/21-objects.png` — EXISTS — 1536 × 1024 RGB PNG — SHA-256 `1013330cd03e6e748cad7cb1a45671e042ee46bf1f7fe5b9d5d07634406e849a`

The approved-reference gate is satisfied for both visible named characters: Fernand is bound by approved Sheet 03 and Mercédès by approved Sheet 02. The Morcerf drawing room and recurring 1838 newspaper are bound by approved permanent setting and object references. These four files remain below the five-input cap.

## Required predecessor and sequential hold

- `pages/page-27.png` — **PROMOTED** — 1024 × 1536 RGB PNG — SHA-256 `dcd32558ed34b372e578865c12f8d2aa51610c61c9def8ae4abd1ae3ecbba030`.
- Page 27 v4 is unconditionally approved and promoted byte-for-byte. Page 28 generation is explicitly released.
- Page 27 is a sequence-status prerequisite only, not a Page 28 generation input. The Page 28 prompt explicitly says the predecessor is a hard cut and **must not be attached**. Even after promotion, do not attach `pages/page-27.png` or carry its ink-and-bare-board palette into Page 28.
- Do not substitute Page 27 candidate evidence, rejected art, Page 26, Page 6, any other page, or prose description for an authorized permanent reference.

## Attach and prohibit bindings

- If released, attach exactly the four approved permanent files listed above, in that order. Attach no predecessor or other page image.
- All other character sheets and character-bearing boards are prohibited generation inputs. Do not attach Albert, Beauchamp, the Count, Haydée, Danglars, Villefort, any servant, guest, crowd, woman other than Mercédès, head board, silhouette board, live-pair proof, or adversarial board.
- Do not attach any unlisted setting, object, newspaper, carrier, candidate, proof, or rejected image. Approved Sheet 18 alone binds the room, and approved Sheet 21 alone binds the recurring newspaper.
- Exactly two human beings may appear: Fernand on the left and Mercédès on the right in every applicable panel. They never swap sides. No servant, guest, crowd, or third figure may appear.
- Fernand must keep his heavy moustache, receding hairline, weathered ruddy-olive face, and heavy soldier's build, with no decorations on his chest. Mercédès must read visibly forty-two, with mature lower-lid and temple lines, grey temple threads, formal Paris coiffure, burgundy-black vertical gown, and no Haydée/Epirote traits.
- The same cheap grey 1838 newspaper appears crushed in Fernand's fist with type as unreadable texture only. No readable headline or other print is allowed.
- The Morcerf room uses burgundy, polished walnut, wax red, old gold, ranked portraits, and purchased legitimacy under flat grey daylight. No candle amber, party guests, or press-room ink-and-bare-board palette.
- Exactly five panels and eight balloons are specified. Preserve the exact order and ownership; Fernand owns four, Mercédès owns four, Fernand is silent in dominant Panel 4, and Panel 5 contains Fernand's face alone with no text of any kind.

No Page 28 image, proof, candidate, audit, critic report, Page 29 material, promotion, `pages/` write, or story-document edit was created during the preparation step. On release, Page 28 must use exactly the four approved permanent inputs listed above and must not attach promoted Page 27.

## Page 28 v1 execution record

- Prompt verification: `qa/production/page-28/prompts/page-28-v1.md` was exact-diff verified against the current §5 Page 28 prompt before generation — SHA-256 `602c3450f862011c15dabe92f4f972afaf8a502202d2242ecb8ca0d9921d4dc6`.
- Sequence release: promoted `pages/page-27.png` exists and matches the released predecessor — 1024 × 1536 RGB PNG — SHA-256 `dcd32558ed34b372e578865c12f8d2aa51610c61c9def8ae4abd1ae3ecbba030`. It was not attached.
- Generation route: one built-in Codex/ChatGPT subscription-backed image-generation call. No API, API key, bundled CLI, prototype, patch, post-hoc lettering, or rejected candidate was used.
- Attached inputs: exactly the four authorized approved permanent files listed above, in manifest order. Promoted Page 27 and every other page, character, setting, object, candidate, proof, and rejected image were excluded.
- Candidate: `qa/production/page-28/candidates/page-28-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `fa80a1f71f5f0796c6f0d6f93a897541529d8e45504d3750e0f5706985d77318`.
- 600 proof: `qa/production/page-28/proofs/page-28-v1-600.png` — 600 × 900 RGB PNG — SHA-256 `e1cc7cad55adce8c1c6c657c791e810c938574dc9f8cdc9d2542a548a84fb642`.
- 768 proof: `qa/production/page-28/proofs/page-28-v1-768.png` — 768 × 1152 RGB PNG — SHA-256 `5596b36454f375221412853581a8e3c38eac6811cd08d0604a5bbae22db93772`.
- Practical audit: `qa/production/page-28/audit-v1.md` — non-gating builder report. The completed candidate is submitted unchanged for independent review.
- Scope confirmation: no approval, promotion, `pages/` write, Page 29 preparation or generation, or story-document edit was performed.

## Page 28 promotion record

- Independent critic: `qa/production/page-28/critic-v1.md` — `APPROVED` after blind transcription of all eight strings and verification of fixed left/right ownership, Mercédès's mature lock, Fernand's undecorated coat, newspaper state, daylight setting, silent dominant confrontation, and textless coda.
- Promoted candidate: `pages/page-28.png` — byte-for-byte copy of `qa/production/page-28/candidates/page-28-v1.png` — 1024 × 1536 RGB PNG — SHA-256 `fa80a1f71f5f0796c6f0d6f93a897541529d8e45504d3750e0f5706985d77318`.
- Promoted 600 proof: `qa/production/page-28/proofs/page-28-promoted-600.png` — byte-for-byte copy of `qa/production/page-28/proofs/page-28-v1-600.png` — SHA-256 `e1cc7cad55adce8c1c6c657c791e810c938574dc9f8cdc9d2542a548a84fb642`.
- Promoted 768 proof: `qa/production/page-28/proofs/page-28-promoted-768.png` — byte-for-byte copy of `qa/production/page-28/proofs/page-28-v1-768.png` — SHA-256 `5596b36454f375221412853581a8e3c38eac6811cd08d0604a5bbae22db93772`.
- Page 29 sequence hold is cleared. Page 28 remains sequence-status only and must not be attached to Page 29 generation.

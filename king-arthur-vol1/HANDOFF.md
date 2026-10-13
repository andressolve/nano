# King Arthur, Volume I: The Sword and the Table — handoff

**Updated:** 2026-10-12

This is the one dynamic state file. `tools/status.py` derives state from disk;
this file records what disk cannot: owner decisions, holds, and the next
bounded action.

## Phase

`ADAPTATION` → `SCRIPT_GATE` → `REFERENCES` → `PACKETS` → `PRODUCTION` → `PUBLICATION`

Current: **PUBLISHED (Nano, 2026-10-13)**

## Owner decisions on record

| Date | Decision |
|---|---|
| 2026-10-13 | Page 2: owner's lettering correction (Re-letter the old wizard's balloon in the middle panel from scratch, in the same hand-lettered style and the same balloo) applied by in-generator edit of the approved page; v4 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 32: owner's lettering correction (Fix one letter only. In the red-bearded king's balloon at the top, the word 'aré' has a stray accent mark over the e. Re) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 2: owner's lettering correction (Fix one punctuation mark only. In the old wizard's balloon in the middle panel, the text currently reads 'Safe, and far ) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 44: owner's lettering correction (In the hand rising from the lake, make the sword itself unmistakable: above the dark-red scabbard show the sword's long ) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Batch gate 41–50 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-13 | Page 21: owner's lettering correction (On top of the stone where the boy stands, add a black iron anvil. And make the plain sword in the boy's hand flare with ) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 13: owner's lettering correction (On top of the grey stone, add a black iron anvil with an empty slot in it where the sword was; no sword in the anvil. Ch) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 8: owner's lettering correction (On top of the great grey stone, add a black iron anvil, with the long plain sword driven down through the anvil into the) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 48: owner's lettering correction (Change the colour of the boy's horse to a plain dapple grey with no white blaze on its face. Change nothing else on the ) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 15: owner's lettering correction (In the third panel, change the surcoat of the black-haired young man to a surcoat quartered in black and yellow squares,) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 54: owner's lettering correction (In the caption at the top left, remove the stray full stop before the first word, so the caption begins exactly 'As each) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 2: owner's lettering correction (In the old wizard's balloon in the middle panel, replace the comma after 'Safe, and far from here' with a full stop, so ) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 49: owner's lettering correction (In every panel, change only the clothing of the tall black-haired young man with the thin moustache: he wears a long pla) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Batch gate 41–50 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-13 | Page 17: owner's lettering correction (Remove the sword that stands upright in the stone behind the two young men: the black iron anvil on top of the stone mus) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Page 16: owner's lettering correction (In the large panel, remove the second sword that stands upright in the stone at the right: leave the black iron anvil on) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-13 | Batch gate 11–20 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-13 | **Published to Nano** on the owner's word: commit `aa0624f`, Pages run `38414284999` success; live at https://andressolve.github.io/nano/king-arthur-vol1/index.html (reader 200, page 59 200, card first in live `stories.js`). |
| 2026-10-13 | **Owner: "add to nano library, and commit and push."** Book complete: all 59 pages promoted, every batch gate APPROVED, whole-book gate APPROVED twice (`qa/whole-book-round-1.md`, `qa/whole-book.md`), edit pass done, reader APPROVED. Open item: p2 comma (see RUN-LOG ship record). |
| 2026-10-13 | Pages 21–50 promoted; gates 21–30 and 31–40 all APPROVED; gate 41–50 sequence and cold-read (1–50) APPROVED, continuity REVISE: p49 drew Kay in his old mail and black-and-yellow surcoat instead of the steward's black. Advisor ruling: cause was the sheet's default views (mail) plus a lock line reading 'blue against black-and-yellow'; fixed that line, added a 'Kay wears only his steward's state' exclusion to every packet 49–57 where Kay appears and a blocking card criterion; p49 fixed by in-generator `--edit` (clothing only), then `--gates 50`, then resume. Also pre-hardened pp 40–47: the sword plate is a multi-state reference never copied as a group, with a blocking 'Sword count' criterion. |
| 2026-10-13 | Pages 1–20 promoted; gates 01–10 all APPROVED. **Gate 11–20:** sequence and continuity REVISE on one defect (p16 showed a second sword standing in the stone beside the one on Arthur's knees; p17 showed the sword back in the stone), cold-read APPROVED. Advisor ruling: cause was the churchyard plate (sword in stone) attached to pages where the stone must be empty — p16/p17 packets restaged without the plate, with 'exactly one sword' exclusions and a new blocking card criterion C6 'One sword'; fix by in-generator `--edit` of each promoted page (remove the extra sword, change nothing else), then `--gates 20`, then resume. |
| 2026-10-12 | **Reference gate APPROVED** (round 3, no findings). Round 2 had found a signature-like mark on `01-arthur` and `set-great-hall-london` and Arthur's reserved blue on the London and tournament banners: Arthur's sheet repaired (plain-ground corner, fresh critic APPROVED, superseded v1 kept), the three plates regenerated with the reserved-blue and no-signature clauses; 'No signature…' added to the register and the page frame. Page run launched. |
| 2026-10-12 | References: all 29 locks approved (8 character sheets, 2 crop boards, 5 adversarial boards, 1 live-pair, 11 set plates, 2 object plates). Whole-cast gate round 1 REVISE on one finding only: `09-REFERENCE-PLAN.md` carried the pre-gate page index. Reindexed to the 59-page script; gate rerun. Packets: 7 fresh writers, assembled, `verify.py` CLEAN. |
| 2026-10-12 | **Script gate cleared at round 10** (`qa/script/round-10.md`, APPROVED, findings NONE; rounds 4, 7, 9 also APPROVED-NONE, their nonblocking notes taken and regated). 59 pages: 35 D / 9 P / 9 S / 6 C. `07-PAGE-CONTRACT.md` generated. Method amended: Chronicle pages render their question first (round 6). |
| 2026-10-12 | Advisor: reference run launched in parallel with the script gate (character sheets do not depend on script wording); all eight characters locked by the gate's end. |
| 2026-10-12 | **Greenlight ① GIVEN.** Owner: "go. proceed autonomously, do not stop for my approval on production docs. do not stop for me to resolve page render issues… let's make this one epic." Full delegated authority through ship (publication still waits for the owner's word). |
| 2026-10-12 | **Owner: go — add the Chronicle mode and start Phase 0.** The family (playing Civ VI's heroes mode) asked for a book "between a graphic novel and an illustrated story": great story plus rich context (history/myth). Owner approved a new page mode, Mode 4 Chronicle, added to `method/` (see RUN-LOG). |
| 2026-10-12 | Book created. Billing: codex in-app on the ChatGPT subscription (standing decision 2026-09-07). |

## Open holds

NONE

## Next bounded action

Published to Nano. Only open item: p2 'here, If' → 'here. If' needs one edit past the ceiling, on the owner's word.

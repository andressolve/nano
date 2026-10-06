# Three Kingdoms, Volume I: The Peach Garden Oath — handoff

**Updated:** 2026-10-03

This is the one dynamic state file. `tools/status.py` derives state from disk;
this file records what disk cannot: owner decisions, holds, and the next
bounded action.

## Phase

`ADAPTATION` → `SCRIPT_GATE` → `REFERENCES` → `PACKETS` → `PRODUCTION` → `PUBLICATION`

Current: **SHIPPED (local) — awaiting the owner's word to publish**

## Owner decisions on record

| Date | Decision |
|---|---|
| 2026-10-05 | **Book complete, not published.** Whole-book gate APPROVED (`qa/whole-book.md`); p 15 typo fixed by edit, batch 11–20 regated APPROVED; reader `index.html` APPROVED by the sixth fresh reader critic (`qa/_publication/reader-critic.md`, rounds 1–5 archived beside it). Ship record in `RUN-LOG.md`; two failure modes promoted to `method/07-FAILURE-MODES.md`. Publication (Nano or elsewhere) waits for the owner's word. |
| 2026-10-05 | Page 15: owner's lettering correction (In Dong Zhuo's first balloon, the full stop after the opening word 'So' is missing. Restore it so the balloon begins exa) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-05 | **All 50 pages promoted.** Batch gates 1–10, 11–20, 21–30, 31–40, 41–50: sequence, continuity, cold-read all APPROVED. Other events: p34 v1 landscape canvas (failed generation, archived in `qa/production/_invalid-canvas/`, regenerated); p31 restaged to one set plate after a montage, p35 pre-emptively the same. Whole-book gate launched (fresh milestone-critic). |
| 2026-10-05 | Advisor (session), p31: v2 rendered a four-panel montage of the two attached multi-view set plates with no prose. Restaged the packet to attach only `set-coalition-camp` (its day study already shows the gate), with an explicit one-continuous-scene instruction; rebuilt and assembled; verify CLEAN. Takes effect from the next candidate after v3. Batch gates 21–30 all APPROVED. |
| 2026-10-05 | Account/capacity failure: the p23 v1 critic `codex exec` failed ("Selected model is at capacity"). The session reran the same blind critic command by hand on the same entrypoint; report VALID APPROVED, route PROMOTE, promoted. Driver relaunched. |
| 2026-10-05 | Batch gates 11–20: sequence, continuity, cold-read all APPROVED. `verify.py` then flagged p20's five generations against the ceiling (it has no per-page exception for an owner-authorized edit); p20 v1 and its report moved intact to `qa/production/_archive-p20-owner-ceiling-exception/` with a README; verify CLEAN. Method note for the ship record: verify and the edit path need a recorded per-page ceiling exception. |
| 2026-10-05 | **Owner: page 20** — promote v4 (only finding: lowercase 't' in Dong Zhuo's "There is no horse…") and fix the letter by one in-generator edit with the ceiling lifted for that edit only. `book.toml` max_versions set to 5 for the single edit run and restored to 4 immediately after. Edit v5 passed the blind critic and supersedes v4. |
| 2026-10-05 | Page 20: owner's lettering correction (In Dong Zhuo's first balloon, the last sentence begins with a lowercase 't'. Capitalize it so that sentence reads exactl) applied by in-generator edit of the approved page; v5 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-04 | Advisor (page 20): Restaged the five-string exchange into four panels with isolated opening and closing balloons, and made shoulder-contact timing nonblocking when the invasive pressure remains clear across the closing exchange. |
| 2026-10-04 | Split complete: script round 7 **APPROVED, findings NONE** (`qa/script/round-07.md`); `07-PAGE-CONTRACT.md` regenerated (50 rows); ledger costume switch moved to the forge (p 8), swords sheathed until p 44; new p7/p8 packets in mov-1; `verify.py` CLEAN (50 packets, 6 promoted). Page loop relaunched at p7. |
| 2026-10-04 | **Owner: split page 7.** Old p7 (prose) dropped "was Third Brother," in four candidates (v4 was briefly promoted by advisor override, then withdrawn; artifacts in `qa/production/_archive-split-old-p7/`, ledger row archived there too). New p7: dramatic, the brothers name their order and Zhang Fei offers to sell everything; new p8: the forge and the farmers (old p7's last two paragraphs verbatim). Pages 8–49 → 9–50; book is 50 pages. Script gate reopened (round 7); packet parts renumbered, new p7/p8 packets being written; contract to be regenerated. Old p8's invalid landscape attempt archived too. |
| 2026-10-04 | Page 7 held after 4 candidates and one advisor reset (V4_OWNER_HOLD); needs a split or a Claude session. |
| 2026-10-03 | Book created. Billing: codex in-app on the ChatGPT subscription (standing decision 2026-09-07, already in book.toml). |
| 2026-10-04 | **Packets written and assembled** (7 fresh writers, one per movement; `qa/_assembly/parts/`; `assemble.py` → 49 packet sets + 5 batch gates in `qa/_run`). `verify.py`: the only problems are inputs not yet in `refs/approved/` (expected until the reference gate clears). Writer rulings kept: p20 Lü Bu still in dark bronze (gold armor is called for in that page); p24 Cao Cao's horse dun, never red; p1 attaches only the ridge plate; cards tolerate a missing diaeresis on Lü. |
| 2026-10-04 | **Script gate cleared at six rounds** (round 6 APPROVED, findings NONE; `qa/script/round-01…06.md`). Script is 49 pages (p 29 added at round 2). `07-PAGE-CONTRACT.md` generated. Round-6 nonblocking notes carried to packets: p36 balloon lanes; p39 Cao Cao's hill readable; p21/p22 one bedchamber; p28 letter one of a bundle; p47 cup refused then held; p26 knife in hand, whetstone in kitchen; ledger arc lines reconciled. |
| 2026-10-04 | Register **Lacquer and Dust** recorded in `book.toml`; `09-REFERENCE-PLAN.md` written (8 sheets, 5 boards, 12 sets, 3 object plates). |
| 2026-10-04 | **Greenlight ① given** ("go"): story as presented in `00`–`05`, 48 pages, cast of eight. The violence rule (deaths real, never drawn) and the farmhouse (pp. 25–27) are both accepted as proposed. |
| 2026-10-03 | The boys chose this book by vote (`menu/VOTES.md`); the pitch they voted for is a protected claim in `02-SOURCE-MAP.md`. |
| 2026-10-04 | **Reference gate APPROVED** (round 2; 34 locks: 8 characters, 2 deterministic + 7 adversarial/neutral boards, 1 live pair, 12 sets, 3 objects). `verify.py` CLEAN (49 packets). Every packet has 1–3 focal inputs, no boards; every card carries the transcription tolerances. **Page production launched.** |
| 2026-10-04 | Whole-cast reference gate round 1: REVISE (`qa/references/reference-gate.md`), 3 findings, all board coverage, no lock changed. Advisor (session): added `adversarial-yuan-shao-uncle` and `adversarial-liu-bei-yuan-shao` (the two ledger collision lanes without boards), and, because `board-heads` is a deterministic crop of each sheet's view (a) and cannot be re-posed without changing the locks, two generated expression-neutral head boards `adversarial-heads-neutral-1/-2` (four heads each, within the five-input limit); `board-heads` kept as the pixel-identity check. Fixed the stale "tuft" phrase in the Cao Cao block. Rerun `refrun.py --all` then the gate. |
| 2026-10-04 | Advisor (session): Guan Yu's sheet view (d) changed from the battle beard-bag (rejected three times, used on no page) to the tavern state the script needs (pp 4–6: green robe, headscarf, no armor, beard loose). The beard is never bagged. The v4 builder was stopped before it produced an image, so no candidate was spent. |
| 2026-10-04 | Advisor: reset Liu Bei after four candidates to a broad compact face with a clean rounded chin, long earlobes, and a tall narrow silhouette, removing the unstable lip tuft and concealed long-arm lock so he stays distinct from Cao Cao and consistent across the story. |
| 2026-10-04 | Advisor: reset the coalition-camp prompt as a clean two-study, visibly unoccupied environmental lock with an isolated blank gold command banner, preserving the camp's story scale while preventing false figures and lettering. |
| 2026-10-04 | Advisor (page 7): Restaged the page into a generous upper narration band with three separately composed paragraph blocks, then a dominant forge panel and a narrower garden consequence, preserving every string while relieving the repeated omission in the first paragraph. |

## Open holds

NONE

## Next bounded action

The book is finished and gated; the reader is `books/three-kingdoms-vol1/index.html`.
Publish only when the owner says where (the Musketeers precedent was Nano). Owner reading
feedback, if any, is executed as `pagerun.py --page N --edit` lettering fixes or page
regenerations through the gates. Optional nonblocking items from the whole-book gate (no action
taken, cost one candidate each if wanted): Liu Bei's horse colour varies (white/brown);
p 46's flinch reads as a near miss; p 48's refused cup is small.

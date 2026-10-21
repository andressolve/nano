# Monkey King, Volume III: Sent Away — handoff

**Updated:** 2026-10-20

This is the one dynamic state file. `tools/status.py` derives state from disk;
this file records what disk cannot: owner decisions, holds, and the next
bounded action.

## Phase

`ADAPTATION` → `SCRIPT_GATE` → `REFERENCES` → `PACKETS` → `PRODUCTION` → `PUBLICATION`

Current: **PUBLISHED (Nano, 2026-10-17)**

## The story (presented at greenlight ①)

- **Engine:** the only one who can see the demon's real face is the one the monk has just sent home — and someone has to go back for him.
- **Spine:** White Tiger Ridge; the White Bone Lady's three faces (girl, old woman, old man); Wukong sees through each, the monk believes each, says the words; the third time Wukong asks first, is refused, strikes to save him; bones with her name; "you are not my disciple"; four bows; home to Flower-Fruit Mountain, happy, he says, looking west every evening. The monk alone walks into the Yellow Robe's golden pagoda; Bajie runs, Wujing tied, the monk made a tiger who will not eat the meat; the white horse becomes the dragon, is wounded, and speaks once: "go and get our big brother." Bajie flies east, lies, is seen through, tells the truth about his lie; Wukong goes back, beats the demon, sees the star under its face and lets it go home rather than leave the monk a minute longer, takes the tiger's shape off. The monk: I couldn't see her face; I should have believed you. Last page: the road west, the monk beside the monkey, looking to him first.
- **Movements (48 pp):** I The Ridge 1–5 · II Three Faces 6–19 · III Home 20–22 · IV The Yellow Robe 23–33 · V Going Back 34–39 · VI The Star in the Pagoda 40–48. Modes 30 dramatic / 7 prose / 11 spectacle.
- **Cast (7 of 8):** Wukong, Sanzang (+ tiger state), Bajie, Wujing (no skulls now), the white horse/dragon, the White Bone Lady (true shape + three disguises), the Yellow Robe. Monkeys of Flower-Fruit Mountain are scenery (ensemble sheet).
- **Cuts:** the four sages, the ginseng-fruit tree, the whole Kingdom of Baoxiang (princess, king, court, framing), the trip to Heaven and the constellations, Wukong's princess disguise, the hunters, the mountain gods, the dismissal letter, Bajie's provoking lie (replaced by his confession). Guanyin named once, not drawn.
- **Graphical direction:** Mineral Ink inherited verbatim; the ridge drained to bone and ash with four red-gold peaches as its warm accent; Flower-Fruit Mountain wet green with the faded pink banner; the pagoda gold outside, black inside, a shaft of moonlight on the cage. Wukong's sight shown as the red rings flaring and a pale ghost of the true shape through the disguise.

## Owner decisions on record

| Date | Decision |
|---|---|
| 2026-10-17 | Page 47: owner's lettering correction (Two changes only. First, the room behind the characters: make it the demon's severe hall of rough black stone - thick bl) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 47: edit candidate v2 for (Change only the room behind the characters: it must be the demon's severe hall of rough black stone - thick black stone ) returned TARGETED; the earlier promotion stands; needs a Claude session. |
| 2026-10-17 | Page 46: owner's lettering correction (Change only the room behind the characters: it must be the demon's severe hall of rough black stone - thick black stone ) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 45: owner's lettering correction (Change only the room behind the characters: it must be the demon's severe hall of rough black stone - thick black stone ) applied by in-generator edit of the approved page; v4 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Batch gate 41–49 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-17 | Page 41: owner's lettering correction (Change only the white horse: it holds its right foreleg lifted off the ground, limping, with one dry charcoal-dark slash) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 46: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 18: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 11: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 10: edit candidate v2 for (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) returned TARGETED; the earlier promotion stands; needs a Claude session. |
| 2026-10-17 | Page 9: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 5: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 3: edit candidate v3 for (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) returned TARGETED; the earlier promotion stands; needs a Claude session. |
| 2026-10-17 | Page 1: owner's lettering correction (Change only Bajie the pig's head, wherever he appears on this page: give him his locked pig face - a long pig snout endi) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Batch gate 31–40 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-17 | Page 34: owner's lettering correction (Change only the wound on the white horse's right foreleg: it must be one clean, dry, charcoal-dark slash line, with no r) applied by in-generator edit of the approved page; v3 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 33: owner's lettering correction (Change only the wound on the white horse's right foreleg: it must be one clean, dry, charcoal-dark slash line, with no r) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Page 32: owner's lettering correction (Change only the wound on the white dragon's right foreleg: it must be one clean, dry, charcoal-dark slash line, with no ) applied by in-generator edit of the approved page; v2 passed the blind critic and supersedes the earlier promotion. |
| 2026-10-17 | Batch gate 31–40 returned REVISE; see qa/batches, qa/continuity, qa/cold-reads. Run stopped for a Claude session to route the named pages. |
| 2026-10-16 | Book created from the kickoff in `notes/NEXT-SESSION-MONKEY-KING-VOL3.md`; slug `monkey-king-vol3`, parent `monkey-king-vol2`, register Mineral Ink, no Chronicle pages, standard pinyin. |
| 2026-10-16 | Billing: Codex in-app on the ChatGPT subscription (standing decision 2026-09-07), recorded in `book.toml`. |
| 2026-10-16 | **Greenlight ① given in advance by the owner** ("fully autonomous, greenlight ① given in advance"). Phase 0–1 docs (`00`–`05`) stand as the greenlit story above. Run proceeds without owner checkpoints. |
| 2026-10-16 | **Publication authorized in advance:** owner's session message: "publish to nano when ready" (supersedes the kickoff's "Publication to Nano waits for my word"). |
| 2026-10-16 | Advisor: Reset `15-yellow-robe` around his proven broad indigo, tusked, black-haired silhouette; star point count is nonbinding and dark-metal scimitar fittings protect distinctness without wasting candidates on invisible ornament counts. |
| 2026-10-16 | Advisor: Reset `06-white-horse` around the inherited slim white, pale-blue-maned identity, replacing the ambiguous bandage option with one contained right-foreleg gash so the wound reads consistently across horse and dragon states. |
| 2026-10-16 | Advisor: Reset `13-bone-old-woman` around her proven short, broad, white-bunned living design and confined Wukong's reveal to the Bone Lady's skull inside her intact face, preserving instant story recognition without unstable full-body skeletons or an accidental handkerchief. |
| 2026-10-16 | Advisor: Reset `13-bone-old-woman` again with the proven short, broad living face and a single skull-headed shadow behind it, preserving an instant demon reveal while removing the unstable transparent anatomy, extra figures and duplicate eye lights. |
| 2026-10-16 | Advisor: Reset `05-dragon` around its inherited slim white serpent identity, made the wound a shared cross-form lock, and removed the horse image input so four dragon-only views stay unmistakable at page scale. |
| 2026-10-16 | Advisor: Reset `05-dragon` again with a compact shield-nosed lizard head and one bold proof-scale foreleg slash, replacing unstable muzzle and pin-line constraints so the dragon stays distinct from the horse and its injury reads consistently. |
| 2026-10-16 | Advisor: Relocked `06-white-horse` after the whole-cast gate so the sheet carries injury through its stable right-flank, lifted-right-hoof posture while the fresh gash and final bandage stay page instructions, preserving the story wound without an unstable red leg ring. |

## Rulings (advisor, delegated authority)

| Date | Ruling |
|---|---|
| 2026-10-16 | Title: *Sent Away* (series cadence: Havoc in Heaven, The Road West). |
| 2026-10-16 | `max_versions = 6` set before any generation (method/07 watch: a v4 advisor reset cannot run at 4). |
| 2026-10-16 | Wujing carries no skulls in this volume (they became the raft, Vol II p46); a skull on Wujing is blocking. No counted story object above five is planned; the four peaches are never counted in text. |
| 2026-10-16 | `set-pagoda-exterior` v2 blocked partly on "five tiers, not seven". Ruling: storey count is not a story object; plan and settings now say five to seven storeys pass. The basket's frogs likewise "two to four". (method/07: counted objects — never hang a block on an uncounted detail.) |
| 2026-10-16 | `15-yellow-robe` v1–v4 REVISE, chiefly on "seven-point stars" (critics counted eight) and gold-toned hilt fittings. Ruling: my plan over-specified an uncounted ornament — any small silver star passes and the point count is never blocking; the hilt may be black or dark iron, a small dark-bronze guard nonblocking, no bright gold. Plan and ledger amended. |
| 2026-10-16 | **Script gate APPROVED** at round 6, findings NONE (`qa/script/round-01..06.md`): rounds 1–5 REVISE with 8, 5, 2, 1, 1 findings, all taken; p28 split at round 3 → **49 pages**. `07-PAGE-CONTRACT.md` regenerated from the approved script. |
| 2026-10-16 | Packets written by eight fresh writers in parallel (`qa/_assembly/parts/mov-1..8-*`), assembled (`assemble.py`: 49 page sets, 5 batches); `verify.py` problems are only the sheets still generating. Every page attaches 2–3 inputs. A second reference worker (`notes/monkey-king-vol3-run-scripts/chars2.sh`) runs monkeys, horse, dragon, Bajie alongside the main chain. |
| 2026-10-16 | `13-bone-old-woman` reached the hard six-candidate ceiling (owner hold): every failure was in view (d), the reveal; the living disguise passed. Ruling (owner-delegate): relock scope = views (a)–(c); no page draws the reveal from this sheet (pp 9–10 prompts say so; the skull comes from `11-bone-lady` and words). Fresh reference critic re-judged v5 under the amended lock: **APPROVED** (`critic-v5-relock.md`); promoted. |
| 2026-10-16 | `05-dragon` hit the six-candidate hold (equine-snout and wound-view findings). Ruling (owner-delegate): lock Volume II's approved `05-dragon` unchanged — same character, already gated; no wound view needed (the cut on pp 31–32 comes from words, `06-white-horse` carries the wound lock). Fresh reference critic: **APPROVED** (`critic-parent-relock.md`); promoted. Ledger head clauses marked superseded. |
| 2026-10-16 | All 16 character sheets and 8 plates locked; `verify.py` CLEAN. **Page run launched** under `notes/monkey-king-vol3-run-scripts/supervise.sh monkey-king-vol3` (log `qa/_logs/pagerun.log`), in parallel with the generated boards and the whole-cast gate (`refrun --all`, log `qa/_logs/refrun.log`) — Vol II precedent; no page depends on a board. |
| 2026-10-16 | Pages 1–10 promoted (p3, p5 on v2; the rest first candidate). **Batch gate 1–10 APPROVED** — sequence, continuity, cold read. All boards locked; whole-cast reference gate running. |
| 2026-10-16 | **Whole-cast reference gate APPROVED** at round 2 (round 1 REVISE: the horse's wound view showed a red band; `06-white-horse` regenerated, the driver's advisor relocked it on the lifted-right-hoof pose with the gash and bandage as page instructions; superseded lock in `refs/superseded/`). 30 locks. Pages 1–20 promoted. |
| 2026-10-17 | Pages 21–27 promoted; batch gate 11–20 APPROVED. p28 v1: the in-app image tool's safety filter refused all three attempts (no candidate; driver stopped). Ruling: restage the captivity in storybook terms — sitting against the pillar inside one loose rope, no "bruised", no tears — in the p28 and p29 prompt sources (prompts only; script unchanged). Driver relaunched under the supervisor. |
| 2026-10-17 | Pages 28–40 promoted; batch gate 21–30 APPROVED. Batch gate 31–40: sequence and cold read APPROVED, continuity REVISE — the dragon/horse foreleg wound drawn red on pp 32–34 reads as blood. Ruling: take it; in-generator `--edit` of the wound only on pp 32, 33, 34 (one dry charcoal-dark slash), then `--gates 40`, then the supervisor resumes (`fix3134.sh`). Pp 41–49 horse prompts already say "clean dark gash, never blood". |
| 2026-10-17 | Wound edits on pp 32–34 promoted; regate 31–40: continuity REVISE on p32 only — the edit drifted it out of Mineral Ink (glossy oil finish, bright fires; method/07 watch "one page drifts out of the register", now seen twice). Ruling: p32 regenerated with a register-emphasis section and the dry-slash wound; **batch gate 31–40 APPROVED**. Supervisor relaunched from p41. |
| 2026-10-17 | **All 49 pages promoted; batch gates 1–10, 11–20, 21–30, 31–40, 41–49 all APPROVED.** p45 took three candidates (v2 lettered "Wujing" for "Wukong"; full prompt reset). Reader `index.html` built (verifier CLEAN). Whole-book gate launched (fresh milestone critic on 600×900 proofs in `qa/_review/proofs-600/`). |
| 2026-10-17 | **Whole-book gate APPROVED**, mandatory findings NONE, no typos (`qa/whole-book.md`). Nonblocking list worked: Bajie's face drifted on pp 1, 3, 5, 9, 10, 11, 18, 46 (soft tuskless cartoon pig, sometimes a cap) → in-generator edits to the locked pig face; p41 horse not limping → edit. Edits p3 and p10 blocked by their edit critics on things the edit did not touch (Wujing's reed sash read as a forbidden "cord"; p10's blow staging, approved at page and batch gates) → advisor overrides (`promote.py --owner-override`, reasons in the ledger); the cards' "cord" clause clarified. Regates 1–10, 11–20 APPROVED. |
| 2026-10-17 | Regate 41–49: sequence and cold read APPROVED; continuity REVISE — pp 45–47 drifted from the locked black-stone hall into a warm gilded shrine (gold Buddha altar on p47). Ruling: take it; setting-only edits on 45, 46, 47 (black stone, iron lamps, cold cage light, no gold), then `--gates 49` (`fix4547.sh`). |
| 2026-10-17 | p47's hall edit moved the first balloon's tail to Wukong (real attribution defect, edit critic REVISE); second edit fixed hall and tail together. **Batch gate 41–49 APPROVED** (re-gated). **Reader critic APPROVED.** Ship record in `RUN-LOG.md`, journal `10-PRODUCTION-MEMOIR.md`; method/07 updated (two watches promoted, two new watches, one corollary); selftest CLEAN; infra re-frozen (INFRA INTACT). |
| 2026-10-17 | **Published to Nano** on the owner's advance authorization: commit `f70de0a` (only `.gitignore`, `stories.js` and `monkey-king-vol3/` staged; nano's other uncommitted work untouched). Publication copy adds the toolbar and ending library links; its verifier requires them and reports CLEAN; pages byte-identical to production. |
| 2026-10-17 | Nano Pages run `39024679904` success; live at https://andressolve.github.io/nano/monkey-king-vol3/index.html (reader 200 with the correct title, pages 1 and 49 200, card first in live `stories.js`). |
| 2026-10-17 | **Owner verdict:** "the book was absolutely epic. well done. amazing work! bravo! and i did not see any image gen glitches." One correction: in the reader quiz the longest option was always the correct answer. Rule added to `method/01-PIPELINE.md` Phase 6 (equal-length options, correct answer longest in at most two of five, letters varied; the reader critic checks it); recorded in RUN-LOG, journal and memory; infra re-frozen, selftest CLEAN. This book's live quiz is unchanged (offered to the owner as a rewrite). |
| 2026-10-17 | Handoff prepared for the next series volume: `notes/NEXT-SESSION-THREE-MUSKETEERS-VOL2.md` (used the same day; *The Three Musketeers, Volume II: Milady* published to Nano 2026-10-18, see `books/three-musketeers-vol2/`). Monkey King Volume IV kickoff remains ready in `notes/NEXT-SESSION-MONKEY-KING-VOL4.md`. |

## Open holds

NONE

## Next bounded action

Done and published. Next session: Monkey King, Volume IV — paste the kickoff in `notes/NEXT-SESSION-MONKEY-KING-VOL4.md`. Journal: `10-PRODUCTION-MEMOIR.md` (Part V: threads and source ground). Run scripts: `notes/monkey-king-vol3-run-scripts/`.

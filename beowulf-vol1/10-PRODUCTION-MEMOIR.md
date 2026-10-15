# Beowulf: The Hall, the Mere, and the Dragon — production journal

Greenlit 2026-10-13 ("go. proceed autonomously… you can sort stuff out"),
completed 2026-10-14, published to Nano the same day (commit `850469d`). Owner's
verdict: "great book. good work." This journal is what the next book should
know. The ship record with numbers is in `RUN-LOG.md`; failure modes are in
`method/07-FAILURE-MODES.md`.

## Part I — The shape decision that made the book

**One volume, the whole poem.** The temptation was to split Grendel/mother from
the dragon. Kept together, the book has a hinge no split could give it:
Hrothgar's warning on p34 ("sickness, or the sword, or fire, or old age") is
paid off item by item in the dragon movement, ending with old Beowulf's "Sickness
too, then. Old Hrothgar left nothing out." The critics called the dragon half
the best thing in the book. **Lesson:** when a source's second half is usually
treated as an epilogue, ask what setup in the first half it pays off, and plant
it in words.

**The one invention that carried the ending:** Wiglaf's forge scene (p41),
not in the poem. "Were you ever afraid?" / "Every time." It turned the young
hero's boasting into a trap he set for his own courage, and gave the climax its
line: "You told me you were afraid every time. So am I. I came anyway." Owner
approved the invention at greenlight. **Lesson:** a hero's climax partner must
have a scene with him before the fight, or the rescue is a stranger's.

**Silent monsters.** Grendel, his mother and the dragon never speak. It made
them more frightening and freed every balloon for the people.

## Part II — What the script critics taught (7 rounds)

Findings ran 10 / 3 / 3 / 2 / 1 / 1, then APPROVED-NONE. The structure was
right from round 1; every later finding was a causal or continuity hole a
careful ten-year-old would catch:

- **Name speakers in rendered text before they matter** (Wealhtheow and Unferth
  spoke for pages unnamed).
- **A death the hero allows needs his grief** (Grendel takes a Geat while
  Beowulf is awake: fixed with "He was too fast" and the empty bench, and the
  count of Geats drops to thirteen for the rest of the book — the number itself
  mourns him).
- **A dead character must be met first** (Hrothgar's oldest friend got a
  caption and a toast before the mother takes him).
- **Kinship is planted, not revealed at the deathbed** ("my cousin's boy").
- **Name the motive for the climax decision** ("For fifty years they've sung
  that I never needed anyone… I'm too old to start now"), then pay it off
  ("Today I did, and you came").
- **An ending that overrides a dying wish must say so.** The buried gold took
  four rounds: the dying king says the gold is for his people; the people bury
  it. Fixed only when the page named the wish and the refusal ("Beowulf had
  wanted the gold for his people. But…").
- **Pronouns at the moral fork** — a page opening "He had wanted the gold for
  them" with only Wiglaf drawn.
- **Chronicle placement:** never between the vigil and the fight it sets up.
- **Arithmetic:** "fifty winters" then a "fifty-year reign" after two other
  kings.

## Part III — References (34 locks, 67 generations, 3 gate rounds)

- **Tiny identity markers resist the generator.** Young Beowulf's crooked nose
  and eyebrow notch took four candidates and a ceiling RESET that rewrote the
  lock as bolder, simpler marks. Choose continuity markers the generator can
  hold at sheet scale (bold, high-contrast, one per face).
- **Multi-object plates fail; split them.** `obj-swords` (five swords at one
  scale) hit the extended ceiling and was retired; human swords live on the
  character sheets, and the one story-critical sword became two plates (whole,
  hilt-only).
- **The gate enforces the two-page rule on extras.** Hrothgar's unnamed old
  friend appears on four pages; the gate required a sheet. The eight named
  characters stayed eight; the sheet is for an unnamed, no-balloon figure.
- **Name a nearest lookalike for every sheet,** even the only woman.
- **Parallel plate workers saved hours** — run sets and objects in a second
  `refrun.py <sheet>` loop while `--all` does characters and boards, and stop
  `--all` after the last board so the two never build the same sheet.

## Part IV — The page run (57 pages, ~80 generations, 42 first-candidate)

Every batch gate found something real or nearly real:
1. **1–10 cold read:** the harp-poet ("an old grey-bearded man") was drawn as
   Hrothgar's double, and the reader took Unferth for the king's old friend.
   An extra described only as "old man" inherits the nearest principal's look.
2. **11–20 continuity:** a background Geat in Beowulf's reserved blue read as
   Beowulf mid-grapple; on rerun, distant Heorot drawn as a fortified compound.
   The reserved-colour leak is now a promoted failure mode (seen twice, with
   King Arthur's banners).
3. **11–20 sequence (rerun):** the Geat taken on p17 "has no aftermath" — the
   aftermath is on p21, outside the batch. A batch-boundary artifact; it passed
   on the next run. Rule it, record it, don't redraw for it.
4. 21–30 through 51–57: approved first time.

**Whole-book gate, 4 rounds.** Round 2 caught the one factual error in the
book: the p7 Chronicle map labelled the European mainland "England", while the
page's own text says England is across the sea. The page critic had passed it.
Maps on Chronicle pages need every label's position written into the card.

**Edits:** a capital-letter fix on p6 turned a colon into a semicolon on the
first try; spell out every string in the region the edit touches. A stray
accent on p42 was verified by a one-line fresh transcription, as King Arthur's
journal advised.

## Part V — Mechanics that worked (keep doing these)

- Gates as work lists: every finding routed to `--edit`, regate the batch,
  rerun the whole-book gate whenever pages changed after it.
- Advisor rulings written into HANDOFF.md the moment they are made, including
  overrules and why (two this book: the batch-boundary artifact, and the reader
  critic objecting to boundary hash aliases its own packet specified).
- A project `.claude/settings.local.json` that allows tools, so an autonomous
  run is never stopped by a permission prompt (owner asked for this mid-run).
- Monitors re-armed every 30 minutes, filtered to promotions, holds, gates and
  failures; act only on state changes.
- Publication mirrors King Arthur: copy without candidates/proofs/logs,
  library links in the published reader, its verifier requires them, card
  first in `stories.js`, stage only the book's paths.

## Part VI — For the next book

- Write every unnamed recurring figure's look (face shape, hair mass, colour)
  into the ledger before references, and give it a sheet if it is on two or
  more pages.
- In packets, name the extras' colours on any page where the hero's reserved
  accent appears.
- On Chronicle maps, list each label and where it sits in the card.
- Expect the climax half of an old story to need the most script rounds:
  that's where the moral decisions are.

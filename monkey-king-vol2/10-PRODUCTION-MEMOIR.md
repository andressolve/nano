# Monkey King, Volume II: The Road West — production journal

Started 2026-10-15 at the owner's request ("lets continue the monkey king
series. next is part 2?"); mid-Phase 0 the owner made the run fully
autonomous ("work on this autonomously … no stopping … to ask my approval").
Completed 2026-10-16 and published to Nano the same day on the owner's word
("commit and push", commit `18efd7d`). Owner's verdict: "great work." This
journal is what the next book, above all Volume III, should know. Numbers are
in `RUN-LOG.md`; failure modes in `method/07-FAILURE-MODES.md`.

## Part I — The decisions that made the book

**The quarrel is the plot.** Chapters 13–22 of the source are a road of
interchangeable stops. The volume mandate made the monk and the monkey's
disagreement (may you hurt someone to protect someone?) the engine, and made
every monster a recruit. Critics named pp 13, 18–23 and 47 as the spine.
**Lesson for III:** the next stretch of the source (the White Bone Demon,
the banishment) is the same quarrel at its breaking point; build on it, don't
restart it.

**The rule that can't be skipped.** Planted three times as a bargain (p3
Guanyin, p8 the monk, p40 Wukong giving it back), never as a moral. Round 4
found the word "carry" broke it (the horse and raft carry him); the rule is
about **flying**, not carrying. Keep that wording.

**Gifts, not takings.** Wukong's wound in this volume: "nobody ever gave me
anything I didn't take." The robe (p9, mended left shoulder) is the book's
emotional root; the cap is the false gift; the apology owns both (p23).
The peaches from his own monkeys are tribute ("Kings get paid"), which the
critics required so the wound would not be contradicted.

**The shoe.** Ao Guang's painting (p15) explains nothing on the page; Wukong
explains it only on p47 ("if a boy can go back for a shoe, I can go back for a
monk"). The critic made us cut the moral line from Ao Guang's mouth.

**Merges that paid.** The white dragon is Ao Guang's son (one face does two
jobs); Wujing makes the raft from his own skulls (Moksa cut); Guanyin gives
the cap undisguised so the reader knows the trap first.

## Part II — What the script critics taught (10 rounds)

Rounds 1–4 found real causal holes: an unintroduced Old Ma; replies spoken by
people not drawn in their panels (round 2 restaged eleven pages); Guanyin's
reason for the band contradicting what the reader saw; the band's rule
("carry" vs "fly"); characters knowing things they never saw (Bajie and the
dragon fight). Round 5 approved; the gate was reopened twice to take small
reader questions and each reopening found one new line. **Lesson:** after
the first clean approval, take only mandatory findings; a fresh critic will
always find one more polish note.

## Part III — References (31 locks, 72 candidates, 5 gate rounds)

- **The uncapped hero.** Volume I's Wukong always wore a cap. Uncapped, the
  generator gave him elf ears and a spiky crest for six candidates; the ledger
  clause written in response was stricter than Volume I's own sheet.
  `01-wukong` was retired and Wukong relocked as `10-wukong` (banded pilgrim
  robe, released state as view d) with small upright cupped ears and a swept
  golden ruff accepted. **For III: `10-wukong.png` is the identity anchor; do
  not try to make the ears rounder.**
- **Nine skulls.** The generator cannot hold nine. Ruling written into the
  ledger: the text carries the number; art passes at eight to ten, spaced and
  separately visible. Wujing's view (d) was simplified to the cord still on
  his neck. (`method/07`: counted objects above five.)
- **Silhouette boards** are generated (`adversarial-silhouettes-a/-b`), not
  crop-and-place.
- The whole-cast gate found real system gaps: an unlocked recurring group
  (the robbers → `13-robbers` ensemble sheet) and reserved stacks for every
  state (the bride, both horses).

## Part IV — Pages (48 pages, 81 generations incl. 6 edits)

- Most pages landed on the first or second candidate. Hard ones: p14 (seven
  balloons, two speakers, tails swapped four times; fixed by the advisor's
  restage into full-width panels with fixed lanes), p41 (the ogre drawn twice),
  p46 (the raft: reed base vs "raft of light", then six skulls, then
  separate floating skulls; fixed by an edit past the ceiling).
- `pagerun.py` cannot run an advisor's v4 reset when `max_versions = 4`;
  this book ran at 6 (7 recorded for the p46 edit).
- Codex returned 503 "model at capacity" twice mid-candidate. The supervisor
  in `notes/monkey-king-vol2-run-scripts/supervise.sh` completes the orphaned
  critic and relaunches; use it from the start next time.
- Gates caught what page critics missed: six skulls (cards said the count was
  nonblocking), the night river gone blue (p47), and the gold band drawn on
  Wukong before the cap (pp 14, 15, 18 — whole-book gate). **For III: every
  card where the band matters says "band on" or "band absent" as blocking.**

## Part V — For Volume III

Threads this volume planted or left open:

- **The band comes off in the west** (Guanyin, p22). It is still on at the
  end. The monk promised to say the words only if he must (p23).
- **"Say the word and he goes back in the river. Your choice, not mine."**
  (p44) Wukong has learned to hand the monk the hard call. The next volume's
  natural crisis is the monk making the wrong one.
- **Flower-Fruit Mountain.** Wukong looked back east at it once (p10). His
  monkeys still bring tribute. If he is ever sent away, that is where he goes.
- **The shoe.** Paid off on p47; available as a callback if someone has to
  go back for *him*.
- **Bajie** asked Old Gao to keep his bed made (p37), calls Wukong "big
  brother" to annoy him (p38), and is brave exactly once (pp 41–43).
- **Wujing** walks at the monk's back (p45) and carries the back end of the
  luggage pole; few words, says the worst thing about himself first.
- **The white horse** never speaks again; it looks into streams (p29).
- **Ao Guang** has his son back on the road; Wukong will "tell him next time
  I need tea" (p29).

Source ground for III (Journey to the West ch. 23 onward), as evidence only:
the four sages' test of the pilgrims' resolve (ch 23); the ginseng-fruit
tree at the Temple of the Five Villages (ch 24–26); the White Bone Demon,
three disguises, Wukong sees through each, the monk believes the disguise,
says the words, and banishes him (ch 27); the Yellow Robe Demon, the monk
turned into a tiger, Bajie sent to Flower-Fruit Mountain to fetch Wukong back
(ch 28–31); the Gold and Silver Horned Kings and the gourd that answers to
your name (ch 32–35); the Red Boy (ch 40–42). The White Bone Demon → the
banishment → Bajie going back for him is the strongest single arc: it is the
quarrel at its breaking point, and the shoe turned round.

# The Count of Monte Cristo, Volume III: The King's Attorney — production journal

Started 2026-10-14 from a fully autonomous kickoff (greenlight ① given in
advance), completed 2026-10-15, published to Nano the same day on the owner's
word (commit `255d72d`). Owner's verdict: "i love what ive read of this one.
bravo: great work!" This journal is what the next book — above all Volume IV —
should know. The ship record with numbers is in `RUN-LOG.md`; failure modes
are in `method/07-FAILURE-MODES.md`.

## Part I — The decisions that made the book

**The crime in his own hand.** Dumas lets the Count lend Madame de Villefort a
recipe with deniable intent. Here he puts the vial in her hand on page 8, after
reading her face, with "Keep it, madame. You may need it one day." Every critic
named that page as the book's spine. It turns the volume from a puzzle into a
bill: every death after p8 is charged to him, and the book never lets him off
it (p30 "I know because I gave it to her", p53 "where he had put it himself").
**Lesson:** a sequel keeps the parent's appetite only if the protagonist's
worst act is on the page, early, done with pleasure — not discovered later.

**One move, repeated: Villefort buries things.** The spine was a single verb.
A sailor (1815), a newborn (1817), a poisoner (now), and at the end he digs
in the wrong garden. Each scene was built to show that move once more ("Stop.
Don't tell me."), and the Count's counter-move is digging up: the box, the
prince at dinner, Valentine from the tomb. **Lesson:** an antagonist the reader
"understands completely" is one gesture, shown in three costumes.

**Mirrors that cost nothing.** The runaway horses (p7) are the Count's doing,
and he saves the boy with one drop; the boy dies of the same vial. Morrel's
pistol case at eleven o'clock (Volume I) comes back in his son's hands on p55
("And at five minutes to eleven, a stranger came." / "How do you know…?").
Volume II's last word, "One.", becomes the word he cannot follow: "Two." None
of these needed a page of its own; each was one image or one line.

**The hard call.** The boy's death stayed in. Told, never drawn: a closed door,
a tin hussar on the floor, the faces in the corridor, and the Count picking up
the toy. Unnamed, no balloons, with a reference sheet so the reader meets him
in pictures (p10 showing the Count the hussar under his father's hand; p25
pressing it into the Count's palm; p41 his father's one gentle line). The
cold readers felt the loss without the book ever showing it.

**Withheld, not spent.** Valentine lives but does not wake; Maximilien is
asked for one month; Danglars is "counting his money"; Haydée puts her hand on
his sleeve once and looks at the hussar once. Volume IV gets all of it intact.

## Part II — What the script critics taught (10 rounds)

Findings ran 15 / 3 / 2 / 2 / 3 / 3 / 1, APPROVED-NONE at round 8, then one
factual fix (a night count) reopened it, round 9 found one real contradiction,
and round 10 approved with none. Every critic called it alive from round 1;
the findings were almost all **knowledge and convention holes**, the kind a
sharp ten-year-old asks out loud:

- **Who knows what, and how?** Round after round: how does the Count know
  Villefort chose not to ask (only public facts may be cited); how does
  Noirtier know who the poisoner is (fixed by having Héloïse dose the milk *in
  front of him*, "the one man in the house who could not tell"); how does the
  Count know about Noirtier's medicine (Valentine tells him; he smells the
  glass); how does Haydée know about the milk. **Every deduction needs its
  clue on the page, in front of the character who uses it.**
- **A mute character's rule must be kept literally.** Noirtier answers yes
  with one long blink and no with many; the asker speaks the answer. Three
  critics flagged every slip — a "No. Don't tell me." that read as Noirtier's
  answer, a "Yes." with no question, and finally "you're the one man who
  can't tell anyone" from a man who had just spelled HÉLOÏSE. The last fix was
  better than the original: "You have kept my name since the day I told you.
  Keep this one too."
- **The protagonist's biggest choice must be dramatized, not narrated.** The
  decision to let the house burn began as a prose page; round 2 asked for a
  scene. The new p17 (Haydée asks him to take the bottle back; "I want to hear
  it fall, Haydée. Every floor of it."; "That is what you said about the boy in
  the carriage.") became the critics' favourite page. Same in round 5: the
  first death needed the Count's own reckoning (new p26, "Did you see the
  milk?"). Both additions were Haydée scenes. **The confidant earns her pages
  by asking the plain question at each hinge.**
- **A boast must be said aloud before it can be thrown back.** Haydée quoted
  "nothing would happen there that I didn't see" before the Count had said it
  to her; the line was moved from private prose into his mouth on p17.
- **Name a returning face in rendered text once** (Fernand = the Count de
  Morcerf; Héloïse's first name before Noirtier spells it).
- **Five-word balloons survived every audit** because each answered a complete
  question in the same panel ("To fathers." / "You didn't look." / "One
  month.").

## Part III — References (34 locks, 42 generations, 3 gate rounds)

- **Sequel sheets from parent locks were cheap.** The Count, Villefort and
  Haydée were continuity passes on Volume II's approved sheets (no ageing);
  Noirtier was aged 23 years from Volume I's two-figure sheet with "the man
  with the cavalry moustache and green coat; the other man is never drawn" —
  locked first time.
- **The unnamed son got a full sheet** and the gate made us name his nearest
  lookalike (his mother: same eyes, hair and violet palette on purpose).
- **Every character pair passed every gate round.** The three findings rounds
  were all about proof boards: the deterministic silhouette board's fixed
  quarter crop fails on sheets whose views are not in exact quarters and whose
  painted grounds defeat thresholding; generated silhouette boards keep
  interior marks unless solid-filled afterwards. `boards.py` was tried and
  restored byte-identical; the fix was generated boards plus a deterministic
  fill.
- **Parallel workers again saved hours:** main `--all` for characters and
  boards, a plates worker in reverse order, main stopped after the live-pair
  lock. The page run started while the reference regate was still running,
  because the open findings touched only critic-only boards.

## Part IV — Pages (56 pages, 69 generations, 51 on the first candidate)

- **Packets by seven parallel writers** from a script-derived state table
  (who is on each page, costume state, object state, which plate). Every page
  attached one to three inputs; no page ever montaged.
- **The two real defects the page critics missed were caught by batch gates:**
  p23 drifted into a soft, pale finish unlike its neighbours (regenerated with
  a register note in its prompt source); p37 drew Villefort with the Count's
  face at a wide funeral panel — two Counts, no Villefort. The first edit
  fixed the face; the cold read still tripped; the second edit made Villefort
  bareheaded and silver-grey and pushed the Count small to the back. Promoted
  to method/07 (seen twice with Beowulf's poet).
- **p55 is the router working:** v1 off-script, v2 perfect but "u stranger",
  the full reset v3 passed. Had v3 failed, v2 plus a one-letter edit was ready.
- **Whole-book gates as work lists:** "Volume Iii", "iis eyes", the hussar
  unmounted on two pages, a stray accent on "Mademoiselle". Each fixed by
  `--edit`, each letter fix verified by a fresh one-line transcription, each
  touched batch regated, and a fresh whole-book gate run again until it found
  nothing.
- **An edit critic can re-judge composition the edit never touched** (p26:
  the word was fixed, the critic blocked on hierarchy that had passed four
  earlier gates). Promoted by advisor override with the reason beside the
  report.

## Part V — For Volume IV

Planted, unspent, and waiting: Danglars ("let him count it a little longer");
Valentine asleep in the Count's house, her hand just closed; Maximilien's
month and the pistol case; "How do you know it was five to eleven?"; Haydée's
hand on his sleeve and her look at the hussar; Benedetto "the most famous
prisoner in France"; Noirtier, who wished he had stopped him; and a man who no
longer knows whether God is on his side. Volume IV's brief already owns
Danglars' ruin, Haydée's ending, the renunciation, and Valentine's return. The
kickoff is `notes/NEXT-SESSION-MONTE-CRISTO-VOL4.md`.

# Builder receipt — Three Kingdoms, Volume I reader

**Built:** `books/three-kingdoms-vol1/index.html`, a single-file reader for the 50 canonical
pages `pages/page-01.png` … `pages/page-50.png`. No page or reference image was touched.

**Adapted from** `books/three-musketeers-vol1/index.html`. Its structure, CSS, and script were
copied whole, then given the new identity:

- the title, the description meta, the top-bar identity (plus a screen-reader-only `<h1>` with the full title),
  the image alt text, and the movement label prefix now read
  `Three Kingdoms, Volume I: The Peach Garden Oath` / `The Peach Garden Oath`;
- the 50-title `titles` array and the seven-movement `movements` array, exactly as in BUILDER.md;
- the storage keys `monte_inspired:three-kingdoms-vol1:page` / `:bookmarks`;
- the routing boundaries `#page-51` → end and `#page-52` → quiz (all other routing lines are
  unchanged and match the verifier's exact strings);
- the progress-bar initial width is 1/52, and the static "Page 1 of 50" / "Volume I · 50 pages" labels;
- the end state (`End of Volume I`) has a new summary, and Volume II is mentioned as text only with no link;
- the quiz (`Test your understanding`) has five new cause-and-choice questions drawn from the script
  (bait plan p9–10, the rice snub p15, the old man on the road p28, the warm cup p34–36, three
  against Lü Bu p44–46), each with three options, one `data-answer`, and plain feedback for
  right and wrong answers.

**Preserved unchanged:** the responsive 2:3 stage, the previous/next buttons and page-edge tap zones,
keyboard and swipe navigation, exact `#page-N` links and the saved position, the movement contents,
device-local bookmarks with quick return, adjacent preloading, fullscreen, the zoom dialog
(fit/125/150/200/250/300%, pan, double-click, page navigation inside zoom), and the race-safe loading
(`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`).

The template had no library link or other-volume link, so there were none to remove.

**Could not preserve:** nothing.

**Checks:** `verify-reader.py` printed CLEAN, and `node --check` on the script passed.

## Correction round (2026-10-05)

Reader-critic nonblocking notes addressed in `index.html` only (no images or other files touched):

1. Quiz options rewritten so all three options per question are similar in length (62–68 characters) and plausible; correct letters now c, a, b, c, a. Correct answers and feedback checked against the lines in `08-FULL-SCRIPT.md` (the ambush plan, the bag of rice, the road outside the farm, the cup of wine, the three against Lü Bu, Yuan Shao's claim); incorrect-feedback for Q3 and Q5 lightly extended to address the new distractors.
2. `#quizScore` now shows a running score ("N of 5 correct so far (M of 5 checked)", then "Final score: N of 5 correct").
3. End card has a visible "Test your understanding →" button (`#endQuizLink`, href `#quiz`) in addition to the → arrow.
4. "Check answer" with nothing selected shows a gentle prompt ("Pick one of the answers first, then press Check answer."), hidden once an option is chosen. Answers still lock after checking.

Verification: `verify-reader.py` → CLEAN; `node --check` on the extracted script → OK.

## Correction round 2 (2026-10-05, managing session)

Reader critic round 2 (REVISE, 1 finding): the correct option was still the longest in Q1, Q2, Q3, Q5. Shortened those four correct options (keys and feedback unchanged) then shortened some wrong options so no length strategy wins: the correct option is longest in one question, shortest in one, and middle in three; verify-reader CLEAN.

## Correction round 3 (2026-10-05, managing session)

Reader critic round 3 (REVISE, 1 finding): Q3's stem was ambiguous about whose family died; rewritten as the critic suggested ("Cao Cao has just killed the old man's whole family by mistake."). Also taken from its nonblocking notes: keyboard shortcuts now ignore Ctrl/Cmd/Alt combinations; Q5's option "Yuan Shao's guards drive him back to the gate" shortened so no length strategy (longest, shortest, middle) scores more than 2 of 5. verify-reader CLEAN.

## Correction round 4 (2026-10-05, managing session)

Reader critic round 4 (REVISE, 1 finding): on narrow screens the fixed Prev/Next bar covered the quiz's final score. Added `.reader-status-card { padding-bottom: calc(80px + env(safe-area-inset-bottom)); }` inside the 860 px media block, as prescribed. Nonblocking taken: Q2 "grab his wrist" → "grab his hand", to match the art. verify-reader CLEAN.

## Correction round 5 (2026-10-05, managing session)

Reader critic round 5 (REVISE, 1 finding): Q2's stem ("grab his hand… the snub hurt him too") could attach "his" to Dong Zhuo. Rewritten as prescribed: "Why does Liu Bei grab Zhang Fei's hand, even though Liu Bei is angry too?" verify-reader CLEAN.

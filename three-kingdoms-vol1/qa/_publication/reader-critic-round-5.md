# Three Kingdoms, Volume I — reader critic report

Inspected: `index.html` (read in full), `verify-reader.py` output (`CLEAN`),
page proofs 09, 10, 15, 28, 34, 36, 44, 45, 46, 47, 48 to check the quiz
against the story. I did not open prompts, audits, candidates, earlier QA
reports or the builder receipt.

## Checks

1. **Page 1, file mapping.** With no hash and no saved position, the page
   opens on index 0: `pages/page-01.png`, "The Yellow Sky", "Page 1 of 50",
   movement "The Peach Garden Oath · The Peach Garden". `fileFor` zero-pads
   1–50. `titles.length === 50`, preloads stay inside 0–49, and no code path
   reaches a page-51 image. Pass.
2. **Navigation at both ends.** `#page-1` goes to index 0 and `#page-50` to 49.
   `#end` and `#page-51` go to the end state (50); `#quiz` and `#page-52` go
   to the quiz (51). An out-of-range hash (`#page-99`) falls back to the saved
   page, and the URL is rewritten to match. Prev is disabled on Page 1 and
   next is disabled on the quiz. Arrow keys, PageUp/PageDown, Home/End, the
   page-edge tap zones and swipes all go through `goPrevious`/`goNext`. Space
   turns the page only on story pages, so on the end and quiz screens it
   scrolls. The saved position is capped at 49. Pass.
3. **Contents and bookmarks.** The seven movements cover 1–9, 10–16, 17–22,
   23–30, 31–38, 39–46 and 47–50: contiguous, each page listed exactly once.
   Bookmarks are stored under `monte_inspired:three-kingdoms-vol1:bookmarks`
   and the position under `…:page`. Saved values are filtered to 0–49. The
   end and quiz screens cannot be bookmarked. Pass.
4. **Zoom.** Opens at 150% (the third level, index 2), horizontally centered,
   at the top of the page. Levels are Fit, 125, 150, 200, 250 and 300%. You
   can pan with the scrollbar, with a mouse drag, or with native touch
   pan/pinch. In-zoom prev/next are disabled at Page 1 and Page 50.
   Esc or × closes it. Nonblocking: changing pages while zoomed resets the
   scroll to the top-left corner rather than re-centering it. On a phone at
   150% the new page therefore starts at its left edge, which is also where
   reading starts.
5. **Ending and quiz.** Page 50 leads to "End of Volume I" (counter "End"),
   then to the quiz (counter "Quiz"). Neither is called Page 51. The ending's
   only link is `#quiz`, and it says the story continues in Volume II without
   linking to anything unpublished. Pass.
6. **Quiz.**
   - Every question has exactly one correct answer, and the answers agree with
     the pages:
     - Q1 matches p9 ("That's why they'll chase me").
     - Q2 matches p15 ("Kill him and we are the rebels").
     - Q3 matches p28.
     - Q4 matches p34/36 ("I will be back before it is cold", "still warm").
     - Q5 matches p45, and its feedback about Yuan Shao's false claim matches
       p48.
   - Each question has its own feedback for no choice, a right choice and a
     wrong choice. Answering locks the question, and the score tallies once
     per question and ends with "Final score: N of 5 correct".
   - The questions test causes and choices, not trivia.
   - The correct letters are c, a, b, c, a, so they vary.
   - No simple strategy passes:
     - always the longest answer: 2 of 5 (Q2, Q5)
     - always the shortest: 1 of 5 (Q4)
     - always the middle length: 2 of 5
     - always a: 2 of 5; always b: 1 of 5; always c: 2 of 5
   - One stem is ambiguous; see Finding 1.
7. **Hygiene.** No Monte Cristo or Musketeers terms. No 49-page labels (the
   only "49" is an rgba color value). No duplicate IDs. Every
   `getElementById` target exists. Pass.

**Narrow screens (≤ 860 px).** The fixed prev/next buttons move to the bottom
center. Their top edge sits `max(12px, inset) + 46px` above the bottom of the
screen. The end and quiz cards are given `padding-bottom: 80px + inset`
(base `.reader-status-card` padding is overridden later in the cascade, and
`.quiz-card` sets only `padding-top`). So once the reader scrolls to the
bottom, the final score and the last question clear the buttons, both with
no safe-area inset (58 < 80) and with a 34 px inset (80 < 114). Opening the
quiz scrolls to the top, and its 78 px top padding clears the 65 px top bar.
The fixed bars cover text only while it is passing under them during a
scroll, and no text stays hidden. Above 860 px, the side buttons
(16–66 px) never reach the card's text, which starts at ≥ 84 px. Pass.

## Findings

1. **Q2 stem has an ambiguous pronoun and a hard word.** The stem reads:
   "Zhang Fei wants to go into the tent after him. Why does Liu Bei grab
   his hand, even though the snub hurt him too?"
   - The nearest antecedent of "his" is the "him" just before it, which is
     Dong Zhuo. A child can read it as Liu Bei grabbing Dong Zhuo's hand,
     which is not what p15 shows (Liu Bei grips Zhang Fei's hand on his
     spear). The child then has to work out the scene before answering.
   - "Snub" is the only word in the quiz the reader probably doesn't know,
     and it sits in the clause that carries the emotion.
   - **Correction:** change the stem's last sentence to "Why does Liu Bei grab
     Zhang Fei's hand, even though Liu Bei is angry too?" Answers and feedback
     stay unchanged.

REVISE

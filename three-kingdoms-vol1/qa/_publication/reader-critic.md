# Three Kingdoms, Volume I — reader critic report

Fresh, zero-history review of `books/three-kingdoms-vol1/index.html`. Inputs were the HTML and script, the
`verify-reader.py` output, and the page proofs that the quiz cites (pp. 9, 10, 15, 28, 34, 44, 45), used to check
the quiz facts. I did not open any prompts, audits, candidates, earlier QA reports, or the builder receipt.

## Mechanical
`python3 books/three-kingdoms-vol1/qa/_publication/verify-reader.py` → **CLEAN**. That covers the 50-title manifest,
the seven movement ranges, the storage keys, the exact routing boundary lines, race-safe loading, stale terms, and
IDs: no duplicates and no references to missing IDs. The pages are exactly page-01…page-50 at 1024×1536. A grep for
Monte/Cristo/Musketeer/d'Artagnan/"49" found none.

## Behaviour traced
1. **Page 1:** the static markup and `render(0)` agree. The title is "Three Kingdoms, Volume I: The Peach Garden Oath",
   the counter reads "Page 1 of 50" and the folio reads "The Yellow Sky". The movement label reads "The Peach Garden
   Oath · The Peach Garden". `fileFor(i)` maps 0–49 to `pages/page-01…50.png`. `preload` and `loadPage` never go past
   index 49. The end and quiz states return before any image load.
2. **Routing:** `#page-1`→0 and `#page-50`→49. `#end` (or the alias `#page-51`)→50 is the end state, and `#quiz`
   (or `#page-52`)→51. An out-of-range hash such as `#page-99` gives `null`, so the reader falls back to the saved
   position, which is clamped to 0–49 and then rewritten to `#page-N`. Prev is disabled on page 1. Next on page 50
   goes to End, then to Quiz, and is disabled on the quiz. Tap zones, arrow/PageUp/PageDown keys, swipes, and
   Home/End all go through the same `goNext`/`goPrevious`/`render` functions. Space advances only on story pages.
   The saved position stores `min(current, 49)`, so the end and quiz states are never saved as story pages.
3. **Contents** lists the seven movements with pages 1–50 exactly once. The bookmarks section is separate. Bookmarks
   use `monte_inspired:three-kingdoms-vol1:bookmarks`, filter out anything outside 0–49, and cannot be set from the
   end or quiz states.
4. **Zoom** opens at 150%, scrolled to the top and centred horizontally. The levels are Fit/125/150/200/250/300.
   Panning works by scroll, mouse drag, and native touch, and double-click toggles between Fit and 200%. The zoom
   view has prev/next, which stop at pages 1 and 50. Close uses the native dialog (Esc or ×), and focus returns.
5. **End state:** a non-page "End of Volume I" card with counter "End". Its only link is the in-page `#quiz`, plus a
   text-only promise of Volume II. The quiz has counter "Quiz". Neither is labelled Page 51.
6. **Quiz:** five questions with one `data-answer` each. Each wrong answer gets "Not quite" feedback that explains the
   right answer. The score reads "Final score: N of 5" after all five are checked. All five questions test causes or
   choices, and each one matches the pages: p9 "worst fighter… That's why they'll chase me", p15 "Kill him and we are
   the rebels… hands shaking", p28 "you'll tell the world… betray the whole world", p34 "Pour it and leave it… before
   it is cold", p44–45 Liu Bei rides down and "could not see all of his enemies at once".
   - **The answer key varies:** c, a, b, c, a.
   - **No length strategy passes:** always-longest scores 2/5, always-shortest 1/5, always-middle 2/5. Always-a scores
     2/5, always-b 1/5, always-c 2/5.
   - **Stem pronouns each have one clear referent:** Q2 "after him" is Dong Zhuo. Q3 "he" is Cao Cao. Q4 "him"/"it"
     are Cao Cao and the cup. Q5 "him" is Lü Bu.
7. **Narrow screens (≤ 860 px):** the fixed prev/next buttons sit at bottom centre, 46 px tall at `max(12px, safe-area)`,
   so they reach at most 58 px + safe-area from the bottom. The end and quiz cards have
   `padding-bottom: calc(80px + safe-area)`, so the last quiz question and the final score always scroll clear of
   the buttons. The quiz card's 78 px top padding is more than the fixed top bar (about 65 px). At widths above 860 px
   the side buttons (16–66 px) stay outside the card's text column.

## Nonblocking notes
- Typing an out-of-range hash into an already open reader triggers `hashchange`, which ignores it and leaves the bad
  hash in the URL until the next navigation. Reloading lands on the saved page and corrects it. Cosmetic.

No reproducible reader harm found.

APPROVED

# Three Kingdoms, Volume I — reader critic

Fresh, zero-history review of `books/three-kingdoms-vol1/index.html`. I read the HTML and script closely and ran `verify-reader.py` (output: `CLEAN`). I spot-checked canonical pages 09, 10, 15, 28, 34, 45 and 47 against the quiz. I did not open any prior QA report, prompt, audit, candidate or receipt.

## Checks

1. **Page 1 / file mapping: pass.** With no hash and no saved position, the reader opens on index 0: "The Yellow Sky", "Page 1 of 50", and the movement label "The Peach Garden Oath · The Peach Garden". `fileFor` maps indexes 0–49 to `pages/page-01.png` through `page-50.png`. There are 50 titles. `preload` and `loadPage` never go past index 49, and all 50 files exist.
2. **Navigation at both ends: pass.** Previous is disabled on page 1. Next goes from page 50 to the ending, then to the quiz, and is disabled on the quiz. Tap zones, the arrow, PageUp and PageDown keys, Home and End (End goes to page 50), and horizontal swipes all call the same `goPrevious`/`goNext`. Space advances only on story pages. Arrow keys are ignored while a radio button has focus. A reload on `#page-N` returns to that page. The saved position is clamped to 0–49, so a reload with no hash after the ending reopens page 50. An out-of-range hash at load falls back to the saved position, and `updateUrl` rewrites it.
3. **Contents and bookmarks: pass.** The seven movements cover 1–9, 10–16, 17–22, 23–30, 31–38, 39–46 and 47–50. That is 50 pages, contiguous, each listed once. The storage keys are `monte_inspired:three-kingdoms-vol1:page` and `:bookmarks`. Saved bookmarks are filtered to 0–49. Bookmarking is disabled on the ending and the quiz.
4. **Zoom: pass.** The zoom view opens at 150% (default level index 2), scrolled to the top and centred horizontally. The levels are Fit (1×), 125%, 150%, 200%, 250% and 300%, set with the +/− buttons and keys, 0 for Fit, and double-click. Mouse-drag panning works, and on touch the viewport scrolls natively. Previous and next work inside zoom and are disabled at pages 1 and 50, so zoom never reaches the ending. Close, Escape and the native `<dialog>` return focus cleanly.
5. **Ending and quiz: pass.** `#end` and `#quiz` are separate states that are not pages. Their counters read "End" and "Quiz", never "Page 51". The zoom and bookmark buttons are disabled on them. The ending's only link is `#quiz`. "Volume II" appears as plain text, not a link.
6. **Quiz content: one finding (below).** Every question has exactly one correct answer. Each feedback text matches its key, and each question asks about a cause or a choice: the bait plan (p.9), "Kill him and we are the rebels" (p.15), the old man and "tell the world" (p.28), "before it is cold" (p.34), and three against one (p.45). The answers match the pages, and the language is plain enough for a seven-year-old. The correct letters vary: c, a, b, c, a.
7. **Hygiene: pass.** There are no duplicate IDs, and every `getElementById` target exists. No Monte Cristo or Musketeers terms remain, and nothing says 49 pages. The only "monte" strings are the workspace storage-key prefix `monte_inspired`.

## Findings

1. **A reader who always picks the longest option scores 4 of 5.** By character count, the correct option is the longest in Q1 (c: 68 vs 65/64), Q2 (a: 66 vs 64/64), Q3 (b: 67 vs 64/63) and Q5 (a: 66, longest by a single character). Only Q4 escapes, because its correct answer (c) is the shortest. So the quiz can be passed without reading the story, and a child who notices the pattern learns to guess instead of remembering why the characters acted. **Correction:** rebalance the option wording, changing no answer keys or feedback, so that the correct option is the strictly longest in at most one question. For example, lengthen a wrong option in Q1, Q2, Q3 and Q5 so it clearly outruns the correct one, or shorten the correct option. Then re-run this length check.

Nonblocking notes:
- A mid-session hashchange to an out-of-range hash is ignored, and the stale hash stays in the address bar.
- Changing page inside zoom at 150% on narrow screens resets the scroll to the left edge rather than centring.

REVISE

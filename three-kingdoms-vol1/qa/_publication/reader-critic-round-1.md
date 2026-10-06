# Three Kingdoms, Volume I — reader critic report

Fresh, zero-history review of `books/three-kingdoms-vol1/index.html`, read without a browser, by tracing the script by hand. `verify-reader.py` returns `CLEAN` (exit 0). Production prompts, audits, candidates, QA reports and the builder receipt were not opened. Pages were viewed only to check the quiz against the story (pp. 9, 10, 15, 28, 36, 45–48).

## 1. Page 1, counter, movement, file mapping — pass
- With no hash and no saved position, `savedIndex()` returns 0. `render(0, true)` sets the title "The Yellow Sky", the counter "Page 1 of 50" and the movement line "The Peach Garden Oath · The Peach Garden". The regex `^\w+ · ` strips the Roman numeral, which also works for "VI · Lü Bu".
- `fileFor(i)` maps to `pages/page-NN.png` for i 0–49. `preload` and `loadPage` are only reached for indices below `titles.length`, so no page-51 file is ever requested. The disk holds exactly page-01 through page-50 at 1024×1536 (verifier).

## 2. Navigation at both ends — pass
- `#page-1` maps to 0 and `#page-50` to 49. `#end` and `#page-51` map to 50, the end state. `#quiz` and `#page-52` map to 51, the quiz. An out-of-range hash (`#page-0`, `#page-99`) maps to null: on load the reader falls back to the saved position or page 1 and `updateUrl` rewrites the hash, and on `hashchange` it is ignored.
- Prev is disabled at index 0 and next at the quiz (index 51). The arrow buttons, tap zones, ArrowLeft/Right, PageUp/Down and swipes all go through `goPrevious`/`goNext` with bounds checks. Space only advances on story pages. Home goes to page 1 and End to page 50. Keys are ignored while focus is on a quiz radio button, so answering does not turn the page.
- `savePosition` clamps to 49, so reloading after the end or quiz reopens page 50 and never a phantom page.

## 3. Contents and bookmarks — pass
- `buildContents` walks the seven movements (1–9, 10–16, 17–22, 23–30, 31–38, 39–46, 47–50). That is every page from 1 to 50 exactly once, and the verifier confirms the ranges.
- Bookmarks are kept as a Set of indices under `monte_inspired:three-kingdoms-vol1:bookmarks`, filtered to 0–49 on load. The position key is `monte_inspired:three-kingdoms-vol1:page`. Bookmarking is disabled in the end and quiz states.

## 4. Zoom — pass
- `openZoom` opens at 150% (`DEFAULT_ZOOM_INDEX` 2), centered horizontally and at the top of the page. The levels are Fit, 125, 150, 200, 250 and 300%, controlled by the buttons, `+`/`-`/`0` and double-click. You can move around by scrolling or by dragging with the mouse; touch pan and pinch are allowed.
- While zoomed, prev/next render the neighbouring page and reset the scroll. Next is disabled at page 50, so zoom never shows the end state. The bookmark button and `b` work in zoom. The close button and Esc (native dialog) return to the reader without changing state. Zoom is disabled in the end and quiz states.

## 5. End and quiz states — pass
- From page 50, next shows the end card: counter "End", page frame hidden, nothing marked as Page 51. Next again shows the quiz: counter "Quiz", scrolled to the top. The end card says "The story continues in Volume II." with no link, so nothing unpublished is linked.

## 6. Quiz — pass
- Each question has exactly one correct answer (b, c, a, b, c), and the right feedback paragraph shows for the choice made. All five ask about a cause or a choice: the bait plan, holding back from Dong Zhuo, Cao Cao's betrayal, the cup of wine as a promise, three against one.
- I checked every claim against the pages: "That's why they'll chase me" / between the hills (p. 9), "He wears the emperor's armor… Kill him and we are the rebels" and the shaking hands (p. 15), the old man with the wine and the "betray the whole world" line (p. 28), "still warm" (p. 36), "could not see all of his enemies at once" (p. 45), Yuan Shao telling the camp his guards drove Lü Bu off (p. 48). The language is plain enough for a seven-year-old to follow.

## 7. Hygiene — pass
- No Monte Cristo or Musketeers terms or keys, no "49 pages" labels, no duplicate IDs, and no `getElementById` call refers to a missing ID. The verifier confirms all of this, and a manual grep found nothing.

## Nonblocking notes
- In all five questions the correct option is clearly the longest, so a reader who always picks the longest answer gets 5/5 without reading. A later pass could make the distractors as long and specific as the right answers.
- `#quizScore` is never filled in. The end card has no in-card "Take the quiz" link; the → arrow is the only way to reach the quiz.
- Once an answer is checked it cannot be changed. Pressing Check with nothing selected does nothing and shows no prompt.

APPROVED

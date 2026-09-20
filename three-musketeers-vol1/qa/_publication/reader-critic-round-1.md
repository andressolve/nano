VERDICT: REVISE

# The Three Musketeers, Volume I — reader critic report

Reviewed `books/three-musketeers-vol1/index.html` (1466 lines) by close reading of markup, CSS, and script, with no browser. Verifier output, last line: `CLEAN`. Mechanical checks I repeated independently: 49 titles, seven contiguous movements (1–7, 8–16, 17–22, 23–27, 28–35, 36–40, 41–49) covering every page exactly once; `pages/page-01.png` … `page-49.png` present and `fileFor()` cannot address anything beyond index 48 from the hash; no duplicate element IDs; every `getElementById` target exists; no Monte Cristo terms, keys, or links; storage keys are `monte_inspired:three-musketeers-vol1:page` / `:bookmarks`; the ending card links nowhere ("The story continues in Volume II." is plain text). Page 1 renders with title "The Yellow Horse", counter "Page 1 of 49", movement label "The Queen's Diamonds · The Yellow Horse". Hash routing: `#page-1`→0, `#page-49`→48, `#end`→49 (End), `#quiz`→50 (Quiz), out-of-range or malformed hashes fall to the saved position and the URL is rewritten. Quiz: five questions, one `data-answer` each, matching correct/incorrect feedback, all five test causes or choices (why he draws, why only two diamonds, why nobody reads the letter, why the jeweler, what the Cardinal learns). Those parts hold. The defects below are in the two non-page states and in two fallbacks.

## Blocking findings

1. **`index.html` line ~366, CSS `body.reader-state .reader-status-card { display: block !important; }`** — This selector matches both `#endState` and `#quizState`, and `!important` overrides the UA `[hidden] { display: none }` rule. So in the End state the whole quiz is visible beneath the ending card, and in the Quiz state the ending card is visible above the quiz: pressing Next on the End screen changes only the counter text ("End" → "Quiz") with no visible change on the page. The ending and the quiz are not two states as item 5 requires; they are one long page shown twice. Fix: delete the `!important` rule (sections are block by default and `hidden` already handles visibility), or change it to `body.reader-state .reader-status-card:not([hidden]) { display: block; }`, and on entering the Quiz state call `window.scrollTo(0, 0)`.

2. **`index.html` `openZoom()` (~line 1298) and the `z` key / Zoom button / center tap** — Nothing stops zoom from opening in the End or Quiz state. Reproduce: go to `#end`, press Z or click Zoom. `updateZoomPage()` reads `titles[49]` → the zoom header shows "undefined" and "Page 50 of 49", and because `displayedPage !== current` the viewport is put into `Loading Page 50…` with the image hidden, and nothing ever clears it. The reader is stuck on a broken modal until Escape. Fix: at the top of `openZoom()` add `if (current >= titles.length) return;`, and in `render()` set `zoomButton.disabled = !isStory` (also guard the `z` key on the same condition).

3. **`index.html` `toggleBookmark()` (~line 1056), the topbar Bookmark button and `b` key** — Also unguarded in the non-page states. Reproduce: on `#end` press B. The toast says "Bookmarked Page 50", and the Contents bookmarks section gains a row reading "50 undefined" (from `titles[49]`), which is exactly the Page 50 label item 5 forbids. The bad entry survives the visit; only a reload filters it. Fix: `if (current >= titles.length) return;` at the top of `toggleBookmark()`, and `bookmarkButton.disabled = !isStory` in `render()`.

4. **`index.html` `savedIndex()` (~line 919)** — The fallback for "no usable saved position" is `titles.length - 1`, i.e. Page 49, the ending. It fires whenever `localStorage` throws (Chrome/Edge with site data blocked, Firefox with storage disabled, some embedded/private contexts) or whenever the stored value is not an integer in range. A first-time reader in such a browser opens the book on the last page. Fix: return `0` in both the out-of-range branch and the `catch` branch (clamp to 48 only if you specifically want over-range integers to land on the last page).

5. **`index.html` keydown handler (~line 1374), `targetIsControl` guard** — The guard skips all reader keys when `event.target` is any `button`. In Chrome, clicking Next, Previous, a page-edge tap zone, the Contents button (and returning from the Contents dialog) leaves that button focused, so Arrow Left/Right, PageUp/Down, Home/End, Z, C, B, F all go dead until the reader clicks elsewhere. The common flow "click the page edge once, then use the arrow keys" silently fails. Fix: narrow the guard to text-entry and radio controls (`input, select, textarea`), or on click of the nav/tap buttons call `event.currentTarget.blur()`.

## Nonblocking

- `#quizScore` exists but is never written; the quiz gives per-question feedback and no total. Fine as is, or tally it.
- Clicking "Check answer" with nothing selected does nothing; a short "Pick an answer first" would help a seven-year-old.
- In all five questions the correct choice is the longest option; a tell for older readers. Consider trimming the correct answers to the length of the distractors.
- Q2 option (b) ("must be caught short at the ball, not robbed") is the densest phrasing in the quiz; simpler wording would suit the younger reader.
- In the Quiz state, Space is `preventDefault`ed (Next is disabled there), so Space no longer scrolls the quiz. Guard Space to story pages.
- Window resize inside zoom resets scroll to top-center; preserving the center would be kinder on tablet rotation.
- `updateUrl()` deletes a `set` query parameter that nothing in this reader uses.
- `#page-50` / `#page-51` are accepted as aliases for `#end` / `#quiz` (rewritten immediately); harmless, but they can be dropped once nothing links to them.
- Initial CSS progress width is `100% / 49` while the script uses `pageNumber / 51`; a one-frame mismatch on first paint.
- In the End/Quiz states `setLoadingState(pageFrame, 50/51, false)` writes "Loading Page 50…" into hidden elements. Invisible today, but it is the label that would leak if finding 1 is fixed carelessly; pass the story-only label there.

Verifier last line: `CLEAN`

REVISE

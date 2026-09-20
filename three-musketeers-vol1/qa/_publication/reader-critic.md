VERDICT: APPROVED

**Reader critic — The Three Musketeers, Volume I (`books/three-musketeers-vol1/index.html`)**
Fresh review, no prior report consulted. No files written or edited (per the spawning instruction; `reader-critic.md` was not created). Verified against `pages/page-01.png`–`page-49.png` (opened page 1 and page 49 proofs only).

`verify-reader.py` last line: `CLEAN`

**Blocking findings:** none.

**What was traced and confirmed**

1. **Page 1 / page mapping.** Static HTML ships `pages/page-01.png`, title "The Yellow Horse", counter "Page 1 of 49"; `render(0, true)` at load sets movement label "The Queen's Diamonds · The Yellow Horse". `fileFor(index)` is only reached for `current < titles.length`; `titles` has exactly 49 unique entries matching the manifest, so nothing beyond `page-49.png` is ever requested. Page 1 proof is the title page; page 49 proof carries "End of Volume I" — both match the reader's identity.
2. **Hash routing** (functions executed in Node): `#page-1`→0, `#page-49`→48, `#end`→49 (End), `#quiz`→50 (Quiz); `#page-0`, `#page-52`, `#page-99`, `#50`, `#foo`, `#page-1a` → `null` → falls to saved position, and `updateUrl()` rewrites the bar to the canonical hash. `#page-50`/`#page-51` alias to End/Quiz and are rewritten to `#end`/`#quiz`, so "Page 50" never appears anywhere. `hashchange` re-renders only for valid, different indexes; `replaceState` doesn't fire it, so no loops.
3. **End and Quiz mutually exclusive.** `render()` sets `endState.hidden = current !== 49` and `quizState.hidden = current !== 50` on every render; CSS only shows `.reader-status-card:not([hidden])` under `body.reader-state`, and `main` is hidden in that state. Exactly one of {page frame, End, Quiz} is visible for every index 0–50. `prev`/`next` are enabled/disabled correctly at index 0 and 50; End→next→Quiz; Quiz→next is a no-op; ArrowLeft from End returns to page 49 with no reload flash (`isAlreadyDisplayed` path).
4. **Zoom and bookmark disabled in End/Quiz.** Buttons: `zoomButton.disabled = bookmarkButton.disabled = !isStory`. Keyboard: `z` and `b` are guarded by `current < titles.length`; `openZoom()` and `toggleBookmark()` also return early on their own, so no path (tap zone, key, zoom-dialog `b`) can bookmark or zoom a non-page. `zoomNext` is disabled at page 49, so the zoom view cannot step into the End state.
5. **Saved-position fallback.** `savedIndex()` wraps `localStorage` in try/catch → 0 when storage throws; `Number()` + `Number.isInteger` + range check → 0 for `null`, `""`, `"abc"`, `"-1"`, `"12.5"`, `"49"`, `"Infinity"`. `savePosition()` stores `min(current, 48)`, so finishing the book saves page 49, not End; hash always takes precedence over storage. Bookmarks: `loadBookmarks` filters non-integers and out-of-range values, tolerates parse errors and non-arrays; keys are exactly `monte_inspired:three-musketeers-vol1:page` / `:bookmarks`.
6. **Keyboard after a button click.** Keydown lives on `document` and only bails for `input, select, textarea` or open dialogs, so arrows/PageUp/PageDown/Home/End work with focus on `next`, `prev`, a tap zone, or the Contents button after a click. Space is intercepted with `preventDefault` on keydown while on a story page (button never goes active, so no double-advance); on End/Quiz Space falls through to native button activation, which is the expected behavior for a focused control. Buttons that become disabled (`next` at Quiz, `check` after answering) drop focus to body and the document listener keeps working. Quiz radios keep native arrow-key behavior because of the control guard.
7. **Contents.** Seven movements 1–7, 8–16, 17–22, 23–27, 28–35, 36–40, 41–49 are contiguous and cover 1–49 exactly once; bookmarks section renders only when non-empty; `aria-current` scroll-into-view on open; selecting an entry closes the dialog and renders.
8. **Zoom.** Opens at 150% (`DEFAULT_ZOOM_INDEX = 2`), horizontally centered, top-aligned; levels Fit/125/150/200/250/300; wheel/scroll pan, mouse drag pan, double-click Fit↔200%, `+`/`-`/`0` keys, prev/next inside the view update `zoomImage` through the same race-safe `renderRequest` path; `×`/Escape close and focus returns to the opener.
9. **Quiz.** Five questions, each with three options, one `data-answer` present among the option values (c, b, a, c, b — position varies), matching correct/incorrect feedback, inputs and button locked after checking. All five test causes/choices (why he draws, why two diamonds, why not read the letter, why the jeweler, what the Cardinal learns) in plain sentences.
10. **Hygiene.** No duplicate IDs; every `getElementById` target exists; no "Monte Cristo", "Dantès", "Morcerf", "nano", library/other-volume anchors, or `page-50` references; End state has no links ("The story continues in Volume II." is text only). "Volume I · 49 pages" and "of 49" are correct for this 49-page book.

**Nonblocking observations**

- Progress bar: JS uses `pageNumber / 51`, so page 49 shows ~96% and only the Quiz reaches 100%; the CSS initial width `100% / 49` also differs from the JS first value (1/51) by a hair. Cosmetic.
- In End/Quiz, the disabled Zoom and Bookmark toolbar buttons have no `:disabled` styling and still show hover color, so they look live though they are inert. A `.tool:disabled { opacity: .3; cursor: default }` rule would make the state visible.
- "Check answer" with no option selected does nothing silently; a one-line "Pick an answer first" status would help a seven-year-old. `#quizScore` exists but is never populated.
- In all five questions the correct option is also the longest; a test-savvy ten-year-old can pattern-match. Consider trimming the correct options or padding a distractor.
- Zoom page navigation resets scroll to `left: 0` rather than horizontal center, which is noticeable only on narrow screens where 150% exceeds the viewport width.
- Very narrow race: if Zoom is opened between the main image's `load` and its `decode()` completing, the zoom viewport can clear its loading state while still holding the previous page's `src`. Practically a few milliseconds; closing and reopening Zoom (or any page step) corrects it.
- `updateUrl()` deletes a `set` query parameter that nothing in this reader uses (template leftover; harmless).
- Editing the URL to an invalid hash (e.g. `#page-99`) while already loaded leaves the bad hash in the bar because `hashchange` ignores `null`; the reader itself stays on the correct page.

*(Round 2, saved verbatim by the orchestrating session. Round 1 is in reader-critic-round-1.md.)*

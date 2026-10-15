# Beowulf reader critic — fresh independent review

Inputs: `books/beowulf-vol1/index.html` (read and traced in full), `verify-reader.py` output (`CLEAN`), and proofs of pages 5, 6, 27, 33, 34, 35, 41, 44, 47, 48 and 57, opened only to check the quiz and ending claims against the book. I did not open the builder receipt, prompts, audits, candidates or QA reports.

## Criteria traced

1. **Load and file mapping: pass.** `titles` has 57 entries. `fileFor(i)` gives `pages/page-01.png` through `page-57.png`, and `preload` stops at `titles.length`. With no hash and no saved position, the reader opens on Page 1, "Something in the Fen", with the counter "Page 1 of 57" and the movement label "The Hall, the Mere, and the Dragon · The Hall That Sang".
2. **Navigation at both ends: pass.** Previous is disabled at index 0, and Next is disabled only on the quiz. The page-edge tap zones, arrow keys, PageUp/PageDown, Space (story pages only), Home/End and horizontal swipe all go through `goPrevious` and `goNext`. Each render replaces the URL with `#page-N`, `#end` or `#quiz`, so reloading returns to the same place. The saved position is clamped to 56, so a reload without a hash never lands on an unpublished page.
3. **Contents and bookmarks: pass.** The seven movements cover 1–7, 8–14, 15–23, 24–32, 33–36, 37–42 and 43–57, so each of the 57 pages appears exactly once with no gaps. Bookmarks persist under `monte_inspired:beowulf-vol1:bookmarks` and the position under `monte_inspired:beowulf-vol1:page`. Both are filtered to the range 0–56.
4. **Zoom: pass.** Zoom opens at 150% (`DEFAULT_ZOOM_INDEX` 2), centred horizontally and scrolled to the top. The levels are Fit, 125%, 150%, 200%, 250% and 300%. It supports +, −, Fit and 0, double-click, mouse drag-pan, native scroll and pinch, and Previous/Next inside zoom (disabled at the ends). The bookmark works inside zoom. Close uses × or Esc, and the zoom cannot open on the End or Quiz screens.
5. **End and quiz: pass, except for finding 1.** After Page 57, Next goes to the End screen (counter "End", no page image), then to the five-question quiz (counter "Quiz"). The ending links only to `#quiz`, gives no volume number and promises no sequel.
6. **Chronicle pages: pass.** Pages 7, 14, 23, 36, 42 and 57 are ordinary entries with their titles, counted and routed like the rest.
7. **Quiz: pass.** The answers are q1 c, q2 a, q3 b, q4 a and q5 c, and each question has exactly one correct option. I checked the key lines against the pages:
   - the father's debt on p6
   - "It's a good sword… generous man to lend it" on p33
   - "For fifty years they've sung…" on p44
   - "we promised to stand by him" on p47
   - "Every time" and "our family always stands by you" on p41
   - "So am I. I came anyway" on p48
   - one manuscript, two scribes, the 1731 fire and the British Library on p57

   Questions 1–4 ask about causes and choices. The Chronicle question adds to the story without debunking it. A seven-year-old can follow the wording. Check-answer, the "pick one first" prompt, and the score all work.
8. **Hygiene: pass, except for finding 1.** There are no Monte Cristo, Three Musketeers, Three Kingdoms or King Arthur terms or links. Element IDs are not duplicated, and every `getElementById` target exists.

## Findings

1. **BLOCKING: out-of-range page hashes open the End and Quiz screens as if they were Pages 58 and 59.**
   - **Where:** `indexFromHash()` contains `if (hash === END_HASH || hash === "#page-58") return titles.length;` and `if (hash === QUIZ_HASH || hash === "#page-59") return titles.length + 1;`.
   - **To reproduce:** opening `index.html#page-58` shows "The End", and `index.html#page-59` shows the quiz. `#page-60` falls back to the saved page, so out-of-range hashes are not handled consistently.
   - **Why it matters:** the routing treats the ending as Page 58, which criterion 5 forbids. `#page-59` is left over from the 59-page King Arthur reader, which criterion 8 forbids. A mistyped or old link drops the reader on the ending, past the story.
   - **Correction:** delete the two `"#page-58"` and `"#page-59"` clauses so that only `#end` and `#quiz` reach those screens. Pages 58 and above then fall back to the saved position like any other out-of-range hash.
2. **Nonblocking: leftover 59-page progress width.** The CSS sets `.progress { width: calc(100% / 61); }`, and 61 = 59 + 2 from the earlier book. `render()` overwrites it right away with `pageNumber / 59`, so a reader never sees the wrong value. Suggested fix: change it to `calc(100% / 59)`.
3. **Nonblocking: an invalid hash entered mid-session stays in the address bar.** `hashchange` ignores the invalid hash but does not rewrite the URL until the next page turn. This does not affect reading.
4. **Nonblocking: one quiz feedback line goes slightly beyond the pages.** The correct-answer text for question 2 says Unferth lent "his own best sword" and that "the two rivals become friends". The pages show the loan, the public thanks and Unferth left speechless, but no friendship scene. This is a fair reading of the story, not an error. Softening it to "and Unferth has nothing left to say" would match the page exactly.

REVISE

---

## Advisor disposition (managing session, 2026-10-14)

1. **Not taken — contradicts the packet.** `BUILDER.md` and `verify-reader.py` require the boundary aliases `#page-58` → End and `#page-59` → Quiz, the same convention as King Arthur's shipped reader (`#page-60`/`#page-61`). The aliases are the specified boundary states, not counted story pages; story routing stops at 57.
2. **Fixed:** progress-bar CSS default now `calc(100% / 59)`.
3. **Not taken:** cosmetic; matches the proven template.
4. **Fixed:** quiz 2 feedback now ends "and Unferth has nothing left to say."

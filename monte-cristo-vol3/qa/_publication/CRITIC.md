# The Count of Monte Cristo, Volume III: The King's Attorney — reader critic

You are one fresh, zero-history reader critic. Review the finished local
implementation independently. Do not edit files.

## Inspect

- `books/monte-cristo-vol3/index.html`
- canonical `books/monte-cristo-vol3/pages/page-01.png` through `page-56.png`
  only as the reader references them
- the output of `python3 books/monte-cristo-vol3/qa/_publication/verify-reader.py`

Do not open production prompts, audits, candidates, QA reports, or the builder
receipt before judging.

Read the HTML and script closely (you have no browser): trace the routing for
`#page-1`, `#page-56`, `#end`, `#quiz`, and an out-of-range hash; the contents
list generation; bookmark persistence; zoom-view behavior; the quiz check
logic. Judge:

1. Page 1 loads with the correct title, counter, and movement; every page
   index maps to `pages/page-NN.png` for 1–56 and nothing beyond.
2. Previous/next, page-edge, keyboard, touch, `#page-N` reload, and saved
   position behave coherently at both ends of the book.
3. Contents covers all six movements and 56 pages exactly once; bookmarks
   persist under the book's own storage keys.
4. Zoom opens centered, supports the required levels, pan/scroll, page
   navigation, and clean close/return.
5. Page 56 leads to a non-page ending state ("End of Volume III") and then a
   five-question quiz; neither is counted as Page 57; the ending links to
   nothing unpublished (a plain-text mention that the story continues in
   Volume IV is expected and correct). The `#page-57`/`#page-58` aliases in
   the routing are the packet's own specification, inherited from the
   previous shipped readers; they are not defects.
6. Every quiz question has one correct answer, correct feedback, and tests the
   story's causes or choices rather than trivia, in plain language.
7. No stale Beowulf, King Arthur, Three Kingdoms, Three Musketeers, or Monte
   Cristo Volume II terms, keys, links, or 57-page labels remain; no duplicate
   element IDs; no script references to missing IDs.

Cosmetic preference and redesign suggestions are nonblocking. A `REVISE`
finding must name reproducible reader harm or broken behavior and a concrete
correction.

Write `books/monte-cristo-vol3/qa/_publication/reader-critic.md` with a
concise report ending in exactly `APPROVED` or `REVISE`, and return only that
word.

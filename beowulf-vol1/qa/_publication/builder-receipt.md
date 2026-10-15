# Builder receipt — Beowulf reader

**Built:** `books/beowulf-vol1/index.html`, a 57-page reader for
*Beowulf: The Hall, the Mere, and the Dragon* (2026-10-14).

## What was built

- The template is `books/king-arthur-vol1/index.html`. I copied all of it and changed only its identity text. The CSS, layout, and JavaScript behavior are unchanged.
- The `<title>`, the hidden heading, the meta description, the page alt text and the top-bar label all use the standalone title. The word "volume" appears nowhere.
- The 57 titles are a `const titles = [` array of JSON strings, exactly as the packet gives them, with straight apostrophes.
- The seven movements are a `const movements = [` array with the approved ranges 1–7, 8–14, 15–23, 24–32, 33–36, 37–42 and 43–57.
- Storage keys are `monte_inspired:beowulf-vol1:page` and `monte_inspired:beowulf-vol1:bookmarks`.
- Routing boundaries now stop at 57 pages: `#page-58` maps to `#end` and `#page-59` maps to `#quiz`. The end state and the quiz are not counted as story pages and do not map to image files.
- The six Chronicle pages (7, 14, 23, 36, 42, 57) are ordinary routed pages.
- **End state:** the eyebrow and the folio page-title both read `The End`. The heading is "There is Beowulf's Barrow". It closes the whole story in plain sentences:
  - the boy everyone laughed at
  - Grendel
  - the mother in the mere
  - Hrunting and Unferth
  - Hrothgar's warning
  - the dragon
  - Wiglaf
  - Beowulf's Barrow

  It then links to the quiz. It promises no sequel and names no other volume.
- **Quiz:** the heading is `Test your understanding`. There are five `class="question"` items, each with three options, one `data-answer`, and plain correct and incorrect feedback. The questions are:
  1. Hrothgar's old debt to Beowulf's father.
  2. Hrunting given back with thanks, and the rivals becoming friends.
  3. The pride that sends old Beowulf down alone.
  4. Wiglaf's promise, his family's loyalty, and "afraid every time … I came anyway."
  5. Chronicle: the single manuscript, two scribes, the 1731 fire, the British Library.

  All facts come from `08-FULL-SCRIPT.md` (pp. 6, 27, 33–34, 41, 44, 47–48, 57).

## Preserved from the template

All of these features are unchanged:

- responsive 2:3 page presentation
- previous/next buttons, page-edge tap zones, keyboard navigation and touch swipes
- exact `#page-N` links and the saved reading position
- contents grouped by movement
- device-local bookmarks and quick return from Contents
- preloading of adjacent pages
- fullscreen
- the centered zoom view: Fit, 125%, 150%, 200%, 250% and 300%; pan and scroll; double-click zoom; page navigation while zoomed
- race-safe image loading (`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`)

## Removed or adapted

- Every King Arthur name, key, title, quiz item and "Volume I" label is gone.
- The "story continues in Volume II" line is gone.
- The template had no library or other-volume anchor, so there was none to remove.
- The template printed the Contents eyebrow (`Volume I · 59 pages`) twice. The new reader prints it once, as `57 pages`.

## Could not preserve

Nothing.

## Verification

`python3 books/beowulf-vol1/qa/_publication/verify-reader.py` reports `CLEAN`. The inline script also parses without errors.

No page image, reference image, other packet or other book was modified.

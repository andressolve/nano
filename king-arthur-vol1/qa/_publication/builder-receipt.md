# Builder receipt — King Arthur, Volume I reader

**Built:** `books/king-arthur-vol1/index.html`. It is a single-file reader for the 59 canonical pages `pages/page-01.png` … `pages/page-59.png`. The six Chronicle pages are routed like every other page. After page 59 come an end state (`#end` / `#page-60`) and a five-question quiz (`#quiz` / `#page-61`). Neither is counted as a story page or mapped to an image.

**Adapted from** `books/three-kingdoms-vol1/index.html`. I copied its behaviour, structure, CSS and visual template wholesale and kept these features: 2:3 stage; prev/next buttons; page-edge tap zones; keyboard; touch swipe; exact `#page-N` links; saved position; movement contents covering every page once; device-local bookmarks with quick return; adjacent preloading; fullscreen; the zoom view (Fit/125/150/200/250/300%, pan/drag, double-click, zoom-view page nav); race-safe loading (`renderRequest`, `displayedPage`, `pendingPageLoads`, `image.decode()`, `aria-busy`).

**Changed for this book:**
- **Identity:** title, heading and alt text now read `King Arthur, Volume I: The Sword and the Table`, and the meta description is new.
- **Pages and contents:** the 59-title array, the seven movements, and the counts (progress width is now 1/61, the page counters read 59).
- **Storage and routing:** storage keys are `monte_inspired:king-arthur-vol1:{page,bookmarks}`, and the boundary hashes are `#page-60`/`#page-61`.
- **End and quiz:** the end state is `End of Volume I`, and it promises Volume II as text only (the Lady's gift, the empty seat). The quiz is `Test your understanding` with five new questions: the locked inn, Bedegraine's spear line, the scabbard and Pellinore, the round table, and the Chronicle question on the stone c. 1200. Their facts come from `08-FULL-SCRIPT.md`.
- **Removed:** every Three Kingdoms name, key, title and quiz item. The template had no library or other-volume anchor, so there was nothing to remove there.

**Not preserved:** nothing.

**Checks:** `verify-reader.py` prints CLEAN, and `node --check` passes on the inline script. No page or reference image was opened, edited or regenerated.

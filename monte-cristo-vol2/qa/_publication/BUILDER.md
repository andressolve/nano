# Volume II reader/publication builder

You are the implementation builder for one bounded reader task. Work only on
the finished 49-page Volume II reader and its library integration. Do not edit,
replace, optimize, recompress, or regenerate any story page or approved
reference image.

## Read only what is needed

1. `HANDOFF.md`
2. `../monte-cristo-expanded/index.html` — primary reader behavior and visual
   template
3. `../treasure-island/volume-2/index.html` — end-state and quiz interaction
   pattern only
4. `../stories.js` — catalog schema

Do not open production prompts, rejected candidates, the large production plan,
or old production sessions.

## Build

Create `index.html` in this directory's project root.

Preserve the proven Volume I reader features:

- responsive 2:3 page presentation;
- previous/next buttons, page-edge controls, keyboard navigation, and touch
  swipes;
- exact `#page-N` links and saved reading position;
- movement-based contents covering every page exactly once;
- device-local bookmarks and quick return from Contents;
- adjacent-page preloading;
- fullscreen;
- the dedicated centered zoom view with fit, 125%, 150%, 200%, 250%, and 300%
  levels, pan/scroll, double-click zoom, and zoom-view page navigation.

Adapt the reader identity to:

- title: `The Count of Monte Cristo — Volume II: The House of Morcerf`;
- 49 canonical story pages at `pages/page-01.png` through
  `pages/page-49.png`;
- storage keys beginning `nano:monte-cristo-vol2:`;
- a visible link to `../monte-cristo-expanded/index.html` as Volume I;
- a home link to `../index.html`.

Do not invent or generate a cover. The reader begins on canonical Page 1. Add
two non-story states after Page 49: an `End of Volume II` state and a five-
question `Test your understanding` quiz. These states must never be counted as
story pages or mapped to image files. The ending state must not link to an
unpublished Volume III; it may name the lit Villefort window as the continuation
promise and link to Volume I and the library.

The quiz tests causal and moral comprehension, not decorative trivia. It must
cover these five ideas with one unambiguously correct answer and useful feedback
for each:

1. why Haydée insists that Fernand come first;
2. how the Count uses Danglars and the newspaper to make Fernand demand a public
   hearing;
3. why Mercédès asks Edmond not to fight Albert;
4. why Albert withdraws and rejects the Morcerf name and fortune;
5. what the Count's final `One` and Villefort's lit window mean.

Use exactly these reader titles and expose them as a simple `const titles = [`
array so the deterministic verifier can inspect them:

1. Three Roofs
2. The Banker First
3. Janina
4. The Real Reason
5. I Shall Enjoy It
6. The Invitation
7. Albert de Morcerf
8. Greece
9. Two Handshakes
10. My Father
11. Fruit from Her Garden
12. She Knows
13. Since 1815
14. The First Lie
15. Appetite Intact
16. Warn Nobody
17. The Pleasure
18. The Receipt
19. Janina, 1822
20. The Price
21. The Market
22. Her Right to Speak
23. The Room
24. Danglars Decides
25. The Reply from Janina
26. In Print
27. The Truth, Not a Retraction
28. She Has Known
29. Beauchamp Returns
30. The Public Stair
31. The Chamber of Peers
32. The Door Opens
33. Haydée Testifies
34. Still Wearing the Decorations
35. At the End of It
36. The Challenge
37. After Victory
38. Edmond
39. Stand Still
40. The Night Before
41. Four Hours Before Dawn
42. Albert Withdraws
43. His Mother's Name
44. It Changes Nothing
45. The Empty Glass
46. I Am Edmond Dantès
47. The Shot
48. They Take Nothing
49. One

Use exactly these six movement ranges in a simple `const movements = [` array:

- `I · The Invitation`, Pages 1–7
- `II · The House of Morcerf`, Pages 8–17
- `III · What Happened at Janina`, Pages 18–25
- `IV · The Fall`, Pages 26–34
- `V · The Son`, Pages 35–44
- `VI · The Cost`, Pages 45–49

Add a visible catalog entry near the top of `../stories.js`:

- slug: `monte-cristo-vol2`
- title: `The Count of Monte Cristo — Volume II: The House of Morcerf`
- cover: `monte-cristo-vol2/pages/page-01.png`
- published: `2026-08-21`
- category: `Myth & Literature`
- series: `The Count of Monte Cristo · Volume II`
- summary: accurately describe Haydée's evidence, Fernand's fall, Albert's
  challenge, Mercédès' intervention, and the contaminated cost of the Count's
  first completed revenge without spoiling the final method in excessive
  detail.

Do not edit the root homepage markup; `stories.js` is its catalog authority.

## Builder checks

Run `python3 qa/_publication/verify-reader.py`. Fix every mechanical problem
until it prints `CLEAN`. Test the reader locally in a browser at desktop and
tablet sizes, including first/middle/final pages, Contents, bookmarks, zoom,
hash reload, end state, all quiz answers, Volume I link, and root catalog card.

Write a concise implementation receipt to
`qa/_publication/builder-receipt.md`. Do not approve your own work.

# Three Kingdoms, Volume I — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 50-page reader for `books/three-kingdoms-vol1/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/three-kingdoms-vol1/HANDOFF.md` (the Phase line and the last few rows).
2. `books/three-musketeers-vol1/index.html` — the proven reader from the last
   volume (itself built from Monte Cristo Vol II's): copy its behavior,
   structure, and visual template wholesale and adapt the identity below. Its
   routing, contents, bookmarks, zoom view, end state, and quiz are the model.
   Remove every Musketeers name, key, title, and quiz item.
3. `books/three-kingdoms-vol1/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/three-kingdoms-vol1/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/three-kingdoms-vol1/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `Three Kingdoms, Volume I: The Peach Garden Oath`;
- 50 canonical story pages at `pages/page-01.png` … `pages/page-50.png`
  (relative to the book directory);
- storage keys `monte_inspired:three-kingdoms-vol1:page` and
  `monte_inspired:three-kingdoms-vol1:bookmarks`;
- no library link and no other-volume link: remove those anchors (the end
  state may promise that the story continues in a Volume II, as text
  only, no link);
- the end state heading: `End of Volume I`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 50
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-51") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-52") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 50 titles as a simple `const titles = [` array of JSON
strings, in order:

1. The Yellow Sky
2. The Notice on the Wall
3. Why Not Do Something?
4. Wine, and Quickly
5. Real Brothers
6. The Oath
7. Third Brother
8. A Weapon for Each Brother
9. A Hundred Each
10. The Ambush
11. The Grass Begins to Glow
12. Somebody Stole Our Battle
13. You're Late
14. The Emperor's Banner
15. A Bag of Rice
16. The Fat General
17. Up the Palace Stairs
18. Do You Think Mine Isn't?
19. The Giant Behind the Old Man
20. Red Hare
21. Father
22. A Dagger in His Sleeve
23. Wake Me When the Horse Comes
24. A Gift
25. Out of the Gate
26. Your Father's Son
27. Tie the Legs Tight
28. The Old Man Never Came Home
29. A Letter to Every Lord
30. We Go
31. Hulao Gate
32. The End of the Bench
33. I Will Bring His Helmet
34. Before It Is Cold
35. The Drums
36. Still Warm
37. With Me, Not with Yuan Shao
38. Give Me the Gate
39. Among Men, Lü Bu
40. Is There No One?
41. Slave of Three Fathers
42. Fifty Times
43. Third Brother, I Am Here
44. Not on a Hill
45. Three Against One
46. The Gate Slams
47. We Are Brothers
48. Two Heroes
49. What He Wanted
50. He Did Not Turn Around

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Peach Garden`, 1–9
- `II · Five Hundred`, 10–16
- `III · The Red Horse`, 17–22
- `IV · The Dagger`, 23–30
- `V · Eighteen Lords`, 31–38
- `VI · Lü Bu`, 39–46
- `VII · The Gate`, 47–50

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences a ten-year-old and a seven-year-old can follow. Test the
story's causes and choices, never trivia, on these five ideas:

1. Why Liu Bei, the worst fighter of the three, rides out as the bait (the
   rebels chase him into the valley between the two hills, where his brothers
   are waiting to come down on them).
2. Why Liu Bei stops Zhang Fei from going after Dong Zhuo, even though the snub
   hurt him too (Dong Zhuo wears the emperor's armor; killing him would make
   the brothers the rebels; his own hands were shaking).
3. Why Cao Cao kills the old man on the road, after killing his family by
   mistake (he is afraid the old man will tell the world what he did; he says
   he would rather betray the whole world than let the world betray him).
4. Why Guan Yu tells Cao Cao to pour the wine and leave it (he is promising to
   come back before it is cold; the warm cup proves he won, when the lords said
   a man with no rank could not).
5. How three brothers make Lü Bu run when no single fighter could stop him
   (they ride in together, as they swore in the peach garden, and he cannot
   watch all three at once).

The end state may say, as text only, that the story continues in Volume II.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.

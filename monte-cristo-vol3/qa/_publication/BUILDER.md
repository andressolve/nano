# The Count of Monte Cristo, Volume III: The King's Attorney — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 56-page reader for `books/monte-cristo-vol3/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/monte-cristo-vol3/HANDOFF.md` (the Phase line and the last few rows).
2. `books/beowulf-vol1/index.html` — the proven reader from the last book:
   copy its behavior, structure, and visual template wholesale and adapt the
   identity below. Its routing, contents, bookmarks, zoom view, end state, and
   quiz are the model. Remove every Beowulf name, key, title, quiz item, and
   Chronicle reference (this book has no Chronicle pages).
3. `books/monte-cristo-vol3/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/monte-cristo-vol3/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/monte-cristo-vol3/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `The Count of Monte Cristo, Volume III: The King's Attorney` (the third volume of a series);
- 56 canonical pages at `pages/page-01.png` … `pages/page-56.png` (relative to
  the book directory);
- storage keys `monte_inspired:monte-cristo-vol3:page` and
  `monte_inspired:monte-cristo-vol3:bookmarks`;
- no library link and no other-volume link: remove those anchors (the Nano
  publication copy adds its own library links later);
- the end state heading (the eyebrow, and the page-title text shown while the
  end state is displayed): `End of Volume III`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 56
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-57") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-58") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 56 titles as a simple `const titles = [` array of JSON
strings, in order (keep the accented letters é and è exactly):

1. The Second Man
2. What Was in the Box
3. I Was the Priest
4. That Chair's Taken
5. Prince Andrea Cavalcanti
6. The King's Attorney
7. Down the Hill
8. One Drop
9. Villefort's Problem
10. The House in the Faubourg
11. Grandfather's Eyes
12. I Was the Sailor
13. Do You Want Me to Stop?
14. The Red Purse
15. If I Ever Find Him
16. Valentine de Villefort
17. Every Floor of It
18. Three Invitations
19. The Iron Gate
20. To Fathers
21. A Story about This House
22. Two in the Morning
23. A Cup of Warm Milk
24. Don't Tell Me
25. Such a Comfort
26. Did You See the Milk?
27. The Steps of the Opéra
28. Bitter, Like Your Medicine
29. Help Her
30. It Was My Bottle
31. Inside the Wall
32. Red Drops
33. Every Night Until You Are Dead
34. So You Will Die
35. The House Believed It
36. One Name, Letter by Letter
37. You Promised Me
38. The Tomb at Night
39. She Did Not Wake
40. A Good Story Needs a Date
41. Use It
42. All Paris Came
43. A Very Big Tree
44. My Father Is You
45. You Didn't Look
46. It Is True
47. Faster
48. I Did What You Told Me
49. The Closed Door
50. I Am Edmond Dantès
51. Nothing Left in It
52. Every Garden in Paris
53. He Could Not Say It
54. Keep This One Too
55. One Month
56. She's Holding On

Use exactly these six movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · What Was Buried`, 1–8
- `II · The King's Attorney's House`, 9–18
- `III · Dinner at Auteuil`, 19–27
- `IV · Valentine`, 28–39
- `V · The Trial`, 40–47
- `VI · The Bill`, 48–56

Use straight apostrophes (`'`) in titles and movements exactly as written
above.

The quiz: five questions, each `class="question"` with three options and one
`data-answer="a|b|c"`, with feedback that explains the right answer in one or
two plain sentences anyone can follow. All five test the story's causes and
choices, never trivia. On these five ideas:

1. Why the Count gives Madame de Villefort the little red bottle (he saw at
   once she was a woman who would use it for her son, and he wanted a
   poisoner loose in the King's Attorney's house to hurt Villefort — whatever
   she did with it, he said, was "Villefort's problem").
2. Why Villefort tells his father "Don't tell me" when Noirtier knows who the
   poisoner is (if he knew, he would have to prosecute, and the name of
   Villefort would be in every newspaper in France; he buries whatever
   threatens his name).
3. Why the Count makes Valentine seem to die instead of carrying her away
   through the wardrobe (if she vanished, her father would search Paris and
   bring her home to the poisoner; nobody hunts for a girl who is dead).
4. How Villefort's own trial destroys him (he asks the prisoner for his
   father's name, and Benedetto — the baby Villefort buried at Auteuil, who
   was dug up alive — says the King's Attorney is his father; Villefort
   admits it is true).
5. Why the Count cannot say "Two" at the end (he won, but the poison he put
   in Madame de Villefort's hand killed her little son, who had done
   nothing; for the first time he does not know whether God is on his side).

The end state should close the volume in a few plain sentences (the house at
Auteuil, the red bottle, Valentine's false death, the trial, the bill, the
word he could not say, and Valentine's hand closing) and then link to the
quiz. It may say the story continues in Volume IV, as plain text with no link.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.

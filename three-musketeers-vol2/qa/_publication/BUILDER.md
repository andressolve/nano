# The Three Musketeers, Volume II: Milady — reader builder

You are the implementation builder for one bounded reader task. Work only on
the finished 58-page reader for `books/three-musketeers-vol2/`. Do not edit,
replace, optimize, recompress, or regenerate any story page or reference image.
No image generation. Do not reopen story-page production.

## Read only what is needed

1. `books/three-musketeers-vol2/HANDOFF.md` (the Phase line and the last few rows).
2. `books/three-musketeers-vol1/index.html` — the proven reader of the previous
   volume of this series: copy its behavior, structure, and visual template
   wholesale and adapt the identity below. Its routing, contents, bookmarks,
   zoom view, end state, and quiz are the model. Replace every Volume I title,
   key, quiz item and reference. This book has no Chronicle pages.
3. `books/three-musketeers-vol2/07-PAGE-CONTRACT.md` — movement names and page
   turns, for orientation only.
4. `books/three-musketeers-vol2/08-FULL-SCRIPT.md` — only to write accurate quiz
   questions and feedback in the story's own facts.

Do not open production prompts, candidates, audits, or QA reports.

## Build

Create `books/three-musketeers-vol2/index.html`. Preserve every proven feature:

- responsive 2:3 page presentation; previous/next buttons, page-edge controls,
  keyboard navigation, touch swipes; exact `#page-N` links and saved reading
  position; movement-based contents covering every page exactly once;
  device-local bookmarks and quick return from Contents; adjacent-page
  preloading; fullscreen; the centered zoom view with fit, 125%, 150%, 200%,
  250%, 300%, pan/scroll, double-click zoom, and zoom-view page navigation;
  the race-safe image loading (`renderRequest`, `displayedPage`,
  `pendingPageLoads`, `image.decode()`, `aria-busy`).

Adapt the identity:

- `<title>` and heading: `The Three Musketeers, Volume II: Milady` (the second
  volume of a series; Volume I was *The Queen's Diamonds*);
- 58 canonical pages at `pages/page-01.png` … `pages/page-58.png` (relative to
  the book directory);
- storage keys `monte_inspired:three-musketeers-vol2:page` and
  `monte_inspired:three-musketeers-vol2:bookmarks`;
- no library link and no other-volume link: remove those anchors (the Nano
  publication copy adds its own library links later);
- the end state heading (the eyebrow, and the page-title text shown while the
  end state is displayed): `End of Volume II`; the quiz heading:
  `Test your understanding`.

Keep the template's routing logic and update its literal boundaries for 58
pages. The verifier looks for these exact lines:

```
const END_HASH = "#end";
const QUIZ_HASH = "#quiz";
if (hash === END_HASH || hash === "#page-59") return titles.length;
if (hash === QUIZ_HASH || hash === "#page-60") return titles.length + 1;
return pageNumber >= 1 && pageNumber <= titles.length ? pageNumber - 1 : null;
const hash = current < titles.length ? `#page-${current + 1}` : current === titles.length ? END_HASH : QUIZ_HASH;
localStorage.setItem(STORAGE_KEY, String(Math.min(current, titles.length - 1)));
```

The end state and quiz are never counted as story pages and never mapped to
image files.

Use exactly these 58 titles as a simple `const titles = [` array of JSON
strings, in order:

1. Only Three Blue Cloaks
2. The Boy from Gascony
3. Something Nobody Can Forget
4. Boys Tell Me Everything
5. Noon on the River Road
6. By the Front Door
7. Ladies Who Are Kind
8. Two of Those
9. How Very Clever of Her
10. The Empty Chair
11. I Don't Know That Name
12. She Was Not Alone
13. The Lily
14. Nobody Said Anything About Windows
15. Which Shoulder?
16. A Friend of Mine
17. It Was You
18. The March to La Rochelle
19. A Bottle from Your Friends
20. That Was Good Grass
21. The Red Dovecote
22. The Broken Stovepipe
23. Then I Shall Do a Great Deal
24. Do You Know Me?
25. On the Road to the Sea
26. Hate Me on the Road
27. Are You Hungry?
28. Who'll Bet Against Us?
29. Breakfast Under the Guns
30. The Cardinal's Paper
31. I Haven't Finished My Chicken
32. All for One, and Push!
33. Everybody Was Running
34. One Minute More
35. In My Red or in the Ground
36. Half a Day
37. The Kind Widow
38. You Were Right to Warn Him
39. One Way or Another
40. Nobody Else Would Ride That Colour
41. To d'Artagnan
42. The Back Gate
43. You Promised, and You Came
44. The Roses
45. You Didn't Pour the Wine Either
46. The Storm
47. Not Like This
48. Judge Me from the Bank
49. Nobody Let Go
50. Never
51. The Lantern Goes Out
52. Good
53. The Sixth Time
54. I Did Not Pour the Wine
55. Men Who Can't Be Bought
56. There. D'Artagnan.
57. The Lamp at the Door
58. Four Blue Cloaks

Use exactly these seven movements as a simple `const movements = [` array of
`{ title: "...", start: N, end: N }` objects:

- `I · The Lady in the Carriage`, 1–9
- `II · The Lily`, 10–18
- `III · The Red Dovecote`, 19–25
- `IV · The Bastion`, 26–36
- `V · Béthune`, 37–45
- `VI · The River`, 46–52
- `VII · The Paper`, 53–58

Use straight apostrophes (`'`) in titles and movements exactly as written.

## The quiz

Five questions, each `<li class="question" data-answer="a|b|c">` with three
options (`<label><input type="radio" name="qN" value="a"> text</label>`) and
feedback that explains the right answer in one or two plain sentences anyone
can follow. All five test the story's causes and choices, never trivia.

**Answer balance (owner's rule, 2026-10-17 — the verifier checks it):** the
three options of a question are written to about the same length and detail;
the wrong options are plausible, specific, and drawn from the story; the
correct answer is the longest option in **at most two** of the five
questions; the correct letters vary — a, b and c each used at least once,
never the same letter three times in a row. A reader must not be able to pass
by picking the longest option.

On these five ideas:

1. How Milady found out where Constance was hidden (on his very first visit,
   dazzled by her front door, the boy told her "a convent in the north"; the
   Cardinal, who knew the Queen's secrets, named Béthune).
2. Why Athos went still when the boy described the lily on her shoulder (he
   had married her when he was a young count, found the thief's brand, and
   hanged her himself without asking one question; the rope was cut and she
   lived).
3. Why the four ate breakfast in the bastion (to talk where no ear in the camp
   could hear them, and to win the King's leave to ride north by doing
   something the whole army saw; leaving without leave meant being shot).
4. Why Athos stopped the boy from killing Milady at the ferry (he had judged
   her once, alone, in the dark, in a rage, and it made everything worse; he
   offered her a trial in daylight, and she chose the river instead).
5. Why the Cardinal gave the boy a Musketeer's commission (the boy gave back,
   unasked, the paper that could have protected him from anything; the
   Cardinal would rather have a man who can't be bought in France than under
   it — and Athos wrote the boy's name in it).

The end state closes the volume in a few plain sentences (a lady nobody
suspected, a lily on her shoulder, a breakfast under the guns, a girl who knew
his horse, four men holding on to each other in a flood, and a blue cloak at
last) and then links to the quiz. It may say the story continues in a later
volume, as plain text with no link.

Write a short receipt at `qa/_publication/builder-receipt.md` (what was built,
what was adapted from the template, anything you could not preserve). Do not
commit. Reply with the two file paths and nothing else.

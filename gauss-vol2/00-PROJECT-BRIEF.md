# 00 — PROJECT BRIEF

## Title
**The Man Who Measured the World**
Subtitle: *Carl Friedrich Gauss, Book Two*

(Counterpart to Book One, *The Boy Who Chose Numbers*. Book One was inward — numbers for their own sake. Book Two turns the same numbers outward, onto the real world.)

## One-sentence window
This bio covers Carl Friedrich Gauss from the height of his early fame (1801, age 24) through the great middle of his life — love and devastating loss, the death of his patron, and the years he aimed his mathematics at the real world: the heavens (lost planets found by calculation), the Earth (measuring a whole kingdom with triangles), and the invisible (magnetism and the first electric telegraph) — closing in the 1830s.

## Spine (decided with user)
**The man who turned numbers outward — and measured the world.** Book One's boy chose numbers over words. Book Two's man aims those numbers at everything he can reach: he finds a lost planet with pure calculation, he measures the curve of the Earth with a mesh of triangles and a mirror that flashes sunlight across mountains, and he sends the first message down an electric wire. The human spine running underneath is **grief**: he loses his patron, then his beloved wife Johanna and their infant son, and he keeps measuring — because measuring the world is how this man holds on. The title nods to Daniel Kehlmann's novel *Measuring the World* (2005), used as inspiration, not as a source of facts.

## Re-enactable hook (the Book One discipline: give the kid something to DO on paper)
**Triangulation** — how to measure a distance you cannot walk (across a river, the height of a tower): pace out one baseline you *can* measure, sight the two angles to the far point, draw it to scale, and read off the distance. This is *exactly* what Gauss did to the entire Kingdom of Hanover. The annotated triangulation page (P9) is the heart-hook, the way the 17-gon was Book One's. Secondary tactile beat: the heliotrope (a mirror flashing sunlight to mark a far station — a signal mirror any kid can try).

## Curricular hook (Lyceum, Collection II → III)
Book One landed the kids' compass-and-straightedge constructions. Book Two extends geometry into **measurement and trigonometry**: triangles with known angles and one known side give you every distance — the bridge from pure Euclidean construction to *applied* geometry (surveying, navigation, coordinates). It also seeds **curvature** (a triangle on a curved Earth does not add up to 180°) and a first, careful glimpse of **non-Euclidean geometry**.

## Audience
Francisco (10) and Sebastian (8). Per the standing framing rule: NOT pitched down by age. Write so any first-time reader who has never heard of Gauss can follow on first read — no withheld facts, period/technical terms glossed on first use (observatory, geodesy, triangulation, baseline, heliotrope, magnetism, telegraph, non-Euclidean), names grounded with a one-line role. "Clear, not dumbed down." Book One ended on Ceres; P1 recaps enough that Book Two stands alone.

## Format
Biographical mode. 3:2 landscape (1536×1024). Oil-painting realism, identical register to Book One / Newton / Honda / da Vinci. Narration baked into the image as off-white serif caption boxes (the Honda formula). Dark-theme page-flipping reader (mirror Book One's `gauss/index.html`), 5-question WHY-quiz.

## Image model
gpt-image-2 standard (`mcp__openai-image-2__{generate_image,edit_image}`), quality high, size 1536×1024. `edit_image` takes ONE imagePath. Book Two has NO 3+ named-character pages (max two named characters share a page: Gauss+Johanna, Gauss+Minna, Gauss+Weber, Gauss+Duke) → use the lock-the-harder-face strategy throughout; no composite plate required. Flag immediately if a script revision introduces a 3-named-character page.

## Page count
Cover + 18 pages (target). Expand or stop as the arc lands. Book Three (the elder statesman of science, his last years, death 1855 with Voltaire-style closing) is plantable, NOT promised here.

## Deliberate editorial choices (traceable — built from RESEARCH.md confidence flags)
- **Disputed values are NOT stated as single hard facts in-image.** Per RESEARCH.md:
  - Hanover survey → "Through the 1820s" (not a single span; tasked 1818 / project 1820–1844 / fieldwork 1821–25 all true).
  - Telegraph wire → "about a kilometre, across the rooftops of Göttingen" (sources give 1.2 km / 3 km / 5000 ft).
  - Theorema Egregium → "1827" (printed edition sometimes dated 1828).
  - Johanna's death → "11 October 1809" used; the day is lightly disputed (~23 Oct in one archive) — month/year are solid. We render the date but keep weight on the event, not the day.
- **Least-squares priority told honestly:** "Legendre published it first in 1805; Gauss said he had used it since 1795 — and they argued over it for years." We do NOT claim Gauss invented it first.
- **Grief framed as biographers' characterization, not clinical fact:** "a sorrow some say he never fully escaped."
- **TRAD details used as texture, flagged not asserted:** Joseph named after Piazzi ("they say"), Minna as Johanna's "dearest friend," "seven ripe fruits" on the seal.
- **Bolyai quote = the 6 March 1832 letter, one chosen English translation, held verbatim.** The act-of-learning line = the 1808 Bolyai-letter wording (verbatim), used as the closing epigraph.
- **Magnetic Union founding year (1836) NOT put in a caption** — purpose stated, year left out (RESEARCH flagged it not double-locked).
- **Velvet cap is a late-life attribute** — appears only on the ~1830s older-Gauss ref/pages, not the 1820s survey pages.
- **Emotional ordering:** strict life-event chronology preserved. Grief (P7) lands at the book's middle as the pivot; the outward-science build (P9–P14) rises out of it so the measuring reads as how he endures, not as detached achievement.

## Production notes
- Refs first, validate the gate, THREE prototypes spanning density AND format (a grief cinematic page / the triangulation annotated-breakthrough page / the closing montage finale), then bulk-batch in parallel.
- Re-Read every ref PNG before writing a page prompt. Describe from the pixels, not from memory.
- Three Gauss age phases (≈28 / ≈45 / ≈55) — never feed the wrong-age ref into edit_image.
- No composite plate needed (no 3-named-character page). Two-named-character pages = lock the harder/more-distinctive face, describe Gauss in prose.
- Cost envelope ~$7–8.

# Relativity: The Life of Albert Einstein

## Project Overview

| Field | Value |
|-------|-------|
| **Title** | Relativity |
| **Subtitle** | The Life of Albert Einstein |
| **Format** | Biographical graphic novel |
| **Target audience** | Francisco (9) and Sebastian (7) |
| **Image model** | Gemini via Nano Banana MCP |
| **Page count** | 20 (cover + 19 story/legacy pages) |

## Concept

A portrait of Albert Einstein — not as the wild-haired icon on posters, but as a living person. A dreamy child who was entranced by a compass needle. A teenager who hated his school so much he dropped out. A young man who couldn't get an academic job and took a "cobbler's" clerk position at the patent office — and used those quiet hours to rewrite physics. A father whose son disappeared into mental illness. A pacifist who signed the letter that led to the atomic bomb. A celebrity who turned down a country.

This is the second biographical graphic novel in the collection, following *Cogito* (Descartes). Like Descartes, Einstein is the protagonist — no fictional POV. The story spans his life from age 5 (the compass) to death at 76, structured around the moments that shaped him and the ideas that shook the world.

## What the Kids Will Take Away

- The most important questions come from curiosity, not from authority
- You can change physics while reviewing patents at a desk job
- A single year (1905) can contain four revolutions
- "Time" is not the same for everyone — it depends on how fast you move
- E = mc²: a tiny amount of matter contains an enormous amount of energy
- Gravity is not a force — it is the shape of space and time
- Even the most famous person in the world can stay humble, play the violin, and refuse a country

## Why This Format Works for Einstein

- **Rich personal archive.** Letters, diaries, recollections of friends (Solovine, Besso), the Olympia Academy reading nights, the violin, the hair, the quips. Gives the character a living dimension — the same thing that worked for Descartes.
- **Concepts the kids already know.** E = mc², "time is relative," light bending around the sun. Kids have heard these phrases. Seeing where they came from mirrors the Cartesian-plane moment in *Cogito*.
- **Built-in narrative spine.** The 1905 "miracle year" is a ready-made story beat — a 26-year-old patent clerk publishing four world-changing papers in a single year.
- **Emotional shading.** His first marriage falling apart, his son Eduard's illness, regret over the atomic bomb letter, refusing Israel's presidency. Not a hagiography.

## Project Structure

| Document | Purpose |
|----------|---------|
| `00-PROJECT-BRIEF.md` | This file — overview and workflow |
| `01-STYLE-GUIDE.md` | Visual direction, palette, panel conventions |
| `02-CHARACTERS.md` | Character lock blocks and reference sheet prompts |
| `03-SETTINGS.md` | Location descriptions and visual references |
| `04-SCRIPT.md` | Full page-by-page script with generation prompts |

## Page Spine (20 pages)

| # | Title | Era | Age | Beat |
|---|-------|-----|-----|------|
| 1 | Cover | — | — | Title page |
| 2 | The Compass | Munich, 1884 | 5 | Father shows Albert a compass; the invisible force thrills him |
| 3 | Uncle Jakob and the Thursday Books | Munich, 1889-93 | 10-14 | Uncle Jakob teaches algebra; Max Talmud brings science books on Thursday nights |
| 4 | The School He Hated | Munich, 1894 | 15 | Luitpold Gymnasium — rote learning, militarism. Albert drops out, follows family to Italy |
| 5 | Aarau and the Beam of Light | Switzerland, 1895-96 | 16 | Cantonal school in Aarau. Rides a bike. First thought experiment: what if I rode a beam of light? |
| 6 | Mileva | ETH Zurich, 1898-1900 | 19-21 | Meets Mileva Marić, the only woman in the physics class. They study together, fall in love |
| 7 | The Patent Office | Bern, 1902 | 23 | Can't get an academic job. Takes a clerk's position reviewing patents. Quiet hours to think |
| 8 | The Olympia Academy | Bern, 1903 | 24 | Three friends reading Hume, Spinoza, Poincaré by candlelight. Named as a joke — "the Academy" |
| 9 | 1905: The Miracle Year Begins | Bern | 26 | Opens the year — the patent clerk about to change physics |
| 10 | Light Is Made of Grains | March 1905 | 26 | Photoelectric effect — light comes in packets (quanta). Nobel-winning paper |
| 11 | Atoms Are Real | May 1905 | 26 | Brownian motion — dust specks in water jiggle because atoms are hitting them |
| 12 | Time Is Not the Same | June 1905 | 26 | Special relativity — the train and the platform, moving clocks tick slower |
| 13 | E = mc² | September 1905 | 26 | A tiny amount of matter contains enormous energy. The world's most famous equation |
| 14 | The Happiest Thought | Bern, 1907 | 28 | A falling person feels no gravity. Seed of general relativity |
| 15 | The Long Climb | Berlin, 1915 | 36 | Eight years of math. Gravity is not a force — it is curved spacetime |
| 16 | The Eclipse | 1919 | 40 | Eddington photographs starlight bending around the sun. Einstein becomes world-famous overnight |
| 17 | Leaving Germany | 1933 | 54 | Nazis rise. Einstein is in the US when Hitler takes power. He never returns. Princeton becomes home |
| 18 | The Letter | 1939 | 60 | Signs Szilard's letter warning Roosevelt about atomic bombs. Later: "I made one great mistake" |
| 19 | God Does Not Play Dice | Princeton, 1930s-50s | 50-70 | Quantum debate with Bohr. Violin. Refuses Israeli presidency (1952). Dies 1955, refuses surgery |
| 20 | Legacy | — | — | Closing image using curved spacetime as the visual structure — moments of his life plotted on a bent grid |

## Production Workflow

### Phase 1: Reference Generation
1. Generate character reference sheets (4:3 landscape, portrait + full body)
2. Save to `refs/` folder
3. Review for quality and consistency before proceeding

**Characters requiring reference sheets:**
- Albert as child (5-10) — short dark hair, round cheeks, dreamy eyes
- Albert as teenager (15-17) — slimmer, curly dark hair starting to lift, beginnings of mustache
- Albert as young man (23-28) — patent office era, trim mustache, dark hair, sharp alert eyes — **primary look for pages 7-14**
- Albert in middle age (36-40) — Berlin/eclipse era, mustache fuller, hair starting to grey and lift
- Albert as elder (60-76) — Princeton era, iconic white hair, deep-lined face, wool sweater — **secondary primary look for pages 17-19**
- Hermann Einstein (father) — one scene, the compass
- Uncle Jakob — one scene
- Max Talmud — one scene, young medical student
- Mileva Marić (19-28) — dark hair pulled back, serious eyes, Serbian
- Niels Bohr (elder) — one scene, the quantum debate

### Phase 2: Page Generation
1. Generate pages sequentially (page 1 → page 20)
2. Always upload relevant character reference images
3. Paste style block and character lock blocks verbatim into every prompt
4. Review each page for character consistency and text legibility
5. Regenerate any page that drifts before moving on

### Phase 3: Assembly
1. Collect all outputs in `pages/` folder
2. Build `index.html` reader (dark theme, page-flipping, quiz at end)
3. Update root `index.html` landing page

## Key Reminders

- **Character consistency:** Albert ages dramatically across the story. Use the correct age-specific reference for each page. Watch especially for hair — it goes from short dark to curly dark to wild white across the 20 pages.
- **NOT a children's book.** Serious, mature, painterly. Reinforce in every prompt.
- **Style block and character lock blocks: COPY VERBATIM** into every generation prompt.
- **Speech bubbles:** Keep under 15 words per bubble.
- **Caption boxes:** Prose narration and Einstein's own words (from letters, papers, quips).
- **Physics pages (10-15):** Diagrams should emerge naturally from the painterly world — chalk equations on a patent office desk, a falling elevator cutaway, curved-grid spacetime over a gravitating sun.
- **Aspect ratio:** 2:3 vertical for story pages, 4:3 landscape for reference sheets.
- **2000 character prompt limit:** Condense script prompts at generation time while keeping all dialogue verbatim.

## Key Objects and Motifs

- **The compass** (page 2) — reappears as a visual echo in the final legacy page
- **The violin** — seen in Bern, Berlin, Princeton
- **Chalk equations** — scribbled on patent desks, cafe napkins, blackboards
- **The wild white hair** — only emerges late; early pages are dark-haired and combed
- **Light** — literal light (compass, beam, eclipse) becomes a recurring visual motif that ties pages together

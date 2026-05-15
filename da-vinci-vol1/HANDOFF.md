# Leonardo da Vinci — Session Handoff

**Source of truth across restarts.** Read this top-to-bottom before resuming.

---

## ✅ SHIPPED 2026-05-09

Book One ("The Boy Who Watched Birds · Leonardo da Vinci · Book One") is complete:
- 10 refs (4 Leonardo age phases + Verrocchio + Ludovico + Salaì + 3 object refs)
- Cover + 22 pages
- 5-question quiz (revised 2026-05-10 after kid feedback — see "Quiz revision" below)
- Dark-themed reader at `da-vinci-vol1/index.html`
- Landing card added to repo root `index.html`
- Total image cost ≈ $7.75 on gpt-image-2 standard

See `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/project_da_vinci_retrospective.md` for the full retrospective.

---

## Window covered

**1452 → December 1499** (~47 years). Closing beats: fall of Milan to Louis XII, clay Sforza horse destroyed by French archers, first flake of the Last Supper, road south with Pacioli and Salaì.

**Deliberately not in this volume** (Book Two material):
- Florence-2 (1500–1506), the Mona Lisa, the Battle of Anghiari cartoon.
- Move to France (1516), Cloux 1519, the king at the bedside.
- The 1476 sodomy accusation.
- Vitruvian Man as a hero page (used only as a notebook motif).
- White-bearded prophet portrait (older-man image — Milan-period Leonardo is 30s–40s with dark hair and a neat beard).

Book Two is plantable but not promised. Per the user's standing instruction, do not foreshadow it heavily.

---

## Production stack (locked, do not change without asking)

- **Model:** `gpt-image-2` standard via `mcp__openai-image-2__{generate_image,edit_image}`. Newton/Honda oil-painting register. No model swap.
- **Aspect:** 3:2 landscape, 1536×1024.
- **Reader:** dark theme, `max-width: min(1400px, 96vw)`, fixed circular nav arrows at the viewport edges, ← / → / spacebar keys, mobile swipe, 5-question quiz at end.
- **Lettering formula:** the Honda formula — off-white parchment caption boxes with dark serif text, opened with "LETTERING — verbatim, render exactly:" preamble and closed with the no-spurious-text restrictions block. Render text exactly as quoted in `04-SCRIPT.md`.

---

## Quiz revision (2026-05-10)

Kids noticed that the longest answer was always the correct one. Quiz rewritten so:
- Correct answer is no longer always the longest option.
- Distractors are substantive — plausible-sounding wrong answers with period detail, similar in length to the correct answer.
- Correct positions shuffled across questions (currently b, c, a, b, a).
- Still tests WHY not WHAT.

**This is now a project-wide rule.** Future biography quizzes must follow it. Recorded in `MEMORY.md` under "CRITICAL QUIZ-WRITING RULE".

---

## Production notes from the ship

- **Three-prototype gate worked.** P1 (kite memory, T5 cinematic), P7 (primary-source letter to Sforza, T5+ with 10 verbatim numbered points), P22 (closing-as-invention notebook page with 12 vignettes) all passed first generation. Remaining 20 pages bulk-batched in two parallel waves of 10 once the template was validated.
- **One safety-filter rejection on P17 (anatomy/dissection).** Original prompt described the chest cavity being opened with a bronze hook. Moderation blocked. Fix: re-anchored on Leonardo at his lectern drawing the heart in his notebook, with the body fully draped under a heavy white linen sheet and only abstractly suggested at the side of the frame. Passed on retry. **Lesson for future anatomy pages: lead with the artifact (the notebook page, the diagram) not the dissection. The sheet stays on.**
- **Multi-character page strategy on gpt-image-2** (no `compose_images`): lock to the harder-to-describe face via `edit_image`, describe Leonardo richly in prose at the age-correct lock. Used on P3 (Verrocchio), P8 (Ludovico), P13 (Ludovico + crowd + horse), P19 (Ludovico), P20 (horse as the lock). No drift.
- **The 4-age-phases-of-Leonardo ref strategy** (ages 10, 17, 30, 45) handles the 47-year arc cleanly. Always feed the age-correct ref into the corresponding page.
- **The closing-as-invention page (P22)** is the highest-leverage page in the book and the cheapest to design. One image, 12 callbacks. Notebook page with embedded sketches of every major beat in the volume.

---

## Repo state at ship

Shipped in commit `81c5baa` on `main`: *Add The Boy Who Watched Birds: Leonardo da Vinci, Book One*. 41 files changed (research dossier + 5 planning docs + reader + 10 refs + 23 page images + landing card). Pushed to `origin/main`. Live at `https://andressolve.github.io/nano/da-vinci-vol1/`.

The research dossier lives at `~/Documents/nano/da-vinci-vol1-research/source-dossier.md`. **Do not introduce facts not in the dossier.** If a future page (Book Two work) needs a detail not yet documented, add it to the dossier with a source first.

---

## If asked to start Book Two

1. Create `~/Documents/nano/da-vinci-vol2/` and `~/Documents/nano/da-vinci-vol2-research/`.
2. Window: late December 1499 → death at Cloux, 2 May 1519. Beats include Mantua, Venice, Florence-2 (Battle of Anghiari, Mona Lisa, the dissections continued), Rome under Leo X, the move to France with Francis I, Cloux 1517–1519, the king at the bedside.
3. Refs to plan: Leonardo at ~52 (Florence-2), ~62 (Rome), ~67 (Cloux); Francis I; Salaì at ~30; Francesco Melzi as the young noble apprentice. Pacioli already locked from Book One; reuse.
4. Cover register: the older Leonardo with the white beard (the one we explicitly did NOT use in Book One). The Self-Portrait of Turin (red-chalk, c.1512) is the model.
5. Use the same gpt-image-2 standard pipeline; same Honda formula lettering; same reader; same ~$7.50 cost envelope.
6. Apply the new quiz rule from day one — no length tells, shuffled positions, substantive distractors.

---

## Files in this folder

- `00-PROJECT-BRIEF.md` — title, audience standard, window, production order.
- `01-STYLE-GUIDE.md` — register block, palette per act, lettering rules, mirror-writing fallback.
- `02-CHARACTERS.md` — 4 Leonardo age locks + Verrocchio + Ludovico + Salaì + 3 object refs.
- `03-SETTINGS.md` — 11 recurring locations from Vinci to the road south.
- `04-SCRIPT.md` — full 22-page script with verbatim text and density tiers.
- `refs/` — 10 generated reference sheets.
- `pages/` — cover + 22 page images.
- `index.html` — reader.

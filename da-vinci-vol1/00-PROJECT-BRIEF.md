# The Boy Who Watched Birds — Project Brief

Biographical graphic novel about Leonardo da Vinci. **Book One** of his life: from his birth in Vinci (1452) through his departure from Milan with Luca Pacioli (December 1499) — the cradle, Verrocchio, the abandoned Adoration, the letter to Sforza, the Lady with an Ermine, the lost bronze horse, and the Last Supper that began to flake while it was still being painted.

## Working thesis

Leonardo da Vinci was barred from his father's profession by an accident of birth, so he taught himself to read the world directly — and ended up reading it more carefully than anyone in Europe. Book One ends in 1499, with the Sforza horse shot to pieces by French archers and the Last Supper already failing on its wall. Leonardo leaves Milan with two saddlebags of notebooks and the discipline that made them.

Sub-themes:
- A boy with no university education turns observation into a method.
- The hand that paints the angel grows into the hand that dissects the heart.
- Ambition outruns completion: the Adoration is abandoned, the bronze horse is destroyed, the Last Supper begins to flake. The notebooks survive.
- A kite that visits a cradle becomes a flying machine fifty years later.

## Source of truth

`/Users/andresrodriguez/Documents/nano/da-vinci-vol1-research/source-dossier.md` — verified facts, dates, and verbatim quotes. **Do not introduce facts not in the dossier.** If a page needs a detail not yet documented, add it to the dossier with a source first.

## Window choice

**1452 → December 1499.** This is a ~47-year window with a clean dramatic close (the fall of Milan, the destruction of the horse, the road south with Pacioli). Book Two would cover Florence-2, the Mona Lisa, France, and Cloux 1519. We are committing to Book One only; Book Two is plantable but not promised.

## Audience standard (project-wide, do not violate)

Per `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md`:
**Never frame as "for ages 7–10." Never pitch the writing down by age.** Standard: write so any first-time reader who has never heard of Leonardo da Vinci can follow on first read. No info-withholding. No gaps. No jigsaw-puzzle reading.

The standing user complaint is *no terse crap; the reader should not be filling in blanks.* Operationalize as **T4–T5 density per hero page**. If a page would have to be terse to fit the format, redesign or split.

## Format

- 22 story pages + cover + 5-question quiz page (HTML).
- Aspect: **3:2 landscape, 1536×1024**, image-native lettering.
- Reader: dark theme, page-flipping, arrow-key nav, fixed side-arrow buttons, 1400px max-width.
- Image model: **gpt-image-2 standard** (Newton/Honda register). No model swap planned. Oil-painting realism — explicitly NOT a comic.

## What's deliberately not in this volume

- The Mona Lisa, the second Florence period, the move to France, and Leonardo's death — Book Two material. Do not foreshadow heavily.
- Vitruvian Man as a hero page — drawn ~1490 but its iconic register is later. Use it only as a notebook-page motif if at all.
- The 1476 sodomy accusation. Not central to Book One's human spine; skip.
- White-bearded prophet portrait of Leonardo — that's the older man. In Milan he was 30s–40s with dark hair and a neat beard.

## Curricular hook (Lyceum)

Lyceum directory contains no markdown lessons currently. The kids will encounter Leonardo through:
- **Anatomy** — observation drawings of the body, parallel to any biology unit.
- **Mirror writing** — the kid can try writing right-to-left with their non-dominant hand.
- **Geometry / perspective** — the *De Divina Proportione* connection (Pacioli/Leonardo).
- **Hydraulics** — water vortex sketches anyone can replicate at a stream.

These are noted in the script as "kid-can-do" beats so the reader can put down the book and act on it.

## Production budget estimate

- 10 refs × $0.21 ≈ $2.10
- 23 page images × $0.21 ≈ $4.83
- 4 prototype regens × $0.21 ≈ $0.84
- **Total: ~$7.75** — in line with Newton ($7.35) and Honda ($7.50) envelopes.

## Files in this folder

- `00-PROJECT-BRIEF.md` — this file.
- `01-STYLE-GUIDE.md` — register block, palette per act, lettering rules.
- `02-CHARACTERS.md` — character + object reference specs.
- `03-SETTINGS.md` — Vinci hill country, Verrocchio's workshop, Ludovico's court, the refectory of Santa Maria delle Grazie.
- `04-SCRIPT.md` — 22-page script with verbatim text and density tiers.
- `refs/` — generated character and object reference sheets.
- `pages/` — generated page images.
- `index.html` — reader (built last).

## Production order

1. Refs (Leonardo at 4 ages + Verrocchio + Ludovico + Salaì + 3 object refs).
2. Three prototype pages: P1 (cinematic — kite memory), P7 (primary-source — letter to Sforza), P22 (closing-as-invention).
3. If prototypes pass: parallel-batch cover + remaining pages.
4. Drift review and repair — pay extra attention to text rendering. Revise any page where a verbatim string is wrong.
5. Reader.
6. Landing-page card.
7. Memory + retrospective update.

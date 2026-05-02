# The Boy Who Chased Engines — Project Brief

Biographical graphic novel about Soichiro Honda. Part 1 of his life: childhood through global motorcycle proof (~1906–1963).

## Status of this folder vs. `honda/`

`honda/` is Codex's research and planning archive. It contains the source dossier, beat map, and style guide that this project builds on. **Do not delete `honda/`** — its source dossier and style guide are referenced from this brief.

This folder (`honda-soichiro/`) is the production project: trimmed script, references, generated pages, reader, quiz.

## What we keep from Codex's work

- `honda/source-dossier.md` — verified chronology with confidence flags. **The source of truth for facts.** Do not rewrite events without consulting it.
- `honda/style-guide.md` — palette, lettering rules, character-age phases, machine continuity. Adopt as-is.
- `honda/reference-plan.md` — character and object reference list. Use the prompts there as starting points.

## What we change from Codex's approach

1. **Density per page goes from T2-T3 (25-60 words) up to T4-T5 (90-150 words).** Codex's prototypes were terse — readers fill in blanks. The T5 text-density test (2026-05-02) proved Pro can render 6 elements / 118 words verbatim per page. Use that ceiling.
2. **Pro endpoint is the default for hero pages, not Flash.** Codex's Page 20 prototype showed Flash's bubble-duplication failure on a partnership scene; Pro fixed this in our test on the same density.
3. **Refs are generated FIRST and not skipped.** Codex's plan said this; Codex's execution did not.
4. **Page count trimmed from 34 to ~24** by combining bridge pages, so each page can carry more weight without the book feeling padded.
5. **Reader is built** as a standard nano dark-theme page-flipper with quiz, not as one-off demo HTMLs.
6. **Landing-page card** is added on completion.

## Working thesis

Soichiro Honda learned by failing in public, and built machines that gave ordinary people freedom to move.

Sub-themes (from Codex's dossier, retained):
- A boy learns that machines answer honestly.
- Repair teaches him respect for reality.
- Manufacturing teaches him that "almost right" is failure.
- War destroys the first version of his dream.
- Postwar scarcity turns small engines into social freedom.
- Fujisawa reveals that a machine cannot help people if no system carries it to them.
- The Super Cub proves the philosophy: high quality, low cost, easy use, broad dignity.

## Target

- 24 story pages + cover + 5-question quiz page (HTML).
- Format: 3:2 landscape, 1536×1024, image-native lettering.
- Reader: dark theme, page-flipping, arrow-key nav, quiz at end.
- Tone: nuanced persistence, not founder worship. Sober about war, postwar scarcity, and near-collapses.

## Audience standard (project-wide)

Per `~/.claude/projects/-Users-andresrodriguez-Documents-nano/memory/MEMORY.md`:
**Never frame as "for ages 7-10." Never pitch the writing down by age.** The standard is: write so any first-time reader who has never heard of Soichiro Honda can follow on first read. No info-withholding, no gaps, no jigsaw-puzzle reading. Francisco (9) and Sebastian (7) are the test users for whether the writing is clear, not the ceiling on its sophistication.

This is the standard the user's complaint about Codex's terse pages was pointing at. Each page should answer: *what changed, and why does it matter?* without the reader needing to know the period, the company, or the machinery.

## Production budget estimate

- Refs (5 Honda + Fujisawa + ~4 objects): ~$1.50
- 3 prototype pages on Pro: ~$0.40
- 21 production pages (mix Pro/Flash): ~$3.00
- **Total: ~$5**

## Files in this folder

- `00-PROJECT-BRIEF.md` — this file.
- `01-STYLE-GUIDE.md` — pointer to `honda/style-guide.md` plus deltas.
- `02-CHARACTERS.md` — character reference specs (adapted from `honda/reference-plan.md`).
- `03-SETTINGS.md` — settings inventory.
- `04-SCRIPT.md` — trimmed 24-page script with T4-T5 density per page.
- `05-PRODUCTION-LOG.md` — appended as work proceeds.
- `refs/` — generated character and object reference sheets.
- `pages/` — generated page images.
- `index.html` — reader (built last).

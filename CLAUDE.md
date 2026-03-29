# CLAUDE.md — Project Notes for nano

## Project Overview

This repo contains illustrated stories for kids (Francisco, 9, and Sebastian, 7). Stories combine narrative text or graphic novel pages with AI-generated images. Each story lives in its own folder with an `index.html` reader.

## Story Formats

- **Text + illustration**: Page-by-page HTML reader with prose, dialogue, and inline images (~4-6 images per story). Light parchment theme. Includes 5-question quiz at the end.
- **Graphic novel**: Full comic pages generated as images (15-20 pages). Dark-themed page-flipping reader. All dialogue baked into speech bubbles in the images. Full project docs (00-brief, 01-style, 02-characters, 03-settings, 04-script).
- **Illustrated essay**: Expository prose with fact boxes, pull quotes, and inline illustrations. No fictional protagonist arc. Clean modern reader.

## Story Catalog

### Text + Illustration

| Folder | Title | Setting | Protagonist | Theme |
|--------|-------|---------|-------------|-------|
| `marcus/` | The View From Above | Rome, 170 CE | Gaius, ~13 | Perspective — a humiliated boy meets Marcus Aurelius, who teaches him to zoom out on his shame |
| `orchard/` | The Orchard of Small Things | Mediterranean coast, 12th c. | Theo, 13 | Patience — restless boy apprentices with an orchard keeper, learns that small daily acts compound |
| `lantern-and-sword/` | The Lantern and the Sword | Sengoku Japan, 16th c. | Koji, 11 | Courage — lantern-maker's son shelters a wounded samurai, learns light outweighs swords |
| `mapped-the-wind/` | The Boy Who Mapped the Wind | Polynesian Pacific, ~1100 AD | Koa, 12 | Attention — navigator-in-training learns to read waves, birds, and clouds from his grandfather |

### Graphic Novel — Salt and Stone (4-volume saga, one protagonist across 25 years)

| Folder | Subtitle | Setting | Nikos's age | Pages | Core arc |
|--------|----------|---------|-------------|-------|----------|
| `salt-and-stone/` | Life One: The Boy | Aegean & Sidon, ~480 BC | 9-10 | 15 | Island destroyed by Persians. Father saves him. Shipwrecked near Sidon. Taken in by Phoenician shipwright Hasdrubal. Chooses to stay. |
| `salt-and-stone-two/` | Life Two: The Youth | Sidon, Salamis & Athens | 14-15 | 15 | Conscripted into Xerxes' fleet. Fights Greeks at Salamis from Persian side. Rescued by Athenians. Settles in Athens, marries Lyra. |
| `salt-and-stone-life-three/` | Life Three: The Man | Athens & Scythian Steppe | 19-20 | 20 | Conscripted again. Third shipwreck. Found by Asha (Scythian rider). Burns the wooden ship. Keeps the shell necklace. Chooses the steppe. |
| `salt-and-stone-life-four/` | Life Four: The Father | Pontic Steppe, ~468 BC | 25-26 | 20 | Married to Asha, son Kian (4). Targitaos dies. Nikos tells Kian everything, gives him the shell necklace. Family rides together. Series complete. |

**Key objects:** Shell necklace (mother's → passes to Kian), carved wooden ship (burned in Life Three), carved wooden horse (new in Life Four).

### Graphic Novel — House of Atreus (2-volume Greek mythology)

| Folder | Subtitle | Chapters | Pages | Core arc |
|--------|----------|----------|-------|----------|
| `house-of-atreus-vol1/` | Vol 1: The Curse | Tantalus's feast → Pelops's chariot race → Atreus vs. Thyestes | 15 | Three generations of sin: each believes they're justified, each makes things worse. Ends with Atreus's horrific feast. |
| `house-of-atreus-vol2/` | Vol 2: The Reckoning | Iphigenia's sacrifice → Clytemnestra's revenge → Orestes's trial | 18 | Agamemnon sacrifices his daughter for wind. Clytemnestra kills him. Orestes kills her. Athena breaks the cycle with the first jury trial. Justice replaces vengeance. |

### Graphic Novel — The Trial of Socrates (single volume)

| Folder | Setting | Protagonist | Pages | Core arc |
|--------|---------|-------------|-------|----------|
| `trial-of-socrates/` | Athens, 399 BC | Alexis, 14 (potter's son, POV) | 15 | A boy watches Socrates' trial, conviction, and death. When Socrates refuses escape, Alexis must reckon with integrity vs. survival. Connects to House of Atreus (same city, same theme of public justice) and Salt and Stone (overlapping Athens timeline). |

### Illustrated Essay

| Folder | Title | Setting | Pages | Topic |
|--------|-------|---------|-------|-------|
| `shock-of-florence/` | The Shock of Florence | France & Florence, 1460 | 10 | How encountering radically different art and thought in Renaissance Florence could reshape a person's worldview. Inspired by Ada Palmer. |

### Dual Story (new format: two parallel stories, interleaved)

| Folder | Title | Settings | Protagonists | Pages | Topic |
|--------|-------|----------|--------------|-------|-------|
| `the-builders/` | The Builders | Segovia, Roman Hispania (~90 AD) & Persian Empire (~500 BC) | Marcus, 12 (engineer's son) & Sana, 11 (muqanni's daughter) | 8 dual pages + ending + quiz | Same problem (city needs water), two solutions (aqueduct vs. qanat). Both use gravity and precision. First girl protagonist. First dual-story format. |

## What the Collection Covers (and Doesn't)

**Geographies:** Greece/Mediterranean (heavy), Rome, Phoenicia, Japan, Polynesia, Scythian Steppe, Renaissance Italy, Roman Hispania (Spain), Persia. **Missing:** Africa, the Americas, India/South Asia, China.

**Historical periods:** ~500 BC through 16th century, plus Greek mythology. **Missing:** Anything modern, anything pre-classical (Egypt, Mesopotamia, Neolithic).

**Themes:** Perspective, patience, courage, attention, displacement/belonging, inheritance, justice vs. vengeance, integrity, engineering/invisible work. **Missing:** Friendship/loyalty, creativity/invention, humor, failure/resilience.

**Protagonists:** Mostly boys ages 9-15. Salt and Stone ages Nikos to 26. House of Atreus has ensemble adults. The Builders introduces first girl protagonist (Sana, 11). **Missing:** Younger child protagonist (closer to Sebastian's age, 7), non-human perspective.

**Tone:** Serious and contemplative throughout. **Missing:** Comedy, adventure-for-adventure's-sake, mystery.

## Image Generation — Gemini Nano Banana MCP

### Tool Selection

- `compose_images`: Use when a page features 2+ characters and you have reference images for each. Requires minimum 2 images.
- `edit_image`: Use when a page features a single character. Pass one reference image.
- `generate_image`: Use when no reference image is needed (e.g., back cover, purely scenic).

### Prompt Constraints

- **2000 character limit** on prompts. Full script prompts from the markdown docs will exceed this — condense while keeping: panel layout, key visual details, all text/captions/speech bubbles verbatim, and character identifiers.
- Don't paraphrase dialogue or caption text — copy it exactly so the model renders it correctly.

### Character Consistency

- Always generate reference sheets first (4:3 landscape, portrait + full body), then feed them into every page generation.
- Character lock descriptions should be condensed but explicit about: skin tone, age, hair color/style, face shape, and signature marks (scars, jewelry, accessories).
- Character consistency weakens when characters are distant, small in frame, or in unusual poses. Regenerate with stronger lock language if drift occurs.
- For child characters: models drift toward children's book aesthetics. Include "NOT a children's book. Serious mature graphic novel, realistic proportions" in every prompt. Watch for oversized eyes, rounded features, bright saturated colors, soft focus.

### File Handling

- The MCP tool sometimes appends `_1` to output filenames instead of overwriting existing files. After regenerating, `mv` the new file to the correct name.

### Text Rendering

- Text in caption boxes and speech bubbles generally renders clean and legible.
- Keep speech bubble dialogue under 15 words for best results.
- Sound effects (KRAAASH, KRAAAKOOM) render well when marked as "large" or "bold" in the prompt.

## Workflow for Generating a Graphic Novel

1. Read all project docs (brief, style guide, characters, settings, script).
2. Generate character reference sheets (one per character, 4:3 landscape).
3. Review references for quality and consistency before proceeding.
4. Generate pages sequentially, always including relevant reference images.
5. Review each page for character consistency, text legibility, and style drift.
6. Regenerate any page that drifts before moving on.

## Repo Structure

```
nano/
  index.html                    # Landing page (card grid, links to all 13 pieces)
  marcus/                       # Text + illustration
  orchard/                      # Text + illustration
  lantern-and-sword/            # Text + illustration
  mapped-the-wind/              # Text + illustration
  salt-and-stone/               # Graphic novel (Life One)
  salt-and-stone-two/           # Graphic novel (Life Two)
  salt-and-stone-life-three/    # Graphic novel (Life Three)
  salt-and-stone-life-four/     # Graphic novel (Life Four)
  house-of-atreus-vol1/         # Graphic novel (Vol 1)
  house-of-atreus-vol2/         # Graphic novel (Vol 2)
  trial-of-socrates/            # Graphic novel (single volume)
  shock-of-florence/            # Illustrated essay
  the-builders/                 # Dual story (new format)
```

Each graphic novel folder contains: `00-PROJECT-BRIEF.md`, `01-STYLE-GUIDE.md`, `02-CHARACTERS.md`, `03-SETTINGS.md`, `04-SCRIPT.md`, `index.html`, `refs/`, `pages/`.
Each text+illustration folder contains: `index.html` with all prose and image references inline.
Deployed via GitHub Pages at `https://andressolve.github.io/nano/`.

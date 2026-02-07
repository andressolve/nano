# CLAUDE.md — Project Notes for nano

## Project Overview

This repo contains illustrated stories for kids (Francisco, 9, and Sebastian, 7). Stories combine narrative text or graphic novel pages with AI-generated images. Each story lives in its own folder with an `index.html` reader.

## Story Formats

- **Text + illustration** (marcus/, orchard/): Page-by-page HTML reader with prose, dialogue, and inline images. Includes quiz at the end.
- **Graphic novel** (salt-and-stone/): Full comic pages generated as images. Dark-themed page-flipping reader. No separate text — all dialogue is baked into the images.

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
  index.html              # Landing page linking to all stories
  marcus/                 # "The View From Above" — text + illustration
  orchard/                # "The Orchard of Small Things" — text + illustration
  salt-and-stone/         # "Salt and Stone" — graphic novel
    00-PROJECT-BRIEF.md
    01-STYLE-GUIDE.md
    02-CHARACTERS.md
    03-SETTINGS.md
    04-SCRIPT.md
    index.html            # Dark-themed comic reader
    refs/                 # Character reference sheets
    pages/                # Generated comic pages
```

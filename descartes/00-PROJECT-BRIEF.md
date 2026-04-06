# Cogito: The Life of René Descartes

## Project Overview

| Field | Value |
|-------|-------|
| **Title** | Cogito |
| **Subtitle** | The Life of René Descartes |
| **Format** | Biographical graphic novel |
| **Target audience** | Francisco (9) and Sebastian (7) |
| **Image model** | Gemini via Nano Banana MCP |
| **Page count** | 20 (cover + 19 story/legacy pages) |

## Concept

A portrait of René Descartes — not as a statue on a pedestal, but as a living person. A sickly child who was allowed to stay in bed all morning and used that stillness to think harder than anyone before him. A restless young man who joined an army just to see the world. A father who wept when his daughter died. A philosopher who stripped away every certainty until only three words remained: *I think, therefore I am.*

This is the first biographical graphic novel in the collection. No fictional POV character — Descartes himself is the protagonist. The story spans his life from age 5 to death at 53, structured around the key moments that made him who he was.

## What the Kids Will Take Away

- You can change the world by lying in bed and thinking
- Mathematics gives certainty that nothing else can
- Questioning everything is not rebellion — it's the beginning of knowledge
- Even the greatest thinkers grieve, doubt, and feel lost
- Two perpendicular lines can describe any point in the universe

## Project Structure

| Document | Purpose |
|----------|---------|
| `00-PROJECT-BRIEF.md` | This file — overview and workflow |
| `01-STYLE-GUIDE.md` | Visual direction, palette, panel conventions |
| `02-CHARACTERS.md` | Character lock blocks and reference sheet prompts |
| `03-SETTINGS.md` | Location descriptions and visual references |
| `04-SCRIPT.md` | Full page-by-page script with generation prompts |

## Production Workflow

### Phase 1: Reference Generation
1. Generate character reference sheets (4:3 landscape, portrait + full body)
2. Save to `refs/` folder
3. Review for quality and consistency before proceeding

**Characters requiring reference sheets:**
- René as child (5-11)
- René as student (14-17)
- René as young man (22-23)
- René as philosopher (32-53) — **primary look, most pages**
- Isaac Beeckman (30, one key scene)
- Francine (4-5, one key scene)
- Queen Christina (22-23, one key scene)

### Phase 2: Page Generation
1. Generate pages sequentially (page 1 → page 20)
2. Always upload relevant character reference images
3. Paste style block and character lock blocks verbatim into every prompt
4. Review each page for character consistency and text legibility
5. Regenerate any page that drifts before moving on

### Phase 3: Assembly
1. Collect all outputs in `pages/` folder
2. Build `index.html` reader (dark theme, page-flipping)
3. Update root `index.html` landing page

## Key Reminders

- **Character consistency:** René ages across the story. Use the correct age-specific reference for each page.
- **NOT a children's book.** Serious, mature, painterly. Reinforce in every prompt.
- **Style block and character lock blocks: COPY VERBATIM** into every generation prompt.
- **Speech bubbles:** Keep under 15 words per bubble.
- **Caption boxes:** Prose narration and Descartes' own words (from letters, the Discourse, etc.).
- **Mathematical pages (15, 20):** Diagrams should emerge naturally from the painterly world — precise geometric lines against warm, textured backgrounds.
- **Aspect ratio:** 2:3 vertical for story pages, 4:3 landscape for reference sheets.
- **2000 character prompt limit:** Condense script prompts at generation time while keeping all dialogue verbatim.

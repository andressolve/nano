# The Invisible Forces — Prompt Architecture

## Purpose

This document defines how prompts should be assembled for Newton Book One.

The goal is not verbal elegance. The goal is reliable generation.

## Core Rule

Every page prompt should be assembled from **stable reusable blocks** plus a **page-specific visual job**.

Do not improvise the whole page from scratch each time.

## Prompt Stack

Each production prompt should use these layers, in this order:

1. `Use case / asset type`
2. `Page objective`
3. `Panel or composition structure`
4. `Character lock blocks`
5. `Setting lock block`
6. `Science or narrative burden`
7. `Exact text to render`
8. `Constraints / avoid list`
9. `Style reinforcement if drift risk is high`

## Master Style Block

Use the style block from `/Users/andresrodriguez/Documents/nano/newton-vol1/01-STYLE-GUIDE.md` verbatim.

It is the top-level visual anchor.

## Character Lock Rules

- Use only the age-appropriate Newton lock for a page.
- Never mix two Newton ages in one page prompt unless the page is explicitly designed as a memory or montage page.
- For supporting characters, include only the locks of figures who are large enough or central enough to need continuity.
- If a supporting character is background-only, describe them functionally instead of pasting the full lock block.
- If a page is already dense with diagrams, reduce the number of full character locks to preserve prompt budget and conceptual focus.

## Setting Lock Rules

- Use one primary setting lock per page.
- If a page crosses two settings, name one as dominant and treat the other as a secondary visual note.
- Reuse setting language exactly for recurring rooms, especially:
  - Woolsthorpe experimental chamber
  - Cambridge scholar's chamber
  - Cambridge study/workshop
  - Royal Society room

## Text Rendering Rules

Even with `gpt-image-2`, text remains easiest when it is short and high-contrast.

- Prefer `1–3` caption boxes per page.
- Prefer `0–2` speech bubbles per page.
- Avoid multiple tiny labels.
- If a diagram needs labels, keep them large and few.
- Never rely on in-image text to carry the whole logic of a science page.
- If exact wording matters, isolate it in a short labeled section:
  - `Text (verbatim): "..."`

## Narrative Page Prompt Template

```text
Use case: illustration-story / historical-scene
Asset type: graphic novel page
Page objective: <what the page must accomplish emotionally and narratively>
Composition structure: <single image, two panels, three panels, split page>
Primary request: <core scene description>
Subject: <main character + action>
Setting: <room/place>
Style/medium: serious painterly historical graphic novel
Lighting/mood: <specific light and emotional weather>
Character locks: <paste only relevant locks>
Setting lock: <paste or condense relevant setting lock>
Text (verbatim): "<exact caption/speech if any>"
Constraints: realistic proportions; serious mature graphic novel; historical plausibility; readable caption boxes only if needed
Avoid: children's book softness; cartoon exaggeration; generic fantasy; clutter; tiny illegible text
```

## Science Page Prompt Template

```text
Use case: illustration-story / historical-scene
Asset type: explanatory graphic novel page
Page objective: <the scientific question this page must answer>
Question to show: <one sentence>
Composition structure: <how the argument will be seen>
Primary request: <the experiment, inference, or comparison>
Subject: Isaac Newton + apparatus / notebook / object / celestial comparison
Setting: <specific room or landscape>
Science burden: <what must be visually understandable>
Character locks: <usually Newton only>
Setting lock: <specific setting block>
Required visible elements: <apparatus, beam, second prism, orbit line, diagram sheet, etc.>
Text (verbatim): "<exact short captions or labels only>"
Constraints: one main argument only; readable and sparse labels; geometry must emerge from real objects and surfaces; realistic 17th-century materials
Avoid: textbook clutter; mystical cosmic symbolism; decorative rainbow effects; floating infographic overlays; tiny text
```

## Revision Prompt Template

Use after a page is mostly right and only one thing is wrong.

```text
Revise this page.
Change only: <one specific issue>
Keep unchanged: character identity, composition, palette, period setting, all correct text
Still required: <one-line page objective>
Avoid: any new layout drift, any costume drift, any extra text
```

## Page-Type Guidance

### Single-Character Narrative Pages

Best for:
- pages 4, 8, 9, 16, 18, 19, 24

Guidance:
- keep composition simple
- let the room or object tell half the story
- avoid unnecessary support characters

### Two-Character Intellectual Confrontation Pages

Best for:
- pages 3, 6, 20, possibly 22

Guidance:
- distinct silhouettes and energy contrast matter more than crowd detail
- use short dialogue only
- one speaker should visually dominate each panel

### Apparatus / Experiment Pages

Best for:
- pages 10, 11, 17

Guidance:
- make the object readable before making it beautiful
- one apparatus per page unless the comparison itself is the point
- put the experiment in a believable room, not abstract void

### Diagram-Argument Pages

Best for:
- pages 12, 14, 15, 21, 23

Guidance:
- anchor every line to paper, chalk, or visible physical demonstration
- avoid overpopulating the frame
- if the concept requires too many labels, redesign the composition

## Science-Page Discipline

For Newton Book One, every science page should answer exactly these three questions:

1. What is the question?
2. What did Newton see, test, or infer?
3. Why does the conclusion matter beyond this immediate scene?

If a draft prompt cannot support those three answers, it is not ready.

## Prompt Budget Discipline

Do not waste prompt space on decorative flourishes.

Always prioritize:

1. page objective
2. composition
3. Newton age lock
4. experiment or diagram logic
5. exact text
6. setting atmosphere

## Drift Controls

Add the anti-drift line from `/Users/andresrodriguez/Documents/nano/newton-vol1/01-STYLE-GUIDE.md` whenever the page features:

- child Newton
- prism color
- cosmic or orbital imagery
- pages with multiple small panels

## What To Do If A Page Still Fails

If a page keeps failing, do not keep re-rolling blindly.

Try in this order:

1. reduce text
2. reduce number of panels
3. reduce number of characters
4. reduce number of simultaneous ideas
5. split the page conceptually
6. prototype the hardest subproblem as its own simpler image

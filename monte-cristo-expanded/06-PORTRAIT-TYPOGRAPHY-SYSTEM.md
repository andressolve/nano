# The Count of Monte Cristo — Portrait Typography System

## Purpose

The expanded edition combines live graphic-novel scenes, illustrated prose,
and silent spectacle without asking the reader to change reading habits from
page to page.

Typography is part of each image's original composition. It is never an HTML,
SVG, or reader overlay, and it is never used to repair art that was composed
without room for text.

## Canvas and Safe Area

- Finished canvas: **1024 × 1536 portrait**.
- Outer safe margin: **64 px** on every side.
- Minimum panel gutter: **24 px**.
- No essential text below 72 px from the bottom edge.
- No balloon, caption, or prose field crosses a panel border.
- The page number belongs to the reader interface and does not appear inside
  the story image.

## Lettering Family

All three text forms belong to one restrained editorial family:

1. **Speech:** dark upright hand-lettered serif/sans hybrid; mixed case;
   expressive through rhythm and word choice, not decorative distortion.
2. **Narrative prose:** highly legible literary serif with moderate contrast;
   mixed case; short paragraphs; no faux-antique display treatment.
3. **Small sounds and object text:** the same family, simplified and enlarged
   enough to remain readable.

Avoid:

- condensed comic-display lettering;
- modern geometric UI fonts;
- cursive body text;
- all-capital prose;
- faux-aged or distressed letterforms;
- tiny handwritten documents carrying essential facts.

## Speech Balloons

- Warm ivory fill, never pure digital white.
- Restrained charcoal-brown outline with a hand-painted edge.
- Normal target lettering height: **44–50 px** on the 1024 × 1536 canvas.
- Short reply target: **48–54 px** when space allows.
- Minimum approved lettering height: **40 px**.
- Comfortable balloon width: **240–390 px**.
- No more than approximately **24 words** in one balloon.
- Internal padding should feel generous: approximately one capital-letter
  height between text and outline.
- Tails point into open space immediately beside the speaker's mouth.
- A balloon belongs unmistakably to the person on its own side of the panel.

When a panel contains opposed speakers:

- first speaker occupies the upper position on that speaker's side;
- reply occupies the opposite upper or middle position;
- a second line from the first speaker drops lower on the original side;
- if that pattern remains ambiguous, split the exchange across panels.

## Illustrated-Prose Fields

- Matte parchment field integrated into the page design.
- Normal prose lettering height: **36–42 px**.
- Target line length: approximately **38–52 characters**, including spaces.
- Target paragraph length: **2–5 lines**.
- One or two prose fields per page; never scatter sentences across many
  caption boxes.
- Field width: normally **78–88% of the canvas**.
- Left-aligned text with a calm ragged right edge.
- Minimum internal padding: **42 px**.
- No busy art, faces, hands, maps, or documents behind the prose.

Prose fields should feel like pauses in the same story, not pasted editorial
notes. Their parchment color comes from the page palette:

- warm cream in Marseille and Villefort's world;
- cool gray-beige during transfer and prison;
- amber parchment in Faria's school;
- pale salt parchment near the sea and Monte Cristo.

## Hierarchy

Story text has only three visible levels:

1. narrative prose;
2. speech;
3. small sound or object label.

Production titles, page titles, scene titles, speaker names, density codes, and
editorial labels never appear in finished art.

Boldface, italics, enlarged shouting, and decorative color are exceptional.
Meaning should come first from staging, expression, silence, and the words
themselves.

## Page-Mode Application

### Dramatic scene

- Speech balloons only unless a brief transition is indispensable.
- Reserve balloon lanes before faces and objects are placed.
- Prefer 45–80 total words.
- A hard dialogue page may reach approximately 105 words only with large,
  protected lettering fields.

### Illustrated prose

- Compose the prose field first.
- Use one dominant image or a continuous-time sequence.
- Keep prose between approximately 50 and 120 words.
- Speech may appear only if the live interruption is the page turn.

### Spectacle or silence

- Text should occupy less than 15% of the visual attention.
- One short line may anchor scale or identity.
- Do not add prose to defend an image whose causal setup belongs on the
  previous page.

## Prototype-Specific Typographic Rhythm

| Page | Primary text form | Intended rhythm |
| --- | --- | --- |
| 12 | One prose field + six balloons | orientation, public ease, interruption |
| 13 | Seven balloons | patient testimony |
| 14 | Seven balloons | question, evidence, release |
| 15 | Eight short balloons + silent lower third | recognition, hesitation |
| 16 | Eight short balloons | reassurance, betrayal |
| 17 | One prose field + four balloons | transit, distance, revelation |
| 18 | Nine short balloons | processing, classification, erasure |

Pages 12 and 17 prove that prose can carry the reader between rooms without
turning the story into a treatise. Pages 15 and 16 prove that silence and
dialogue can share one moral decision without compressing it.

## Rejection Conditions

Reject and regenerate a full page when:

- any word differs from the exact script;
- a letter is malformed, missing, duplicated, or replaced;
- lettering must be interpreted from context rather than read;
- a balloon's tail points at the wrong speaker, a silent person, an object, or
  empty space;
- the first balloon encountered belongs to a later speaker;
- the reading path crosses backward;
- text touches a panel edge, face, hand, letter, flame, key, or other decisive
  object;
- prose appears over patterned or high-detail art;
- a story-world document carries essential information only through
  handwriting;
- a line becomes too small at normal reader size;
- the generated canvas is not 1024 × 1536 portrait.

## Reader-Size Test

**Display-target correction — 2026-08-07:** the intended readers will use
desktop monitors and only rarely tablets. A cold reader must be able to read
every line without zooming at the reader's normal desktop fit-to-height size.
Tablet is a secondary check. Phone-size and 390 px proofs may still expose
crowding, but they are no longer approval gates.

For future production QA:

1. inspect the 1024 × 1536 source;
2. inspect the page in the normal desktop reader without zooming;
3. inspect a representative tablet-size rendering when density or layout makes
   it useful;
4. read the sequence without production notes;
5. reject any page that requires desktop/tablet magnification, source
   knowledge, or a guess about balloon ownership.

## Prototype Result — 2026-07-27

Pages 12–18 were rendered as finished 1024 × 1536 images and historically
inspected at source size and a 390 px-wide display equivalent.

- Both illustrated-prose fields remained readable without zoom.
- Speech remained readable across T2, T3, and T4 pages.
- No page required lettering below the minimum scale.
- Page 14's first generation exposed a reversed visual dialogue order; the
  blocking was corrected and the full page regenerated.
- The accepted sequence confirms the prose-field, balloon, safe-area, and
  portrait-rhythm rules above.

See [`08-PROTOTYPE-QA.md`](08-PROTOTYPE-QA.md) for the complete audit.

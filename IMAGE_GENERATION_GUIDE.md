# Image Generation Guide: Character Consistency

This guide documents the reference-first workflow for generating illustrated stories with consistent characters.

It was originally written around Gemini MCP tools, but the same workflow still applies when using newer OpenAI image models such as `gpt-image-2`: lock the characters first, keep page text sparse, prototype the hardest pages early, and use targeted revisions instead of hoping the model will maintain continuity by itself.

## The Problem

When generating multiple images for a story, characters often look different in each image - different faces, hair, clothing, etc. This breaks immersion.

## The Solution: Character Reference Images

Generate **reference images** of each character first, then use those as inputs when generating scene images.

---

## Workflow

### Step 1: Define Character Descriptions

Write detailed, consistent character descriptions. Include:

- Age
- Hair (color, style, length)
- Skin tone
- Eye color/description
- Clothing (specific colors and details)
- Build/posture
- Any distinctive features

**Example - Gaius:**
```
Young Roman boy, approximately 12-13 years old, short dark curly hair,
olive Mediterranean skin, large expressive dark brown eyes, wearing a
simple cream/off-white linen tunic with a pale terracotta border,
modest appearance (middle-class Roman), slender athletic build
```

### Step 2: Generate Reference Images

Generate a portrait/reference image for each main character using your image-generation tool of choice (`generate`, `create`, etc.):

```
Character reference sheet for [NAME]: [Full character description]

Show the character in a 3/4 view portrait pose, neutral expression,
against a simple warm-toned background. The style should be [your style].
No text, no labels.
```

Save these as `ref_[character].png`.

### Step 3: Generate Scene Images

For scenes with characters, use the reference images as inputs:

#### Single Character Scenes → Edit / Transform

Use an edit/transform flow with the character reference as the base image:

```
Transform this character reference into a full scene: [Scene description].
Keep the character's appearance exactly as shown - same clothing, same hair,
same facial features. [Lighting/atmosphere]. [Style notes]. No text, no labels.
```

#### Multiple Character Scenes → Multi-Reference Compose

Use a multi-reference compose flow with all relevant character references (requires 2+ images):

```
Scene from illustrated story. [Scene description].
Both characters must match their reference images exactly.
[Character 1] has [key features]. [Character 2] has [key features].
[Lighting/atmosphere]. [Style notes]. No text, no labels.
```

---

## Mode Reference

### Generate
- Use for: Landscapes, establishing shots, character references
- Input: Text prompt only
- Best for: Images without specific characters that need consistency

### Edit / Transform
- Use for: Single character scenes
- Input: One reference image + prompt
- The prompt should describe how to transform/place the character into a scene

### Multi-Reference Compose
- Use for: Multi-character scenes
- Input: 2+ reference images + prompt
- Requires minimum 2 images
- Good for dialogue scenes, group shots

### Style Transfer
- Use for: Applying consistent artistic style
- Input: Base image + style reference image
- Useful if you want all images to match a specific artistic style

## GPT Image 2 Calibration (April 2026)

- `gpt-image-2` is good enough to make graphic-novel planning more ambitious: readable caption boxes, cleaner comic lettering, reference-sheet style outputs, and targeted iterative repairs are all materially better than older image models.
- Those gains do **not** eliminate the core risks of sequential storytelling. Recurring-character drift, panel-layout drift, and over-dense science/exposition pages still need human discipline.
- Keep each science page to one main visual argument. If a page needs too many labels or too much narration, split it.
- Prototype the hardest pages first: scientific diagrams, multi-character argument scenes, and any page where text and composition must both be exact.
- Prefer a targeted full-image edit request once a page is mostly right. Do not crop a defect, regenerate it in isolation, and composite it back into a finished page; that method creates visible seams and often fails to preserve identity or lettering.

## Speech-Bubble Attribution Calibration (July 2026)

- OpenAI's official [GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) provides useful general rules for composition, literal text, indexed inputs, invariants, and controlled iteration, but no dedicated speech-balloon attribution recipe.
- Treat attribution as composition. Put speakers in dialogue order and keep each bubble on the same side as its speaker.
- For A-B-A in one panel, use two tiers: A upper-left, B upper-right, A lower-left. A numbered balloon map must name the speaker, verbatim line, position, and tail endpoint for every bubble.
- State exact balloon counts per speaker and identify silent characters explicitly.
- Keep mouths visible and leave a clear tail corridor without hands, props, animals, or bystanders.
- Even a repeated strong prompt can produce a tail that ends at a torso or an orphan tail fragment. Inspect every page; do not treat "tail ends at the mouth" as a guarantee.
- One visible speaker and one bubble per panel is the most robust fallback for difficult dialogue.
- If attribution fails, revise the blocking and regenerate the full page. Do not crop-patch tails or swap text between existing bubble shapes.
- Validate canvas dimensions after every generation. A test requesting 3:2 returned a 1774x887 strip when the three-panel structure dominated the prompt.

The controlled Earthsea tests, raw images, canonical prompt block, and QA checklist are in `earthsea-wizard-part1/05-SPEECH-ATTRIBUTION-STUDY.md`.

---

## Narrative/Dialogue-Driven Builder/Critic Calibration (August 2026)

The completed 55-page `monte-cristo-expanded/` run established a reliable
workflow for long, sequential, fully lettered **narrative and dialogue-driven**
graphic novels.

The workspace-wide playbook is [`dialogue.md`](dialogue.md). The exact Monte
Cristo orchestration record remains in
`monte-cristo-expanded/36-BUILDER-CRITIC-RUN-NOTES.md` as its evidence source.

This calibration is deliberately scoped. It does **not** alter the established
biographical graphic-novel workflow in `bio.md` or the `honda-soichiro/` model.
Biographical production keeps its existing research, reference, prototype,
density, QA, and iteration rules unchanged.

### Separate making from approving

- The **builder** writes the prompt, generates one candidate, and performs one
  practical essentials audit.
- The **critic** independently decides whether the page passes. The builder does
  not keep rerolling privately in pursuit of an imagined perfect page.
- While Page N is under review, the builder may prepare the Page N+1 prompt, but
  must not generate it until Page N is approved, promoted, and explicitly
  released.

### Use a reasonable essentials gate

The Monte Cristo critic was implemented as a separate agent. For each candidate,
the production lead sent it the image path, pointed it to the sibling page
prompt, builder audit, and desktop/tablet proofs, and used this repeated brief:

> Independently review Page NN under the corrected essentials gate: exact
> script/story, clear attribution, obvious generation/anatomy integrity,
> consequential identity/continuity, and actual desktop/tablet comfort.
> Typography/cosmetic/numeric prompt deviations are nonblocking unless they
> materially harm reading or story. Write a concise critic report and return
> APPROVED or REJECTED with mandatory findings only. Do not edit or promote.

The production lead then added a short page-specific checklist taken from that
page's script and prompt—for example, a required action sequence, memory/source
boundary, decisive object handoff, forbidden premature reveal, or closed-case
safety boundary. This was how visual faithfulness to the page prompt was put in
front of the critic in the actual run; the critic was not merely asked whether
the page looked good.

The repeated review areas were:

1. exact script, story facts, or causal/reading order;
2. the page-specific staging, action, object, source, and exclusion checks
   named in the critic task;
3. clear speech, sound, narration, and memory attribution;
4. obvious actor or anatomy integrity;
5. consequential character, setting, or object continuity;
6. comfortable reading at the actual desktop and tablet targets.

Nominal font pixels, tiny margin differences, exact panel percentages,
microscopic tail distances, phone-only legibility, and cosmetic polish are not
independent reasons to regenerate. They become blocking only when their
deviation causes a real failure in the six review areas above.

The reusable workflow lives in `dialogue.md`; the exact page-review task,
builder task, promotion boundary, and batch-gate task used in the source run
remain recorded in `monte-cristo-expanded/36-BUILDER-CRITIC-RUN-NOTES.md`.

### Correct narrowly, but redraw honestly

- When a real defect exists, preserve the rejected candidate and name the one
  defect being corrected.
- Regenerate the complete page. Do not patch, crop, swap lettering, or repair a
  tail in isolation.
- Do not use the correction as permission for unrelated refinement.

In Monte Cristo, redraws were reserved for concrete failures such as reversed
cause/response order, an answer appearing before an approaching-sound cue, and
a required story line being missing. Pages were not regenerated for typography
size or finish preferences.

### Advance from approved state only

- Use the latest approved canonical page as the immediate visual and narrative
  anchor, plus only the minimum character/object references needed for the new
  page.
- Never feed a rejected page back as an image reference.
- Promote the critic-approved candidate byte-for-byte and retain its prompt,
  builder audit, desktop/tablet proofs, critic report, hash, and any rejected
  evidence.

### Add sequence gates

Individual page approval cannot prove that a run works as a story. After each
ten-page batch—and after the final shorter batch—review the canonical pages
uninterrupted for:

- story and emotional continuity;
- identity, setting, and object continuity;
- cross-page attribution and reading order;
- generation/anatomy integrity;
- actual desktop/tablet comfort.

The Monte Cristo production authority and audit trail live in
`monte-cristo-expanded/29-PAGES-21-55-BUILDER-CRITIC-WORKFLOW.md` and the
numbered production QA ledgers that follow it.

---

## Tips for Best Results

1. **Be explicit about consistency**: In every prompt, remind the model to keep clothing, hair, and features "exactly as shown" in the reference.

2. **Repeat key details**: Even when using references, mention the most important details (e.g., "cream tunic with decorative border", "graying beard").

3. **Consistent style language**: Use the same style description across all prompts (for example, "serious painterly historical graphic novel, realistic proportions"). Do not let the model drift into a children's-book register unless that is actually the goal.

4. **Consistent lighting**: Define your lighting once (e.g., "warm dusk lighting") and use it throughout.

5. **Be explicit about text policy**: If a page should contain no text, say "no text, no labels." If it should contain text, keep the amount small and specify that the wording must be exact.

6. **Save your prompts**: Keep a `prompts.md` file documenting all prompts used for reproducibility.

---

## Example Project Structure

```
story-name/
├── index.html          # The story
├── prompts.md          # All image prompts documented
├── ref_character1.png  # Character reference
├── ref_character2.png  # Character reference
├── cover.png           # Cover image
├── image1.png          # Story illustrations
├── image2.png
└── ...
```

---

## Limitations

- Multi-reference compose requires minimum 2 images in workflows that distinguish it from single-image editing
- Characters may still vary slightly between images - the references help but aren't perfect
- Complex poses or unusual angles may not preserve character features as well
- Better text rendering does not mean unlimited text density - overloaded pages still fail

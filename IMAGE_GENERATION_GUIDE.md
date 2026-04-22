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
- Prefer targeted local edits once the page is mostly right. Full rerolls tend to lose solved continuity.

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

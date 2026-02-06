# Salt and Stone — Style Guide

## Style Block (COPY VERBATIM TO EVERY PROMPT)

```
Art Style: Cinematic painterly realism with restrained brush texture, historical graphic novel aesthetic
Color palette: Aegean blue, sun-bleached gold, burnt sienna, charcoal black, weathered stone gray
Effects: Natural Mediterranean light, atmospheric depth, salt-air haze, realistic weather
```

## Visual Rules

### Palette by Life

**Life One — The Boy** uses the full palette above with emphasis on:
- **Aegean blue** and **sun-bleached gold** for the island (warmth, home)
- **Charcoal black** and **burnt sienna** for the raid and shipwreck (violence, fire)
- **Weathered stone gray** and muted versions of the palette for Sidon (unfamiliarity, rebuilding)

### Atmosphere Notes

- Light should feel like actual Mediterranean light — bright, high-contrast, with deep shadows
- Sea scenes should have weight and movement — the sea is not decorative, it is a character
- Interior scenes (workshops, docks) should feel dim and warm by contrast
- Night scenes use deep blue-black with orange fire accents only
- Dust, salt, wood grain, rope fiber — texture matters. This world is tactile.

### Panel Style

- Black panel borders, consistent weight
- Gutters (space between panels) should be clean white
- No decorative borders or flourishes — the art carries the story
- Caption boxes: simple rectangular, muted parchment background, dark text
- Speech bubbles: classic white with black outline, tail pointing to speaker
- Thought bubbles: NOT USED in this story (narration is external)

### Typography Guidance

- Do not request specific fonts (the model won't follow them)
- Caption text should be "clean, readable, slightly serif"
- Speech bubble text should be "clean, bold, comic lettering"
- Sound effects should be "bold, large, integrated into the scene"

### What This Should NOT Look Like

- NOT anime or manga
- NOT cartoon or stylized
- NOT superhero comics (no spandex aesthetics, no exaggerated anatomy)
- NOT watercolor or impressionist
- **NOT children's book illustration** — the protagonist is young but the visual treatment is adult
- Think: the visual seriousness of a film like "Troy" or "Gladiator" translated into graphic novel form
- Reference touchstones: Eric Shanower's "Age of Bronze", Frank Miller's "300" (but with color and less stylization)

### CRITICAL: Anti-Drift Directive

AI image models tend to soften toward children's book aesthetics when the subject is a child. **Fight this actively.** If any generation comes back looking soft, rounded, cartoonish, or "cute," regenerate immediately.

Add this line to ANY prompt that produces kiddie-looking results:

```
STYLE REINFORCEMENT: This is NOT a children's book illustration. Render in a serious, mature graphic novel style with realistic proportions, natural lighting, and cinematic composition. The protagonist is young but the visual treatment is adult.
```

This is especially likely to happen on:
- Nikos's character reference sheet (a 9-year-old as subject)
- Pages 5 and 7 (Nikos alone, vulnerable moments — models default to softness)
- Page 8 (Nikos in a big city — models may default to "wide-eyed child in wonderland")

Watch for: oversized eyes, rounded features, bright saturated colors, soft focus, whimsical atmosphere. All of these are drift signals. Regenerate.

# Style Guide — The Name of the Rose, Book One

## Style Block (paste verbatim into every page prompt)

```
STYLE: Oil-painting realism. Cinematic single-image composition, 3:2 landscape. Muted period palette of cold stone grey, deep burgundy, candle-amber, snow white, ink black, vellum cream. Natural light sources only — candlelight, hearth, snow-light, oil lamp, the slate-grey daylight of a north-Italian winter. Painterly brushwork. Heavy chiaroscuro. The world is the Italian Apennines in late November 1327: cold, snowy, mountainous, austere.

NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition.

NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork, cinematic lighting, muted period palette.
```

These lines are mandatory in every page prompt. Without them the model drifts toward children's-book aesthetics or ink-comic register.

## Period accuracy

- **1327, north Italy, Benedictine abbey.** Habits:
  - Benedictine = **black** wool habit, dark cloth belt
  - Franciscan = undyed **brown** wool habit, knotted **rope belt** (three knots: poverty, chastity, obedience), often sandalled or barefoot
  - Dominican = **white** wool tunic + long white scapular + **black** wool mantle and hood over it
- **No modern artifacts.** No printed books (Gutenberg is 130 years away). No metal-frame eyeglasses — William's spectacles are *riveted leather-and-glass*, the brand-new technology they were in 1284. No paper as primary medium — books are on vellum (calfskin). No firearms. No clocks (the bell is the clock).
- **Architecture.** Romanesque only — round arches, thick walls, narrow slit windows, no Gothic pointed arches, no flying buttresses, no later Renaissance refinement. Heavy stone, small openings, smoke-stained walls inside.
- **Light.** Tallow and beeswax candles, oil lamps, hearth fires. Outdoor: thin grey winter sunlight, snow reflection, dusk by 4pm. Nights are very dark.
- **Snow.** It is late November on a mountainside. Snow on all exterior shots. Breath visible in the cold.

## Lettering treatment (the Honda formula, period-appropriate variant)

The narration lives **inside the image** as caption boxes, not in the reader-app HTML below the image. Period register:

- **Caption boxes:** *ivory parchment with serif ink, slightly worn at edges.* Repeat this phrase verbatim per caption in every prompt.
- **Speech bubbles:** off-white parchment-feel, dark serif text, tail explicitly described ("tail pointing to the figure on the LEFT", or to the named character).
- **Banners and signage in-scene:** monastery doorway carvings (Latin), library room labels (LEONES, AEGYPTUS, HIBERNIA), Bernard Gui's official seal — described as physical objects with their text quoted verbatim.
- **Full-width bands:** allowed on T5 hero pages. Top band sets the moment, bottom band closes it. 50–80 words each.
- **Verbatim block in every prompt:** open the lettering section with the line `LETTERING — verbatim, render exactly:` then list each text element with its position and exact quoted string.
- **Restrictions block:** close every prompt with the block below.

## Illuminated chapter-break style (P1, P9, P14, P19)

These four pages use the manuscript register *inside* the page, while still rendered by gpt-image-2 in the same oil-painting style:

```
A page styled as a 14th-century illuminated manuscript folio.

— Gold-leaf border running all four sides, with intertwined vines and oak leaves. Two small drolleries (medieval marginalia) at lower corners: a FOX-IN-MONK'S-HABIT — a sly red fox wearing a brown Franciscan cowl, preaching from a tiny vellum book to a small audience of hens. The same fox-in-monk's-habit drollery appears on ALL FOUR chapter-break pages (P1, P9, P14, P19) — consistent marginalia across the volume, the way a single manuscript would have its own scribe's recurring motif.

— Large historiated initial letter at top-left (the opening letter of the first Latin word below), gilt and lapis-blue, with a small narrative scene painted inside the bowl of the letter.

— Central painted miniature, framed by a thin gilt border, occupying the upper two-thirds of the page. The miniature is in muted oil-painting realism (NOT flat illumination — the inner scene matches the rest of the book's painted register, just contained in a frame).

— Below the miniature, CENTERED on the page: the Latin tag rendered verbatim in Gothic blackletter type, large enough to read. Immediately below the Latin, an off-white parchment caption box containing the English translation in dark serif (small, restrained — the Latin is the artifact, the English is the helper).

— Below the translation caption: a second slightly larger caption box with the old-Adso narrating-voice setup line for the day to come.

— The whole composition reads as one page from Adso's lost manuscript.
```

Each chapter-break page carries, in this stacked order from top to bottom:
1. Gold-leaf border + historiated initial + central miniature
2. Latin tag in Gothic blackletter, centered, large (the artifact)
3. English translation in small off-white caption box (the helper, never paraphrased)
4. Old-Adso narrating-voice setup line in a slightly larger caption box

The locked marginalia (fox-in-monk's-habit) ties the four chapter breaks together visually and quietly echoes Eco's themes of laughter, hypocrisy, and the forbidden book.

## In-image Latin always has an English helper (canonical rule)

Any Latin rendered as art inside an image — chapter-break tags, primary-source manuscript pages, in-scene signage, speech bubbles in Latin or pidgin Latin — **must carry an English helper visible in the same image**. The Latin is the artifact; the English is the helper; the reader (a first-time reader who does not read Latin) must never be locked out of the meaning of a line that the page itself is asking them to read.

Treatment depends on the type of Latin:

- **Single-line tag** (chapter-break daily tags like `Dies secundus…`): Latin in Gothic blackletter, English on the line below in a small ivory parchment caption box, dark serif. Already locked for P1, P9, P14, P19.
- **Latin speech bubble** (e.g. Salvatore's macaronic Latin–Italian): a smaller `[bracketed]` subtitle caption directly under the bubble in ivory parchment, smaller serif, with the English translation prefixed by a one-line note on what the speaker is saying. Already used on P15.
- **Latin column / paragraph on a primary-source page** (P11 cipher, P24 *Practica*): a narrower ivory parchment **helper column** placed adjacent to the Latin (typically just to its left, framed as a smaller pasted-in helper panel so the manuscript still reads as the artifact). Smaller serif. Line-for-line English alignment when the Latin is a numbered list (P24); a single short prose gloss when the Latin is a sentence or fragment (P11).
- **In-scene Latin signage** (LEONES, AEGYPTUS, HIBERNIA over doorways in the labyrinth): a tiny ivory ribbon below or beside the carved word with the English gloss in dark serif. Used sparingly — one or two words per scene only.

**The rule does not apply** to ornamental Latin that is intentionally illegible at page scale (the body of a painted miniature book, distant signage in the background of a wide shot, the engraved Latin on the abbey gate barely visible in P3). If the reader can read it, it must have a helper. If they cannot, it is decoration and needs no helper.

When in doubt, add the helper. Latin without translation breaks the first-time-reader audience rule documented in `00-PROJECT-BRIEF.md`.

## Hybrid layouts (P5, P13 INTERLUDE, P15, P22)

User has opened the door to half-page-painting / half-page-text compositions for teaching pages. Template:

```
3:2 landscape page divided vertically by a clean painted edge (no border, no comic-style gutter).

ONE HALF: a painted scene in oil-painting realism (specify LEFT or RIGHT per page).

OTHER HALF: a parchment-textured panel containing 120–140 words of caption text in dark serif ink, with a small medieval-style decorated initial (gilt + lapis) at the start of the first word. The panel reads as a torn-out manuscript page glued into the picture.
```

This format is used three times in Vol 1, varying which half is image and which is text. Vary the side to keep the visual rhythm.

## Restrictions block (close every prompt verbatim)

```
All words spelled correctly. Latin spelled verbatim as supplied above. Do not duplicate text. Do not invent extra captions or signage. NO modern logos, NO watermarks, NO modern wire-frame eyeglasses (only the riveted leather-and-glass spectacles of 1327), NO printed books (vellum codices and scrolls only), NO Gothic architecture (Romanesque only — round arches), NO Renaissance clothing, NO modern faces (period-realistic features only). Single image composition unless layout explicitly states hybrid or chapter-break.
```

## Prompt structure — the canonical six-block order

This scaffold implements the six-block order from `~/.claude/skills/graphic-novel/SKILL.md` (gpt-image-2 prompt structure section). Do **not** reorder the blocks. The model anchors on early tokens — the Style + register + anti-drift lines must arrive before any subject content can pull the aesthetic toward digital-painting or children's-book registers, and the lettering block must come last so text strings don't bleed into character description.

The Style Block above already bundles blocks 1–3 (style, register, anti-drift) into one paste.

## Character lock locks the visual, not the name

When pasting a character lock from `02-CHARACTERS.md`, the visual description does the work. Do **not** lean on a famous name in the prompt to carry the lock. This rule applies most sharply to **Bernard Gui** — he is the only real historical figure in the cast, and gpt-image-2 will drift toward stock-photo Wikipedia portraits if his name is in the prompt. Keep "Bernard Gui" in the narration (script) and the ref filename (`refs/ref_gui.png`); keep his face purely visual in the prompt block. William of Baskerville, Adso, the Abbot, Jorge, Salvatore, and the village girl are all fictional and not face-recognized by the model, so the same risk doesn't apply — but the discipline of *the visual description is the lock* still holds.

## Per-page template (paste this scaffold and fill in)

```
[STYLE BLOCK — verbatim, includes register + anti-drift lines]

CHARACTER LOCKS (for those appearing, age-appropriate version):
[Lock block(s) verbatim from 02-CHARACTERS.md — visual description only, no famous-name reliance]

SETTING:
[Setting block verbatim from 03-SETTINGS.md]

COMPOSITION:
[Camera, layout, what happens in the frame — 2-4 sentences.]

LETTERING — verbatim, render exactly:
- Top caption band (full width): "..."
- Speech bubble, tail pointing to [character on the LEFT / RIGHT]: "..."
- Bottom caption band: "..."
[etc.]

[RESTRICTIONS BLOCK — verbatim]
```

Every page prompt follows this scaffold. The script in `04-SCRIPT.md` provides the composition + lettering content. The style guide provides the rest.

## Pre-flight before every `edit_image` call

Before launching any page generation that attaches a ref:
1. **Glob `refs/` and confirm the exact filename exists** at the path you're about to pass. The MCP does not fail loudly on missing refs — it silently substitutes a plausible image, and the resulting page is unsalvageable as "locked." If a ref was supposed to be built earlier in the session but slipped, verify before generating.
2. **Confirm age phase if applicable.** Wrong-age refs cause silent drift across the volume. (Not heavily relevant here — Name of the Rose is one week, no phase-spanning subject — but build the habit.)
3. **For multi-character pages** (P-Brunellus deduction, the abbot-meeting, the labyrinth, the Salvatore Adso encounter, the interrogation, the chapter-house trial), lock to the *harder secondary face* via `edit_image`, describe the protagonist in prose. See the skill's *Multi-character pages* section. For this volume, William (wire-rim spectacles + tall sharp Englishness) is usually easier to describe in prose than Salvatore (mashed-up Babel face) or Gui (real-historical-figure risk) — so lock those when paired with William.

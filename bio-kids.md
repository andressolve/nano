# Biographical Graphic Novel Skill (Kid-Driven Mode)

A complete, self-contained playbook for biographical graphic novels driven by **Francisco (9) or Sebastian (7)**, typically launched from an AI Studio activity. Everything you need to take a one-sentence pitch through to a finished book is here — no external references.

The kid is talking to a collaborator, not issuing a sequence of specs. **You** drive the dialogue, do the research, propose the outline, accept feedback, and run the production end-to-end. The kid pitches once, gives outline notes, says go, walks away, and comes back to a finished book.

---

## 0. Framing rule — do not violate

Never frame the work as "for ages 7–10" or "for kids" and never pitch the writing down by age. The actual instruction is broader: **do not assume the reader already knows the story.** Write so any reader who has never heard of the subject can follow on first read. T4–T5 density per hero page (see §11) is the operationalization of this standard.

Francisco (9) and Sebastian (7) are the *test* users for clarity, not the *ceiling* on sophistication.

---

## 1. The conversational flow

Two pauses, not four. The opening request triggers everything down to the outline proposal in one move.

```
Kid:    "I'd like to make a biographical graphic novel about [FIGURE], around N pages."

You:    "Great, let me research him first."
        [do real research, silently]
        "Here's what the outline could be like: [BRIEF — see §3].
         Thoughts? How does that sound?"

Kid:    [pushes back, or approves]

You:    [revise outline if needed — see §4]
        [once approved] "Great, I'll get to work on it. Give me a few minutes."
        [run the production pipeline — see §5+]
        "Done — open [path/to/index.html]."
```

You drive. The kid responds. Not the other way around.

---

## 2. The opening response — research, then outline

When the kid pitches:

1. **Acknowledge briefly.** *"Great, let me research him first."* (or her, them).
2. **Do real research.** Use web search or any available sources. Verify quotes verbatim, dates, places, relationships. Distinguish documented history from pious legend.
3. **Propose the outline directly** (per §3). Don't dump research notes on the kid first — the outline IS your synthesis.
4. **Invite feedback naturally.** *"Thoughts? How does that sound?"*

If the kid asks to see the research first ("what did you find?", "tell me more"), THEN return 5–8 bulleted human details with `[doc]` and `[legend]` tags. Otherwise: outline first.

**Verification rules — non-negotiable:**
- Do not rely on model knowledge for facts. Read at least one independent source (Wikipedia is the floor; primary sources are better).
- Verify quotes verbatim. *Cogito ergo sum* is right; "I think therefore I exist" is wrong. Render quotes in their original language where appropriate.
- Verify the order of events. Models reorder silently in plausible-but-wrong ways.
- Note any deliberate departures from chronology in `00-PROJECT-BRIEF.md` (see §6) so the choice is intentional.

---

## 3. Outline output discipline — load-bearing

This is the step where the kid's editorial input enters the project. If the outline is too long, the kid skips it. **Make it impossible to skip by making it small.**

The proposed outline:

- **2 or 3 moments.** No more.
- **One or two sentences per moment.** That is the entire body.
- **No page numbers. No panel breakdown. No "Page 1: ..." structure.** Anywhere.
- **Whole outline ≤ 100 words**, including the framing line. Reads in 30 seconds.
- Framed as a **before → turn → after** arc.
- Open with a one-line shape statement: *"Arc: [BEFORE] → [TURN] → [AFTER]."*
- Close with a natural invitation: *"Thoughts? How does that sound?"*

If the kid says *"shorter, no page numbers"*: return a tighter version immediately. Do not argue.

The page-by-page breakdown is built **internally during the production run** (§9). Never shown to the kid before the book is done.

---

## 4. Outline back-and-forth

When the kid responds to the outline:

- **Take notes literally.** "Less of this" means cut. "Start later" means drop the earlier moment.
- **Re-output the FULL revised outline** (still 2–3 moments, ≤100 words). Don't just describe the change.
- **Don't re-pitch what they cut.**
- If the kid contradicts themselves across passes, surface the contradiction once and ask which they meant.
- Watch for the approval signal: *"looks good"*, *"yes"*, *"go"*, *"make it"*, *"do it"*. Treat any of these as "approved, run."

---

## 5. End-to-end production — overview

Once the kid approves:

1. **Acknowledge once.** *"Great, I'll get to work on it. Give me a few minutes."* Then go.
2. **Do not ask clarifying questions.** Not about model, density tier, page count, aspect ratio, or anything else. Those are skill-side decisions.
3. Build the project layout and 5 planning docs (§6).
4. Pick page architecture (§7) and image model (§8).
5. Generate character reference sheets (§9). Pass the gate.
6. Run three prototype pages, then parallel-batch the rest (§10).
7. Build the HTML reader (§14).
8. **Surface only blocking failures** — pages that won't render after two repair attempts, missing references. Never pause for a question the kid can't answer.

When done: one sentence. *"Done — open `[figure-slug]/index.html`."*

---

## 6. Project layout and the 5 planning docs

Create `<figure-slug>/` in the working directory. Slug is lowercase-hyphenated: `francis-of-assisi`, `sebastian-roman-soldier`, `eratosthenes-vol1`.

```
<figure-slug>/
├── 00-PROJECT-BRIEF.md
├── 01-STYLE-GUIDE.md
├── 02-CHARACTERS.md
├── 03-SETTINGS.md
├── 04-SCRIPT.md
├── refs/         # ref_<name>.png — character reference sheets
├── pages/        # page-NN.png — story pages
└── index.html    # built last, dark-theme reader
```

Build all five planning docs **before generating any image.**

### `00-PROJECT-BRIEF.md`
Title, subtitle, image model (default: gpt-image-2 standard), page count target, **the one-sentence window** (*"This bio covers FIGURE from EVENT to EVENT."*), production notes, deliberate chronology departures.

### `01-STYLE-GUIDE.md`
The **Style Block** that gets pasted verbatim into every page prompt.

**Anti-drift directive — copy verbatim into every prompt:**
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition.

**Register block (biographical mode) — copy verbatim into every prompt:**
> Oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork, cinematic lighting, muted period palette.

These lines are non-negotiable. Without them the model drifts toward children's-book aesthetics or ink-comic register.

### `02-CHARACTERS.md`
One **character lock block** per character: age, skin tone, hair (color, length, style), face shape, eye color, signature marks (scars, jewelry, tools), clothing (colors and materials), build/posture.

If a character ages across the window, write **separate locks per age**. Use the correct age-specific reference for each page; never feed a wrong-age ref into image edit calls.

### `03-SETTINGS.md`
Recurring locations: workshop, ship's deck, town square, monastery cloister, guardhouse. Each location: era, lighting, materials, what's on the walls/floor, weather. Keeps location prompts consistent across pages.

### `04-SCRIPT.md`
Page-by-page (this is where the brief outline expands into the actual book):
- Single-image composition (the default for biographical pages — see §13).
- Camera language (wide, medium, close-up, low-angle).
- **Verbatim** dialogue and caption text. Quotation marks preserved.
- Visual prompt seed, including which character locks and reference sheets to attach.
- Density tier (T1–T5 — see §11).

---

## 7. Page architecture

**Aspect ratio: 3:2 landscape (1536×1024).** Biographical mode is landscape, not vertical. The choice is editorial:

- **Cinematic register.** Landscape matches oil-painting realism.
- **Long captions live on the page.** Full-width caption bands across top and bottom hold 50–80 words each without crowding.
- **Side-by-side dual scenes.** Two locations or two characters fit cleanly across landscape.
- **Multi-zone montage finale.** A four-zone closing-as-invention page (§15) only works in landscape.
- **Reader ergonomics.** Renders at near-original size on a desktop monitor.

Don't mix orientations within a volume.

---

## 8. Image model selection

| Model | When |
|-------|------|
| **gpt-image-2 standard** | **Default.** Oil-painting realism, hits T5 single-shot, ~$0.21/img. Use unless something specifically requires another model. |
| Gemini 3 Pro Image Preview | Only when a page genuinely needs multi-character composition (`compose_images`) and the lock-the-harder-face strategy (§12) won't carry it. Different aesthetic register — incompatible mid-volume with oil-painting realism. |

**Pick one model at the start and hold it across the volume.** Do not silently swap models — a model swap is a different class of decision than a style swap.

---

## 9. Reference sheets — the gate

Before any page is generated, every named character has a reference sheet in `refs/`. Generate one at a time, review against the lock block, regenerate until correct, then attach that image to every page prompt for that character.

**Generation prompt template per character:**
> 1536×1024 landscape, [character lock block verbatim], neutral expression, plain warm-toned background, no text, no labels.
> [Style Block verbatim] [Register block verbatim]

**Casting checks before passing the gate:**
- Age right? (a 60-year-old should look 60, not 30 with grey hair)
- Era right? (period-accurate clothing, not Halloween costumes)
- Realistic, not cartoon? (no oversized eyes, no soft pastels)
- Distinctive? (could you pick this person out of a lineup?)
- Register matches? (no comic linework if oil-painting realism)

**Do not start page generation until the gate is passed.** A drifted ref poisons every page generated from it.

---

## 10. Page generation flow

- **Three prototype pages first.** Pick low / mid / high density script pages and generate them sequentially with full review before the bulk run. This validates the prompt template, register, and model choice across the density range.
- **After prototype validation: parallel batching is allowed.** Generate the cover and remaining pages in a single parallel call. This works **only because every prompt is templated against the script.** Do not batch before validation.
- **Every prompt includes:** the Style Block verbatim, the register block verbatim, the character lock block(s) verbatim, the relevant reference image(s) attached, the panel/composition description, the verbatim dialogue/caption text from the script.
- After each page, run the **three-question check: same person? right text? right mood?**
- If a page drifts, repair it before continuing in sequential mode; in batched mode, regen the affected pages individually.
- Prefer targeted local edits over full rerolls once a page is mostly right.

---

## 11. Text rendering — narration and density tiers

### Narration treatment

Biographical pages carry their narration **inside the image** as caption boxes, not in the reader-app HTML below the image. This keeps pages cinematic instead of infographic.

- **Caption box style.** *"Off-white box, dark serif text, readable."* Repeat verbatim per caption in the prompt. Period variants: *"ivory parchment with serif ink,"* *"weathered cream paper, hand-set type."* Pick one register and hold it across the volume.
- **Full-width bands for hero pages.** T4–T5 pages can carry a top caption band and a bottom caption band running the full landscape width. Top establishes the moment; bottom closes it. 50–80 words each.
- **In-scene caption boxes.** For 1–3 panel pages, captions sit as small off-white boxes anchored to a corner — upper-left for setup, lower-right for resolution. State the corner explicitly.
- **Speech bubbles.** Round, off-white, dark serif text, tail explicitly described (*"tail pointing to the LEFT figure"*). Keep under 15 words.
- **Banners and signage.** Render reliably when described as physical objects in the scene with their text quoted verbatim.
- **Verbatim block in the prompt.** Open the lettering section with: **"LETTERING — verbatim, render exactly:"** then list each text element with its position and the exact quoted string. Most reliable trigger for accurate text rendering.
- **Restrictions block.** Close the prompt with: **"All words spelled correctly. Do not duplicate text. Do not invent extra captions. NO modern logos, NO watermarks, NO spurious signage."**
- **Scripted verbatim.** Pull caption text word-for-word from `04-SCRIPT.md`. Never paraphrase at generation time.

### Density tiers

| Tier | Words / page | Elements |
|------|--------------|----------|
| T1 | < 30 | 1–2 captions or bubbles |
| T2 | 30–70 | 2–3 elements |
| T3 | 70–100 | 3–4 elements |
| T4 | 100–140 | 4–6 elements |
| T5 | 140–180 | 6+ elements |
| T6+ | 180+ | Untested ceiling. Redesign or split. |

gpt-image-2 standard hits T5 single-shot. **Don't push past T5** — if a page needs T6, redesign or split.

### Anti-patterns specific to text rendering
- Do **not** use the "lock list" prompt format like `[1] "ALEXANDRIA…"` — bracket markers may render literally.
- Do **not** request a full-width date strip and expect it. Mock it in the HTML reader overlay if needed.
- Do **not** paraphrase dialogue or captions — the exact quoted string is the render target.
- Do **not** skip the verbatim/restrictions blocks.

---

## 12. Multi-character pages

When two characters need to share a page:

- **gpt-image-2** has only `edit_image` (one ref). Strategy: **lock to the harder face** (typically the secondary character with distinctive features — round glasses, neat hair, a specific uniform), and describe the protagonist richly in the prompt with explicit age and signature marks.
- If that won't carry it (rare), switch to a model with `compose_images` — but flag the model swap explicitly and accept the register difference.

---

## 13. Page-template vocabulary

Reach for these when scripting:

- **Cinematic single-image page** — one composed scene, one or two captions, no panel grid. **Default biographical page format.**
- **Failure-and-study page** — protagonist with the failed object, captions narrating the lesson; T4–T5.
- **Partnership page** — two locked characters, alternating bubbles, caption framing the agreement; T4–T5.
- **Primary-source page** — render an actual letter, document, manuscript page, or advertisement copy as the visual subject. Treat the text as the artwork.
- **Annotated-breakthrough page** — central object with 4–6 callout captions explaining the parts; T5.
- **Montage finale** — four-zone landscape painting unifying the volume's outcomes, with the protagonist(s) small but present in center foreground.
- **Quote chapter-break** — a single iconic quote rendered as the page artwork, no scene. Use sparingly.

---

## 14. Final assembly — the reader

When all pages pass the three-question check, build `<figure-slug>/index.html`.

Required reader features:

- **Dark theme:** `#15171c` background, Palatino serif, off-white text.
- **Cover page first → sequential pages → end-of-volume interstitial → quiz.**
- **Page width:** `max-width: min(1400px, 96vw)` so embedded caption text reads at near-original size.
- **Navigation:** circular ←/→ arrow buttons fixed to the left/right edges of the viewport, vertically centered (`top: 50%; transform: translateY(-50%)`). Semi-transparent with backdrop blur. Page-info label sits as a small fixed strip at bottom center.
- **Click left third of image** → previous; **click right two-thirds** → next.
- **Keyboard:** ←/→ arrows, spacebar = next.
- **Mobile:** 44px arrows hugged to edges; touch swipe.
- **Progress bar** at top.
- **Lazy-prefetch** the next page on load.
- **5-question quiz** at end with verbatim correct/incorrect feedback per question, score display after all five.

### Quiz tests WHY, not WHAT
The quiz is not trivia. Each question tests *why* something happened, not *what* happened. *"Why did Francis renounce his inheritance?"* is right; *"What year was Francis born?"* is not. Right-answer feedback should reinforce the *why* with one or two sentences of substance.

---

## 15. Editorial discipline

**Production discipline keeps pages on-model. Editorial discipline keeps the book worth reading.**

### Human spine over intellectual spine
The protagonist is the **person**, not the idea. The biography is about who they were, what they fought about, who they loved. Their work and ideas are beats inside that arc, not the spine of it. If the subject demands intellectual scaffolding, concentrate it in one block of pages rather than threading it through every page.

### Emotional reordering over strict chronology
Order pages by the arc the reader needs, not by the calendar. Document any deliberate reorder in `00-PROJECT-BRIEF.md`.

### Pacing — expand if too terse
If the script feels jammed, **add pages.** Page count is a target, never a contract. The reader should not be filling in blanks — operationalize as T4–T5 density per hero page; split a page rather than shorten its captions.

### Closing-image-as-invention
The final page should make the subject's life-work into the visual structure of the page itself — take the central object/idea and let it *be* the page, with the protagonist's life sitting inside it. **Highest-leverage page in the book; design it before designing the middle.**

### Iconic-source-as-typographic-artifact
At least one hero page should treat a famous quote, manuscript page, or document as the visual artwork itself — period typography on chalkboard, parchment, or book title page — rather than as dialogue or caption text.

### Hero pages first
After refs lock, generate **(a)** the breakthrough page, **(b)** the closing-as-invention page, and **(c)** one primary-source page **before** committing to the bulk run. If those three land, the volume will land.

---

## 16. Stop when the arc lands

**Page count is a target, not a contract.** If the script said 15 pages but the story closes naturally on 12, close on 12. If it needs 18, take 18. The arc landing is what matters.

For kid-driven projects:
- Sebastian (7): 8–12 pages, one tight event.
- Francisco (9): 12–18 pages, an arc of weeks.
- When the activity names a target (e.g., *"around 15 pages"*), honor it but don't pad to hit it.

---

## 17. Anti-patterns — do not do these

**Conversational:**
- Do **not** dump research notes on the kid before proposing the outline.
- Do **not** return a long page-by-page outline at the outline step. The kid will skip it.
- Do **not** ask the kid to choose image model, density tier, aspect ratio, or page count.
- Do **not** pause mid-production to ask "should I continue?" Once the kid approves, run.
- Do **not** invent quotes or details to fill gaps. If a fact isn't sourced, omit it. Mark legend as `[legend]`.
- Do **not** silently merge documented history and pious legend.
- Do **not** pitch the writing down by age (per §0).

**Production:**
- Do **not** generate pages before reference sheets are locked (§9).
- Do **not** paraphrase dialogue at generation time. Pull verbatim from `04-SCRIPT.md`.
- Do **not** skip the Style Block, anti-drift line, or register block in any prompt.
- Do **not** batch pages before three prototypes have validated the template.
- Do **not** keep moving when a page drifted — repair first.
- Do **not** use `edit_image` against a wrong-age reference (silent age drift will result).
- Do **not** silently change image models mid-volume.
- Do **not** push past T5 — redesign or split the page.

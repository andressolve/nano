# Ratio: The Seeker — Project Brief (Vol 1 of 2)

## Series
**Ratio: The Life of Pythagoras** — two-volume biographical graphic novel. This is **Volume 1: The Seeker**. Volume 2 is **The Brotherhood** (separate folder, produced after Vol 1 ships and passes kid-QA).

This is a from-scratch second attempt. An earlier 2-volume version (`pythagoras-vol1/` "Ratio: The Seeker", `pythagoras-vol2/` planning-only) was produced on the old Gemini NB2 pipeline and is preserved untouched as a historical artifact. This volume is rebuilt on the gpt-image-2 oil-painting pipeline (Newton / Honda / da Vinci / Name of the Rose register).

## Format
Biographical graphic novel, biographical mode. 3:2 landscape pages (1536×1024), gpt-image-2 standard, oil-painting realism. Dark-themed HTML reader. ~18 pages (1 cover + 17 story). 5-question WHY-quiz at the end.

## Audience
Francisco (9) and Sebastian (7) are the test readers — NOT a ceiling on sophistication. The standing project rule: **do not assume the reader already knows the story.** Write so any first-time reader can follow on first read. Clear, not dumbed down.

Why Pythagoras hits hard for these readers: the Pythagorean Theorem is a dedicated Lyceum lesson, and a²+b²=c² is the most DRAWABLE theorem in math — the kid can re-enact it on paper. **This volume plants the seed (the 3-4-5 rope that makes a perfect right angle); Volume 2 delivers the theorem and its proof.**

## The emotional arc of Volume 1
A boy hears the world speaking in numbers. He leaves home to find out how deep that goes. He spends years in foreign lands gathering pieces of an answer no teacher can complete — the Egyptians can *make* a perfect right angle with a knotted rope but cannot say *why* it works; the Babylonians have charted numbers into the sky but cannot say why either. He comes home to an island that cannot hold him. He leaves again, west, carrying an unanswered question to a strange city where he will finally build the place to answer it.

**The one emotional beat:** *seeking.* The satisfaction is the arrival — finding the ground where the work can begin. The reader does not yet learn the answer. They feel only that a long journey has found its landing.

## The one central idea (Vol 1)
**"The world is made of ratios — and the question is how deep the pattern goes."** The volume is this hypothesis tested against three civilizations. Everyone the boy meets *uses* the pattern; no one can *explain* it. The unanswered "why?" is the engine that carries him to Croton — and into Volume 2.

## Honesty policy (load-bearing — see 00-RESEARCH.md)
Almost the entire ancient biography of Pythagoras is late legend. We do NOT pretend otherwise, and we turn that into the book's strength:
- The **forge / harmony-of-hammers** story is legend (and physically false). In Vol 1 it is the boyhood *spark* — captioned as the famous tale, not as fact. The real string-ratio experiment is a Vol 2 payoff.
- The **Egyptian 3-4-5 rope** is staged vividly but captioned honestly: the surveyors' knotted-cord technique is real and ancient; whether they used *exactly* 3-4-5 is a tradition/conjecture, not a documented fact. The book's claim is "they could make the corner but could not say why," which is both honest and the perfect hook.
- The **Babylon captivity** is legend; the **Babylonian triples (Plimpton 322)** are real and predate Pythagoras by ~1,200 years. We use this to make the honest point: the pattern was loose in the world before him. His role is synthesizer and seeker, not lone discoverer.
- **No invented quotations attributed to Pythagoras.** He wrote nothing and no contemporary quotes him. Dialogue we give him is clearly in-scene narrative voice, never framed as a historical quote. Real quotation marks + Greek are reserved for attested testimonia (Xenophanes' puppy line; Heraclitus' *polymathíē*).

A light frame-opener establishes that this is a life reconstructed from fragments — consistent with the clarity standard, and it makes the myth-vs-reality beats legible instead of confusing.

## Volume 1 structure (3 movements)
- **Movement A — Samos (boyhood → departure, P1–P4):** the gem-cutter's son who hears the world in numbers; the forge; Pherecydes; Polycrates' Samos; the question outgrows the island.
- **Movement B — Foreign Lands (P5–P11):** crossing to Egypt; the temples; **the rope-stretchers and the 3-4-5 right angle (hero page)**; the unanswerable "why"; Egypt falls to Persia; Babylon and the number-sky; the realization that the pattern is everywhere and unexplained.
- **Movement C — Return & Re-departure (P12–P17):** return to a changed Samos; the too-small school; the decision to leave again; the crossing to Italy; first sight of Croton; the step to the assembly and the first word. Ends on the threshold of Vol 2.

## Volume 1 does NOT include
The Brotherhood; the Pythagorean Theorem and its proof; the monochord/music-of-the-spheres teaching; Theano, Hippasus, Cylon; √2 and the irrationality crisis; the fire and the bean-field death. All of these are Vol 2.

## What Vol 1 plants that Vol 2 pays off
- The forge hammers → the monochord and whole-number harmony (Vol 2).
- The Egyptian 3-4-5 rope → the theorem's general proof (Vol 2).
- The "why?" no teacher could answer → the beach moment where he answers his own decades-old question (Vol 2).
- The Babylonian number-sky → the tetraktys and the Brotherhood's number-reverence (Vol 2).
- The cave/school too small → the Brotherhood hall (Vol 2).

## Deliberate departures from chronology
None major. Events are kept in life-event order. The only compression: the years abroad (Egypt → Babylon → return) are telescoped; captions mark passing time rather than dating each beat, since the dates themselves are reconstructed (see 00-RESEARCH.md). Egypt-then-Babylon order follows the standard tradition (Persian conquest of Egypt as the hinge).

## Title and subtitle
- **Series title:** *RATIO* (the prominent word on the cover).
- **Volume 1 subtitle:** *The Seeker.*
- Cover displays **RATIO · The Seeker**; the "Volume 1 of 2" indication lives on the landing card, not the cover.

## Image model
gpt-image-2 standard via `mcp__openai-image-2__{generate_image,edit_image}`, 1536×1024, quality `high`. NOT fal.ai (that is the video pipeline). Oil-painting realism register. Cost envelope ~$7.50 (≈6 refs + ~18 pages + a few prototype regens).

## Generation order
1. Write all 5 planning docs (+ this brief + research). 
2. Generate the ~6 character reference sheets (3 Pythagoras age-phases + Pherecydes + Egyptian priest/rope-stretcher + Babylonian Magus). Review each against its lock; regenerate until correct. **This is the gate.**
3. Generate 3 prototype pages spanning density AND format vocabulary (forge T4, the 3-4-5 rope annotated-breakthrough T5, the Croton-arrival cinematic T3). **Re-Read each generated PNG and confirm character lock before any bulk run.**
4. Bulk-batch the remaining pages against locked refs + validated template.
5. Build reader + 5-question quiz + landing card.
6. STOP for the kid-QA pass before producing Vol 2.

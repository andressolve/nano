# The Name of the Rose — Book One: The Abbey

## One-sentence window

This volume covers **Days One through Four** of Umberto Eco's seven-day story: the arrival of the Franciscan friar **William of Baskerville** and his Benedictine novice **Adso of Melk** at a wealthy mountain abbey in late November **1327**, the deaths of three monks, the slow revelation that the killings trace to a forbidden book hidden in the abbey's labyrinth library, and the arrival of the papal inquisitor **Bernard Gui**. Book Two will cover Days Five through Seven plus the epilogue.

## Source

Umberto Eco, *Il nome della rosa* (1980). Adaptation is **faithful to Eco**, not to the 1986 Annaud film. We restore the theology, the Avignon backstory, and the political weight of the Inquisition. We preserve Adso's grief over the village girl in Vol 2 and William's *"there is no order in the universe"* speech for Vol 2's closing.

Full research dossier: [`00-RESEARCH-DOSSIER.md`](./00-RESEARCH-DOSSIER.md) — read first if landing fresh.

## Audience

Francisco (9) and Sebastian (7). Standing project rule: **do not assume the reader already knows the story.** Write so any first-time reader can follow on first read — no info-withholding, no jigsaw reading. The kids are the test of clarity, not the ceiling of sophistication. "Clear, not dumbed down" is the operating standard.

## The goal under the goal

Give the reader a window into a worldview where **knowledge was scarce, carefully preserved, and carefully controlled**. Not "dark ages" condescension. The framing is *constrained intelligence*: people in 1327 were trained in three languages and the entire surviving corpus of philosophy, they built the most sophisticated information systems in 14th-century Europe, *and* a single fire could erase Aristotle. That tension is the story.

Load-bearing sentence (William's voice; lands explicitly at the end of Vol 2, seeded in Vol 1):
> "The monks here are not stupid, Adso. They know more than most kings. They have built the largest library in Christendom. And one fire could end it. That is the world."

## Volume count and shape

Two-volume series.
- **Book One: The Abbey** (this volume) — Days 1–4.
- **Book Two: The Fire** — Days 5–7 + epilogue.

## Page count

Cover + 24 story pages = **25 total**.

Day allocation:
- **Frame opener:** 1 page (P1)
- **Day 1:** 7 pages (P2–P8)
- **Day 2:** 5 pages (P9 chapter break + P10–P12 + P13 INTERLUDE hybrid teaching page)
- **Day 3:** 5 pages (P14 chapter break + P15–P18)
- **Day 4:** 6 pages (P19 chapter break + P20–P24)

**Note on P13 INTERLUDE (added late in planning):** a dedicated hybrid teaching page covering (a) what a heretic was and what the Inquisition did, and (b) why the Pope was in Avignon and the Emperor in Munich and why their envoys were meeting in this abbey. Added because audit found the words *heretic* and *Inquisition* — the whole engine of the plot — were used four times across the book but never explicitly defined for a first-time reader. Diagrammatic painted map of Latin Christendom 1327 on the left, ~165-word concept caption on the right. Sits between the first labyrinth attempt (P12) and the Day 3 chapter break (P14).

## Image model

**gpt-image-2 standard** via `mcp__openai-image-2__{generate_image,edit_image}`. **NOT Google Gemini** — user explicitly reconfirmed at handoff: Gemini struggles with the dense Latin / manuscript text rendering this volume requires (T5 captions, blackletter Latin tags on every chapter break, primary-source pages P11 and P24, the ~165-word INTERLUDE on P13). gpt-image-2 hits T5 single-shot per the Newton / Honda / da Vinci playbook. Do NOT swap to Gemini mid-production even if a page fails; repair on gpt-image-2 instead and flag any model-swap proposal explicitly to the user.

## Aspect ratio

**3:2 landscape (1536×1024).** Biographical-mode default.

## Stylistic decisions locked

1. **Oil-painting realism** register. Muted period palette: cold stone grey, deep burgundy, candle-amber, snow white, ink black, vellum cream. Painterly brushwork. Heavy chiaroscuro. Natural light sources only — candle, hearth, oil lamp, slate winter daylight.
2. **Illuminated-manuscript chapter breaks** for the frame opener (P1) and each new Day (P9, P14, P19). Gold-leaf border, marginalia (drolleries — fox-in-monk's-habit, hare-with-lute), large historiated initial with a small scene painted inside, central painted miniature in the same oil-painting realism as the rest of the book, a Latin tag in Gothic blackletter with English translation in caption-box style underneath. Four such pages out of 25.
3. **Hybrid layouts allowed** on teaching pages (user has explicitly opened this door). Used four times in Vol 1:
   - **P5 scriptorium** — left half painted scene + right half parchment-textured caption-box panel teaching how a medieval book was made (~140 words).
   - **P13 INTERLUDE** — left half diagrammatic painted map of Latin Christendom 1327 (Pope at Avignon / Emperor at Munich / Aedificium in the Italian Apennines) + right half parchment panel defining *heretic*, *Inquisition*, and *Avignon* (~165 words). The riskiest hybrid because of the novel diagrammatic-map style.
   - **P15 Salvatore + Dolcinians** — same split, teaching the Fra Dolcino backstory by example.
   - **P22 three orders** — same split, teaching the difference between Benedictines, Franciscans, Dominicans.
4. **Primary-source-as-artifact** beats:
   - **P11** — Venantius's coded Greek cipher rendered as the visible artifact, with William's margin notes.
   - **P24** (cliffhanger / closing-as-invention for Vol 1) — a page from Bernard Gui's actual *Practica Inquisitionis* rendered as the visual frame, with a small inset scene of Gui pointing at his first chosen monk.

## Character roster — Vol 1

**Locked refs (7):** William of Baskerville, Adso of Melk, Abbot Abo, Jorge of Burgos, Salvatore, Bernard Gui, the village girl.

**Description-only** (carried by prose in each page prompt; appear in group scenes anchored by a locked ref):
Malachi, Berengar, Severinus, Remigio.

Plus 1 architectural ref: the **Aedificium** (great tower, dominates exteriors).

See [`02-CHARACTERS.md`](./02-CHARACTERS.md).

## Settings locked

Abbey approach (snow, mountain road); the great Aedificium tower; abbey courtyard; scriptorium; labyrinth library interior; herbarium / infirmary; great kitchen at night; cloister at midday; chapter house.

See [`03-SETTINGS.md`](./03-SETTINGS.md).

## Production sequence

1. Generate **8 refs** (7 characters + Aedificium architectural ref). Cast-check each against the lock block before passing the gate.
2. **Four prototype pages** spanning both density and format vocabulary (one more than the standard three — the new P13 INTERLUDE introduces a novel diagrammatic-map painted style that must be validated before bulk-batch):
   - **P2 — Brunellus deduction** (cinematic single-image, T3, William + Adso outdoors). Tests: standard biographical page template, the snow / mountain palette, the William ref.
   - **P13 — INTERLUDE (heresy / Inquisition / Avignon)** (hybrid teaching layout, T5, diagrammatic painted map of Latin Christendom 1327, no character refs). Tests: the diagrammatic-but-painted-realism map style, three miniature vignettes in one frame, dense ~165-word concept caption.
   - **P15 — Salvatore + Dolcinian backstory** (hybrid teaching layout, T5, Salvatore + Adso). Tests: the character-anchored hybrid format (compare against P13's diagrammatic hybrid), the Salvatore ref, dense Italian-history caption text.
   - **P24 — Cliffhanger primary-source frame** (Gui's *Practica* page as artifact + small inset scene, T5, Bernard Gui). Tests: primary-source-as-artifact format, the Gui ref, the Vol-1-closing visual hook.
3. Review prototypes. If all four land single-shot, lock the template. If any drift, repair before bulk run.
4. **Bulk-batch** the remaining 20 pages in two parallel waves of ~10. Skill convention.
5. Generate the **cover** as the final image generation step (informed by everything that worked).
6. Build `index.html` reader (dark theme, side-arrow nav, 1400px max-width, quiz at end).
7. Add landing-page card to `~/Documents/nano/index.html`.
8. Update memory + retrospective on ship.

## Cost envelope

~$7.77 estimated. 8 refs + 25 pages (cover + 24 story pages) + ~4 prototype regens × $0.21 (gpt-image-2 standard). Slightly above the Newton / Honda / da Vinci envelope because of the added P13 INTERLUDE teaching page and one extra prototype.

## Quiz (5 questions, written when reader is built)

Per project rule: tests **why**, not **what**. Distractors substantive, similar in length to the correct answer, shuffled positions. The five Vol 1 quiz questions live at the bottom of `index.html`; written during reader build.

## Anti-patterns specific to this volume

- **CAPTION CLARITY RULE — every caption must stand alone for a first-time reader.** No cryptic teasers, no "but…" / "yet…" sentences whose punch depends on a fact the reader hasn't been told, no medieval vocabulary introduced without an inline gloss on first use. If a caption needs the reader to figure out what's missing, rewrite it to say the missing thing plainly. The kid should not be filling in blanks. Inline glosses for terms first used in body captions: *refectory* (the great hall where the monks ate together), *cloister* (the covered walk around the abbey's inner garden), *chapter house* (the great vaulted room where an abbey held its trials and councils), *novice* (a monk-in-training, not yet sworn for life). Canonical hours (Matins/Lauds/Prime/Terce/Sext/None/Vespers/Compline) are introduced wholesale in P1's frame opener and may then be used as time markers without re-explanation. Apply this rule to every Vol 2 page as well.
- Do **not** soften or skip the village girl's arrest in P21. The whole point of P16 + P21 is the Inquisition burning the innocent. Her execution lands in Vol 2.
- Do **not** frame the medieval period as "dark" or "ignorant." The framing is *constrained intelligence*, not stupidity. The library is the most sophisticated information system in 14th-century Europe; that is exactly why losing it matters.
- Do **not** paraphrase Latin tags. Render them verbatim and translate in caption.
- Do **not** show any sexual content in the Adso/village girl scene (P16). Reframe per user direction: meeting + sharing bread, no sex. Adso's confusion and later grief carry the moral weight without needing the original encounter.
- Do **not** generate pages before all 8 refs are locked.
- Do **not** describe the body of Berengar in the bathtub explicitly. The body is half-glimpsed, half-covered, in dim morning light. Lead with William's face reading the evidence, not with the corpse.
- Do **not** describe Adelmo's fall on Page 4 graphically. Reference the death; do not show the body.

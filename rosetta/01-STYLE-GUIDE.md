# 01 — STYLE GUIDE

## §1 Register — "Ink & Lamplight" (PROPOSED — prototype before committing)

The detective shelf needs its own signature, distinct from the myth shelf's heroic
daylight (Icarus) and the sci-fi airbrush (Foundation). Proposal:

**Register-B machinery, nocturnal scholar's tuning.** Bold ink-line comic art with flat
color — the validated one-shot multi-panel idiom — but the palette is a detective's:
deep ink blues and charcoal blacks, parchment cream, warm lamplight ambers. Scenes live
at desks, in archives, by candlelight; Egypt flashes in sun-bleached ochre as the
counter-world. **One accent: lamplight gold `#d9a441`** — it marks EVIDENCE and
UNDERSTANDING (lit documents, the glow on a cartouche at the moment it yields, the final
temple wall). Documents, cartouches, and letter-grids render as crisp cream "evidence
insets" pinned into panels — the case-file look.

**STYLE BLOCK (paste verbatim into every prompt):**
> Bold ink-line comic-book art with flat color, in the tradition of modern literary
> graphic novels. Clean confident black linework, flat color fills, minimal soft
> rendering. Nocturnal scholar's palette: deep ink-blue and charcoal shadows, parchment
> cream, warm amber lamplight; sun-bleached ochre only for Egypt scenes. One accent
> color: lamplight gold on documents and hieroglyphs at moments of discovery.
> Hieroglyphic evidence appears as crisp cream inset panels, like exhibits in a case file.

**REGISTER GUARD (block 2):**
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural
> lighting, cinematic composition. Serious mystery tone — a true intellectual detective
> story, not a cartoon caper.

**Alternative (floated, not chosen):** period-engraving / expedition-notebook — sepia
aquatint texture, Description-de-l'Égypte plates. Riskier: engraving texture fights speech
bubbles and flat-color consistency across 17 pages. If the user prefers it, prototype both
on P2 before committing. **DECISION OPEN at the review gate.**

## §2 Format

- **3:2 landscape, 1536×1024**, gpt-image-2 standard, quality high. One-shot whole-page
  bake: all panels + all lettering in a single `generate_image`/`edit_image` call.
- 3–4 panels per page, explicit geometry in every prompt (e.g. "THREE panels: two equal
  across the TOP, one WIDE across the BOTTOM; reading order top-left, top-right, bottom"),
  clean solid-black borders, clear white gutters.
- Evidence pages (P7, P10, P12, P16) may break the grid: one large "case-file splash" with
  pinned exhibits instead of panels. State it explicitly.
- Text density: generous (narrative-mode rule — do not hold back). Keep each element
  legible; ~8 elements / ~75 words per page is proven; evidence pages run caption-heavy.

## §3 Prompt order (six blocks, do not reorder)

1. Layout spec (panel geometry / case-file splash)
2. STYLE BLOCK (verbatim, §1)
3. REGISTER GUARD (verbatim, §1)
4. RECURRING CHARACTERS lock block — "keep them IDENTICAL in every panel"; visual locks
   only, never the famous name; refs passed via `imagePaths`
5. Per-panel scene beats (who / where / action / camera)
6. `LETTERING — verbatim, render exactly:` … closing with the restrictions block:
   "All words spelled correctly. Do not duplicate text. Do not invent extra captions.
   NO modern logos, NO watermarks, NO spurious signage. Do not put quotation marks inside
   speech bubbles."

## §4 Ref strategy — multi-ref native (Strategy 0)

`edit_image` takes `imagePaths` (1–16). Per page: pass the **master cast plate** + the
**solo refs** of every character on the page + any **cartouche plate** the page exhibits.
- **Master cast plate** (`refs/ref_cast_plate.png`): ONE single generation, 5 entities,
  faces large: Champollion-boy (~12), Champollion-man (~31), Jacques-Joseph (~44),
  Thomas Young (~48), the Rosetta Stone (its true look: dark granodiorite, broken top,
  three text bands). Thin name labels under each; prompts tell the model to ignore labels.
- **Solo refs:** one per entity (5), generated after the plate passes the casting gate,
  each anchored on the plate via multi-ref so plate and solos agree.
- Pre-flight rules unchanged: glob `refs/` before batches; Re-Read every involved ref and
  write a one-line verbatim observation before prompting.

## §5 Cartouche-fidelity plan (the volume's central image risk)

The clues are specific glyphs. The model must never freehand a load-bearing glyph string.

1. **Build cartouche plates locally (PIL), not by generation.** Render the needed signs
   from a hieroglyph font (e.g. Noto Sans Egyptian Hieroglyphs) or traced verified images,
   against cream card: (a) PTOLEMY cartouche, (b) CLEOPATRA cartouche, (c) RAMESSES
   cartouche (sun disc + ms + s + s), (d) THUTMOSE cartouche (ibis + ms), (e) the clue-key
   strip (lion=L, folded cloth=S, sun disc=RA, ibis=THOTH). Verify sign sequences against
   British Museum diagrams at build time.
2. Pass the relevant plate via `imagePaths` on every page that exhibits it; the prompt
   says "copy the cartouche EXACTLY from the reference — same signs, same order."
3. On-page glyph annotations (letters under signs) are part of the LETTERING block.
4. Only the ~5 clue signs carry deductive weight on-page; background hieroglyphs may be
   decorative and unlabeled (decoration needs no fidelity or helper).

## §6 Lettering rules

- Captions: cream case-file boxes, dark serif text; corner placement stated per caption.
- **CLUE BOXES** — the shelf's signature device: a small cream box with a gold pin/corner
  tab reading `CLUE:` followed by the fact. Every clue the detective gets, the reader gets,
  on the page where he gets it. Honest-mystery rule: no clue used in a solve may appear
  for the first time in the solve.
- Speech bubbles: round, off-white, dark serif, tails explicitly aimed; no quotation marks
  inside bubbles.
- **Non-English text always carries an English helper**, same panel: "Je tiens mon
  affaire !" → *I've got it!*; "notre alphabet est bon" → *our alphabet is good*; Coptic
  and Greek words glossed inline. Ornamental/unreadable-scale text is decoration, no helper.
- Period vocabulary glossed on first use in captions: cartouche, demotic, Coptic, decree,
  stele, philologist, lithograph.

## §7 Footer CASE-FILE strip (reader HTML, not in-image)

Persistent footer strip, gold-on-dark, six stages; the active stage lights per page:

`THE SILENCE · THE STONE · FALSE TRAILS · THE CLUES · THE REVEAL · THE LANGUAGE`

Mapping: P1 Silence; P2–P3 Stone; P4 False Trails (P8 also lights False Trails);
P5–P7, P9–P11 Clues; P12–P14 Reveal; P15–P17 Language. Hidden on cover and quiz.
Reader accent `#d9a441`; dark flipper per project standard.

## §8 Moderation notes

Low-risk subject. Watch only: the collapse on P13 (frame as exhaustion/being caught by his
brother — no injury language); Champollion's death (single dignified caption, no scene);
Napoleonic soldiers carry muskets slung, never aimed.

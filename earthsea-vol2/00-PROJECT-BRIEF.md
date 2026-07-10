# Project Brief — The Tombs of Atuan · Part One: The Eaten One

**Series:** Earthsea (Ursula K. Le Guin) — Book Two of the source cycle, Volume 2 of our shelf.
**Volume title:** *The Tombs of Atuan — The Eaten One*
**Folder:** `earthsea-vol2/`
**Format:** Narrative-mode graphic novel, 3:2 landscape 1536×1024, gpt-image-2 standard, quality high.
**Page count:** Cover + 20 pages.
**Sibling volume:** `earthsea/` — *A Wizard of Earthsea: The Shadow and the Name* (shipped 2026-07-08). Same register family, inverted palette.

## The partition (the most important decision in this brief)

**Vol 2 covers the Prologue through Chapter 6 ("The Man Trap") ONLY.** Chapters 7–12 (The Great Treasure, Names, the ring rejoined, Kossil's war, the escape, the earthquake, Havnor) are **Volume 3**.

Why: Vol 1 compressed all ten chapters of *A Wizard of Earthsea* into 20 pages and the user's QA verdict — while enthusiastic — flagged cramming ("stuff felt like it was happening in the background, but no space for it"). Standing instruction: *no need to rush; if we need many volumes, so be it; don't skimp on pages/volumes.* The Tombs of Atuan splits naturally at the man-trap hinge:

- **Part One (this volume) is Tenar's book.** A girl is taken from her family, her name is eaten, and she is raised as the reborn priestess of dark powers — until a forbidden light appears under the hill and she traps the wizard who carries it, and then, against everything she is, keeps him alive. It is a complete arc: eaten → obedient darkness → guilt → wonder → first free act.
- **Part Two (Vol 3) is the two of them.** Names given, the ring rejoined, Kossil's hatred, the escape, the Tombs falling, the white ring brought to Havnor.

Ending Part One on the bolted Painted Room door — her prisoner alive inside, her own longing for the beauty of the lit cavern locked behind her shut eyes — is a true cliff-edge, not a cut-off.

**Ged does not appear until Page 15.** This is faithful to the book (he enters 60% in) and deliberate: the reader must live Arha's whole darkness first, so the werelight lands with the force it has for her.

## One-sentence pitch

A girl whose name was taken and fed to the dark meets the first light she has ever seen underground — and must choose between being the Eaten One and being Tenar.

## Source and research

- Ground truth: full novel text at `tmp/tombs-research/tombs_full.txt` (chapter offsets: Prologue 99, The Eaten One 117, The Wall 184, The Prisoners 355, Dreams and Tales 600, Light Under the Hill 788, The Man Trap 935, ch.7 begins 1234).
- Every baked quote in `04-SCRIPT.md` was verified verbatim against that file. Do not paraphrase them at generation time; do not invent new "quotes."
- All other lettering is original adaptation prose, kept in Le Guin's plain register.

## Editorial commitments

1. **Skin-tone law (first visual law, non-negotiable).** Le Guin's inversion is the volume's moral geometry, doubled here: the *protagonist* is now the white-skinned Karg and the *foreign sorcerer* is dark. Tenar/Arha and every Karg (Manan, Kossil, Thar, Penthe, priestesses, guards) are WHITE-skinned. Ged is DEEP RED-BROWN COPPER, exactly as in Vol 1 — reuse `../earthsea/refs/ref_ged_scarred.png`. Cross-check every ref and every page against this law before passing any gate (Vol 1 lesson: refs drifted light on first gen even with strong lock language).
2. **Arha is not a villain and not a victim-doll.** She orders three men's deaths and the page after shows what it costs her. Play her pride, boredom, cruelty, and wonder honestly; the book trusts kids to follow a dark protagonist.
3. **Darkness is rendered, not skipped.** Roughly a third of the volume happens in places where light is forbidden. The register solves this (see style guide light logic); we do not cheat by brightening the Undertomb before P15.
4. **The Nameless Ones are never drawn.** No monster, no glowing eyes in the dark. Their presence is absolute flat matte black, oppressive framing, and other people's fear. (Continuity with Vol 1's SHADOW rule.)
5. **The prisoners page (P10) is implied, not gory.** Source itself hides their faces in matted hair and shadow. Shapes in smoke; no visible wounds, no nudity readable as such. Arha's decree carries the horror.
6. **The ceremony page (P2) freezes the stayed blade.** We compose the moment of balance — white figure and black figure poised, sword glittering at its height — never a blade descending on a child.

## Moderation notes

- P2 (sword over kneeling child): compose as ritual tableau at the instant the dark figure STAYS the sacrificer's arms; caption states the blade is stayed. If it still trips, fall back to the moment after (the poured libation, sword sheathed, child robed).
- P10 (chained prisoners): "three huddled shapes in torch-smoke, faces hidden by matted hair" — no chains-on-skin close-ups, no emaciation detail.
- P19 (Ged unconscious, bloodied mouth): keep it "dust-caked, exhausted"; the water-drip mercy is the subject, not the injury.

## Production pipeline (for the image-gen session)

Refs first → 3 prototypes (P15 splash, P9 darkness page, P12 dialogue-dense page) → user-visible check → two parallel bulk waves → reader + quiz + landing card. Full instructions in `HANDOFF.md`. Cost envelope ~$6 (≈27 images at ~$0.21).

## Reader

Dark flipper matching Vol 1's chassis. Accent: **werelight violet `#9c8ad6`** (Vol 1 was teal). Footer strip = **descent-strip**: THE ORCHARD · THE THRONE HALL · THE WALL · THE TOMBSTONES · THE UNDERTOMB · THE LABYRINTH · THE PAINTED ROOM — the reader descends with Tenar; active location highlighted per page via `data-depth` attribute. 5-question WHY-quiz (drafted in HANDOFF.md). Landing card into Latest strip + literary-adaptation shelf beside Vol 1 and Name of the Rose.

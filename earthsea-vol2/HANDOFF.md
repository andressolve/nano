# HANDOFF — The Tombs of Atuan · Part One: The Eaten One

> **STATUS UPDATE 2026-07-09, later pass: pages 4, 6, and 18 have been fixed with clean full-page regenerations and promoted to the active filenames.** Active files now use `page-04-v5.png` for page 4 and `page-06-v3.png` / `page-18-v3.png` for pages 6 and 18. Page 4's `-v3` and `-v4` were superseded because panel 3 still needed clearer speaker attribution and reading order; `-v5` stages the girl on the left and Manan on the right so the girl says only "I am not Tenar anymore" and Manan's reply is unambiguous. The failed Claude crop-patch composites remain preserved as `page-04-v2.png`, `page-06-v2.png`, and `page-18-v2.png`; do not reuse that patch method. The original unpatched art remains preserved as `page-04-v1.png`, `page-06-v1.png`, and `page-18-v1.png`. See `earthsea-vol2/FIXES-NEEDED.md` for defect history and resolution notes.

**Volume complete, 2026-07-09.** Cover, 20 active pages, five locked refs, reader, descent strip, quiz, root collection card, and full-page attribution/identity corrections are present. Production used the built-in Codex image-generation path under the user's ChatGPT/Codex entitlement. No API key, imagegen CLI, or direct Image API billing was used.

For future dialogue pages, use `../earthsea-wizard-part1/05-SPEECH-ATTRIBUTION-STUDY.md`. Its core finding applies here: explicit tail instructions reduce risk but do not make attribution deterministic. Solve attribution through speaker placement and reading order, inspect every tail and orphan white fragment, and use full-page regeneration rather than crop patches.

## Read order (before generating anything)

1. `00-PROJECT-BRIEF.md` — partition rationale, editorial commitments, moderation notes.
2. `01-STYLE-GUIDE.md` — STYLE BLOCK, THREE LIGHTS, DARKNESS RULE, ANTI-DRIFT (all verbatim-paste blocks).
3. `02-CHARACTERS.md` — locks + ref-sheet prompts.
4. `03-SETTINGS.md` — locations keyed to descent-strip depths.
5. `04-SCRIPT.md` — cover + 20 pages, verbatim lettering, page→ref map.
6. Vol 1 for register continuity: `../earthsea/01-STYLE-GUIDE.md` and its `pages/` (what the ink-line family looks like when it works).

Ground-truth source text (if any lettering question arises): `../tmp/tombs-research/tombs_full.txt` — now the COMPLETE novel (missing Ch 11 tail + Ch 12 recovered 2026-07-08). Never bake a quote you can't find in it.

Vol 3 (Ch 7–12, "The Ring") is seeded, not planned: see `VOL3-SEED.md`. Not this session's job.

## Production order

1. **Copy Ged's ref:** `cp ../earthsea/refs/ref_ged_scarred.png refs/ref_ged_scarred.png`. Do NOT regenerate him.
2. **Generate refs** (gpt-image-2, 1536×1024, prompts per 02-CHARACTERS): `ref_tenar_child`, `ref_arha`, `ref_manan`, `ref_group_priestesses` (single-gen group sheet: Kossil left / Thar center / Penthe right).
3. **Skin-tone gate (hard gate).** Open and LOOK at every ref. Arha/Tenar/Kargs unmistakably pale white; Ged's copy still shows deep copper + 4 left-cheek scars. Vol 1 lesson: first gens drift light/olive even against strong locks — if drifted, regen with intensified language ("PALE WHITE, NOT tan, NOT olive…"). Check against the law, not "looks okay."
4. **Three prototypes, in this order, and STOP to inspect each:**
   - **P15** (crystal-cavern werelight splash) — the volume's hero page and hardest lighting job. If the werelight renders warm/gold instead of silver-violet, fix language before anything else ("silver-VIOLET marshlight, NOT golden, NOT firelight").
   - **P9** (descent into darkness) — validates the DARKNESS RULE and white-on-black caption boxes. If 90%-black panels fail (model fills with blue wash or detail), fall back to: smaller lit slivers (a candle they shouldn't have is NOT allowed — use the door-slit light and near-silhouettes) and park captions on parchment boxes instead.
   - **P12** (Penthe's apples, dialogue-dense daylight) — validates text density and the two-girl double-lock.
5. **Bulk batch** the remaining 17 pages + cover in two parallel waves (Vol 1 ran 2×9 with zero regens). Three-question check per image: same person? right text? right mood? Also: no gold light underground before P15; the Nameless Ones never drawn.
6. **Known moderation flashpoints** (fallbacks already scripted in brief/script): P2 stayed-blade tableau, P10 prisoners, P19 unconscious Ged. Use the scripted fallback framing on first rejection — do not improvise new compositions.

## Reader build

- Dark flipper, same chassis as `../earthsea/index.html`. Accent: **werelight violet `#9c8ad6`** (replaces Vol 1's teal `#5aa8a2`).
- Footer = **descent-strip**: `THE ORCHARD · THE THRONE HALL · THE WALL · THE TOMBSTONES · THE UNDERTOMB · THE LABYRINTH · THE PAINTED ROOM` — same CSS/JS pattern as Vol 1's voyage-strip, driven by `data-depth` per page (values in 04-SCRIPT page headers). Strip label: "The descent of the Eaten One".
- Title page metadata: *The Tombs of Atuan — Part One: The Eaten One*, "from the novel by Ursula K. Le Guin", Earthsea Volume 2.

## WHY-quiz (5 questions, use these)

1. **Why do the priestesses say Tenar "is eaten"?** → Her name and self are given to the Nameless Ones; the girl Tenar is supposed to be gone, leaving only Arha, the Priestess Ever Reborn.
2. **Why does Arha order the three prisoners' deaths — and why does she then dream of carrying water?** → Because it is the duty she was raised for and Kossil is watching; the dreams are the part of her the Tombs couldn't eat, grieving what she did.
3. **Why has no one ever seen the Undertomb, and what does the wizard's light reveal about it?** → Light is forbidden in the holiest dark; the werelight shows the "house of death" is actually beautiful — a palace of crystal — which changes how Arha sees everything she serves.
4. **Why did the wizard come to the Tombs?** → To find the lost half of the ring of Erreth-Akbe (the crescent on his chain is the other half) — the treasure wizards have died seeking for centuries.
5. **Why does Arha keep the wizard alive, when her whole duty says to kill him?** → It is her first act that is truly her own — Tenar's act, not Arha's. Mercy, curiosity, and the memory of the light outweigh the rules of the dark.

## Landing card

Add to root `index.html`: card in "Latest · just shipped" strip (drop the oldest of the 6) + link under the literary-adaptation shelf beside Vol 1 and Name of the Rose. Card copy suggestion: *"Her name was fed to the dark. Then a light came under the hill. Le Guin's Tombs of Atuan, Part One."*

## Billing Path

- Built-in Codex image generation under the user's ChatGPT/Codex entitlement.
- No `OPENAI_API_KEY`, bundled imagegen CLI, or direct API request.
- Usage belongs to the Codex/ChatGPT allowance or credit pool configured for the account, not the API Platform bill.

## Ship checklist

- [x] Refs generated + skin-tone gate passed
- [x] Three prototypes approved (P15, P9, P12)
- [x] Cover + 20 pages, three-question check each
- [x] Reader (`index.html`) with descent-strip + violet accent
- [x] WHY-quiz wired
- [x] Landing card + shelf link in root `index.html`
- [x] Pages 4, 6, and 18 corrected with full-page regenerations
- [x] Commit and push requested; scope isolated from unrelated worktree changes

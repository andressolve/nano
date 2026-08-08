# The Count of Monte Cristo — Pages 11–20 Production QA

> **Historical QA authority for the superseded Round 10 canonical batch.** On
> 2026-08-06, Andres approved the later visual-continuity set and both final
> gates passed. The current canonical file map and hashes are in
> [`28-PAGES-11-20-VISUAL-CONTINUITY-FINAL-GATE.md`](28-PAGES-11-20-VISUAL-CONTINUITY-FINAL-GATE.md).
> The exact pages described below remain archived under
> `qa/pre-visual-continuity-canonical-2026-08-06/`.

## Current status

**Pages 11–20 passed both independent clean-room critic gates unconditionally
in Round 10 on 2026-08-04 and are now canonical.** The ten canvases under
[`pages/`](pages/) are flattened **1024 × 1536 portrait PNGs** with native
lettering. Matching **390 × 585** proofs are under
[`qa/mobile-pages-11-20/`](qa/mobile-pages-11-20/), and the approved sequence is
shown in [`qa/pages-11-20-contact-sheet.png`](qa/pages-11-20-contact-sheet.png).

Pages 12–18 are complete new generations. The July 27 prototype images were
not reused; they are preserved under
[`qa/historical-prototypes-2026-07-27/`](qa/historical-prototypes-2026-07-27/)
for audit history only.

The ten-round findings, whole-page regeneration contracts, and final exact
approval tokens are recorded in
[`26-PAGES-11-20-CRITIC-LOOP.md`](26-PAGES-11-20-CRITIC-LOOP.md).

## Accepted-version map

| Page | Accepted production version | Material regeneration history |
| --- | --- | --- |
| 11 | v16 | Rebuilt family/merchant identity separation, mobile prose, all dialogue lanes, and the final Edmond mouth-level tail |
| 12 | v12 | Enlarged reception text and locked Villefort at age thirty while preserving the royalist-family stakes |
| 13 | v16 | Locked nineteen-year-old Edmond, kept the memory figures silent, and moved both testimony balloons into Edmond's right speaker lane |
| 14 | v10 | Preserved separate accusation and sealed letter, corrected ages, enlarged the final reply, and rebuilt both final tails |
| 15 | v15 | Rebuilt the A–B–A recognition exchange with three separate mouth-level tails and one unframed blank-order beat |
| 16 | v18 | Corrected ages and the Edmond trust tail while preserving the burn → reassurance → signed-order → guard sequence |
| 17 | v12 | Corrected Edmond/guard identity, compact Château d'If, blank sealed order, transfer staging, and mobile text |
| 18 | v8 | Restored exact dimensions, numeral-only dominant register, distinct clerk/guard/jailer identities, and readable lower exchange |
| 19 | v12 | Restored petition writing and unopened-petition continuity and differentiated the two recurring silent guards |
| 20 | v21 | Locked Morrel across Panels 1–3, age-thirty Villefort across Panels 1/4, Louis/clerk identities, red purse, and every mouth connector |

Rejected and intermediate full-page generations remain under
[`qa/production-pages-11-20/`](qa/production-pages-11-20/). No accepted page
contains a crop-patched face, tail, balloon, word, or panel.

## Script and attribution gate

The accepted pages were checked visually at source size against the exact text
and panel records in
[`10-FULL-52-PAGE-SCRIPT.md`](10-FULL-52-PAGE-SCRIPT.md). The batch preserves:

- every scripted prose block and speech line, including `Dantès`, `Mercédès`,
  `Château d'If`, `Thirty-four`, and `Bonapartist`;
- the required speaker sides and A–B–A or A–B–A–B reading tiers;
- silent status for feast guests, memory figures, guards, rowers, and clerks;
- separate physical handling of the sealed letter, unsigned accusation,
  burning true letter, detention order, register, petition, and red purse;
- one normal top-to-bottom reading path with no production labels, ordinals,
  speaker names, or stray text.

The final strict gate passed every required speaker lane and mouth endpoint;
the blind gate independently passed every attribution at phone and source size.

## Identity gate

The final full-size identity pass caught and corrected the material errors
that survived the first mobile read:

- the tall auburn-moustached navy escort belongs to Pages 16–18 only as guard;
- the speaking Château d'If jailer on Pages 18–19 is the separate short,
  ruddy, balding, gray-red-stubbled civilian with rust waistcoat and keys;
- the intake clerk remains thin, sandy, drooping-faced, tobacco/ochre, and
  ledger-led;
- the prison governor remains heavy, clean-shaven, white-haired, and
  bottle-green/gold;
- Morrel remains square-faced and clean-shaven with silver temples, navy coat,
  and burgundy waistcoat;
- young Edmond remains clean-shaven and loose-curled throughout, while revised
  Villefort remains pale, narrow, aquiline, side-parted, and high-collared;
- Louis, young Mercédès, Renée, the Marquise, Leclère, and the principal guard
  retain their ledger silhouettes and nearest-neighbor exclusions.

## Reader-size and causal-sequence gate

All ten accepted pages were reduced from the canonical files to 390 × 585 and
read in order. The dense Pages 17–20 remain legible without opening the source
images. The sequence communicates this chain in one normal read:

1. Mercédès, Louis, Morrel, and even Fernand react after Edmond is taken; Morrel
   leaves to find Villefort while Edmond still expects to return.
2. Villefort's royalist marriage and Bonapartist father make Edmond's sealed
   letter personally dangerous to him.
3. Edmond explains the dying-captain promise and unopened letter honestly.
4. Villefort concludes that Edmond is innocent and identifies the anonymous
   accusation as a trap.
5. Noirtier's name changes Villefort's private risk, not Edmond's conduct.
6. Villefort burns the only evidence, secures Edmond's silence, and signs a
   separate detention order after Edmond says he trusts him.
7. The order moves Edmond past the city prison and out to Château d'If.
8. The clerk accepts the file and replaces Edmond's name with Prisoner
   Thirty-four; a separate jailer locks him away.
9. Edmond tries payment, the governor, a petition, and sentence length, then
   learns that an open-ended detention order has no release date.
10. Morrel, Louis, and Mercédès are actively trying to help, but Villefort
    deliberately marks the file to block visitors and correspondence.

## Production method

The pages were generated with the built-in subscription-backed Codex image
generation path. No API key, direct Image API billing, overlay lettering, or
partial image repair was used. The reproducible baseline prompt set and exact
page maps are recorded in
[`24-PAGES-11-20-PRODUCTION-PROMPTS.md`](24-PAGES-11-20-PRODUCTION-PROMPTS.md).

## Checkpoint

The final Round 10 sequence received both exact approvals:
`SCRIPT-FIDELITY APPROVED` and `COLD-READ/VISUAL APPROVED`. SHA-256 comparison
confirmed that the promoted canonical files are byte-identical to the approved
Round 10 packet. User review is now the only remaining checkpoint before the
batch is locked and production advances to Page 21.

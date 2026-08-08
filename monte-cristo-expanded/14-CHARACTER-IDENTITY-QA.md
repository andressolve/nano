# The Count of Monte Cristo — Character Identity QA

## Status

**Round 2 approved by the independent critic on 2026-07-31.**

The full verdict and blocker-by-blocker evidence are in
[`12-CHARACTER-DISTINCTNESS-CRITIC-REPORT.md`](12-CHARACTER-DISTINCTNESS-CRITIC-REPORT.md).

The first-edition references remain untouched. Twelve new expanded-edition
reference sheets were generated through the subscription-backed built-in image
path and saved in [`refs/`](refs/). All reference sheets are 1536 × 1024 RGB
PNGs with no labels or story text.

## New reference set

1. [`refs/01-villefort-1815-v2.png`](refs/01-villefort-1815-v2.png)
2. [`refs/02-count-v2.png`](refs/02-count-v2.png)
3. [`refs/03-jacopo-v2.png`](refs/03-jacopo-v2.png)
4. [`refs/04-louis-dantes-v2.png`](refs/04-louis-dantes-v2.png)
5. [`refs/05-fernand-1815-v2.png`](refs/05-fernand-1815-v2.png)
6. [`refs/06-julie-emmanuel-v2.png`](refs/06-julie-emmanuel-v2.png)
7. [`refs/07-mercedes-1838-v2.png`](refs/07-mercedes-1838-v2.png)
8. [`refs/08-busoni-wilmore-v2.png`](refs/08-busoni-wilmore-v2.png)
9. [`refs/09-leclere-noirtier.png`](refs/09-leclere-noirtier.png)
10. [`refs/10-renee-marquise.png`](refs/10-renee-marquise.png)
11. [`refs/11-principal-guard-jailer.png`](refs/11-principal-guard-jailer.png)
12. [`refs/12-clerk-governor.png`](refs/12-clerk-governor.png)

The exact positive and forbidden identity locks are recorded in
[`13-CHARACTER-IDENTITY-LEDGER.md`](13-CHARACTER-IDENTITY-LEDGER.md).

## Comparison boards

The boards are deliberately label-free so a name cannot rescue a weak design.
The fixed row-major order for the full-cast head and silhouette boards is:

1. young Edmond;
2. prison Edmond;
3. the Count;
4. Faria;
5. Villefort;
6. Mercédès 1815;
7. Mercédès 1838;
8. Louis Dantès;
9. Danglars;
10. Fernand;
11. Caderousse;
12. Morrel;
13. Julie;
14. Emmanuel;
15. Jacopo;
16. smuggler captain;
17. Busoni;
18. Wilmore;
19. Leclère;
20. Noirtier;
21. Renée;
22. the Marquise;
23. principal guard;
24. jailer;
25. intake clerk;
26. governor.

Files:

- [`qa/character-heads-board.png`](qa/character-heads-board.png) — equal-size
  color head crops;
- [`qa/character-silhouettes-board.png`](qa/character-silhouettes-board.png) —
  equal-cell grayscale full-body comparison;
- [`qa/adversarial-edmond-villefort.png`](qa/adversarial-edmond-villefort.png)
  — young Edmond / Villefort / Fernand / Danglars;
- [`qa/adversarial-formal-men.png`](qa/adversarial-formal-men.png) — Count /
  Villefort / Emmanuel / Wilmore;
- [`qa/adversarial-escape-men.png`](qa/adversarial-escape-men.png) — young
  Edmond / prison Edmond / Jacopo / smuggler captain;
- [`qa/adversarial-fathers-and-daughters.png`](qa/adversarial-fathers-and-daughters.png)
  — Louis / Faria / young Mercédès / Julie.

Each adversarial board presents equal-size color head crops above grayscale
silhouettes in the same left-to-right order.

The deterministic board builder is
[`qa/build-character-boards.sh`](qa/build-character-boards.sh). It crops the
actual approved candidates; it does not redraw, interpolate, or prompt new
faces.

## Hardest live-pair proof

[`qa/page15-edmond-villefort-identity-proof.png`](qa/page15-edmond-villefort-identity-proof.png)
is a 1024 × 1536 portrait, unlettered four-panel proof using the revised
Villefort and retained young Edmond locks. It tests:

- an opposed waist-up two-shot in low warm office light;
- tight face-only opposed profiles with most costume removed;
- Villefort alone controlling a document;
- Edmond alone turning toward the door.

The proof is not final Page 15 artwork and contains no approved story text. It
exists only to determine whether the two identities survive the exact setting,
lighting, scale, angle, and close-crop conditions that exposed the original
collision.

## Internal checks before Round 2

- Young Edmond and Villefort now differ in apparent age, face geometry, nose,
  forehead, hairline, complexion, and posture before costume is considered.
- The Count remains visibly descended from Edmond's bones but has late-thirties
  planes, swept-back hair, prison pallor, and columnar stillness absent from
  Villefort.
- Jacopo differs from both Edmond states in face width, ears, nose, moustache,
  curl scale, height, posture, palette, and grayscale silhouette.
- Louis and Faria now oppose bald tidy domestic stoop to wild animated teacher.
- Fernand is broader, tied-haired, aquiline, planted, and umber rather than
  Edmond's lean loose-curled indigo sailor.
- Emmanuel and Julie no longer borrow the lead male or Mercédès face grammars.
- Every causally important recurring Volume I role named in the Round 1 report
  now has a permanent reference lock.
- All source files and comparison boards passed dimension/type inspection.

The reference system is approved for page production. Approval is not inherited
automatically by generated pages: every finished page must still pass the
native-size, face-crop, grayscale, mobile, thumbnail, wording, reading-order,
and balloon-attribution checks.

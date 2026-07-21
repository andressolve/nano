# Euclid — Production QA

## Reference gate — passed

All accepted references are 1536×1024 RGB PNGs created through subscription-backed Codex image generation.

### Observed pixel locks

- `ref_euclid_young.png`: long narrow olive face, large deep brown eyes, strong straight nose, dense black curls to nape, close black beard, lean frame, cream linen, dark weathered blue mantle. Portrait is solemn; working view bends low over a black wax tablet.
- `ref_euclid_master.png`: recognizably the same long face and eyes; forehead and cheek lines, gray threaded curls, gray-black beard, same cream linen and dark blue mantle. Standing view carries bronze dividers; teaching view uses an open right hand over papyrus.
- `ref_nefru.png`: rich brown skin, broad oval face, high cheekbones, dark steady eyes, close braids under cream headband, white linen and rust-red wrap. Strong hands; cord and reed pen read clearly.
- `ref_philippos.png`: warm olive-brown skin, triangular-oval young face, hazel-brown eyes, thick cropped black curls, pale malachite chiton, slender late-adolescent build, wax tablet and stylus.
- `ref_philippos_teacher.png`: same face aged subtly, same malachite chiton, charcoal wrap and pebble pouch, rows of counting stones in teaching pose.
- `ref_ptolemy.png`: broad older weathered face, iron curls and beard, white cloth diadem, white tunic, deep purple mantle and round gold pin. Working view includes a left-hand scar and city plan.
- `ref_alexandria.png`: active blue harbor, measured unfinished quay, survey cords and stakes, mixed workers, red-based colonnade under construction. No completed lighthouse or Roman monument.
- `ref_workroom_tools.png`: strongly painterly cedar-and-limestone room; papyrus cupboards, reed pens, ink cups, stone weights, bronze dividers, unmarked straightedge, cord, sand tray, and blue courtyard. Central working sheet contains only a circle and angle, no fake writing.

### Rejection record

- `refs/rejected/ref_workroom-v1.png` was rejected because it drifted toward photographic rendering and included dense pseudo-writing on the central papyrus.
- The final was a targeted whole-image edit: same layout and tools, visibly painted register, pseudo-writing removed. No crop patch or overlay was used.

## Prototype gate

- [x] Page 1 — cinematic hook and uncertainty contract. Exact three-block uncertainty contract; master Euclid lock; 1536×1024. First render rejected for a prematurely completed Pharos; accepted repair uses a low unfinished harbor skyline.
- [x] Page 13 — annotated Proposition 1 artifact. Exact seven text elements; exactly two endpoint-centered equal-radius circles; mathematically equilateral triangle; 1536×1024. Image-generated constructions were rejected for an extra circle, a squat triangle, and later center/radius drift. The final construction is deterministic code composited onto an image-generated clean papyrus plate.
- [x] Page 28 — proof-shaped transmission finale. Exact five text elements; distinct Greek, Arabic, Latin, print, and modern work; Euclid alone as the recurring identity; correct equilateral construction; 1536×1024. Earlier renders were rejected for incorrect geometry and a Greek copyist who duplicated Euclid's face.

Accepted prototypes are preserved in `research/prototypes/` and copied into `pages/`. Rejected renders are preserved in `pages/rejected/` with the defect named in the filename.

## Full-run checks

For every final:

- [x] 1536×1024. Cover plus Pages 1–28 validated with `sips` on 2026-07-20.
- [x] same identity / correct age-state. Young/master Euclid, young/teacher Philippos, Nefru, and Ptolemy checked against accepted locks; wrong-face renders for Pages 10 and 14 were rejected and repaired.
- [x] exact lettering, no omissions, paraphrases, duplicates, or extra text. Every accepted page was inspected at generation size against `04-SCRIPT.md`.
- [x] clear dialogue reading order and tail endpoints. Page 7's duplicate-speaker staging was rejected and rebuilt as a single continuous scene; the Page 18 five-beat exchange was checked after its coin repair.
- [x] no modern notation, codex books, Roman drift, magical geometry, or fake signage. Completed-Pharos renders on Pages 1 and 19 were rejected and repaired.
- [x] page states what changed and why it matters. Volume-level contact sheet saved as `research/contact-sheet.jpg` for the continuity pass.

Additional object/diagram checks: Page 13 contains exactly two endpoint-centered equal-radius circles and a true equilateral triangle; Page 18 contains exactly three obols; Page 26 contains five regular-solid models and one row of thirteen roll compartments; Page 28 repeats the correct construction proportions.

Page 11 repair, 2026-07-21: the original accepted render was later rejected after a floating severed forearm/hand was found above the right papyrus. It is preserved as `pages/rejected/page-11-floating-hand.png`. The repaired page removes only that anatomy defect, restores continuous tabletop, and lays the bronze dividers naturally beside the completed circle; lettering, Euclid, framing, and the three visual zones remain locked.

Page 13 repair, 2026-07-21: `research/proposition-1-geometry-reference.svg` defines the reference construction with exact coordinates. After a reference-guided image edit still distorted the centers and triangle height, it was rejected as `pages/rejected/page-13-code-reference-drift.png`. Image generation then produced only `research/page-13-clean-plate.png`; the final geometry comes from `research/proposition-1-page-overlay.svg`, where A=(650,500), B=(890,500), AB=240, and C=(770,500−240√3/2). The code-rendered overlay and clean plate produce `research/page-13-code-composite.png`, copied identically to the prototype and production page.

## Reader checks

- [x] cover through Page 28 load in order. The complete path was exercised in the in-app browser; every page resolved to a 1536×1024 source image.
- [x] afterword and five-question WHY quiz reachable. All five correct-answer paths were exercised and produced the final `5 out of 5` score.
- [x] fixed navigation, keyboard, click zones, swipe, progress, zoom, and lazy prefetch work. Arrow-button, ArrowRight, image-click, zoom-open, and Escape-close paths were browser-exercised; touch and adjacent-image handlers were code-inspected.
- [x] proof-strip stages update correctly. Browser samples passed at Pages 6, 11, 13, 19, and 27: Definitions, Postulates, Proof, Elements, and Transmission, with the preceding stages complete.
- [x] mobile viewport has no body overflow or control collisions. At 390×844, client width and scroll width both measured 390 pixels; the page, fixed controls, and proof strip remained visible.
- [x] catalog card and archive link work. The home card opened the Euclid reader and the archive contained exactly one Euclid link.

Final browser pass: no console errors in the reader, home-card launch, or archive path.

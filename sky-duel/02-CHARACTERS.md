# 02 — CHARACTERS & LOCKED OBJECTS

In this volume the recurring "characters" are mostly machines. Same lock discipline as faces: never rely on the model knowing a name; the visual description is the lock. Refs gate page production.

## HERO JET — `refs/ref_hero_jet.png`

Lock block (paste verbatim):
> Single-engine single-seat fighter jet, compact delta-blended wing-body, bubble canopy with no frame forward, single tail fin, air intake under the nose, light gray air-superiority paint with subtle darker gray radome, low-visibility star-and-bar roundel on fuselage, slender white missile on each wingtip rail. No squadron numbers, no text stenciling.

(It is an F-16 silhouette; do not write "F-16" in image prompts — script/captions may name it.)

Ref prompt: side three-quarter view in flight over desert, full airframe visible, neutral lighting, no text, no labels. + Style/Register/Anti-drift blocks.

## ADVERSARY JET — `refs/ref_adversary_jet.png`

Lock block:
> Twin-engine twin-tail fighter jet, dark blue-gray camouflage with lighter gray underside, sharp shovel-nose radome, widely spaced engine nacelles, red star-style roundel partially visible, menacing wide stance. No text stenciling.

Ref prompt: three-quarter front view in flight among dark clouds, no text, no labels. + blocks.

## THE MISSILE — `refs/ref_missile.png`

Lock block:
> Slender air-to-air missile, 3 meters long and only 13 centimeters thick, smooth white-gray body, glossy black glass seeker dome at the very tip, four small triangular steering canard fins just behind the nose, four larger swept tail fins at the rear, a tiny metal wheel embedded at the tip of each tail fin (rollerons), slim solid rocket nozzle at the back.

Ref prompt: clean studio side profile on warm ivory background, museum-quality painted technical illustration, entire missile in frame, no text, no labels. + blocks.

## THE ENGINEER — `refs/ref_engineer.png`

(Bill McLean — name NEVER in image prompts.)

Lock block:
> American engineer in his mid-forties, 1950s era, short neatly combed dark hair starting to gray at the temples, round wire-rim glasses, thoughtful steady expression, white short-sleeved shirt with a pen in the breast pocket, dark trousers, lean build, holding a small electronic assembly in his hands. Realistic adult anatomy, period-accurate.

Ref prompt: 3/4 portrait at a cluttered 1950s electronics workbench, warm tungsten light, vacuum tubes and oscilloscope behind him, no text, no labels. + blocks.

## Multi-element pages

gpt-image-2 `edit_image` (our direct-API equivalent) takes ONE image. Pages needing 2+ locked elements use a locally-stitched composite plate (PIL/sips paste of accepted refs onto one canvas) saved as `refs/composite_<page>.png`, passed as the single image, with the plate prompt: "This input is a REFERENCE SHEET, not a layout to keep — paint ONE NEW unified single-scene painting using the references; do not reproduce the sheet's split layout; ignore any printed labels."

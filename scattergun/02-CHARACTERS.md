# 02 — CHARACTERS & LOCKED OBJECTS

The recurring "characters" are mostly machines (Sky Duel discipline). The visual description is the lock; famous names never appear in image prompts. Refs gate page production.

## HERO SHOTGUN — `refs/ref_hero_shotgun.png`

The over-under sporting gun seen on FIELD pages and the finale.

Lock block (paste verbatim):
> Classic over-and-under sporting shotgun: two barrels stacked vertically, deep blued-steel barrels, warm oiled-walnut stock and forend with visible wood grain, color-case-hardened receiver with fine scrollwork engraving (no lettering), thin brass bead sight at the muzzle, gentle curved trigger guard. Elegant, well-kept, museum-grade.

Ref prompt: clean studio side profile on warm ivory background, entire gun in frame, museum-quality painted technical illustration, no text, no labels. + Style/Register/Anti-drift blocks.

## THE SHELL — `refs/ref_shell.png`

Lock block:
> A 12-gauge shotgun shell: glossy deep-red ribbed plastic hull, polished brass head at the base, neatly folded star crimp at the top, about 7 centimeters long. Beside it the same shell in cutaway: brass head with a small silver primer disk at center bottom, a thin layer of dark powder grains, a translucent plastic wad cup with crumple legs, and a tight cluster of small gray lead pellets under the crimp.

Ref prompt: studio pair on warm ivory background — whole shell standing upright on the left, cutaway shell on the right at the same scale, museum-quality painted technical illustration, no text, no labels. + blocks.

## THE GUNSMITH — `refs/ref_gunsmith.png`

(John Moses Browning — name NEVER in image prompts.)

Lock block:
> American gunsmith in his mid-forties, around 1900: tall and lean, dark hair neatly side-parted and graying at the temples, full dark mustache, calm appraising gray eyes, white collarless shirt with sleeves rolled to the elbow, dark vest, worn leather apron, strong careful hands. Realistic adult anatomy, period-accurate.

Ref prompt: 3/4 portrait at a frontier gunsmith's workbench, warm lamplight, wood shavings and steel parts and hand tools around him, holding a steel receiver up to the light, no text, no labels. + blocks.

## THE HUMPBACK — `refs/ref_humpback.png`

The Auto-5 silhouette for P10 and the finale.

Lock block:
> Early-1900s semi-automatic shotgun with an unmistakable silhouette: single barrel, long tubular receiver whose rear end is squared off in an abrupt high hump before dropping to the walnut stock, oiled walnut forend, blued steel, charging handle on the right side of the bolt. No lettering on the metal.

Ref prompt: clean studio side profile on warm ivory background, entire gun in frame, museum-quality painted technical illustration, no text, no labels. + blocks.

## THE CLAY DISC — prose-locked, no ref

> A clay pigeon: bright hunter-orange inverted saucer disc, about 11 centimeters across, with a shallow dome top and ribbed rim.

Simple enough to hold by prose alone (validated approach: Sky Duel's flares/chaff were prose-locked).

## Multi-element pages

gpt-image-2 `edit_image` takes ONE `imagePath`. Pages needing 2+ locked elements use a locally-stitched composite plate (PIL paste of accepted refs onto one canvas, thin REFERENCE A/B/C labels) saved as `refs/composite_<name>.png`, passed as the single image, with the plate instruction: "This input is a REFERENCE SHEET, not a layout to keep — paint ONE NEW unified single-scene painting using the references; do not reproduce the sheet's split layout; ignore any printed labels."

Planned composites:
- `composite_field.png` = hero shotgun + shell → cover, P1, P5, P13.
- `composite_finale.png` = hero shotgun + humpback + shell → P14 montage.

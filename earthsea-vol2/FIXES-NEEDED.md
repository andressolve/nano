# Fix notes — page 4, page 6, page 18

## Resolution update — 2026-07-09

The failed local crop-patch composites were replaced with clean full-page regenerations:

- `pages/page-04-v5.png` promoted to `pages/page-04.png` (`page-04-v3.png` and `page-04-v4.png` were superseded because panel 3 needed clearer speaker attribution and reading order)
- `pages/page-06-v3.png` promoted to `pages/page-06.png`
- `pages/page-18-v3.png` promoted to `pages/page-18.png`

The replacement pages were generated through the Codex built-in image generation path, not the API/CLI path. The original unpatched `-v1` pages and failed `-v2` patch composites are still preserved for provenance. Do not resume the crop-patch-blend method described below.

Historical note from the session that attempted (and botched) local patch-fixes on three pages. User's verdict on those patch results: "absolute shit." Do not trust `page-04-v2.png`, `page-06-v2.png`, or `page-18-v2.png` — they contain the failed patches. **Original, unpatched art is preserved at `page-04-v1.png`, `page-06-v1.png`, `page-18-v1.png`; fixed full-page regenerations are preserved at `page-04-v5.png`, `page-06-v3.png`, and `page-18-v3.png`.**

## My method (why it produced bad results — avoid repeating it)

For all three pages I did NOT regenerate the full page. Instead I:
1. Cropped a small region around the defect (a panel or two-bubble area) out of the original PNG with PIL.
2. Ran `mcp__openai-image-2__edit_image` on just that crop with a prompt describing the one fix.
3. The model returned a 1024x1024 (or similar) image that had reframed/rescaled the crop content (sometimes with padding, sometimes filling the frame with slightly different zoom).
4. I resized that output back down to the original crop's exact pixel dimensions (often a non-integer scale, e.g. 1024x1024 → 370x300), did a crude per-channel mean/std color match against the original crop, feathered the patch edges with a Gaussian-blurred rectangular alpha mask, and pasted it back into the full-res page with PIL.
5. Promoted the result over the clean filename (keeping `-v1` as the untouched original, and saving my patch as `-v2`).

**Suspected root causes of the bad output**, based on re-inspection after the user's reaction:
- The resize round-trip (crop → 1024x1024 model output → resize back to e.g. 370x300 or 776x520) softens/blurs the patch relative to the crisp native-resolution rest of the page — visible as a mushy patch at full zoom even though my small preview crops looked okay to me.
- The crude mean/std color match doesn't actually match tone/contrast well in areas with strong local lighting gradients (e.g. Manan's face half-lit half-shadowed) — likely produced a visible flatness or color cast in the patch vs. surrounding art.
- For the speech-bubble tail fixes, my edits only nudged the tail direction slightly and the result is ambiguous — the tail doesn't clearly terminate on the correct character's face, it just points into empty space nearby. This doesn't actually read as "fixed" attribution.
- For Ged's page-18 likeness fix, the model produced "a brown-skinned man" but not confidently *Ged specifically* — hawk-like face shape, sharp features, and the four-scar detail from `refs/ref_ged_scarred.png` didn't transfer strongly. Skin tone shift registered but character identity didn't lock the way it should.

**Recommendation for the next attempt:** prefer a real full-page regeneration (img2img on the whole page at native 1536x1024 with the six-block prompt from `01-STYLE-GUIDE.md`/`04-SCRIPT.md`, all relevant refs attached, and very explicit "keep everything identical except X") over crop-patch-blend. If a full-page reroll is used, budget for the fact composition may shift and the result needs a fresh three-question check (same person? right text? right mood?), not just a zoomed-in check of the patched region.

---

## Page 4 — panel 3 (bottom wide panel)

**File:** `pages/page-04.png` (fixed full-page regen, same as `page-04-v5.png`) / **original:** `pages/page-04-v1.png` / **failed patch:** `pages/page-04-v2.png` / **superseded regens:** `pages/page-04-v3.png`, `pages/page-04-v4.png`

**Defects in the original (`-v1`):**
1. The two speech bubbles in panel 3 have their tails pointing to the wrong speaker. "I am not Tenar anymore." (the child's line) has its tail pointing toward Manan. "No. I know. Now you're the little Eaten One. But I . . ." (Manan's line) has its tail pointing toward the child. They're swapped.
2. Manan is missing his nose in both panel 2 (close-up, "Ho, Tenar, my little honeycomb...") and panel 3 — his face reads as a flat curve from brow to jaw with no nose at all. He has a proper heavy/bulbous nose on page 6 and (presumably) page 8 — see `refs/ref_manan.png` for his correct face.

**What I tried:** Cropped panel 2 alone and fixed the nose (this one may actually be closer to acceptable — check it). Cropped panel 3 alone, ran an edit for both the nose and a tail-swap in one prompt — this produced a botched result with the bubbles' whole layout shifted and blank white space added, so I abandoned that combined attempt. I then did panel 3's nose via a very tight crop of just Manan's face (`(450,500)-(820,800)` in original page coordinates), and separately did the bubble fix via a tight crop of just the two bubbles (`(720,460)-(1536,680)`) asking the model to swap the TEXT CONTENT between the two existing bubble shapes (keeping shapes/tails as-is) rather than redirect the tails — reasoning that if bubble A's tail already (wrongly) pointed at speaker of bubble B's line, swapping the text would fix both at once. Patched all three regions (panel 2 nose, panel 3 nose, panel 3 bubble text) back into the page with the resize/color-match/feather method described above.

**Current state:** `page-04.png` = fixed full-page regeneration promoted from `page-04-v5.png`. `page-04-v5.png` stages panel 3 with the girl on the left and Manan on the right, so left-to-right reading order and speech tails both assign the lines correctly: the child says only "I am not Tenar anymore"; Manan says "No. I know. Now you're the little Eaten One. But I . . ." `page-04-v3.png` was cleaner than the patch but still visually ambiguous in panel 3. `page-04-v4.png` improved attribution but still had awkward left-right reading order. `page-04-v2.png` = failed local patch composite. `page-04-v1.png` = clean original with both defects still present, untouched.

---

## Page 6 — panel 2 (bottom-left panel)

**File:** `pages/page-06.png` (fixed full-page regen, same as `page-06-v3.png`) / **original:** `pages/page-06-v1.png` / **failed patch:** `pages/page-06-v2.png`

**Defect in the original (`-v1`):** In panel 2 (close two-shot of Penthe on the left, Arha on the right), the bubble "What for? All that happens everywhere, begins here." is Arha's line per the script (`04-SCRIPT.md` page 6 lettering block), but its tail points down-left toward Penthe. The second bubble in that panel, "I know. . . . But I'd like to see some of it happening!" (Penthe's line), correctly points to Penthe already — only the first bubble is wrong.

**What I tried:** Cropped a region containing both faces and just the first bubble (`(0,460)-(500,780)` in original page coordinates — note my first attempt used a crop starting at y=505 which cut off the top of the original bubble and caused a double-exposure ghosting artifact when pasted back; the corrected crop starts at y=460). Ran an edit asking only to redirect the bubble's tail from Penthe to Arha, keeping bubble text/shape/position otherwise identical. Patched back with the same resize/color-match/feather method.

**Current state:** `page-06.png` = fixed full-page regeneration promoted from `page-06-v3.png`. `page-06-v2.png` = failed local patch composite. `page-06-v1.png` = clean original with the tail still pointing at Penthe.

---

## Page 18 — panels 2 and 3 (Ged's likeness)

**File:** `pages/page-18.png` (fixed full-page regen, same as `page-18-v3.png`) / **original:** `pages/page-18-v1.png` / **failed patch:** `pages/page-18-v2.png`

**Defect in the original (`-v1`):** The unconscious wizard lying in the Painted Room, shown in panel 2 (top-right, "Go back along the river wall...") and panel 3 (bottom-left, "Do you want to see the treasure of the Tombs of Atuan, wizard?"), does not match Ged's established design. Per `refs/ref_ged_scarred.png` and `02-CHARACTERS.md`, Ged should have DEEP RED-BROWN COPPER skin, straight BLACK hair, and four parallel whitish scars raking down the left cheek. In the original page-18 he's drawn with pale/grey skin, grey-white hair, and no visible scars — reads as a generic old man, not Ged.

**What I tried:** Cropped panel 2 (`(768,0)-(1536,512)`) and panel 3 (`(0,512)-(768,1024)`) separately, each time attaching `refs/ref_ged_scarred.png` as a second reference image alongside the crop, and asking the model to correct skin tone/hair/scars while keeping pose, clothing, dialogue, and the other character (Arha/Kossil) unchanged. Patched both back with the resize/color-match/feather method.

**Current state:** `page-18.png` = fixed full-page regeneration promoted from `page-18-v3.png`. `page-18-v2.png` = failed local patch composite that shifted skin tone but did not lock Ged's identity. `page-18-v1.png` = clean original with the wrong-looking wizard.

---

## Other Ged pages rechecked

Ged also appears on pages 15, 16, 17, 19, 20 (he enters the story at P15). These were visually rechecked during the `-v3` fix pass. Pages 15, 17, 19, and 20 read consistently as the copper-skinned, black-haired, scarred wizard. Page 16's single profile view is less explicit but not broken like the old page 18.

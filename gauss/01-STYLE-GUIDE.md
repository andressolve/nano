# 01 — STYLE GUIDE

## Style Block (paste VERBATIM into every page prompt, block 1)
> Oil-painting realism in a muted northern-German palette: candle-amber and hearth-orange interiors against cold slate-blue dawns and chalk-gray winters. Visible painterly brushwork, glazed shadows, warm rim light on faces. Cinematic composition, shallow depth where it helps, late-18th-century / early-19th-century Brunswick and Göttingen period detail. The look of a museum history painting, not an illustration.

## Register Block (block 2, verbatim)
> Oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork, cinematic lighting, muted period palette.

## Anti-drift directive (block 3, verbatim)
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition.

For any page with child Gauss, append to his lock block:
> Realistic child anatomy. NOT cute, NOT mascot proportions, NOT oversized eyes.

## Lettering treatment (the Honda formula — hold across the volume)
- **Caption boxes:** "off-white box, dark serif text, readable." Period variant for primary-source/diary pages: "ivory paper, dark serif ink." Pick the off-white box as default and hold it.
- **Hero pages (T4–T5):** full-width top band sets the moment, full-width bottom band closes it. 50–80 words each is fine.
- **Speech bubbles:** round, off-white, dark serif, tail explicitly described. Under 15 words. NO quotation marks inside bubbles — the bubble shape IS the quote.
- **Numbers and equations rendered in-image** (5050, the pairing, the 17-gon) are part of the artwork — render them large and clean, like chalk on slate or ink on ivory.
- **Lettering block opens with:** `LETTERING — verbatim, render exactly:` then each element with placement + exact quoted string.
- **Restrictions block closes every prompt:** `All words spelled correctly. Do not duplicate text. Do not invent extra captions. NO modern logos, NO watermarks, NO spurious signage.`

## In-image non-English / archaic text always gets an English helper
- Latin diary entry, German signage, the *Disquisitiones* title → small English gloss in the same panel or an adjacent caption.
- Mathematical notation (≡, the 17-gon) → a plain-English caption naming what it is.
- Ornamental text too small to read = decoration, no helper needed.

## Visual rules
- **Palette anchors the emotional arc.** Poverty/childhood = warm cramped candlelight + cold outside. Patronage = richer warm interiors, better cloth. Göttingen indecision = cold gray scholarly light. The 17-gon morning = a single shaft of dawn light (the turn). Ceres/fame = night sky, telescope, starlight.
- **The two re-enactable hooks get the cleanest, largest in-image math:** the summation pairing (P3) and the 17-gon construction (P9–P10). A child must be able to read the numbers.
- **Hands matter.** Gauss writing, drawing the compass arc, holding the slate. Anchor breakthrough pages on the hand + the mark, not on a posed portrait.
- **Period accuracy:** 1780s–1800 German dress; transition from powdered wigs/knee breeches to natural hair/high collars. Candles and oil lamps, not gaslight. Quill and slate, not pencil. No anachronisms.

## Anti-patterns
- No children's-book aesthetic (oversized eyes, pastel, rounded). No comic linework/halftones.
- No full-width date STRIP expectation (renders as a small box) — mock date bands in the HTML if needed; in-image use a caption box.
- Do not name "Gauss," "Newton," etc. inside a character lock block — the visual is the lock.
- Do not paraphrase captions/dialogue at generation time — pull verbatim from 04-SCRIPT.md.
- Do not push past T5; split a page instead.

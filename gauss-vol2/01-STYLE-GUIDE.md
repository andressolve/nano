# 01 — STYLE GUIDE

Register is identical to Book One (oil-painting realism). Hold continuity so the two
books read as one set. Only the emotional-palette arc and the re-enactable hook change.

## Style Block (paste VERBATIM into every page prompt, block 1)
> Oil-painting realism in a muted northern-German palette: candle-amber and hearth-orange interiors against cold slate-blue dawns, starlit observatory nights, and chalk-gray survey weather. Visible painterly brushwork, glazed shadows, warm rim light on faces. Cinematic composition, shallow depth where it helps, early-19th-century Brunswick, Göttingen, and Hanover-survey period detail. The look of a museum history painting, not an illustration.

## Register Block (block 2, verbatim)
> Oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork, cinematic lighting, muted period palette.

## Anti-drift directive (block 3, verbatim)
> NOT a children's book. Serious mature graphic novel, realistic proportions, natural lighting, cinematic composition.

## Lettering treatment (the Honda formula — hold across the volume)
- **Caption boxes:** "off-white box, dark serif text, readable." Period variant for the diary/letter/primary-source pages: "ivory paper, dark serif ink."
- **Hero pages (T4–T5):** full-width top band sets the moment, full-width bottom band closes it. 50–80 words each is fine.
- **Speech bubbles:** round, off-white, dark serif, tail explicitly described. Under 15 words. NO quotation marks inside bubbles — the bubble shape IS the quote.
- **Numbers, diagrams, equations rendered in-image** (the triangulation mesh, the angle marks, the baseline, the telegraph needle code) are part of the artwork — render them large and clean, like chalk on slate, ink on ivory, or surveyor's lines on a field map. A child must be able to read the triangulation numbers.
- **Lettering block opens with:** `LETTERING — verbatim, render exactly:` then each element with placement + exact quoted string.
- **Restrictions block closes every prompt:** `All words spelled correctly. Do not duplicate text. Do not invent extra captions. NO modern logos, NO watermarks, NO spurious signage.`

## In-image non-English / archaic text always gets an English helper
- Latin titles (*Theoria Motus*, *Disquisitiones generales*, *Pauca sed matura*), German signage, the Bolyai-letter Latin/German → small English gloss in the same panel or an adjacent caption.
- Mathematical notation (angle marks, the curvature idea, the ≡ from Book One if it recurs) → a plain-English caption naming what it is.
- Ornamental text too small to read = decoration, no helper needed.

## Visual rules
- **Palette anchors the emotional arc.**
  - Fame/heavens (P1–P3): deep starlit observatory blues, brass instruments, candle-amber study.
  - Love (P4, P6): warm domestic gold, soft hearth light — the only fully warm pages.
  - The Duke's death (P5): cold, smoke, battlefield gray.
  - Grief (P7): the coldest page — gray dawn, a single guttering candle, desaturated.
  - Rebuilding (P8): tentative warmth returning, muted.
  - The survey & the Earth (P9–P12): open-air daylight, green-gray Hanover hills, the heliotrope's single hot spark of reflected sun against cool distance.
  - Curvature (P13): study light, a globe, ivory diagrams.
  - The invisible / telegraph (P14–P15): night lab, copper wire, the warm glow of the first signal.
  - The private man / Bolyai (P15) and loss (P16): inward lamplight, quiet.
  - Legacy & finale (P17–P18): wide, luminous, the whole world he measured.
- **The re-enactable hook gets the cleanest, largest in-image geometry:** the triangulation page (P9) — big clear baseline, two angle arcs, a far point, drawn so a child can copy it onto paper. Do NOT crowd it.
- **Hands matter.** Gauss at the eyepiece, sighting an angle, holding the heliotrope, touching the telegraph needle. Anchor breakthrough pages on the hand + the instrument, not a posed portrait.
- **Period accuracy:** early-1800s German dress; natural hair and high collars/cravats moving through the 1820s–30s; the velvet cap only on the ~1830s older Gauss. Oil lamps, candles, brass-and-mahogany instruments, quill and ink. The Göttingen observatory is a neoclassical stone building. No anachronisms (no gaslight in interiors of the 1800s, no modern telegraph poles — the 1833 wire is bare copper strung over rooftops).

## Anti-patterns
- No children's-book aesthetic (oversized eyes, pastel, rounded). No comic linework/halftones.
- No full-width date STRIP expectation (renders as a small box) — use a caption box in-image; mock true bands in the HTML if needed.
- Do not name "Gauss," "Weber," etc. inside a character lock block — the visual is the lock.
- Do not paraphrase captions/dialogue at generation time — pull verbatim from 04-SCRIPT.md.
- Do not state a DISPUTED value as a single hard fact — use the safe phrasings in 00-PROJECT-BRIEF.md.
- Do not push past T5; split a page instead.

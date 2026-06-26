# 01 — STYLE GUIDE

## Style Block (paste VERBATIM into every page prompt)
> Oil-painting realism. NOT a comic. NO halftones, NO cel shading, NO ink linework. Painted brushwork,
> cinematic lighting, muted period palette. NOT a children's book. Serious mature graphic novel, realistic
> proportions, natural lighting, cinematic composition.

These two lines are non-negotiable (anti-drift + register). Without them the model drifts to children's-book
or ink-comic looks.

## Palette
- **Base world:** travertine and tufa grey, senatorial off-white wool, terracotta, bronze, wine-dark shadow,
  ink-brown. Late-Republican Rome — austere, stony, lamplit. NOT gilded imperial marble (that's the later empire).
- **The one accent: LAMP-GOLD** `#d4a84b` — warm oil-lamp light. It marks the *voice / the word*: it falls on
  Cicero when he speaks or writes, glows on scrolls and the Rostra. Use it sparingly and meaningfully.
- **Accent discipline (emotional control):** lamp-gold is FULL and warm through the rise (P1–P7) and the
  philosophy (P14). It DIMS / goes cold in exile (P9), the shut-out years (P12), and Tullia's death (P13). On
  the death page (P17) the gold is the cold grey dawn — the lamp is out. The finale (P18) brings the gold back,
  but now in the *scrolls*, not on the man — the word, not the speaker.

## Period accuracy (late Republic, ~80–43 BC — lock this)
- **Dress:** the **toga** is the costume and the theme (the toga = the civilian, the statesman; "let arms yield
  to the toga"). Off-white undyed wool (*toga virilis*) for citizens. As consul/curule magistrate Cicero wears
  the **toga praetexta** — off-white with a **single purple-red border stripe**. Senators wear tunics with a
  broad purple stripe (*latus clavus*). NO togas on soldiers — soldiers wear lorica (mail or muscled cuirass),
  red cloaks (*paludamentum* for generals). The toga/armour contrast is the whole visual argument.
- **Hair/beards:** late-Republican Roman men are **CLEAN-SHAVEN** with short hair. Cicero is clean-shaven on
  EVERY page (the model loves to add a philosopher's beard — block it explicitly each time). Cato may wear a
  short austere beard (he affected old-Roman/Stoic style) — but keep subtle.
- **Architecture:** Republican, not imperial. Travertine and painted stucco, Tuscan/early-Corinthian columns,
  red roof tiles, the Forum Romanum, the Curia (Senate house), the Rostra (the speaker's platform faced with
  bronze ships' prows/rams — the *rostra*). NO Colosseum (built 80 AD), NO imperial fora, NO domes.
- **Objects:** papyrus scrolls (*volumina*), wax tablets + stylus, oil lamps (*lucerna*), reed pens, ink pots,
  the curule chair (*sella curulis*), bronze braziers.

## Narration treatment (the Honda formula — default)
Narration lives INSIDE the image as caption boxes, not in the reader HTML. Keeps pages cinematic.
- **Caption box style (hold verbatim across the volume):** "aged ivory parchment box, dark serif Roman
  capitals/ink lettering, clean and readable." Period-right and matches the scroll motif.
- **Hero pages (T4–T5):** a top caption band (sets the moment) + a bottom caption band (closes it), full
  landscape width, 40–70 words each.
- **In-scene caption boxes:** small ivory boxes anchored to a stated corner (upper-left = setup, lower-right =
  resolution).
- **Speech bubbles:** round, off-white, dark serif, tail explicitly described. Under 15 words. NO quotation
  marks inside the bubble (the bubble IS the quote).
- **Verbatim block:** open the lettering section with **"LETTERING — verbatim, render exactly:"**, list each
  element with position and exact quoted string.
- **Restrictions block (close every prompt):** **"All words spelled correctly. Do not duplicate text. Do not
  invent extra captions. NO modern logos, NO watermarks, NO spurious signage."**

## In-image Latin always has an English helper (project-wide rule)
Cicero's famous Latin lines are rendered as artifacts (chiseled, on a scroll, in a bubble) WITH an English
helper in the same panel, small ivory caption directly below/beside:
- Iconic-quote pages (P5 "Quo usque tandem…", P14 word-list, P17 inscription): Latin large as the artwork, the
  English translation as a smaller caption ribbon under it.
- Latin speech bubbles get a translation caption beside the bubble.
- Ornamental Latin too small to read (background inscriptions) = decoration, no helper needed.

## Anti-patterns (text rendering)
- Do NOT paraphrase any caption/quote at generation — copy verbatim from 04-SCRIPT.md.
- Do NOT request a full-width date strip (renders as a small box) — overlay dates in the HTML reader if needed.
- Do NOT push past T5 — split or redesign.
- Do NOT leave quotation marks inside speech bubbles.

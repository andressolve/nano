# Page 32 intent-pilot — builder packet

## Role and boundary

You are the fresh zero-history builder for one real production candidate for
Page 32 of *The Count of Monte Cristo, Volume II*. Generate exactly one finished
page and submit it. You do not approve, reject, promote, or regenerate it.

Open only:

1. `qa/_pilot/page-32/INTENT.md`
2. the four image inputs listed under **Approved image inputs** below

Do not open the old Page 32 prompt, appendix, candidates, proofs, audits, critic
reports, component frames, master production plan, or any Page 33–49 packet.
Never edit `07-PAGE-CONTRACT.md` or `08-FULL-SCRIPT.md`.

Use only the built-in Codex in-app image-generation path covered by the user's
ChatGPT subscription. Do not use an API key, bundled image CLI, or API fallback.

## Generation prompt

Create one finished, flattened graphic-novel story page at exactly **1024 ×
1536, 2:3 portrait, RGB PNG**. It is a canonical production candidate, not a
prototype, mockup, exercise, component frame, or spread.

The page has two connected images in the same Chamber of Peers, seconds apart:

1. A narrower upper reaction band: ranked faces and shoulders of the assembled
   chamber turn collectively toward the sound of the great door. The reaction
   must read immediately as one room responding to one event.
2. A large lower reveal: the great door stands open and Haydée is there alone,
   full figure, framed by the doorway. The enormous crimson-and-gold chamber
   remains visibly inhabited between her and Fernand; it must not look empty.
   Haydée may be physically small within the architecture, but the composition
   belongs to her. Fernand is distant at the far end near the bar, visually
   subordinate and exposed rather than a foreground co-star.

Haydée is twenty-seven: olive-gold skin, long unbound black hair, large dark
eyes, slight build, direct unornamented stillness. She wears deep
crimson-and-gold Epirote embroidery on a loose vertical silhouette—never a
corseted French waist, coiffure, bonnet, or hat. Her color belongs naturally to
the chamber's crimson benches without making her look camouflaged.

Fernand is forty-six: heavy iron-and-black military moustache, receding black
hair with iron-grey at the sides, thick neck, heavy upright build, and the glint
of decorations. At his distance, silhouette and value separation matter more
than facial detail. He must not resemble the Count.

Render in the established **Velvet Cinema** register: layered matte gouache and
opaque watercolor over sparse charcoal and ink construction, broad visible
brushwork, bold shadow masses, tactile crimson bench baize, dark oak, aged gold,
and cold high daylight. Avoid glossy concept-art surfaces, airbrushed skin,
engraved cross-hatching, and children's-book softness.

This is a silent page. Render **no text of any kind**: no balloons, captions,
labels, title, date, sound effect, signature, or page number. Do not show the
Count, Albert, Mercédès, Beauchamp, Villefort, a second woman, or a second
Haydée. Do not make any handheld prop or tiny object a focal point.

## Approved image inputs

Attach only these four images:

1. `refs/approved/05-haydee.png` — Haydée identity and clothing.
2. `refs/approved/03-fernand-1838.png` — Fernand identity and decorations.
3. `refs/approved/19-set-chamber.png` — chamber architecture, tiers, and door.
4. `pages/page-31.png` — canonical predecessor; same room, palette, light, hour,
   and Fernand position.

The objects sheet is not an authorized input. All other reference sheets and
story pages are prohibited inputs.

## Output paths

Write exactly:

- candidate: `qa/production/page-32/intent-pilot/candidate.png`
- issued prompt: `qa/production/page-32/intent-pilot/issued-prompt.md`
- builder audit: `qa/production/page-32/intent-pilot/builder-audit.md`
- desktop proof: `qa/production/page-32/intent-pilot/desktop-600x900.png`
- tablet proof: `qa/production/page-32/intent-pilot/tablet-768x1152.png`

If any output path already exists, stop without overwriting it.

## Builder audit contract

The audit is a report, never a gate. Keep it under 180 words and use exactly
these headings:

```text
## Intent read
[From the 600 × 900 proof alone, state what happens and who owns the page.]

## Technical facts
- Canvas: [dimensions and mode]
- Visible text: [NONE, or list what you can read]
- Obvious integrity issues: [NONE, or concise observations]

## Prompt variances observed
[Concise observations, or NONE. Variance does not authorize regeneration.]

## Submission
SUBMITTED TO INDEPENDENT CRITIC
```

Submit every completed, correctly sized, non-corrupt candidate even if the
audit identifies a likely story or prompt problem. Regeneration without a
critic verdict is allowed only if generation itself failed: wrong canvas,
corrupt or truncated output, or gross anatomical breakage. Preserve evidence of
such a failure and stop; this pilot authorizes only one successful generation.

Return only the five output paths, candidate dimensions/mode, and file hashes.

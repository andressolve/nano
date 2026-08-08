# Page 21 — Builder Self-Audit

## Status

**BUILDER CANDIDATE ONLY — NOT CRITIC-APPROVED AND NOT CANONICAL.**

No file under `monte-cristo-expanded/pages/` was created, overwritten, or
promoted. The review reader was not edited.

## Candidate history

- `page-21-v1.png` — correct 1024 × 1536 portrait render with exact readable
  image text, strong four-stage continuous-time Edmond progression, and good
  prison/style continuity. Builder rejected it because the distant jailer was
  duplicated in two doorway slices.
- `page-21-v2.png` — complete full-page regeneration. The duplicated lower
  doorway and second jailer are removed. This is the builder's preferred
  candidate for independent criticism.

## v2 checks

### Script fidelity

- One stable prose field contains the full Page 21 prose once, in the approved
  order.
- Full-size visual transcription found no missing, substituted, duplicated, or
  malformed word; `Mercédès` retains its accent and all sentence punctuation
  is present.
- The only speech text is `No one is coming.` exactly once.
- No title, page number, speaker label, watermark, production note, or other
  readable story text appears.
- Four successive Edmond figures are present in one continuous cell.
- Exactly one distant silent jailer appears once.
- The bottom consequence strip contains the untouched bowl and bread in
  silence.

### Dimensions and readability

- Source file reports 1024 × 1536 RGB PNG.
- A temporary 390 × 585 reader proof was inspected without zoom. The complete
  prose and balloon remain readable in one normal top-to-bottom pass.
- Prose sits in one protected parchment field and does not cover a face, hand,
  petition, wall scratch, doorway, or bowl.
- The one balloon remains inside the page safe area and points toward the
  latest Edmond; no silent figure receives a balloon or orphan tail.

### Identity and continuity

- The four appearances preserve Edmond's long clean nose, strong brow,
  high-cheekboned face, dark eyes, black hair, and shared facial geometry.
- Age/time progression is legible: nearly clean-shaven and upright; early beard
  while writing; gaunt and rough-bearded among abandoned petitions; long-haired,
  deeply gaunt, rag-clothed final figure.
- The earliest figure continues accepted Page 19's face and indigo/white
  costume. The final figure converges on the locked Prison Edmond reference.
- The one jailer is small, bald-crowned, barrel-bodied, rust-brown, key-bearing,
  and clearly separate from Edmond.
- No Faria-like white hair, Jacopo/Caderousse collision, or unrelated generic
  prisoner face is present.

### Style, composition, and anatomy

- The page uses the accepted mineral gray, damp brown, rust, black-green, weak
  amber, and cold-light prison palette.
- The surface reads as matte gouache/opaque watercolor with visible painted
  texture, not glossy game art or smooth photographic realism.
- The descending figures, increasing scratches, growing paper accumulation,
  deteriorating clothes, and lowered posture make elapsed years legible before
  all prose is read.
- The latest Edmond's extended open hand reads as refusal/pushing away; the
  separate silent bowl supplies the final consequence. Independent criticism
  should still test whether this action is sufficiently unmistakable at first
  read.
- Visible hands and limbs appear anatomically credible; no duplicated limb or
  obvious extra/missing finger was found.

## Residual critic checks

- Confirm the speech balloon's serif-leaning letterform is close enough to the
  accepted Pages 3–5 and 7–10 hand-lettered serif/sans family; it is fully
  readable but slightly closer to the prose face than Page 10's speech face.
- Confirm the balloon tail terminates close enough to the latest Edmond's mouth
  and cannot be read as belonging to the earlier figure above.
- Confirm the extended hand plus isolated bowl makes `pushed away his food`
  effortless rather than merely recoverable.
- Confirm four repeated Edmond figures read immediately as continuous time,
  not simultaneous cellmates.

## Generation path and prompts

- Built-in subscription-backed Codex ImageGen only; no API key, CLI, or
  separately billed API path was used.
- v1 prompt: `page-21-v1-generation-prompt.md`
- v2 prompt: `page-21-v2-generation-prompt.md`

## Reference inputs

v1 used the tool's five-input maximum:

1. `monte-cristo/refs/02-edmond-prison.png`
2. accepted `monte-cristo-expanded/pages/page-05.png`
3. accepted `monte-cristo-expanded/pages/page-08.png`
4. accepted `monte-cristo-expanded/pages/page-10.png`
5. accepted `monte-cristo-expanded/pages/page-19.png`

v2 used:

1. `page-21-v1.png` as composition evidence only
2. `monte-cristo/refs/02-edmond-prison.png`
3. accepted `monte-cristo-expanded/pages/page-08.png`
4. accepted `monte-cristo-expanded/pages/page-10.png`
5. accepted `monte-cristo-expanded/pages/page-19.png`

Before prompt construction, the builder also inspected the complete accepted
Pages 11–20 sequence at source size. The five-image tool limit required using
Page 19 as the strongest direct prison-continuity attachment.

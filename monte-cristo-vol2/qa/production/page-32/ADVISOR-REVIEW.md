# Page 32 — Independent Visual-Production Advisory

**Scope reviewed:** all five Page 32 prompts, full-resolution candidates, 600 × 900 proofs, and critic reports v1–v5, with the approved Haydée, Fernand, chamber, and object references and canonical Page 31 used for continuity comparison.

## Decision

**Best generation: v4.** It is the strongest production base in the sense of solved visual problems, but it is not promotable and should not be crop-patched into a final page without explicit owner authorization.

V4 is the only candidate that resolves the hardest lower-panel requirements together:

- Haydée is a single figure, recognizably close to her approved face, hair, slight build, crimson-and-gold Epirote silhouette, and direct stillness.
- The folded paper is unmistakably connected to her hand, and the red wax seal remains conspicuous at the 600 × 900 proof.
- Fernand is reduced to a small distant black figure at the far bar. He does not become a readable portrait or a competing foreground presence.
- There is no separate Count-like black vertical in the foreground or midground.
- The page has exactly two panels, a clear 30/70 hierarchy, zero strings, strong crimson/gold continuity, and sound basic anatomy and rendering.

Its central failure is decisive: Haydée fills roughly half the lower panel and is staged at a near threshold between giant door leaves. This changes the story from “a small solitary woman commands an enormous chamber” into “a heroic full-length portrait enters the room.” The chamber is visible behind her, but it no longer supplies the intended scale, distance, or spectacle.

I also find one exact-compliance weakness understated by critic v4: the top-panel crowd does not share one literal screen-direction gaze vector. The left mass looks screen-right and the right mass looks screen-left, converging toward the center. This communicates collective attention toward the door, but it does not meet the stricter one-vector requirement later made explicit in v5. V4 is therefore best, but not a one-correction page.

### Comparative assessment

- **V1:** Strong architectural depth and a suitably small doorway Haydée, but Fernand becomes the largest lower-panel figure in the immediate foreground. The crowd gaze is mixed, and the seal disappears at proof scale. Haydée is recognizable mainly through costume and silhouette. Useful evidence for room depth, not a usable production base.
- **V2:** Best large-scale Haydée identity after v4 and an excellent readable document/seal, but she is in the chamber rather than isolated in the doorway, while Fernand is a prominent readable man directly behind her. The top crowd converges from both sides rather than sharing one screen vector. It reverses the required scale hierarchy.
- **V3:** Best literal one-direction crowd turn and a strong small-Haydée/vast-room ratio. However, the central black-coated man is a dominant Count-like false positive and cannot read as tiny far-end Fernand; the document and seal are not legible. Haydée is too small for facial identity to be assessed, though her color/silhouette work.
- **V4:** Best combined identity, object, Fernand, figure-count, and false-positive control. It fails the central scale/staging beat and the strict screen-vector reading of the crowd.
- **V5:** Best architectural scale and elevated establishing composition, but it duplicates Haydée, puts a conspicuous Count-like black man at the central bar, loses the document/seal, and again splits the crowd gaze. Its architecture is useful as design evidence only; four interacting story failures make it a poor literal base.

At the intended distance, Fernand should not be identifiable by face. Correct identity is therefore a placement-and-silhouette test: far-bar anchoring, heavy compact outline, moustache mass if visible, and a minute decoration glint. V4 handles that functional identity best. V1–v3 make the black figure too large and narratively ambiguous; v5 makes it conspicuous and Count-like.

## Ranked courses of action

### 1. Generate the two final panels separately, then assemble a single flattened page in code — **recommended**

Treat both panels as canonical production components, not prototypes. Generate a fresh top panel whose only human problem is the unanimous screen-right crowd vector. Generate a fresh lower panel whose only human figures are one small doorway Haydée and one minute, bar-occluded Fernand. Assemble them with a fixed white gutter into one 1024 × 1536 RGB PNG, then submit the assembled page—not merely the components—to a fresh independent critic at native, 600 × 900, and 768 × 1152 sizes.

**Why this is most promising:** the five whole-page attempts show interference between unrelated instructions. Solving the seal tends to enlarge Haydée; solving the room scale tends to duplicate her or invent a central black figure; solving the crowd adds another mass-figure problem to the same generation. Separating the panels removes the crowd from the already difficult architectural tableau and gives the lower panel the full prompt budget and reference attention.

**Tradeoffs:** independently generated panels may drift in brushwork, contrast, daylight, architecture, lens height, and crimson value. A code-assembled page is not byte-for-byte a single generator output, so the owner must explicitly authorize this production architecture after the page exceeded the normal version ceiling. Both components and the final composite need an evidence trail and independent review.

### 2. Authorize one more fresh whole-page generation using a short, hierarchy-first prompt

Use only the approved references and canonical Page 31; do not attach or feed any rejected Page 32 candidate. Keep the prompt shorter than v5 and prioritize four non-negotiable visual facts: one-direction crowd; one small doorway Haydée; one tiny bar-occluded Fernand; one high-chroma seal. Describe the lower panel as a chamber establishing shot with two tiny figures, not as a Haydée portrait with many negative prohibitions.

**Tradeoffs:** this preserves the established one-generation/one-page topology and gives the best chance of seamless style. However, v5 demonstrates that even an unusually explicit prompt could satisfy the room scale while violating figure count, Fernand, seal, and gaze. The probability of another coupled regression is materially higher than with separated panels.

### 3. Accept v4 by explicit owner tolerance

V4 is visually accomplished and carries the correct identities, object, color rhyme, zero-text state, and Fernand/Count separation. If schedule risk outweighs exact staging, it is the least-bad existing page.

**Tradeoffs:** this would waive the page's dominant dramatic idea, not a cosmetic preference. It would also tolerate a converging rather than literal one-direction crowd gaze. Because Page 32 is the reveal that controls Page 33's continuity, this compromise would propagate a near, heroic Haydée scale into the next page. I do not recommend it.

## Separate-panel generation and code assembly

### What it would solve

- It isolates the crowd-gaze problem from the doorway tableau.
- It lets the lower-panel generator devote its composition to architectural distance, exact figure count, and exclusion of human-shaped black foreground forms.
- It makes the seal-vs-scale conflict more tractable: the lower panel can use a simple pale packet and one saturated red disk without also rendering hundreds of faces.
- It permits deterministic control of the 30/70 split, gutter, final canvas dimensions, color mode, and proof derivation.

### What it could break

- The two panels may look as though they come from different paintings: inconsistent grain, palette, edge treatment, black level, or daylight.
- The hall may not feel like the same continuous room if architectural motifs, bench geometry, or camera orientation conflict.
- Separately generated edges can make the gutter feel mechanically imposed rather than naturally composed.
- If existing rejected candidates are cropped and recombined, the evidence chain becomes ambiguous and the result risks becoming a patchwork repair of rejected art. Fresh production components are cleaner.
- Future pages may inherit an assembled image whose internal continuity is less coherent than a single generation, so Page 33 should reference the final flattened composite only after approval.

### Standing-rule compliance

For Page 32, the method can comply cleanly because the page has **zero strings**. Code would perform layout only: scale/crop approved final panel rasters, place them on the fixed canvas, add the gutter, flatten, and export. It would add no dialogue, captions, tails, document lettering, figures, seals, paint, or story information.

For pages that contain text, panel-level generation can still comply only if every balloon, caption, tail, and exact string is natively rendered inside its generated panel before assembly. Code may position already-lettered panel pixels, but it must never add, replace, correct, or overlay lettering. The final reader continues to display a single finished flattened page and remains only a navigation/quiz surface; it is not a lettering layer.

This is compatible with the spirit of the baked-lettering and reader rules, but it is a process exception to the current complete-page candidate topology. Because the normal v4 ceiling has already been exceeded, it requires an explicit owner decision before any new generation. It should not be treated as authorization to adopt post-hoc panel patching generally.

### Workable architecture

1. **Owner authorization and version reset for method only:** authorize one Page 32 component-assembly round, without changing the protected page contract or script.
2. **Locked geometry:** define exact pixel rectangles for top panel, gutter, and lower panel on the 1024 × 1536 canvas before generation.
3. **Fresh Panel A production candidate:** crowd only, same chamber material/light, ranked heads and shoulders, every nose/chin/eye vector screen-right, no central doorway focal point, no text.
4. **Fresh Panel B production candidate:** remote elevated chamber view, exactly one small Haydée enclosed in the complete distant doorway, exactly one minute bar-occluded Fernand, no other human vertical, pale packet and saturated red seal readable at the eventual 600 × 900 page proof, no text.
5. **Shared visual locks:** both prompts use the approved chamber reference and canonical Page 31; Panel B additionally uses Haydée, Fernand, and object references. Use the same medium, daylight, crimson value, black level, and edge-language paragraph in both prompts.
6. **Component QA:** reject only failed generations before assembly; otherwise have fresh critics review each component against its limited contract. Do not use v1–v5 as generation references.
7. **Deterministic assembly:** fit the two approved component rasters into the locked rectangles without content-aware edits; add only the fixed gutter; flatten to one 1024 × 1536 RGB PNG.
8. **Whole-page gate:** a fresh critic reviews the composite for story, figure count, scale, gaze, seal, Fernand, false positives, style cohesion, and reduced-size readability. Promotion, if approved, is of the exact composite bytes.

An even safer variant is to generate each component at its final aspect ratio and at or above its final pixel dimensions, avoiding aggressive crops. The lower panel should be judged from a proof of the **assembled page**, because a seal readable in an isolated panel may disappear after page-scale reduction.

## Immediate next step

**Stop further whole-page retries and ask the owner to authorize Course 1: one fresh two-component production round with deterministic flattened assembly and a fresh whole-page critic.** Do not promote or patch v4, do not use any rejected candidate as a generation input, and do not modify the script or page contract. Use v4 only as evidence of the successful lower-panel locks—Haydée identity, readable sealed document, tiny Fernand, and absence of a Count-like foreground man—while rebuilding both panels as fresh canonical production components.

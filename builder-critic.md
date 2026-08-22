# Builder/critic production method — compatibility pointer

The active builder/critic method now lives in the specialized Dialogue Studio:

- [`dialogue/PLAYBOOK.md`](dialogue/PLAYBOOK.md)
- [`dialogue/PROMPTING.md`](dialogue/PROMPTING.md)
- [`dialogue/templates/roles/`](dialogue/templates/roles/)
- [`dialogue/templates/gates/`](dialogue/templates/gates/)
- [`dialogue/tools/`](dialogue/tools/)

The old prompt-visible critic construction is superseded. A page critic now
blind-reads a version-neutral candidate/proof capsule and then receives only
the exact script, reader intent, and numbered critic card. It never receives
the generation prompt or builder audit.

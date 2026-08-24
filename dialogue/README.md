# Dialogue studio

For a new work, start at `NEW-WORK.md`; a title and source location are enough.
`AUDIENCE.md` supplies the default reader profile. `ADAPTATION.md` governs
bounded research, audience-first adaptation, graphical direction, the two-stage
audience critic, and owner greenlight. Research is evidence, not a completeness
mandate. The target is ultra-premium storytelling for the named readers.

`PREPRODUCTION.md` generalizes the proven Monte Cristo Volume II preparation
system: production-complete panel scripts, whole-script readability, page
contracts, intent/prompt/card siblings, casting/reference approval, two
non-transitive owner decisions, deterministic gates, context limits, and a
hash-bound handoff.

After both gates and the second owner approval, start production at
`works/<project>/SESSION-START.md`. From that directory the framework is
reached as `../../PLAYBOOK.md`, `../../PROMPTING.md`, and `../../tools/`.
`PLAYBOOK.md` governs production; `PROMPTING.md` governs builder-only prompt
writing.

`templates/project/` is the project skeleton. `templates/research/`,
`templates/adaptation/`, and `templates/preproduction/` hold the upstream
artifacts. `templates/roles/` and
`templates/gates/` contain executable role and gate packets. `tools/` performs
only initialization and mechanical readiness, assembly, preflight, report,
candidate, and retry checks. `check_adaptation.py` opens reference
preparation; only `check_preproduction.py` opens story-page production.
`case-studies/` is evidence, never authority.

The transport invariant is simple: a critic sees a neutral candidate/proof capsule, then exact script + page intent + numbered card. It never sees a generation prompt, builder audit, references, version, or history.

# Start a new Dialogue Studio work

A fresh task launched from `dialogue/` needs only the work title and available
source location. Read `AGENTS.md`, `AUDIENCE.md`, `ADAPTATION.md`, and
`PREPRODUCTION.md`, then initialize the project:

```sh
python3 -B tools/init_project.py PROJECT-SLUG --name "Project Name"
```

Move into `works/PROJECT-SLUG/` and follow its `NEW-WORK.md`. Conduct bounded
research, adaptation, and paper pre-production only. Do not generate
references, style explorations, story pages, or prototypes before the story
greenlight. A clean `tools/check_adaptation.py` result opens bounded reference
preparation only. Do not open page production until reference/casting approval,
complete page packets, context and handoff records, a second owner production
approval, and `tools/check_preproduction.py` all pass.

The compact user prompt is sufficient:

> Start a new Dialogue Studio work: TITLE. Source material: PATH OR DESCRIPTION.

Do not ask the user to restate the studio workflow already stored here.

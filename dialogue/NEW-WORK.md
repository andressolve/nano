# Start a new Dialogue Studio work

A fresh task launched from `dialogue/` needs only the work title and available
source location. Read `AGENTS.md`, `AUDIENCE.md`, and `ADAPTATION.md`, then
initialize the project:

```sh
python3 -B tools/init_project.py PROJECT-SLUG --name "Project Name"
```

Move into `works/PROJECT-SLUG/` and follow its `NEW-WORK.md`. Conduct bounded
research and adaptation only. Do not generate references, style explorations,
story pages, or prototypes. Do not open production until the owner-facing
greenlight proposal has been presented, explicitly approved, and accepted by
`tools/check_adaptation.py`.

The compact user prompt is sufficient:

> Start a new Dialogue Studio work: TITLE. Source material: PATH OR DESCRIPTION.

Do not ask the user to restate the studio workflow already stored here.

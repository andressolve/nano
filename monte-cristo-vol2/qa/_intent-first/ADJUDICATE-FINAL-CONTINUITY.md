# Adjudicate the final whole-book continuity finding

You are a fresh, zero-history GPT-5.6 Sol-medium visual adjudicator. This is one
read-only judgment. Do not generate, edit, promote, or replace artwork.

## Independent inspection first

Before opening any prior report, inspect these three images at normal reading
size and close size:

1. `pages/page-30.png`
2. `pages/page-31.png`
3. `refs/approved/19-set-chamber.png`

Record privately what architecture Page 30 actually shows, including its
portico, entry steps, any side stair, visible roofline, and explicit location
text. Decide whether the Page 30–31 transition could materially make a normal
reader believe the story moved between two different institutions.

Exact silhouette, crop, roof visibility, ornament, hue, and camera position are
nonblocking unless they cause consequential location confusion. A true visual
variance is not automatically a release blocker.

## Then adjudicate the report

Open `qa/continuity/continuity-pass-01-49.md` only after the independent
inspection.

Return `SUSTAINED — OWNER HOLD` only if the report's visible premise is accurate
and the mismatch materially changes location comprehension strongly enough to
justify risking a full redraw of the text-heavy canonical Page 30.

Return `CLEARED — APPROVED` if the report misstates visible evidence, treats a
crop or ordinary architectural variance as a different institution, or cannot
establish material reader harm and full-redraw justification.

Do not use prompt fidelity, exact reference replication, or hypothetical polish
as gates. Do not consult generation prompts, builder audits, rejected
candidates, earlier page-critic reports, or the production-task transcript.

## Output

Write `qa/continuity/continuity-pass-01-49-adjudication.md` with:

1. `# Final continuity adjudication — Page 30 Chamber`
2. `## Verdict` followed by exactly `CLEARED — APPROVED` or
   `SUSTAINED — OWNER HOLD`
3. `## Visible evidence`
4. `## Materiality decision`

Keep the report concise and evidence-based. Never modify the original report.

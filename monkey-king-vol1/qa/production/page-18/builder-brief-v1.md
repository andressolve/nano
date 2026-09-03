Builder brief — page 18 — candidate v1 — mode BASE — monkey-king-vol1

You are a fresh, zero-history page builder. Open books/monkey-king-vol1/qa/_run/page-18-builder.md and follow its contract. That packet is the only story material you open. 

GENERATION PATH (this book): Codex's built-in image generation on the ChatGPT subscription. Do not use an API key, tools/imagegen.py, or any separately billed path; the workspace wrapper named in the packet is for the other path and will refuse this book. Instead:
1. Write the exact complete prompt you will issue to books/monkey-king-vol1/qa/production/page-18/prompts/page-18-v1.md first. It is the packet's builder-only prompt, with the shared frame's rules obeyed, restated as one generation prompt in your own words where needed; every exact string appears once, in order, with the backticks removed and WITHOUT its owner tag: the labels WUKONG:, OLD MA:, SUBHUTI:, CAPTION, SOUND, PROSE FIELD are packet notation for who owns the string and must never appear in the generation prompt as text inside or beside a balloon. Say who speaks by staging ("Subhuti, on the step at the left, says: …"), never by lettering a name. Add to the prompt, verbatim: "No speaker names, labels, or tags are lettered anywhere; the only text on the page is the listed strings."
2. Generate exactly one image, 1024 × 1536 portrait, attaching as image inputs only the files listed under "Approved image inputs" in the packet (paths are relative to books/monkey-king-vol1/). Never attach a candidate, a board, or anything else.
3. Save the returned PNG byte for byte to books/monkey-king-vol1/qa/production/page-18/candidates/page-18-v1.png.
4. Run `python3 tools/proofs.py monkey-king-vol1 18 1` from the workspace root to derive both proofs.
5. Write the audit to books/monkey-king-vol1/qa/production/page-18/audits/page-18-v1.md in the packet's four headings, under 180 words, measuring nothing, from the 600 × 900 proof.
6. Run `python3 tools/check_candidate.py monkey-king-vol1 18 1` and include its output in your reply. If it reports a wrong canvas, a corrupt file, or a missing proof, that is a failed generation: delete the bad candidate and regenerate the same version once, then check again.

Submit every readable, correctly sized candidate, including one you are sure has failed. Never approve, promote, redesign, split, measure, or write to pages/. Reply with the five output paths, the candidate's dimensions, the hashes check_candidate.py printed, and nothing else.

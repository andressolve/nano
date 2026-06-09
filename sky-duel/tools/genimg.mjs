#!/usr/bin/env node
// Direct gpt-image-2 caller for sky-duel (openai-image-2 MCP not registered in this session).
// Same key + model as the MCP; standard mode only (no reasoning param).
// Usage:
//   node genimg.mjs gen  --prompt-file p.txt --out out.png [--size 1536x1024] [--quality high]
//   node genimg.mjs edit --prompt-file p.txt --image ref.png --out out.png [--size 1536x1024]

import { readFile, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import path from "node:path";

const args = process.argv.slice(2);
const mode = args[0];
const opt = {};
for (let i = 1; i < args.length; i += 2) opt[args[i].replace(/^--/, "")] = args[i + 1];

const cfg = JSON.parse(await readFile(path.join(homedir(), ".claude.json"), "utf8"));
const env = cfg.projects["/Users/andresrodriguez/Documents/nano"].mcpServers["openai-image-2"].env;
const API_KEY = env.OPENAI_API_KEY;
const MODEL = env.OPENAI_IMAGE_MODEL || "gpt-image-2";

const prompt = await readFile(opt["prompt-file"], "utf8");
const size = opt.size || "1536x1024";
const quality = opt.quality || "high";

let res;
if (mode === "gen") {
  res = await fetch("https://api.openai.com/v1/images/generations", {
    method: "POST",
    headers: { Authorization: `Bearer ${API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ model: MODEL, prompt, size, quality, n: 1 }),
  });
} else if (mode === "edit") {
  const buf = await readFile(opt.image);
  const ext = path.extname(opt.image).slice(1).toLowerCase() || "png";
  const mime = ext === "jpg" || ext === "jpeg" ? "image/jpeg" : `image/${ext}`;
  const form = new FormData();
  form.append("model", MODEL);
  form.append("prompt", prompt);
  form.append("size", size);
  form.append("quality", quality);
  form.append("image", new Blob([buf], { type: mime }), path.basename(opt.image));
  res = await fetch("https://api.openai.com/v1/images/edits", {
    method: "POST",
    headers: { Authorization: `Bearer ${API_KEY}` },
    body: form,
  });
} else {
  console.error("mode must be gen|edit");
  process.exit(1);
}

if (!res.ok) {
  console.error(`API error ${res.status}: ${(await res.text()).slice(0, 800)}`);
  process.exit(1);
}
const json = await res.json();
const b64 = json.data?.[0]?.b64_json;
if (!b64) {
  console.error("No image in response:", JSON.stringify(json).slice(0, 500));
  process.exit(1);
}
await writeFile(opt.out, Buffer.from(b64, "base64"));
console.log(`saved ${opt.out}`);

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(
  scriptDir,
  "sources",
  "monte-cristo-gutenberg-en.txt",
);
const outputPath = path.join(scriptDir, "CHAPTER-MAP.md");

const source = fs.readFileSync(sourcePath, "utf8").replace(/\r\n?/g, "\n");
const headingPattern = /^[ \t]*Chapter (\d+)\.\s+(.+)$/gm;
const headingsByNumber = new Map();

for (const match of source.matchAll(headingPattern)) {
  const number = Number(match[1]);
  if (number >= 1 && number <= 117) {
    headingsByNumber.set(number, {
      number,
      title: match[2].trim(),
      start: match.index,
      bodyStart: match.index + match[0].length,
    });
  }
}

if (headingsByNumber.size !== 117) {
  throw new Error(`Expected 117 chapters, found ${headingsByNumber.size}`);
}

const chapters = [...headingsByNumber.values()].sort((a, b) => a.number - b.number);
for (let index = 0; index < chapters.length; index += 1) {
  const chapter = chapters[index];
  const end = chapters[index + 1]?.start ?? source.length;
  const body = source.slice(chapter.bodyStart, end);
  chapter.words = (body.match(/\b[\p{L}\p{N}’'-]+\b/gu) ?? []).length;
}

const volumeForChapter = (number) => {
  if (number <= 30) return "I";
  if (number <= 56) return "II";
  if (number <= 83) return "III";
  if (number <= 103) return "IV";
  return "V";
};

const volumeNames = {
  I: "Edmond",
  II: "The Return",
  III: "The Web",
  IV: "Judgment",
  V: "Providence",
};

const volumeRows = Object.keys(volumeNames).map((roman) => {
  const included = chapters.filter((chapter) => volumeForChapter(chapter.number) === roman);
  return {
    roman,
    name: volumeNames[roman],
    start: included[0].number,
    end: included.at(-1).number,
    chapters: included.length,
    words: included.reduce((sum, chapter) => sum + chapter.words, 0),
  };
});

const output = [
  "# The Count of Monte Cristo — Chapter Map",
  "",
  "Mechanical map of the public-domain Project Gutenberg English text. Word",
  "counts are directional, not editorially authoritative. The Robin Buss Penguin",
  "Classics edition remains the preferred complete working English text for close",
  "reading; no Buss text is stored in this repository.",
  "",
  "## Working Five-Volume Distribution",
  "",
  "| Volume | Working title | Source chapters | Chapters | Approx. words |",
  "| --- | --- | ---: | ---: | ---: |",
  ...volumeRows.map(
    (volume) =>
      `| ${volume.roman} | ${volume.name} | ${volume.start}–${volume.end} | ${volume.chapters} | ${volume.words.toLocaleString("en-US")} |`,
  ),
  "",
  "## Full Chapter Index",
  "",
  "| Ch. | Source title | Approx. words | Working volume |",
  "| ---: | --- | ---: | :---: |",
  ...chapters.map(
    (chapter) =>
      `| ${chapter.number} | ${chapter.title.replace(/\|/g, "\\|")} | ${chapter.words.toLocaleString("en-US")} | ${volumeForChapter(chapter.number)} |`,
  ),
  "",
].join("\n");

fs.writeFileSync(outputPath, output);

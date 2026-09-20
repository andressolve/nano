"""Emit qa/_assembly/parts/mov-N-{intents,prompts,cards}.md from a movement module.

Each movement module defines MOV (int) and PAGES: {n: dict(title, intent, turn,
moments=[...], locks, exclusions, inputs=[...], card=[(title, body), ...])}.
The exact-strings section is generated from the script parser so no string is
ever retyped by hand.
"""
import importlib, sys
sys.path.insert(0, '/Users/andresrodriguez/Documents/monte_inspired/tools')
from common import parse_script

BOOK = '/Users/andresrodriguez/Documents/monte_inspired/books/three-musketeers-vol1/'
pages = parse_script(open(BOOK + '08-FULL-SCRIPT.md').read())


def strings_block(n):
    lines = []
    count = 0
    for s in pages[n].strings:
        if s.kind == 'prose' or s.owner == 'TITLE CARD':
            for para in s.text.split('  '):
                lines.append(f"{s.owner}: `{para.strip()}`")
                count += 1
        else:
            lines.append(f"{s.owner}: `{s.text}`")
            count += 1
    return "\n".join(lines), count


def emit(mod):
    m = importlib.import_module(mod)
    P = m.PAGES
    intents, prompts, cards = [], [], []
    for n in sorted(P):
        d = P[n]
        intents.append(f"## PAGE {n}\n\n{d['intent'].strip()}\n")
        sb, count = strings_block(n)
        moments = "\n".join(f"{i+1}. {t}" for i, t in enumerate(d['moments']))
        inputs = "\n".join(f"{i+1}. `{p}`" for i, p in enumerate(d['inputs']))
        obj = d.get('object_text', '')
        close = (f"Render exactly these {count} strings once each, in this order, with clear ownership; "
                 f"no other text anywhere on the page." + (f" {obj}" if obj else ""))
        prompts.append(
            f"## PAGE {n} — {d['title']}\n\n### Reader turn\n{d['turn'].strip()}\n\n"
            f"### Ordered moments\n{moments}\n\n### Exact strings\n{sb}\n\n{close}\n\n"
            f"### Character locks\n{d['locks'].strip()}\n\n### Consequential exclusions\n{d['exclusions'].strip()}\n\n"
            f"### Approved image inputs\n{inputs}\n\nAttach only these images.\n")
        crit = "\n\n".join(f"### C{i+1} — {t}\n{b.strip()}" for i, (t, b) in enumerate(d['card']))
        cards.append(f"## Page {n} — card\n\n{crit}\n")
    out = BOOK + 'qa/_assembly/parts/'
    open(out + f'mov-{m.MOV}-intents.md', 'w').write("\n".join(intents))
    open(out + f'mov-{m.MOV}-prompts.md', 'w').write("\n".join(prompts))
    open(out + f'mov-{m.MOV}-cards.md', 'w').write("\n".join(cards))
    print(f"mov-{m.MOV}: pages {sorted(P)}")


if __name__ == '__main__':
    import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    for mod in sys.argv[1:]:
        emit(mod)

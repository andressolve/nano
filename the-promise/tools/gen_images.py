"""Generate the painted supporting images for "The Promise".

Uses the same gpt-image-2 endpoint and key as the project's openai-image-2 MCP
server. Images here are SUPPORTING only - no image in this essay carries a
numeral or any load-bearing notation. That is the plates' job.
"""

import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images")
os.makedirs(OUT, exist_ok=True)

cfg = json.load(open(os.path.expanduser("~/.claude.json")))
env = cfg["projects"]["/Users/andresrodriguez/Documents/nano"]["mcpServers"]["openai-image-2"]["env"]
KEY = env["OPENAI_API_KEY"]
MODEL = env.get("OPENAI_IMAGE_MODEL", "gpt-image-2")

STYLE = (
    "Painted illustration for a serious book of ideas, in the manner of a fine oil study. "
    "Warm parchment, ink-brown and stone palette with restrained lapis-blue and vermillion accents only. "
    "Soft directional light, painterly realism, museum quality, muted and unsaturated. "
    "Quiet, still, contemplative. "
    "NOT a children's book: no cartoon styling, no cute rounded shapes, no bright saturated colour, no soft focus glow. "
    "Absolutely NO text, NO lettering, NO numerals, NO signage, NO labels anywhere in the image."
)

GEOMETRY = (
    "The figure is EUCLID'S PROPOSITION I.1 and nothing else: TWO circles of equal size, "
    "overlapping so that each one's edge passes through the other's centre, plus THREE straight "
    "lines joining the two centres to the upper point where the circles cross, forming one "
    "equilateral triangle. That is the entire figure. "
    "CRITICAL: absolutely NO star shape of any kind - no five-pointed star, no six-pointed star, "
    "no pentagram, no hexagram, no pentagon, no star polygon, no interlaced or woven lines, "
    "no rays radiating from a centre, no wheel or spoke pattern, no zodiac or occult sigil. "
    "It must read as a plain schoolroom geometry construction, not as a magic symbol. "
    "Thin, even, precise lines. No writing, no letters, no numerals anywhere on it."
)

SCENES = {
    "cover-v2.png": (
        "A plain wooden writing table at dusk, lit by a single oil lamp from the left. "
        "On the table a single sheet of pale paper bearing one faint geometric construction drawn in ink. "
        + GEOMETRY +
        " Beside the sheet a bronze stylus and a pair of brass dividers. "
        "Beyond the pool of lamplight the room falls away into deep warm darkness. "
        "The sheet of paper is the brightest thing in the frame, as though it matters more than the room."
    ),
    "image-survives-v2.png": (
        "A ruined classical courtyard in late afternoon light. Cracked marble flagstones with weeds pushing "
        "through the joints, broken column drums lying where they fell, a collapsed architrave. Long golden "
        "shadows. In the foreground ONE large intact unbroken flagstone, free of cracks, and scratched into "
        "that single stone - still crisp and sharp and undamaged - a small geometric figure. "
        + GEOMETRY +
        " The figure sits wholly within that one uncracked stone and does not cross any joint. "
        "The building has failed completely; the scratched figure has not aged at all."
    ),
    "cover.png": (
        "A plain wooden writing table at dusk, lit by a single oil lamp from the left. "
        "On the table a single sheet of pale paper bearing a faint geometric construction drawn in ink "
        "- straight lines and one circle, pure geometry, indistinct, containing no writing and no numbers. "
        "Beside it a bronze stylus and a pair of brass dividers. "
        "Beyond the pool of lamplight the room falls away into deep warm darkness. "
        "The sheet of paper is the brightest thing in the frame, as though it matters more than the room."
    ),
    "image-ledger.png": (
        "A night watchman's ledger lying open on a cold stone window sill. Its ruled columns are filled with "
        "hundreds of short repetitive handwritten entries in faded iron-gall ink - the handwriting is seen at a "
        "shallow angle, indistinct and completely illegible, no readable words or figures. The earliest pages are "
        "browned with age. Through the window behind it, the first cold grey light of dawn over tiled rooftops. "
        "A guttering candle stub has burned almost to nothing. A record kept faithfully for a very long time."
    ),
    "image-ledgers.png": (
        "The interior of an enormous archive. Identical leather-bound ledgers packed on tall wooden shelves that "
        "recede into darkness in both directions with no end visible anywhere in frame. A single oil lamp on a "
        "reading desk in the foreground lights one open volume. Dust hangs in the lamplight. "
        "Deep one-point perspective, overwhelming scale, a human-sized desk dwarfed by shelving that never stops."
    ),
    "image-alexandria.png": (
        "A man seated at a low table in a sunlit stone colonnade in ancient Alexandria, seen from BEHIND and "
        "slightly above. His face is completely hidden from the viewer - he is turned fully away, and no part of "
        "his features is visible. Pale limestone columns, bright Mediterranean light and hard shadow, a rack of "
        "papyrus scrolls, a bronze compass and a wax tablet on the table before him. Plain undyed linen robes, "
        "sandals, close-cropped grey hair at the back of the head. Ordinary and quiet - no grandeur, no crowd, "
        "no audience, an unremarkable man at work."
    ),
    "image-survives.png": (
        "A ruined classical courtyard in late afternoon light. Cracked marble flagstones with weeds pushing "
        "through the joints, broken column drums lying where they fell, a collapsed architrave. Long golden "
        "shadows. Scratched into one intact flagstone in the foreground, still crisp and sharp and undamaged, "
        "a simple geometric figure of straight lines and a circle - pure geometry, no writing and no numerals. "
        "The building has failed completely; the scratched figure has not aged at all."
    ),
    "image-vienna.png": (
        "A small university seminar room in central Europe in winter, early 1930s. Half a dozen empty bentwood "
        "chairs, a bare wooden lectern, a large dark slate blackboard wiped almost clean leaving only faint "
        "grey chalk smears with no legible writing of any kind. Tall windows with cold flat grey light. "
        "A single dark wool overcoat hangs on a hook by the door. Entirely empty of people. Quiet, austere, cold."
    ),
    "image-desk.png": (
        "A modern child's wooden desk at night, lit by one warm desk lamp. An ordinary lined exercise book lies "
        "open, covered in careful pencil working-out seen at a shallow oblique angle - the handwriting is "
        "indistinct and completely illegible, no readable figures. A yellow pencil, an eraser, a glass of water. "
        "Beyond the lamp's pool of light the bedroom falls into darkness. Warm, intimate, contemporary, unstaged."
    ),
}


def generate(name):
    prompt = SCENES[name] + "\n\n" + STYLE
    body = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "size": "1536x1024",
        "quality": "high",
        "n": 1,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=420) as r:
            data = json.load(r)
        b64 = data["data"][0]["b64_json"]
        path = os.path.join(OUT, name)
        with open(path, "wb") as f:
            f.write(base64.b64decode(b64))
        return f"OK   {name}  ({os.path.getsize(path)//1024} KB)"
    except urllib.error.HTTPError as e:
        return f"FAIL {name}  HTTP {e.code}: {e.read().decode()[:300]}"
    except Exception as e:
        return f"FAIL {name}  {type(e).__name__}: {e}"


if __name__ == "__main__":
    targets = sys.argv[1:] or list(SCENES)
    with ThreadPoolExecutor(max_workers=4) as ex:
        for line in ex.map(generate, targets):
            print(line, flush=True)

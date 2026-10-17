# Writer notes — Monkey King, Volume III (read after PACKET-SPEC.md)

Book-specific rules every packet writer applies. They come from the reference
phase and the script gate; they are not optional.

## Which sheet carries whom

| Who | Sheet to attach | State on the page |
|---|---|---|
| Wukong, every page he is on | `refs/approved/10-wukong.png` | banded pilgrim: hemp robe with the mended left shoulder, tiger-skin kilt under it, **the thin plain gold band on his brow in every panel** (blocking on every card: "band on"); needle behind the right ear when the staff is away. At home (pp 21–22, 36–39) a crown of flowers and leaves sits on top of the band, and the band still shows under it. p 18 panel 2: four identical Wukongs, band on each — the only page where he is drawn more than once |
| Sanzang (man) | `02-sanzang.png` | saffron robe, red kasaya with gold grid, ringed staff, shaven head; on the white horse on the ridge; walking in the wood |
| Sanzang as the tiger, pp 29 panel 2, 30, 32, 45, 46 panel 2 | `16-sanzang-tiger.png` | lean tiger, torn red kasaya with the gold grid knotted at the throat, the monk's dark almond eyes, sitting upright paws together; never snarling, never eating |
| Bajie | `07-bajie.png` | black tunic, blue sash, rake; luggage pole on the road; small sagging gray cloud on pp 35, 40 |
| Wujing | `08-wujing.png` | **no skulls anywhere on him** (blocking: "a skull or necklace on Wujing"); sand-brown tunic, reed sash, crescent spade |
| The white horse | `06-white-horse.png` | dark-red brass-fitted saddle; **right foreleg wounded** (gash, hoof lifted) on pp 33–34, 41–42, 48; **bandaged** on p 49 |
| The white dragon, pp 31–32 | `05-dragon.png` | slim white serpent, sea-green eyes, pale-blue mane, two short horns |
| The White Bone Lady (true shape), pp 2, 4 p1, 9 p1, 15 | `11-bone-lady.png` | skull face with green pinpoints, long loose black hair, ash-gray/violet burial silk |
| The girl, pp 4–6 | `12-bone-girl.png` | peach-pink jacket, single plait with red string, lidded bamboo basket |
| The old woman, pp 9–11 | `13-bone-old-woman.png` | white bun, brown padded jacket, bamboo cane |
| The old man, pp 13–15 | `14-bone-old-man.png` | white beard, gray pilgrim gown, brown prayer beads |
| The Yellow Robe | `15-yellow-robe.png` | indigo face, tusks, black topknot, mustard-ochre robe with small silver stars over black armour, silver scimitar, pale silver eyes |
| Flower-Fruit monkeys, pp 20–22, 36, 39 | `09-monkeys.png` | brown, bare, young; no clothing, no gold, no band |

Setting plates: `set-ridge` (pp 1–19), `set-flower-fruit` (pp 20–22, 36–39),
`set-pagoda-exterior` (pp 23, 26–27, 31, 33–34, 41–44, 48),
`set-pagoda-hall` (pp 24–25, 28–30, 32, 45–47), `set-road-west` (p 49).
Object plates: `obj-basket` (pp 4, 6: lidded with rice and noodles, then open
with maggots and green frogs — p 6 only the second state), `obj-bones`
(pp 15–17: the plate's skull has a blank carved band; the page letters
WHITE BONE LADY there), `obj-cage-meat` (pp 30, 45). If a plate is not yet in
`refs/approved/`, still name it by this exact file name; the manager checks
every manifest before launch.

**Two or at most three image inputs per page, never more.** Pick the focal
characters of the dominant panel; minor figures are drawn from words with
their lock and their nearest lookalike named. Wukong's sheet is attached
whenever his face carries the page. Plates are optional when two character
sheets are needed; the prompt then describes the place in words.

## Staging notes from the script gate (carry them into the prompts and cards)

- **The seeing rule (blocking on pp 5, 6, 9, 10, 15, 43).** The demon's true
  shape inside a disguise, the hollow skin and the escaping mist are shown
  only as Wukong's view: a pale ghost-image inside the flare of his
  red-ringed eyes, framed as his view (the panel tinted by his sight, or the
  ghost drawn faint and translucent over the disguise). To the monk, a fallen
  disguise is a still body lying face-down; never a wound, never blood. On
  p 15 the monk's face is buried in the horse's neck, eyes shut.
- **No blood anywhere** (pp 6, 10, 15, 32, 33). The dragon's wound is a clean
  dark gash.
- **The basket on p 6** is open on its side with white maggots and small
  green frogs; gross and comic, not horror.
- **p 16 panel 2:** a close, large skull with WHITE BONE LADY carved across
  its brow in big clear capital letters — the one printed object in the book;
  it must read from the proof.
- **p 18:** four Wukongs, each identical with the band, kneeling on four sides
  of the monk; the monk in the centre.
- **pp 23–26 geography:** the pagoda stands just inside the trees; its heavy
  black-iron front door is open on pp 23–24 (the monk drops his staff on its
  threshold), shut on p 26 with the staff lying on the ground in front of it.
- **p 30:** the hall's high window is shuttered; p 31 the dragon tears the
  shutter off; p 45 the cage is lit by the iron lamp and the window is boarded shut again; Wukong's eyes see the monk's face inside the tiger.
- **The horse speaks on pp 33–34 only:** his mouth closed or barely open, the
  balloon tail to his head. Never let a balloon point at Bajie by mistake —
  stage the horse on the right, Bajie on the left, in every panel.
- **Yellow Robe vs Wujing** (same panel pp 26–29, 45): name the separation
  sentence (huge planted indigo-faced demon with black topknot and short
  black beard in mustard-ochre over black armour vs gaunt stooped slate
  blue-gray ogre with wild red hair and red beard in sand-brown).
- **Yellow Robe vs Sanzang** (pp 24–25, 29): the demon is half again the
  monk's height; mustard-ochre with silver stars over black armour vs saffron
  robe under red kasaya.
- **The star (pp 43–44):** silver light through cracks in the indigo face and
  robe; then a silver streak rising and one bright star.
- **Owner tags** `GIRL`, `OLD WOMAN`, `OLD MAN`, `HORSE`, `WHITE BONE LADY`,
  `YELLOW ROBE` are never lettered.
- **No counted story object above five.** The peaches are four, never counted
  in text; "four or five" passes.

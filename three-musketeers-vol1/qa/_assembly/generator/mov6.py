MOV = 6
from mov1 import C1_TAIL, DART
from mov5 import DART_ROAD

BUCK = ("The Duke of Buckingham, keyed to his sheet: thirty-five, broad-shouldered, as tall as the tallest man in the book, handsome square-jawed face, straight nose, blue eyes, high colour, wide mouth, golden hair in long loose curls past the shoulder, a short golden beard and full moustache; athletic, fast; "
        "white satin doublet and breeches slashed with gold, a wide collar of white lace, a rope of pearls, a sash of blue silk, no cloak, no hat; habitual gesture pulling off one glove (one state, pp 36–39; glove off from p 37).")
PAIR_AB = "The risky pair by type is Buckingham against the absent Aramis: keep Buckingham broad, golden-curled past the shoulder, bearded, in white satin and pearls, so he can never be taken for the slim blond Musketeer in blue serge."
CASKET10 = "The casket keyed to the casket plate: a small velvet-lined casket standing open with twelve slots in two rows of six, ten holding a diamond stud and two slots plainly empty; the two empty slots are drawn large and obvious, and the reader is never asked to count the stones."
MUD = "The boy has mud to the waist and holds his hat in his hand indoors (mud state, pp 33–46)."

PAGES = {
36: dict(
    title="the richest man in England",
    intent="""Spectacle. A river of masts, and a white palace with a marble stair running down to the water. At the foot of the stair, a boy with mud to the waist, hat in one hand, holding up a small letter with a blue crowned seal to a footman. At the top of the stair, in white satin and pearls, a golden-haired man already coming down two steps at a time. One caption names London and the Duke of Buckingham. The dominant turn is London, a white palace, and a boy in mud at the gate, with the richest man in England coming down himself. The Duke owns the stair; the boy owns the mud. The reader turns because the Duke is coming down himself and you want to know what the letter says. Everything is white, gold, and mirror, with no shadow: this place must look like a different world from France.""",
    turn="A muddy boy holds up the Queen's seal at the foot of a white palace's water stair, and the Duke of Buckingham comes down it himself, two steps at a time.",
    moments=[
        "One image, the whole page, about 100%: a river crowded with masts across the bottom; rising from it a white palace front with a marble stair running down to the water, everything white, gold, and mirror-bright, no shadow. At the foot of the stair, lower LEFT, the boy in ochre with mud to the waist, hat in one hand, the other hand holding up a small letter with a blue crowned seal toward a footman in livery who has stepped back. At the top of the stair, upper RIGHT, Buckingham in white satin, gold curls, pearls, the blue sash, already coming down two steps at a time, one hand on the balustrade.",
        "The caption sits along the lower edge over the water, tail-free. Nothing else is lettered; no words on the palace or the boats.",
    ],
    locks=DART_ROAD + " " + MUD + " " + BUCK + " " + PAIR_AB + " The footman: livery, faceless, silent, no balloon. The Queen's letter: small, blue seal with a crown, no legible writing.",
    exclusions="Athos, Porthos, Aramis, Constance, Rochefort, and the Cardinal are absent. No blood. The letter is the small blue-sealed one. No lettering except the caption.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/08-buckingham.png", "refs/approved/obj-letters-pass.png", "refs/approved/set-buckingham-water-stair.png"],
    card=[
        ("Caption transcription", "The one caption reads exactly from the 600 × 900 proof, once, tail-free, with no other text on the page. " + C1_TAIL),
        ("The page is not a duke coming down his own stair to a muddy boy", "The eye must find a white palace stair over a river of masts, a muddy boy at the bottom holding up a small sealed letter, and a golden man in white satin coming down fast. If the Duke is still at the top standing, or the boy is not plainly muddy, or the page reads as panels, the turn has not landed."),
        ("Buckingham fails identity", "Broad, golden curls past the shoulder, short golden beard, white satin slashed with gold, lace collar, pearls, blue sash, no hat, no cloak. A slim blond man in blue, a dark man, or a cloaked man is blocking."),
        ("d'Artagnan or the letter fails", "The boy clean-shaven, black-haired, in ochre with mud to the waist, hat in hand, holding a small blue-sealed letter. A clean boy or a red-sealed letter is blocking."),
        ("The register fails", "The palace must be white, gold, and bright with no heavy shadow, plainly another world from grey France. A dark or grey palace is blocking. Exact architecture is nonblocking."),
        ("Focal generation failure", "A duplicated Duke or boy, gross anatomy on the hand holding up the letter, or text colliding with a figure is blocking. Masts and water are not."),
    ]),

37: dict(
    title="ten",
    intent="""Dramatic. A white and gold bedroom. Buckingham reads the letter by the window, pulling off one glove with his teeth; the boy drips on the carpet. She writes that the King wants the studs on Monday and that the Cardinal is smiling; who are you, boy? d'Artagnan, nobody, I ride fast. A small table by the bed, a velvet casket open: twelve slots in a double row, ten diamonds, and two empty places large and plain to see. The Duke's face goes white; she gave them to him, he keeps them here where he sleeps and nobody comes in; ten; there are two holes. Both hands flat on the table: two are gone, someone has been in this room. The dominant turn is the casket: ten, and two holes. Buckingham owns the page; the boy names the holes. The reader turns because someone has been in the Duke's bedroom and the boy knows who. The empty slots, not the count, carry the page.""",
    turn="The Duke reads the Queen's letter, opens the casket he keeps where he sleeps, and finds two empty slots where twelve diamonds should be.",
    moments=[
        "Panel one, about 25%, wide: a white and gold bedroom, bright, no shadow. Buckingham on the RIGHT at the window reading the small opened letter, pulling one glove off with his teeth; the boy on the LEFT, muddy, hat in hand, dripping on the carpet. Buckingham's line upper right, tail to his mouth; the boy's answer lower left, after it, tail to his.",
        "Panel two, the dominant panel, about 50%, close and tall: a small table by the bed with a velvet casket standing open toward the viewer: twelve slots in two rows of six, ten holding a bright diamond stud, and two slots empty, dark, and plainly visible, the largest thing in the panel. Buckingham on the RIGHT above it, his face gone white, the bare hand on the table edge; the boy on the LEFT looking in over the Duke's arm. Three balloons A–B: Buckingham's line about where he keeps them upper right, his one word below it on his side, the boy's four words lower left, after both, tails to each mouth.",
        "Panel three, about 25%: Buckingham straightening, both hands flat on the table, the boy beside him. Buckingham's line beside him, tail to his mouth.",
    ],
    locks=DART_ROAD + " " + MUD + " " + BUCK + " " + PAIR_AB + " " + CASKET10,
    exclusions="Athos, Porthos, Aramis, Constance, Rochefort, and the Cardinal are absent. No blood. Exactly ten studs in the casket and exactly two empty slots, and the empty slots must read at a glance without counting; a full casket or a casket with one or three empty slots is wrong. The letter is small and blue-sealed, now opened, no legible writing. No lettering except the six spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/08-buckingham.png", "refs/approved/obj-casket-pouch-ring.png", "refs/approved/set-buckingham-bedchamber.png"],
    card=[
        ("Dialogue transcription or ownership fails", "All six lines read exactly from the 600 × 900 proof, once each, in causal order; Buckingham's four hang from the golden man in white and the boy's two from the muddy boy; the single word Ten belongs to the Duke and sits beside the open casket. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: the Duke reads and asks who the boy is, opens a casket with two obviously empty places, and says someone has been in the room. If the open casket with two empty slots is not the largest image the eye finds, the turn has not landed."),
        ("The casket state fails", "Two empty slots must be plain at reading size without counting stones; a full casket, or empty slots that cannot be seen, is blocking. The exact number of visible stones is nonblocking so long as two holes read."),
        ("Buckingham fails identity", "Broad, gold curls past the shoulder, short gold beard, white satin, pearls, blue sash, one glove off. A slim blond in blue or a dark man is blocking."),
        ("d'Artagnan fails identity", "Clean-shaven, black-haired, ochre with mud to the waist, hat in hand. A moustache or a clean coat is blocking."),
        ("Focal generation failure", "A second casket, a duplicated Duke, gross anatomy on the hands flat on the table, or a balloon across a face is blocking."),
    ]),

38: dict(
    title="send for my jeweler",
    intent="""Dramatic. The bedroom. Buckingham pacing with the glove in his fist, thinking aloud, the boy following him with his eyes; in a corner a small memory inset: a masked man with a scar showing under the mask bowing on a stair as the Duke passes. Three nights ago the Duke gave a ball, every door stood open, a masked man begged his pardon on the stair outside this door; a scar under the mask. The man with the scar, the Cardinal's man; the boy fought him at Calais this morning; he climbed out of the harbour with something in his fist, and it flashed twice. Buckingham stops dead: then he sees it; she wears ten and the Cardinal steps forward with the two she lacks; then she wears twelve, send for my jeweler. Hands on the boy's shoulders: it's Thursday, the ball is Monday; two days for the diamonds, two for the road, sleep on the boat; I don't sleep. The dominant turn is the trap understood and the decision to make two. Buckingham owns the page; the boy supplies the flash. The reader turns because a duke is going to make two diamonds in two days and the boy has to carry twelve home in two more.""",
    turn="Remembering a masked man with a scar on his stair, the Duke sees the Cardinal's trap in one breath and sends for his jeweler to make two diamonds in two days.",
    moments=[
        "Panel one, about 30%, wide: Buckingham on the RIGHT pacing, the glove crushed in his fist, thinking aloud; the boy on the LEFT following him with his eyes. In the upper corner a small inset, softer, as memory: a masked man in black with a scar showing below the mask's edge, bowing on a stair as the Duke in white passes; no text in the inset. Four balloons as two single-speaker beats: Buckingham's two lines stacked upper right, tails to his mouth; the boy's two lines stacked lower left, after them, tails to his.",
        "Panel two, the dominant panel, about 45%, close and tall: Buckingham stopped dead, facing the viewer, understanding, the glove hitting the table; the boy behind him on the LEFT. Two balloons stacked on the Duke's side, the trap first, the order below it, both tails to his mouth.",
        "Panel three, about 25%: Buckingham with both hands on the boy's shoulders, the boy on the LEFT, the Duke on the RIGHT. Three balloons A–B–A: the boy's day line upper left, the Duke's plan middle right, the boy's three words lowest left, tails to each mouth, none level.",
    ],
    locks=DART_ROAD + " " + MUD + " " + BUCK + " " + PAIR_AB + " The masked man in the memory inset: black clothes, a mask covering the eyes, a pale scar visible on the cheek below the mask, bowing; no red feather needed; silent, no balloon.",
    exclusions="Athos, Porthos, Aramis, Constance, and the Cardinal are absent; Rochefort appears only in the small memory inset, masked, and nowhere else. No blood. The casket is closed or unfocal on this page. No lettering in the inset; only the nine spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/08-buckingham.png", "refs/approved/07-rochefort.png", "refs/approved/set-buckingham-bedchamber.png"],
    card=[
        ("Dialogue transcription or ownership fails", "All nine lines read exactly from the 600 × 900 proof, once each, in causal order; Buckingham's five hang from the golden man and the boy's four from the muddy boy; each reply sits after the line it answers; the memory inset carries no text. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: the Duke remembers a masked man with a scar on his stair, the boy says he fought that man and saw something flash, the Duke sees the trap and calls for his jeweler, then sets the days. If the Duke stopped dead in understanding is not the largest image the eye finds, the turn has not landed."),
        ("The memory inset fails", "A small softer image of a masked man with a visible scar bowing on a stair must be present in the first panel and must not be mistaken for a present-tense figure in the room. A masked man standing in the bedroom now is blocking."),
        ("Buckingham or d'Artagnan fails identity", "The Duke broad, golden, bearded, in white satin and pearls; the boy clean-shaven in muddy ochre. Blocking if contradicted."),
        ("Focal generation failure", "Exactly two hands on the boy's shoulders in the last panel; a duplicated Duke, gross anatomy on the fist with the glove, or a balloon across a face is blocking."),
    ]),

39: dict(
    title="tell her",
    intent="""Illustrated prose, two locations because the two days end at the water: the jeweler's workroom, and the water stair. The dominant image is the workroom: an old jeweler at a bench with a loupe in his eye and a small fire, two new diamond studs in his tongs beside the ten, Buckingham standing over him and not sitting, and in a corner chair the boy asleep after all with his hat over his face. The smaller image is the water stair: Buckingham putting the closed casket into the boy's hands, a boat waiting below. The prose carries the two days and two nights, the Duke never sitting, the new stones nobody can tell apart, and the sentence Buckingham starts and cannot finish. The dominant turn is the jeweler's fire, two days, twelve, and tell her. Buckingham owns the page; the jeweler is scenery who never talks. The reader turns because there are twelve diamonds in a box, it is Saturday night, and the ball is Monday.""",
    turn="An old jeweler makes two diamonds in two days while the Duke stands over him, and at the water stair the Duke starts to say tell her and cannot finish.",
    moments=[
        "Panel one, the dominant image, about 55%, close: the jeweler's workroom, white and bright: an old man at a bench with a loupe in his eye and a small fire beside him, two new diamond studs in his tongs, the open casket with the ten beside them; Buckingham standing over him on the RIGHT, not sitting, glove in his fist; in a chair in the corner on the LEFT the boy asleep, hat over his face, mud drying on his boots. Exactly two focal hands: the jeweler's on the tongs.",
        "Panel two, about 45%: the marble water stair, a boat waiting below; Buckingham on the RIGHT putting the closed casket into the boy's two hands on the LEFT and holding on to it a moment longer, both men's hands on the box.",
        "The prose field sits over the white wall in panel one, a matte parchment field across most of the width, never over the bench, the tongs, or the faces. Three paragraphs. No other lettering.",
    ],
    locks=DART_ROAD + " " + MUD + " " + BUCK + " " + PAIR_AB + " The jeweler: an old man, bald or white-haired, in a plain apron, a loupe in one eye, faceless where possible, silent, no balloon. The casket keyed to its plate, open with ten and two in the tongs in panel one, closed in panel two.",
    exclusions="Athos, Porthos, Aramis, Constance, Rochefort, and the Cardinal are absent. No blood. The jeweler never speaks. The casket is closed at the water stair. No lettering except the one prose field; no words on the bench or the boat.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/08-buckingham.png", "refs/approved/obj-casket-pouch-ring.png", "refs/approved/set-buckingham-workroom.png", "refs/approved/set-buckingham-water-stair.png"],
    card=[
        ("Prose transcription", "The prose field reads exactly, all three paragraphs in order, once, from the 600 × 900 proof, over plain ground and never over faces or the bench, with no other text on the page. " + C1_TAIL),
        ("The workroom does not own the page", "The eye must find first an old man at a bench with a loupe and tongs and the Duke standing over him, and second the box passing at the water stair. If the stair competes, or the page reads as a comic strip, the turn has not landed."),
        ("Buckingham or d'Artagnan fails identity", "The Duke golden, bearded, in white satin, standing; the boy clean-shaven in muddy ochre, asleep with his hat over his face in the first image and awake with the box in the second. Blocking if contradicted."),
        ("Object state fails", "The casket open with two studs in the tongs beside it in the workroom; closed in the boy's hands at the stair. An open box at the stair is blocking."),
        ("Focal generation failure", "A talking jeweler with a balloon, a duplicated Duke, gross anatomy on the hands on the box, or the prose field over a face is blocking."),
    ]),

40: dict(
    title="the road home",
    intent="""Illustrated prose, two locations because the ride ends at the gate: the road from Calais, and the Paris gate at sunset. The dominant image is the road south: one rider changing horses at a post inn without properly dismounting, a blown horse behind him, a fresh one under him, the sun coming up, and in the inn yard a red cloak looking hard at every rider and looking past him. The smaller image is Paris at sunset: the rider coming through the gate, and beyond the roofs the long front of the Louvre with every window lit. The prose carries the rough sea, the sergeant who did not ask, five changes of horse, the red cloak who looked past a muddy boy for a Musketeer, the towns he did not ride through, the names said at milestones, and Monday's sun going down on the Louvre. The dominant turn is the road home and Monday's sun. The boy owns the page alone. The reader turns because he is in Paris with the box, the ball has started, and the Queen is not yet wearing anything.""",
    turn="Sick on the boat and changing horses five times, the boy is looked past by a red cloak and comes through the Paris gate at Monday's sunset with the box.",
    moments=[
        "Panel one, the dominant image, about 60%, wide: a post-inn yard at dawn on the road south; the boy in muddy ochre swinging from a blown, steaming horse onto a fresh one without touching the ground, the closed casket under his arm; in the yard a guard in a red cassock looking hard at the riders and looking straight past the muddy boy; ostlers faceless.",
        "Panel two, about 40%: Paris at sunset; the rider coming through the great gate toward the viewer, and beyond the roofs the long front of the Louvre with every window lit gold against the dusk.",
        "The prose field sits over the road and sky in panel one, a matte parchment field across most of the width, never over the rider or the red cloak. Three paragraphs. No other lettering.",
    ],
    locks=DART_ROAD + " " + MUD + " The red cloak at the post inn: red cassock with a white cross, plain helmet, faceless, no feather, silent. Ostlers: faceless, silent. The casket keyed to its plate, closed.",
    exclusions="Athos, Porthos, Aramis, Constance, Rochefort, the Cardinal, and Buckingham are absent; the sergeant and the sea are in the prose only. No blood. The casket stays closed. No lettering except the one prose field; no words on the gate or the inn.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/set-road.png", "refs/approved/set-paris.png"],
    card=[
        ("Prose transcription", "The prose field reads exactly, all three paragraphs in order, once, from the 600 × 900 proof, over plain ground and never over the rider, with no other text on the page. " + C1_TAIL),
        ("The horse change does not own the page", "The eye must find first the boy changing horses at a post inn under the eye of a red cloak who looks past him, and second the lit Louvre beyond the Paris gate at sunset. If the gate competes, or the page reads as equal panels, the turn has not landed."),
        ("d'Artagnan fails identity", "Clean-shaven, black-haired, muddy ochre, with a closed box. A cloaked Musketeer or a bearded rider is blocking."),
        ("The red cloak wears a lock", "The guard in the yard must have no scar and no feather and no balloon; a guard who reads as Rochefort is blocking."),
        ("Focal generation failure", "A duplicated rider, an open casket, or the prose field over a face is blocking. Yard clutter and rooftops are not."),
    ]),
}

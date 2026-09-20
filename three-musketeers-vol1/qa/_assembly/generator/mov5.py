MOV = 5
from mov1 import C1_TAIL, DART, ROCH, PAIR_DR
from mov2 import PORTHOS, ARAMIS, THREE, GUARDS
from mov3 import ATHOS

DART_ROAD = DART.replace("(default state, pp 1–32)", "(default state, pp 1–32; road-dusty from page 28, mud to the waist from page 33)")
ROCH_WET = ("Rochefort soaked (page 35, his sheet's view d): hatless, black hair flat and dripping, black clothes streaming, the scar and thin moustache unchanged, his RIGHT arm held against his chest by his left hand, the other fist closed; no red feather because the hat is in the sea.")

PAGES = {
28: dict(
    title="I drink to the Queen",
    intent="""Dramatic. A bright inn room at noon at Chantilly, a long table, the four eating standing up with their cloaks on. At the far end of the table a stranger in a plain coat has risen with his cup raised toward Porthos and is looking at him and waiting. Porthos says the man is drinking the Cardinal's health and waiting for him to drink it too; Aramis says then drink it, they are in a hurry. Porthos on his feet, enormous, cup up: he drinks to the Queen and to nobody else in this room; the stranger's cup hits the floor and his sword comes out. Porthos throws off his cloak and smooths his baldric; the other three are at the door, the boy looking back: they can't wait; nobody asked you to, go, he's mine, an hour behind you, and I'll have his hat. The dominant turn is the toast and Porthos staying. Porthos owns the page. The reader turns because three riders leave the inn and the loudest man in Paris is not one of them. The stranger is scenery: he raises a cup, drops it, draws, and never speaks.""",
    turn="A stranger toasts the Cardinal at Porthos, Porthos toasts the Queen instead, and stays behind to fight him so the other three can ride.",
    moments=[
        "Panel one, about 30%, wide: the bright inn room at noon, a long table, the four on the LEFT and centre eating standing with cloaks on; at the far RIGHT end of the table a stranger in a plain brown coat risen with his cup raised toward Porthos, looking at him, waiting, silent. Porthos's line upper left over Porthos, tail to his mouth; Aramis's reply middle, over Aramis, after it, tail to his.",
        "Panel two, the dominant panel, about 45%, close and tall: Porthos on his feet, enormous, his own cup raised high, chest out, on the LEFT; the stranger's cup already smashing on the floor at the RIGHT edge with the sound cue beside it. Porthos's toast upper left, tail to his mouth. Exactly two hands focal: Porthos's on his cup and on his baldric.",
        "Panel three, about 25%: the stranger on the RIGHT with his sword out, faceless or turned; Porthos in the middle throwing off his cloak with one hand and smoothing the gold front of his baldric with the other; the other three at the door on the LEFT, the boy looking back over his shoulder. The boy's line upper left, tail to his mouth; Porthos's answer lower centre-right, after it, tail to his.",
    ],
    locks=DART_ROAD + " " + ATHOS + " " + PORTHOS + " " + ARAMIS + " " + THREE + " The stranger: a man in a plain brown coat and no cloak, faceless or turned away, no red cassock, no feather, no scar, no beard of any locked kind; silent, no balloon.",
    exclusions="Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. No blood; no blade touches anyone. The stranger never speaks. Porthos does not fight on this page; he prepares. No lettering on the inn or the cups; only the five spoken strings and the one sound cue.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/03-porthos.png", "refs/approved/04-aramis.png", "refs/approved/set-chantilly-inn.png"],
    card=[
        ("Dialogue transcription or ownership fails", "The five lines and the sound cue read exactly from the 600 × 900 proof, once each, in causal order; Porthos's three hang from the huge red-moustached man, Aramis's one from the slim blond, the boy's one from the boy; the stranger carries no balloon. The run length of the cue's letters is nonblocking. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: a stranger raises a cup at Porthos, Porthos raises his to the Queen and the stranger's cup smashes, Porthos stays while the three go out the door. If Porthos with his cup raised is not the largest image the eye finds, the turn has not landed."),
        ("The Musketeers collide or Porthos fails", "Porthos enormous, red curls, waxed moustache, gold baldric, red plumes; Athos tall and bearded without a sling; Aramis slim and blond; the boy clean-shaven in ochre. Any two merging is blocking."),
        ("The stranger wears a lock", "The stranger must have no scar, no red feather, no red cassock, and no balloon. A stranger who reads as Rochefort or a guard is blocking."),
        ("Bloodless or state fails", "No blood; no blade in anyone; the stranger's cup on the floor in the second panel; the three at the door in the third."),
        ("Focal generation failure", "A fifth companion, a duplicated Porthos, gross anatomy on Porthos's cup hand, or a balloon across a face is blocking. Table clutter is not."),
    ]),

29: dict(
    title="I'll hold the road",
    intent="""Dramatic. Dusk, a stone bridge over a brown river. At the far end, men with picks and a line of stones dragged across the road; the three riders slowing. Aramis: road workers at dusk with their picks pointed at us; as the Fathers tell us, no. The horses drive through the gap in the stones; the men swing; Aramis's horse goes down on the planks and Aramis rolls clear onto his feet, sword out, the lace handkerchief already wound round his hand; the other two horses are through and beyond; six men close on the one in blue. Go on, both of you, don't turn around; Aramis, there are six of them; six, and a bridge is narrow, so they come one at a time; I'll hold the road, go. The dominant turn is Aramis's horse going down and Aramis choosing the bridge. Aramis owns the page. The reader turns because Aramis is holding a bridge alone against six and you are riding away from him. The road workers are scenery with picks; the horse is not hurt.""",
    turn="An ambush on a bridge at dusk brings Aramis's horse down, and he sends the other two on and turns to hold the bridge alone against six.",
    moments=[
        "Panel one, about 30%, wide: the stone bridge at dusk, the brown river beneath, the three riders on the LEFT slowing; at the far RIGHT end a line of stones across the road and six men with picks behind it, faces shadowed. Aramis's single line beside him, tail to his mouth.",
        "Panel two, the dominant panel, about 45%, tall: the moment on the bridge: the men swinging; Aramis's horse going down on the planks in the centre, unhurt, Aramis rolling clear onto his feet on the RIGHT with his slim sword out and the white lace handkerchief wound round his sword hand; the other two horses through the gap and beyond on the LEFT, the boy twisted in the saddle looking back. The sound cue at the horse on the planks. Aramis's shout upper right, tail to his mouth; the boy's cry lower left, after it, tail to his.",
        "Panel three, about 25%, close: Aramis alone with his back to the bridge rail on the RIGHT, calm, two fingers of his free hand at his moustache, the handkerchief on his sword hand; six men crowding in from the LEFT, small and faceless. Aramis's long line beside him, tail to his mouth.",
    ],
    locks=DART_ROAD + " " + ATHOS + " " + ARAMIS + " The risky pair by presence is Aramis against the absent Buckingham; keep Aramis slim, in blue serge with the lace collar, curls to the collar only, so he can never be taken for the golden Duke. The six road workers: rough coats, picks, faces shadowed or turned, no cassocks, no feathers, no scars; silent.",
    exclusions="Porthos is absent from this page (he stayed at Chantilly); Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. No blood; the horse goes down and is not hurt; no blade touches anyone. Exactly six men. The handkerchief carries a small monogram, no legible letters. No lettering on the bridge; only the four spoken strings and the one sound cue.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/04-aramis.png", "refs/approved/set-beauvais-bridge.png"],
    card=[
        ("Dialogue transcription or ownership fails", "The four lines and the sound cue read exactly from the 600 × 900 proof, once each, in causal order; Aramis's three hang from the slim blond man and the boy's one from the boy; the road workers carry no balloon. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: three riders approach men with picks on a bridge, the horse goes down and Aramis comes up with his sword out sending the others on, Aramis alone with his back to the rail and six in front. If the horse going down with Aramis rolling clear is not the largest image the eye finds, the turn has not landed."),
        ("Aramis fails identity", "Slim, blond curls to the collar, small moustache, lace collar, blue cassock, white plume, handkerchief round the sword hand. A beard, dark hair, or bulk is blocking."),
        ("Bloodless or the horse fails", "No blood on anyone; the horse down but plainly not hurt (no blood, no broken leg); no blade in a man. A wounded horse is blocking."),
        ("Count fails", "Exactly six attackers and exactly three riders arriving, two leaving. Seven attackers or Porthos on the page is blocking."),
        ("Focal generation failure", "A duplicated Aramis, a horse with wrong anatomy that reads as injury, gross anatomy on the sword hand with the handkerchief, or a balloon over a face is blocking."),
    ]),

30: dict(
    title="he held the road",
    intent="""Spectacle. From behind the two departing riders, looking back down the road: the bridge at dusk, small, and on it one slim figure in blue with his back to the rail and six men in front of him, one already sitting in the road holding his arm, and the first star over the river. One caption: he held the road, and was still holding it when it got dark, and the horse got up and trotted home without him. The dominant turn is Aramis on the bridge, six in front of him, two riders going away. The reader turns because two riders are left and the Cardinal has not run out of inns. The horse is alive and going home.""",
    turn="Seen from the backs of two riders galloping away, a small figure in blue holds a bridge alone against six as the first star comes out.",
    moments=[
        "One image, the whole page, about 100%: the road seen from just behind and between the two departing riders, whose backs and horses fill the lower foreground on the LEFT and RIGHT edges, the boy in ochre and Athos in blue, the boy's head turned to look back. Down the road, small in the middle distance, the stone bridge at dusk, and on it one slim figure in blue with his back to the parapet rail, sword up, six men in front of him, one already sitting in the road holding his arm; and beyond the bridge on the road, a riderless horse trotting away toward the far side. Above the river, the first star in a deepening sky.",
        "The caption sits along the lower edge over the road between the two horses' hindquarters, tail-free. Nothing else is lettered.",
    ],
    locks=DART_ROAD + " " + ATHOS + " " + ARAMIS + " (small, on the bridge). The six attackers: small, rough coats, picks, faceless; silent.",
    exclusions="Porthos, Constance, Rochefort, the Cardinal, and Buckingham are absent. No blood; the man holding his arm is holding it, not bleeding. The horse is up and moving, unhurt. Athos has no sling. No lettering except the caption.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/04-aramis.png", "refs/approved/set-beauvais-bridge.png"],
    card=[
        ("Caption transcription", "The one caption reads exactly from the 600 × 900 proof, once, tail-free, with no other text on the page. " + C1_TAIL),
        ("The page is not a look back at a bridge held by one man", "The eye must find two riders' backs in the foreground and, down the road, a small blue figure with his back to a bridge rail against six, and a riderless horse going home. If the bridge is large and the riders absent, or the page reads as panels, the turn has not landed."),
        ("Bloodless or the horse fails", "No blood anywhere; the man in the road holds his arm; the horse is up and trotting, not down or hurt."),
        ("The figures fail identity", "The near riders must be the ochre boy and the tall blue Athos; the small figure on the bridge must read as the slim blue Musketeer; Porthos must not be on the page."),
        ("Focal generation failure", "A duplicated bridge figure, a third near rider, or text colliding with a figure is blocking. Distant crowd and sky are not."),
    ]),

31: dict(
    title="I have the wine and I have the door",
    intent="""Dramatic. Evening at the inn at Amiens, the next day; a caption says so and says the coin was good and the innkeeper had been told to say it was not. Athos and the boy dismounting in the yard; the innkeeper holding one of Athos's coins up to the light and shaking his head, and behind him, on cue, four red cloaks with white crosses coming into the yard. The boy: he says your coin is false, and there are red cloaks in the yard; Athos: there are always red cloaks in the yard. Inside, chaos: Athos backing down the cellar steps with his sword in one hand and a barrel rolling into the doorway behind him, red cloaks in the inn door, the boy at the back window with one leg over the sill looking back. Ride, d'Artagnan, not for me, for the letter; I'm not leaving you in a cellar. Athos at the cellar door with a barrel across it and guards on the stairs above, his face level: he has the wine and he has the door, they'll be a week getting him out. Ride. The dominant turn is the last friend behind a cellar door and the boy alone with the letter. Athos owns the page with the fewest words. The reader turns because the boy is alone now.""",
    turn="At Amiens a good coin is called false, red cloaks fill the yard, and Athos barricades himself in the wine cellar so the boy can go out the back window with the letter.",
    moments=[
        "Panel one, about 25%, wide: the inn yard at evening, lanterns being lit. Athos on the LEFT and the boy beside him dismounting; the innkeeper on the RIGHT, aproned, holding a coin up to the lantern light and shaking his head; behind the innkeeper, coming into the yard, four guards in red cassocks with white crosses, faces turned. The caption upper left over the inn wall, tail-free. The boy's line beside him, tail to his mouth; Athos's reply after it, lower, tail to his.",
        "Panel two, the dominant panel, about 45%, tall, inside the inn: Athos on the RIGHT backing down stone cellar steps, sword in one hand, a barrel rolling into the cellar doorway behind him; red cloaks crowding the inn's front door at the back; the boy on the LEFT at the back window with one leg over the sill, looking back. Athos's order upper right, tail to his mouth; the boy's protest lower left, after it, tail to his.",
        "Panel three, about 30%, close: Athos at the cellar door seen from the boy's side, a barrel across the doorway, guards on the stairs above him small and faceless, Athos's face perfectly level. Two balloons stacked on his side, the long line first, the one-word line alone below it, both tails to his mouth.",
    ],
    locks=DART_ROAD + " " + ATHOS + " The risky pair by type is Athos against the absent Rochefort: keep the pointed beard, the blue cassock, the white plume, and the stillness. The innkeeper: aproned, bareheaded, heavy, faceless, silent. " + GUARDS,
    exclusions="Porthos, Aramis, Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. No blood; no blade touches anyone; the guards never reach Athos on this page. Exactly four guards. No lettering on the inn sign or the coin; only the caption and the six spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/set-amiens-inn.png"],
    card=[
        ("Dialogue transcription or ownership fails", "The caption and all six lines read exactly from the 600 × 900 proof, once each, in causal order; Athos's four hang from the tall bearded man and the boy's two from the boy; the single word Ride stands alone in its own balloon below Athos's longer line; the innkeeper and guards carry no balloon. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: a coin is refused as red cloaks enter the yard, Athos backs into the cellar with a barrel while the boy goes out the back window, Athos holds the cellar door and says ride. If Athos backing down the cellar steps with the boy at the window is not the largest image the eye finds, the turn has not landed."),
        ("Athos fails identity", "Tall, dark shoulder-length hair, pointed beard, blue cassock, white plume, no sling, level face. A scar, black clothes, or a sling is blocking."),
        ("d'Artagnan fails identity", "Clean-shaven, black-haired, ochre, no cloak, at the window. A moustache is blocking."),
        ("Guards, bloodless, or state fail", "Exactly four red-cassocked guards with faces turned and no feather; no blood; a barrel across the cellar door in the last panel; nobody touched."),
        ("Focal generation failure", "A duplicated Athos, a fifth guard, gross anatomy on the hand with the sword or the leg over the sill, or a balloon across a face is blocking."),
    ]),

32: dict(
    title="the sea",
    intent="""Illustrated prose, two locations because the night and the dawn are the turn: the night road, and the sea. The dominant image is one rider on a night road under an enormous sky, bent low, going hard. The smaller image is dawn: the road cresting a long hill and beyond it the grey sea, gulls, and a harbour full of masts. The prose has him take the first horse in the back paddock, ride all night further from anyone than he has ever been, count the three men who stopped for him to keep himself awake, and come over the hill to a sea bigger than Paris. The dominant turn is alone: the night road, counting friends, the sea. The boy owns the page entirely. The reader turns because he has reached the sea alone and everything now depends on a boat.""",
    turn="Alone for the first time, the boy rides all night counting the friends who stopped for him, and comes over a hill at dawn to a sea bigger than Paris.",
    moments=[
        "Panel one, the dominant image, about 60%, tall: a night road under an enormous sky full of stars, one rider bent low over a dark horse, going hard, small against the sky, a milestone catching the moon.",
        "Panel two, about 40%, wide: dawn. The road cresting a long hill, and beyond and below it the grey sea, gulls, and a harbour full of masts; the rider small at the crest, stopped, looking.",
        "The prose field sits over the night sky in panel one, a matte parchment field across most of the width, never over the rider or the sea. Three paragraphs. No other lettering.",
    ],
    locks=DART_ROAD + " On a plain dark horse, not the yellow horse and not the bay from the gate; the horse is unfocal.",
    exclusions="Athos, Porthos, Aramis, Constance, Rochefort, the Cardinal, and Buckingham are absent; the three named in the prose are not drawn. No blood. No lettering except the one prose field; the milestone carries no readable numerals.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/set-road.png"],
    card=[
        ("Prose transcription", "The prose field reads exactly, all three paragraphs in order, once, from the 600 × 900 proof, over plain ground and never over the rider, with no other text on the page including on the milestone. " + C1_TAIL),
        ("The night ride does not own the page", "The eye must find first one small rider under a vast night sky and second the sea at dawn from a hilltop. If the sea competes or the page reads as panels of equal weight, the turn has not landed."),
        ("d'Artagnan fails identity", "The rider must read as the clean-shaven boy in ochre with the grey hat; a cloaked Musketeer or a bearded man is blocking. Face detail at this size is nonblocking so long as nothing contradicts him."),
        ("A companion appears", "Any second rider, any blue cassock, any red cloak on this page is blocking; the point is that he is alone."),
        ("Focal generation failure", "A duplicated rider, a horse with wrong anatomy, or the prose field over the rider is blocking. Star field and sea texture are not."),
    ]),

33: dict(
    title="closed by order of the Cardinal",
    intent="""Dramatic. A stone quay at Calais, a boat, a gangplank, gulls; across the quay a wooden barrier with a sergeant of guards at it and a printed notice nailed to the barrier saying the harbour is closed by order of the Cardinal and no one sails without his pass. The boy, off his horse, reads it: closed, he has closed the sea. A second boat, coming in from England, gangplank down, and walking down it in black with a red feather, showing a folded paper to the sergeant, one hand on a small pouch inside his coat: the scar, coming in, not going out. Face to face across the barrier: the Gascon, on the sea road, what could a farm boy want in England? Your pass; the third time you'd stay, this is the fourth, you're staying. On a quay, in front of the sergeant? Gladly; nobody stops the Cardinal's man. The dominant turn is the closed harbour and the scar walking off the boat with the only pass. The reader turns because the man with the scar has the only pass in Calais and the boy has a sword. The printed sign is object text, lettered on the board; the sergeant is scenery.""",
    turn="The sea is closed by the Cardinal's order, and the only man with a pass is walking off the England boat with a scar on his face and a pouch in his coat.",
    moments=[
        "Panel one, about 30%, wide: the stone quay, a boat alongside with its gangplank down on the RIGHT, gulls; across the quay a wooden barrier with a printed notice nailed to it and a sergeant in a red cassock standing at it, faceless; the boy on the LEFT, off his horse, mud to the waist, reading the notice. The notice's words are painted large and plain on the board itself, object text, not a balloon. The boy's line beside him, tail to his mouth.",
        "Panel two, about 25%: a second boat's gangplank, and walking down it toward the barrier, Rochefort in black with the red feather, hat on, one hand holding a folded paper out toward the sergeant and the other hand pressed flat over a small pouch inside his open coat. His line beside him, tail to his mouth.",
        "Panel three, the dominant panel, about 45%, close and tall: Rochefort on the RIGHT and the boy on the LEFT face to face with the barrier between them, the folded pass still in Rochefort's raised hand, the scar toward the viewer. Three balloons A–B–A: Rochefort's question upper right, the boy's demand middle left, Rochefort's answer lower right, tails to each mouth, none level.",
    ],
    locks=DART_ROAD + " " + ROCH + " " + PAIR_DR + " The sergeant: a red cassock with a white cross, a plain morion, faceless, a paper in his hand, silent. Sailors: bareheaded, aproned, faceless, silent.",
    exclusions="Athos, Porthos, Aramis, Constance, the Cardinal, and Buckingham are absent. No blood; no sword is drawn on this page. The pass in Rochefort's hand shows no legible words on this page; the only legible object text is the notice on the barrier. The pouch stays inside the coat under his hand. No lettering on the boats.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/07-rochefort.png", "refs/approved/obj-letters-pass.png", "refs/approved/set-calais-quay.png"],
    object_text="The printed notice is object text painted on the barrier board, not a balloon; the pass in Rochefort's hand carries no legible words on this page.",
    card=[
        ("Transcription or ownership fails", "The notice reads exactly from the 600 × 900 proof as words painted on the barrier board, once; the five spoken lines read exactly, once each, in causal order, the boy's two from the boy and Rochefort's three from the scarred man in black; the sergeant and sailors carry no balloon. The board legible again in a second panel is continuity, not a doubled string. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: the boy reads that the harbour is closed, the scar walks off a boat with a pass, the two face each other across the barrier. If the boy and the scar face to face over the barrier is not the largest image the eye finds, the turn has not landed."),
        ("Rochefort fails identity or collides with the boy", "One scar across a cheek from temple to mouth (which cheek is nonblocking), thin moustache, no beard, black, red feather, hat on, a paper in one hand and the other on a pouch in his coat; the boy clean-shaven in ochre with mud to the waist. Blocking if either is contradicted or they merge."),
        ("The sergeant wears a lock", "The sergeant is a red cassock with a plain helmet and no feather, no scar, no balloon. A sergeant who reads as Rochefort is blocking."),
        ("Bloodless or state fails", "No sword drawn on this page; no blood; the pouch inside the coat, not visible; the pass in Rochefort's hand."),
        ("Focal generation failure", "A duplicated scar-man, two barriers, gross anatomy on the hand holding the pass, or a balloon across a face is blocking. Gulls and rigging are not."),
    ]),

34: dict(
    title="steel on a plank",
    intent="""Spectacle. The duel on the gangplank: the two of them on a plank a foot wide over grey water, blades crossed high, the boy's hair flying, Rochefort's hat already gone into the sea, gulls exploding upward, sailors and the sergeant frozen along the quay. One sound at the blades, one caption. The dominant turn is the duel itself, on a plank over the sea, a thing his father never taught him. The boy and the scar own the page together. The reader turns because one of them is going into the water. Bloodless: blades cross, nobody is cut.""",
    turn="A boy and a scarred man fight with swords on a plank a foot wide over the harbour, and one of them is going in.",
    moments=[
        "One image, the whole page, about 100%: the gangplank from the quay to the boat, a foot wide, over grey water; on it the boy in ochre on the LEFT, mud to the waist, hair flying, and Rochefort in black on the RIGHT, hatless now, his black hat floating on the water below; the two blades crossed high at the centre of the page; gulls bursting upward all round; along the quay behind, small and frozen, the sergeant in his red cassock and a few sailors. No blood, no cut.",
        "The sound cue at the crossed blades in large simple letters. The caption along the lower edge over the water, tail-free. Nothing else is lettered.",
    ],
    locks=DART_ROAD + " " + ROCH.replace("black hat with a single red feather,", "hatless on this page, the black hat with its red feather floating on the water below,") + " " + PAIR_DR + " The sergeant and sailors: small, faceless, silent.",
    exclusions="Athos, Porthos, Aramis, Constance, the Cardinal, and Buckingham are absent. No blood, no cut, no wound. Rochefort's hat is in the water, not on his head. Nobody has fallen in yet. No lettering except the sound cue and the caption; the barrier notice, if visible, is far and illegible.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/07-rochefort.png", "refs/approved/set-calais-quay.png"],
    card=[
        ("Sound cue and caption transcription", "The sound cue at the blades and the caption along the bottom read exactly from the 600 × 900 proof, once each, with no other text on the page. The run length of the cue's letters is nonblocking. " + C1_TAIL),
        ("The duel on the plank does not own the page", "The eye must find two men with crossed swords balanced on a narrow plank over water, with a hat floating below and gulls flying up. If they fight on the quay, or the plank is not plainly narrow and over water, or the page reads as panels, the turn has not landed."),
        ("Bloodless fails", "Any blood, cut, or wound is blocking."),
        ("The pair collides or fails", "The boy clean-shaven in ochre, the man scarred, thin-moustached, hatless, in black. Blocking if either could be the other, if the scar is missing, or if Rochefort still wears his hat."),
        ("Focal generation failure", "A duplicated fighter, a third man on the plank, gross anatomy on either sword hand, or text colliding with a figure is blocking. Gulls and water are not."),
    ]),

35: dict(
    title="the bearer",
    intent="""Dramatic. Rochefort in the harbour, streaming, his hat floating beside him, and the boy on the end of the plank stooping for the folded pass where it fell out of the black coat: you stayed, I said you would. The barrier: the boy holds the pass up to the sergeant, who reads it, looks past him at the man shouting in the harbour, reads it again, and lifts the bar; the pass says let the bearer cross, signed the Cardinal; it says the bearer, you can read, and I'm the bearer; a caption says the sergeant decided he could read. From the boat's rail pulling out: Rochefort climbing the harbour stairs one-handed, soaked, his right arm held against his chest, and opening the other fist to look at what he still has: two diamonds catching the light; a caption says the boy did not know what was in the hand. The dominant turn is the pass in the boy's hand and two diamonds in a wet fist. The reader turns because the scar had two diamonds in his fist and the boy is sailing away from them. The pass is object text in the sergeant's hand.""",
    turn="The scar is in the harbour, the boy has the pass, the sergeant decides he can read, and from the boat's rail the boy sees two diamonds flash in the scar's wet fist without knowing what they are.",
    moments=[
        "Panel one, the dominant panel, about 45%, tall: Rochefort in the harbour water on the RIGHT, streaming, hatless, his hat floating beside him; the boy on the LEFT at the end of the gangplank stooping to pick up a folded paper lying on the plank. The sound cue at the water beside Rochefort. The boy's line beside him, tail to his mouth.",
        "Panel two, about 25%: the barrier; the boy on the LEFT holding the folded pass open and up to the sergeant on the RIGHT, who holds it and reads; behind the sergeant the first boat's sailors casting off; the bar lifting. The pass's single line is painted plainly on the paper in the sergeant's hand as object text, not a balloon. The boy's line upper left, tail to his mouth. The caption beside the bar, tail-free.",
        "Panel three, about 30%, from the boat's rail pulling out, the boy small at the rail in the lower LEFT foreground: on the harbour stairs on the RIGHT, Rochefort climbing out soaked, hatless, his RIGHT arm held against his chest by his left hand, and his other fist half open with two small bright stones catching the light. The caption over the grey water, tail-free.",
    ],
    locks=DART_ROAD + " " + ROCH_WET + " " + PAIR_DR + " The sergeant: red cassock, plain morion, faceless, silent, the pass in his hands. Sailors: faceless, silent. The two studs keyed to the casket plate: two diamond studs, small and bright, in the open fist.",
    exclusions="Athos, Porthos, Aramis, Constance, the Cardinal, and Buckingham are absent. No blood, no wound: the held arm is a hurt from the fall, nothing drawn on it. Rochefort's sword is gone into the water and his hat is floating. Exactly two stones in the fist, no pouch visible. The only legible object text is the one line on the pass; the barrier notice, if in frame, is far and illegible. No lettering on the boat.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/07-rochefort.png", "refs/approved/obj-letters-pass.png", "refs/approved/obj-casket-pouch-ring.png", "refs/approved/set-calais-quay.png"],
    object_text="The pass line is object text painted on the paper in the sergeant's hand, not a balloon.",
    card=[
        ("Transcription or ownership fails", "The sound cue, the boy's two lines, the pass's one line as words on the paper, and the two captions read exactly from the 600 × 900 proof, once each, in causal order; the boy's lines hang from the boy; the captions are tail-free; Rochefort, the sergeant, and the sailors carry no balloon. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: the scar in the water and the boy picking up the pass, the sergeant reading it and lifting the bar, and from the departing boat the scar climbing out one-armed with two bright stones in his fist. If the scar in the harbour with the boy stooping for the pass is not the largest image the eye finds, the turn has not landed."),
        ("Rochefort fails identity or state", "One scar across a cheek and the thin moustache unchanged; hatless, soaked, RIGHT arm held to the chest in the last panel, sword gone. A hat on his head, a sword in his hand, or the left arm held is blocking."),
        ("The two diamonds fail", "In the last panel exactly two small bright stones must catch the light in the open fist; none, one, three, or a whole pouch is blocking. Their exact cut is nonblocking."),
        ("The sergeant's choice fails", "The bar must be lifting or lifted with the pass in the sergeant's hand and the man visible in the water behind; a sergeant blocking the boy is blocking. No blood anywhere."),
        ("Focal generation failure", "A duplicated scar-man in water and on the stairs in the same panel, gross anatomy on the open fist, or a balloon across a face is blocking."),
    ]),
}

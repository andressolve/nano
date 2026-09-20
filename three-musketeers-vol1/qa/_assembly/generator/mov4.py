MOV = 4
from mov1 import C1_TAIL, DART
from mov2 import PORTHOS, ARAMIS, THREE
from mov3 import ATHOS, CONST

QLETTER = "The Queen's letter, keyed to the letters plate: a SMALL folded letter sealed in BLUE wax with a crown impressed in the seal; never the cream letter with the red seal."

PAGES = {
23: dict(
    title="she gave them away",
    intent="""Dramatic. The attic at night, a week later. Constance at the top of the stair in the attic doorway, still in her Louvre grey, white as paper; the boy up off the bed. A caption sets the interval: six nights and nobody came for her; on the seventh she came up the stair. The King gives a ball on Monday and the Queen is to wear her twelve diamond studs; then she wears them; she can't, she gave them away. Sitting on the edge of the table with her hands pressed together, the boy crouched before her: they were the King's present, she gave them to the Duke of Buckingham in London; if she comes without them the court will know, and the Cardinal smiled when the King asked her to wear them. The boy on his feet: then someone rides to London and brings them back before Monday; someone the Cardinal doesn't own; there isn't anyone. The dominant turn is the news: the ball is Monday, the diamonds are in London, and the Cardinal smiled. Constance owns the page; the boy already has his answer. The reader turns because the Queen is going to be caught on Monday, the Cardinal arranged it, and there is nobody to send.""",
    turn="Constance comes up the stair white as paper: the Queen must wear twelve diamonds on Monday, gave them away to a duke in London, and the Cardinal smiled.",
    moments=[
        "Panel one, about 25%, a strip: the attic at night by candlelight, Constance on the RIGHT at the top of the stair in the doorway, in her grey with the apron and cap, white-faced; the boy on the LEFT up off the bed. The caption upper left over the dark beam, tail-free. Three balloons A–B–A: Constance's news upper right, the boy's four words middle left, Constance's answer lower right, tails to each mouth.",
        "Panel two, the dominant panel, about 45%, close and tall: Constance sitting on the edge of the table on the RIGHT, hands pressed together, the boy crouched in front of her on the LEFT looking up. Two balloons stacked on her side, the King's present first, the court and the Cardinal's smile below it, both tails to her mouth.",
        "Panel three, about 30%: the boy on his feet on the LEFT, Constance unmoved on the RIGHT. The boy's line upper left, tail to his mouth; Constance's answer lower right, after it, tail to hers.",
    ],
    locks=DART + " " + CONST,
    exclusions="Athos, Porthos, Aramis, Rochefort, the Cardinal, and Buckingham are absent. No letter appears on this page; the Queen's letter comes out on the next. The sword stays on its nail. No blood. No lettering except the caption and the seven spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/05-constance.png", "refs/approved/set-house.png"],
    card=[
        ("Dialogue transcription or ownership fails", "The caption and all seven lines read exactly from the 600 × 900 proof, once each, in causal order; Constance's five hang from the girl in the cap and the boy's two from the boy; each reply sits after the line it answers; the caption is tail-free. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: she brings news of a ball, admits the Queen gave the diamonds away to a duke in London while the Cardinal smiled, and says there is nobody to send. If the girl on the table's edge with the boy crouched before her is not the largest image the eye finds, the turn has not landed."),
        ("Constance fails identity", "Small, freckled, dark curls under the white cap, grey dress, white apron with the small gold crown, keys. Finery or blonde hair is blocking."),
        ("d'Artagnan fails identity", "Clean-shaven, black-haired, ochre doublet, no cloak. A moustache is blocking."),
        ("Continuity fails", "No letter is visible on this page; the sword hangs on its nail; the attic is the same room as before. A letter in her hand here is blocking."),
        ("Focal generation failure", "A third figure, a duplicated girl, gross anatomy on her pressed hands, or a balloon across a face is blocking."),
    ]),

24: dict(
    title="are you asking?",
    intent="""Dramatic. The attic. Constance takes a small letter sealed in blue wax with a crown out of her bodice and holds it in both hands, not yet offering it: the Queen wrote to the Duke tonight and told her to find someone to carry it to London, and there isn't anyone. There's me, are you asking? Face to face a step apart with the letter between them, she looks at him properly for the first time: two days' hard riding to the sea and the Cardinal owns every inn, she has no right to ask; that isn't no. He takes his father's sword down off the nail while she holds the letter out to him now: one boy against the Cardinal? one boy and three friends, you haven't met them; the kitchen door at the back of the Louvre, she will be in it every night until he comes. The dominant turn is the ask that is not made and the yes that answers it. Constance owns the letter; the boy owns the sword. The reader turns because she has asked without asking and he has said yes.""",
    turn="Constance holds out the Queen's letter without asking, the boy answers the question she did not ask, and takes his sword down off the nail.",
    moments=[
        "Panel one, about 30%: Constance on the RIGHT drawing a small blue-sealed letter from her bodice and holding it in both hands against herself, not offering it; the boy on the LEFT watching the letter. Constance's line upper right, tail to her mouth; the boy's question lower left, after it, tail to his.",
        "Panel two, the dominant panel, about 45%, close and tall: the two of them face to face a step apart, the small blue-sealed letter between them in her hands, she looking at him properly for the first time. Constance's line upper right, tail to her mouth; the boy's three words lower left, after it, tail to his.",
        "Panel three, about 25%, as single-speaker beats: the boy on the LEFT reaching up to take the too-long sword down off the nail in the beam, exactly two hands on the sword; Constance on the RIGHT now holding the letter out to him. Three balloons: Constance's question upper right, the boy's answer middle left, Constance's last line lowest right, each tail to its own mouth.",
    ],
    locks=DART + " " + CONST + " " + QLETTER,
    exclusions="Athos, Porthos, Aramis, Rochefort, the Cardinal, and Buckingham are absent. The letter is small and blue-sealed with no legible writing; the cream red-sealed letter is not on this page. No blood. The sword comes off the nail in the last panel only. No lettering except the seven spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/05-constance.png", "refs/approved/obj-letters-pass.png", "refs/approved/set-house.png"],
    card=[
        ("Dialogue transcription or ownership fails", "All seven lines read exactly from the 600 × 900 proof, once each, in causal order; Constance's four hang from the girl holding the letter and the boy's three from the boy; each reply sits after the line it answers. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: she produces a small sealed letter and says there is nobody, he asks if she is asking, she says she has no right, he says that isn't no and takes his sword down while she holds the letter out. If the two of them face to face over the letter is not the largest image the eye finds, the turn has not landed."),
        ("The letter is the wrong letter", "The letter must be small with a BLUE wax seal; a cream letter with a red seal, a large sheet, or legible writing is blocking."),
        ("Constance or d'Artagnan fails identity", "The girl small in grey and white with the cap; the boy clean-shaven and black-haired in ochre. Blocking if contradicted."),
        ("Object continuity fails", "The sword must be on the nail in the first two panels and in the boy's hands in the last; the letter must end the page held out to him."),
        ("Focal generation failure", "Exactly two hands on the sword and two on the letter at the moments they are focal; a third figure, a duplicated girl, or a balloon over a face is blocking."),
    ]),

25: dict(
    title="so that one arrives",
    intent="""Dramatic. Athos's bare whitewashed room: one chair with Athos in it, one table with Aramis on its edge holding his book, one bed, a single sword on the wall, and Porthos filling the window. The boy stands in the middle holding up the small blue-sealed letter: two days to the sea, a day to London, back by Monday, it can be done, the Cardinal will try to stop him. What does the letter say? I don't know. Good, then nobody can make us tell. Porthos turns from the window delighted: London, he has never once beaten an Englishman. Aramis closes his book: in theory four riders are more than one, in practice the Cardinal will not let four through. Athos: that's why it takes four, so that one arrives. The boy looks from face to face: you haven't asked me why, not one of you. Porthos: why would we, you're going, that's the why. The dominant turn is three men deciding to ride for a reason none of them asks. Porthos gets the line. The reader turns because they are about to say the thing.""",
    turn="Three Musketeers agree to ride to London for a letter none of them has read, and when the boy notices nobody asked why, Porthos tells him why.",
    moments=[
        "Panel one, about 30%, wide: the bare whitewashed room. Athos in the one chair on the RIGHT, still; Porthos filling the window at the back; Aramis on the edge of the table with his book on the LEFT of centre; the boy standing in the middle, nearest the viewer, holding up the small blue-sealed letter. Four balloons as two single-speaker beats: the boy's plan upper left over the boy, Athos's question upper right over Athos, the boy's three words middle left, Athos's answer lower right; each tail to its own mouth, descending, none level.",
        "Panel two, the dominant panel, about 40%, close: Porthos on the LEFT turning from the window, delighted, one hand at his baldric; Aramis in the MIDDLE closing his book, two fingers at his moustache; Athos on the RIGHT in the chair, hands on his pommel. Three balloons read left to right and down: Porthos's upper left, Aramis's middle centre, Athos's lower right, each tail to its own mouth.",
        "Panel three, about 30%: the boy on the LEFT looking from one face to the next; Porthos on the RIGHT, large, arms spread. The boy's line upper left, tail to his mouth; Porthos's answer lower right, after it, tail to his.",
    ],
    locks=DART + " " + ATHOS + " " + PORTHOS + " " + ARAMIS + " " + THREE + " " + QLETTER,
    exclusions="Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. The room holds one chair, one table, one bed, and one sword on the wall, nothing else on the walls. The letter is small and blue-sealed with no legible writing. No blood; no sword drawn. No lettering except the nine spoken strings.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/03-porthos.png", "refs/approved/04-aramis.png", "refs/approved/obj-letters-pass.png", "refs/approved/set-athos-room.png"],
    card=[
        ("Dialogue transcription or ownership fails", "All nine lines read exactly from the 600 × 900 proof, once each, in causal order, each hanging by its tail from its owner: the boy's three from the boy with the letter, Athos's three from the seated man with the pointed beard, Porthos's two from the huge red-moustached man, Aramis's one from the slim blond with the book; the three-man exchange reads left to right and down. " + C1_TAIL),
        ("The turn does not land", "The page must read in order as: the boy lays out the ride, Athos is glad nobody knows what the letter says, the three each say yes in his own way, and the boy notices nobody asked why. If the three faces answering is not the image the eye finds, the turn has not landed."),
        ("The three Musketeers collide", "Athos tall, dark, pointed beard, seated, no sling; Porthos huge, red curls, waxed moustache, gold baldric, at the window; Aramis slim, blond, small moustache, book. Any two merging is blocking."),
        ("The letter or d'Artagnan fails", "The boy clean-shaven in ochre holding a small blue-sealed letter; a red-sealed cream letter here, or a moustached boy, is blocking."),
        ("The room fails", "A bare whitewashed room with one sword on the wall; a cluttered or decorated room with pictures or many weapons is blocking because it contradicts who Athos is. Exact furniture proportion is nonblocking."),
        ("Focal generation failure", "A fifth figure, a duplicated Musketeer, gross anatomy on the boy's hand with the letter, or a balloon across a face is blocking."),
    ]),

26: dict(
    title="all for one",
    intent="""Spectacle. Four sword points meeting above the table, four hands on four hilts, four faces lit from below by the one candle: Athos grave, Porthos huge and grinning, Aramis with one eyebrow up, and the boy looking as if he might cry and would rather die first. Athos says it, all four answer it, and one caption admits nobody had said it before and after that nobody had to. The dominant turn is the oath: four swords, all for one, one for all. The four own the page equally. The reader turns because they have said it and the sun comes up in an hour. The bare room is dark around the candle; nothing else is in the picture.""",
    turn="Four sword points meet over a candle in a bare room, and four men say the thing for the first time.",
    moments=[
        "One image, the whole page, about 100%: the bare room dark, one candle on the table throwing light upward. Four sword points meeting in the air above the candle at the centre of the page; four hands on four hilts converging; four faces lit from below around the meeting point: Athos on the RIGHT grave, Porthos at the back huge and grinning, Aramis on the LEFT with one eyebrow up, the boy nearest the viewer looking as if he might cry and would rather die first. Athos's three-word balloon beside his mouth on the right, tail to him. The shared answer as one balloon at the centre above the blades with four short tails, one to each mouth, or as four small identical balloons each at its own mouth; either way the words appear once and the owner tag is never lettered. The caption along the lower edge under the candlelight, tail-free.",
        "Nothing else is lettered; the walls are bare; the single sword on the wall is unfocal or out of frame.",
    ],
    locks=DART + " " + ATHOS + " " + PORTHOS + " " + ARAMIS + " " + THREE,
    exclusions="Constance, Rochefort, the Cardinal, and Buckingham are absent. Athos has no sling. Exactly four swords and four hands. No blood. The words are lettered once; if four balloons are used they must be one string shared, not four copies counted as four. No name plates, no laugh lines.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/02-athos.png", "refs/approved/03-porthos.png", "refs/approved/04-aramis.png", "refs/approved/set-athos-room.png"],
    card=[
        ("Transcription or ownership fails", "Athos's three words hang from Athos alone; the shared four-word answer reads once and belongs plainly to all four by tails or placement; the caption is tail-free along the bottom; nothing else is lettered. Four separate copies of the answer, or the answer hanging from one man only, is blocking. " + C1_TAIL),
        ("The oath does not own the page", "The eye must find four sword points meeting above a candle and four faces lit from below. If the page reads as panels, or the swords do not meet, or fewer than four faces are lit, the turn has not landed."),
        ("The four fail identity", "Athos grave and bearded, Porthos huge and grinning with the waxed moustache, Aramis slim and blond with one eyebrow up, the boy clean-shaven and near tears. Any face missing, duplicated, or merged is blocking."),
        ("Count or state fails", "Exactly four swords, four hands on hilts, no sling on Athos, no blood. A fifth blade or hand is blocking."),
        ("Focal generation failure", "Gross anatomy on any of the four hands at the hilts, a face with two mouths, or a balloon across a face is blocking. Candle flare and shadow are not."),
    ]),

27: dict(
    title="the Saint-Denis gate",
    intent="""Illustrated prose, two locations because the leaving is the turn: the attic before dawn, and the Saint-Denis gate at sunrise. The smaller image is the attic by candlelight: Constance sewing the small blue-sealed letter into the lining of the boy's ochre coat with tiny stitches while he watches her hands. The dominant image is the gate: four riders going through it at a canter as the sun comes up, the boy in ochre in the middle on a tall bay, Porthos's red plumes, Aramis's white one, Athos on the outside, and above the street behind them, small, a girl in a white cap at an attic window. The prose carries the stitches, her hands flat on his chest, the come back she does not say, the yellow horse left behind, and the window watched until the road is empty. The dominant turn is the letter in the coat and four riders through the gate at dawn. Constance owns the first half; the four own the second. The reader turns because it is four riders, one letter, two days to the sea, and the Cardinal owns every inn on the road.""",
    turn="Constance sews the Queen's letter into the boy's coat without saying come back, and four riders go out through the Saint-Denis gate at sunrise.",
    moments=[
        "Panel one, about 40%: the attic by candlelight before dawn. Constance on the RIGHT sewing, the small blue-sealed letter half inside the lining of the ochre coat across her lap, needle and thread in her fingers; the boy on the LEFT in his shirt, watching her hands. Exactly two hands doing the sewing.",
        "Panel two, the dominant image, about 60%, wide and tall: the Saint-Denis gate, a great stone arch, at sunrise, four riders coming through it toward the viewer at a canter: the boy in ochre on a tall bay horse in the MIDDLE, Porthos on one side with the three red plumes, Aramis with the single white plume, Athos on the outside; behind and above them, over the rooftops of a narrow street, small, a girl in a white cap at an attic window. The yellow horse is nowhere on this page.",
        "The prose field sits over the dawn sky above the gate in panel two, a matte parchment field across most of the width, never over the four riders or over the two hands sewing. Two paragraphs. No other lettering.",
    ],
    locks=DART + " " + CONST + " " + ATHOS + " " + PORTHOS + " " + ARAMIS + " " + THREE + " " + QLETTER + " The boy's horse on this page is a tall bay, not the yellow horse.",
    exclusions="Rochefort, the Cardinal, and Buckingham are absent. The yellow horse does not appear. Athos has no sling. The letter in the coat is the small blue-sealed one, no legible writing. No blood. No lettering except the one prose field; no words on the gate.",
    inputs=["refs/approved/01-dartagnan.png", "refs/approved/05-constance.png", "refs/approved/02-athos.png", "refs/approved/03-porthos.png", "refs/approved/04-aramis.png", "refs/approved/set-paris.png"],
    card=[
        ("Prose transcription", "The prose field reads exactly, both paragraphs in order, once, from the 600 × 900 proof, over plain ground and never over the riders or the sewing hands, with no other text on the page including on the gate. " + C1_TAIL),
        ("The gate does not own the page", "The eye must find first four riders coming through a great arch at sunrise with the boy in the middle, and second the small warm image of a girl sewing a letter into a coat. If the sewing competes, or the page reads as a comic strip, the turn has not landed."),
        ("The four fail identity", "Four riders: the clean-shaven boy in ochre on a bay, the huge red-plumed Porthos, the slim white-plumed Aramis, the tall bearded Athos without a sling. A fifth rider, a missing one, or the yellow horse is blocking."),
        ("Constance or the letter fails", "The girl in the cap sewing a small blue-sealed letter into an ochre coat; a red-sealed letter or a girl in finery is blocking."),
        ("Focal generation failure", "Gross anatomy on the sewing hands, a duplicated rider, or the prose field over a face is blocking. Gate stonework and sky are not."),
    ]),
}

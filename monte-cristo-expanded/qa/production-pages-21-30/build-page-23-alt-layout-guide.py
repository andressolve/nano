from pathlib import Path

from PIL import Image, ImageDraw


OUT = Path(__file__).with_name("page-23-alt-layout-guide.png")
image = Image.new("RGB", (1024, 1536), "#111417")
draw = ImageDraw.Draw(image)


def panel(box):
    draw.rounded_rectangle(box, radius=6, fill="#34383a", outline="#050607", width=8)


def balloon(box, radius=64, tail=None):
    draw.rounded_rectangle(box, radius=radius, fill="#f2e8cc", outline="#5a4a3a", width=6)
    if tail:
        draw.polygon(tail, fill="#f2e8cc", outline="#5a4a3a")


panel((80, 80, 944, 320))
panel((80, 344, 944, 584))
panel((80, 608, 944, 828))
panel((80, 852, 944, 1222))
panel((80, 1246, 944, 1436))

# P1: a stone edge overlaps a schematic ear/face; one large safe balloon.
draw.rectangle((84, 84, 342, 316), fill="#667074")
draw.ellipse((312, 132, 388, 272), fill="#b37a55", outline="#d49a6a", width=10)
draw.polygon(((340, 90), (492, 82), (585, 210), (532, 294), (354, 312)), fill="#73818a")
draw.rounded_rectangle((132, 224, 244, 262), radius=10, fill="#d7ae55")
balloon((544, 102, 914, 292), radius=78, tail=((566, 250), (518, 242), (554, 220)))

# P2: left Voice field, right speaker/reply, visible tool, closed seam.
balloon((94, 366, 466, 556), radius=72, tail=((420, 534), (462, 564), (444, 514)))
draw.ellipse((580, 386, 800, 550), fill="#73818a")
draw.ellipse((646, 382, 722, 458), fill="#b37a55")
draw.line((606, 520, 480, 558), fill="#bd7745", width=14)
draw.line((100, 566, 918, 566), fill="#9a734d", width=5)
balloon((650, 370, 926, 520), radius=64, tail=((668, 472), (704, 440), (690, 486)))

# P3: same speaker lanes with a closed hairline seam.
balloon((94, 630, 466, 800), radius=68, tail=((424, 782), (470, 812), (448, 760)))
draw.ellipse((596, 648, 804, 788), fill="#73818a")
draw.ellipse((656, 646, 728, 718), fill="#b37a55")
draw.line((100, 810, 918, 810), fill="#9a734d", width=4)
balloon((650, 640, 926, 786), radius=62, tail=((666, 748), (706, 716), (688, 762)))

# P4: first opening, raised slab, A-B-A balloons, smaller figure on right.
draw.ellipse((250, 1000, 650, 1210), fill="#060809")
draw.polygon(((250, 1020), (520, 920), (646, 1008), (382, 1090)), fill="#687075", outline="#23282a")
balloon((94, 874, 466, 1084), radius=72, tail=((408, 1058), (388, 1154), (454, 1082)))
draw.ellipse((628, 968, 860, 1172), fill="#73818a")
draw.ellipse((678, 946, 754, 1022), fill="#b37a55")
balloon((644, 880, 926, 1026), radius=62, tail=((660, 982), (704, 962), (674, 1006)))
balloon((102, 1100, 358, 1198), radius=46, tail=((324, 1154), (414, 1178), (352, 1128)))

# P5: silent black opening plus one five-digit hand schematic.
draw.ellipse((268, 1262, 756, 1438), fill="#060809")
draw.polygon(
    (
        (500, 1420), (494, 1348), (456, 1306), (470, 1294), (510, 1330),
        (504, 1272), (520, 1268), (530, 1324), (540, 1260), (556, 1264),
        (552, 1328), (574, 1278), (590, 1286), (568, 1340), (604, 1308),
        (616, 1320), (564, 1376), (554, 1424),
    ),
    fill="#b37a55",
    outline="#d49a6a",
)

image.save(OUT)

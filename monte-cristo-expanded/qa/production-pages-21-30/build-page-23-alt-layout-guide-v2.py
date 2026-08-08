from pathlib import Path

from PIL import Image, ImageDraw


OUT = Path(__file__).with_name("page-23-alt-layout-guide-v2.png")
image = Image.new("RGB", (1024, 1536), "#111417")
draw = ImageDraw.Draw(image)


def panel(box):
    draw.rounded_rectangle(box, radius=6, fill="#34383a", outline="#050607", width=8)


def balloon(box, radius=62, tail=None):
    draw.rounded_rectangle(box, radius=radius, fill="#f2e8cc", outline="#5a4a3a", width=6)
    if tail:
        draw.polygon(tail, fill="#f2e8cc", outline="#5a4a3a")


# Doubled visual frame to survive model compression.
panel((128, 88, 896, 320))
panel((128, 344, 896, 584))
panel((128, 608, 896, 828))
panel((128, 852, 896, 1222))
panel((128, 1246, 896, 1436))

# P1: left stone, ear pinned at its right edge, head/nose explicitly points right.
draw.rectangle((132, 92, 318, 316), fill="#667074")
draw.ellipse((292, 152, 350, 252), fill="#b37a55", outline="#d49a6a", width=8)
draw.polygon(((330, 118), (452, 116), (548, 188), (590, 206), (546, 230), (450, 294), (334, 288)), fill="#73818a")
draw.ellipse((528, 202, 546, 212), fill="#1d2428")
draw.rounded_rectangle((152, 236, 246, 268), radius=10, fill="#d7ae55")
balloon((540, 108, 876, 290), radius=72, tail=((548, 232), (516, 232), (544, 216)))

# P2.
balloon((146, 368, 500, 556), radius=68, tail=((444, 532), (486, 566), (468, 512)))
draw.ellipse((570, 388, 778, 550), fill="#73818a")
draw.ellipse((626, 386, 700, 460), fill="#b37a55")
draw.line((602, 520, 484, 562), fill="#bd7745", width=14)
draw.line((140, 566, 884, 566), fill="#9a734d", width=5)
balloon((604, 370, 876, 520), radius=60, tail=((628, 474), (676, 442), (650, 490)))

# P3.
balloon((146, 630, 500, 800), radius=64, tail=((444, 780), (488, 812), (468, 758)))
draw.ellipse((574, 650, 782, 788), fill="#73818a")
draw.ellipse((632, 646, 704, 718), fill="#b37a55")
draw.line((140, 810, 884, 810), fill="#9a734d", width=4)
balloon((604, 640, 876, 786), radius=58, tail=((628, 748), (678, 716), (648, 764)))

# P4.
draw.ellipse((286, 1000, 642, 1210), fill="#060809")
draw.polygon(((260, 1020), (514, 920), (620, 1008), (380, 1090)), fill="#687075", outline="#23282a")
balloon((146, 874, 500, 1084), radius=68, tail=((438, 1056), (398, 1156), (476, 1080)))
draw.ellipse((610, 972, 818, 1174), fill="#73818a")
draw.ellipse((650, 946, 724, 1020), fill="#b37a55")
balloon((602, 880, 876, 1026), radius=58, tail=((626, 982), (676, 960), (646, 1006)))
balloon((150, 1100, 394, 1198), radius=44, tail=((356, 1154), (438, 1180), (384, 1128)))

# P5: silent single hand.
draw.ellipse((294, 1262, 730, 1438), fill="#060809")
draw.polygon(
    ((500, 1420), (494, 1348), (456, 1306), (470, 1294), (510, 1330),
     (504, 1272), (520, 1268), (530, 1324), (540, 1260), (556, 1264),
     (552, 1328), (574, 1278), (590, 1286), (568, 1340), (604, 1308),
     (616, 1320), (564, 1376), (554, 1424)),
    fill="#b37a55",
    outline="#d49a6a",
)

image.save(OUT)

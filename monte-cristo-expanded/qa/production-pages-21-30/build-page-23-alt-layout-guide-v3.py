from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).parent
source = ROOT / "page-23-alt-layout-guide-v2.png"
out = ROOT / "page-23-alt-layout-guide-v3.png"
image = Image.open(source).convert("RGB")
draw = ImageDraw.Draw(image)


def clear_panel(box):
    draw.rectangle(box, fill="#34383a")


def balloon(box, radius=62, tail=None):
    draw.rounded_rectangle(box, radius=radius, fill="#f2e8cc", outline="#5a4a3a", width=6)
    if tail:
        draw.polygon(tail, fill="#f2e8cc", outline="#5a4a3a")


# P1: the wall deliberately crosses the ear; nose points right; tail reaches mouth lane.
clear_panel((132, 92, 892, 316))
draw.rectangle((132, 92, 410, 316), fill="#667074")
draw.ellipse((378, 152, 442, 254), fill="#b37a55", outline="#d49a6a", width=8)
draw.polygon(((414, 118), (500, 116), (560, 170), (606, 204), (560, 234), (500, 294), (416, 288)), fill="#73818a")
draw.ellipse((544, 202, 562, 212), fill="#1d2428")
draw.rounded_rectangle((156, 236, 250, 268), radius=10, fill="#d7ae55")
balloon((526, 108, 866, 290), radius=72, tail=((526, 230), (426, 226), (526, 208)))

# P2: wider Voice field; reply tail reaches far into mouth lane.
clear_panel((132, 348, 892, 580))
balloon((140, 366, 530, 558), radius=68, tail=((468, 532), (498, 566), (486, 512)))
draw.ellipse((544, 388, 766, 550), fill="#73818a")
draw.ellipse((592, 386, 668, 462), fill="#b37a55")
draw.line((584, 520, 486, 562), fill="#bd7745", width=14)
draw.line((140, 566, 884, 566), fill="#9a734d", width=5)
balloon((580, 370, 872, 520), radius=60, tail=((580, 468), (472, 442), (580, 494)))

# P3: same protected fields and extended local reply tail.
clear_panel((132, 612, 892, 824))
balloon((140, 630, 530, 800), radius=64, tail=((470, 780), (500, 812), (488, 758)))
draw.ellipse((544, 650, 766, 788), fill="#73818a")
draw.ellipse((594, 646, 668, 720), fill="#b37a55")
draw.line((140, 810, 884, 810), fill="#9a734d", width=4)
balloon((580, 640, 872, 786), radius=58, tail=((580, 744), (472, 716), (580, 770)))

# P4: preserve opening sources; extend Edmond reply to mouth lane; widen upper Voice.
clear_panel((132, 856, 892, 1218))
draw.ellipse((286, 1000, 642, 1210), fill="#060809")
draw.polygon(((260, 1020), (514, 920), (620, 1008), (380, 1090)), fill="#687075", outline="#23282a")
balloon((140, 874, 530, 1086), radius=68, tail=((466, 1056), (398, 1156), (500, 1080)))
draw.ellipse((574, 972, 808, 1174), fill="#73818a")
draw.ellipse((614, 946, 690, 1022), fill="#b37a55")
balloon((580, 880, 872, 1026), radius=58, tail=((580, 976), (472, 956), (580, 1004)))
balloon((146, 1100, 394, 1198), radius=44, tail=((356, 1154), (438, 1180), (384, 1128)))

image.save(out)

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).parent
image = Image.open(ROOT / "page-23-alt-layout-guide-v3.png").convert("RGB")
draw = ImageDraw.Draw(image)


def clear_panel(box):
    draw.rectangle(box, fill="#34383a")


def balloon(box, radius=62, tail=None):
    draw.rounded_rectangle(box, radius=radius, fill="#f2e8cc", outline="#5a4a3a", width=6)
    if tail:
        draw.polygon(tail, fill="#f2e8cc", outline="#5a4a3a")


# P1: keep the through-ear wall; bring the question inward and put its tail at mouth.
clear_panel((132, 92, 892, 316))
draw.rectangle((132, 92, 410, 316), fill="#667074")
draw.ellipse((378, 152, 442, 254), fill="#b37a55", outline="#d49a6a", width=8)
draw.polygon(((414, 118), (488, 116), (538, 166), (572, 202), (538, 236), (488, 294), (416, 288)), fill="#73818a")
draw.ellipse((526, 200, 544, 210), fill="#1d2428")
draw.rounded_rectangle((156, 236, 250, 268), radius=10, fill="#d7ae55")
balloon((548, 108, 850, 290), radius=68, tail=((548, 228), (524, 218), (548, 206)))

# P2: Voice left; reply balloon inward and immediately LEFT of far-right face.
clear_panel((132, 348, 892, 580))
balloon((142, 366, 500, 558), radius=66, tail=((458, 532), (490, 566), (478, 512)))
draw.ellipse((700, 392, 878, 552), fill="#73818a")
draw.ellipse((790, 386, 864, 460), fill="#b37a55")
draw.line((718, 520, 506, 562), fill="#bd7745", width=12)
draw.line((140, 566, 884, 566), fill="#9a734d", width=5)
balloon((566, 370, 790, 520), radius=56, tail=((790, 444), (814, 430), (790, 470)))

# P3: same inward reply-left / face-right staging.
clear_panel((132, 612, 892, 824))
balloon((142, 630, 500, 800), radius=62, tail=((458, 780), (492, 812), (478, 758)))
draw.ellipse((700, 650, 878, 790), fill="#73818a")
draw.ellipse((790, 646, 864, 720), fill="#b37a55")
draw.line((140, 810, 884, 810), fill="#9a734d", width=4)
balloon((566, 640, 790, 786), radius=54, tail=((790, 716), (814, 704), (790, 744)))

# P4: preserve opening; reply immediately left of far-right face.
clear_panel((132, 856, 892, 1218))
draw.ellipse((286, 1000, 642, 1210), fill="#060809")
draw.polygon(((260, 1020), (514, 920), (620, 1008), (380, 1090)), fill="#687075", outline="#23282a")
balloon((142, 874, 500, 1086), radius=66, tail=((452, 1056), (398, 1156), (480, 1080)))
draw.ellipse((690, 972, 876, 1174), fill="#73818a")
draw.ellipse((786, 946, 862, 1022), fill="#b37a55")
balloon((566, 880, 790, 1026), radius=54, tail=((790, 958), (814, 944), (790, 984)))
balloon((146, 1100, 394, 1198), radius=44, tail=((356, 1154), (438, 1180), (384, 1128)))

image.save(ROOT / "page-23-alt-layout-guide-v4.png")

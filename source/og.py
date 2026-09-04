"""Builds og-image.png (1200x630), the social-share card, from OG in content.py.
Run from the repo root: python3 source/og.py"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from content import OG

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
P = OG["palette"]  # primary, dark, gold, paper, sky, far, mid, green

def font(size, bold=True):
    for c in ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()
def sans(size):
    for c in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

img = Image.new("RGB", (W, H), P["paper"])
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=tuple(int(P["paper"][i] * (1 - t) + P["sky"][i] * t) for i in range(3)))
d.ellipse([940, 60, 1080, 200], fill=P["gold"])
d.polygon([(0, 430), (200, 400), (420, 420), (700, 392), (960, 416), (1200, 396), (1200, 630), (0, 630)], fill=P["far"])
d.polygon([(0, 470), (260, 440), (520, 474), (800, 452), (1040, 472), (1200, 456), (1200, 630), (0, 630)], fill=P["mid"])
d.polygon([(0, 500), (300, 492), (600, 506), (900, 496), (1200, 504), (1200, 630), (0, 630)], fill=P["primary"])
cx, cy, r = 120, 120, 54
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=P["primary"])
if OG.get("mark") == "star5":
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = 36 if i % 2 == 0 else 15
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=P["gold"])
elif OG.get("mark") == "sun":
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=P["gold"])
    for i in range(12):
        a = i * math.pi / 6
        d.line([(cx + 28 * math.cos(a), cy + 28 * math.sin(a)), (cx + 40 * math.cos(a), cy + 40 * math.sin(a))], fill=P["gold"], width=5)
elif OG.get("mark") == "arch":
    d.arc([cx - 34, cy - 30, cx + 34, cy + 44], 180, 360, fill=P["gold"], width=14)
    d.rectangle([cx - 34, cy + 6, cx - 20, cy + 40], fill=P["gold"]); d.rectangle([cx + 20, cy + 6, cx + 34, cy + 40], fill=P["gold"])
else:
    d.polygon([(cx, cy - 34), (cx + 9, cy - 9), (cx + 34, cy), (cx + 9, cy + 9), (cx, cy + 34), (cx - 9, cy + 9), (cx - 34, cy), (cx - 9, cy - 9)], fill=P["gold"])
d.text((200, 78), "ECOS Medicare Solutions", font=sans(30), fill=(70, 83, 94))
d.text((200, 118), OG["line1"], font=font(74), fill=(28, 38, 48))
d.text((200, 200), OG["line2"], font=font(96), fill=P["primary"])
d.text((200, 318), OG["sub1"], font=sans(26), fill=(70, 83, 94))
d.text((200, 352), OG["sub2"], font=sans(26), fill=(70, 83, 94))
pw = 226 + int(sans(24).getlength(OG["domain"])) + 26
d.rounded_rectangle([200, 536, pw, 592], radius=28, fill=P["dark"])
d.text((226, 549), OG["domain"], font=sans(24), fill=(255, 255, 255))
d.text((pw + 24, 552), "Darin Weidauer, MBA, RSSA · NPN 18580338", font=sans(20), fill=P["paper"])
img.save(ROOT / "og-image.png", optimize=True)
print("wrote og-image.png", (ROOT / "og-image.png").stat().st_size, "bytes")

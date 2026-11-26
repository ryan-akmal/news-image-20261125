#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news front page (1024x1024 PNG).

All artwork is original: every pictogram is assembled from flat Pillow
shapes, every word is set in DejaVu. No photograph, no borrowed art, no
network access. Deterministic: same input, same bytes.
Run:  python3 generate_image.py   (writes entry.png here)
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
INK = (24, 32, 48)
NAVY = (16, 30, 58)
GOLD = (233, 196, 106)
CRIMSON = (178, 34, 34)
MUTED = (98, 98, 98)
GREY = (64, 64, 64)
CARD_EDGE = (205, 200, 190)
STRIP = (234, 228, 214)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, face, width):
    """Greedy word wrap by pixel width."""
    rows, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=face) <= width:
            cur = trial
        else:
            if cur:
                rows.append(cur)
            cur = word
    if cur:
        rows.append(cur)
    return rows


def block(d, x, y, text, face, colour, width, step):
    for line in wrap(d, text, face, width):
        d.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def flame(d, cx, base, w, h):
    """A two-tone flame polygon rising from (cx, base)."""
    d.polygon([(cx - w, base), (cx - w * 0.55, base - h * 0.55),
               (cx - w * 0.10, base - h * 0.80), (cx + w * 0.25, base - h),
               (cx + w * 0.55, base - h * 0.55), (cx + w, base - h * 0.30),
               (cx + w * 0.45, base)], fill=(230, 126, 34))
    d.polygon([(cx - w * 0.45, base), (cx - w * 0.15, base - h * 0.45),
               (cx + w * 0.20, base - h * 0.55), (cx + w * 0.45, base)],
              fill=(246, 200, 70))


def smoke(d, cx, cy, r, colour=(168, 168, 168)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour)


# ---------- pictograms, each drawn inside a square of side s ----------
def pic_tanker(d, x, y, s):
    # Oil tanker on waves, flames licking the deck.
    hull_top = y + s * 0.52
    d.polygon([(x + s * 0.06, hull_top), (x + s * 0.94, hull_top),
               (x + s * 0.86, y + s * 0.80), (x + s * 0.14, y + s * 0.80)],
              fill=(52, 68, 96), outline=NAVY, width=3)
    d.rectangle([x + s * 0.66, y + s * 0.30, x + s * 0.88, hull_top],
                fill=(70, 88, 120), outline=NAVY, width=3)
    d.rectangle([x + s * 0.20, y + s * 0.38, x + s * 0.30, hull_top],
                fill=(232, 194, 104), outline=NAVY, width=2)
    d.rectangle([x + s * 0.38, y + s * 0.38, x + s * 0.48, hull_top],
                fill=(232, 194, 104), outline=NAVY, width=2)
    flame(d, x + s * 0.24, y + s * 0.40, 22, 34)
    flame(d, x + s * 0.55, y + s * 0.52, 26, 40)
    for wy in (y + s * 0.84, y + s * 0.90):
        d.arc([x + s * 0.05, wy, x + s * 0.95, wy + 8], 0, 180,
              fill=(42, 110, 143), width=4)


def pic_refinery(d, x, y, s):
    # Two refinery towers with pipes, a flame and drifting smoke.
    d.rectangle([x + s * 0.14, y + s * 0.34, x + s * 0.34, y + s * 0.94],
                fill=(96, 104, 122), outline=NAVY, width=3)
    d.rectangle([x + s * 0.42, y + s * 0.22, x + s * 0.60, y + s * 0.94],
                fill=(70, 78, 96), outline=NAVY, width=3)
    d.rectangle([x + s * 0.66, y + s * 0.55, x + s * 0.90, y + s * 0.94],
                fill=(122, 96, 78), outline=NAVY, width=3)
    for wy in (y + s * 0.44, y + s * 0.62, y + s * 0.80):
        d.rectangle([x + s * 0.18, wy, x + s * 0.30, wy + 8],
                    fill=(232, 194, 104))
        d.rectangle([x + s * 0.46, wy, x + s * 0.56, wy + 8],
                    fill=(232, 194, 104))
    flame(d, x + s * 0.51, y + s * 0.24, 20, 32)
    smoke(d, x + s * 0.74, y + s * 0.16, 13)
    smoke(d, x + s * 0.86, y + s * 0.08, 10)


def pic_tanks(d, x, y, s):
    # Round storage tanks at an oil terminal, one on fire.
    for i, (fx, fw) in enumerate(((0.08, 0.34), (0.46, 0.34))):
        tx = x + s * fx
        d.rectangle([tx, y + s * 0.46, tx + s * fw, y + s * 0.92],
                    fill=(150, 158, 172), outline=NAVY, width=3)
        d.ellipse([tx, y + s * 0.38, tx + s * fw, y + s * 0.54],
                  fill=(190, 196, 206), outline=NAVY, width=3)
    flame(d, x + s * 0.63, y + s * 0.42, 24, 44)
    smoke(d, x + s * 0.80, y + s * 0.18, 12)
    smoke(d, x + s * 0.68, y + s * 0.10, 9)
    d.rectangle([x + s * 0.06, y + s * 0.92, x + s * 0.94, y + s * 0.97],
                fill=(64, 64, 64))


def pic_ruin(d, x, y, s):
    # A damaged apartment block with a jagged top and dust clouds.
    bx, by = x + s * 0.12, y + s * 0.30
    d.polygon([(bx, by + s * 0.20), (bx + s * 0.10, by + s * 0.08),
               (bx + s * 0.20, by + s * 0.16), (bx + s * 0.30, by),
               (bx + s * 0.38, by + s * 0.12), (bx + s * 0.38, by + s * 0.64),
               (bx, by + s * 0.64)], fill=(70, 78, 96), outline=NAVY, width=3)
    d.rectangle([bx + s * 0.46, by + s * 0.12, bx + s * 0.80, by + s * 0.64],
                fill=(96, 104, 122), outline=NAVY, width=3)
    for wy in (by + 18, by + 38, by + 58):
        d.rectangle([bx + s * 0.52, wy, bx + s * 0.52 + 12, wy + 9],
                    fill=(232, 194, 104))
        d.rectangle([bx + s * 0.66, wy, bx + s * 0.66 + 12, wy + 9],
                    fill=(60, 60, 60))
    smoke(d, x + s * 0.24, y + s * 0.12, 12)
    smoke(d, x + s * 0.40, y + s * 0.06, 9, (190, 190, 190))


def pic_chart(d, x, y, s):
    # Axes and a steep falling line with a down arrow.
    d.line([(x + s * 0.14, y + s * 0.10), (x + s * 0.14, y + s * 0.88)],
           fill=INK, width=4)
    d.line([(x + s * 0.14, y + s * 0.88), (x + s * 0.92, y + s * 0.88)],
           fill=INK, width=4)
    pts = [(x + s * 0.22, y + s * 0.30), (x + s * 0.40, y + s * 0.36),
           (x + s * 0.58, y + s * 0.48), (x + s * 0.76, y + s * 0.66),
           (x + s * 0.88, y + s * 0.80)]
    d.line(pts, fill=CRIMSON, width=6, joint="curve")
    d.polygon([(pts[-1][0] - 2, pts[-1][1] + 14), (pts[-1][0] - 14, pts[-1][1] - 6),
               (pts[-1][0] + 12, pts[-1][1] - 6)], fill=CRIMSON)
    for px, py in pts:
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=CRIMSON)


def pic_gavel(d, x, y, s):
    # A judge's gavel resting on its sound block.
    d.rectangle([x + s * 0.16, y + s * 0.30, x + s * 0.62, y + s * 0.48],
                fill=(122, 84, 48), outline=NAVY, width=3)
    d.rectangle([x + s * 0.52, y + s * 0.44, x + s * 0.92, y + s * 0.58],
                fill=(96, 64, 36), outline=NAVY, width=3)
    d.rectangle([x + s * 0.30, y + s * 0.72, x + s * 0.74, y + s * 0.84],
                fill=(150, 110, 60), outline=NAVY, width=3)
    burst(d, x + s * 0.80, y + s * 0.16, 12, 5, 6, (255, 220, 120))


def burst(d, cx, cy, r_out, r_in, points, colour):
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / points - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=colour)


PANELS = [
    # (tag, accent, headline, caption, pictogram)
    ("UKRAINE", (42, 110, 143), "UKRAINE HITS TWO REFINERIES",
     "Drones hit the Syzran and Kuibyshev refineries overnight; fires, "
     "one killed, 145 drones downed.", pic_refinery),
    ("YEMEN \u2022 SAUDI ARABIA", (120, 40, 32), "HOUTHIS HIT RAS TANURA",
     "Houthis say they attacked Saudi Arabia's Ras Tanura oil refinery; "
     "fires reported at the terminal.", pic_tanks),
    ("GAZA", (178, 34, 34), "ISRAEL KILLS HAMAS COLONEL",
     "A strike kills Hamas security colonel Mohammad Abuelouf, his wife "
     "and two children in Gaza City.", pic_ruin),
    ("MARKETS", (155, 34, 38), "ASIAN STOCKS TUMBLE",
     "KOSPI -6.16%, Nikkei -2.78%; Nasdaq -1.5% Tuesday, S&P 500 -0.5% "
     "for an eighth loss in nine days.", pic_chart),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.text((W // 2, 12), "THE WORLD IN ONE DAY",
           font=font(SERIF, 54), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 80), "WEDNESDAY  \u2022  25 NOVEMBER 2026",
           font=font(BOLD, 30), fill=GOLD, anchor="ma")
    d.rectangle([0, 128, W, 134], fill=GOLD)

    # Standfirst
    block(d, 28, 146,
          "Six stories that defined the day: tankers ablaze in Hormuz, "
          "drones over Russian refineries, Ras Tanura hit, a Hamas colonel "
          "killed in Gaza, markets tumbling \u2014 and Huawei convicted.",
          font(PLAIN, 19), INK, W - 56, 25)

    # Lead story, full width
    lx, ly, lw, lh = 24, 206, W - 48, 156
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=(255, 255, 255),
                outline=CARD_EDGE, width=2)
    d.rectangle([lx, ly, lx + lw, ly + 30], fill=(120, 40, 32))
    d.text((lx + 14, ly + 3), "MIDDLE EAST  \u2022  STRAIT OF HORMUZ",
           font=font(BOLD, 18), fill=(255, 255, 255))
    pic_tanker(d, lx + lw - 168, ly + 38, 124)
    block(d, lx + 16, ly + 42, "TANKERS ABLAZE IN HORMUZ",
          font(BOLD, 31), INK, lw - 200, 38)
    block(d, lx + 16, ly + 90,
          "Iran's Revolutionary Guard says two oil tankers struck naval "
          "mines and caught fire in the strait; the vessels were on an "
          "unauthorised route, Tehran says.",
          font(PLAIN, 18), GREY, lw - 200, 24)

    # Four panels: 2 columns x 2 rows
    gx, gy = 24, 378
    pw, ph, gap = 480, 176, 16
    for i, (tag, accent, head, cap, pic) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x0 = gx + col * (pw + gap)
        y0 = gy + row * (ph + gap)
        d.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(255, 255, 255),
                    outline=CARD_EDGE, width=2)
        d.rectangle([x0, y0, x0 + pw, y0 + 30], fill=accent)
        d.text((x0 + 14, y0 + 3), tag, font=font(BOLD, 18),
               fill=(255, 255, 255))
        pic(d, x0 + 10, y0 + 40, 118)
        block(d, x0 + 140, y0 + 42, head, font(BOLD, 24), INK,
              pw - 156, 29)
        block(d, x0 + 140, y0 + 106, cap, font(PLAIN, 16),
              GREY, pw - 156, 21)

    # Tech panel, full width
    sx, sy, sw, sh = 24, 762, W - 48, 84
    d.rectangle([sx, sy, sx + sw, sy + sh], fill=(255, 255, 255),
                outline=CARD_EDGE, width=2)
    d.rectangle([sx, sy, sx + 150, sy + sh], fill=(28, 92, 58))
    d.text((sx + 75, sy + 26), "TECH", font=font(BOLD, 22),
           fill=(255, 255, 255), anchor="ma")
    pic_gavel(d, sx + 158, sy + 6, 66)
    block(d, sx + 232, sy + 10, "HUAWEI CONVICTED",
          font(BOLD, 25), INK, sw - 250, 31)
    block(d, sx + 232, sy + 44,
          "A Brooklyn jury convicts Huawei on 10 of 12 counts, including "
          "bank fraud, wire fraud, sanctions violations and trade-secret "
          "theft.",
          font(PLAIN, 16), GREY, sw - 250, 21)

    # Also in the news
    ay = 862
    d.rectangle([24, ay, W - 24, ay + 78], fill=STRIP,
                outline=CARD_EDGE, width=2)
    block(d, 40, ay + 8,
          "ALSO IN THE NEWS:  Poland seeks a permanent US troop presence  "
          "\u2022  Sudan: RSF strikes kill 19 civilians  \u2022  Colombia "
          "frees Cartagena hostages  \u2022  Australia\u2013Solomon Islands "
          "treaty signed  \u2022  Bogor mine toll rises to six  \u2022  "
          "Shenzhou-24 docks with Tiangong",
          font(BOLD, 15), INK, W - 80, 21)

    # Footer
    d.text((W // 2, H - 26),
           "Sources: Just Security, The Independent, AP, Reuters \u2014 "
           "reported 25 November 2026",
           font=font(PLAIN, 15), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()

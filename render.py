#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page as a 1024x1024 PNG.

Only Pillow is needed. The picture is fully fixed: no clock, no network,
no random numbers, so every run writes identical bytes.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

SIDE = 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (20, 36, 61)
GOLD = (198, 164, 70)
CARD = (255, 255, 255)
MUTED = (90, 90, 90)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        print("WARNING: font not found, using default: " + name,
              file=sys.stderr)
        return ImageFont.load_default()


SERIF_BIG = None
SERIF_HEAD = None
SANS = None
SANS_BOLD = None
SANS_SMALL = None
SANS_FOOT = None


def init_fonts():
    global SERIF_BIG, SERIF_HEAD, SANS, SANS_BOLD, SANS_SMALL, SANS_FOOT
    SERIF_BIG = load("DejaVuSerif-Bold.ttf", 54)
    SERIF_HEAD = load("DejaVuSerif-Bold.ttf", 25)
    SANS = load("DejaVuSans.ttf", 17)
    SANS_BOLD = load("DejaVuSans-Bold.ttf", 16)
    SANS_SMALL = load("DejaVuSans-Bold.ttf", 14)
    SANS_FOOT = load("DejaVuSans-Bold.ttf", 13)


def wrap(draw, text, font, width):
    """Split text into lines that fit width, measured with the real font."""
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split(" ")
        current = ""
        for word in words:
            trial = word if not current else current + " " + word
            if draw.textlength(trial, font=font) <= width or not current:
                current = trial
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_globe(draw, cx, cy, radius, colour):
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 outline=colour, width=3)
    draw.ellipse([cx - radius // 3, cy - radius, cx + radius // 3,
                  cy + radius], outline=colour, width=2)
    draw.line([cx - radius, cy, cx + radius, cy], fill=colour, width=2)
    draw.arc([cx - radius, cy - radius // 2, cx + radius,
              cy + radius // 2], start=200, end=340, fill=colour, width=2)


def draw_spiral(draw, cx, cy, colour):
    for step in range(5):
        r = 10 + step * 5
        box = [cx - r, cy - r, cx + r, cy + r]
        draw.arc(box, start=step * 70, end=step * 70 + 250,
                 fill=colour, width=3)
    for dx in (-26, 0, 26):
        draw.line([cx + dx, cy + 30, cx + dx - 6, cy + 44],
                  fill=colour, width=3)


def draw_cricket(draw, cx, cy, colour):
    for i in (-14, 0, 14):
        draw.rectangle([cx + i - 3, cy - 30, cx + i + 3, cy + 18],
                       fill=colour)
    draw.rectangle([cx - 17, cy - 36, cx + 17, cy - 30], fill=colour)
    draw.line([cx - 34, cy + 36, cx - 10, cy - 8], fill=colour, width=9)
    draw.line([cx - 10, cy - 8, cx - 2, cy - 20], fill=colour, width=5)
    draw.ellipse([cx + 20, cy + 22, cx + 36, cy + 38], fill=(178, 34, 34))


def draw_chart(draw, cx, cy, colour):
    heights = (16, 28, 42)
    for i, h in enumerate(heights):
        x0 = cx - 34 + i * 24
        draw.rectangle([x0, cy + 20 - h, x0 + 16, cy + 20], fill=colour)
    draw.line([cx - 36, cy + 6, cx + 34, cy - 38], fill=colour, width=5)
    draw.polygon([(cx + 22, cy - 44), (cx + 44, cy - 34),
                  (cx + 20, cy - 24)], fill=colour)


def draw_dome(draw, cx, cy, colour):
    draw.arc([cx - 30, cy - 28, cx + 30, cy + 28], start=180, end=360,
             fill=colour, width=4)
    draw.rectangle([cx - 34, cy + 6, cx + 34, cy + 12], fill=colour)
    for i in (-24, -8, 8, 24):
        draw.rectangle([cx + i - 3, cy + 12, cx + i + 3, cy + 34],
                       fill=colour)
    draw.rectangle([cx - 38, cy + 34, cx + 38, cy + 40], fill=colour)
    draw.line([cx, cy - 28, cx, cy - 42], fill=colour, width=3)
    draw.polygon([(cx, cy - 42), (cx + 16, cy - 37), (cx, cy - 32)],
                 fill=colour)


def draw_flag(draw, cx, cy, colour):
    for row in range(3):
        for col in range(4):
            if (row + col) % 2 == 0:
                x0 = cx - 34 + col * 15
                y0 = cy - 26 + row * 15
                draw.rectangle([x0, y0, x0 + 15, y0 + 15], fill=INK)
    draw.line([cx - 36, cy - 30, cx - 36, cy + 40], fill=colour, width=4)


def draw_bag(draw, cx, cy, colour):
    draw.polygon([(cx - 26, cy - 10), (cx + 26, cy - 10),
                  (cx + 32, cy + 36), (cx - 32, cy + 36)], fill=colour)
    draw.arc([cx - 16, cy - 30, cx + 16, cy + 2], start=180, end=360,
             fill=colour, width=4)
    pound = load("DejaVuSans-Bold.ttf", 26)
    text = "\u00a3"
    w = draw.textlength(text, font=pound)
    draw.text((cx - w / 2, cy - 2), text, font=pound, fill=(255, 255, 255))


PICTOGRAMS = {
    "spiral": draw_spiral,
    "cricket": draw_cricket,
    "chart": draw_chart,
    "dome": draw_dome,
    "flag": draw_flag,
    "bag": draw_bag,
}

STORIES = [
    {
        "tag": "WEATHER \u00b7 INDIA",
        "colour": (13, 110, 120),
        "picto": "spiral",
        "headline": "Cyclone Akvan hits India's east coast",
        "body": "Severe Cyclone Akvan is due to cross the coast near "
                "Gopalpur, Odisha, around noon, winds 90\u2013100 km/h "
                "gusting to 110. Red warnings stand across the coast, "
                "and 100,000+ people in Odisha have moved to shelters.",
        "foot": "LANDFALL ~NOON \u00b7 REUTERS / CNBC-TV18",
    },
    {
        "tag": "SPORT \u00b7 WELLINGTON",
        "colour": (46, 125, 50),
        "picto": "cricket",
        "headline": "Phillips century puts NZ on top on Day 2",
        "body": "Glenn Phillips, resuming on 94, reaches his second "
                "Test century with 118 before Akash Deep ends his "
                "216-run stand with Nicholls. At lunch: Nicholls 146 "
                "not out, New Zealand 317 for 6.",
        "foot": "DAY 2, 1ST TEST \u00b7 REUTERS / AP",
    },
    {
        "tag": "ECONOMY \u00b7 TOKYO",
        "colour": (178, 34, 34),
        "picto": "chart",
        "headline": "Japan prices rise 2.2%, rate rise looms",
        "body": "Core consumer prices rose 2.2% from a year earlier in "
                "October, data showed on Friday \u2014 above the Bank of "
                "Japan's 2% target for a second month. A rate rise to "
                "1.5% (from 1.25%) is now expected in December.",
        "foot": "OCTOBER CPI \u00b7 REUTERS / WSJ",
    },
    {
        "tag": "CULTURE \u00b7 NEW DELHI",
        "colour": (176, 124, 20),
        "picto": "dome",
        "headline": "Delhi opens first SCO dialogue forum",
        "body": "Prime Minister Narendra Modi is to inaugurate the "
                "first Civilisational Dialogue Forum of the Shanghai "
                "Cooperation Organisation (SCO) at Purana Qila at "
                "about 5:30 p.m. today. The three-day meeting "
                "celebrates the shared heritage of SCO members.",
        "foot": "OPENS 5:30 P.M. IST \u00b7 NDTV / PIB",
    },
    {
        "tag": "SPORT \u00b7 LAS VEGAS",
        "colour": (88, 48, 140),
        "picto": "flag",
        "headline": "Vegas qualifying decides the grid",
        "body": "Formula 1's Las Vegas weekend reaches its sharp end "
                "tonight: final practice at 4:30 p.m., then qualifying "
                "at 8 p.m. Las Vegas time. The 50-lap race runs on "
                "Saturday night under the Strip lights.",
        "foot": "QUALIFYING 8 P.M. PT \u00b7 PLANETF1 / NBC",
    },
    {
        "tag": "ECONOMY \u00b7 LONDON",
        "colour": (30, 80, 160),
        "picto": "bag",
        "headline": "UK shops' October verdict due today",
        "body": "Britain's October retail sales figures are due at "
                "7 a.m. GMT. Forecasters expect sales flat (0.0%) on "
                "the month after volumes fell 0.4% in September, as "
                "shoppers hold back for Black Friday.",
        "foot": "DUE 7 A.M. GMT \u00b7 ONS / EUROPESAYS",
    },
]


def paint_masthead(draw):
    draw.rectangle([0, 0, SIDE, 116], fill=NAVY)
    title = "SIX STORIES, ONE FRIDAY"
    tw = draw.textlength(title, font=SERIF_BIG)
    draw.text(((SIDE - tw) / 2, 14), title, font=SERIF_BIG,
              fill=(255, 255, 255))
    sub = "FRIDAY 20 NOVEMBER 2026 \u2014 THE WORLD'S NEWS IN ONE IMAGE"
    sw = draw.textlength(sub, font=SANS_BOLD)
    draw.text(((SIDE - sw) / 2, 80), sub, font=SANS_BOLD,
              fill=(200, 210, 225))
    draw_globe(draw, 956, 58, 28, GOLD)
    draw.rectangle([0, 116, SIDE, 119], fill=GOLD)


def paint_card(draw, story, x, y, width, height):
    colour = story["colour"]
    draw.rectangle([x, y, x + width, y + height], fill=CARD,
                   outline=INK, width=2)
    draw.rectangle([x, y, x + 10, y + height], fill=colour)
    tag = story["tag"]
    pad = 8
    tag_w = draw.textlength(tag, font=SANS_BOLD)
    draw.rectangle([x + 22, y + 16, x + 22 + tag_w + pad * 2, y + 42],
                   fill=colour)
    draw.text((x + 22 + pad, y + 20), tag, font=SANS_BOLD,
              fill=(255, 255, 255))
    PICTOGRAMS[story["picto"]](draw, x + width - 62, y + 58, colour)
    head_lines = wrap(draw, story["headline"], SERIF_HEAD, width - 140)
    if len(head_lines) > 2:
        print("WARNING: headline truncated in card '" +
              story["headline"] + "': " + str(len(head_lines)) +
              " lines > 2", file=sys.stderr)
    hy = y + 54
    for line in head_lines[:2]:
        draw.text((x + 22, hy), line, font=SERIF_HEAD, fill=INK)
        hy += 31
    body_lines = wrap(draw, story["body"], SANS, width - 44)
    if len(body_lines) > 5:
        print("WARNING: body truncated in card '" +
              story["headline"] + "': " + str(len(body_lines)) +
              " lines > 5", file=sys.stderr)
    by = hy + 8
    for line in body_lines[:5]:
        draw.text((x + 22, by), line, font=SANS, fill=INK)
        by += 22
    draw.line([x + 22, y + height - 32, x + width - 22, y + height - 32],
              fill=(200, 200, 200), width=1)
    draw.text((x + 22, y + height - 24), story["foot"],
              font=SANS_SMALL, fill=MUTED)


def paint():
    init_fonts()
    image = Image.new("RGB", (SIDE, SIDE), PAPER)
    draw = ImageDraw.Draw(image)
    paint_masthead(draw)
    margin = 24
    gap = 16
    card_w = (SIDE - margin * 2 - gap) // 2
    card_h = 272
    for index, story in enumerate(STORIES):
        col = index % 2
        row = index // 2
        x = margin + col * (card_w + gap)
        y = 140 + row * (card_h + gap)
        paint_card(draw, story, x, y, card_w, card_h)
    note = ("SIX STORIES FROM FRIDAY 20 NOVEMBER 2026 \u00b7 SOURCES: "
            "REUTERS, AP, WSJ, NDTV, CNBC-TV18, PLANETF1, NBC, ONS, PIB, "
            "EUROPESAYS")
    nw = draw.textlength(note, font=SANS_FOOT)
    draw.text(((SIDE - nw) / 2, 994), note, font=SANS_FOOT, fill=MUTED)
    return image


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    paint().save(target, format="PNG")
    print("wrote " + target)


if __name__ == "__main__":
    main()

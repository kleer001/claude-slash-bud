#!/usr/bin/env python3
"""Compose docs/images/banner.jpg from branch-source.jpg and the wordmark.

Ink colour is sampled from the branch itself rather than set to black, so the type
belongs to the picture instead of sitting on top of it. The tagline auto-fits the
gutter left of the branch, so changing the wording cannot collide with the artwork.

Requires the Inter font family at the path in F. Run from anywhere:
    python3 docs/images/make_banner.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = HERE / "branch-source.jpg"
OUT = HERE

F = "/usr/share/fonts/opentype/inter"
INK = (60, 68, 68)          # darkened from the branch's #657878
MUTED = (108, 112, 108)


NAME = "/bud"
TAG1 = ["For every folder", "that outgrows its mother repo"]
TAG2 = "Split. Publish. Prune."


def font(style, size):
    return ImageFont.truetype(f"{F}/Inter-{style}.otf", size)


def fit(d, lines, style, start_px, avail):
    """Largest size at which every line clears the picture's free gutter."""
    px = start_px
    while px > 12:
        f = font(style, px)
        if max(d.textlength(s, font=f) for s in lines) <= avail:
            return px
        px -= 1
    return px


def draw_block(d, x, y, name_px, t1_px, t2_px, rule=True, max_right=None):
    if max_right:
        avail = max_right - x
        name_px = fit(d, [NAME], "Bold", name_px, avail)
        t1_px = fit(d, TAG1, "SemiBold", t1_px, avail)
        t2_px = fit(d, [TAG2], "Light", t2_px, avail)
    d.text((x, y), NAME, font=font("Bold", name_px), fill=INK)
    y += int(name_px * 1.26)
    for line in TAG1:
        d.text((x, y), line, font=font("SemiBold", t1_px), fill=INK)
        y += int(t1_px * 1.34)
    y += int(t1_px * 0.42)
    d.text((x, y), TAG2, font=font("Light", t2_px), fill=MUTED)
    if rule:
        y += int(t2_px * 1.9)
        d.line([(x, y), (x + int(name_px * 1.9), y)], fill=INK + (0,), width=2)
        d.line([(x, y), (x + int(name_px * 1.9), y)], fill=MUTED, width=2)


img = Image.open(SRC).convert("RGB")
a = img.resize((1400, 660), Image.LANCZOS).crop((0, 30, 1400, 630))   # 1400x600
d = ImageDraw.Draw(a)
# The branch's leftmost pixels across the tagline rows sit at x≈481; leave a gutter.
draw_block(d, 78, 60, 92, 30, 23, max_right=452)
a.save(OUT / "banner.jpg", quality=90, optimize=True, subsampling=0)

print("wrote banner.jpg")

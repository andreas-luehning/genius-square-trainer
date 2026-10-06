#!/usr/bin/env python3
"""Generate the PWA icons in the app's default colour theme.

Requires Pillow: python3 -m pip install pillow
"""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent
ICON_DIR = ROOT / "icons"
SCALE = 4

BG = "#fbf4e4"
BOARD = "#69c3ef"
BOARD_EDGE = "#3f94c6"
HOLE = "#277fae"
PEG = "#dfb473"
PEG_LIGHT = "#f3d49c"
CORAL = "#eb5b44"
GREEN = "#8bbe3d"
ORANGE = "#f5a04e"


def rounded_rectangle(draw, box, radius, fill):
    draw.rounded_rectangle(tuple(v * SCALE for v in box), radius * SCALE, fill=fill)


def ellipse(draw, box, fill):
    draw.ellipse(tuple(v * SCALE for v in box), fill=fill)


def build_icon(size: int, maskable: bool = False) -> Image.Image:
    canvas = Image.new("RGB", (size * SCALE, size * SCALE), BG)
    draw = ImageDraw.Draw(canvas)

    # Maskable artwork stays inside the central 80% safe zone.
    inset = 66 if maskable else 34
    board_box = (inset, inset, size - inset, size - inset)
    edge_box = (inset, inset + 8, size - inset, size - inset + 8)
    radius = 76 if maskable else 88
    rounded_rectangle(draw, edge_box, radius, BOARD_EDGE)
    rounded_rectangle(draw, board_box, radius, BOARD)

    left, top, right, bottom = board_box
    pad = 42 if maskable else 48
    grid_left, grid_top = left + pad, top + pad
    grid_right, grid_bottom = right - pad, bottom - pad
    step_x = (grid_right - grid_left) / 5
    step_y = (grid_bottom - grid_top) / 5
    hole_r = 13 if maskable else 15
    pegs = {(0, 0), (4, 0), (2, 1), (5, 2), (1, 3), (3, 4), (4, 5)}

    for row in range(6):
        for col in range(6):
            cx = grid_left + col * step_x
            cy = grid_top + row * step_y
            r = hole_r
            ellipse(draw, (cx - r, cy - r, cx + r, cy + r), HOLE)
            if (col, row) in pegs:
                ellipse(draw, (cx - r - 2, cy - r - 1, cx + r + 2, cy + r + 3), "#a87532")
                ellipse(draw, (cx - r, cy - r - 3, cx + r, cy + r), PEG)
                ellipse(draw, (cx - r * .45, cy - r * .6, cx + r * .3, cy + r * .15), PEG_LIGHT)

    # Three small theme accents make the launcher icon recognisable at a glance.
    accent_y = size - inset - 20
    for x, colour in ((size / 2 - 25, GREEN), (size / 2, ORANGE), (size / 2 + 25, CORAL)):
        ellipse(draw, (x - 7, accent_y - 7, x + 7, accent_y + 7), colour)

    return canvas.resize((size, size), Image.Resampling.LANCZOS)


def main() -> None:
    ICON_DIR.mkdir(exist_ok=True)
    build_icon(192).save(ICON_DIR / "icon-192.png", optimize=True)
    icon_512 = build_icon(512)
    icon_512.save(ICON_DIR / "icon-512.png", optimize=True)
    build_icon(512, maskable=True).save(ICON_DIR / "icon-maskable-512.png", optimize=True)
    print(f"Generated icons in {ICON_DIR}")


if __name__ == "__main__":
    main()

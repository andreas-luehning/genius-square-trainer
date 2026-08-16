#!/usr/bin/env python3
"""Generate the PWA icons from the 512 px source artwork."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "icon-512.png"
OUTPUT = ROOT / "icons"
BACKGROUND = (105, 195, 239, 255)


def resample_filter():
    return Image.Resampling.LANCZOS


def main():
    if not SOURCE.is_file():
        raise SystemExit(f"Quelldatei fehlt: {SOURCE.name}")

    OUTPUT.mkdir(exist_ok=True)
    source = Image.open(SOURCE).convert("RGBA")

    source.resize((192, 192), resample_filter()).save(OUTPUT / "icon-192.png", optimize=True)
    source.resize((512, 512), resample_filter()).save(OUTPUT / "icon-512.png", optimize=True)

    # Android may crop maskable icons to different shapes. Keep the artwork
    # inside the central safe zone and fill the complete canvas.
    maskable = Image.new("RGBA", (512, 512), BACKGROUND)
    artwork = source.resize((384, 384), resample_filter())
    maskable.alpha_composite(artwork, ((512 - 384) // 2, (512 - 384) // 2))
    maskable.save(OUTPUT / "icon-maskable-512.png", optimize=True)

    for path in sorted(OUTPUT.glob("*.png")):
        print(f"erzeugt: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

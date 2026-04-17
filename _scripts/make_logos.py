"""Produce logo variants from logo.png.

- logo-cropped.png: trimmed whitespace, original colors (for light backgrounds)
- logo-nav.png: trimmed whitespace, navy text -> white, gold star preserved (for navy backgrounds)

Run from Website/ dir:
    python3 _scripts/make_logos.py
"""
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
src = Image.open(ROOT / "logo.png").convert("RGBA")
arr = np.array(src)

# --- 1) find bounding box of content pixels (opaque AND not near-white) ---
opaque = arr[:, :, 3] > 50
near_white = (arr[:, :, 0] > 240) & (arr[:, :, 1] > 240) & (arr[:, :, 2] > 240)
content_mask = opaque & ~near_white
rows = np.any(content_mask, axis=1)
cols = np.any(content_mask, axis=0)
ymin, ymax = np.where(rows)[0][[0, -1]]
xmin, xmax = np.where(cols)[0][[0, -1]]
pad = 12
ymin = max(0, ymin - pad)
xmin = max(0, xmin - pad)
ymax = min(arr.shape[0], ymax + pad + 1)
xmax = min(arr.shape[1], xmax + pad + 1)

# --- 2) cropped original ---
cropped = src.crop((xmin, ymin, xmax, ymax))
cropped.save(ROOT / "logo-cropped.png")
print(f"wrote logo-cropped.png  {cropped.size}")

# --- 3) nav variant: navy -> white, whitespace -> transparent, keep gold ---
c = np.array(cropped)
R, G, B, A = c[:, :, 0], c[:, :, 1], c[:, :, 2], c[:, :, 3]

# Gold star detection: R high, G moderate, B low, roughly gold-family (#C9933A-ish)
gold_mask = (R > 150) & (G > 100) & (G < 200) & (B < 120) & (R > B)

# Near-white pixels: make transparent
near_white = (R > 230) & (G > 230) & (B > 230)

# Navy pixels: everything dark-blueish that isn't gold
dark = (R < 150) & (G < 150) & (B < 200) & ~gold_mask

nav = c.copy()
# Navy -> white
nav[dark] = [255, 255, 255, 255]
# Near-white -> transparent
nav[near_white, 3] = 0
# Gold stays (do nothing)

# Anti-aliased edges between navy text and white background:
# for pixels that aren't cleanly one bucket, tint toward white proportional to darkness.
# Skip: leave as-is — minor imperfection acceptable at 48px.

nav_img = Image.fromarray(nav, mode="RGBA")
nav_img.save(ROOT / "logo-nav.png")
print(f"wrote logo-nav.png     {nav_img.size}")

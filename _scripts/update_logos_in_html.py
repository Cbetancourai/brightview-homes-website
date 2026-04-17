"""Swap nav/footer <img src="logo.png"> -> <img src="logo-nav.png">,
remove the brightness(0) invert(1) filter (logo-nav.png is already white),
and bump logo size for better visibility.

Favicon and Open Graph references (which use href/content, not <img src>) are
left untouched and continue to use logo.png (navy-on-transparent) — correct for
those contexts.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

REPLACEMENTS = [
    # 1) Swap nav/footer image source
    ('<img src="logo.png"', '<img src="logo-nav.png"'),

    # 2) Drop the white-invert filter (variations we've seen across files)
    ('filter: brightness(0) invert(1);', ''),
    ('filter:brightness(0) invert(1);', ''),

    # 3) Bump nav logo from 32px -> 44px (and larger 48px for sites where it's center-stage)
    ('.nav-logo img { height: 32px;', '.nav-logo img { height: 44px;'),
    ('.nav-logo img { height: 32px ;', '.nav-logo img { height: 44px ;'),

    # 4) Bump footer logo height
    ('.footer-brand-logo img { height: 30px;', '.footer-brand-logo img { height: 40px;'),

    # 5) Mobile nav logo (index, etc.)
    ('.mobile-nav-logo img { height: 28px;', '.mobile-nav-logo img { height: 36px;'),
]

targets = [p for p in ROOT.glob("*.html")]
targets += [ROOT / "bv-landing.css"]

updated = []
for path in targets:
    text = path.read_text()
    new_text = text
    for old, new in REPLACEMENTS:
        new_text = new_text.replace(old, new)
    if new_text != text:
        path.write_text(new_text)
        updated.append(path.name)

print(f"Updated {len(updated)} files:")
for n in updated:
    print(f"  {n}")

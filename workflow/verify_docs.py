#!/usr/bin/env python3
"""
Verify docs/index.html readiness for GitHub Pages deployment.
"""
import re
from pathlib import Path

docs_html = Path("docs/index.html")
if not docs_html.exists():
    print("[ERROR] docs/index.html does not exist!")
    exit(1)

content = docs_html.read_text(encoding="utf-8")

# 1. Check for local file paths
file_refs = re.findall(r"file://[^\s\"'>]+", content)
if file_refs:
    print(f"[ERROR] Found local file:// references: {file_refs}")
    exit(1)
print("✓ Zero local file:// references found.")

# 2. Check for slides
slides = re.findall(r'<section\b[^>]*data-slide-id=["\'](\d+)["\'][^>]*>', content)
if len(slides) != 8:
    print(f"[ERROR] Expected 8 slides, found {len(slides)}")
    exit(1)
print(f"✓ Exactly 8 designated slides verified: {slides}")

# 3. Check for speaker notes
notes = re.findall(r'<aside\s+class=["\']notes["\']>', content)
if len(notes) != 8:
    print(f"[ERROR] Expected 8 notes, found {len(notes)}")
    exit(1)
print(f"✓ Exactly 8 Speaker Notes (<aside class='notes'>) verified.")

# 4. Check for source footers
footers = re.findall(r'<div\s+class=["\']source-footer["\']>', content)
if len(footers) != 8:
    print(f"[ERROR] Expected 8 source footers, found {len(footers)}")
    exit(1)
print(f"✓ Exactly 8 Source Footers verified.")

# 5. Check CDN links
if "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js" in content and \
   "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css" in content and \
   "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/notes/notes.min.js" in content:
    print("✓ All Reveal.js CDN HTTPS dependencies verified.")
else:
    print("[ERROR] Missing Reveal.js CDN links!")
    exit(1)

# 6. Check .nojekyll
nojekyll = Path("docs/.nojekyll")
if nojekyll.exists():
    print("✓ docs/.nojekyll present (ensures GitHub Pages does not run Jekyll processor on assets).")
else:
    print("[WARNING] docs/.nojekyll missing.")

print("\nSUCCESS: docs/index.html is 100% verified and ready for GitHub Pages deployment!")

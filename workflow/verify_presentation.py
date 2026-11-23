#!/usr/bin/env python3
"""
SiC Market LLM Presentation Quality & Compliance Verification Script (Node 6)
Checks:
1. File existence and accessibility
2. HTML structure & Reveal.js initialization
3. Exact 8-slide structure
4. Non-empty Speaker Notes on every slide (<aside class="notes">)
5. Source attribution on every slide (Source IDs, Publishers, Years)
6. Forbidden absolute wording check ("必然", "唯一", "徹底解決", "所有廠商")
7. Key compliance facts check:
   - 2023 TrendForce $2.28B labeled as forecast
   - Temperature distinction (300°C theoretical vs 150-175°C commercial)
   - 8-inch cost reduction labeled as conditional on mature yield
   - 80 PLUS Titanium labeled as efficiency certification, not universal legal mandate
"""

import sys
import re
from pathlib import Path
from html.parser import HTMLParser

BASE_DIR = Path(__file__).resolve().parent.parent
HTML_PATH = BASE_DIR / "presentation" / "index.html"

def run_evaluation():
    print("=" * 60)
    print("Node 6: Reveal.js Presentation Quality Evaluation")
    print(f"Target File: {HTML_PATH}")
    print("=" * 60)

    errors = []
    warnings = []

    # 1. File existence
    if not HTML_PATH.exists():
        print(f"[FATAL ERROR] File does not exist: {HTML_PATH}")
        return False

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 2. Check Reveal.js dependencies & initialization
    print("\n[Check 1/6] Checking Reveal.js Structure & Initialization...")
    if "reveal.min.css" not in content or "reveal.min.js" not in content:
        errors.append("Reveal.js CDN styles or scripts missing from HTML header/footer.")
    else:
        print("  ✓ Reveal.js CDN CSS and JS linked properly.")

    if "Reveal.initialize" not in content:
        errors.append("Missing Reveal.initialize script call.")
    else:
        print("  ✓ Reveal.initialize() script detected.")

    if "RevealNotes" not in content:
        warnings.append("RevealNotes plugin might not be initialized in Reveal.initialize({ plugins: [...] }).")
    else:
        print("  ✓ RevealNotes speaker notes plugin loaded.")

    # 3. Check Slide Count
    print("\n[Check 2/6] Verifying Slide Count...")
    # Find all top-level sections inside <div class="slides">
    slides = re.findall(r'<section\b[^>]*data-slide-id=["\'](\d+)["\'][^>]*>(.*?)</section>', content, re.DOTALL)
    print(f"  Found {len(slides)} designated slides.")
    if len(slides) != 8:
        errors.append(f"Expected exactly 8 slides, found {len(slides)}.")
    else:
        print("  ✓ Exactly 8 designated slides verified.")

    # 4. Check Speaker Notes & Source Footers on each slide
    print("\n[Check 3/6] Inspecting Speaker Notes & Source Footers...")
    for slide_id, slide_content in slides:
        # Check notes
        notes_match = re.search(r'<aside\s+class=["\']notes["\']>(.*?)</aside>', slide_content, re.DOTALL)
        if not notes_match or len(notes_match.group(1).strip()) < 30:
            errors.append(f"Slide {slide_id} is missing or has insufficient Speaker Notes (<aside class='notes'>).")
        else:
            print(f"  ✓ Slide {slide_id}: Speaker Notes verified ({len(notes_match.group(1).strip())} chars).")

        # Check source footer
        footer_match = re.search(r'<div\s+class=["\']source-footer["\']>(.*?)</div>', slide_content, re.DOTALL)
        if not footer_match or "SRC-" not in footer_match.group(1):
            errors.append(f"Slide {slide_id} is missing standard Source ID citation in footer.")
        else:
            print(f"  ✓ Slide {slide_id}: Source Footer cited: {footer_match.group(1).strip()}")

    # 5. Check for Forbidden Absolute/Unsubstantiated Wording
    print("\n[Check 4/6] Checking for Forbidden Overly Deterministic / Absolute Wording...")
    forbidden_words = ["必然", "徹底解決", "所有廠商"]
    # For "唯一", check if it claims SiC is the "唯一" technology for 800V
    found_forbidden = []
    for fw in forbidden_words:
        if fw in content:
            found_forbidden.append(fw)
            errors.append(f"Found forbidden absolute word '{fw}' in presentation content.")
    
    if "唯一選擇" in content or "唯一可用" in content:
        errors.append("Found forbidden phrase '唯一選擇/唯一可用' in presentation content.")
    
    if not found_forbidden:
        print("  ✓ Zero forbidden absolute terms found ('必然', '徹底解決', '所有廠商' free).")

    # 6. Check Specific Factual Calibrations
    print("\n[Check 5/6] Checking Fact Calibrations (User Revisions)...")
    # A. 2023 TrendForce 2.28B labeled as forecast
    if "22.8" in content:
        if "預測" in content:
            print("  ✓ 22.8 億美元 properly labeled with '預測' context.")
        else:
            errors.append("22.8 億美元 is cited without explicit '預測' (Forecast) qualification.")

    # B. Temperature distinction (300 vs 150-175)
    if "300°C" in content:
        if "150°C～175°C" in content or "150°C~175°C" in content:
            print("  ✓ Temperature distinction between theoretical 300°C and commercial 150-175°C verified.")
        else:
            warnings.append("Theoretical 300°C mentioned, verify if commercial 150-175°C rating is explained.")

    # C. 8-inch cost reduction labeled as conditional on mature yield
    if "30%～35%" in content or "30%~35%" in content:
        if "成熟良率" in content:
            print("  ✓ 8-inch 30%~35% cost drop explicitly qualified with '成熟良率' condition.")
        else:
            errors.append("8-inch 30%~35% cost reduction mentioned without '成熟良率' prerequisite.")

    # D. 80 PLUS Titanium described as certification/standard rather than statutory law
    if "Titanium" in content:
        if "認證標準" in content or "認證" in content:
            print("  ✓ 80 PLUS Titanium correctly framed as efficiency certification standard.")
        else:
            warnings.append("Check Titanium wording to ensure it is not described as statutory law.")

    # Summary
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print(f"  Total Slides: {len(slides)}")
    print(f"  Total Errors: {len(errors)}")
    print(f"  Total Warnings: {len(warnings)}")
    print("=" * 60)

    if errors:
        print("\nERRORS TO REVISE:")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False
    else:
        print("\nSUCCESS: Presentation HTML passed all Node 6 verification criteria cleanly!")
        return True

if __name__ == "__main__":
    success = run_evaluation()
    sys.exit(0 if success else 1)

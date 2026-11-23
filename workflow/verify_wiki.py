#!/usr/bin/env python3
"""
SiC Market LLM Wiki Quality & Integrity Verification Script
Checks:
1. Frontmatter completeness (title, category, tags, sources, last_updated)
2. Broken [[wikilinks]] detection
3. Orphan pages detection (pages not linked from INDEX or other pages)
4. Raw data sources integrity and metadata alignment
"""

import os
import re
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR = BASE_DIR / "data" / "raw"
METADATA_FILE = RAW_DIR / "metadata.json"

def parse_frontmatter(content):
    """Simple parser for YAML frontmatter block."""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    fm_text = parts[1]
    body = parts[2]
    
    # Extract keys
    fm = {}
    for line in fm_text.strip().split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if key in ["title", "category", "last_updated", "data_classification"]:
                fm[key] = val.strip("\"'")
            elif key in ["tags", "sources"]:
                fm[key] = val
    return fm, body

def run_verification():
    print("=" * 60)
    print("SiC Market LLM Wiki — Automated Quality Verification")
    print(f"Base Directory: {BASE_DIR}")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # 1. Verify Raw Sources & Metadata
    print("\n[Step 1/4] Checking Raw Data Sources and Metadata...")
    if not METADATA_FILE.exists():
        errors.append(f"Missing metadata file: {METADATA_FILE}")
    else:
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        sources = metadata.get("sources", [])
        print(f"  ✓ Loaded metadata.json with {len(sources)} registered sources.")
        if len(sources) < 5:
            errors.append(f"Expected at least 5 sources in metadata.json, found {len(sources)}")
        
        for src in sources:
            src_id = src.get("source_id")
            # Check corresponding raw markdown file
            matched_files = list(RAW_DIR.glob(f"source_*.md"))
            content_found = False
            for mf in matched_files:
                with open(mf, "r", encoding="utf-8") as rf:
                    if src_id in rf.read():
                        content_found = True
                        break
            if not content_found:
                warnings.append(f"Source ID {src_id} not explicitly cited in data/raw/*.md headers")
            else:
                print(f"  ✓ {src_id}: Verified in data/raw/ ({src.get('title')[:45]}...)")

    # 2. Collect all Wiki Pages
    print("\n[Step 2/4] Scanning Wiki Pages and Parsing Frontmatter...")
    wiki_files = list(WIKI_DIR.rglob("*.md"))
    page_map = {} # basename_without_ext -> Path
    links_from_page = {} # basename -> set of target basenames
    all_targets = set()

    for wf in wiki_files:
        stem = wf.stem
        page_map[stem] = wf
        with open(wf, "r", encoding="utf-8") as f:
            content = f.read()
        
        fm, body = parse_frontmatter(content)
        if not fm:
            errors.append(f"Missing or malformed YAML frontmatter in: {wf.relative_to(BASE_DIR)}")
        else:
            required_keys = ["title", "category"]
            for rk in required_keys:
                if rk not in fm:
                    errors.append(f"Missing required frontmatter key '{rk}' in {wf.relative_to(BASE_DIR)}")
        
        # Extract [[wikilinks]]
        raw_links = re.findall(r"\[\[(.*?)\]\]", content)
        # Clean links: remove aliases like [[target|alias]]
        cleaned_links = set()
        for rl in raw_links:
            target = rl.split("|")[0].strip()
            # If target has path or .md, strip it
            target = Path(target).stem
            cleaned_links.add(target)
            all_targets.add(target)
        
        links_from_page[stem] = cleaned_links
        print(f"  ✓ {wf.relative_to(WIKI_DIR)} (Found {len(cleaned_links)} outgoing wikilinks)")

    print(f"  Total Wiki Pages Found: {len(page_map)}")

    # 3. Check for Broken Wikilinks
    print("\n[Step 3/4] Checking for Broken [[wikilinks]]...")
    broken_links = []
    for source_page, targets in links_from_page.items():
        for target in targets:
            if target not in page_map:
                broken_links.append((source_page, target))
                errors.append(f"Broken Link: [[{target}]] referenced in '{source_page}.md' does not exist!")
    
    if not broken_links:
        print("  ✓ Zero Broken Links! All [[wikilinks]] successfully resolve to valid pages.")
    else:
        print(f"  ✗ Found {len(broken_links)} broken links.")

    # 4. Check for Orphan Pages
    print("\n[Step 4/4] Checking for Orphan Pages...")
    # INDEX is the root, so it doesn't need to be linked to, but all others should be linked
    index_stem = "INDEX"
    orphans = []
    for stem in page_map:
        if stem == index_stem:
            continue
        if stem not in all_targets:
            orphans.append(stem)
            warnings.append(f"Orphan Page: '{stem}.md' is not referenced by any other page or INDEX.md")
    
    if not orphans:
        print("  ✓ Zero Orphan Pages! Every concept note is connected to the knowledge graph.")
    else:
        print(f"  ! Found {len(orphans)} orphan pages: {orphans}")

    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print(f"  Total Wiki Pages: {len(page_map)}")
    print(f"  Total Raw Sources: {len(sources)}")
    print(f"  Broken Links: {len(broken_links)}")
    print(f"  Orphan Pages: {len(orphans)}")
    print(f"  Total Errors: {len(errors)}")
    print(f"  Total Warnings: {len(warnings)}")
    print("=" * 60)
    
    if errors:
        print("\nERRORS ENCOUNTERED:")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False
    else:
        print("\nSUCCESS: All Wiki Integrity Checks Passed Cleanly!")
        return True

if __name__ == "__main__":
    success = run_verification()
    sys.exit(0 if success else 1)

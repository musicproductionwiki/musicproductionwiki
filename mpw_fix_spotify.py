#!/usr/bin/env python3
"""
mpw_fix_spotify.py — MusicProductionWiki.com
Patches eq.html and compression.html to replace Spotify iframes with green link buttons.
Only these 2 files ever had iframes — all other v3.0 entries were clean.

Usage:
    python mpw_fix_spotify.py --dry-run     # show changes, do not commit
    python mpw_fix_spotify.py               # patch + commit to GitHub

GitHub API:
    Token read from GITHUB_TOKEN env var, or hardcoded fallback below.
    All commits use Trees API (single commit, no sequential blobs).
"""

import os
import re
import sys
import json
import base64
import hashlib
import argparse
import requests
from datetime import datetime

# ── Config ─────────────────────────────────────────────────────────────────────
REPO_OWNER  = "musicproductionwiki"
REPO_NAME   = "musicproductionwiki"
BRANCH      = "main"
TOKEN       = os.environ.get("GITHUB_TOKEN", "YOUR_GITHUB_TOKEN_HERE")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

TARGET_FILES = ["bible/eq.html", "bible/compression.html"]

# ── Spotify green link button HTML template ─────────────────────────────────────
# Matches the v4.0 standard. Extracts track URI and builds the button.
SPOTIFY_LINK_TEMPLATE = """<a href="https://open.spotify.com/track/{track_id}"
   target="_blank"
   rel="noopener noreferrer"
   class="spotify-link-item">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424a.623.623 0 01-.857.207c-2.348-1.435-5.304-1.76-8.785-.964a.623.623 0 11-.277-1.215c3.809-.87 7.077-.496 9.712 1.115a.624.624 0 01.207.857zm1.223-2.722a.78.78 0 01-1.072.257c-2.687-1.652-6.785-2.131-9.965-1.166a.78.78 0 01-.973-.519.781.781 0 01.519-.972c3.632-1.102 8.147-.568 11.234 1.328a.78.78 0 01.257 1.072zm.105-2.835C14.692 8.95 9.375 8.775 6.297 9.71a.937.937 0 11-.543-1.794c3.532-1.072 9.404-.865 13.115 1.338a.937.937 0 01-.954 1.614z"/>
  </svg>
  <span>{label}</span>
</a>"""

# ── Regex patterns for iframe detection ────────────────────────────────────────
# Matches: <iframe ... src="https://open.spotify.com/embed/track/TRACKID" ...></iframe>
# Also catches multi-line iframes.
IFRAME_PATTERN = re.compile(
    r'<iframe[^>]*src=["\']https://open\.spotify\.com/embed/track/([A-Za-z0-9]+)[^"\']*["\'][^>]*>\s*</iframe>',
    re.IGNORECASE | re.DOTALL
)

# Wrapper patterns — strip containing divs if they only wrap the iframe
SPOTIFY_WRAPPER_PATTERN = re.compile(
    r'<div[^>]*class=["\'][^"\']*spotify[^"\']*["\'][^>]*>\s*(<iframe[^>]*src=["\']https://open\.spotify\.com/embed/track/([A-Za-z0-9]+)[^"\']*["\'][^>]*>\s*</iframe>)\s*</div>',
    re.IGNORECASE | re.DOTALL
)

# ── Label extraction ────────────────────────────────────────────────────────────
def extract_label_near_iframe(html: str, iframe_match) -> str:
    """Try to find a nearby track title to use as button label."""
    start = max(0, iframe_match.start() - 400)
    context = html[start:iframe_match.start()]
    
    # Look for aria-label on the iframe itself
    aria = re.search(r'aria-label=["\']([^"\']{5,80})["\']', iframe_match.group(0))
    if aria:
        return aria.group(1)
    
    # Look for a heading or strong tag just before
    heading = re.findall(r'<(?:h[2-6]|strong|b)[^>]*>([^<]{5,80})</(?:h[2-6]|strong|b)>', context)
    if heading:
        return heading[-1].strip()
    
    # Look for a paragraph with "Listen" text
    listen = re.search(r'Listen(?:\s+to)?\s+["\u201c]?([^"<\u201d]{5,60})["\u201d]?', context)
    if listen:
        return listen.group(1).strip()
    
    return "Listen on Spotify"

# ── Core patch function ─────────────────────────────────────────────────────────
def patch_html(html: str, filename: str) -> tuple[str, int]:
    """
    Replace all Spotify iframes with green link buttons.
    Returns (patched_html, iframe_count_replaced).
    """
    replaced = 0
    
    # First pass: wrapper divs containing iframes
    def replace_wrapper(m):
        nonlocal replaced
        track_id = m.group(2)
        # Find label from context
        start = max(0, m.start() - 400)
        context = html[start:m.start()]
        heading = re.findall(r'<(?:h[2-6]|strong|b)[^>]*>([^<]{5,80})</(?:h[2-6]|strong|b)>', context)
        label = heading[-1].strip() if heading else "Listen on Spotify"
        replaced += 1
        return SPOTIFY_LINK_TEMPLATE.format(track_id=track_id, label=label)
    
    patched = SPOTIFY_WRAPPER_PATTERN.sub(replace_wrapper, html)
    
    # Second pass: bare iframes not caught by wrapper pattern
    def replace_iframe(m):
        nonlocal replaced
        track_id = m.group(1)
        label = extract_label_near_iframe(patched, m)
        replaced += 1
        return SPOTIFY_LINK_TEMPLATE.format(track_id=track_id, label=label)
    
    patched = IFRAME_PATTERN.sub(replace_iframe, patched)
    
    if replaced:
        print(f"  [{filename}] Replaced {replaced} iframe(s) with green link button(s)")
    else:
        print(f"  [{filename}] No iframes found — file already clean")
    
    return patched, replaced

# ── GitHub API helpers ──────────────────────────────────────────────────────────
def get_latest_commit_sha() -> str:
    url = f"{BASE_URL}/git/ref/heads/{BRANCH}"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()["object"]["sha"]

def get_tree_sha(commit_sha: str) -> str:
    url = f"{BASE_URL}/git/commits/{commit_sha}"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()["tree"]["sha"]

def get_file_content(path: str) -> tuple[str, str]:
    """Returns (decoded_html, blob_sha)."""
    url = f"{BASE_URL}/contents/{path}?ref={BRANCH}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 404:
        raise FileNotFoundError(f"File not found in repo: {path}")
    r.raise_for_status()
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return content, data["sha"]

def create_blob(content: str) -> str:
    url = f"{BASE_URL}/git/blobs"
    payload = {
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "encoding": "base64"
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    r.raise_for_status()
    return r.json()["sha"]

def create_tree(base_tree_sha: str, file_blobs: list[dict]) -> str:
    """file_blobs: list of {"path": str, "blob_sha": str}"""
    url = f"{BASE_URL}/git/trees"
    tree = [
        {"path": fb["path"], "mode": "100644", "type": "blob", "sha": fb["blob_sha"]}
        for fb in file_blobs
    ]
    payload = {"base_tree": base_tree_sha, "tree": tree}
    r = requests.post(url, headers=HEADERS, json=payload)
    r.raise_for_status()
    return r.json()["sha"]

def create_commit(tree_sha: str, parent_sha: str, message: str) -> str:
    url = f"{BASE_URL}/git/commits"
    payload = {
        "message": message,
        "tree": tree_sha,
        "parents": [parent_sha]
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    r.raise_for_status()
    return r.json()["sha"]

def update_ref(commit_sha: str):
    url = f"{BASE_URL}/git/refs/heads/{BRANCH}"
    payload = {"sha": commit_sha, "force": False}
    r = requests.patch(url, headers=HEADERS, json=payload)
    r.raise_for_status()

# ── Main ────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Patch Spotify iframes in eq.html and compression.html")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without committing")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print("mpw_fix_spotify.py — Spotify iframe patcher")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE COMMIT'}")
    print(f"Target files: {', '.join(TARGET_FILES)}")
    print(f"{'='*60}\n")

    patched_files = []
    total_replaced = 0

    for path in TARGET_FILES:
        print(f"Fetching {path} ...")
        try:
            html, blob_sha = get_file_content(path)
        except FileNotFoundError as e:
            print(f"  WARNING: {e} — skipping")
            continue

        patched, count = patch_html(html, path)
        total_replaced += count

        if count > 0:
            if args.dry_run:
                # Show a diff summary
                orig_iframes = len(IFRAME_PATTERN.findall(html))
                print(f"  [DRY RUN] Would replace {count} iframe(s) in {path}")
                # Write patched version locally for inspection
                local_name = path.replace("/", "_") + ".patched"
                with open(local_name, "w", encoding="utf-8") as f:
                    f.write(patched)
                print(f"  [DRY RUN] Patched version saved locally as: {local_name}")
            else:
                patched_files.append({"path": path, "content": patched})

    if total_replaced == 0:
        print("\n✅ Both files already clean — no iframes found. Nothing to commit.")
        return

    if args.dry_run:
        print(f"\n[DRY RUN] Would commit {len([f for f in TARGET_FILES])} file(s), {total_replaced} total replacement(s).")
        print("Run without --dry-run to commit.")
        return

    if not patched_files:
        print("\nNo files needed patching. Done.")
        return

    print(f"\nCommitting {len(patched_files)} patched file(s) via Trees API...")

    # Trees API commit
    latest_commit = get_latest_commit_sha()
    base_tree    = get_tree_sha(latest_commit)

    file_blobs = []
    for pf in patched_files:
        print(f"  Creating blob for {pf['path']} ...")
        bsha = create_blob(pf["content"])
        file_blobs.append({"path": pf["path"], "blob_sha": bsha})

    new_tree   = create_tree(base_tree, file_blobs)
    date_str   = datetime.utcnow().strftime("%Y-%m-%d")
    msg        = f"fix: replace Spotify iframes with green link buttons in eq.html + compression.html [{date_str}]"
    new_commit = create_commit(new_tree, latest_commit, msg)
    update_ref(new_commit)

    print(f"\n✅ Committed successfully.")
    print(f"   Commit SHA : {new_commit}")
    print(f"   Message    : {msg}")
    print(f"   Files      : {', '.join(pf['path'] for pf in patched_files)}")
    print(f"   Replacements: {total_replaced} iframe(s) → green link buttons")
    print(f"\n🔗 Verify live:")
    for pf in patched_files:
        slug = pf["path"].replace("bible/", "").replace(".html", "")
        print(f"   https://musicproductionwiki.com/bible/{slug}")

if __name__ == "__main__":
    main()

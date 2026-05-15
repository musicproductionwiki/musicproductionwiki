"""
mpw_session_start.py — MusicProductionWiki.com Session Start Gate
Run at the beginning of every session before taking any action.

Fetches MPW-HANDOFF-CORE.md from GitHub, counts articles + Bible entries via Trees API,
prints 3 most recent commits, lists available module files.
"""

import requests
import base64
import json
import sys

TOKEN = 'YOUR_GITHUB_TOKEN_HERE'
REPO = 'musicproductionwiki/musicproductionwiki'
HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

HANDOFF_MODULES = [
    'MPW-HANDOFF-CORE.md',
    'MPW-HANDOFF-SCRIPTS.md',
    'MPW-HANDOFF-CONTENT.md',
    'MPW-HANDOFF-BIBLE.md',
    'MPW-HANDOFF-ARTICLES.md',
    'MPW-HANDOFF-TECH.md',
]


def fetch_core():
    """Fetch and print MPW-HANDOFF-CORE.md from repo."""
    print("=" * 70)
    print("FETCHING MPW-HANDOFF-CORE.md FROM GITHUB...")
    print("=" * 70)
    r = requests.get(
        f'https://api.github.com/repos/{REPO}/contents/MPW-HANDOFF-CORE.md',
        headers=HEADERS, timeout=30
    )
    if r.status_code != 200:
        print(f"[ERROR] Could not fetch CORE.md: {r.status_code}")
        sys.exit(1)
    content = base64.b64decode(r.json()['content']).decode('utf-8')
    print(content)
    return content


def count_articles_and_bible():
    """Count articles and Bible entries via Trees API (fast, no pagination)."""
    print("=" * 70)
    print("COUNTING ARTICLES + BIBLE ENTRIES VIA TREES API...")
    print("=" * 70)

    r = requests.get(
        f'https://api.github.com/repos/{REPO}/git/trees/main?recursive=1',
        headers=HEADERS, timeout=60
    )
    if r.status_code != 200:
        print(f"[ERROR] Trees API failed: {r.status_code}")
        return

    tree = r.json().get('tree', [])

    articles = [
        f for f in tree
        if f['path'].startswith('articles/') and f['path'].endswith('.html')
    ]
    bible_entries = [
        f for f in tree
        if f['path'].startswith('bible/') and f['path'].endswith('.html')
        and f['path'] != 'bible/index.html'
    ]
    category_pages = [
        f for f in tree
        if f['path'].startswith('categories/') and f['path'].endswith('.html')
    ]

    print(f"  Articles:      {len(articles)}")
    print(f"  Bible entries: {len(bible_entries)}")
    print(f"  Category pages:{len(category_pages)}")

    # Check for MPW-CATALOG.md
    has_catalog = any(f['path'] == 'MPW-CATALOG.md' for f in tree)
    print(f"  MPW-CATALOG.md: {'PRESENT' if has_catalog else 'MISSING'}")

    # Check bible-index.json entry count
    catalog_file = next((f for f in tree if f['path'] == 'bible-index.json'), None)
    if catalog_file:
        try:
            r2 = requests.get(
                f'https://api.github.com/repos/{REPO}/contents/bible-index.json',
                headers=HEADERS, timeout=30
            )
            index_content = base64.b64decode(r2.json()['content']).decode('utf-8')
            index_data = json.loads(index_content)
            print(f"  bible-index.json: {len(index_data)} entries")
        except Exception:
            print("  bible-index.json: could not parse")

    return len(articles), len(bible_entries)


def print_recent_commits():
    """Print 3 most recent commits."""
    print("=" * 70)
    print("3 MOST RECENT COMMITS:")
    print("=" * 70)
    r = requests.get(
        f'https://api.github.com/repos/{REPO}/commits?per_page=3',
        headers=HEADERS, timeout=30
    )
    if r.status_code != 200:
        print(f"[ERROR] Could not fetch commits: {r.status_code}")
        return
    commits = r.json()
    for i, c in enumerate(commits, 1):
        sha = c['sha'][:8]
        msg = c['commit']['message'].split('\n')[0][:80]
        date = c['commit']['committer']['date'][:10]
        print(f"  {i}. [{sha}] {date} — {msg}")


def check_module_files():
    """Check which handoff module files are present in repo."""
    print("=" * 70)
    print("HANDOFF MODULE FILES IN REPO:")
    print("=" * 70)
    for module in HANDOFF_MODULES:
        r = requests.get(
            f'https://api.github.com/repos/{REPO}/contents/{module}',
            headers=HEADERS, timeout=30
        )
        status = "✅ PRESENT" if r.status_code == 200 else "❌ MISSING"
        print(f"  {status} — {module}")

    # Check mpw_session_start.py itself
    r = requests.get(
        f'https://api.github.com/repos/{REPO}/contents/mpw_session_start.py',
        headers=HEADERS, timeout=30
    )
    status = "✅ PRESENT" if r.status_code == 200 else "❌ MISSING"
    print(f"  {status} — mpw_session_start.py")


def session_start_checklist():
    """Print the session start checklist."""
    print("=" * 70)
    print("SESSION START CHECKLIST — STATE THESE BACK BEFORE TAKING ANY ACTION:")
    print("=" * 70)
    print("  1. Current article count (from Trees API above)")
    print("  2. Current Bible entry count (check MPW-CATALOG.md in repo)")
    print("  3. P0 priority (from Section 2 of CORE.md above)")
    print("  4. Every NEVER rule added in last 2 sessions (from Rule 3 above)")
    print()
    print("  If you cannot recite all four, re-read CORE.md. Do not proceed.")
    print("=" * 70)


if __name__ == '__main__':
    try:
        fetch_core()
        count_articles_and_bible()
        print_recent_commits()
        check_module_files()
        session_start_checklist()
        print()
        print("mpw_session_start.py complete. Proceed with session start checklist.")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        sys.exit(1)

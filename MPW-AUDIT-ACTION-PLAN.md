# MPW Site Audit & Session Action Plan
*Audit Date: May 26, 2026 — Session 70*
*Last Updated: May 27, 2026 — Session 73 (post-session audit)*

---

## WHAT WAS FIXED THIS SESSION (Session 70)

| Fix | Method | SHA | Result |
|-----|--------|-----|--------|
| robots.txt created | Single PUT (new file — acceptable) | `bef10798` | ✅ |
| sitemap: www. stripped from 41 tool URLs | Single PUT (one file) | `2d65f573` | ✅ |
| sitemap: 24 missing Bible entries added | Same PUT as above | `2d65f573` | ✅ |
| Model string → claude-sonnet-4-6 on 4 API tools | 4 individual PUTs (1 file each — acceptable) | 4 SHAs | ✅ |
| Favicon on 36 non-API tools | ❌ 36 individual PUTs — WRONG. Should have been 1 Trees API commit | 36 SHAs | ✅ done but costly |
| root main.js deleted | Trees API ✅ | `09357a33` | ✅ |
| search-index: +222 Bible +36 Tools (789 total) | Single PUT (one file) | `d2eb4a95` | ✅ |
| 17 root orphan article drafts deleted | Trees API ✅ | `064bc4fd` | ✅ |
| browser-daw.html — already gone from repo | No action needed | — | ✅ |
| sitemap — root orphan URLs not present | No action needed | — | ✅ |

**Session 70 mistake logged:** 36 individual commits for favicon batch = 36 Netlify deploys.
Rule: any batch of 2+ files MUST use Trees API. One commit = one deploy.

---

## WHAT WAS FIXED THIS SESSION (Session 71)

| Fix | Method | SHA | Result |
|-----|--------|-----|--------|
| main.js SEARCH_INDEX: +222 Bible +41 Tool entries | Single PUT | `a565a93f` | ✅ |
| main.js search URL fix (window.location.origin) | Single PUT | `c45959b3` | ⚠️ superseded |
| Article search renderItem hardcoded /articles/ prefix | Trees API — 526 files | `17142bd9` | ✅ |
| index.html renderItem fix | Single PUT | `ba94b314` | ✅ |
| tools/index.html renderItem fix | Single PUT | `a47608b0` | ✅ |
| categories + about.html renderItem fix | Trees API — 90 files | `f162f141` | ✅ |
| Tool nav batch — partial progress | Multiple test commits | various | ⚠️ continued S72 |

---

## WHAT WAS FIXED THIS SESSION (Session 72)

| Fix | Method | SHA | Result |
|-----|--------|-----|--------|
| fix_tool_navs.py: add `has_mob_wire` to GOOD state detection | Script update | — | ✅ |
| fix_tool_navs.py: add mobile eyeglass CSS override after nav CSS block | Script update | — | ✅ |
| 35 tools: full nav injection (NO_NAV → GOOD) | Trees API | `fb32b50e` | ✅ |
| ai-music-ddex-checker: full nav replace (old stub nav removed) | Trees API | `3831e5a1` | ✅ |
| ai-music-rights-navigator: wireMobSearch + mobSearchBtn added | Trees API | `3831e5a1` | ✅ |
| suno-prompt-optimizer: searchOverlay + mpw-search-js + wire added | Trees API | `3831e5a1` | ✅ |
| tools/index.html: style.css removed, nav JS + overlay added | Trees API | `3831e5a1` | ✅ |
| All 41 tools + index: mobile eyeglass CSS — initial attempt (wrong) | Trees API | `a3ee22ff` | ❌ broke hamburger |
| Hamburger restored — reverted broken media query on 42 files | Trees API | `db467a8b` | ✅ |
| tools/index.html: dark background restored, duplicate navMob removed | Single PUT | `f5cb1694` | ✅ |
| Mobile eyeglass: inject override after nav CSS block (correct position) | Trees API | `5a615e07` | ✅ |
| tools/index.html: hamburger restored — reverted broken MQ, removed stale blocks | Single PUT | `adf7ff2e` | ✅ |

---

## WHAT WAS FIXED THIS SESSION (Session 73)

| Fix | Method | SHA | Result |
|-----|--------|-----|--------|
| og-image.png created and uploaded to repo root | Single PUT (new file) | `967f1cf2` | ✅ |
| Batch A: og:image added to 36 tools, www. stripped from 5 canonicals + og:url, overflow-x added to 5 Gen2/3 tools | Trees API — 41 files | `ab2faf98` | ✅ |
| Batch B: Share row standardized — Copy/X/Reddit flex nowrap — all 3 generations | Trees API — 41 files | `5e54f584` | ✅ |
| Batch C: Beehiiv audit — NO-OP (0 broken iframes found, already clean) | — | — | ✅ |
| Batch D: Embed mode (?embed=true) added to 36 tools missing it | Trees API — 36 files | `67bc8334` | ✅ |
| Batch E: Suno drawer → 2-col grid; thc-right clip fix; footer www. stripped on 3 Gen2 tools | Trees API — 4 files | `e021c66c` | ✅ |
| backToTop arrow hidden on all 41 tools (main.js injects it — hidden via CSS per tool) | Trees API — 41 files | `3d278d0d` | ✅ |
| Gen 1 footer replaced with clean standard footer on 38 tools | Trees API — 41 files | `3d278d0d` | ✅ |
| "Interactive Tool" badge removed from card headers — all 39 tools with a card | Trees API — 39 files | `4d8530e9` | ✅ |
| Tool card names corrected — 21 mismatches fixed to match H1 titles | Trees API — 21 files | `0d30f23b` | ✅ |

**Session 73 key lessons:**
- Batch C was a ghost — the audit from S70 said 37 broken iframes but live inspection found 0. Always re-audit live before executing a batch.
- overflow-x:clip (Gen 1) is functionally better than overflow-x:hidden — don't change what works.
- og:image tags pointing to non-existent files are equivalent to no tag — always verify the image exists before adding the meta tag.
- Tool card names were wrong on 21/36 Gen 1 tools — all were template copy-paste artifacts never corrected. Always audit name accuracy when touching card headers.
- Full scope before any batch. No assumptions. No guessing. Read live files first.

---

## TOOL NAV — CURRENT STATE (End of Session 73)

| Tool | Nav | Mobile Eyeglass | Hamburger | Mobile Search Wire |
|------|-----|-----------------|-----------|-------------------|
| All 39 standard tools | ✅ | ✅ | ✅ | ✅ |
| tools/index.html | ✅ | ✅ | ✅ | ✅ |
| ai-music-ddex-checker | ✅ | ✅ | ✅ | ✅ |
| ai-music-rights-navigator | ✅ | ✅ | ✅ | ✅ |
| suno-prompt-optimizer | ✅ | ✅ | ✅ | ✅ |
| suno-credits-calculator | ✅ | ✅ | ✅ | ✅ |

---

## AUDIT NUMBERS — CURRENT STATE (End of Session 73)

| Metric | Value |
|--------|-------|
| Articles in repo | 526 |
| Bible entries in repo | 234 |
| Tools in repo | 41 (excl. index.html) |
| Tools with correct MPW nav | 41 ✅ |
| Tools with mobile eyeglass | 41 ✅ |
| Tools with working hamburger | 41 ✅ |
| Tools with wireMobSearch | 41 ✅ |
| Tools with overflow-x (clip or hidden) | 41 ✅ |
| Tools with og:image | 41 ✅ |
| Tools with correct canonical (non-www) | 41 ✅ |
| Tools with embed mode | 41 ✅ |
| Tools with correct beehiiv | 41 ✅ (nav link only — no broken iframes found) |
| Tools with standardized share row | 41 ✅ |
| Tools with correct footer | 41 ✅ |
| Tools with backToTop arrow hidden | 41 ✅ |
| Tools with correct card name matching H1 | 41 ✅ |
| Category pages with non-www canonical | 89/89 ✅ (confirmed clean — already done pre-S73) |
| Favicon sitewide fix | 851/851 ✅ (confirmed clean — all pages have /favicon.svg) |

---

## REMAINING AUDIT ISSUES — PRIORITIZED

### ✅ COMPLETE — Category page canonical URLs
All 89 category pages confirmed non-www canonical. Already done prior to S73.

### ✅ COMPLETE — Favicon sitewide
All ~851 files confirmed /favicon.svg. Articles, Bible, categories — all clean.

### 🔴 PRIORITY 1 — Affiliate applications (REVENUE BLOCKER)
Plugin Boutique, Amazon Associates, Loopmasters, Sweetwater, PluginFox.
Owner action only — cannot be done by Claude.

### 🔴 PRIORITY 2 — mpw_writer.py 4 pending updates
Blocks next article batch. Updates needed: new MPW mobile drawer HTML (2-col grid), Tools→ nav link, correct Bible link selector, pushState/popstate.
Must be done before any new article production.

### 🔴 PRIORITY 3 — mpw_bible_writer.py updates
Blocks next Bible batch. Updates needed: 650wpm read time, new nav, v5.3 build.
Must be done before next T1 Bible batch.

### 🟠 PRIORITY 4 — Next article batch
526 articles live, none added since S69. Blocked on mpw_writer.py updates (Priority 2).

### 🟠 PRIORITY 5 — Next Bible batch
234 entries live. Blocked on mpw_bible_writer.py updates (Priority 3).

### 🟡 PRIORITY 6 — about.html not reachable from tool nav
About link present in index.html nav but missing from all 41 tool pages. Low impact — investigate and fix when convenient.

### 🟡 PRIORITY 7 — Sitemap resubmission to GSC
Submit updated sitemap via Google Search Console after any structural changes.

---

## TREES API COMMIT PATTERN — MANDATORY REFERENCE

Rule: 2+ files = Trees API. Always. For >200 files use incremental chunks of 100.

```python
import requests, base64, time

TOKEN = "[GITHUB_TOKEN — from setenv.ps1, NEVER hardcode]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

main_sha = requests.get(f"{BASE}/git/refs/heads/main", headers=HEADERS).json()['object']['sha']

new_tree = []
for path, content in files.items():
    blob_sha = requests.post(f"{BASE}/git/blobs", headers=HEADERS, json={
        "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
        "encoding": "base64"
    }).json()['sha']
    new_tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob_sha})
    time.sleep(0.1)

CHUNK = 100
chunks = [new_tree[i:i+CHUNK] for i in range(0, len(new_tree), CHUNK)]
current_base = main_sha
for chunk in chunks:
    current_base = requests.post(f"{BASE}/git/trees", headers=HEADERS, json={
        "base_tree": current_base, "tree": chunk
    }).json()['sha']

commit_sha = requests.post(f"{BASE}/git/commits", headers=HEADERS, json={
    "message": "descriptive message",
    "tree": current_base,
    "parents": [main_sha]
}).json()['sha']

requests.patch(f"{BASE}/git/refs/heads/main", headers=HEADERS, json={"sha": commit_sha})
print(f"✅ {len(files)} files — 1 commit — 1 deploy: {commit_sha[:8]}")
```

---

*Document created: Session 70, May 26, 2026*
*Last updated: Session 73, May 27, 2026*

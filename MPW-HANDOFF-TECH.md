# MPW — Technical Reference
*Fetch via: `python mpw_session_start.py --fetch tech`*

---

# 3. Gold Standard Article — FULLY LOCKED

**URL:** https://musicproductionwiki.com/articles/suno-vs-udio.html
**File:** articles/suno-vs-udio.html
**Last confirmed commit:** 06a564c
**DO NOT TOUCH UNDER ANY CIRCUMSTANCES.**

## Structural Fingerprints (required on all articles)

| # | Fingerprint | Label |
| --- | --- | --- |
| 1 | class="mpw-site-nav" | nav wrapper — r7 standard |
| 2 | mpw-nav-v4-final-r7 | nav CSS fingerprint — current standard |
| 3 | class="nav-logo-mark" | 32x32 teal square logo mark |
| 4 | class="nav-logo-name" | logo text |
| 5 | class="nav-toggle" | dropdown trigger — pure CSS :focus-within |
| 6 | class="nav-bible-link" | amber Producer's Bible link |
| 7 | class="nav-search-btn" | search icon button |
| 8 | id="searchOverlay" | search overlay |
| 9 | id="main-content" | main-content |
| 10 | class="article-layout" | article-layout grid wrapper |
| 11 | class="article-body" | article body |
| 12 | class="quick-answer" | quick-answer box |
| 13 | class="faq-accordion" | FAQ section |
| 14 | class="site-footer" | site-footer |
| 15 | ../css/style.css | asset path css |
| 16 | ../js/main.js | asset path js |

**NOTE:** suno-vs-udio.html was written before r7. Its nav fingerprint is mpw-nav-v4-final-r6, not r7. Content structure fingerprints (items 9-16) are what matter for content quality checks. Items 1-8 are correct on all articles after the r7 run.

---

# 3B. Bible Gold Standard Entry — LOCKED

**File:** `bible/eq.html`
**Canonical URL:** `https://musicproductionwiki.com/bible/eq`
**Status:** LIVE — layout AND mobile BOTH fixed Session 26 ✅
**NEVER TOUCH — it is the template.**

**Old template (DO NOT USE):** `bible/compression.html` — LIVE — commit e387c341 — LOCKED — NOT the template.

---

# 41. Nav Architecture — SESSION 20 FINAL STATE

**Fingerprint:** `mpw-nav-homepage-v1` — Commit: dbc09281

**CSS key rules:**
```css
/* Homepage and category pages: */
nav.mpw-site-nav .nav-inner { max-width:1200px; padding:0 24px }

/* Article pages override (Session 21 LOCKED): */
nav.mpw-site-nav .nav-inner { max-width:1360px !important; padding:0 24px !important; }

.nav-item.open > .nav-dropdown { opacity:1; visibility:visible; pointer-events:auto }
.nav-dropdown.wide { min-width:500px; display:grid; grid-template-columns:1fr 1fr }
```

**HTML:** `class="logo-mark"` (32x32 teal square), absolute paths throughout.
**JS:** Scoped to `nav.mpw-site-nav .nav-item` — no conflict with main.js.
**nav-inner article pages:** max-width:1360px confirmed correct — getBoundingClientRect() — logo-mark left = H1 left = 301px. LOCKED.

---

# 41B. Always Check for and Remove Old Inline Nav Scripts

When running any nav patch, check for and remove old inline nav scripts in the same patch operation.

---

# 44. Site Structure

```
repo root/
├── index.html                     — Homepage — LOCKED Session 17
├── about.html                     — Needs bible bar (P0.2)
├── sitemap.xml                    — 598 URLs — resubmitted GSC May 13, 2026
├── search-index.json              — 526 entries — CLEAN — commit 925f3931
├── bible-index.json               — 1 entry (EQ) — grows with each batch
├── netlify.toml                   — Needs /dictionary/* → /bible/:splat 301
├── MPW-HANDOFF-CORE.md            — NEW Session 28
├── MPW-HANDOFF-SCRIPTS.md         — NEW Session 28
├── MPW-HANDOFF-CONTENT.md         — NEW Session 28
├── MPW-HANDOFF-BIBLE.md           — NEW Session 28
├── MPW-HANDOFF-ARTICLES.md        — NEW Session 28
├── MPW-HANDOFF-TECH.md            — NEW Session 28
├── articles/                      — 526 .html files
├── bible/
│   ├── index.html                 — LIVE — commit 29ee26a9 ✅
│   ├── compression.html           — LIVE — LOCKED — commit e387c341
│   └── eq.html                    — LIVE — LOCKED — gold standard ✅
├── categories/                    — 90 category pages
├── css/
│   └── style.css
└── js/
    └── main.js
```

---

# 37. Category Pages

**Total:** 90 category pages
- 89 original: ALL patched to mpw-nav-homepage-v1 via mpw_fix_sitewide_r7.py ✅
- breakdowns.html: LIVE — commit ef987b6b — needs r7 nav on next mpw_fix_sitewide_r7.py run
- /bible/index.html: LIVE — own nav system — no main.js

**Pages that still need building:**
- `recreations.html` — must exist before Batch 11
- `vocal-autopsies.html` — must exist before Batch 12
- `brands.html` — in nav but page doesn't exist

---

# 35. Comprehensive Audit — mpw_full_audit.py

**Location:** `Desktop\mpw-scripts\mpw_full_audit.py`
**Last run:** May 14, 2026
**Results:** 12 total issues: 7 date-2025 (4 fixed — 3 remain to verify), 5 missing og:image (retry mpw_fix_meta.py)
**All other checks clean:** 0 missing canonicals, 0 duplicate titles, 0 old nav, 0 duplicate bible bars, 0 orphans.

Run weekly: `python mpw_full_audit.py`

**13 checks:**
1. Canonical tags present and `/articles/filename.html` format (no trailing slash)
2. Meta description present
3. OG tags (og:title, og:description, og:image)
4. Date strings — no 2025
5. Bible bar — present exactly once (bible-bar-v4)
6. Nav fingerprint — mpw-nav-v4-final-r7
7. Structural elements (quick-answer, faq-accordion, article-layout, etc.)
8. Word count — above floor for category
9. Orphaned articles (not in search-index.json)
10. Duplicate titles across site
11. Canonical format check — no trailing slash
12. robots meta — `max-snippet:-1` present
13. Search index entry — slug present in search-index.json

---

# 36. Search Index

| Index | Status |
| --- | --- |
| search-index.json | LIVE — 526 entries — ALL TITLES CLEAN — commit 925f3931 |
| Session 27 audit | CLEAN — 0 dead slugs in search index ✅ |
| bible-index.json | LIVE — 1 entry (EQ) — grows with each Bible batch |

---

# 39. Sidebar Structure — ALL ARTICLES

Correct sidebar structure:
```
aside
  └── TOC widget
  └── Newsletter widget
      └── Related Articles widget (nested inside newsletter widget)
```

Sidebar audit: COMPLETED Session 18 — 526 articles: ALL OK — 0 CRITICAL — 0 HIGH.

---

# 40. mpw_writer.py v3.0 nav-inner

```css
nav.mpw-site-nav .nav-inner { max-width:1360px !important; padding:0 24px !important; }
```
Confirmed pixel-perfect. LOCKED. Do not change.

---

# Repo & Hosting Reference

| Key | Value |
| --- | --- |
| GitHub repo | github.com/musicproductionwiki/musicproductionwiki |
| GitHub token | ghp_YOUR_TOKEN_HERE |
| Netlify site ID | classy-haupia-be8e43 |
| Netlify plan | Pro ($20/mo) — 3,000 credits/month — NEVER use individual file commits |
| Auto-deploy | GitHub push → Netlify build → live in 30-60 seconds |
| Pretty URLs | NEVER enable — breaks site |
| GA4 | G-79VB543KCT |
| Email | mpwikiofficial@gmail.com |
| Google Workspace | Case 70817574 — unresolved — domain conflict dispute pending |

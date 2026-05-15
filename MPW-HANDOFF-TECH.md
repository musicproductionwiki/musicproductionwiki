# MPW-HANDOFF-TECH.md
*Updated: May 15, 2026 (SESSION 29)*

---

# Infrastructure

| Item | Value |
| --- | --- |
| Hosting | Netlify — project ID: classy-haupia-be8e43 |
| Repo | github.com/musicproductionwiki/musicproductionwiki |
| GitHub token | YOUR_GITHUB_TOKEN_HERE (expires Aug 2, 2026) |
| Stack | Pure HTML/CSS/vanilla JS — no frameworks, no CMS |
| Deploy | Auto-deploy from GitHub main branch |
| Newsletter | Beehiiv — "The Producer's Briefing" |
| Local files | C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles |
| Scripts dir | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ |
| Search Console | Google Search Console |
| Contact | mpwikiofficial@gmail.com |
| Analytics | GA4 — G-79VB543KCT |
| Pretty URLs | NEVER enable — breaks site |

---

# File Structure

```
repo root/
├── index.html
├── about.html
├── genres.html
├── brands.html (MISSING — in nav but no page)
├── css/style.css
├── js/main.js
├── js/mpw-analytics.js
├── search-index.json
├── sitemap.xml
├── bible-index.json (200 entries)
├── MPW-CATALOG.md (auto-generated)
├── MPW-HANDOFF-CORE.md
├── MPW-HANDOFF-SCRIPTS.md
├── MPW-HANDOFF-CONTENT.md
├── MPW-HANDOFF-BIBLE.md
├── MPW-HANDOFF-ARTICLES.md
├── MPW-HANDOFF-TECH.md
├── mpw_session_start.py
├── articles/
│   ├── [slug].html  (526 articles)
│   └── ...
├── bible/
│   ├── index.html (LOCKED — commit 29ee26a9)
│   ├── eq.html (GOLD STANDARD)
│   ├── compression.html
│   └── [term].html  (201 entries total)
└── categories/
    └── [category].html  (90 pages)
```

Asset paths in articles: `../css/style.css`, `../js/main.js`
Asset paths in bible: self-contained (NO main.js on bible pages)
Asset paths in categories: `../css/style.css`, `../js/main.js`

---

# 3. Article Gold Standard — FULLY LOCKED

URL: https://musicproductionwiki.com/articles/suno-vs-udio.html
File: articles/suno-vs-udio.html
Last confirmed commit: 06a564c

**DO NOT TOUCH UNDER ANY CIRCUMSTANCES.**

## Structural Fingerprints

| # | Fingerprint | Label |
| --- | --- | --- |
| 1 | class="mpw-site-nav" | nav wrapper — r7 standard |
| 2 | mpw-nav-v4-final-r7 | nav CSS fingerprint |
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

---

# 41. Nav Architecture — SESSION 20 FINAL STATE

Fingerprint: **mpw-nav-homepage-v1**
Commit: **dbc09281**
Nav inner: `nav.mpw-site-nav .nav-inner { max-width:1360px !important; padding:0 24px !important; }`

All 614 article + category pages patched to this nav in 1 commit — dbc09281.
Bible pages: SELF-CONTAINED nav — NO main.js.

Key nav rules:
- ALL nav links must be absolute paths (/, /about.html, /bible/, /categories/x.html)
- Dropdowns: CSS :focus-within ONLY — never JS-only
- Logo: SVG logo-mark — 32x32 teal square, 18x18 waveform SVG, dark bars
- NEVER relative paths (../) in nav links

---

# 44. Mobile Nav Architecture — SESSION 25 FINAL STATE

## index.html mobile nav
Bible bar: sticky top:0, z-index:9001. Nav: top:40px. Mobile drawer: The Producer's Bible → articles → gear → Sound Better.

## Articles + category pages mobile nav
Bible bar: bible-bar-v4. Nav: search icon restored. .mobile-drawer top:100px.

## Bible pages mobile nav
Self-contained. NO bible bar from main nav system. All mobile fixes via @media(max-width:768px) only — never touch desktop CSS. Append-only <style> blocks.

---

# 42. Multiagent Orchestration

Architecture: Orchestrator → 8 parallel workers → assembler → Trees API commit.
Rate limit: claude-sonnet-4-6 — 8 workers CONFIRMED SAFE.
Backoff: 15s, 30s, 60s, 120s, 240s on 429.
NEVER use parallel blob creation for GitHub API — always sequential with 403 backoff.

---

# 37. Category Pages

All 89 original category pages patched to mpw-nav-homepage-v1. breakdowns.html added Session 22. Total: 90 category pages.
Location: categories/[name].html
Do NOT commit breakdowns article subcategory pages before articles exist.

---

# 36. Search Index

search-index.json: LIVE — commit 925f3931 — 526 entries — ALL TITLES CLEAN.
bible-index.json: LIVE — 200 entries — grows with each Bible batch.

---

# 35. Comprehensive Article Quality Audit

mpw_full_audit.py — BUILT Session 27.
Last run: May 14, 2026. Results: 12 total issues (7 date-2025, 5 missing-og-image).
Run weekly: `python mpw_full_audit.py`

---

# 34H. Strategy Notes

## Bible entry economics (v3.0)
200 entries × ~20,000 tokens = 4M tokens. Per entry: ~$0.09-0.12.

## Bible entry economics (v4.0)
200 entries × ~36,000 tokens = 7.2M tokens. Per entry: ~$0.18.

## Suno audio as competitive moat
Dry/wet clips per Bible term turn the reference from reading to listening. No competitor can replicate this without significant infrastructure.

## TruClarify integration
Every music business article should funnel to TruClarify. Currently underutilized — every article in the Music Business pillar should mention TruClarify for rights verification.

---

# Affiliate Link Placeholder

All affiliate links use `href="#affiliate"` as placeholder until approvals come through.
Do NOT hardcode any affiliate URLs before approvals.

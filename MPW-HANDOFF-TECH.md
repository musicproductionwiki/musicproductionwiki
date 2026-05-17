# MPW-HANDOFF-TECH.md
*Updated: May 16, 2026 (SESSION 32 FINAL)*

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
├── bible-index.json (201 entries)
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
│   ├── eq.html (v3.0 gold standard — LOCKED)
│   ├── compression.html (v5.1 gold standard — commit Session 33)
│   └── [term].html  (202 entries total — v3.0/v4.0 template)
│   └── categories/
│       ├── dynamics/index.html
│       ├── frequency/index.html
│       ├── time-based/index.html
│       ├── signal-processing/index.html
│       ├── mixing/index.html
│       ├── mastering/index.html
│       ├── synthesis/index.html
│       └── music-theory/index.html
│       └── tools/index.html (PLANNED — build after /tools/ hub)
├── tools/ (PLANNED — /tools/ hub page + /tools/[slug]/ individual tools)
└── categories/
    └── [category].html  (90 pages)
```

Asset paths in articles: `../css/style.css`, `../js/main.js`
Asset paths in bible: self-contained (NO main.js on bible pages)
Asset paths in bible/categories: self-contained (NO main.js)
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

---

# 4. Bible Gold Standard — v5.1

URL: https://musicproductionwiki.com/bible/compression
File: bible/compression.html
Built: Session 32, May 16, 2026
Status: Built locally — COMMIT SESSION 33

**DO NOT MODIFY THE COMMITTED FILE. Update the writer to match it.**

## v5.1 Structural Fingerprints

| # | Fingerprint | Value |
| --- | --- | --- |
| 1 | mpw-slim-bar | top:0, z:700, height:40px, bg:#181818 |
| 2 | bible-bar | top:40px, z:600, height:50px, bg:#0d0800 |
| 3 | bb-cats | 8 category pills, active highlighted amber |
| 4 | entry-nav | top:90px, z:400, 19 pill links, no label |
| 5 | signal-chain SVG | viewBox 0 0 1440 160, 8 boxes, full labels |
| 6 | signal-chain-mobile | .scm-box vertical stack, shown @768px |
| 7 | openGateFor | unified smart gate function, 3 asset types |
| 8 | setTocActive | sidebar TOC IntersectionObserver tracking |
| 9 | calcGR | live gain reduction calculator JS |
| 10 | comparison-callouts | CSS class for 2-col vs comparison grid |
| 11 | history-card | CSS class for left-border history sub-sections |
| 12 | start-here-box | CSS class for learning path callout |
| 13 | Also in The Bible | consolidates Further Reading + Related Terms |
| 14 | 5 JSON-LD blocks | Article+sameAs, FAQPage, BreadcrumbList, Speakable, HowTo |
| 15 | overflow-x:clip | on html and body — NOT overflow:hidden |

## Nav Architecture — v5.1 (LOCKED)

```
Desktop sticky chain:
  .mpw-slim-bar    position:sticky  top:0     z-index:700  height:40px
  .bible-bar       position:sticky  top:40px  z-index:600  height:50px
  .entry-nav       position:sticky  top:90px  z-index:400
  Dropdowns        z-index:99999
  #reading-progress display:none (desktop hidden)

Mobile (≤768px):
  #reading-progress display:block
  .bb-cats          display:none
  .bible-mobile-bar display:flex, position:sticky, top:90px, z:300, height:36px
  .entry-nav        top:126px
  .signal-chain-diagram svg display:none
  .signal-chain-mobile display:flex (vertical stack)
  .entry-sidebar display:none
  Grid: single column

1024px: hide nav links, show hamburger
768px: mobile layout (above)
600px: DAW tab wrap, comparison callouts 1-col
480px: plugin recs 1-col, calc inputs 1-col, QR/genre table smaller font
400px: prereq chain smaller, calc result grid 1-col
380px: slim bar font/padding reduction
```

MPW slim bar content: SVG logo-mark (24×24 teal) + site name / Articles, Gear, About links (muted) / "A MusicProductionWiki Publication" (italic, right) / search icon / Sound Better CTA button / hamburger (≤1024px)

Bible bar content: ◆ + "The Producer's Bible" (amber, left) / divider / 8 category pills (active amber highlighted) / "All entries →" (right)

## Mobile Checklist (38 checks — must all pass before any commit)

Run this audit on every generated Bible entry before committing:

Critical checks:
- Viewport meta: width=device-width, initial-scale=1.0
- overflow-x:clip on html and body
- mpw-slim-bar links hidden @1024px
- hamburger shown @1024px
- bb-cats hidden @768px
- bible-mobile-bar shown @768px
- entry-nav top:126px @768px
- entry-sidebar hidden @768px
- signal-chain SVG hidden @768px
- signal-chain-mobile shown @768px
- single col grid @768px
- tables overflow-x:auto
- progress bar shown @768px
- scroll-margin-top 136px @768px
- parameters 1-col @768px
- types 2-col @768px, 1-col @480px
- plugin-recs 1-col @768px
- flags 1-col @768px
- before-after 1-col @768px
- related-terms 1-col @768px
- comparison-callouts 1-col @600px
- DAW tab wrap @600px
- calc inputs 1-col @480px
- history-card mobile padding @480px
- PDF modal full width @480px
- QR table smaller font @480px
- genre table smaller font @480px
- slim bar font reduction @380px
- progress bar z:99999
- entry-nav overflow-x:auto scrollbar-width:none
- all section IDs have entry-section class
- No horizontal scroll at 360px
- File under 200KB

---

# 5. Nav Architecture — Article Pages (LOCKED)

Nav: mpw-nav-homepage-v1 — commit dbc09281
Nav CSS fingerprint: mpw-nav-v4-final-r7
Nav inner: max-width:1360px, padding:0 24px
All nav links: absolute paths (/about.html, /categories/techniques.html, /bible/, etc.)
Sound Better CTA: desktop only, hidden ≤1024px via @media
Hamburger: shown ≤1024px
Bible link: amber color, nav-bible-link class

Key: article pages use main.js. Bible pages do NOT use main.js. Never mix.

---

# 6. Bible Nav Architecture — v5.1 (LOCKED)

See section 4 above and HANDOFF-BIBLE Section 47 for full spec.

Mobile drawer: 2-column grid (bmn-drawer-cats / bmn-drawer-cat)
History API: pushState({drawerOpen:true}) on drawer open — back button closes drawer

---

# 7. CSS Injection Rules

For Bible pages:
- ALWAYS append CSS as new `<style>` block before `</style>` — NEVER strip or modify existing style blocks
- Mobile fixes go in @media(max-width:768px) — NEVER touch desktop CSS in mobile fix scripts
- Use !important for override rules in media queries
- If a class needs a mobile override, add the class first (not just an inline style)

For article pages:
- All CSS in /css/style.css — committed via GitHub API PUT (never web editor)
- Never use `<style>` blocks in articles — only inline styles for one-off structural elements

---

# 8. Commit Procedures

## Single file commit (acceptable):
```python
import base64, requests
headers = {'Authorization': f'token {TOKEN}'}
r = requests.get(f'https://api.github.com/repos/{REPO}/contents/{path}', headers=headers)
sha = r.json()['sha']
encoded = base64.b64encode(content.encode()).decode()
requests.put(f'https://api.github.com/repos/{REPO}/contents/{path}', headers=headers,
    json={'message': 'commit message', 'content': encoded, 'sha': sha})
```

## Multi-file commit (MANDATORY — Trees API):
```python
# NEVER commit multiple files individually
# Always use gh_trees_commit() from mpw_commit_articles.py
gh_trees_commit(files_dict, 'commit message')
# files_dict = {'path/file.html': html_content, ...}
```

One commit = one Netlify deploy. Multiple individual commits = multiple deploys = rate limit risk.

---

# 9. Search Index

File: /search-index.json — array of {title, slug, category, description}
File: /bible-index.json — array of {term, slug, category, definition}

bible-index.json is used by:
- Bible index page search (Fuse.js)
- Tooltip system (Moat 1 — Session 33) — JS fetches and builds lookup map
- Search overlay on Bible entry pages

Always include bible-index.json update in same Trees API commit as Bible entry commits.

---

# 10. Tools Architecture (Planned — Session 33+)

## /tools/ Hub Page

Standalone page. Not a category page in the existing sense.
Grid of tool cards: tool name + one-line description + which Bible entry it belongs to + "Try Free" button.
Submit to Product Hunt after 5+ tools are live.
URL: musicproductionwiki.com/tools/

## /bible/categories/tools/

9th Bible category. Filter Bible entries that have tool_type != null in bible-index.json.
Build after /tools/ hub page exists.
Link from Bible bar as 9th category pill.

## /tools/[slug]/

Individual tool pages when tools graduate from Bible entries.
GR Calculator → /tools/compression-calculator/ (future, when it has save history + sharing)
Delay Calculator → /tools/delay-calculator/ (start here Session 33)

## Tool-in-Entry Pattern (current)

Tools live inside Bible entries. The tool section (id="tools") in every Tier 1 entry:
1. Cards the primary tool with description + "Jump to Tool ↓" button
2. "More tools coming" teaser with newsletter subscribe link
3. The actual tool (calculator etc) is embedded earlier in the content where contextually relevant

Gate pattern: tool is always free. Email gate on the download/save output only.

---

# 11. Monetization Technical Notes

## Beehiiv Integration

Newsletter signup: POST to https://api.beehiiv.com/v2/publications/BEEHIIV_PUB_ID/subscriptions
Body: {email, reactivate_existing: true, send_welcome_email: true}
Auth: Bearer BEEHIIV_API_KEY

BEEHIIV_PUB_ID and BEEHIIV_API_KEY are placeholders in all Bible entry HTML.
Steve replaces these before committing. Not secrets in the traditional sense (publications-only, low risk) but keep as placeholders in generated code.

## Affiliate Links

All affiliate links use `href="#affiliate"` as placeholder until applications approved.
After approval, run find-and-replace on the placeholder with real affiliate URLs.
Never embed tracking pixels or third-party JS until Mediavine milestone.

## PDF Downloads (Email Gated)

downloadQuickRef() and downloadGenreTable() generate Blob files client-side and trigger download.
No server required. Files are generated from hardcoded content strings in the JS.
Content matches the visible table data — keep in sync if tables are updated.
File names: compression-quick-reference-mpw.txt, compression-by-genre-mpw.txt

---

# 12. Google Search Console

Property: musicproductionwiki.com
Sitemap submitted: ✅ Success
Current state (May 15, 2026): 301 impressions, 0 clicks, position 16.4
Action: optimize title tags + meta descriptions on top comparison articles

After Tier 1 batch commits: regenerate sitemap.xml and resubmit to GSC.

---

# 13. about.html Bible Bar Patch (one-liner — pending if not applied)

```powershell
cd C:\Users\swarn\OneDrive\Desktop\mpw-scripts
. .\setenv.ps1
python -c "
import base64, requests, re
TOKEN = 'YOUR_GITHUB_TOKEN_HERE'
REPO = 'musicproductionwiki/musicproductionwiki'
headers = {'Authorization': f'token {TOKEN}', 'Accept': 'application/vnd.github.v3+json'}
r = requests.get(f'https://api.github.com/repos/{REPO}/contents/about.html', headers=headers)
sha = r.json()['sha']
html = base64.b64decode(r.json()['content']).decode('utf-8')
if 'bible-bar-v4' in html:
    print('Already patched')
else:
    from mpw_add_bible_bar import INJECT, NAV_MARKER, strip_old_bars
    html = strip_old_bars(html)
    html = html.replace(NAV_MARKER, INJECT + NAV_MARKER, 1)
    encoded = base64.b64encode(html.encode('utf-8')).decode()
    res = requests.put(f'https://api.github.com/repos/{REPO}/contents/about.html', headers=headers, json={'message': 'Add bible bar to about.html (bible-bar-v4)', 'content': encoded, 'sha': sha})
    print(res.status_code, res.json().get('commit', {}).get('sha', ''))
"
```

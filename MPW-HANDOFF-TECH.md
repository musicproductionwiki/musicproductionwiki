# MPW-HANDOFF-TECH.md
*Updated: May 18, 2026 (SESSION 37)*

---

# Infrastructure

| Item | Value |
| --- | --- |
| Hosting | Netlify — project ID: classy-haupia-be8e43 |
| Repo | github.com/musicproductionwiki/musicproductionwiki |
| GitHub token | stored in setenv.ps1 (expires Aug 2, 2026) — NEVER hardcode |
| Stack | Pure HTML/CSS/vanilla JS — no frameworks, no CMS |
| Deploy | Auto-deploy from GitHub main branch |
| Newsletter | Beehiiv — "The Producer's Briefing" |
| Local files | C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles |
| Scripts dir | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ |
| Search Console | Google Search Console |
| Contact | team@musicproductionwiki.com (Fastmail) |
| Legacy contact | mpwikiofficial@gmail.com (kept as fallback) |
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
├── netlify.toml (updated Session 36 — ssl-2-plus-review redirect added)
├── css/style.css
├── js/main.js
├── js/mpw-analytics.js
├── search-index.json
├── sitemap.xml (739 URLs — regenerated Session 35)
├── bible-index.json (210 entries)
├── MPW-CATALOG.md (auto-generated)
├── MPW-HANDOFF-CORE.md
├── MPW-HANDOFF-SCRIPTS.md
├── MPW-HANDOFF-CONTENT.md
├── MPW-HANDOFF-BIBLE.md
├── MPW-HANDOFF-ARTICLES.md
├── MPW-HANDOFF-TECH.md
├── mpw_session_start.py
├── handoff_state.json (LOCAL ONLY — never committed — tracks SHA state for handoff runner)
├── articles/
│   ├── [slug].html  (526 articles — unchanged Session 37)
│   └── ...
├── bible/
│   ├── index.html (LOCKED — commit 29ee26a9)
│   ├── eq.html (v3.0 gold standard — LOCKED)
│   ├── compression.html (v5.1 gold standard — writer QA complete Session 37)
│   └── [term].html  (210 entries total — v3.0/v4.0 template)
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
Refined: Sessions 33 + 34 + 35 + 36, May 17–18, 2026
Writer QA: Complete Session 37 — approved by Steve
Status: READY FOR TIER 1 BATCH

**DO NOT MODIFY THE COMMITTED FILE. Update the writer to match it.**

## v5.1 Structural Fingerprints

| # | Fingerprint | Value |
| --- | --- | --- |
| 1 | mpw-slim-bar | top:0, z:700, height:40px, bg:#181818 |
| 2 | bible-bar | top:40px, z:600, height:50px, bg:#0d0800 |
| 3 | bb-cats | 8 category pills, active highlighted amber |
| 4 | entry-nav | top:90px, z:400, 20 pill links, no label |
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
| 16 | mpw-share-bar | unified share bar class — Copy Link → X → Reddit |
| 17 | footer-share-btn | footer override class — flex:0 0 auto !important |
| 18 | bible-entry-wrap inline grid | display:grid!important;grid-template-columns:1fr 280px!important — inline style on element |
| 19 | calc-share-bar | auto-width buttons on calculator and tools share bars |
| 20 | tools after quick-reference | Tools section injected immediately after quick-reference — never at bottom |
| 21 | Verdict in sidebar TOC | ('verdict', 'Verdict') link between Types and Plugins |

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
  .entry-nav        top:84px (40px slim + 44px bible)
  .signal-chain-diagram svg display:none
  .signal-chain-mobile display:flex (vertical stack)
  .entry-sidebar display:none !important
  .bible-entry-wrap display:block !important (grid collapses to single col)

1024px: hide nav links, show hamburger
768px: mobile layout (above)
600px: DAW tab wrap, comparison callouts 1-col
480px: plugin recs 1-col, calc inputs 1-col, QR/genre table smaller font
400px: prereq chain smaller, calc result grid 1-col
380px: slim bar font/padding reduction
```

## style.css — Key Findings (Session 34)

- Total length: 52,585 chars
- **NO rules for .bible-entry-wrap** — confirmed Session 34 via grep
- **NO rules for .entry-sidebar** — confirmed Session 34 via grep
- Has `.article-layout > aside { display:none !important }` — does NOT affect Bible pages (different class hierarchy)
- Has `.article-sidebar` rules — does NOT affect Bible pages (different class)
- Bible page layout is entirely self-contained in the page's two style blocks
- The inline grid on `bible-entry-wrap` was added as a nuclear override after this was confirmed

## Bible Page Layout — DOM Structure (Session 34 — confirmed)

```html
<main id="main-content">
  <div class="bible-entry-wrap" style="display:grid!important;grid-template-columns:1fr 280px!important;gap:40px!important;align-items:start!important;max-width:1100px!important;margin:0 auto!important;padding:40px 24px!important">
    <div class="entry-main">
      <!-- ALL CONTENT SECTIONS -->
      <!-- gain-calculator div MUST be closed before signal-chain section -->
      </div><!-- /gain-calculator -->
      <!-- Signal Chain Position -->
      ...
    </div><!-- /entry-main -->

    <!-- Sidebar -->
    <aside class="entry-sidebar" style="min-width:280px;width:280px;position:sticky;top:148px;align-self:start;overflow-y:auto;height:calc(100vh - 168px);">
      ...
    </aside>
  </div><!-- /bible-entry-wrap -->
</main>
```

**CRITICAL: The aside MUST be a direct child of bible-entry-wrap, NOT nested inside entry-main.**
**NEVER close entry-main before the aside tag.**
**NEVER add display:block!important to the aside inline style — mobile CSS cannot override inline !important.**

## Sidebar Display Rules (Session 34 — CONFIRMED)

Desktop (@media min-width:769px): CSS sets `display:block !important` on `.entry-sidebar`
Mobile (@media max-width:768px): CSS sets `display:none !important` on `.entry-sidebar`
Aside inline style: contains ONLY width/min-width/position/top/align-self/overflow/height — NO display property

## Div Balance Check — MANDATORY before every Bible commit

```python
import re
# segment = html between <div class="entry-main"> and </div><!-- /entry-main -->
segment = body[em_open:em_close]
opens = len(re.findall(r'<div[^>]*>', segment))
closes = len(re.findall(r'</div>', segment))
# balance should be 1 (entry-main itself is the one unclosed div)
# Any other value = broken DOM — find and fix before committing
```

Pattern for finding specific unclosed divs: find_unclosed2.py — iterates with regex, maintains stack, prints context of each unclosed opener.

## Mobile Checklist (38 checks — must all pass before any commit)

Run this audit on every generated Bible entry before committing:

Critical checks:
- Viewport meta: width=device-width, initial-scale=1.0
- overflow-x:clip on html and body
- mpw-slim-bar links hidden @1024px
- hamburger shown @1024px
- bb-cats hidden @768px
- entry-nav top:84px @768px (NOT 126px — updated Session 33)
- entry-sidebar hidden @768px
- signal-chain SVG hidden @768px
- signal-chain-mobile shown @768px
- single col grid @768px
- tables overflow-x:auto
- progress bar shown @768px
- scroll-margin-top 110px @768px
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
- progress bar z:9999
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
- ALWAYS append CSS as new `<style>` block before `</head>` — NEVER strip or modify existing style blocks
- Mobile fixes go in @media(max-width:768px) — NEVER touch desktop CSS in mobile fix scripts
- Use !important for override rules in media queries
- If a class needs a mobile override, add the class first (not just an inline style)
- Bible pages have exactly 2 style blocks — do not add a 3rd

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

## PowerShell Script Creation — CRITICAL (Session 34)

NEVER use Set-Content or here-strings in PowerShell to create Python scripts that contain CSS values.
PowerShell mangles colons, semicolons, and CSS property syntax.

ALWAYS use Claude's create_file tool to output .py files → Steve downloads → saves to mpw-scripts\ → runs.

---

# 9. Search Index

File: /search-index.json — array of {title, slug, category, description}
File: /bible-index.json — array of {term, slug, category, definition}

bible-index.json is used by:
- Bible index page search (Fuse.js)
- Tooltip system (Moat 1 — planned) — JS fetches and builds lookup map
- Search overlay on Bible entry pages

Always include bible-index.json update in same Trees API commit as Bible entry commits.

---

# 10. Tools Architecture (Planned — Session 38+)

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
Delay Calculator → /tools/delay-calculator/ (next Session 38+)

## Tool-in-Entry Pattern (current — Session 37 update)

Tools live inside Bible entries. The tools section (id="tools") in every Tier 1 entry:
- NOW injected immediately after id="quick-reference" closes — high-intent position for SEO and conversion
- Contains GR Calculator + Share This Tool bar (Copy Link → X → Reddit)
- Email gate on download/save output only — tool itself always free

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
State (May 18, 2026): 587 not indexed, 14 indexed. "Discovered - currently not indexed" (585) is normal — Google crawls at its own pace for new sitemaps. Will resolve over weeks.

GSC issues fixed Session 36:
- /ssl-2-plus-review/ — 301 redirect added to netlify.toml → /articles/ssl-2-plus-review.html (both with and without trailing slash)
- /articles/best-studio-monitors-under-300.html — canonical self-closing slash removed
- After deploy: open each URL in GSC and click Request Indexing

After Tier 1 batch commits: regenerate sitemap.xml and resubmit to GSC.
Future improvement: add `<lastmod>` dates to sitemap.xml entries for better crawl budget allocation.

---

# 14. Session 37 — Key Technical Findings

## mpw_bible_writer.py State (end of Session 37 — FINAL)

- Version: v5.1 — Pass 2 rewrite complete
- Model: claude-sonnet-4-6 ✅
- API timeout: 600s ✅
- Validation: 81/81 checks pass ✅
- Pass 2 content quality: APPROVED by Steve ✅
- Tools position: after quick-reference ✅ (new Session 37)
- Tools share bars: Copy Link + X + Reddit ✅ (new Session 37)
- Producer spotlight: cite-tag parsing from rendered HTML ✅ (new Session 37)
- Verdict in sidebar TOC ✅ (new Session 37)
- FAQ empty answer filter ✅ (new Session 37)
- History: 4 cards × 120–150w = 500–600w ✅ (new Session 37)
- Verdict: MPW editorial opinion mandate ✅ (new Session 37)
- UnboundLocalError on html variable: FIXED ✅ (new Session 37)
- SEO: meta description, keywords, HowTo schema, timeRequired ✅ (new Session 37)
- Internal linking: 6–10 amber links per entry ✅ (new Session 37)

## Session 37 — Build Function Order in build_html_t1()

**CRITICAL:** The following order is mandatory to prevent UnboundLocalError:

```python
# 1. Build all component HTML from p1 data
signal_chain = build_signal_chain_svg(...)
genre_html = build_genre_table_html(...)
plugin_html = build_plugin_recs_html(...)
# ... all other components ...
tools_html = build_tools_section(p1, slug)
sidebar_toc = build_sidebar_toc_html(slug)
# NOTE: spotlight_html NOT called yet

# 2. Build html from Pass 2 content
html = content_html
html = html.replace('THE_NUMBER_PLACEHOLDER', ...)
# ... all other replacements ...

# 3. Inject tools after quick-reference via string replacement
if '</section>\n\n<section class="entry-section" id="signal-chain">' in html:
    html = html.replace(..., f'</section>\n{tools_html}\n...')
tools_html_final = ''  # don't append at bottom

# 4. NOW build spotlight (html is fully populated with cite tags)
spotlight_html = build_producer_spotlight_html(p1, quotes_filtered, html)

# 5. Assemble full page
word_count = count_words_html(html)
# ...final assembly...
```

## Handoff Automation System (Session 37)

- mpw_handoff_runner.py: permanent script — fetches, inserts at zone tags, validates, commits
- add_zones.py: one-time — run SHA: 6afa90d5 — DO NOT run again
- session_patch_s37.py: template — copy for each session, update patch dict
- handoff_state.json: local only in mpw-scripts\ — never committed — tracks SHA state

Zone tag format in markdown files: `# SESSION_APPEND_ZONE`
Secrets scrubbed: ghp_ and sk-ant- patterns automatically removed before commit.

---

# 14B. Session 36 — Key Technical Findings

## compression.html Share Bar State (end of Session 36 — FINAL)

All share bars now use .mpw-share-bar class with correct order and branding:

| Bar | Status | Class |
|---|---|---|
| Quick Reference | ✅ Copy Link → X → Reddit | mpw-share-bar |
| GR Calculator | ✅ Copy Link → X → Reddit | mpw-share-bar calc-share-bar |
| Genre Table | ✅ Copy Link → X → Reddit | mpw-share-bar |
| Verdict | ✅ Copy Link → X → Reddit (centered) | mpw-share-bar |
| Tools | ✅ Copy Link → X → Reddit | mpw-share-bar calc-share-bar |
| Bottom page | ✅ Copy Link → X → Reddit | mpw-share-bar |
| Sidebar | ✅ Copy Link → X → Reddit (vertical) | mpw-share-bar |
| Footer | ✅ X → Reddit (Steve's decision — no Copy Link) | inline styled |

## calc-share-bar CSS (Session 36 — appended before </head>)

```css
/* calc-share-bar: auto-width buttons, not flex:1 stretched */
.calc-share-bar { justify-content: flex-start !important; }
.calc-share-bar .mpw-share-btn {
  flex: 0 0 auto !important;
  width: auto !important;
  padding: 0 18px !important;
  height: 34px !important;
}
/* Copy Link — solid amber inside calc bars */
.calc-share-bar .mpw-share-btn.share-copy {
  background: #f5a623 !important;
  color: #000 !important;
  border-color: #f5a623 !important;
}
/* Mobile: 3 equal columns so all buttons sit on one row */
@media(max-width:768px) {
  .calc-share-bar {
    display: grid !important;
    grid-template-columns: 1fr 1fr 1fr !important;
    gap: 6px !important;
  }
  .calc-share-bar .mpw-share-label {
    grid-column: 1 / -1 !important;
  }
  .calc-share-bar .mpw-share-btn {
    width: 100% !important;
    padding: 0 4px !important;
    font-size: 11px !important;
    justify-content: center !important;
  }
}
```

## Session 36 netlify.toml (full content after update)

```toml
[build]
  publish = "."

[[redirects]]
  from = "/ssl-2-plus-review/"
  to = "/articles/ssl-2-plus-review.html"
  status = 301
  force = false

[[redirects]]
  from = "/ssl-2-plus-review"
  to = "/articles/ssl-2-plus-review.html"
  status = 301
  force = false
```

---

# 13. Session 35 — Key Technical Findings

## PowerShell Lessons (Session 35 — CRITICAL)

NEVER paste multi-line Python with CSS values inline in PowerShell.
PowerShell interprets semicolons, colons, and exclamation marks in CSS as command separators.
ALWAYS use Claude's create_file tool → Steve downloads .py file → runs python script.py.

## Sitemap (Session 35)

gen_sitemap.py written and committed to mpw-scripts\.
Counts: 526 articles + 210 Bible entries + 3 static pages = 739 URLs.
Committed to repo. Resubmit to Google Search Console.

---

# 13B. Session 34 — Key Technical Findings

## style.css Audit Results
- Confirmed: NO .bible-entry-wrap rules in style.css
- Confirmed: NO .entry-sidebar rules in style.css
- Has: `.article-layout > aside { display:none !important }` — does not affect Bible pages
- Has: `.article-sidebar` rules — does not affect Bible pages
- Bible page layout is 100% self-contained in page style blocks

## Share Bar CSS Architecture (Session 34 — FINAL)

```css
/* Base — all share buttons */
.mpw-share-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 4px;
  flex: 1 1 0; min-width: 0;
  height: 34px; padding: 0 8px; border-radius: 6px;
  font-size: 11px; font-weight: 700; line-height: 1;
  text-decoration: none; white-space: nowrap;
  cursor: pointer; font-family: inherit;
  box-sizing: border-box; transition: opacity .15s;
}
.mpw-share-btn:hover { opacity: 0.82; }
.mpw-share-btn.share-x { background: #000; color: #fff; border: 1px solid #000; }
.mpw-share-btn.share-reddit { background: #ff4500; color: #fff; border: 1px solid #ff4500; }
.mpw-share-btn.share-copy { background: #f5a623; color: #000; border: 1px solid #f5a623; }

/* Footer override — prevents flex:1 stretching */
.footer-share-btn { flex: 0 0 auto !important; width: auto !important; padding: 0 18px !important; }

/* Mobile — 3-column grid */
@media(max-width:768px) {
  .mpw-share-bar { display: grid !important; grid-template-columns: 1fr 1fr 1fr !important; gap: 6px !important; }
  .mpw-share-label { grid-column: 1 / -1 !important; }
  .mpw-share-btn { width: 100% !important; height: 34px !important; }
}
```

Button order everywhere: **Copy Link → Share on X → Reddit**
Footer exception: **Share on X → Reddit** only (no Copy Link), buttons use both `.mpw-share-btn` and `.footer-share-btn`

## Dead Category Card Slugs (Session 35 — Partial Fix)

7 dead slugs found by mpw_dead_slug_audit.py — 448 references in category card pages:
- about → ../about.html
- genres → ../categories/techniques.html
- daw-comparison-2026 → ../articles/ableton-live-12-vs-fl-studio-21.html
- fl-studio-beginner-guide → ../articles/fl-studio-beginners-guide.html
- how-to-license-music → ../articles/how-music-royalties-work.html
- midi-controller-buying-guide → ../categories/gear.html
- plugins-explained → ../categories/plugins.html

fix_dead_slugs.py written but did not patch (href format mismatch — bare slugs not matching). Needs investigation Session 38 — fetch one category page and print actual href format before writing replacement strings.

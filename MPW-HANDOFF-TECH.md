# MPW-HANDOFF-TECH.md
*Updated: May 19, 2026 (SESSION 41)*

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
│   ├── [slug].html  (526 articles — unchanged Sessions 38 + 39)
│   └── ...
├── bible/
│   ├── index.html (LOCKED — commit 29ee26a9)
│   ├── eq.html (v3.0 gold standard — LOCKED)
│   ├── compression.html (v5.1 gold standard — writer QA complete Session 37)
│   ├── [15 other v5.1 entries with correct tools — patched Session 39]
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
Status: LOCKED

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

# 10. Tools Architecture

## Current State (Session 39)

12 tools live in Bible entries via mpw_tools_v3.py. All 16 Tier 1 entries have working tools confirmed by Steve. Tools section always at id="tools", positioned after id="quick-reference".

Tool CSS class: `.t3` — self-contained, amber branding, no external dependencies, no setTimeout.

## /tools/ Hub Page (Planned)

Standalone page. Not a category page.
Grid of tool cards: tool name + one-line description + which Bible entry it belongs to + "Try Free" button.
Submit to Product Hunt after 5+ tools are live.
URL: musicproductionwiki.com/tools/

## /bible/categories/tools/

9th Bible category. Filter Bible entries that have tool_type != null in bible-index.json.
Build after /tools/ hub page exists.
Link from Bible bar as 9th category pill.

## /tools/[slug]/

Individual tool pages when tools graduate from Bible entries.
GR Calculator → /tools/compression-calculator/ (future)
Delay Calculator → /tools/delay-calculator/ (future)

## Tool-in-Entry Pattern (current)

Tools live inside Bible entries. The tools section (id="tools") in every Tier 1 entry:
- Injected immediately after id="quick-reference" closes — high-intent position for SEO and conversion
- Contains correct interactive tool per slug (per TOOL_OVERRIDES in mpw_tools_v3.py)
- Email gate on download/save output only — tool itself always free
- Share bar: Copy Link + X + Reddit

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

# 14. Session 39 — Key Technical Findings

## mpw_tools_v3.py — Architecture

- Fully self-contained Python file — no external imports
- Public API: `build_tools_section_v3(slug, term)` returns complete HTML string
- 12 tools, 49 slug mappings
- Tool CSS class `.t3` with `.tb` body
- All init functions called directly at end of each tool's script block — NEVER setTimeout
- Brand: teal logomark + MusicProductionWiki.com + ◆ The Producer's Bible + Interactive Tool badge
- Dark amber header (#0d0800), amber border 2px, amber result numbers

## Duplicate Tool Block Root Cause (Session 39)

Multiple patch script iterations (v1–v5) each injected a new tool without cleanly removing all prior injections. Result: some entries ended up with TWO `.t3` blocks:
1. The correct one: inside `<section id="tools">` with direct init calls — WORKING
2. A dead bare block: sitting after `</section>` with dashes (—) for results, possibly with setTimeout — NON-FUNCTIONAL

patch_live_tools_v6.py removes the dead bare block surgically. Does not touch the working section.

Detection pattern: `html.count('<div class="t3">')` — if > 1, duplicate exists.
Removal: find `</section>\n\n` followed by `<style>\n.t3{` — that's the start of the bare block. Remove everything from there to the next `<section class="entry-section"`.

## Tool Init Call Pattern (NEVER use setTimeout)

**WRONG:**
```javascript
setTimeout(function(){ rtCalc(); }, 0);
```

**CORRECT:**
```javascript
rtCalc();
```

Mid-document scripts execute after their preceding DOM is parsed. The tool's inputs and result elements are already in the DOM when the script runs. setTimeout is unnecessary and caused tools to fail to initialize in some browser/load-order combinations.

---

# 14A. Session 38 — Key Technical Findings

## mpw_bible_writer.py State (end of Session 38)

- 16 Tier 1 entries committed (compression + 15 batch)
- Tools visual quality: tools were wrong for 15 entries — needed rebuild
- Tools rebuild completed Session 39 — all 15 now confirmed correct by Steve

---

# 14B. Session 37 — Key Technical Findings

## mpw_bible_writer.py State (end of Session 37 — FINAL)

- Version: v5.1 — Pass 2 rewrite complete
- Model: claude-sonnet-4-6 ✅
- API timeout: 600s ✅
- Validation: 81/81 checks pass ✅
- Pass 2 content quality: APPROVED by Steve ✅
- Tools position: after quick-reference ✅
- Tools share bars: Copy Link + X + Reddit ✅
- Producer spotlight: cite-tag parsing from rendered HTML ✅
- Verdict in sidebar TOC ✅
- FAQ empty answer filter ✅
- History: 4 cards × 120–150w = 500–600w ✅
- Verdict: MPW editorial opinion mandate ✅
- UnboundLocalError on html variable: FIXED ✅
- SEO: meta description, keywords, HowTo schema, timeRequired ✅
- Internal linking: 6–10 amber links per entry ✅

## Session 37 — Build Function Order in build_html_t1()

**CRITICAL:** The following order is mandatory to prevent UnboundLocalError:

```python
# 1. Build all component HTML from p1 data
signal_chain = build_signal_chain_svg(...)
genre_html = build_genre_table_html(...)
plugin_html = build_plugin_recs_html(...)
# ... all other components ...
tools_html = build_tools_section_v3(slug, term)
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

# 14C. Session 36 — Key Technical Findings

## compression.html Share Bar State (end of Session 36 — FINAL)

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
.calc-share-bar { justify-content: flex-start !important; }
.calc-share-bar .mpw-share-btn {
  flex: 0 0 auto !important; width: auto !important;
  padding: 0 18px !important; height: 34px !important;
}
.calc-share-bar .mpw-share-btn.share-copy {
  background: #f5a623 !important; color: #000 !important; border-color: #f5a623 !important;
}
@media(max-width:768px) {
  .calc-share-bar { display: grid !important; grid-template-columns: 1fr 1fr 1fr !important; gap: 6px !important; }
  .calc-share-bar .mpw-share-label { grid-column: 1 / -1 !important; }
  .calc-share-bar .mpw-share-btn { width: 100% !important; padding: 0 4px !important; font-size: 11px !important; justify-content: center !important; }
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
.mpw-share-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 4px;
  flex: 1 1 0; min-width: 0; height: 34px; padding: 0 8px; border-radius: 6px;
  font-size: 11px; font-weight: 700; text-decoration: none; white-space: nowrap;
  cursor: pointer; font-family: inherit; box-sizing: border-box; transition: opacity .15s;
}
.mpw-share-btn:hover { opacity: 0.82; }
.mpw-share-btn.share-x { background: #000; color: #fff; border: 1px solid #000; }
.mpw-share-btn.share-reddit { background: #ff4500; color: #fff; border: 1px solid #ff4500; }
.mpw-share-btn.share-copy { background: #f5a623; color: #000; border: 1px solid #f5a623; }
.footer-share-btn { flex: 0 0 auto !important; width: auto !important; padding: 0 18px !important; }
@media(max-width:768px) {
  .mpw-share-bar { display: grid !important; grid-template-columns: 1fr 1fr 1fr !important; gap: 6px !important; }
  .mpw-share-label { grid-column: 1 / -1 !important; }
  .mpw-share-btn { width: 100% !important; height: 34px !important; }
}
```

Button order everywhere: **Copy Link → Share on X → Reddit**
Footer exception: **Share on X → Reddit** only (no Copy Link)

## Dead Category Card Slugs (Session 35 — Partial Fix)

7 dead slugs found by mpw_dead_slug_audit.py — 448 references in category card pages:
- about → ../about.html
- genres → ../categories/techniques.html
- daw-comparison-2026 → ../articles/ableton-live-12-vs-fl-studio-21.html
- fl-studio-beginner-guide → ../articles/fl-studio-beginners-guide.html
- how-to-license-music → ../articles/how-music-royalties-work.html
- midi-controller-buying-guide → ../categories/gear.html
- plugins-explained → ../categories/plugins.html

fix_dead_slugs.py written but did not patch (href format mismatch — bare slugs not matching). Needs investigation — fetch one category page and print actual href format before writing replacement strings.

---

# SESSION 41 UPDATE — KEY TECHNICAL FINDINGS

## Mobile Fix — Root Cause Confirmed

Inline `style="display:grid!important;..."` on `<div class="bible-entry-wrap">` beat the CONSOLIDATED OVERRIDES stylesheet `display:block!important` at mobile breakpoint.

CSS specificity rule: **inline !important > stylesheet !important**

Fix: removed inline style. CONSOLIDATED OVERRIDES + checkWidth() JS now controls layout correctly.
patch_mobile_fix.py — SHA: a0553356 — 70 entries fixed ✅

## Entry Nav Scroll — Root Cause Confirmed

From live writer CSS line 724 (read directly from mpw_bible_writer.py upload):
`.entry-nav-inner{display:flex;justify-content:center;gap:4px;padding:10px 10px;min-width:max-content;margin:0 auto}`

`min-width:max-content` = inner div exactly as wide as its content.
`justify-content:flex-start` has zero effect when min-width = content width.

**Real fix:** `margin:0!important` — removes auto-centering. Pills start at left edge. Content overflows right. `overflow-x:auto` on `.entry-nav` activates. Scroll works.

patch_nav_mobile.py injected wrong fix — DO NOT USE.
patch_nav_and_btt.py needed — copy margin:0!important from this spec.

## Back-to-Top — Root Cause Confirmed

patch_mobile_fix.py injected checkWidth() JS before `</body>`.
build_js() scroll listener calls `getElementById('btt-btn')`.
The `<button id="btt-btn">` HTML element was NEVER injected into entries.
`getElementById` returned null. Listener attached to non-existent element.
Nothing shown.

Fix: inject the button HTML element + scroll JS before `</body>`.
Exact code in MPW-HANDOFF-CORE.md Session 41 update section.

## Live Bible State After All Session 41 Patches

| Issue | v5.1 Original 16 | Session 40 new 54 | v3.0 153 |
|---|---|---|---|
| Mobile layout | ✅ FIXED | ✅ FIXED | ✅ N/A |
| Entry nav scroll | ❌ BROKEN | ❌ BROKEN | ✅ N/A |
| Back-to-top button | ❌ MISSING (15 of 16) | ❌ MISSING | ✅ N/A |
| Tools position | ✅ CORRECT | ❌ AT BOTTOM | ✅ N/A |
| Verdict quality | ✅ GOOD | ❌ WEAK | ✅ N/A |
| Genre table | ✅ CORRECT | ❌ N/A COLUMNS | ✅ N/A |
| Producer quotes | ✅ 2 (ok for now) | ❌ 2 ONLY | ✅ N/A |

compression.html: ALL features working ✅ (only entry with everything correct)

## Entry Count Correction

Previous handoff incorrectly stated 226 entries and 210 v3.0 entries.
mpw_diagnose.py confirmed: **223 total — 16 + 54 + 153**.
bible-index.json still shows 210 (v3.0 only — not updated for v5.1 entries).

---

# SESSION 41 ADDENDUM — Tools Section Nav Tracking

## Root Cause (read from live writer and compression.html)

compression.html GR Calculator: `id="gr-calculator"` — NOT a `<section class="entry-section">`, NO `<h2>`. Sits between Quick Ref and Signal Chain. The IntersectionObserver watches for `id="tools"` — that's the nav card at the BOTTOM of compression, not the calculator.

Result: Tools nav pill does not activate when user views the GR Calculator.

mpw_tools_v3.py `_wrap()` generates correct structure: `<section class="entry-section" id="tools"><h2>Tools for This Entry</h2>`. This WILL track correctly for all entries that use it in the right position.

Fix for compression.html: wrap gr-calculator in `<section class="entry-section" id="tools"><h2>Tools for This Entry</h2>` and remove the separate bottom tools nav card. Fetch file before patching.

Fix for Session 40 entries: regenerate with v5.2 writer (tools position fix).

---

# SESSION 46 UPDATE — KEY TECHNICAL FINDINGS

## Tool JS Root Causes — Solved

Three bugs killed the LFO tool on every Bible entry:

### Bug 1 — "" leak after </script> in mpw_tools_v3.py
Pattern in every tool body string:
```python
    ...calc();\n</script>""
    """
    return _wrap(...)
```
The `""` between `</script>` and `"""` emitted literally into HTML → JS SyntaxError → all tool JS dead.
Fixed by `fix_v3_permanent.py`.

### Bug 2 — Duplicate {tools_html} in writer f-string
Tools were injected twice: once via `TOOLS_PLACEHOLDER` replacement (correct) and once via `{tools_html}` in the final page assembly f-string (duplicate). Result: two `<section id="tools">` blocks, duplicate DOM IDs, lfoCalc fails.
Fixed by `fix_writer_permanent.py`.

### Bug 3 — Single-quoted LTIPS JS strings with apostrophes
LTIPS dict values used single-quoted JS strings containing `you've`, `don't` etc. Apostrophes terminated strings early → `Unexpected identifier 've'` SyntaxError.
Fixed by `fix_v3_permanent.py` — all 7 LTIPS values converted to double-quoted JS strings.

## Fix Scripts (save to mpw-scripts\)

| Script | Purpose | Idempotent |
|---|---|---|
| fix_v3_permanent.py | Fixes "" leak + LTIPS quotes in mpw_tools_v3.py | Yes — safe to re-run |
| fix_writer_permanent.py | Removes duplicate {tools_html} from writer | Yes — safe to re-run |
| verify_fixes.py | Confirms all 3 fixes applied to both files | Yes — run any time |

## ⚠️ Install Scripts STALE

install_bible_writer_v52_part1/2/3.ps1 write the UNFIXED mpw_bible_writer.py.
DO NOT RUN. P0b next session: generate new install scripts from fixed file on disk.

## Diagnostic Commands (Session 46)

```powershell
# Verify fixes:
python verify_fixes.py

# Check tool section count in HTML (write to .py file, not inline):
# python count_tools.py

# Generate test entry:
. .\setenv.ps1; python mpw_bible_writer.py --test --slug chorus --term "Chorus" --category "Time-Based" --tier 1 --no-commit
```

---

# SESSION 47 UPDATE — KEY TECHNICAL FINDINGS

## v5.2 Writer — Architecture Changes Session 47

### Plugin Section Merge (FIX 43)
`id="hardware-plugin"` and `id="plugin-recs"` merged into single `id="plugins"`. All nav pills, sidebar TOC entries, and Pass 2 prompt references updated. `PLUGIN_RECS_PLACEHOLDER` now lives inside `id="plugins"`. Nav order and sidebar TOC order now match canonical section order exactly.

### Quote System (FIX 44)
Pass 1 now receives `available_quote_authors` list from quotes.json and must select spotlight producers from it. Pass 2 now receives actual quote text verbatim for each spotlight producer. However, quotes.json is missing entries for Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, and other producers that Pass 1 wants to select for modulation entries. The mismatch continues until these quotes are added to quotes.json.

### Internal Link Color (FIX 50)
`.entry-main a` now has explicit amber color in both regular CSS and CONSOLIDATED OVERRIDES with !important. Mobile browser-default blue links eliminated. `.entry-breadcrumb a` rule is more specific and wins — breadcrumb links not affected.

### Verdict Share Bar (FIX 45)
Post-processor in build_html_t1() hardcodes the verdict share bar regardless of what Pass 2 writes. No more plain text "Copy Verdict + Share on X + Reddit" appearing in the verdict section.

### Session File Breakdown (FIX 49)
Step text "Step N —" prefix stripped by build_session_breakdown_html() regex. Number circles handle numbering.

### Difficulty Badge (FIX 48)
Removed from masthead visual display. Remains in JSON-LD schema for SEO. Visual badge was confusing — entries cover all three levels in their progression section.

### Read Time (FIX 47)
500 wpm confirmed by Steve. count_words_html() strips non-prose blocks (tables, tools, nav, DAW tabs, signal chain) before counting. Read time now reflects prose only.

### Footer Share Bar (FIX 46)
Footer share buttons converted from inline styles to mpw-share-btn classes. X + Reddit only (no Copy Link) — Steve's confirmed decision. Pattern now consistent with spec.

## v5.2 Structural Fingerprints — New in Session 47

| # | Fingerprint | Value |
|---|---|---|
| 22 | id="plugins" (merged) | Single section — hardware table + plugin recs — no id="hardware-plugin" or id="plugin-recs" |
| 23 | MusicProductionWiki Recommends | Hardcoded amber intro block before plugin cards — never "MPW Recommends" |
| 24 | .sfb-step / .sfb-num / .sfb-text | Session File Breakdown CSS — amber number circles |
| 25 | .entry-main a color | Amber #f5a623 — explicit override to prevent browser-default blue |
| 26 | Verdict share bar post-processed | Hardcoded by build_html_t1() — not written by Pass 2 |

## Canonical Section Order — v5.2 (LOCKED)

Nav pills and sidebar TOC MUST match this order exactly:
1. Definition
2. How It Works
3. Parameters
4. Quick Reference
5. Tools (after Quick Reference)
6. Signal Chain
7. History
8. How To Use
9. Genre Table
10. Plugins & Hardware (merged — id="plugins")
11. Before / After
12. In The Wild
13. Signatures
14. Types
15. Verdict
16. Mistakes
17. Flags
18. Progression
19. FAQ
20. Related

## Session 47 CSS Additions to build_css()

```css
/* entry-main link color — prevents browser-default blue */
.entry-main a{color:#f5a623;text-decoration:none;border-bottom:1px solid rgba(245,166,35,0.3)}
.entry-main a:hover{color:#ffbb44;border-bottom-color:rgba(245,166,35,0.7)}

/* CONSOLIDATED OVERRIDES addition */
.entry-main a{color:#f5a623!important;text-decoration:none!important}
.entry-main a:hover{color:#ffbb44!important}

/* Session File Breakdown */
.sfb-step{display:flex;gap:10px;margin-bottom:10px;font-size:13px;color:#c8c8d8;line-height:1.6}
.sfb-num{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;min-width:22px;background:#f5a623;color:#000;font-size:11px;font-weight:800;border-radius:50%;flex-shrink:0;margin-top:2px}
.sfb-text{flex:1}
```

## Install Scripts State — End of Session 47

| Script | Status |
|---|---|
| install_writer_v52_s47d_part1/2/3.ps1 | ✅ CURRENT — use these |
| install_writer_v52_s47b_part1/2/3.ps1 | ❌ SUPERSEDED — DO NOT RUN |
| install_writer_v52_s47_part1/2/3.ps1 | ❌ PS1 syntax error — DO NOT RUN |
| install_writer_v52_s46_part1/2/3.ps1 | ❌ SUPERSEDED — DO NOT RUN |
| install_bible_writer_v52_part1/2/3.ps1 | ❌ Writes unfixed writer — DO NOT RUN |

## Diagnostic Commands — Session 47

```powershell
# Verify all fixes applied:
python verify_fixes.py

# Test chorus entry:
. .\setenv.ps1; python mpw_bible_writer.py --test --slug chorus --term "Chorus" --category "Time-Based" --tier 1 --no-commit

# After chorus confirmed — regen all 70:
. .\setenv.ps1; python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-21 --workers 8

# After regen:
python mpw_bible_cat_pages.py --run
python gen_sitemap.py
# Submit sitemap to GSC manually
```

---

# SESSION 51 UPDATE — May 21, 2026

## reverb.html S51 — Technical Architecture Notes

### bible-entry-wrap — CSS-only approach (S51 change)

reverb.html does NOT use `display:grid` in the inline style on `bible-entry-wrap`. Grid is handled entirely in CSS:
```css
/* In main style block: */
.bible-entry-wrap{max-width:1100px;margin:0 auto;padding:40px 24px;display:grid;grid-template-columns:1fr 280px;gap:40px;align-items:start}
/* In CONSOLIDATED OVERRIDES: */
@media(min-width:769px){
  .bible-entry-wrap{display:grid!important;grid-template-columns:1fr 280px!important;...}
  .entry-sidebar{display:block!important;...}
}
@media(max-width:768px){
  .bible-entry-wrap{display:block!important;...}
  .entry-sidebar{display:none!important}
}
```
The inline style on the element is: `style="max-width:1100px;margin:0 auto"` ONLY.
This is cleaner than compression.html's nuclear inline approach and avoids mobile override issues.

### Entry Nav + Sidebar TOC Scroll Offset — Critical Values

```javascript
// Desktop: 148px (40px slim-bar + 50px bible-bar + 40px entry-nav + 18px buffer)
// Mobile: 84px (40px slim-bar + 44px bible-bar mobile height)
// S51 bug: offset was 60px (entry nav) and 140px (sidebar TOC) → pills frozen
// Fixed to 148px for both
```

### JS String Safety — Apostrophe Rule

All JS string literals containing natural language text MUST use escaped apostrophes or double quotes:
```javascript
// WRONG — breaks entire script block:
{type:'q', text:'Elements don't sound cohesive', answers:[...]}

// CORRECT option 1 — escaped apostrophe:
{type:'q', text:'Elements don\'t sound cohesive', answers:[...]}

// CORRECT option 2 — double quotes:
{type:"q", text:"Elements don't sound cohesive", answers:[...]}
```
This is the SAME bug class as LTIPS single-quoted strings (Session 46, Root Cause 3). Now a NEVER rule.

### S51 Interactive Features — JS Architecture

**Settings Fingerprint (id="fingerprint"):**
- IIFE draws with `setTimeout(draw, 0)`
- Genres object: 8 genres, 5 axes each (decay, diffusion, predelay, damping, width)
- `activeG = null` shows all polygons; set to genre name highlights one
- Genre buttons in `fp-controls` div, created by IIFE
- Legend items in `fp-legend` div, created by IIFE

**Decision Tree (id="decision-tree"):**
- `DT_S` = current node index (0-15)
- `DT_N` = array of 16 nodes: type 'q' (question with answers array) or type 'fix' (fix text)
- `dtRender()` called on load, on `dtAnswer(next)`, on `dtReset()`
- All text in DT_N uses escaped apostrophes

**Error Diagnostic (in id="mistakes"):**
- `ED_A` = object tracking selected symptoms
- `ED_F` = object mapping symptom key → fix text
- `edToggle(btn, key)` adds/removes from ED_A, calls edUpdate()
- `edUpdate()` builds combined fix text from all selected symptoms
- `edClear()` resets all

**Recall Sheet (id="recall-sheet"):**
- `contenteditable="true"` spans for each field
- `downloadRecallSheet()` reads all spans by ID, builds .txt, triggers download

### reverb.html S51 Structural Fingerprints

| # | Fingerprint | Value |
|---|---|---|
| 1 | Sections | 28 (id: definition through related) |
| 2 | File size | 191KB |
| 3 | BTT button | class="btt-btn" id="btt-btn" — present ✅ |
| 4 | bible-entry-wrap | max-width + margin ONLY in inline style — NO display:grid inline |
| 5 | Entry nav offset | 148px desktop, 84px mobile — FIXED S51 |
| 6 | Sidebar TOC offset | 148px — FIXED S51 |
| 7 | DT_N apostrophes | All escaped with \' — FIXED S51 |
| 8 | Footer share | X + Reddit ONLY — no Copy Link |
| 9 | ts-badge | Timestamp class on 7 track examples |
| 10 | Settings Fingerprint | SVG radar chart, 8 genres, 5 axes |
| 11 | Decision Tree | 16-node branching JS diagnostic |
| 12 | Error Diagnostic | 8 symptom buttons, edToggle() |
| 13 | Recall Sheet | contenteditable spans, downloadRecallSheet() |
| 14 | Producer DNA | 3 dna-card divs (Clearmountain, Everett, Finneas) |
| 15 | Psychoacoustics | 6 psy-card divs |
| 16 | Era Translator | 6-row et-table |
| 17 | Contrast Listen | 2 cl-card divs + cl-vs separator |
| 18 | Mono Check | 6 mc-item divs with mc-safe/mc-risk/mc-danger |
| 19 | Symptom Diagnostic | 7 sd-btn buttons at top of main |
| 20 | RT60 Calculator | .t3 tool, rtCalc(), rtRoom(), 6 presets |

## File Location

reverb.html: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html`
Commit target: `bible/reverb.html` in GitHub repo

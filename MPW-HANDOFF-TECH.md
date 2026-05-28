# MPW-HANDOFF-TECH.md
*Updated: May 26, 2026 (SESSION 70 — Full merge: S65 + S65b + S66 + S67 + S68 appends integrated)*

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
| Scripts dir | C:\Users\swarn\OneDrive\Desktop\mpw-scripts\ |
| Article storage | C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles (⚠️ Steve to confirm if still active path) |
| Search Console | Google Search Console |
| Contact | team@musicproductionwiki.com (Fastmail) |
| Legacy contact | mpwikiofficial@gmail.com (kept as fallback) |
| Analytics | GA4 — G-79VB543KCT |
| Pretty URLs | NEVER enable — breaks site |
| Proxy URL | https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy |
| Claude model | claude-sonnet-4-6 (NEVER claude-sonnet-4-5 or claude-sonnet-4-20250514) |


---

# File Structure

```
repo root/
├── index.html
├── about.html
├── genres.html
├── brands.html (MISSING — in nav but no page)
├── netlify.toml (updated Session 67 — /dictionary/* redirect + function build command added)
├── css/style.css
├── js/main.js
├── js/mpw-analytics.js
├── search-index.json
├── sitemap.xml (744 URLs — submit to GSC pending)
├── bible-index.json (223 entries)
├── favicon.svg (teal square with bar chart — committed Session 67)
├── favicon.ico
├── MPW-CATALOG.md (auto-generated)
├── MPW-HANDOFF-CORE.md
├── MPW-HANDOFF-SCRIPTS.md
├── MPW-HANDOFF-CONTENT.md
├── MPW-HANDOFF-BIBLE.md
├── MPW-HANDOFF-ARTICLES.md
├── MPW-HANDOFF-TECH.md
├── MPW-TOOL-BUILD-SPEC.md (frozen tool design system — do not modify)
├── netlify/
│   └── functions/
│       └── claude-proxy.js (Anthropic API proxy — committed Session 67)
├── articles/
│   └── [slug].html  (526 articles — ALL updated Session 65: Tools→ nav, grid drawer, pushState JS, CSS fix)
├── bible/
│   ├── index.html (REBUILT S63 — reverb nav, Beehiiv wired — SHA 7bfb2b6b)
│   ├── reverb.html (gold standard T1 entry — v1.6 — SHA 8b6dd26d — 324KB)
│   ├── compression.html (v5.1 gold standard — LOCKED)
│   ├── [15 other v5.1 entries — tools injected, nav confirmed]
│   ├── [54 v5.1 Session 40 entries]
│   ├── [153 v3.0/v4.0 legacy entries]
│   └── categories/
│       ├── dynamics/index.html     ← bmn-drawer ✅ replaceState ✅
│       ├── frequency/index.html    ← bmn-drawer ✅ replaceState ✅
│       ├── time-based/index.html   ← bmn-drawer ✅ replaceState ✅
│       ├── signal-processing/index.html ← bmn-drawer ✅ replaceState ✅
│       ├── mixing/index.html       ← bmn-drawer ✅ replaceState ✅
│       ├── mastering/index.html    ← bmn-drawer ✅ replaceState ✅
│       ├── synthesis/index.html    ← bmn-drawer ✅ replaceState ✅
│       ├── music-theory/index.html ← bmn-drawer ✅ replaceState ✅
│       ├── production/index.html   ← bmn-drawer ✅ replaceState ✅
│       ├── recording/index.html    ← bmn-drawer ✅ replaceState ✅
│       └── tools/index.html        ← bmn-drawer ✅ replaceState ✅ "The Producer's Tools" ✅
├── tools/
│   ├── index.html           ← LIVE — SHA 8c7269d2 (amber cards + nav fix) ✅
│   ├── browser-daw.html     ← LIVE — SHA 2a0e05c2 ✅
│   ├── suno-prompt-optimizer.html    ← LIVE — ⚠️ needs UI/function update
│   ├── ai-music-rights-navigator.html ← LIVE — ⚠️ needs UI/function update
│   ├── ai-music-ddex-checker.html    ← LIVE — SHA 206e2a44 — ⚠️ needs UI/function update
│   ├── ai-copyright-strength.html    ← LIVE — SHA 7f113017 — ⚠️ needs UI/function update
│   ├── suno-credits-calculator.html  ← LIVE — SHA 4d827292 — ⚠️ needs UI/function update
│   └── [31 other tool pages]        ← LIVE ✅
└── categories/
    └── [category].html  (90 pages)
```

Asset paths in articles: `../css/style.css`, `../js/main.js`
Asset paths in tools: `../js/main.js` ONLY — NEVER `../css/style.css` (causes 600px blobs)
Asset paths in bible: self-contained (NO main.js on bible pages)
Asset paths in bible/categories: self-contained (NO main.js)
Asset paths in categories: `../css/style.css`, `../js/main.js`

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

---

# 10. Tools Architecture

## Current State (Session 70)

**Total tools live: 40**

- 12 tools in Bible entries via mpw_tools_v3.py (all 16 Tier 1 entries confirmed working)
- 24 v5 dispatch tools (mpw_tools_v5_dispatch.py — 145 slugs)
- 4 tools standalone at /tools/: browser-daw.html + 3 built in parallel sessions (see below)

Tool CSS class: `.t3` (v3), `.t4` (v4), `.t5` (v5) — all self-contained, amber branding, no external dependencies.

**Tools needing UI/function update (built in undocumented parallel sessions):**
- suno-prompt-optimizer.html — ⚠️ needs UI redesign (dedicated session, read MPW-TOOL-BUILD-SPEC.md first)
- ai-music-rights-navigator.html — ⚠️ needs UI/function update
- ai-music-ddex-checker.html — SHA 206e2a44 — ⚠️ needs UI/function update
- ai-copyright-strength.html — SHA 7f113017 — ⚠️ needs UI/function update
- suno-credits-calculator.html — SHA 4d827292 — ⚠️ needs UI/function update

## /tools/ Hub Page (Live)

URL: musicproductionwiki.com/tools/
File: tools/index.html — SHA 8c7269d2
Hand-crafted HTML — NEVER convert to a generator script (full design control).
Static label only — NEVER show tool count (goes stale).
Stats row: `Free forever · No signup required · Works on mobile` — never change.

## /bible/categories/tools/

9th Bible category. Filters Bible entries that have tool_type != null in bible-index.json.
Link from Bible bar as 9th category pill. ✅ Live (regenerated S63).

## /tools/[slug]/

Individual tool pages. All 36+ tool slugs live at this path.
NEVER use bible-bar/slim-bar nav on /tools/ pages — uses mpw-site-nav system.

## Tool-in-Entry Pattern (current)

Tools live inside Bible entries. The tools section (id="tools") in every Tier 1 entry:
- Injected immediately after id="quick-reference" closes — high-intent position
- Contains correct interactive tool per slug (per TOOL_OVERRIDES in mpw_tools_v3.py)
- Email gate on download/save output only — tool itself always free

## Tool Dispatch Architecture — v5

```python
# Import pattern for mpw_bible_writer.py integration
from mpw_tools_v5_dispatch import build_tools_section_v5
# Dispatcher routes 145 slugs to correct tool function
# 24 tools across 3 Python files: v5a (T1-T8), v5b (T9-T16), v5c (T17-T24)
```

## Tool Mapping Checklist — Required After Every Tool Build

Run this check before closing any tool build session:

```
[ ] tools/[slug].html — committed to GitHub
[ ] tools/index.html — card added, count updated, same Trees API commit
[ ] bible/categories/tools/index.html — bcat-card added INSIDE #catGrid div (verify position)
[ ] sitemap.xml — URL added with priority 0.8
[ ] search-index.json — entry added with category "Tools"
[ ] GSC — URL inspection + request indexing (Steve)
[ ] OG image — /images/[slug]-og.jpg referenced (Steve creates)
```

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

---

# SESSION 52 UPDATE — May 22, 2026

## New Gold Standard Bible Entry — reverb_v11.html

reverb_v11.html is now the T1 gold standard. File: bible/reverb.html after commit.
Size: 299.7KB. Lines: 2,593. 4 script blocks — all pass node --check.

## Email Standard

All Bible entries now use: **team@musicproductionwiki.com**
Legacy: mpwikiofficial@gmail.com (kept as fallback only)
Updated in reverb_v11.html — 2 instances.

## Upload Method Clarification (CRITICAL)

The 200KB Cloudflare limit applies ONLY to ZIP files via Notepad → Save As → All Files.
Single-file GitHub API PUT has NO size limit.
reverb.html at 299.7KB is fine for single-file PUT.

| Method | Size Limit | Use For |
|---|---|---|
| GitHub API PUT (single) | None | Single Bible entry, single article fix |
| GitHub Trees API | None | Multi-file batch (2+ files) |
| Notepad → Save As → All Files | 200KB (Cloudflare intercepts larger ZIPs) | Local file save only — not the upload method |
| GitHub web editor | NEVER | Silent corruption |

## Bible Entry CSS Architecture (CRITICAL — ADDED S52)

Main CSS is one large minified <style> block in <head> containing fingerprint comments.
CSS injection MUST be append-only — add NEW <style> block before </head>.
NEVER modify the existing block. Regex targeting fingerprints destroys the entire block.

```html
<!-- CORRECT: append new style block -->
<style>
  .new-feature { ... }
</style>
</head>

<!-- WRONG: modify existing block — destroys all CSS -->
```

## Bible Entry JS Architecture (ADDED S52)

IntersectionObserver for sidebar TOC — rootMargin: '-120px 0px -60% 0px'
Entry nav offset: 60px for getBoundingClientRect highlighting
Mobile: entry-nav top 84px, sidebar hidden, grid becomes block

```javascript
// Correct sidebar TOC implementation:
var tocLinks = document.querySelectorAll('.sidebar-toc a');
function setTocActive(id){ tocLinks.forEach(function(a){ a.classList.toggle('active', a.getAttribute('href')==='#'+id); }); }
var sections = document.querySelectorAll('.entry-section[id]');
var obs = new IntersectionObserver(function(entries){ entries.forEach(function(e){ if(e.isIntersecting) setTocActive(e.target.id); }); }, {rootMargin:'-120px 0px -60% 0px'});
sections.forEach(function(s){ obs.observe(s); });
if(sections[0]) setTocActive(sections[0].id);
```

## JS Safety Protocol (ADDED S52)

All JS in Bible entries must be:
1. ASCII-safe — no unicode chars directly — use \uXXXX escapes
2. Apostrophe-safe — possessives + contractions escaped with \'
3. No literal newlines in string values
4. No literal newlines in regex literals (scan separately)
5. All script blocks pass node --check before output

## New CSS Namespaces in reverb_v11.html

| Prefix | Feature |
|---|---|
| .mtt-* | Mix Translation Tool |
| .dna-chain-* | DNA Signal Chain panels |
| .beginner-protocol-grid | Beginner Trap protocol grid |
| .framework-qr | Decision Framework quick reference grid |
| .psy-* | Psychoacoustics block (folded into Definition) |
| .cl-* | Contrast Listen (folded into In The Wild) |
| .mc-* | Mono Check (folded into Mistakes) |
| .et-* | Era Translator (folded into History) |
| .t3, .tb, .sh, .tr, .rb, .tc, .co, .nt | Standard tool container classes |

## JS Functions in reverb_v11.html Main Script Block

| Function | Purpose |
|---|---|
| rtCalc(), rtRoom(r) | RT60 Calculator |
| fpDraw(), fpBtn(b,g) | Fingerprint radar chart |
| dawTab(b,d) | DAW tab switcher |
| faqToggle(i) | FAQ accordion |
| dtRender(), dtAnswer(n), dtReset() | Decision Tree |
| edToggle(sym), edClear() | Error Diagnostic |
| tcCalc() | Tempo-Locked Calculator |
| mttRender(), mttSelect(idx), mttToggle(si,sym), mttMarkFixed(si,sym), mttMarkDone(si), mttExport() | Mix Translation Test |
| atlRender(), atlSelect(idx), atlClick(e,...) | Arrangement Timeline |
| dnaToggle(pid) | DNA Signal Chain panel toggle |

## reverb.html Commit Command

```powershell
. .\setenv.ps1
$content = [System.IO.File]::ReadAllBytes("C:\Users\swarn\OneDrive\Desktop\mpw-scripts\reverb.html")
$base64 = [System.Convert]::ToBase64String($content)
$sha_resp = Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Headers @{Authorization="token $env:GITHUB_TOKEN"} -ErrorAction SilentlyContinue
$body = @{message="feat: reverb.html S52 — world-class gold standard — 10 additions — 23 sections";content=$base64;branch="main"}
if ($sha_resp.sha) { $body.sha = $sha_resp.sha }
Invoke-RestMethod -Uri "https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/bible/reverb.html" -Method PUT -Headers @{Authorization="token $env:GITHUB_TOKEN";"Content-Type"="application/json"} -Body ($body | ConvertTo-Json)
```

---

# SESSION 53 UPDATE — May 22, 2026

## reverb.html S53 — Final Gold Standard Fingerprints

| # | Fingerprint | Value |
|---|---|---|
| 1 | File size | 324KB (up from 299.7KB S52) |
| 2 | Lines | 2,745 |
| 3 | Script blocks | 4 — all pass node --check |
| 4 | Sections | 25 (beginner-trap repositioned to section 3) |
| 5 | Nav pills | 25 — correct order including beginner-trap at position 3 |
| 6 | Sidebar | TOC + Newsletter + Share — NO Producer Spotlight |
| 7 | bible-entry-wrap | max-width:1100px;margin:0 auto ONLY (no display:grid inline) |
| 8 | BTT button | Present ✅ |
| 9 | Version history | v1.4 May 22, 2026 — 14 itemized changes |
| 10 | Dates | All May 22, 2026 |
| 11 | Plugin section | Three editorial cards (Free/Mid/Pro) with descriptions + affiliate links |
| 12 | Share buttons (sidebar) | flex:none;width:100% — NOT width:100%;justify-content:center |

## Sidebar DOM Architecture (UPDATED S53)

```html
<aside class="entry-sidebar" style="min-width:280px;width:280px">
  <div class="sidebar-toc">
    <h4>Contents</h4>
    <!-- 25 TOC links — beginner-trap at position 3 -->
  </div>
  <div class="sidebar-nl">
    <!-- Newsletter signup -->
  </div>
  <div style="background:#13132a;...">
    <!-- Share This Entry -->
    <!-- Buttons use flex:none;width:100% — NOT justify-content:center -->
  </div>
</aside>
```

**Producer Spotlight div is removed entirely from sidebar.** CSS rule `.producer-spotlight` remains in the style block (it is used on other entries) but the HTML element is not present in reverb.html S53 or any future T1 entry.

## GitHub Commit Capability — Confirmed S53

Claude can commit single Bible entries directly from bash environment via GitHub API PUT using the stored token. Confirmed working in Session 53 (commit + revert both successful). This is the correct method for single-file Bible entry commits going forward.

- No size limit on API PUT (only ZIP/Notepad method has 200KB limit)
- reverb.html at 324KB commits cleanly
- Steve must explicitly authorize the commit ("go ahead and commit")

## Affiliate Link Architecture (NEW S53)

Plugin links in Bible entries now use `rel="noopener sponsored"` on all paid plugin recommendations.

```html
<a href="https://[manufacturer-url]" target="_blank" rel="noopener sponsored" style="...">View on [Manufacturer] →</a>
```

When Plugin Boutique / Sweetwater / Loopmasters affiliate programs are approved:
1. Swap URL to affiliate tracking URL
2. No structural HTML changes needed
3. `rel="sponsored"` is already in place for Google compliance

Transparency note template (already in reverb.html):
> "Plugin prices listed are standard retail. Links above go directly to manufacturer sites. When Plugin Boutique and Sweetwater affiliate programs are live, discounted links will be added here. All editorial picks remain independent of commercial relationships."

---

# SESSION 54 UPDATE — May 22, 2026

## reverb.html S54 — Final Gold Standard Fingerprints

| # | Fingerprint | Value |
|---|---|---|
| 1 | File size | 383.5KB |
| 2 | Lines | 3,140 |
| 3 | Script blocks (internal) | 4 — all pass node --check |
| 4 | Script blocks (external, head) | 2 — Beehiiv loader + attribution |
| 5 | Sections | 25 — unchanged |
| 6 | Nav pills | 25 — correct order |
| 7 | Type cards | 7 — Shimmer added as standalone |
| 8 | Version | v1.6 (May 22, 2026) |
| 9 | wordCount schema | 16500 |
| 10 | Read time displayed | 33 min |
| 11 | Beehiiv form ID | a0962c52-4819-4b09-b13d-b26517b76e01 |
| 12 | Title tag | Reverb: Settings, Types & Pro Techniques | The Producer's Bible |

## Beehiiv Newsletter Infrastructure (NEW S54)

**Embed method:** Beehiiv v3 script loader (NOT iframe — confirmed with Beehiiv dashboard)

```html
<!-- In <head> — both scripts required -->
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="a0962c52-4819-4b09-b13d-b26517b76e01"></script>
<script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script>

<!-- In body — one div per form location -->
<div data-beehiiv-form="a0962c52-4819-4b09-b13d-b26517b76e01"></div>
```

**Form details:**
- Publication: The Producer's Briefing
- Form ID: `a0962c52-4819-4b09-b13d-b26517b76e01`
- From address: `theproducersbriefing@mail.beehiiv.com`
- Reply-To: `team@musicproductionwiki.com`
- Plan: Launch (free) — 1/2,500 subscribers
- Double opt-in: check setting — recommend disabling for music production audience

**All T1 Bible entries going forward must include both Beehiiv scripts in `<head>` and replace any static email input/button newsletter forms with `data-beehiiv-form` divs.**

## CSS Architecture Update — cl-grid (S54)

The Contrast Listen grid was fixed from a broken 2-column layout to a correct 3-column layout.

**CORRECT (S54 standard):**
```css
.cl-grid { display:grid; grid-template-columns:1fr auto 1fr; gap:0; align-items:stretch }
.cl-vs { display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900; color:#f5a623; padding:0 20px; flex-shrink:0 }
```

**WRONG (causes card wrap):**
```css
.cl-grid { display:grid; grid-template-columns:1fr 1fr; gap:16px }
```

Rule: whenever a separator element (VS, OR, →) is a direct grid child between two content columns, the grid must be `1fr auto 1fr` — never `1fr 1fr`.

## SEO Standards Update (S54)

### Title Tag Pattern for Bible Entries
`{Term}: Settings, Types & Pro Techniques | The Producer's Bible`

Adjust secondary terms to match the entry's actual content:
- For time-based: "Settings, Types & Pro Techniques"
- For dynamics: "Settings, Types & Signal Chain"
- For frequency: "Settings, Types & EQ Techniques"
- For synthesis: "Parameters, Types & Sound Design"

### Meta Description Pattern
Lead with the entry's strongest differentiator — not generic description.
Format: `The definitive {term} guide: {tool/feature 1}, {differentiator 2}, {differentiator 3}, and every {common problem} fixed with exact parameters.`

Example (reverb): `The definitive reverb guide: RT60 calculator, producer signal chains (Clearmountain, Everett, Finneas), The Three Questions framework, 7 reverb types, genre settings, and every common mistake fixed with exact parameters.`

## Affiliate Link Policy (CONFIRMED S54)

| Link Type | rel attribute | Example |
|---|---|---|
| Paid plugin (affiliate pending) | `rel="noopener sponsored"` | Valhalla Room, FabFilter Pro-R 2 |
| Free plugin (no affiliate) | `rel="noopener"` | Valhalla Supermassive, Dragonfly Reverb |
| External reference (no affiliate) | `rel="noopener"` | Wikipedia, Wikidata |
| Internal | none | /bible/delay, /articles/valhalla-room-review.html |

**NEVER use `rel="sponsored"` on free plugin links — Google policy violation.**

## reverb.html Commit Command (Session 55)

Claude commits directly from bash after Steve uploads reverb_v16b.html renamed as reverb.html.

```bash
# Claude executes this in bash after file is uploaded to session
TOKEN="ghp_[REDACTED — stored in setenv.ps1 — expires Aug 2 2026]"
# Read file, base64 encode, get current SHA, PUT to GitHub
# Commit message: "feat: reverb.html S54 — definitive reverb reference — v1.6 — 383KB — SEO + revenue pass"
```

File size 383.5KB — fine for single-file API PUT (no size limit applies to API PUT).

---

# SESSION 54 ADDENDUM — TECHNICAL ARCHITECTURE FOR NEW BIBLE TYPES — May 22, 2026

## New Content Type File Structure

```
bible/
├── index.html (LIVE — LOCKED)
├── [term].html (T1/T2/T3 entries — existing)
├── producers/
│   └── [producer-slug].html (Type 4 — Producer DNA entries)
├── tracks/
│   └── [track-slug].html (Type 5 — Track Anatomy entries)
├── gear/
│   └── [gear-slug].html (Type 6 — Gear/Plugin Reference entries)
└── genres/
    └── [genre-slug].html (Type 7 — Genre Production Bible entries)
```

**URL structure:**
- Producer DNA: `/bible/producers/metro-boomin`
- Track Anatomy: `/bible/tracks/billie-jean`
- Gear Reference: `/bible/gear/valhalla-room`
- Genre Bible: `/bible/genres/trap`

**NOTE: URL structure must be confirmed before any batch runs. Verify Netlify routing handles these subdirectory paths correctly before committing first entries.**

## New Bible Index Categories

bible-index.json must be updated to include all 7 content types. New fields required:

```json
{
  "slug": "metro-boomin",
  "term": "Metro Boomin",
  "type": "producer-dna",
  "category": "Producer DNA",
  "path": "/bible/producers/metro-boomin",
  "definition": "One of the most influential trap producers of the 2010s..."
}
```

Type field values: `"t1"`, `"t2"`, `"t3"`, `"producer-dna"`, `"track-anatomy"`, `"gear-reference"`, `"genre-bible"`

## Schema Requirements by Content Type

### Type 4 — Producer DNA
```json
{
  "@type": "Person",
  "name": "Metro Boomin",
  "jobTitle": "Music Producer",
  "url": "https://musicproductionwiki.com/bible/producers/metro-boomin",
  "sameAs": ["https://en.wikipedia.org/wiki/Metro_Boomin"]
}
```
Plus: Article schema, BreadcrumbList, FAQPage (5 questions about their technique)

### Type 5 — Track Anatomy
```json
{
  "@type": "MusicRecording",
  "name": "Billie Jean",
  "byArtist": {"@type": "MusicGroup", "name": "Michael Jackson"},
  "producer": "Quincy Jones",
  "datePublished": "1983"
}
```
Plus: Article schema, BreadcrumbList, HowTo (production technique steps)

### Type 6 — Gear/Plugin Reference
```json
{
  "@type": "Product",
  "name": "Valhalla Room",
  "manufacturer": {"@type": "Organization", "name": "Valhalla DSP"},
  "category": "Audio Plugin",
  "offers": {"@type": "Offer", "price": "50", "priceCurrency": "USD"}
}
```
Plus: Article schema, BreadcrumbList, FAQPage, Review schema

### Type 7 — Genre Bible
```json
{
  "@type": "Article",
  "about": {"@type": "MusicGenre", "name": "Trap"},
  "educationalLevel": "Beginner to Advanced"
}
```
Plus: BreadcrumbList, FAQPage, HowTo (how to make the genre)

## Sitemap Updates Required

After each new content type batch commits:
- Add `/bible/producers/`, `/bible/tracks/`, `/bible/gear/`, `/bible/genres/` paths to sitemap.xml
- Resubmit to Google Search Console
- Priority: Genre Bible entries at 0.9 (highest traffic potential), others at 0.8

## Digital Product Delivery Infrastructure

For PDF digital products ($9–49 price points):
- Option A: Gumroad (0% monthly fee, 10% + $0.50 per transaction) — start here
- Option B: Lemon Squeezy (similar structure, better EU VAT handling)
- Option C: Payhip (free plan, 5% transaction fee)

**Recommendation:** Gumroad for launch — zero upfront cost, immediate setup, handles payment processing and file delivery. Migrate to own infrastructure when volume justifies.

PDF generation workflow:
1. Entry content generated by writer
2. Python script extracts key data (signal chain, settings, gear list)
3. Populates PDF template (Canva or InDesign)
4. PDF hosted on Gumroad, linked from Bible entry
5. Purchase confirmation email delivers download link

Build this workflow as part of Producer DNA writer development (Session 59+).

## Plugin Partnership Program — Technical Infrastructure

For editorial partnerships ($500–2,000/year per developer):
- Dedicated partnership landing page: `/partners/`
- Partner badge CSS class: `.mpb-partner-badge` — amber outline, "Producer's Bible Reference" text
- Partner entries get a `data-partner="true"` attribute on their gear reference entry
- Disclosure block required: "This entry was developed in editorial partnership with [Company]. All technical assessments remain independent."
- Annual renewal — entries updated to current plugin version each year

## Beat Licensing Marketplace — Technical Spec (Future)

URL structure: `/marketplace/beats/[slug]`
Integration: TruClarify clearance API for sample verification
Revenue split: 70% producer / 30% MPW
Payment: Stripe
File delivery: secure download after payment
Metadata required: BPM, key, stems available, exclusive/non-exclusive, license tiers
Build trigger: After TruClarify API is production-ready

---

# SESSION 55 ADDENDUM — TECH — May 22, 2026

## reverb.html — Live Structural Fingerprints (v1.6 gold standard)

| # | Fingerprint | Value |
|---|---|---|
| 1 | mpw-slim-bar | top:0, z:700, height:40px, bg:#181818 |
| 2 | bible-bar | top:40px, z:600, height:50px, bg:#0d0800 |
| 3 | entry-nav | top:90px, z:400 — 25 pill links |
| 4 | bible-entry-wrap | max-width:1100px — 1fr 280px grid on desktop — display:block on mobile |
| 5 | 25 entry-section IDs | canonical order: definition, how-it-works, beginner-trap, parameters, quick-reference, tools, fingerprint, signal-chain, history, decision-framework, how-to-use, decision-tree, genre-table, plugins, before-after, in-the-wild, producer-dna, signatures, types, verdict, mistakes, mix-translation, progression, faq, related |
| 6 | ba-cols class | grid-template-columns:1fr 1fr desktop — collapses to 1fr at 768px — NEVER inline grid |
| 7 | ba-param-row class | grid-template-columns:110px 1fr desktop — collapses to 1fr at 768px — NEVER inline grid |
| 8 | scrollIntoView nav | scroll+touchmove listeners — no IntersectionObserver (obs2 = NEVER) |
| 9 | mtt-wrap | Mix Translation Tool — 5 systems — symptom checklist + diagnosis |
| 10 | atl-svg-wrap | Arrangement Timeline — SVG bar chart — click section for detail |
| 11 | fp-svg | Fingerprint radar chart — 8 genres — 5 axes — filter buttons |
| 12 | cl-grid | 1fr auto 1fr — Contrast Listen two-track comparison |
| 13 | 5 JSON-LD blocks | Article+sameAs, FAQPage, BreadcrumbList, Speakable, HowTo |
| 14 | Version history | Above citation block — v1.x versioning system |
| 15 | Citation block | {{DOI}} placeholder — APA/MLA/Chicago format |
| 16 | Embed block | On every tool — iframe code + Copy Embed button |
| 17 | Beehiiv loader | In `<head>` — form ID a0962c52-4819-4b09-b13d-b26517b76e01 |
| 18 | reading-progress | `display:none` desktop — `display:block` at 768px |
| 19 | overflow-x:clip | On html and body — NOT overflow:hidden |
| 20 | rel="noopener sponsored" | On paid affiliate links ONLY — never on free plugins |

## mpw_tools_v3.py — Current State (Session 55)

File: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_tools_v3.py`
Lines: 1,227 — Size: 80.0KB — Syntax: CLEAN
Tools: 12 — Slug mappings: 49
Branding: CONFIRMED matches reverb.html gold standard (6 gaps fixed Session 55)

**Share bar — gold standard pattern (all tools):**
```html
<div style="display:flex;align-items:center;gap:8px;margin-top:16px;padding-top:12px;border-top:1px solid #1e1e1e;flex-wrap:wrap">
  <span style="font-size:10px;color:#555;flex:1;font-weight:600;letter-spacing:.04em">◆ The Producer's Bible — MusicProductionWiki.com</span>
  <button ...>Copy Link</button>
  <a ... X SVG>Share on X</a>
  <a ... Reddit SVG>Reddit</a>
</div>
<!-- Embed block below -->
<div style="margin-top:16px;padding-top:14px;border-top:1px solid #1e1e1e">
  <div ...>◆ Embed This Tool</div>
  <code>iframe embed code</code>
  <button>Copy Embed</button>
</div>
```

**Brand header — gold standard pattern:**
```html
<div style="background:#0d0800;border-bottom:2px solid #f5a623;padding:12px 20px;display:flex;align-items:center;gap:14px">
  [MPW teal logo SVG]
  <div style="flex:1">
    <div style="font-size:12px;font-weight:800;color:#e8e8e3">MusicProductionWiki.com</div>
    <div style="font-size:10px;color:#f5a623;font-weight:600;letter-spacing:.08em">◆ The Producer's Bible</div>
  </div>
  <span ...>Interactive Tool</span>
  <div style="font-size:11px;font-weight:700;color:#c8c8c3;text-align:right">[TOOL NAME]</div>
</div>
```

## mpw_tools_v4.py — Spec (To Build Session 56)

12 new tools to add. All must match mpw_tools_v3.py branding exactly. Full specs defined in HANDOFF-BIBLE.md tool inventory section.

Priority order:
1. Attack/Release Time Calculator — covers compression, limiting, parallel-compression, multiband, bus-compression, noise-gate, adsr, envelope
2. Vocal Chain Builder — covers compression, eq, saturation, limiting, reverb, delay, gain-staging, send-return, automation
3. EQ Problem Solver (symptom→fix) — covers eq, parametric-eq, shelving-eq, hpf, lpf, air-frequency-eq, resonance
4. Frequency Conflict Detector — covers eq, parametric-eq, gain-staging, mix-bus, stereo-imaging, dynamic-range
5. Saturation/Harmonic Character Reference — covers saturation, distortion, harmonic-distortion, clip-gain, limiting
6. Mix Bus Headroom & Summing Reference — covers mix-bus, bus-compression, headroom, gain-staging, mastering, limiting, lufs
7. Pre-Delay & Reverb Tail Calculator — covers reverb, plate-reverb, room-reverb, convolution-reverb, send-return
8. Stereo Field & Mono Compatibility Checker — covers stereo-imaging, mid-side-processing, bus-compression, chorus, reverb, delay
9. Mastering Signal Chain Reference — covers mastering, limiting, lufs, loudness-normalization, true-peak-limiting, dynamic-range, eq
10. Sidechain/Ducking Frequency Reference — covers compression, parallel-compression, send-return, bus-compression, noise-gate, limiting
11. Synthesis Parameter Reference — covers subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, oscillator, lfo, adsr, envelope, resonance
12. Tempo & Key Finder Reference — covers music-theory (planned), mastering, automation, gain-staging

**NEVER rules for mpw_tools_v4.py:**
| Rule | Detail |
|---|---|
| NEVER use setTimeout for any tool init | Direct calls only — Netlify CSP + DOM readiness confirmed |
| NEVER use innerHTML for card population | createElement/appendChild only — Netlify CSP blocks innerHTML on /bible/* |
| NEVER assign lfoCalc-style functions without window.* | HTML attribute onclick cannot access non-window functions |
| ALWAYS match exact branding from _brand_header() and _share() | No variations — every tool identical header/footer |
| ALWAYS add new slugs to TOOL_OVERRIDES | Every new tool needs complete slug mapping |

## Email Gate — Deferred Architecture (For Future Reference)

When traffic warrants:
- Gate position: Between Quick Reference section and Tools section
- Gate HTML: Beehiiv embed + "Unlock the tools" copy + "Already subscribed" link
- Unlock mechanism: Beehiiv form submit callback → `localStorage.setItem('mpw_unlocked','1')`
- Page load check: if `localStorage.getItem('mpw_unlocked') === '1'` → hide gate, show tools
- Persistence: Indefinite — no expiry ever
- Scope: Single localStorage key works across all Bible entries

## File Structure Updates (Session 55)

```
bible/
  reverb.html (v1.6) — LIVE — gold standard ✅
  chorus.html (v5.2) — LIVE ✅
  [15 other v5.1 entries] — LIVE
  compression.html (v5.1) — LIVE
  [54 v5.1 Session 40 entries] — LIVE
  [153 v3.0/v4.0 entries] — LIVE
  Total: 225 entries
```

## NEVER Rules Added Session 55

| Rule | Detail |
|---|---|
| NEVER write ba-cols or ba-param-row grids as inline styles | Must be CSS class — inline styles override media queries and break mobile |
| NEVER write mix-translation share bar buttons with inline style= | Use mpw-share-btn class only — flex:1 1 0 must come from the class |
| NEVER declare mobile QA done based on desktop DevTools | Only real iPhone confirmation counts — S55 found 2 real bugs DevTools missed |


---

# SESSION 56 UPDATE — TECH — May 22, 2026

## mpw_tools_v4.py — Status

**File:** mpw_tools_v4.py — 84.4KB — 1,310 lines — 47 slugs
**State:** On Steve's machine — REJECTED — do not use

**Technical summary:** All 12 tool builder functions pass syntax check and smoke test. The architecture (TOOL_OVERRIDES router, _wrap() pattern, brand header/share footer) is correct and matches v3. The tools themselves are the problem — they are shallow lookup tables not real calculators. The file can be used as a structural template for the rebuild but the tool body content must be rewritten entirely.

## Tool Architecture — v3 vs v4 Gap Analysis

**v3 build_adsr():**
- Canvas element: 560×185px
- 9 presets load all 4 ADSR values simultaneously
- requestAnimationFrame-free but smooth: canvas redraws on every slider input event
- ADSR shape filled with rgba amber gradient, stroke amber 2.5px
- Section labels A/D/S/R positioned dynamically based on computed x positions
- Contextual tip 50+ chars specific to each preset

**v4 equivalent (Attack/Release Calculator):**
- Two dropdowns + one number input
- Three result boxes showing computed numbers
- Two static progress bars (set to hardcoded width percentages)
- No canvas. No presets that load values. No click-to-copy.

This gap is the core problem. The rebuild must close it.

## NEVER Rules Added Session 56 — Tech

| Rule | Detail |
|---|---|
| NEVER write tool body with static progress bar widths | Bar widths must be computed from inputs — hardcoded percentages are meaningless |
| NEVER use chunk assembly files for Python modules | Assembling tools_1_4.py + tools_5_8.py + tools_9_12.py + router.py is fragile — write the complete file directly |
| NEVER call print() at module level in any mpw_tools file | print("Tools 1-4 OK") executes on import — confirmed during session — use if __name__ == '__main__' guard |

## PowerShell Multi-Line Python — CONFIRMED BROKEN

Session 56 confirmed: PowerShell silently mangles multi-line `python -c "..."` strings with backslash-quote sequences. The symptom is a SyntaxError on a line that looks correct. The fix is always a .py file.

```powershell
# BROKEN — PowerShell corrupts this:
python -c "
html = '<html><body style=\"background:#0d0d0d\">'
"

# CORRECT — always use a .py file:
# 1. Save make_preview.py to mpw-scripts\
# 2. python make_preview.py
```

This has been in the NEVER rules since Session 44. It was violated again in Session 56. It will not be violated again.


---

# SESSION 57/58 UPDATE — TECH — May 22, 2026

## mpw_tools_v4.py — Technical Architecture

**File:** mpw_tools_v4.py
**Size:** 195,294 bytes
**CSS class prefix:** `.t4` (isolated from `.t3` — no conflicts)
**Public API:** `build_tools_section_v4(slug, term)` → HTML string or None

### CSS Architecture

All v4 tools share a single `CSS` constant injected once per tool call. Class prefix `.t4` prevents any clash with v3 `.t3` classes.

Key CSS variables:
- Container: `.t4` — `background:#0d0d0d; border:1.5px solid rgba(245,166,35,.45); border-radius:10px`
- Result box: `.t4 .rb` — dark bg, amber number (`.rn`), gray label (`.rl`)
- Tier card: `.t4 .tc` — clickable, hover amber border, `.hl` for selected state
- Canvas: `.t4 canvas` — `display:block; width:100%; border-radius:6px; border:1px solid #1e1e1e; background:#0a0a0a`
- Mobile: `@media(max-width:600px)` — `.c3,.c4` collapse to 2 columns

### JS Safety Rules Confirmed S57/58

1. **NEVER innerHTML** — Netlify CSP blocks it on `/bible/*` — all DOM manipulation via createElement/appendChild
2. **NEVER setTimeout for init** — call init functions directly at script end
3. **All functions on window** if called from HTML `oninput`/`onclick` attributes
4. **chr(39)** for apostrophes in JS strings within Python f-strings
5. **`'</' + 'script>'`** for closing script tags (SC constant)
6. **No unicode in JS strings** — use `\uXXXX` or ASCII alternatives
7. **No literal newlines in JS string values**

### Canvas Pattern (Used in T1, T4, T5, T6)

All canvases use `devicePixelRatio` for retina sharpness:
```javascript
var dpr = window.devicePixelRatio || 1;
var W = canvas.offsetWidth || 560;
canvas.width = W * dpr;
canvas.height = H * dpr;
var ctx = canvas.getContext('2d');
ctx.scale(dpr, dpr);
```

All canvas functions are called on `window.addEventListener('resize', ...)` for responsive behavior.

### SVG Pattern (Used in T3, T4)

All SVGs use `createElementNS` — never innerHTML:
```javascript
var NS = 'http://www.w3.org/2000/svg';
var el = document.createElementNS(NS, 'rect');
el.setAttribute('x', x);
el.setAttribute('fill', col);
svg.appendChild(el);
```

### Delivery Method — Two-Part Base64 PS1

mpw_tools_v4.py is 195,294 bytes (260,392 chars base64). Single PS1 would be 255KB — over Cloudflare limit. Split into two parts:

- `deliver_v4_part1.ps1` — 127.4KB — writes base64 Part 1 to `%TEMP%\mpw_v4_b64_part1.txt`
- `deliver_v4_part2.ps1` — 127.9KB — reads Part 1 from temp, concatenates Part 2, writes final binary via `[System.IO.File]::WriteAllBytes()`

Both files saved via Notepad → Save As → All Files to bypass Cloudflare.

## NEVER Rules Added Session 57/58 — Tech

| Rule | Detail |
|---|---|
| NEVER use innerHTML in Bible tool JS | Netlify CSP `/bible/*` blocks it — all DOM via createElement/appendChild |
| NEVER use Python escape sequences for unicode in JS strings inside f-strings | `\\u25b2` renders as actual unicode char in f-string output — use ASCII alternatives or HTML entities |
| NEVER omit devicePixelRatio scaling on canvas elements | Retina displays show blurry canvas without DPR scaling — always scale by `window.devicePixelRatio||1` |
| NEVER put tool preview HTML inside zip for Cloudflare delivery | Cloudflare intercepts — use separate file opens or base64 PS1 delivery |


---

# SESSION 59 UPDATE — TECH — May 22, 2026

## mpw_tools_v4_append.py — Technical Architecture

**File:** mpw_tools_v4_append.py
**Size:** 109,607 bytes
**Content:** SC constant + 6 build functions (T7-T12) — NO helpers, NO dispatcher
**Requires:** `_wrap`, `_share`, `_plug`, `SC` from existing mpw_tools_v4.py scope
**Public functions:** `build_predelay`, `build_stereo_field`, `build_mastering_chain`, `build_sidechain`, `build_synthesis`, `build_tempo_key`

### Mobile CSS — MPW_TOOLS_V4_CSS

New constant exported from `mpw_tools_v4_append.py`. Bible writer injects once per page into `<style>` block. Never inject per-tool — one injection per page.

```css
.t4-plug{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:16px;padding-top:14px;border-top:1px solid #1e1e1e}
.t4-plug-card{background:#0a0a0a;border:1px solid #1e1e1e;border-radius:6px;padding:10px;display:flex;flex-direction:column}
.t4-plug-card.amber{background:#100c00;border-color:rgba(245,166,35,.2)}
.t4-plug-lbl{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.t4-plug-txt{font-size:11px;color:#999;line-height:1.65;flex:1}
.t4-plug-card.amber .t4-plug-txt{color:#c8a060}
.t4-share{display:flex;align-items:center;gap:8px;margin-top:16px;padding-top:12px;border-top:1px solid #1e1e1e;flex-wrap:wrap}
.t4-share-lbl{font-size:10px;color:#555;font-weight:600;letter-spacing:.04em;flex:1;min-width:160px}
.t4-share-btns{display:flex;gap:6px;flex-wrap:wrap}
.t4-cv{display:block;width:100%;border-radius:6px;background:#080810}
.t4-sliders{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:12px}
.t4-chord-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:12px}
.t4-cof-wrap{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
.t4-hdr-title{font-size:14px;font-weight:800;color:#f5a623;text-align:right;letter-spacing:.01em;max-width:180px}
@media(max-width:600px){
  .t4-plug{grid-template-columns:1fr 1fr}
  .t4-sliders{grid-template-columns:1fr}
  .t4-chord-grid{grid-template-columns:repeat(4,1fr)}
  .t4-cof-wrap{grid-template-columns:1fr}
  .t4-hdr-title{font-size:11px;max-width:120px}
  .t4-share-lbl{flex:unset;width:100%}
}
```

### Canvas Pattern — T7-T12 (Updated from T1-T6)

T7-T12 use a different canvas sizing pattern from T1-T6. Key difference: `offsetWidth` read at draw time (not at init), `ResizeObserver` for live reflow. No `devicePixelRatio` scaling (intentional — simpler, sufficient for these visualisations).

```javascript
function draw() {
  var cv = document.getElementById('cv-id');
  if (!cv) return;
  var cw = cv.offsetWidth || 640;  // fallback to 640 if hidden or pre-layout
  cv.width = cw;
  cv.height = H;  // fixed height
  var ctx = cv.getContext('2d');
  // ... draw at cw x H pixels
}

// ResizeObserver for responsive reflow
if (window.ResizeObserver) {
  var ro = new ResizeObserver(function() { draw(); });
  var container = document.getElementById('container-id');  // parent element, always visible
  if (container) ro.observe(container);
}
```

**CRITICAL:** Never observe a canvas that may be inside `display:none`. Always observe a parent container that is always visible. The ResizeObserver callback must guard against hidden modes (e.g. T11 checks `_syMode` before deciding which canvas to redraw).

### T11 Synthesis — Three-Mode Architecture

Three modes toggled by `syMode(m)`:
- `sub` — Subtractive: waveform canvas + filter frequency response canvas + ADSR envelope canvas
- `fm` — FM Synthesis: Bessel-function waveform canvas from FM formula
- `target` — Sound Target Finder: 8 classic sounds with exact parameters, all click-to-copy

Mode switching: `display:none` / `display:block` on `#sy-sub`, `#sy-fm`, `#sy-tgt` divs.

ResizeObserver watches `#sy-sub` container (always visible on sub mode). Callback checks `_syMode` before drawing — only draws canvases for the active mode to prevent 0-width draws on hidden canvases.

### T12 Circle of Fifths — Touch Support

Click and touch both handled:

```javascript
document.getElementById('tk-cof').addEventListener('click', tkCofClick);
document.getElementById('tk-cof').addEventListener('touchend', function(e) {
  e.preventDefault();  // prevents ghost click
  tkCofClick(e);
});

function tkCofClick(ev) {
  var ex = ev.touches ? ev.touches[0].clientX : ev.clientX;
  var ey = ev.touches ? ev.touches[0].clientY : ev.clientY;
  // ... hit test against circle segments
}
```

ResizeObserver watches CoF canvas parent node (always visible). Canvas redraws as `offsetWidth` changes — circle always fills available width and height equals width (square canvas, circular border-radius).

### T9 Mastering Chain — Touch + Hover

Stage buttons use both `onmouseenter` (desktop hover) and `ontouchstart` (mobile tap) to show the panel. Previously hover-only — broke entirely on touch devices.

```html
<button onmouseenter="mcBuildPanel('hpf')" ontouchstart="mcBuildPanel('hpf')" onclick="mcCheck('hpf',this)">
```

Panel instruction copy updated from "Hover a stage above" to "Tap a stage above to see settings" — mobile-first language.

### Delivery Pattern — Parts 3 and 4

mpw_tools_v4_append.py is 109,607 bytes (146,144 chars base64). Each PS1 is ~72KB — well under Cloudflare 200KB limit.

- `deliver_v4_part3.ps1` — 71.7KB — writes base64 Part 1 to `%TEMP%\mpw_v4_b64_t712.txt`
- `deliver_v4_part4.ps1` — 71.9KB — reads Part 1 + Part 2, assembles, writes `mpw_tools_v4_append.py` to SRCDIR

After delivery, append content manually into `mpw_tools_v4.py` and add `TOOL_OVERRIDES_V4.update({...})` block.

---

## Competitive Research — AI Mix Tools (Session 59)

Researched for MixMentor product roadmap. Summary of live competitors:

| Tool | Tracks processed | Strengths | Gaps |
|------|-----------------|-----------|------|
| RoEx Mix Check Studio | 5M+ | Free, genre selection, established | Generic feedback, no parameter values, no reference anchoring |
| TrackScore.ai | Unknown | EDM-specific, 9 subgenres, genre scoring | EDM only, "hit potential" score distrusted by pros |
| Slapback.io | Unknown | Timestamped notes, AI personas, collaboration | Uses OpenAI/Google (not proprietary), no audio model |
| mixanalytic.com | Unknown | Freemium, multiple modules, Claude Premium tier | Credits model, no reference anchoring |
| LANDR | Millions | Auto-mastering, distribution | Applies processing, doesn't diagnose |

**The gap nobody has filled:** Reference-anchored delta analysis (your track vs a reference YOU choose), parameter-level feedback (exact dB/Hz/Q values), iterative re-analysis (before/after delta), stem-level problem identification, arrangement density analysis.

---

## MixMentor — Technical Architecture (Planned)

### Frontend Stack
- Pure HTML/CSS/JS — consistent with MPW stack
- Web Audio API for client-side FFT preview (fast, no upload needed for initial display)
- File upload → base64 or FormData → RunPod endpoint
- Claude API for feedback generation from feature JSON

### RunPod Pod Spec
- **Runtime:** Python 3.11 + CUDA (for demucs stem separation)
- **Libraries:** `essentia`, `librosa`, `pyloudnorm`, `aubio`, `demucs`, `numpy`, `scipy`
- **Endpoint:** Serverless function — POST audio file → JSON feature blob
- **Analysis modules:**
  - Perceptual loudness (LUFS integrated, short-term, true peak)
  - Spectral balance (7-band energy profile)
  - Dynamic range (crest factor, DR score)
  - Stereo field (correlation, mid/side energy, width)
  - Transient detection (attack times, peak density)
  - Key + tempo detection
  - Arrangement density (energy over time in 4-bar windows)
- **Processing time:** ~3-8 seconds per stereo bounce, ~15-30 seconds with demucs stem separation

### Claude API Integration
- Model: claude-sonnet-4-6 (fast, sufficient for structured feedback)
- Input: feature JSON + genre selection + reference feature JSON (if uploaded)
- Output: structured feedback JSON with priority-ranked fix list, each item containing:
  - Description (plain producer language)
  - Severity (1-10)
  - Exact parameter recommendation (e.g. "Cut 3.5dB at 340Hz, Q 1.2")
  - Which track or bus to apply it to
  - Before/after expectation
- System prompt: trained on mix engineering principles, genre-specific targets, producer vocabulary

### Genre Reference Database
50+ profiles to build (vs 9 at TrackScore):
- Electronic: House, Techno, Trance, DnB, Dubstep, Trap, Future Bass, Lo-Fi, Hyperpop, Ambient
- Hip-Hop: Boom Bap, Drill (UK/US), Mumble Rap, Conscious, Chopped & Screwed
- Pop: Mainstream Pop, Bedroom Pop, Synth-Pop, Dark Pop, K-Pop
- Rock: Indie Rock, Metal, Post-Rock, Punk, Shoegaze
- R&B/Soul: Contemporary R&B, Neo-Soul, Afrobeats, Reggaeton
- Country, Jazz, Classical, Acoustic, Singer-Songwriter

Each profile: median frequency balance (7 bands), LUFS target, DR target, stereo width target, transient density target — derived from 50-200 reference tracks per genre.

### Zero-Storage Architecture
- Audio never written to disk beyond processing duration
- Feature JSON retained (no audio content — safe for unreleased tracks)
- Reference track features cached by track fingerprint (avoid re-processing same reference)
- GDPR-compliant by design

---

## NEVER Rules Added — Session 59 Tech

| Rule | Detail |
|------|--------|
| NEVER use ResizeObserver with `\|\|document.body` fallback | Causes "Script error" on mobile Safari before DOM settles — always observe a named parent container |
| NEVER call canvas draw when canvas is inside `display:none` | `offsetWidth` returns 0; draw functions must check active mode before executing |
| NEVER use `onmouseenter` alone on interactive elements | Touch devices cannot hover — always pair with `ontouchstart` |
| NEVER write tool preview HTML for branding review without real iPhone test | Desktop DevTools misses ResizeObserver and canvas scale failures that appear on real device |
| NEVER inject MPW_TOOLS_V4_CSS once per tool | Inject once per page in the `<style>` block — multiple injections cause class conflicts |


---

## Mobile Optimisation — Technical Spec for All Tools (Session 59 Mandate)

Steve confirmed: all 25 tools must be fully mobile-optimised before any tool is considered production-ready. This section documents the exact technical fixes required for v3 (12 tools) and v4 T1-T6 (6 tools). T7-T12 were already fixed in Session 59.

### Canvas Sizing — Universal Fix Pattern

Every canvas in every tool must use this pattern. No exceptions.

```javascript
function drawSomething() {
  var cv = document.getElementById('canvas-id');
  if (!cv) return;
  var cw = cv.offsetWidth;
  if (!cw) cw = 640;  // fallback if hidden or pre-layout — never 0
  cv.width = cw;
  cv.height = FIXED_HEIGHT;  // height is always fixed, width is responsive
  var ctx = cv.getContext('2d');
  // all drawing at cw x FIXED_HEIGHT pixels
}
```

**NOT this (v3/v4 T1-T6 current pattern):**
```javascript
// WRONG — uses hardcoded attribute width, canvas never resizes
<canvas width="640" height="200">
// WRONG — reads width at init, not at draw time
var W = canvas.offsetWidth || 640;
canvas.width = W;
// ... init only, never redraws on resize
```

### ResizeObserver — Universal Add Pattern

Add to every tool's script block, after all draw functions are defined:

```javascript
// Observe a VISIBLE parent container, not the canvas itself
// Never observe: canvas that may be in display:none, document.body
if (window.ResizeObserver) {
  var _ro = new ResizeObserver(function() {
    drawSomething();  // call all draw functions for this tool
  });
  // Observe the tool's outer container — always visible, always has width
  var _container = document.getElementById('tool-outer-container-id');
  if (_container) _ro.observe(_container);
}
```

**For tools with multiple canvases in multiple display modes (e.g. T11):**
```javascript
if (window.ResizeObserver) {
  var _ro = new ResizeObserver(function() {
    // Only draw canvases that are currently visible
    if (currentMode === 'sub') { drawSub(); drawFilt(); drawAdsr(); }
    else if (currentMode === 'fm') { drawFm(); }
    // target mode has no canvas
  });
  var _container = document.getElementById('mode-container');
  if (_container) _ro.observe(_container);
}
```

### Touch Events — Universal Fix Pattern

Any interactive element that currently uses `onmouseover`, `onmouseenter`, or `onmouseleave` must also have a touch equivalent. Pattern:

```html
<!-- Desktop hover + mobile touch — both trigger the same handler -->
<button
  onmouseenter="showPanel(this)"
  ontouchstart="showPanel(this)"
  onclick="toggleCheck(this)">
  Stage Name
</button>
```

For complex hover panels (T3 EQ spectrum tooltip, T9 mastering stages):
- Desktop: hover shows panel, mouse leave hides it
- Mobile: tap shows panel, tap same button again hides it (toggle)
- Implementation: add a `_panelOpen` flag; `ontouchstart` checks flag and toggles

```javascript
var _panelOpen = false;
function showPanel(id) {
  if (_panelOpen && _currentPanel === id) {
    hidePanel(); _panelOpen = false;
  } else {
    renderPanel(id); _panelOpen = true; _currentPanel = id;
  }
}
```

### Responsive Grid — CSS Class Requirements

All multi-column grids in all tools must use CSS classes, never inline `display:grid` with fixed column counts. The breakpoint rules must live in the tool's `<style>` block.

**v3 tools — new classes to add:**
```css
/* Add to v3 tool style blocks */
.t3-grid2 { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.t3-grid3 { display:grid; grid-template-columns:repeat(3,1fr); gap:8px; }
.t3-grid4 { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; }
.t3-plug  { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-top:14px; }
@media(max-width:600px) {
  .t3-grid3, .t3-grid4 { grid-template-columns:1fr 1fr; }
  .t3-plug { grid-template-columns:1fr 1fr; }
  .t3-grid2 { grid-template-columns:1fr; }  /* inputs stack 1-col */
}
```

**v4 T1-T6 — existing inline grids to convert to classes:**
- T1: compressor character 4-col grid — convert to `.t4-char-grid` class
- T2: step card grid — convert to `.t4-step-grid` class
- T3: symptom 4-col grid — convert to `.t4-symptom-grid` class
- T6: mastering stage row — convert to `.t4-stage-row` class

### Tap Target Minimum Size

All buttons, toggle pills, preset buttons, and clickable elements must have:
```css
min-height: 44px;   /* iOS HIG minimum tap target */
padding: 10px 12px; /* ensures content doesn't shrink below 44px */
touch-action: manipulation; /* prevents 300ms delay on iOS */
```

For pill/badge style buttons that are shorter by design (10px font, 6px padding):
```css
@media(max-width:600px) {
  .pill-btn { padding: 10px 12px; font-size: 12px; }
}
```

### iOS Safari `navigator.clipboard` — Compatibility

`navigator.clipboard.writeText()` works on iOS Safari 13.4+ when the page is served over HTTPS. MPW is always HTTPS via Netlify — this is fine. No polyfill needed. The existing pattern is correct:
```javascript
navigator.clipboard && navigator.clipboard.writeText(value);
```

The `&&` guard is sufficient. Never use `document.execCommand('copy')` as fallback — it's deprecated.

### Mobile Audit Script — `mpw_tools_mobile_audit.py`

To be built next session. Script generates a single `tool_mobile_preview.html` containing all tools in one scrollable page, with a `<meta viewport>` tag, outputting to `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tool_mobile_preview.html`. Steve opens this URL in Safari on iPhone using local file sharing or a temporary ngrok tunnel.

```python
# mpw_tools_mobile_audit.py
# Generates mobile preview of all 24 tools
# Output: tool_mobile_preview.html in SRCDIR
import sys
SRCDIR = r'C:\Users\swarn\OneDrive\Desktop\mpw-scripts'
sys.path.insert(0, SRCDIR)

from mpw_tools_v3 import build_tools_section_v3
from mpw_tools_v4 import build_tools_section_v4
# from mpw_tools_v4_append import build_predelay, build_stereo_field, ...

ALL_TOOLS = [
    # v3
    ('compression', 'Compression'),
    ('eq', 'EQ'),
    ('limiting', 'Limiting'),
    ('reverb', 'Reverb'),
    ('delay', 'Delay'),
    ('adsr', 'ADSR'),
    ('gain-staging', 'Gain Staging'),
    ('headroom', 'Headroom'),
    ('stereo-imaging', 'Stereo Imaging'),
    ('lfo', 'LFO'),
    # v4 T1-T6
    # v4 T7-T12
]
# ... generate preview page with viewport meta ...
```

### Mobile Status Tracking Table — All 24 Tools

Add this to the session start readout from `mpw_session_start.py` in a future update:

| Tool | File | Mobile status | Last tested |
|------|------|--------------|-------------|
| GR Calculator | v3 | ❌ Not audited | Never |
| Delay Time Calculator | v3 | ❌ Not audited | Never |
| LUFS Target Reference | v3 | ❌ Not audited | Never |
| Frequency Band Reference | v3 | ❌ Not audited | Never |
| RT60 Calculator | v3 | ❌ Not audited | Never |
| Note→Frequency | v3 | ❌ Not audited | Never |
| ADSR Visualizer | v3 | ❌ Not audited | Never |
| Gain Staging Reference | v3 | ❌ Not audited | Never |
| Headroom Calculator | v3 | ❌ Not audited | Never |
| Stereo Width & M/S | v3 | ❌ Not audited | Never |
| LFO Rate Sync | v3 | ❌ Not audited | Never |
| Chord & Key Reference | v3 | ❌ Not audited | Never (superseded by T12) |
| T1 Attack/Release | v4 | ❌ Not audited | Never |
| T2 Vocal Chain | v4 | ❌ Not audited | Never |
| T3 EQ Problem Solver | v4 | ❌ Not audited | Never |
| T4 Freq Conflict Detector | v4 | ❌ Not audited | Never |
| T5 Saturation Reference | v4 | ❌ Not audited | Never |
| T6 Mix Bus Headroom | v4 | ❌ Not audited | Never |
| T7 Pre-Delay & Reverb Tail | v4-append | ✅ Audited | Session 59 |
| T8 Stereo Field & Mono | v4-append | ✅ Audited | Session 59 |
| T9 Mastering Signal Chain | v4-append | ✅ Audited | Session 59 |
| T10 Sidechain & Ducking | v4-append | ✅ Audited | Session 59 |
| T11 Synthesis Reference | v4-append | ✅ Audited | Session 59 |
| T12 Tempo, Key & Chord | v4-append | ✅ Audited | Session 59 |
| Tool 25 | TBD | ❌ Not confirmed | — |

### NEVER Rules — Mobile Optimisation (Session 59)

| Rule | Detail |
|------|--------|
| NEVER declare a tool mobile-ready without testing on a real iPhone | DevTools emulation misses ResizeObserver timing, canvas scale, and iOS Safari clipboard bugs |
| NEVER hardcode canvas `width` attribute to a fixed pixel value | Always read `cv.offsetWidth` at draw time — fixed attribute width overrides CSS width:100% |
| NEVER use `onmouseenter` or `onmouseover` alone on interactive elements | Touch devices cannot hover — always pair with `ontouchstart` |
| NEVER put grid column counts in inline styles on tool elements | Inline styles override media queries — all grid layouts must use CSS classes |
| NEVER observe `document.body` in ResizeObserver | Fires before layout settles — observe the tool's named parent container |
| NEVER build mobile fixes without testing the fix on a real iPhone | Fix may work in DevTools but fail on iOS Safari — always verify on device |


---

# SESSION 60 UPDATE — TECH — May 23, 2026

## File Structure — Updated

```
repo root/
├── index.html
├── articles/          (526 articles)
├── bible/             (223 entries)
├── tools/             ← NEW — top-level directory — DECIDED Session 60
│   ├── index.html     ← hub page — 8 categories, search/filter — BUILD Session 61
│   └── [slug].html    ← 36 standalone tool pages — BUILD Session 61
├── css/style.css
├── js/main.js
├── js/mpw-analytics.js
└── [handoff files]
```

Asset paths in `/tools/`: `../css/style.css`, `../js/main.js` — identical to `/bible/` pattern.

## New Python Files — Tool Infrastructure (All in mpw-scripts\)

| File | Status | Purpose |
|------|--------|---------|
| `mpw_tools_v5a.py` | ✅ DELIVERED — PASS 8/8 | Tools 1–8 — v3 rebuilds |
| `mpw_tools_v5b.py` | ✅ DELIVERED — PASS 8/8 | Tools 9–16 — v3 rebuilds + 4 new |
| `mpw_tools_v5c.py` | ✅ DELIVERED — PASS 8/8 | Tools 17–24 — 8 new tools |
| `mpw_tools_v5_dispatch.py` | ✅ DELIVERED — PASS | Unified dispatcher — 145 slugs |
| `fix_v3_mobile.py` | ✅ CONFIRMED PASS | v3 canvas mobile fix — Steve confirmed 7/7 |
| `patch_canvas_mobile.py` | ✅ READY — run after iPhone preview | Patches 3 live Bible entries |
| `mpw_affiliates.py` | ⏳ BUILD Session 61 | Affiliate link registry |
| `mpw_tool_manifest.py` | ⏳ BUILD Session 61 | Master tool record — source of truth |
| `generate_tool_pages.py` | ⏳ BUILD Session 61 | Generates 36 standalone tool pages |
| `generate_tools_hub.py` | ⏳ BUILD Session 61 | Generates /tools/index.html |

## Tool Dispatch Architecture — v5

```python
# Import pattern for mpw_bible_writer.py integration
from mpw_tools_v5_dispatch import build_tools_section_v5 as build_tools_section_v3, TOOL_OVERRIDES_V5 as TOOL_OVERRIDES
```

The dispatcher routes 145 slugs across 3 batch files. All TOOL_OVERRIDES_V5A, V5B, V5C are merged. Later dicts override earlier on collision (C > B > A).

## V5 Canvas Standard — LOCKED

All canvas tools in all v5 files follow this pattern exactly:

**HTML element:**
```html
<canvas id="CVID" style="width:100%;height:Xpx;display:block;margin-bottom:10px"></canvas>
```
No `width=` or `height=` attributes on the element.

**Draw function:**
```javascript
var cv = document.getElementById('CVID');
var dpr = window.devicePixelRatio || 1;
var W = cv.offsetWidth || 560; var H = HEIGHT_PX;
cv.width = W * dpr; cv.height = H * dpr;
var ctx = cv.getContext('2d'); ctx.scale(dpr, dpr);
```

**ResizeObserver:**
```javascript
if (window.ResizeObserver) {
  var _ro = new ResizeObserver(function() { draw(); });
  var _cv = document.getElementById('CVID');
  if (_cv) _ro.observe(_cv.parentElement || _cv);
}
```

## V5 Mobile Standard

- Grid collapse breakpoint: **480px** (not 600px — v3 was 600px, v5 corrects to 480px)
- Touch targets: minimum 44px height on all interactive elements
- No hardcoded widths on any container
- `navigator.clipboard` guard: `navigator.clipboard && navigator.clipboard.writeText(value)` — HTTPS only, iOS Safari 13.4+ safe

## Mobile Status — Updated Session 60

| File | Tools | Mobile Status |
|------|-------|---------------|
| `mpw_tools_v3.py` | 12 | ⚠️ Canvas fix applied locally (fix_v3_mobile.py) — 3 live entries pending patch |
| `mpw_tools_v4.py` | T1-T6 | ❌ Not audited — innerHTML CSP issue blocks /bible/* |
| `mpw_tools_v4_append.py` | T7-T12 | ✅ Audited Session 59 |
| `mpw_tools_v5a.py` | Tools 1–8 | ✅ Canvas standard applied — 480px breakpoint |
| `mpw_tools_v5b.py` | Tools 9–16 | ✅ Canvas standard applied — 480px breakpoint |
| `mpw_tools_v5c.py` | Tools 17–24 | ✅ Canvas standard applied — 480px breakpoint |

## V4 T1-T6 innerHTML CSP Issue — Unresolved

v4 T1-T6 tools use `innerHTML` in rendering functions (`arRenderPresets()`, `arRenderFamous()`, `arRenderChars()`, `arRenderPlugins()`, `vcBuild()`, `vcRenderFamous()`). Netlify CSP blocks `innerHTML` on `/bible/*` pages. Fix: replace all `el.innerHTML = ''` + string concatenation with `createElement/appendChild` pattern. **Not yet fixed — blocked pending v5 dispatch integration.**

## TOOL_OVERRIDES_V5 — Complete 145-Slug Map

The full slug map lives in `mpw_tools_v5_dispatch.py`. Summary by tool:

**v5a slugs (Tools 1–8):** compression, saturation, distortion, parallel-compression, multiband-compression, noise-gate, bus-compression, dynamic-range, limiting, gain-reduction, delay, plate-reverb, automation, slapback, ping-pong-delay, lufs, mastering, loudness-normalization, true-peak-limiting, streaming-mastering, eq, parametric-eq, high-pass-filter, low-pass-filter, shelving-eq, air-frequency-eq, resonance, harmonic-distortion, air, eq-frequency, frequency-masking, reverb, convolution-reverb, room-reverb, acoustic-treatment, room-acoustics, oscillator, fm-synthesis, wavetable-synthesis, additive-synthesis, vocoder, subtractive-synthesis, note-frequency, midi, tuning, adsr, envelope, envelope-generator, synth-basics, amplitude-envelope, gain-staging, send-return, clip-gain, signal-flow, headroom, mix-bus

**v5b slugs (Tools 9–16):** headroom, mix-bus, true-peak, mastering-delivery, audio-delivery, stereo-imaging, mid-side-processing, stereo-width, mono-compatibility, m-s-eq, lfo, chorus, flanger, phaser, tremolo, vibrato, modulation, chord, key, scale, music-theory, chord-progression, circle-of-fifths, modes, 808-bass, sub-bass, trap-production, bass-design, 808, bass-layering, arrangement, song-structure, intro, verse, chorus, bridge, drop, build-up, outro, saturation, harmonic-distortion, tape-saturation, tube-saturation, distortion, overdrive, clipping, analog-warmth, parallel-compression, parallel-processing, new-york-compression, drum-bus, bus-compression

**v5c slugs (Tools 17–24):** transient-shaper, transient-design, transient, punch, attack-design, sample-rate, bit-depth, digital-audio, recording-settings, dither, aliasing, nyquist, oversampling, sidechain, sidechain-compression, ducking, pumping, kick-sidechain, voiceover-ducking, pitch-correction, auto-tune, melodyne, vocal-tuning, vibrato, intonation, pitch-shifting, reverb, plate-reverb, hall-reverb, room-reverb, spring-reverb, convolution-reverb, algorithmic-reverb, shimmer-reverb, gated-reverb, synthesis, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, granular-synthesis, sound-design, synthesizer, mix-bus-processing, master-bus, mastering-chain, bus-processing, stem-mastering, mix-bus-compression, mastering-delivery, streaming-delivery, audio-delivery, mixing-checklist, stem-export, pre-release-checklist, sync-delivery

**NOTE:** Some slugs appear in multiple batches (e.g. 'saturation', 'reverb'). The dispatcher resolves collisions: C > B > A priority order.

## Sitemap — Pending Updates Session 61

After generating all tool pages, add to sitemap.xml:
- `/tools/` hub page — priority 0.9, changefreq monthly
- All 36 `/tools/[slug].html` pages — priority 0.8, changefreq monthly
- Total new URLs: 37

Submit to Google Search Console after sitemap update.



---

# SESSION 62 UPDATE — TECH — May 24, 2026

## File Structure — Updated

```
repo root/
├── bible-index.json     ← 222 entries (rebuilt Session 62)
├── bible/
│   ├── index.html       ← cat bar fixed (no duplicates) — SHA 72e881c7 — nav system still .mpw-site-nav / .bcb-link (NOT yet reverb.html slim-bar)
│   ├── reverb.html      ← gold standard — unchanged
│   ├── [222 entries]    ← mobile-drawer still in place — bmn-drawer PENDING
│   └── categories/
│       ├── dynamics/    ← ✅ reverb.html nav — A-Z threshold 50 — no subcat pills
│       ├── frequency/   ← ✅ reverb.html nav
│       ├── time-based/  ← ✅ reverb.html nav
│       ├── signal-processing/ ← ✅ reverb.html nav
│       ├── mixing/      ← ✅ reverb.html nav
│       ├── mastering/   ← ✅ reverb.html nav
│       ├── synthesis/   ← ✅ reverb.html nav
│       ├── music-theory/ ← ✅ reverb.html nav
│       ├── production/  ← ✅ reverb.html nav
│       ├── recording/   ← ✅ reverb.html nav
│       └── tools/       ← ✅ reverb.html nav — new copy — tagline — why block — request link
└── tools/
    ├── gain-reduction-calculator.html     ← ✅ live — real dispatch content
    ├── parallel-processing-calculator.html ← ✅ live
    ├── [34 more tool pages]               ← ✅ all 36 live
    └── index.html                         ← ❌ NOT YET BUILT
```

---

## Tool Pages Architecture — `/tools/[slug].html`

### CSS Path
Absolute: `/css/style.css` — NEVER use `../css/style.css` from `/tools/` depth.

### Nav
Tool pages use `generate_tool_pages_v2.py` SITE_HEADER which includes:
- `.mpw-slim-bar` (36px, faint logo, Articles/Gear/About/Tools links, search, Sound Better CTA)
- `.bible-bar` (amber border, diamond + The Producer's Bible, 11 category pills)
- `.bmn-drawer` (grid, all 11 Bible categories + Articles section)
- Search overlay JS

All nav CSS is defined **inline in TOOL_PAGE_CSS** — not from style.css. This is mandatory because the nav CSS classes are not reliably defined in style.css at the `/tools/` path depth.

### Content
Tool HTML comes from `mpw_tools_v5_dispatch.py` via `build_tools_section_v5(bible_key, name)`. The `<h2>Tools for This Entry</h2>` heading is stripped from dispatch output — it is redundant on standalone tool pages.

### Slug Override
`transient-shaper-reference` maps to `transient-shaping` in dispatch via: `_overrides = {"transient-shaping": "transient-shaper"}` in `generate_tool_pages_v2.py`.

### Footer
`make_footer()` generates inline-styled footer — `.site-footer` CSS is defined in `TOOL_PAGE_CSS`. Footer includes share buttons (X, Reddit) and amber nav links.

### Removed Elements
- `<div class="bible-mobile-bar" aria-hidden="true">The Producer's Bible</div>` — was rendering as raw white text top-left — removed from SITE_HEADER entirely.

---

## Category Pages Architecture — `/bible/categories/[slug]/index.html`

Generated by `mpw_bible_cat_pages.py`. Key architectural decisions confirmed Session 62:

| Decision | Detail |
|----------|--------|
| A-Z letter index | Only shown when category has ≥ 50 entries |
| Subcat filter pills | Tools page only — content pages had no subcategory tags on entries so pills were misleading |
| Hero max-width | 1100px — gives proper breathing room at 1440px+ |
| Hero desc | Empty string for Tools page — tagline + why block replace it |
| Tools page copy | H1: "The Producer's Tools" — tagline: "Built for the session. Not the syllabus." — see below |
| Mobile grid | Single column at 768px breakpoint |
| Empty letter headers | JS hides letter header rows with no visible entries after filter applied |

### The Producer's Tools Page — Approved Copy

**Tagline (italic amber under H1):** Built for the session. Not the syllabus.

**Hero lede:** Most audio tools are designed for someone learning the fundamentals. These are designed for someone who already knows them — and just needs the answer, right now.

**Pull quote (amber left border):** Every calculator here came from a real gap. A delay calculator that made you do the BPM math yourself. A loudness reference buried in a spec sheet. A compression guide that explained theory when you just needed the ratio. We built the tools we kept wishing existed.

**Why block (◆ On what we build):** We're not running a tool factory. Every tool here went through the same question: would a working producer actually open this mid-session? If the answer was anything other than yes, we didn't build it. These aren't demos. They aren't lead magnets. They're reference tools — the kind that stay open in a tab while you work.

**Request block:** Got a gap we haven't filled yet? Send us the tool you wish existed → team@musicproductionwiki.com. We read every request. The good ones get built.

**Stats:** 36 tools live · Free to use · More in development

---

## bible/index.html — Nav System State

The bible/index.html uses a **different nav system** from reverb.html and category pages:
- Nav: `.mpw-site-nav` with dropdown menus (Articles, Gear, About)
- Category bar: `.bible-cat-bar` / `.bcb-link` (horizontal scrollable bar)
- Mobile: `.mobile-drawer` with `id="mobileDrawer"`

This is intentionally different from the slim-bar/bible-bar system. The question of whether to replace it with the reverb.html slim-bar system was raised but **not executed** — must be discussed with Steve before any nav changes to bible/index.html.

The cat bar duplicate link bug (Production/Recording/Tools appearing twice) was fixed — SHA `72e881c7`.

---

## Pending Nav Work

| Page/System | State | Action Needed |
|-------------|-------|---------------|
| bible/index.html nav | `.mpw-site-nav` system — different from reverb | Discuss with Steve before touching |
| 222 Bible entries | old `mobile-drawer` still in place | Safe batch per Session 61 rules — discuss approach first |
| Tool page breadcrumbs | `/tools/` and `/tools/#dynamics-compression` both 404 | Needs tools hub page first |

---

## NEVER Rules Added — Session 62 — Tech

| Rule | Detail |
|------|--------|
| NEVER use `../css/style.css` on pages in `/tools/` | Absolute `/css/style.css` required |
| NEVER build SITE_HEADER without confirming all CSS classes are defined inline | Nav rendered as unstyled bullet text — classes existed in HTML but not in CSS |
| NEVER include `<div class="bible-mobile-bar">` in any page template | Renders as raw white text — remove from all generators |
| NEVER declare tool pages live without visual confirmation of rendered content | Placeholder block was committed and declared working — it was not |
| NEVER change bible/index.html nav without discussing with Steve first | The index uses a different nav architecture — changes need deliberate approval |
| NEVER execute subcat pill removal or other UI component changes without asking Steve | Discuss before executing on any component that affects user-facing layout |

---

# SESSION 63 UPDATE — TECH — May 24, 2026

## Category Pages Architecture — Final State

### File Structure Update

```
bible/
├── index.html           ← REBUILT S62/S63 — slim-bar/bible-bar/bmn-drawer — Beehiiv wired — SHA 7bfb2b6b
├── reverb.html          ← gold standard — read time patched 33→25min — SHA 8b6dd26d
├── [222 entries]        ← mobile-drawer still in place — bmn-drawer patch PENDING
└── categories/
    ├── dynamics/        ← regenerated S63 from mpw_bible_cat_pages_s63f.py ✅
    ├── frequency/       ← regenerated S63 ✅
    ├── time-based/      ← regenerated S63 ✅
    ├── signal-processing/ ← regenerated S63 ✅
    ├── mixing/          ← regenerated S63 ✅
    ├── mastering/       ← regenerated S63 ✅
    ├── synthesis/       ← regenerated S63 ✅
    ├── music-theory/    ← regenerated S63 ✅
    ├── production/      ← regenerated S63 ✅
    ├── recording/       ← regenerated S63 ✅
    └── tools/           ← regenerated S63 ✅ — duplicate tagline removed
```

### Category Page CSS Architecture — LOCKED S63

The following CSS values are confirmed correct for all 11 category pages as of S63. All changes go in `mpw_bible_cat_pages.py` — NEVER inject CSS into generator-managed pages.

**Hero section:**
```css
.bcat-hero { background:linear-gradient(135deg,#1a0a00,#0d0d1a); border-bottom:1px solid rgba(245,166,35,.15); padding:56px 24px 48px }
.bcat-hero-inner { max-width:1100px; margin:0 auto; text-align:center }
.bcat-breadcrumb { font-size:12px; color:#666; margin-bottom:16px; font-family:monospace; text-align:center }
.bcat-eyebrow { font-size:10px; font-family:monospace; letter-spacing:.14em; text-transform:uppercase; color:#f5a623; font-weight:700; margin-bottom:12px; display:block; text-align:center }
.bcat-hero h1 { font-size:clamp(2rem,5vw,3.5rem); font-weight:900; color:#fff; line-height:1.1; margin-bottom:14px; letter-spacing:-0.03em; text-align:center }
.bcat-hero-desc { font-size:15px; color:#a0a0c0; max-width:720px; line-height:1.75; margin-bottom:20px; margin-left:auto; margin-right:auto }
.bcat-count { display:inline-flex; align-items:center; gap:6px; background:#1a1a3a; border:1px solid rgba(245,166,35,.25); border-radius:20px; padding:5px 16px; font-size:13px; color:#888; margin-bottom:20px; margin-left:auto; margin-right:auto }
.bcat-subcats { display:flex; gap:7px; flex-wrap:wrap; margin-top:4px; justify-content:center }
```

**Main content:**
```css
.bcat-main { max-width:1100px; margin:0 auto; padding:40px 24px 80px }
```

**Bible entry cards:**
```css
.az-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:8px }
.az-entry { background:#111118; border:1px solid #1e1e2e; border-left:3px solid rgba(245,166,35,.2); border-radius:6px; padding:14px 14px 14px 15px; text-decoration:none; display:flex; flex-direction:row; align-items:center; justify-content:space-between; gap:10px; transition:border-color .1s,border-left-color .1s,background .1s,box-shadow .1s; min-height:56px }
.az-entry:hover { background:#16130a; border-color:rgba(245,166,35,.25); border-left-color:#f5a623; box-shadow:0 2px 12px rgba(0,0,0,.3) }
.az-entry:active { background:#1a1500; border-left-color:#f5a623 }
.az-entry-body { display:flex; flex-direction:column; gap:3px; flex:1; min-width:0 }
.az-entry-term { font-size:13.5px; font-weight:600; color:#e8e8f0; letter-spacing:-.01em; line-height:1.3 }
.az-entry-cat { font-size:11px; color:#f5a623; font-weight:600; letter-spacing:.03em; text-transform:uppercase; opacity:.6 }
.az-entry:hover .az-entry-term { color:#f5a623 }
.az-entry-arrow { font-size:13px; color:#333; flex-shrink:0; transition:color .1s,transform .1s; line-height:1 }
.az-entry:hover .az-entry-arrow { color:#f5a623; transform:translateX(3px) }
.az-letter-header { display:none }
```

**Tools page cards:**
```css
.bcat-tools-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:8px }
.bcat-card { background:#111118; border:1px solid #1e1e2e; border-left:3px solid rgba(245,166,35,.2); border-radius:6px; padding:16px 16px 16px 18px; text-decoration:none; display:flex; align-items:center; gap:14px; transition:border-color .1s,border-left-color .1s,background .1s,box-shadow .1s; min-height:64px }
.bcat-card:hover { background:#16130a; border-color:rgba(245,166,35,.25); border-left-color:#f5a623; box-shadow:0 2px 12px rgba(0,0,0,.3) }
.bcat-card:active { background:#1a1500; border-left-color:#f5a623 }
.bcat-card-term { font-size:13.5px; font-weight:600; color:#e8e8f0; display:block; line-height:1.3; letter-spacing:-.01em }
.bcat-card:hover .bcat-card-term { color:#f5a623 }
.bcat-card-cat { font-size:11px; color:#f5a623; font-weight:600; text-transform:uppercase; letter-spacing:.03em; display:block; margin-top:3px; opacity:.6 }
.bcat-card-arrow { font-size:15px; color:#333; flex-shrink:0; transition:color .1s,transform .1s; line-height:1 }
.bcat-card:hover .bcat-card-arrow { color:#f5a623; transform:translateX(3px) }
```

**Tools hero extra blocks — centered:**
```css
.bcat-tools-why { background:#13132a; border-left:3px solid #f5a623; border-radius:0 8px 8px 0; padding:14px 18px; margin-top:20px; max-width:720px; margin-left:auto; margin-right:auto }
.bcat-tools-why-label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#f5a623; margin-bottom:6px; text-align:center }
.bcat-tools-why p { font-size:13px; color:#a0a0c0; line-height:1.65; margin:0; text-align:center }
.bcat-tools-request { display:block; background:#13132a; border:1px solid #2a2a4a; border-radius:8px; padding:16px 24px; max-width:720px; margin-top:16px; margin-left:auto; margin-right:auto; text-align:center }
.bcat-tools-request-dot { display:none }
.bcat-tools-request-text { font-size:13px; color:#707090; line-height:1.65; text-align:center }
```

**Responsive breakpoints:**
```css
@media(max-width:1200px) { .az-grid { grid-template-columns:repeat(3,1fr) } .bcat-tools-grid { grid-template-columns:repeat(3,1fr) } }
@media(max-width:1024px) { .bcat-hero { padding:40px 24px 36px } .bcat-main { padding:32px 24px 80px } .az-grid { grid-template-columns:repeat(3,1fr) } .bcat-tools-grid { grid-template-columns:repeat(2,1fr) } }
@media(max-width:768px) { .bcat-hero { padding:28px 16px 24px } .bcat-main { padding:20px 16px 60px } .az-grid { grid-template-columns:repeat(2,1fr) } .bcat-tools-grid { grid-template-columns:1fr } .az-entry { min-height:60px; border-left-color:rgba(245,166,35,.25) } .bcat-card { min-height:68px; border-left-color:rgba(245,166,35,.25) } .az-entry-arrow { display:none } }
@media(max-width:480px) { .az-grid { grid-template-columns:1fr } }
```

### Category Page JS Architecture — Filter System

**JS filter (confirmed working S63):**
```javascript
var _sub='', _q='';
function updateGrid() {
  var sel = '{grid_class}'==='az-grid' ? '.az-entry' : '.bcat-card';
  var cards = document.querySelectorAll('#catGrid '+sel);
  var visible = 0;
  cards.forEach(function(c) {
    var term = (c.querySelector('.az-entry-term,.bcat-card-term')||{}).textContent||'';
    var subcat = (c.dataset && c.dataset.subcat) || '';
    var matchQ = !_q || term.toLowerCase().indexOf(_q) !== -1;
    var matchS = !_sub || subcat === _sub;
    var show = matchQ && matchS;
    c.style.display = show ? 'flex' : 'none';
    if(show) visible++;
  });
}
function filterSub(btn) {
  _sub = (btn.dataset.filter||'').toLowerCase();
  document.querySelectorAll('.bcat-sub').forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  updateGrid();
}
```

**Critical rules:**
- `matchS` uses EXACT equality (`subcat === _sub`) — NOT substring search
- `filterSub()` lowercases the filter value — pill `data-filter` values must be pre-lowercased
- `data-subcat` values on cards must exactly match pill `data-filter` values
- `c.style.display = show ? 'flex' : 'none'` — cards use flexbox so must restore to `flex` not `block`

### SUBCAT_MAP — Complete 232-Slug Reference

The authoritative SUBCAT_MAP lives in `mpw_bible_cat_pages.py` (S63f version). Key rules:
- Every value must exactly match a pill `data-filter` attribute (lowercased)
- Zero mismatches confirmed against all 222 live entries via cross-check script
- Slugs that appear in multiple categories get one entry — assigned to their actual category

### Card HTML Structure — az-entry

```html
<a class="az-entry" href="/bible/{slug}" data-term="{term.lower()}" data-subcat="{subcat}">
  <div class="az-entry-body">
    <span class="az-entry-term">{term}{badge}</span>
    <span class="az-entry-cat">{subcat.title() if subcat else ecat}</span>
  </div>
  <span class="az-entry-arrow">→</span>
</a>
```

**Critical:** card label shows `subcat.title()` — the specific subcategory — NOT the parent category name.

### Beehiiv Newsletter — bible/index.html

```html
<!-- In <head> — both scripts required -->
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="a0962c52-4819-4b09-b13d-b26517b76e01"></script>
<script type="text/javascript" async src="https://subscribe-forms.beehiiv.com/attribution.js"></script>

<!-- In body — replaces hardcoded input/button form -->
<div data-beehiiv-form="a0962c52-4819-4b09-b13d-b26517b76e01"></div>
```

Form ID: `a0962c52-4819-4b09-b13d-b26517b76e01` — confirmed live in bible/index.html (SHA `7bfb2b6b`).

### 650 WPM Read Time Standard — CONFIRMED S63

All Bible entries going forward: `read_time = round(word_count / 650)` — minimum 1 min.

Updated entries this session: reverb.html (33→25min), bible/index.html featured card (~25min).
Remaining 222 live entries: not yet updated — patch when convenient, not a blocker.
`mpw_bible_writer.py`: must be updated to use 650 wpm before next batch run.

### Category Page Audit Results — S63 Final

Post-session audit of all 12 pages (11 category + 1 bible/index):

| Page | SHA | Status |
|------|-----|--------|
| Bible Index | 7bfb2b6b | ✅ Clean — Beehiiv wired |
| Dynamics | eb155bdc | ✅ Clean |
| Frequency | faaf57c1 | ✅ Clean |
| Time-Based | 97b92634 | ✅ Clean |
| Signal Processing | 6a11ec2a | ✅ Clean |
| Mixing | aa530324 | ✅ Clean |
| Mastering | c968d1e9 | ✅ Clean |
| Synthesis | 4549a73c | ✅ Clean |
| Music Theory | 8a99cb4c | ✅ Clean |
| Production | 4f7d2fd8 | ✅ Clean |
| Recording | 94ef5432 | ✅ Clean |
| Tools | dfcac826 | ✅ Clean |

All pages confirmed: slim-bar/bible-bar/bmn-drawer ✅, `/css/style.css` absolute ✅, `max-width:1100px` ✅, `text-align:center` on hero ✅, amber card borders ✅, `data-subcat` on all cards ✅, `dataset.subcat` filter ✅, GA4 ✅, canonical ✅, OG meta ✅, JSON-LD ✅, no 2025 dates ✅, mobile breakpoints ✅

## NEVER Rules Added — Session 63 — Tech

| Rule | Detail |
|------|--------|
| NEVER use CSS inject approach on generator-managed pages | `mpw_bible_cat_pages.py --run` regenerates from scratch — any CSS injected into live pages is overwritten on next run. ALL changes go in the generator. |
| NEVER increase category page max-width beyond 1100px | Tested 1400px — 4-col cards at 1400px become ~340px wide and look blown out. 1100px is the confirmed correct maximum. |
| NEVER declare hero centering done without verifying every direct child element individually | `text-align:center` on the outer container does NOT automatically center all children. Breadcrumb, eyebrow, h1, desc, count badge, pills, tools-why, tools-request — each needs explicit `text-align:center` or `margin:auto`. |
| NEVER center hero content by changing max-width | The centering issue was always a text-alignment issue, not a width issue. Increasing max-width made cards wider, not content more centered. |
| NEVER show parent category name as card label | `az-entry-cat` must show `subcat.title() if subcat else ecat` — never the raw `ecat` parent category. |
| NEVER write a SUBCAT_MAP without running zero-mismatch verification against live bible-index.json | 62 mismatches in first S63 version caused subcategory filters to show wrong entries across all categories. Always run cross-check before delivery. |
| NEVER use Beehiiv iframe embed | Current embed method is v3 loader script + `data-beehiiv-form` div — confirmed with Beehiiv dashboard. iframe method is legacy and unreliable. |
| NEVER deliver a category page script without running it locally with --test first | The --test flag prints the first 600 chars of one generated page — catches template errors before committing all 11 pages. |

---

# SESSION 63/64 UPDATE — TECH — May 24, 2026

## `/tools/index.html` — Final Architecture

### File Location
`tools/index.html` in repo root — served at `musicproductionwiki.com/tools/`

### Asset Paths
`../css/style.css` and `../js/main.js` — identical to `/bible/` pattern (one level deep from root).

### Nav System
Uses `mpw-nav-homepage-v1` inline style block — same as all article pages. NOT bible-bar/slim-bar system. This is an MPW page, not a Bible page.

**Desktop nav order:** `Articles ▾ · Gear ▾ · Tools → · The Producer's Bible →`

**CSS specificity lesson learned this session:** The general rule `nav.mpw-site-nav .nav-item>a{color:#a0a0b4!important}` uses a child combinator and beats `.nav-bible-link{color:#f5a623!important}` even though both have `!important`, because child combinator increases specificity. The correct override pattern is:
```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
```
Always use `nav-item>a.classname` pattern for nav color overrides on pages using mpw-nav-homepage-v1.

### Card Design — Locked
```css
.tool-card {
  background: #111118;
  border: 2px solid rgba(245,166,35,0.45);  /* amber 2px — matches Bible family */
  border-radius: 8px;
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  min-height: 80px;
  transition: border-color .12s, background .12s, box-shadow .12s;
}
.tool-card:hover {
  background: #1a1200;
  border-color: rgba(245,166,35,0.85);
  box-shadow: 0 2px 16px rgba(245,166,35,0.12);
}
.tool-card:active {
  background: #1a1200;
  border-color: #f5a623;
}
```

**Design rationale:** Amber borders connect tools to the Bible family. Teal is reserved for the tools identity (eyebrow, active pills, Tools nav link). Hover is amber not teal — reinforces the premium/Bible feel.

### Grid Breakpoints — Locked
```css
@media(max-width:1024px) { .tools-grid { grid-template-columns: repeat(2,1fr); } }
@media(max-width:768px)  { .tools-grid { grid-template-columns: repeat(2,1fr); } }  /* 2-col on mobile — cards have enough content */
@media(max-width:420px)  { .tools-grid { grid-template-columns: 1fr; } }  /* single col only at very small screens */
```

### Static Elements — Never Auto-Update
- Section label: static `"Tools"` — never shows count
- Stats row: `Free forever · No signup required · Works on mobile` — no count
- Request link: mailto:mpwikiofficial@gmail.com with subject `Tool%20Request`

### Mobile Drawer — tools/index.html specific
The tools hub page uses the standard `mpw-nav-homepage-v1` mobile drawer with additional entries:
```html
<div class="mobile-drawer" id="mobileDrawer">
  <a href="/tools/" class="mob-tools">✦ The Producer's Tools</a>
  <a href="/bible/" class="mob-bible">● The Producer's Bible — Explore Free</a>
  <div class="mob-section-label">Articles</div>
  <a class="mob-link" href="/categories/techniques.html">Techniques</a>
  ...
  <a href="https://theproducersbriefing.beehiiv.com" class="mob-cta">Sound Better →</a>
</div>
```
Note: `mob-tools` CSS class is defined in the mpw-nav-homepage-v1 style block on this page.

---

## File Structure — Updated

```
repo root/
├── bible/
│   ├── index.html           ← REBUILT S63 — reverb.html nav, Reverb featured, ~25min, Beehiiv wired — SHA 7bfb2b6b
│   ├── reverb.html          ← gold standard entry — read time patched 33→25min — SHA 8b6dd26d
│   ├── [222 entries]        ← mobile-drawer still in place — bmn-drawer PENDING (batch approach confirmed safe for S65)
│   └── categories/
│       ├── dynamics/        ← regenerated S63 from mpw_bible_cat_pages_s63f.py ✅
│       ├── frequency/       ← regenerated S63 ✅
│       ├── time-based/      ← regenerated S63 ✅
│       ├── signal-processing/ ← regenerated S63 ✅
│       ├── mixing/          ← regenerated S63 ✅
│       ├── mastering/       ← regenerated S63 ✅
│       ├── synthesis/       ← regenerated S63 ✅
│       ├── music-theory/    ← regenerated S63 ✅
│       ├── production/      ← regenerated S63 ✅
│       ├── recording/       ← regenerated S63 ✅
│       └── tools/           ← regenerated S63 ✅
├── tools/
│   ├── index.html           ← BUILT S64 — tools hub — SHA 44c8f9b8 (amber cards) → 8c7269d2 (nav fix) ✅ LIVE
│   └── [36 slug].html       ← all 36 standalone tool pages — LIVE ✅
├── index.html               ← Tools → added to nav SHA fe168acb ✅
├── css/style.css
├── js/main.js
└── [handoff files]
```

---

## MPW Article Nav Audit — Session 64

Audited all 526 article pages (sample every 25th = 22 articles checked). Results:

**All 526 articles are identical nav structure — one pattern, zero variants.**

| Property | Value |
|----------|-------|
| Nav system | `mpw-site-nav` with `mpw-nav-homepage-v1` style block |
| Style IDs present | `mpw-nav-homepage-v1`, `mpw-bible-bar-css` |
| Drawer type | `mobile-drawer` (NOT bmn-drawer) |
| Bible link HTML | `<li class="nav-item"><a href="/bible/" class="nav-bible-link">The Producer\u2019s Bible \u2192</a></li>` |
| Tools link present | ❌ Not yet |
| `.nav-tools-link` CSS | ✅ Already defined in mpw-nav-homepage-v1 style block |
| Target string bytes | Smart apostrophe U+2019, rightward arrow U+2192 |

**This confirms the batch is clean to run** — one string replacement, one drawer replacement, 526 identical files.

---

## Homepage (`index.html`) — Nav Updated

SHA: `fe168acb`

Homepage has a different nav pattern from articles — Bible link uses inline style not class. Tools was added matching that pattern:
```html
<li class="nav-item"><a href="/tools/" style="color:#00e8a2!important;font-weight:600;text-decoration:none;">Tools →</a></li>
```
Mobile drawer also updated with inline-styled teal Tools entry before mob-bible.

---

## NEVER Rules Added — Session 63/64 — Tech

| Rule | Detail |
|------|--------|
| NEVER use `.nav-bible-link` or `.nav-tools-link` alone for color overrides on mpw-nav-homepage-v1 pages | `nav.mpw-site-nav .nav-item>a` child combinator beats class-only selectors even with !important. Always use `nav.mpw-site-nav .nav-item>a.classname` pattern |
| NEVER show tool count on tools/index.html | Static label only — count goes stale as tools are added |
| NEVER change the tools hub to a generator script | Hand-crafted HTML gives full design control — same approach as reverb.html and bible/index.html |
| NEVER use bible-bar/slim-bar nav on /tools/ pages | Tools hub is MPW side, not Bible side — uses mpw-site-nav system |

---

# SESSION 65 UPDATE — TECH — May 24, 2026

## Article Nav — Final Confirmed State (All 526 Articles)

### Desktop Nav — Confirmed
```html
<li class="nav-item"><a href="/tools/" class="nav-tools-link">Tools →</a></li>
<li class="nav-item"><a href="/bible/" class="nav-bible-link">The Producer's Bible →</a></li>
```

### CSS Specificity — Confirmed Fix
Old (broken — beaten by child combinator rule):
```css
nav.mpw-site-nav .nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
```

New (correct — matches specificity of the overriding rule):
```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
```

**Lesson:** On `mpw-nav-homepage-v1` pages, the general rule `nav.mpw-site-nav .nav-item>a{color:#a0a0b4!important}` uses a child combinator and beats any class-only selector. Child combinator (`>`) increases specificity beyond a simple class. Always use `nav-item>a.classname` pattern for nav color overrides.

## CSS Specificity Reference — mpw-nav-homepage-v1 Pages

This rule governs all article pages and tools/index.html:

```css
/* THE OVERRIDING RULE (already in mpw-nav-homepage-v1 block): */
nav.mpw-site-nav .nav-item>a{color:#a0a0b4!important}
/* Child combinator (>) means: specificity = (0,2,1) — beats class-only selectors */

/* WRONG — beaten even with !important: */
nav.mpw-site-nav .nav-bible-link{color:#f5a623!important}
/* specificity = (0,2,0) — loses to (0,2,1) despite !important */

/* CORRECT — matches the specificity pattern: */
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important}
/* specificity = (0,3,1) — wins */
```

**This gotcha has burned us three times** (tools/index.html S63/64, all 526 articles S65, tool pages S66). On any page using `mpw-nav-homepage-v1`, all nav link color overrides MUST use the `nav.mpw-site-nav .nav-item>a.classname` pattern.

### Mobile Drawer — Confirmed Final HTML (All 526 Articles)
```html
<div class="mobile-drawer" id="mobileDrawer">
  <a href="/tools/" style="display:flex;align-items:center;gap:8px;padding:12px 16px;border-radius:9px;background:rgba(0,232,162,0.07);border:1px solid rgba(0,232,162,0.22);color:#00e8a2;font-size:14px;font-weight:600;text-decoration:none;margin:4px 0 8px">✦ The Producer's Tools</a>
  <a href="/bible/" class="mob-bible">●&nbsp;The Producer's Bible — Explore Free</a>
  <div class="mob-section-label">Articles</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:4px">
    <a href="/categories/techniques.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Techniques</a>
    <a href="/categories/reviews.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Reviews</a>
    <a href="/categories/comparisons.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Comparisons</a>
    <a href="/categories/breakdowns.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Breakdowns</a>
    <a href="/categories/recreations.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Recreations</a>
    <a href="/genres.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Genres</a>
    <a href="/categories/ai-music.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">AI Music</a>
    <a href="/categories/music-business.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Music Business</a>
  </div>
  <div class="mob-section-label">Gear</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:4px">
    <a href="/categories/daws.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">DAWs</a>
    <a href="/categories/plugins.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Plugins</a>
    <a href="/categories/gear.html" style="display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a">Hardware</a>
  </div>
  <a href="https://theproducersbriefing.beehiiv.com" class="mob-cta">Sound Better →</a>
</div>
```

**Important:** `mob-bible` link contains `\u00a0` (non-breaking space U+00A0) after the bullet character — NOT a regular space. Any future patch script targeting this string must use the exact bytes. Confirmed by fetching live file and printing `repr()`.

### Drawer JS — pushState/popstate Pattern (All 526 Articles)
```javascript
var mob=document.getElementById('navMob');
var drawer=document.getElementById('mobileDrawer');
if(mob&&drawer){
  mob.addEventListener('click',function(){
    var opening=!drawer.classList.contains('open');
    drawer.classList.toggle('open');
    if(opening&&window.history&&window.history.pushState){history.pushState({drawerOpen:true},'',location.href);}
  });
  drawer.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){drawer.classList.remove('open');});});
  window.addEventListener('popstate',function(e){if(drawer.classList.contains('open')){drawer.classList.remove('open');}});
}
```

**pushState vs replaceState — Why It Matters:**
- Category pages use `replaceState` — Netlify redirect creates double history entry on load, collapsing it prevents extra back-press
- Article pages have no redirect — load cleanly. `pushState` on drawer open adds a fake history entry; back button fires `popstate` → closes drawer instead of navigating away
- NEVER use `replaceState` on article drawer pages

## NEVER Rules Added — Session 65 — Tech

| Rule | Detail |
|------|--------|
| NEVER use `replaceState` to fix the drawer back-button on article pages | `replaceState` is for Netlify-redirect double-history-entry (category pages). Article pages need `pushState` on open + `popstate` listener to close — confirmed working, commit f6979227 |
| NEVER patch mobile drawer HTML without printing exact `repr()` of the live target string | `\u00a0` non-breaking space in `mob-bible` link was only found by inspecting exact bytes — not visible in normal output |
| NEVER add nav color overrides with class-only selectors on mpw-nav-homepage-v1 pages | Child combinator specificity beats `!important` class-only — must use `nav.mpw-site-nav .nav-item>a.classname` — burned three times, now permanently documented |
| NEVER run a 500+ file batch without at least 4 iterative fixes confirmed on the test article first | Session 65 ran 4 commits on test article before the full batch — this is correct and prevents corrupting all 526 |
| NEVER use bmn-drawer-cat CSS class on article pages | Article pages lack bmn-drawer CSS — use inline styles for grid card items only |


---

# SESSION 65 UPDATE — TECH (Part 2) — May 24, 2026

## Browser App Technology Reference

### Web Audio API — Capabilities Confirmed Available

The Web Audio API is built into every modern browser. No CDN import needed. All Browser Apps on MPW can use it immediately.

**What Claude can build with Web Audio API alone:**
- Real oscillators generating sine, square, sawtooth, triangle waves
- Real-time filter effects (lowpass, highpass, bandpass, notch)
- Reverb simulation via ConvolverNode
- Delay effects via DelayNode with feedback loops
- Distortion/overdrive via WaveShaperNode
- Gain/volume control via GainNode
- Real-time frequency spectrum analysis via AnalyserNode (for spectrum visualizer, tuner)
- Microphone input via getUserMedia → MediaStreamSourceNode
- Audio recording via MediaRecorder API
- Panning via StereoPannerNode

**Tone.js additional capabilities (importable via CDN):**
- Musical note names (C4, Bb3, etc.) mapped to frequencies automatically
- Tempo-synced scheduling (Transport — plays events on the beat)
- Pre-built synth voices (Synth, PolySynth, MembraneSynth for kicks, MetalSynth for hi-hats)
- Musical timing (Tone.Time for note values: "8n" = eighth note, "16n" = sixteenth note)
- Automatic BPM management

**CDN import:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

### getUserMedia — Microphone Input Pattern

```javascript
async function initMicrophone() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true, video: false});
    const audioContext = new AudioContext();
    const source = audioContext.createMediaStreamSource(stream);
    const analyser = audioContext.createAnalyser();
    analyser.fftSize = 2048;
    source.connect(analyser);
    return {audioContext, analyser};
  } catch (err) {
    console.warn('Microphone not available:', err);
    return null;
  }
}
```

Always include graceful fallback when microphone is denied — show a static reference version.

### Audio Context Autoplay Policy — CRITICAL

Every modern browser blocks AudioContext autoplay until a user gesture occurs.

**CORRECT pattern:**
```javascript
let audioStarted = false;
document.getElementById('playButton').addEventListener('click', async () => {
  if (!audioStarted) {
    await Tone.start(); // or new AudioContext() and .resume()
    audioStarted = true;
  }
  transport.start();
});
```

**WRONG pattern (silently blocked):**
```javascript
// Do NOT do this — blocked in all modern browsers
const synth = new Tone.Synth().toDestination();
synth.triggerAttack("C4"); // blocked — no user gesture
```

All Browser Apps must display a visible "Click to Start" or "Tap to Begin" interface element before any audio output.

### Browser DAW — Tone.js Instrument Patterns

```javascript
// Kick drum
const kick = new Tone.MembraneSynth({
  pitchDecay: 0.05, octaves: 5,
  envelope: {attack: 0.001, decay: 0.4, sustain: 0, release: 1.4}
}).toDestination();

// Snare
const snare = new Tone.NoiseSynth({
  noise: {type: 'white'},
  envelope: {attack: 0.001, decay: 0.15, sustain: 0, release: 0.05}
}).toDestination();

// Step sequencer scheduling
let step = 0;
const seq = new Tone.Sequence((time) => {
  if (grid[0][step]) kick.triggerAttackRelease('C1', '8n', time);
  if (grid[1][step]) snare.triggerAttackRelease('8n', time);
  Tone.getDraw().schedule(() => { updateStepDisplay(step); }, time);
  step = (step + 1) % 16;
}, null, '16n');
```

### Tools Hub (`/tools/index.html`) — Adding Browser App Cards

```html
<a class="tool-card" href="/tools/browser-daw.html" data-cat="browser-app" data-name="browser daw">
  <div class="tool-card-body">
    <span class="tool-card-name">Browser DAW ⭐</span>
    <span class="tool-card-desc">Make music in your browser. 16-step sequencer, built-in synth, 5 genre presets. No download.</span>
    <span class="tool-card-cat">Browser Apps</span>
  </div>
</a>
```

Add category pill:
```html
<button class="tools-cat-btn" data-cat="browser-app">Browser Apps</button>
```

The filter JS handles any `data-cat` value — no JS changes needed, just add the pill button.

### AI Music Tools — No New Infrastructure

All AI Music tools are static HTML at `/tools/[slug].html`. The API-powered variants (Rights Navigator, Prompt Optimizer, DDEX Checker, Copyright Strength) call the Anthropic API via the Netlify proxy. No new backend. No additional hosting cost.

## NEVER Rules Added — Session 65 Part 2 — Tech

| Rule | Detail |
|------|--------|
| NEVER create AudioContext before a user gesture in any Browser App | Browsers block all audio autoplay — always create or resume AudioContext inside a click/tap event handler. `await Tone.start()` is the correct pattern with Tone.js |
| NEVER add a "Browser Apps" category pill to `/tools/index.html` until at least one Browser App is live | Filter pill for a category with zero results is confusing — add pill in same commit as first browser app |
| NEVER use a Tone.js CDN URL not verified on cdnjs.cloudflare.com | Unverified CDN URLs may be blocked by Netlify or unavailable |
| NEVER build the Browser DAW with more than 8 tracks in the MVP | 8 tracks, 16 steps, basic effects is the MVP |
| NEVER commit a Browser App to /tools/ without adding its card to /tools/index.html in the same Trees API commit | An orphaned tool page with no hub card is unfindable |


---

# SESSION 66 UPDATE — TECH — May 25, 2026

## MPW-TOOL-BUILD-SPEC.md — The Frozen Tool Template

**Every tool build session MUST read MPW-TOOL-BUILD-SPEC.md first.** It contains the frozen visual system, component library, and quality checklist that ensures all tools look and function identically.

### Frozen CSS Variables (copy verbatim into every tool)

```css
:root {
  --bg:        #0d0d1a;
  --bg2:       #111120;
  --bg3:       #16162a;
  --bg4:       #1c1c32;
  --border:    rgba(255,255,255,0.07);
  --border2:   rgba(255,255,255,0.12);
  --border3:   rgba(255,255,255,0.18);
  --amber:     #f5a623;
  --amber2:    rgba(245,166,35,0.12);
  --amber3:    rgba(245,166,35,0.06);
  --teal:      #00e8a2;
  --teal2:     rgba(0,232,162,0.1);
  --red:       #ff3d5a;
  --green:     #00e8a2;
  --text:      #f0f0f4;
  --text2:     #a0a0b8;
  --text3:     #5a5a7a;
  --mono:      'DM Mono', monospace;
  --sans:      'DM Sans', sans-serif;
}
```

**Session 67 confirmed actual background:** `#06061a` (overrides `--bg: #0d0d1a` from spec — use `#06061a` as body background on tool pages built S67+).

### Frozen Font Import (copy verbatim into every tool `<head>`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Frozen Tool Header Component

```html
<div class="tool-header-card">
  <div class="tool-header-brand">
    <div class="tool-logo-mark">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
        <rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
        <rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>
        <rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>
        <rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
      </svg>
    </div>
    <div class="tool-brand-text">
      <div class="tool-brand-name">MusicProductionWiki.com</div>
      <div class="tool-brand-sub">◆ The Producer's Bible</div>
    </div>
  </div>
  <div class="tool-header-right">
    <span class="tool-badge">INTERACTIVE TOOL</span>
    <a href="/tools/[RELATED-TOOL]" class="tool-related-link">[Related Tool Name]</a>
  </div>
</div>
```

### Frozen Components — Quick Reference

Full CSS for all frozen components is in MPW-TOOL-BUILD-SPEC.md. Summary:

| Component | CSS Class | Notes |
|-----------|-----------|-------|
| Header card | `.tool-header-card` | Required on every tool |
| Section card | `.tool-section` + `.tool-section-label` | Dark bg, amber label |
| Insight callout | `.tool-insight` | Amber left-border, amber3 bg |
| Slider | `.tool-slider` + `.tool-slider-val` | Amber thumb |
| Select/dropdown | `.tool-select` | SVG chevron, no appearance |
| Primary button | `.tool-btn` | Amber gradient, hover lift |
| Click-to-copy chip | `.copy-chip` | Teal on copied state |
| Canvas container | `<canvas>` | CSS width/height only — JS sets pixel dimensions |

### Tool Page Required Elements Checklist

Every tool page MUST include all of the following before committing:

**Head Section:**
- [ ] `<meta charset="UTF-8">`
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] `<title>` — tool name + MPW brand + keyword
- [ ] `<meta name="description">` — 150–160 chars, keyword-rich
- [ ] `<link rel="canonical" href="https://www.musicproductionwiki.com/tools/[slug].html">`
- [ ] OG tags: og:title, og:description, og:url, og:type="website"
- [ ] Twitter card tags
- [ ] GA4 script (G-79VB543KCT)
- [ ] DM Sans + DM Mono font import
- [ ] ~~`<link rel="stylesheet" href="../css/style.css">`~~ **NEVER — causes 600px blobs** (S68 correction)
- [ ] Favicon: `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` + `<link rel="alternate icon" href="/favicon.ico">`
- [ ] FAQPage JSON-LD schema (minimum 3 FAQ pairs)
- [ ] BreadcrumbList JSON-LD schema
- [ ] WebPage JSON-LD schema

**Body — Required:**
- [ ] Full MPW site nav (mpw-nav-homepage-v1 style block + nav HTML)
- [ ] Nav CSS specificity fix: `nav.mpw-site-nav .nav-item>a.nav-bible-link` + `nav.mpw-site-nav .nav-item>a.nav-tools-link`
- [ ] Mobile drawer: grid style with Tools teal pill + Bible amber pill + pushState JS
- [ ] Tool title (H1) + description paragraph
- [ ] Tool header branded card (MPW logo + Interactive Tool badge)
- [ ] Interactive tool body — use `.tool-hero` / `.tool-container` NOT `.hero` / `.container`
- [ ] Related tools section (link to 3 relevant other tools)
- [ ] Footer with copyright + links to /tools/, /bible/, newsletter
- [ ] `<script src="../js/main.js"></script>` at end of body — NEVER style.css

**Commit Checklist:**
- [ ] File committed to `/tools/[slug].html` via GitHub API
- [ ] Tool card added to `/tools/index.html` in same Trees API commit
- [ ] Sitemap updated (or flagged for batch update)
- [ ] Steve visually confirms on live site

### Tool Card HTML Pattern for /tools/index.html

```html
<a class="tool-card" href="/tools/[slug].html" data-cat="[category]" data-name="[searchable name]">
  <div class="tool-card-body">
    <span class="tool-card-name">[Tool Name]</span>
    <span class="tool-card-desc">[One-sentence description. 12 words max.]</span>
    <span class="tool-card-cat">[Category Name]</span>
  </div>
  <span class="tool-card-arrow">→</span>
</a>
```

Category `data-cat` values:
- AI Music tools: `data-cat="ai-music"`
- Mix/vocal tools: `data-cat="mixing"`
- Beat/drum tools: `data-cat="beat-making"`
- Business tools: `data-cat="business"`
- Frequency tools: `data-cat="frequency"`
- Music theory tools: `data-cat="arrangement"`
- Browser apps: `data-cat="browser-app"`

## NEVER Rules Added — Session 66 — Tech

| Rule | Detail |
|------|--------|
| NEVER use class-only nav selectors | Child combinator required: `nav.mpw-site-nav .nav-item>a.classname` — documented repeatedly |
| NEVER build a tool page without the frozen CSS variables block | Copy from MPW-TOOL-BUILD-SPEC.md — do not re-derive colors |
| NEVER set canvas width/height via HTML attributes | Use CSS width/height; set canvas.width/canvas.height via JS after offsetWidth check |
| NEVER commit a tool without adding its card to /tools/index.html | Same Trees API commit — never two separate deploys for one tool |
| NEVER launch AI Music tools without verifying current platform terms | Suno, Udio, DDEX terms change frequently |
| NEVER add new category pill to tools hub without at least one tool in that category live | Add the pill in the same commit as the first tool in that category |


---

# SESSION 67 UPDATE — TECH — May 25, 2026

## Netlify Function — Final Working Implementation

### `netlify/functions/claude-proxy.js`
```javascript
const https = require('https');

exports.handler = async (event) => {
  const cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json'
  };
  if (event.httpMethod === 'OPTIONS') return { statusCode: 204, headers: cors, body: '' };
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return { statusCode: 500, headers: cors, body: JSON.stringify({ error: 'ANTHROPIC_API_KEY not set' }) };
  return new Promise((resolve) => {
    const data = Buffer.from(event.body || '{}');
    const req = https.request({
      hostname: 'api.anthropic.com', port: 443, path: '/v1/messages', method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': data.length, 'x-api-key': key, 'anthropic-version': '2023-06-01' }
    }, (res) => {
      let body = '';
      res.on('data', c => body += c);
      res.on('end', () => resolve({ statusCode: res.statusCode, headers: cors, body: body }));
    });
    req.on('error', e => resolve({ statusCode: 502, headers: cors, body: JSON.stringify({ error: e.message }) }));
    req.write(data); req.end();
  });
};
```

### `netlify.toml` — Current State (Session 67)
```toml
[build]
  publish = "."
  command = "echo 'build complete'"

[functions]
  directory = "netlify/functions"

[[redirects]]
  from = "/api/claude"
  to = "/.netlify/functions/claude-proxy"
  status = 200
  force = true

[[redirects]]
  from = "/dictionary/*"
  to = "/bible/:splat"
  status = 301

[[redirects]]
  from   = "/ssl-2-plus-review/"
  to     = "/articles/ssl-2-plus-review.html"
  status = 301

[[redirects]]
  from   = "/ssl-2-plus-review"
  to     = "/articles/ssl-2-plus-review.html"
  status = 301
```

**CRITICAL:** `[build] command` is required. Without it Netlify skips function bundling on static sites.

---

## Claude API Call Pattern — Correct for All Future Tools

```javascript
var res = await fetch('https://classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'claude-sonnet-4-6',
    max_tokens: 800,
    system: systemPrompt,
    messages: [{ role: 'user', content: userMessage }]
  })
});
var data = await res.json();
var raw = data.content && data.content[0] ? data.content[0].text : '';
console.log('RAW:', raw.substring(0, 300)); // always log for debugging
```

**Note:** S66 append showed direct `api.anthropic.com` calls — that pattern is SUPERSEDED. CORS prevents direct API calls from browser tool pages. Always use the proxy.

---

## Favicon

```html
<!-- In every tool <head> -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.ico">
```

```svg
<!-- /favicon.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#00e8a2"/>
  <rect x="3" y="13" width="4" height="15" rx="2" fill="#06061a"/>
  <rect x="10" y="8" width="4" height="20" rx="2" fill="#06061a"/>
  <rect x="17" y="3" width="4" height="26" rx="2" fill="#06061a"/>
  <rect x="25" y="10" width="4" height="15" rx="2" fill="#06061a"/>
</svg>
```

---

## Tool Design System — Session 67 Confirmed Actual Values

These override the CSS variables spec from MPW-TOOL-BUILD-SPEC.md where they conflict:

| Property | Value |
|----------|-------|
| Background | `#06061a` |
| Body text | `#e8e8ff` |
| Chip text unselected | `#c0c0e8` |
| Chip border unselected | `rgba(255,255,255,0.18)` |
| Section label | `#00e8a2` teal, DM Mono bold, 9-10px |
| Group labels | `#8080b8` DM Mono bold |
| Waveform speed — main | `0.00125` |
| Waveform speed — blue | `0.0019` |
| Waveform speed — amber | `0.0008` |
| Output text | DM Sans 16-18px — NEVER monospace |
| Monospace | DM Mono — labels/counts/hints ONLY |

---

## Robust Response Parsing Pattern

```javascript
function extract(pattern, text, fallback) {
  var m = text.match(pattern);
  return m ? m[1].trim() : fallback;
}
var optimized = extract(/OPTIMIZED:\s*([^\n]+)/i, raw, '') || input;
var analysis  = extract(/ANALYSIS:\s*([\s\S]+?)(?=\nNEXT:|\n\d+\.|$)/i, raw, '');
var next      = extract(/NEXT:\s*([\s\S]+?)$/i, raw, '');

// Fallback if parsing fails completely
if (!analysis && !next && raw.length > 50) {
  var lines = raw.split('\n').filter(l => l.trim());
  analysis = lines.filter(l => !/^(SCORE|OPTIMIZED|ANALYSIS|NEXT|\d+[\.)])/i.test(l.trim()) && l.length > 20).join(' ');
  next = lines.filter(l => /^\d+[\.)]\s/.test(l.trim())).join('\n');
}
```

---

## NEVER Rules Added — Session 67 — Tech

| Rule | Detail |
|------|--------|
| NEVER call Netlify functions via custom domain | `musicproductionwiki.com/.netlify/functions/*` = 404. Always use `classy-haupia-be8e43.netlify.app` |
| NEVER use `fetch()` inside Netlify Functions | Use `https.request()` + `Buffer.from()` |
| NEVER omit `[build] command` from netlify.toml | Required for function bundling on static sites |
| NEVER use `claude-sonnet-4-5` or `claude-sonnet-4-20250514` | Correct model is `claude-sonnet-4-6` |
| NEVER use assistant prefill in API calls | Returns empty content array |
| NEVER put output text in monospace | DM Sans everywhere readable — DM Mono for labels/counts/hints ONLY |
| NEVER insert catGrid cards without position verification | Confirm: grid_open < insert_pos < catEmpty_pos |


---

# SESSION 68 UPDATE — TECH — May 26, 2026

## Critical Technical Lessons

### 1. Python-in-JS Causes Silent Syntax Errors

**Root cause:** Writing JS via Python string interpolation in heredocs.

**Example of what broke:**
```python
# This looks fine in Python but writes broken JS
sys_prompt = f"SCORE: [1-10]\nGENRE_SCORE: [0-10]"
# Writes literal newline into JS string → SyntaxError
```

**Correct pattern — always:**
```bash
# Write JS as pure heredoc
cat > /home/claude/tool_js.js << 'JSEOF'
var sys = 'SCORE: [1-10]\nGENRE_SCORE: [0-10]';  // \n is a real escape here
JSEOF
# Verify syntax
node --check /home/claude/tool_js.js && echo "OK"
# Read into HTML as raw bytes — never as Python string
```

**The rule:** Python never touches JS content. Write JS → check JS → read as bytes → embed.

---

### 2. Nav Div Balance — Use Depth Tracking

**Root cause:** Extracting nav block with `find('</div>', mob_end)` truncated mid-drawer.

**Broken pattern:**
```python
nav_end = html.find('</div>', mob_drawer_end)
nav_block = html[nav_start:nav_end + 6]  # Wrong — grabs first </div> after drawer
```

**Correct pattern:**
```python
# Track div depth to get perfectly balanced block
depth = 0
pos = nav_start
while pos < len(html):
    open_m = html.find('<div', pos)
    close_m = html.find('</div>', pos)
    if open_m == -1: open_m = len(html)
    if close_m == -1: close_m = len(html)
    if open_m < close_m:
        depth += 1; pos = open_m + 4
    else:
        depth -= 1; pos = close_m + 6
        if depth == 0: break
nav_block = html[nav_start:pos]
# Verify: nav_block.count('<div') == nav_block.count('</div>')
```

---

### 3. style.css Cannot Be Loaded on Tool Pages

**Why:** `style.css` defines `.hero::before` (600px circle) and `.hero::after` (400px circle) as massive black radial-gradient blobs. These render as giant black shapes that push tool content hundreds of pixels down.

**What the working tools do:** They load `main.js` only. The nav renders because `main.js` provides JS behavior (dropdown toggle, mobile drawer). The nav's visual CSS comes from the browser's cached `style.css` from other site pages OR the 4 nav specificity lines in the tool's own `<style>` block.

**Rule:** NEVER add `<link rel="stylesheet" href="/css/style.css">` or `<link rel="stylesheet" href="../css/style.css">` to tool pages.

---

### 4. Class Name Conflicts With Global CSS

Classes to NEVER use in tool pages (defined in `style.css` with conflicting rules):
- `.hero` — has `::before`/`::after` 600px/400px blobs, `padding: 5rem 0 4rem`
- `.container` — has `max-width: var(--max-w)`, `overflow-x: hidden`
- `.newsletter-section` — has 700px blob
- `.category-header` — has 400px blob
- `.hero-lines` — has full-viewport background-image

**Safe alternatives:** `.tool-hero`, `.tool-container`, or any unique prefixed class.

---

### 5. File Assembly for Large HTML Tools

**Working pattern (no Python interpolation touching JS):**

```python
# 1. Write JS as pure heredoc — node --check it
# 2. Write HTML sections as Python writes (ok for HTML strings)
# 3. Assemble by reading files as raw bytes

with open('/home/claude/final_tool.html', 'wb') as out:
    for section in ['head.html', 'css.html', 'body.html']:
        with open(f'/home/claude/{section}', 'rb') as f:
            out.write(f.read())
    # JS file — read as raw bytes, never as Python string
    with open('/home/claude/tool.js', 'rb') as f:
        out.write(b'\n<script>\n')
        out.write(f.read())
        out.write(b'\n</script>\n</body>\n</html>')
```

---

### 6. Pre-Commit Verification Checklist for Tool Pages

Run `mpw_precommit_check.py` before every commit. Key checks:

```python
import re, subprocess

with open('tool.html') as f: html = f.read()

# Div balance
assert html.count('<div') == html.count('</div>'), "Unbalanced divs"

# No style.css
assert 'style.css' not in html, "style.css must not be loaded"

# JS syntax check — extract each <script> block and node --check it
scripts = re.findall(r'<script(?![\s\S]{0,10}(?:async|ld\+json|src=))[^>]*>([\s\S]+?)</script>', html)
for i, s in enumerate(scripts):
    with open(f'/tmp/check_{i}.js','w') as f: f.write(s)
    r = subprocess.run(['node','--check',f'/tmp/check_{i}.js'], capture_output=True, text=True)
    assert r.returncode == 0, f"Script {i} syntax error: {r.stderr}"

# Model string
assert 'claude-sonnet-4-6' in html, "Wrong model"

# Proxy URL
assert 'classy-haupia-be8e43' in html, "Wrong proxy"

print("ALL CHECKS PASSED")
```


---

# ⛔ SESSION 78 UPDATE — May 27, 2026

## State at End of Session 78
- Articles: **526** live (unchanged)
- Bible entries: **223+** live
- Tools: **41** live (unchanged)

## New Canonical CSS Patterns — Bible Flagship Entries

### Share Bar (mandatory for all flagship entries)
```css
.mpw-share-bar{display:flex;flex-direction:column;gap:8px;margin-top:14px;padding-top:14px;border-top:1px solid #2a2a4a}
.mpw-share-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#666;display:block}
.mpw-share-btns{display:flex;gap:6px;width:100%}
.mpw-share-btn{display:inline-flex;align-items:center;justify-content:center;gap:5px;flex:1;height:36px;padding:0 10px;border-radius:6px;font-size:11px;font-weight:700;text-decoration:none;cursor:pointer;font-family:inherit;transition:opacity .15s;white-space:nowrap;border:none;min-width:0}
.share-copy{background:#f5a623;color:#000}
.share-x{background:#000;color:#fff!important}
.share-reddit{background:#ff4500;color:#fff}
```

HTML structure (label must be own row, buttons in .mpw-share-btns):
```html
<div class="mpw-share-bar" style="margin-top:20px">
  <span class="mpw-share-label">LABEL</span>
  <div class="mpw-share-btns">
    <button class="mpw-share-btn share-copy" onclick="...">Copy Link</button>
    <a href="https://x.com/intent/tweet?..." class="mpw-share-btn share-x">[X SVG]Share on X</a>
    <a href="https://www.reddit.com/submit?..." class="mpw-share-btn share-reddit">[Reddit SVG]Reddit</a>
  </div>
</div>
```

### Genre Table — CSS Grid (replaces HTML table permanently)
HTML tables produce uncontrollable row heights on mobile regardless of `table-layout:fixed`. CSS grid with card layout on mobile is the only reliable pattern. See BIBLE handoff for full CSS.

```css
.genre-grid-wrap{margin:16px 0;background:#13132a;border:1px solid #2a2a4a;border-radius:10px;overflow:hidden}
.gthead{display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr 1fr 0.8fr 1fr;background:#1a0800}
.gtrow{border-bottom:1px solid #1a1a3a;display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr 1fr 0.8fr 1fr;align-items:start}
.gtnote{grid-column:1/-1;font-size:11px;color:#666;font-style:italic;background:#0f0f22}
.gtlbl{display:none}
@media(max-width:768px){
  .gthead{display:none}
  .gtrow{display:flex;flex-direction:column;padding:12px;gap:4px;border-bottom:1px solid #2a2a4a}
  .gtgenre{font-size:14px;font-weight:800;color:#f5a623;margin-bottom:4px}
  .gtlbl{display:inline;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:#555;margin-right:6px}
  .gtnote{border-top:1px solid #1a1a3a;margin-top:6px;background:none}
}
```

### Fix-It Accordion Pattern
8 symptoms. Each symptom button has its own `.fixit-result` div directly beneath it. Result drops in place — no page jump. Chevron `id="fic-{key}"` rotates on open.

```javascript
window.fixitSelect = function(btn, key){
  var panel = document.getElementById('fix-'+key);
  var chevron = document.getElementById('fic-'+key);
  var isOpen = panel && panel.style.display !== 'none';
  document.querySelectorAll('.fixit-symptom').forEach(function(b){ b.classList.remove('active'); });
  document.querySelectorAll('.fixit-result').forEach(function(p){ if(p) p.style.display='none'; });
  document.querySelectorAll('.fixit-chevron').forEach(function(c){ if(c) c.style.transform=''; });
  if(!isOpen && panel){
    btn.classList.add('active');
    panel.style.display='block';
    if(chevron) chevron.style.transform='rotate(180deg)';
  }
};
```

### Entry Nav — IntersectionObserver (Bible flagship standard)
```javascript
(function(){
  var nl=document.querySelectorAll('.entry-nav-inner a');
  var s=Array.from(document.querySelectorAll('.entry-section[id]'));
  var last=null;
  function getId(){
    var o=148,b=null;
    for(var i=0;i<s.length;i++){var r=s[i].getBoundingClientRect();if(r.top<=o&&r.bottom>o){b=s[i].id;break;}}
    if(!b){for(var j=s.length-1;j>=0;j--){if(s[j].getBoundingClientRect().top<=o){b=s[j].id;break;}}}
    return b||(s[0]&&s[0].id);
  }
  function update(){
    var id=getId();if(!id||id===last)return;last=id;
    nl.forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+id);});
    var al=document.querySelector('.entry-nav-inner a.active');
    if(al)al.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});
  }
  window.addEventListener('scroll',update,{passive:true});
  window.addEventListener('touchmove',update,{passive:true});
  update();
})();
```

## Gold Standard Update
- **Structure + SEO gold standard:** `bible/compression.html` v1.2 — LOCKED S78
- **Prose + content gold standard:** `bible/reverb.html` v1.6 — LOCKED S55
- Both must be studied before writing any new flagship entry

## Session 78 Commits Affecting Tech
| SHA | Change |
|-----|--------|
| `7bcc86f7` | Share bar CSS + Fix-It accordion + entry nav IntersectionObserver pattern established |
| `9de422e2` | `.mpw-share-bar` flex-direction:column + `.mpw-share-btns` full-width row — global pattern locked |
| `d1314123` | Genre table replaced with CSS grid — HTML table pattern deprecated for Bible entries |

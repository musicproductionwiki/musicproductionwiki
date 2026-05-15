# MusicProductionWiki.com — CORE Handoff
*Updated: May 15, 2026 (SESSION 29B) · 526 articles + 202 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

All 6 handoff modules must be reproduced in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context.

Module files (all in repo root):
- MPW-HANDOFF-CORE.md — this file
- MPW-HANDOFF-SCRIPTS.md — all script documentation
- MPW-HANDOFF-CONTENT.md — article standards, word counts, batch pipeline
- MPW-HANDOFF-BIBLE.md — Producer's Bible architecture + v4.0 spec
- MPW-HANDOFF-ARTICLES.md — pointer file (live catalog = MPW-CATALOG.md)
- MPW-HANDOFF-TECH.md — nav architecture, gold standard fingerprints, infrastructure

---

# ⛔ RULE 2 — SESSION START IS A HARD GATE

Run `python mpw_session_start.py` first. It fetches MPW-HANDOFF-CORE.md from GitHub, counts articles + Bible entries via Trees API, prints 3 recent commits, and lists available module files.

Do not take any action until you have stated back:
1. Current article count (from mpw_session_start.py output)
2. Current Bible entry count (check MPW-CATALOG.md in repo)
3. P0 priority from Section 2 of this file
4. Every NEVER rule from Rule 3 added in the last 2 sessions

If you cannot recite all four, you have not read this document. Stop and re-read it.

---

# ⛔ RULE 3 — NEVER RULES

| Rule | Detail |
| --- | --- |
| NEVER enable Netlify Pretty URLs | Breaks site |
| NEVER zip over 200KB | Cloudflare intercepts — save via Notepad → Save As → All Files |
| NEVER write partial batches | All articles first, commit once |
| NEVER update index.html for rewrites | Only new filenames need index updates |
| NEVER propose topics without duplicate check | Check MPW-CATALOG.md |
| NEVER deliver under minimum word count | See MPW-HANDOFF-CONTENT.md |
| NEVER use Updated May 2025 | Always 2026 |
| NEVER truncate any handoff module | Full reproduction required |
| NEVER use GitHub web editor for CSS or JS | Silent corruption — always fetch via API → edit → commit via API PUT |
| NEVER start normalisation before gold standard confirmed clean | Gold standard = suno-vs-udio.html — LOCKED |
| NEVER rewrite suno-vs-udio.html | It is the gold standard — do not touch it |
| NEVER run injection scripts blind | Test on 3 articles first |
| NEVER declare audit results reliable without visual confirmation | String matching is not sufficient |
| NEVER run batch before --test passes and article is visually confirmed live | One test article confirmed on live site before any batch |
| NEVER let Claude auto-detect category without checking the result | Always confirm [CATEGORY] line in output |
| NEVER commit an article with garbled share buttons | Must render cleanly before commit |
| NEVER change a review score between runs | Extract from existing article and lock |
| NEVER COMMIT MULTIPLE FILES INDIVIDUALLY | ALWAYS use GitHub Trees API — single commit — single Netlify deploy |
| NEVER delete local HTML files before running commit script | Files must be committed before deletion |
| NEVER tell Steve to delete files before confirming commit success | Confirm GitHub shows all files live first |
| ALWAYS warn at 75% context window | Stop immediately and warn Steve |
| ALWAYS check CSS live after every commit | Fetch /css/style.css and confirm changes present |
| ALWAYS regenerate article list from GitHub API | Never copy old list |
| ALWAYS run . .\setenv.ps1 at start of every PowerShell session | Keys clear on window close |
| ALWAYS use Trees API for multi-file scripts | 1 file = individual PUT OK. 2+ files = Trees API ONLY |
| NEVER run batches 09-13 before new category pages exist | breakdowns.html LIVE ✅ — recreations.html + vocal-autopsies.html must exist first |
| NEVER start Producer's Bible entries before entry template is approved | Gold standard entry must be confirmed first |
| NEVER use /dictionary/ as the Bible URL | URL structure is /bible/ |
| NEVER touch suno-vs-udio.html | Article gold standard — LOCKED |
| NEVER use self-contained category page nav as sitewide nav | Must use unified nav via mpw_fix_sitewide_r7.py |
| NEVER regenerate category pages without fixing Bible bar CSS first | Must be centered — copy exact CSS from index.html |
| NEVER build category pages without fetching live GitHub article slug list first | Invented slugs cause broken links |
| NEVER use text logo on any page | All pages must use SVG logo-mark |
| TREES API MANDATORY | If a script commits more than one file and does NOT use Trees API — it is WRONG |
| NEVER run a nav update script without --test on 3 articles first | Verify visually before full batch |
| NEVER assume a script produced the correct result | Always check the live page |
| NEVER build a new nav patch script when the existing one can be fixed | Avoid script pile-up |
| NEVER use JS-only dropdowns | Use CSS :focus-within |
| NEVER run the article quality audit blind | Write mpw_audit.py, run --dry-run, review CSV before acting |
| NEVER rewrite an article without first checking mpw_audit.py output | Audit tells you rewrite vs targeted fix |
| NEVER fix one thing reactively without checking what else is broken first | Reactive patching causes cascading damage |
| NEVER run a script that fetches slugs from GitHub API | Always read from slugs.txt — API hangs |
| NEVER deliver a script with Python SyntaxWarning for backslash in docstring | Use double backslash |
| NEVER revert to a commit without first confirming what that commit's state was | Always check before reverting |
| ALWAYS read slugs from C:\Users\swarn\OneDrive\Desktop\slugs.txt | Never hit GitHub API for slug list |
| NEVER push main.js or style.css changes via GitHub web editor | Silent corruption guaranteed |
| NEVER wrap commented-out JS code in /* */ if code contains */ | Use if(false){} wrapper instead |
| NEVER fetch and recommit a file without applying ALL needed fixes in same operation | Avoid accidental restores |
| NEVER guess HTML structure | Always fetch live file before writing any patch script |
| NEVER check for Bible link in footer and call it already in nav | Check specifically inside nav element |
| NEVER hardcode category page paths without running list_categories.py first | 89 category pages confirmed |
| NEVER run mpw_fix_sitewide_r7.py without --test first | Full run touches 614 files |
| NEVER guess sidebar HTML — always fetch live article first | Multiple script iterations failed otherwise |
| NEVER assume all articles use same related-card HTML format | Four different formats found |
| NEVER build new mpw_writer.py without reading MPW-HANDOFF-SCRIPTS.md | New writer must include correct sidebar and nav |
| NEVER run mpw_fix_sitewide_r7.py after homepage updated to newer nav | Always update r7 to match homepage nav first |
| NEVER use old r7 NAV_HTML in mpw_writer.py or mpw_fix_sitewide_r7.py | New homepage nav is the standard |
| NEVER assume aside is direct child of article-layout | JS fix required — baked into mpw_writer.py v3.0 |
| NEVER commit test articles without aside JS fix | Mandatory — baked into v3.0 |
| NEVER use nav-link relative paths (../) | All nav links must be absolute paths starting with / |
| NEVER guess nav-inner max-width or padding | Always fetch live confirmed-working article computed styles |
| NEVER run mpw_fix_sitewide_r7.py without retry session | Use persistent requests.Session with exponential backoff |
| NEVER write new articles without running --test first and visually confirming | mpw_writer.py v3.0 test-first always |
| ALWAYS strip mpw-nav-js script from articles | Old mpw-nav-js in main.js conflicts with new dropdown JS |
| ALWAYS strip ALL search overlay duplicates | patch() runs 20-pass removal |
| ALWAYS use absolute paths in nav links | /about.html, /categories/techniques.html, /bible/, etc. |
| ALWAYS use claude-sonnet-4-6 for new article generation | Mandatory — upgraded Session 21 |
| NEVER run multiagent batch without --dry-run first | Always dry-run then test then full run |
| NEVER run mpw_count.py using old GitHub contents API pagination | Replaced with Trees API version ✅ |
| ALWAYS use mpw_slugs.py after every batch commit | Refreshes slugs.txt from live repo |
| NEVER trust local slugs.txt as article count source | Only accurate immediately after mpw_slugs.py |
| NEVER fix title capitalisation in mpw_search_index.py as patch | Correct fix is in article <title> tags |
| NEVER include main.js on /bible/ pages | Conflicts with Bible page nav JS — crashes silently |
| NEVER write Bible page JS via Python heredoc with single-quote escaping | Use raw string r"""...""" |
| NEVER commit bible-index.json before /bible/index.html exists | Index page must exist first — RESOLVED ✅ |
| NEVER use position:absolute for dropdowns inside section with overflow:hidden | Use position:fixed with getBoundingClientRect() |
| NEVER use bible-compression.html as Bible entry gold standard | bible/eq.html is the gold standard |
| NEVER run mpw_bible_writer.py without --test first and visual confirmation | Mandatory — always test before batch |
| NEVER guess Bible entry layout CSS | Always derive from live gold standard via DevTools |
| ANTHROPIC_KEY env var is ANTHROPIC_API_KEY in setenv.ps1 | Script reads ANTHROPIC_API_KEY — also ANTHROPIC_KEY as fallback |
| PASS1_TOKENS must be 20000 for Bible entries | Lower values truncate JSON |
| NEVER run sitewide fix script with parallel blob creation | Always sequential with exponential backoff on 403s |
| ALWAYS run mpw_dead_slug_audit.py after every batch commit | Dead slugs accumulate silently |
| ALWAYS run mpw_slugs.py before every batch write AND after every batch commit | Stale slugs cause dead related-article links |
| NEVER use parallel thread fetching for GitHub Contents API in fix scripts | 15-20 threads triggers secondary rate limit — use 10 max |
| NEVER paste Python code directly into PowerShell | Save as .py file and run python script.py |
| NEVER strip entire <style> blocks when looking for CSS fingerprints | Nukes all page CSS — use append-only with !important |
| NEVER write Bible page mobile fixes that touch desktop CSS | ALL Bible mobile fixes are @media(max-width:768px) only |
| ALWAYS append mobile CSS as new <style> block — never strip-and-replace | Append-only approach is correct |
| NEVER guess live HTML structure of Bible page before writing patch | Always fetch live HTML first |
| NEVER run parallel blob creation for GitHub API | Always sequential with 403 backoff |
| NEVER assume GitHub API is reachable from Claude's environment | Session 28 — api.github.com blocked — all GitHub ops from Steve's PowerShell |
| NEVER give Steve browser console commands to paste in PowerShell | Console commands go in Chrome F12 → Console only |
| NEVER deliver fix script without verifying target string exists in live file | Multiple scripts failed due to mismatched patterns |
| NEVER build Bible writer without running verification suite first | v4.0 = 55-check suite — all must pass before delivery |
| ALWAYS verify mpw_bible_writer.py with python3 check script before delivering | Syntax check + content checks — fix any MISSING before delivery |
| NEVER include Spotify iframes in Bible entries | Always use styled green link buttons |
| Bible batch format is slug:Term:Category (colon-separated, 3 parts) | Pipe-separated format fails — colons required |
| NEVER patch Bible template incrementally across multiple iterations | One complete rewrite — audit fully — then test once |
| NEVER remove Sound Better from desktop nav | Desktop keeps it — mobile only removal via @media(max-width:768px) |
| NEVER link track examples to MPW article pages or any external page | Spotify green link buttons only — href to open.spotify.com/track/URI |
| NEVER allow producer quote to render with literal asterisks | Strip asterisks in post-processing — wrap in <blockquote class="producer-quote"> |
| NEVER allow AI to output related_terms or further_reading slugs not in live Bible index | Validate all slugs against bible-index.json before HTML build — omit invalid ones |
| NEVER run Tier 1 batch before Bible template passes full desktop AND mobile visual QA | Template is broken as of Session 29B — fix first |
| NEVER build new Bible entries before SEO head block is complete | 25 SEO items missing — canonical, OG, Twitter, Article schema, BreadcrumbList, GA4, H1, H2, keywords, alt text, share buttons |
| NEVER commit Bible page with navs not sticky | position:sticky requires correct parent overflow — verify on live page after every template change |
| NEVER commit Bible page with horizontal scroll on mobile | html,body must have overflow-x:hidden AND all child elements must be max-width:100% |
| ALWAYS audit mpw_bible_writer.py output with python audit script before delivering | Run the 55-check suite plus the new mobile/SEO checks |
| NEVER set $env:GITHUB_TOKEN or $env:ANTHROPIC_API_KEY inline in a .py file committed to GitHub | GitHub secret scanning blocks the commit — always use env vars |
| ALWAYS set both env vars at start of every PowerShell session | $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY — both required |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY

At 75% context, Claude must stop all work immediately and tell Steve:

***"⚠️ I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."***

This is not optional.

---

# ⛔ RULE 4 — CALL OUT SKIPPED STEPS IMMEDIATELY

If Claude skips a step in the session start checklist, delivers output without required deliverables, or takes action before completing the hard gate — Steve must call it out immediately.

---

# ⛔ RULE 5 — DELIVERABLES CHECKLIST

Every handoff update requires ALL of the following:
- [ ] All 6 MPW-HANDOFF-*.md modules updated in GitHub via Trees API
- [ ] MPW-CATALOG.md auto-regenerated and included in same commit
- [ ] Session log updated in MPW-HANDOFF-CORE.md (Section 21 — keep 3 most recent)
- [ ] Section 2 Priority table updated
- [ ] Section 16 Next Session Start Prompt updated
- [ ] mpw_session_start.py updated if session start logic changed

---

# 2. PRIORITY TABLE (Updated Session 29B)

| Priority | Task | Status | Detail |
|---|---|---|---|
| **P0** | Bible template ground-up rewrite | ❌ BLOCKS EVERYTHING | Full rewrite of build_html() — see Section 30 spec below |
| **P0.1** | SEO head block — 25 missing items | ❌ BLOCKS EVERYTHING | Canonical, OG, Twitter, schemas, GA4, H1, H2, keywords, alt, share buttons |
| **P0.2** | Mobile template fix | ❌ BLOCKS EVERYTHING | Nav, bible bar, hamburger, overflow, sticky positions |
| **P0.3** | Visual QA desktop + mobile before any batch | ❌ BLOCKS EVERYTHING | Must pass all checks |
| **P1** | Tier 1 batch — 50 Bible rewrites | After P0 confirmed | bible-upgrade-tier1.txt ready in mpw-scripts\ |
| **P1.1** | Sitemap regeneration + GSC resubmission | After Tier 1 batch | 202 Bible entries not yet in sitemap |
| **P1.2** | Genres page (genres.html) | After Tier 1 | Nav links to it but page doesn't exist |
| **P1.3** | netlify.toml redirect /dictionary/* → /bible/:splat | Pending | 301 redirect for old URLs |
| **P2** | Batch 09 — 100 track breakdowns | After Tier 1 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 |
| **P2.1** | Air Bible entry retry | After template fix | --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" |
| **P3** | Fix 5 articles missing og:image | mpw_fix_meta.py | Rate limited Session 27 — retry |
| **P4** | Affiliate applications | REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — Steve must do |
| **P5** | Google Workspace email | Steve action | Case 70817574 — domain-in-use conflict |
| **P6** | recreations.html category page | Before Batch 11 | Must exist before Batch 11 runs |
| **P7** | vocal-autopsies.html category page | Before Batch 12 | Must exist before Batch 12 runs |

---

# 16. NEXT SESSION START PROMPT (Session 30)

"Run python mpw_session_start.py. Then read Section 30 of CORE.md in full — it contains the complete Bible template rewrite spec. P0 is Bible template ground-up rewrite. Do NOT patch incrementally. Read the full spec, write build_html() completely from scratch including all SEO, mobile, nav, and content fixes. Run --test on compression slug. Do desktop AND mobile visual QA against the checklist in Section 30 before committing any batch."

---

# 21. SESSION LOG (3 Most Recent)

## May 15, 2026 — SESSION 29B — BIBLE TEMPLATE QA + BUG LIST

### What Was Tested
Live visual QA of musicproductionwiki.com/bible/compression on desktop (Chrome) and mobile (iPhone).

### What Works
| Item | Status |
|---|---|
| Two-pass streaming generation | ✅ Pass 1: 36 fields, Pass 2: 11 fields |
| Word count | ✅ 13,885 words |
| Nav dropdowns desktop | ✅ Articles + Gear working |
| TOC sidebar active highlighting | ✅ Amber highlight on scroll |
| Progress bar | ✅ Percentage-based |
| Back to top button | ✅ Amber, bottom right |
| Further reading links | ✅ /bible/ paths |
| Search overlay opens | ✅ ESC closes |
| Content quality | ✅ Institutional grade |
| mpw_fix_spotify.py | ✅ eq.html + compression.html patched |

### What Is Broken — Full List
| Item | Bug | Fix Required |
|---|---|---|
| Navs not sticky | position:sticky broken — parent has overflow conflict | Rewrite sticky chain: progress bar z:99999, bible bar z:300, nav z:200, entry-nav z:100 |
| TOC sidebar not sticky | Same overflow conflict | position:sticky; top:120px; align-self:start on sidebar |
| Dropdown z-index | Appears behind entry nav bar | Nav z-index must be higher than entry-nav |
| Sound Better on desktop | Accidentally removed — must restore | Keep on desktop, hide on mobile only via @media |
| Mobile nav broken | No hamburger, no dropdowns visible | Hamburger button must show <768px, desktop ul hides |
| Mobile bible bar gone | Removed entirely — needs to return | Second sticky bar below nav: "The Producer's Bible" centered, larger font, amber, no badges/CTAs |
| Producer quote asterisks | Literal *text* renders | Post-process: strip leading/trailing asterisks, wrap in styled blockquote |
| Track examples wrong | Billie Jean → Breathe, SLTS → Linkin Park, When Doves Cry → 404 | Track examples must use only confirmed Spotify URIs — no MPW article links |
| Track links 404 | Linking to MPW article pages that don't exist | Track examples: Spotify green button only, no internal links |
| Types of Compression mobile | Cut off on right side | overflow-x:auto on types-grid wrapper |
| Horizontal scroll mobile | Can scroll right revealing blank space | html,body overflow-x:hidden + all sections max-width:100% |
| SEO head | 25 items missing — see Section 30 | Complete head rewrite required |
| Social share buttons | Missing entirely | X, Reddit, Copy Link — after FAQ section |
| H1 tag | Term rendered as styled div not H1 | entry-term must be <h1> tag |
| H2 tags | Section headings not H2 | All section headings must be <h2> for SEO |
| GA4 | Missing from Bible pages | G-79VB543KCT must be in head |
| Canonical URL | Missing | <link rel="canonical" href="https://musicproductionwiki.com/bible/{slug}"> |
| Open Graph | All 5 tags missing | og:title, og:description, og:image, og:type, og:url |
| Twitter Card | All 4 tags missing | twitter:card, twitter:title, twitter:description, twitter:image |
| Article schema | Missing | JSON-LD Article with all required fields |
| BreadcrumbList schema | Missing | Home > The Producer's Bible > {Term} |
| robots meta | Missing | index, follow, max-snippet:-1 |
| keywords meta | Missing | term + category + related terms |
| Related terms 404 | Transient Shaping → 404 | Validate slugs against bible-index.json at build time |
| Citation on producer quote | Shows as * | Remove asterisks, style quote properly |

---

## May 15, 2026 — SESSION 29 — HANDOFF RESTRUCTURE + BIBLE WRITER V4.0

| Task | Result |
|---|---|
| Handoff restructure (6 modular files) | ✅ Committed — b0f1fbb |
| mpw_bible_writer.py v4.0 | ✅ Built — streaming, 55-check suite |
| mpw_fix_spotify.py | ✅ Built — patched eq.html + compression.html |
| mpw_session_start.py | ✅ Built — fetches live state |
| commit_handoff.py | ✅ Built — Trees API commit script |

## May 15, 2026 — SESSION 28 — BIBLE BATCH RUNS

| Task | Result |
|---|---|
| Bible page UI audit | ✅ 4 issues fixed |
| Batch B 20 entries | ✅ LIVE — a424aa9b |
| Batch C 179 entries | ✅ 106/179 LIVE |
| Total Bible live | 202 entries |
| Air entry | ❌ Failed JSON parse — pending retry |

---

# 30. SESSION 30 — BIBLE TEMPLATE COMPLETE REWRITE SPEC

## Ground Rules
- Do NOT patch the existing build_html(). Rewrite it completely.
- Read every item in this spec before writing a single line of code.
- After writing, run the Python audit script to verify all 55 + new SEO checks pass.
- Run --test on compression slug.
- Open live page on desktop Chrome AND mobile (use Chrome DevTools mobile emulation if no phone available).
- Do not run any batch until both pass.

## HEAD Block — Required Elements (in order)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{term} — The Producer's Bible | MusicProductionWiki.com</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{term}, {category}, music production, producer reference, {related_keywords}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="https://musicproductionwiki.com/bible/{slug}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{term} — The Producer's Bible">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="https://musicproductionwiki.com/bible/{slug}">
  <meta property="og:image" content="https://musicproductionwiki.com/images/og-bible-{slug}.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="MusicProductionWiki">
  <meta property="article:published_time" content="{pub_date}T00:00:00Z">
  <meta property="article:modified_time" content="{pub_date}T00:00:00Z">
  <meta property="article:section" content="{category}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{term} — The Producer's Bible">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="https://musicproductionwiki.com/images/og-bible-{slug}.jpg">
  <meta name="twitter:site" content="@mpwikiofficial">

  <!-- GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-79VB543KCT"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-79VB543KCT');</script>

  <!-- JSON-LD Schemas (3 separate script tags) -->
  <!-- 1. Article schema -->
  <!-- 2. FAQPage schema -->
  <!-- 3. BreadcrumbList schema -->
</head>
```

## JSON-LD — Article Schema (required fields)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{term} — The Producer's Bible",
  "description": "{meta_desc}",
  "url": "https://musicproductionwiki.com/bible/{slug}",
  "datePublished": "{pub_date}",
  "dateModified": "{pub_date}",
  "wordCount": {word_count},
  "image": "https://musicproductionwiki.com/images/og-bible-{slug}.jpg",
  "author": {"@type": "Organization", "name": "MusicProductionWiki", "url": "https://musicproductionwiki.com"},
  "publisher": {"@type": "Organization", "name": "MusicProductionWiki", "logo": {"@type": "ImageObject", "url": "https://musicproductionwiki.com/images/logo.png"}},
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://musicproductionwiki.com/bible/{slug}"},
  "about": {"@type": "Thing", "name": "{term}"},
  "isPartOf": {"@type": "WebSite", "name": "MusicProductionWiki", "url": "https://musicproductionwiki.com"}
}
```

## JSON-LD — BreadcrumbList Schema (required)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://musicproductionwiki.com"},
    {"@type": "ListItem", "position": 2, "name": "The Producer's Bible", "item": "https://musicproductionwiki.com/bible/"},
    {"@type": "ListItem", "position": 3, "name": "{term}", "item": "https://musicproductionwiki.com/bible/{slug}"}
  ]
}
```

## NAV Architecture — Desktop

Sticky chain (top to bottom, z-indexes must be in this order):
1. `#reading-progress` — position:fixed, top:0, z-index:99999, height:3px, width:0%, background:#f5a623
2. Main nav — position:sticky, top:0, z-index:500, height:60px (matches homepage exactly)
3. Entry section nav — position:sticky, top:60px, z-index:400, overflow-x:auto, scrollbar-width:none

Desktop nav HTML: Copy EXACTLY from index.html homepage nav (the one with Articles dropdown + Gear dropdown + About + Producer's Bible → + Search + Sound Better →). Bible pages are NOT on main.js — nav JS must be self-contained in the page.

"Sound Better →" button: KEEP on desktop. Remove ONLY on mobile via @media(max-width:768px).

## NAV Architecture — Mobile

At ≤768px:
- Desktop nav `<ul>` hides (`display:none`)
- Hamburger button shows (`display:flex`)
- Mobile drawer slides in from top — full list: Bible, Techniques, Reviews, Comparisons, Breakdowns, Recreations, Genres, AI Music, Music Business, DAWs, Plugins, Hardware

Bible bar on mobile:
- Sits as second sticky bar BELOW the main nav bar
- Shows ONLY on mobile (hidden on desktop via @media)
- Content: just "The Producer's Bible" — centered, amber color, slightly larger font (~15px), no badges, no CTAs, no dividers
- Height: 36px
- Background: #131000
- Border-bottom: 1px solid rgba(245,166,35,0.28)

## HTML Structure — Term Heading
The term name MUST be an `<h1>` tag for SEO. Currently it is a styled `<div>`. Change to:
```html
<h1 class="entry-term">{term}</h1>
```

## HTML Structure — Section Headings
Every section heading (Definition, How It Works, Parameters, etc.) must be `<h2>` tags, not `<div>` or `<p>`. This is required for Google to understand page structure.

## Producer Quote — Post-Processing
The AI outputs quotes wrapped in asterisks like `*quote text*`. The build_html() function must strip leading and trailing asterisks before rendering. Wrap in:
```html
<blockquote class="producer-quote">
  <p>{quote_text_with_asterisks_stripped}</p>
</blockquote>
```

## Track Examples — Links
Track examples must ONLY use Spotify green link buttons. They must NOT link to any MPW article page or any other external page. Format:
```html
<a href="https://open.spotify.com/track/{spotify_uri}" target="_blank" rel="noopener" class="spotify-link-item">
  <svg>...</svg>
  <span>Listen on Spotify</span>
</a>
```
The AI must only output verified Spotify URIs. The system prompt must be updated to explicitly state: "For track_examples, provide only the spotify_uri (track ID only, e.g. '4uLU6hMCjMI75M1A2tKUQC'). Never fabricate track-to-article links. Never link to MPW articles from track examples."

## Related Terms — Slug Validation
Before building HTML, validate all related_terms slugs and further_reading_slugs against the live bible-index.json fetched from GitHub. Remove any slug not found in the index. Never display a link to a slug that doesn't exist.

## Social Share Buttons
Place after FAQ section, before Further Reading. Three buttons:
1. Share on X: `https://twitter.com/intent/tweet?text={term}+—+The+Producer%27s+Bible&url=https://musicproductionwiki.com/bible/{slug}`
2. Share on Reddit: `https://www.reddit.com/submit?url=https://musicproductionwiki.com/bible/{slug}&title={term}+—+The+Producer%27s+Bible`
3. Copy Link: JS copies URL to clipboard, button text changes to "Copied!" for 2 seconds

## Breadcrumb Nav (visible, not just schema)
Visible breadcrumb above masthead:
```
Home > The Producer's Bible > {Term}
```

## OG Image
Use `/images/og-default.jpg` as fallback since per-entry OG images don't exist yet. Future: generate per-entry OG images. For now: `content="https://musicproductionwiki.com/images/og-default.jpg"` on all Bible pages.

## Mobile Visual QA Checklist (must pass before batch)
- [ ] No horizontal scroll — cannot drag page left or right
- [ ] Bible bar visible as second bar below nav
- [ ] Hamburger shows, tapping opens drawer with all links
- [ ] Progress bar stays within viewport
- [ ] Entry section nav scrolls horizontally, active item highlighted
- [ ] All content full width — nothing cut off on right
- [ ] TOC hidden on mobile (sidebar hidden)
- [ ] Back to top button visible after scrolling
- [ ] Search opens on tap
- [ ] No sticky nav z-index conflicts

## Desktop Visual QA Checklist (must pass before batch)
- [ ] Progress bar at top, 3px, amber
- [ ] Nav sticky at top, doesn't move on scroll
- [ ] Articles and Gear dropdowns work, appear above entry nav
- [ ] Sound Better button present in nav
- [ ] Entry section nav sticky below main nav, active item highlights amber
- [ ] TOC sidebar sticky on right, highlights current section
- [ ] Back to top visible after scrolling
- [ ] Search opens with Ctrl+K, finds Bible + Article results with badges
- [ ] Social share buttons render after FAQ
- [ ] Breadcrumb visible above masthead
- [ ] Further Reading links all go to /bible/ (not 404)
- [ ] Related terms all go to /bible/ (not 404)
- [ ] Producer quote styled as blockquote, no asterisks

---

# INFRASTRUCTURE REFERENCE

- **Repo:** github.com/musicproductionwiki/musicproductionwiki
- **GitHub Token:** YOUR_GITHUB_TOKEN_HERE (expires Aug 2, 2026)
- **Anthropic API Key:** Set via $env:ANTHROPIC_API_KEY in PowerShell — get from console.anthropic.com → API Keys
- **Netlify:** Project ID classy-haupia-be8e43 — auto-deploys on GitHub push
- **Scripts dir:** C:\Users\swarn\OneDrive\Desktop\mpw-scripts\
- **Articles dir:** C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles\
- **GA4 ID:** G-79VB543KCT
- **Newsletter:** Beehiiv — "The Producer's Briefing"
- **Contact:** mpwikiofficial@gmail.com
- **Twitter/X:** @mpwikiofficial
- **Gold standard article:** articles/suno-vs-udio.html — LOCKED, do not touch
- **Gold standard Bible entry:** bible/eq.html (v3.0) — v4.0 gold standard is bible/compression once template is fixed
- **OG default image:** /images/og-default.jpg
- **Bible URL structure:** /bible/{slug} — never /dictionary/

## GSC Data (May 15, 2026 — 3 month view)
- 301 total impressions
- 0 clicks
- 0% CTR
- 16.4 average position
- Top queries: "serum 2 vs vital" (10 imp), "logic pro vs ableton" (9 imp), "ableton live vs logic pro" (6 imp), "rode nt1 vs shure sm7b" (5 imp)
- All top queries are comparison articles — comparisons are the traffic beachhead
- Spike on May 7 (~90 impressions) — unknown cause
- Action: Fix SEO on Bible pages → submit updated sitemap → monitor

## Confirmed Live Bible Slugs (for slug validation)
compression, eq, limiting, saturation, distortion, reverb, delay, sidechain-compression, parallel-compression, multiband-compression, transient-shaping, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

## Pending Owner Actions (Steve must do — not Claude)
1. Affiliate applications: Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — REVENUE BLOCKER
2. Google Workspace email: Case 70817574 — domain-in-use conflict
3. Beehiiv newsletter: confirm embed code for Bible page newsletter widget
4. Twitter/X account: confirm @mpwikiofficial handle is live for share buttons

## Batch Files Ready to Run (after template fix)
- `bible-upgrade-tier1.txt` — 50 Tier 1 Bible rewrites — in mpw-scripts\
- `batch09.txt` — 100 track breakdowns — location TBC


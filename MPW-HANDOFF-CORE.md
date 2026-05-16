# MusicProductionWiki.com — CORE Handoff
*Updated: May 16, 2026 (SESSION 31 FINAL) · 526 articles + 202 Bible entries live*
*Modular format — 6 GitHub files replace single monolithic handoff*

---

# ⛔ RULE 1 — DOCUMENT INTEGRITY

All 6 handoff modules must be reproduced in full when updated. Never truncate. Article count must match GitHub API. Warn Steve at 75% context.

Module files (all in repo root):
- MPW-HANDOFF-CORE.md — this file
- MPW-HANDOFF-SCRIPTS.md — all script documentation
- MPW-HANDOFF-CONTENT.md — article standards, word counts, batch pipeline
- MPW-HANDOFF-BIBLE.md — Producer's Bible architecture + v5.1 spec
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
| NEVER use GitHub web editor for CSS or JS | Silent corruption — always fetch via API then edit then commit via API PUT |
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
| NEVER run batches 09-13 before new category pages exist | breakdowns.html LIVE — recreations.html + vocal-autopsies.html must exist first |
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
| NEVER run mpw_count.py using old GitHub contents API pagination | Replaced with Trees API version |
| ALWAYS use mpw_slugs.py after every batch commit | Refreshes slugs.txt from live repo |
| NEVER trust local slugs.txt as article count source | Only accurate immediately after mpw_slugs.py |
| NEVER fix title capitalisation in mpw_search_index.py as patch | Correct fix is in article title tags |
| NEVER include main.js on /bible/ pages | Conflicts with Bible page nav JS — crashes silently |
| NEVER write Bible page JS via Python heredoc with single-quote escaping | Use raw string r triple-quote |
| NEVER commit bible-index.json before /bible/index.html exists | Index page must exist first — RESOLVED |
| NEVER use position:absolute for dropdowns inside section with overflow:hidden | Use position:fixed with getBoundingClientRect() |
| NEVER use bible-compression.html as Bible entry gold standard | bible/eq.html is the v3.0 gold standard |
| NEVER run mpw_bible_writer.py without --test first and visual confirmation | Mandatory — always test before batch |
| NEVER guess Bible entry layout CSS | Always derive from live gold standard via DevTools |
| ANTHROPIC_KEY env var is ANTHROPIC_API_KEY in setenv.ps1 | Script reads ANTHROPIC_API_KEY — also ANTHROPIC_KEY as fallback |
| PASS1_TOKENS must be 20000 for Bible entries | Lower values truncate JSON |
| NEVER run sitewide fix script with parallel blob creation | Always sequential with exponential backoff on 403s |
| ALWAYS run mpw_dead_slug_audit.py after every batch commit | Dead slugs accumulate silently |
| ALWAYS run mpw_slugs.py before every batch write AND after every batch commit | Stale slugs cause dead related-article links |
| NEVER use parallel thread fetching for GitHub Contents API in fix scripts | 15-20 threads triggers secondary rate limit — use 10 max |
| NEVER paste Python code directly into PowerShell | Save as .py file and run python script.py |
| NEVER strip entire style blocks when looking for CSS fingerprints | Nukes all page CSS — use append-only with !important |
| NEVER write Bible page mobile fixes that touch desktop CSS | ALL Bible mobile fixes are @media(max-width:768px) only |
| ALWAYS append mobile CSS as new style block — never strip-and-replace | Append-only approach is correct |
| NEVER guess live HTML structure of Bible page before writing patch | Always fetch live HTML first |
| NEVER run parallel blob creation for GitHub API | Always sequential with 403 backoff |
| NEVER assume GitHub API is reachable from Claude's environment | api.github.com blocked — all GitHub ops from Steve's PowerShell |
| NEVER give Steve browser console commands to paste in PowerShell | Console commands go in Chrome F12 Console only |
| NEVER deliver fix script without verifying target string exists in live file | Multiple scripts failed due to mismatched patterns |
| NEVER build Bible writer without running verification suite first | v5.1 = 75+ check suite — all must pass before delivery |
| ALWAYS verify mpw_bible_writer.py with python3 check script before delivering | Syntax check + content checks — fix any MISSING before delivery |
| NEVER include Spotify iframes or YouTube links in Bible entries | v5.1 uses text-only track citations — Option A confirmed Session 31 |
| Bible batch format is slug:Term:Category (colon-separated, 3 parts) | Pipe-separated format fails — colons required |
| NEVER patch Bible template incrementally across multiple iterations | One complete rewrite — audit fully — then test once |
| NEVER remove Sound Better from desktop nav | Desktop keeps it — mobile only removal via @media(max-width:768px) |
| NEVER link track examples to any external page | v5.1 uses text-only track citations — no links of any kind |
| NEVER allow producer quote to render with literal asterisks | Strip asterisks in post-processing — wrap in blockquote.producer-quote |
| NEVER allow AI to output related_terms or further_reading slugs not in CONFIRMED_LIVE_SLUGS | Validate at build time — omit invalid ones silently |
| NEVER run Tier 1 batch before Bible template passes full desktop AND mobile visual QA | --test must pass and be visually confirmed first |
| NEVER commit Bible page with navs not sticky | overflow:clip on html/body — NOT overflow:hidden |
| NEVER commit Bible page with horizontal scroll on mobile | Verify in DevTools mobile emulation before batch |
| ALWAYS audit mpw_bible_writer.py output with python audit script before delivering | Run full 75+ check suite — all must pass |
| NEVER set env vars inline in .py files committed to GitHub | GitHub secret scanning blocks commit — always use env vars |
| ALWAYS set both env vars at start of every PowerShell session | $env:GITHUB_TOKEN and $env:ANTHROPIC_API_KEY — both required |
| NEVER use overflow:hidden on html/body in Bible pages | Use overflow:clip — hidden breaks position:sticky on all descendants |
| NEVER use Spotify URIs or YouTube links in v5.1 Bible entries | Track examples are text-only citations — Option A confirmed |
| NEVER invent article slugs for related-article links | Always verify against CONFIRMED_LIVE_SLUGS |
| NEVER use a progress bar on Bible pages desktop | Replaced by Bible category nav bar — progress bar mobile only |
| NEVER fabricate quotes from real producers | All quotes must come from quotes.json with verified source URL |
| NEVER add quotes to entries without tag matching against quotes.json | Pass 1.5 filters by tag — never invent quotes inline |
| NEVER build Producer Profile pages before Batch 09 exists | Option C sidebar now — Option B full profiles after Batch 09 |
| NEVER build app before 1000 Bible entries + 25000 monthly visitors | Milestone trigger — revisit then |
| NEVER use identity bar on Bible pages | Removed Session 31 — MPW slim bar + Bible bar replace it |
| NEVER use Sections label in entry nav | Removed Session 31 — pill links only no label |
| ALWAYS set scroll-margin-top on all Bible section headings | 128px desktop / 136px mobile — see Section 32 |
| NEVER use the old Bible nav stack (identity bar + main nav + entry nav) | New stack: MPW slim bar + Bible bar + entry nav — Session 31 locked |

---

# ⛔ RULE 3B — 75% CONTEXT WARNING — MANDATORY

At 75% context, Claude must stop all work immediately and tell Steve:

"I am at approximately 75% context. I will complete the current task only, then update the handoff and stop. A new session is required after this."

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

# 2. PRIORITY TABLE (Updated Session 31 Final)

| Priority | Task | Status | Detail |
|---|---|---|---|
| P0 | Build mpw_bible_writer.py v5.1 | SESSION 32 P0 | Full rewrite incorporating all Session 31 decisions — see Section 32 spec |
| P0.1 | Run --validate on v5.1 | After v5.1 built | 75+ checks must pass |
| P0.2 | Run --test compression on v5.1 | After --validate passes | Visual QA desktop + mobile |
| P0.3 | Run mpw_bible_cat_pages.py --run | After --test confirmed | 8 Bible category pages committed |
| P1 | Tier 1 batch — 50 Bible rewrites | After P0 confirmed | python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16 |
| P1.1 | Air entry retry | After Tier 1 | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" |
| P1.2 | Sitemap regeneration + GSC resubmission | After Tier 1 | 202+ Bible entries not yet in sitemap |
| P1.3 | netlify.toml redirect /dictionary/* to /bible/:splat | Pending | 301 redirect for old URLs |
| P2 | Batch 09 — 100 track breakdowns | After Tier 1 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 |
| P2.1 | Run mpw_dead_slug_audit.py | After Tier 1 commits | Find all dead related-article links |
| P3 | Fix 5 articles missing og:image | mpw_fix_meta.py | Rate limited Session 27 — retry |
| P4 | Affiliate applications | REVENUE BLOCKER | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — Steve must do |
| P5 | Google Workspace email | Steve action | Case 70817574 — domain-in-use conflict |
| P6 | recreations.html category page | Before Batch 11 | Must exist before Batch 11 runs |
| P7 | vocal-autopsies.html category page | Before Batch 12 | Must exist before Batch 12 runs |
| P8 | Producer Profile pages /producers/ | After Batch 09 | Full content pillar — Option B — see Section 32 |
| P9 | Bible subcategory pages | After 500 entries | /bible/categories/dynamics/compression/ etc |
| P10 | Mobile app PWA first then React Native | After 1000 entries + 25K monthly visitors | Milestone trigger |

---

# 16. NEXT SESSION START PROMPT (Session 32)

"Run python mpw_session_start.py. State article count, Bible entry count, P0 priority, and last 3 NEVER rules added. P0 is building mpw_bible_writer.py v5.1 — a complete rewrite incorporating all Session 31 decisions. Read Section 32 of CORE in full before writing a single line of code. The v5.1 spec is complete and locked. Build it, run --validate (75+ checks), run --test compression, do desktop + mobile visual QA against the checklist in Section 32, then run mpw_bible_cat_pages.py --run, then Tier 1 batch."

---

# 21. SESSION LOG (3 Most Recent)

## May 16, 2026 — SESSION 31 FINAL — STRATEGIC PLANNING + HANDOFF

### What Was Decided (major — all implemented in v5.1)

Nav architecture locked:
- MPW slim bar 40px top — publisher identity, muted, Articles/Gear/About links, "A MusicProductionWiki Publication" right, search, Sound Better CTA
- Bible bar 50px below — dominant amber branding, category nav, All entries right
- Entry section nav 38px third — pill links only, NO Sections label
- Progress bar: REMOVED desktop (category bar replaces it). KEPT mobile.
- Identity bar: REMOVED entirely
- scroll-margin-top: 128px desktop / 136px mobile on ALL section headings
- Anchor jump fix: section IDs must match entry nav href targets exactly

Track examples Option A confirmed:
- Text-only citations. No links. No YouTube. No Spotify.
- Format: Artist — Track Title (Year, Album). Produced by Name.

Quotes database confirmed:
- quotes.json: 318 verified quotes, 177 people — drop in mpw-scripts\
- Pass 1.5 between Pass 1 and Pass 2 — filter by tag, send max 10 to Pass 2
- Pass 2 picks 1-2, weaves naturally with attribution
- blockquote.producer-quote with cite linking to source URL
- NEVER fabricate. NEVER use quotes not in quotes.json.

13 new v5.1 features confirmed:
1. Producer Profiles sidebar — Option C quotes-driven, links to /producers/{slug} placeholder
2. The Number box — one definitive stat per entry
3. Before/After text examples — prose before/after processing
4. Common misconception block — myth + truth per entry
5. Difficulty indicator — Beginner / Intermediate / Advanced badge
6. Prerequisite chain — understand this first linked terms
7. Print/PDF export — email gated via Beehiiv modal
8. Last verified date — in entry footer
9. Speakable schema — definition + quote sections tagged
10. sameAs entity disambiguation — Wikipedia + Wikidata in Article schema
11. DAW implementation notes — tabbed: Ableton / Logic / FL Studio / Pro Tools
12. Plugin recommendations — tiered Free / Mid / Pro with affiliate placeholders
13. Genre-specific settings tables — concrete numbers per genre

Long term architecture confirmed:
- Producer Profile pages /producers/{slug} — after Batch 09 — highest value pillar not yet built
- Bible subcategory pages — after 500 entries
- Mobile app — PWA first, then React Native — after 1000 entries + 25K monthly visitors
- App pricing: Free (50 rotating) / Pro $4.99mo or $39yr / Studio $9.99mo or $79yr
- One subscription covers web + app

### What Was Built
| Deliverable | Status |
|---|---|
| quotes.json v2 | 318 quotes 177 people — delivered to Steve |
| All 6 handoff modules updated | Session 31 Final versions |
| Nav stack mockup | Approved and locked |
| v5.1 spec written | Section 32 of this file |

### Nothing Committed to GitHub This Session
Steve commits via commit_handoff.py. quotes.json manually dropped into mpw-scripts\.

---

## May 16, 2026 — SESSION 31 MORNING — HANDOFF UPDATE + VALIDATE

### What Was Done
- Uploaded all 6 handoff modules Session 30 versions
- Updated all 6 handoff modules to Session 31
- --validate confirmed 54/54 on v5.0
- --test compression confirmed live

---

## May 15, 2026 — SESSION 30 — v5.0 BIBLE WRITER REWRITE

### What Was Built
| Deliverable | Status |
|---|---|
| mpw_bible_writer.py v5.0 | Built — 54/54 validation checks |
| mpw_bible_cat_pages.py | Built — generates 8 Bible category pages |
| All 6 handoff modules | Session 30 versions delivered |

### Key v5.0 Changes
- Two-pass architecture — Pass 1 20000 tokens JSON / Pass 2 16000 tokens prose
- overflow:clip on html/body — fixed position:sticky
- 54-check validation suite
- CONFIRMED_LIVE_SLUGS dead link prevention
- Track examples used YouTube search links (superseded by Option A text-only in v5.1)

---

# 32. SESSION 32 — v5.1 BIBLE WRITER COMPLETE SPEC

## Ground Rules
- Read this entire section before writing a single line of code
- v5.1 is a complete rewrite of build_html() AND pass architecture
- Do NOT patch v5.0 incrementally — full clean rewrite
- After writing run --validate — 75+ checks must all pass
- Run --test compression — visual QA desktop + mobile — then batch

## Nav Architecture — LOCKED (approved Session 31)

Desktop sticky chain (top to bottom):
```
MPW slim bar       position:sticky  top:0    z-index:700  height:40px  background:#181818
Bible bar          position:sticky  top:40px z-index:600  height:50px  background:#0d0d0d
Entry section nav  position:sticky  top:90px z-index:400  height:38px  background:#080808
Dropdowns          z-index:99999
Reading progress   display:none on desktop
```

MPW slim bar content: SVG logo-mark + MusicProductionWiki name (left) / Articles Gear About links (muted, center-left) / "A MusicProductionWiki Publication" italic muted (right) / search icon / Sound Better CTA button

Bible bar content: diamond + "The Producer's Bible" amber (left) / vertical divider / 8 category pills center (active category highlighted amber) / "All entries right"

Entry nav: pill links for each section. NO label. Active pill highlighted amber. overflow-x:auto scrollable. scrollbar-width:none.

scroll-margin-top on ALL section heading elements:
```css
[id].entry-section { scroll-margin-top: 128px; }
@media (max-width: 768px) {
  [id].entry-section { scroll-margin-top: 136px; }
}
```

Mobile overrides:
```css
@media (max-width: 768px) {
  .bb-cats { display:none; }
  .bible-mobile-bar { display:flex; position:sticky; top:90px; z-index:300; }
  .entry-nav { top:126px; }
  #reading-progress { display:block; }
}
```

## Track Examples — Option A Text Only

No links of any kind. Format:
```html
<div class="track-examples-list">
  <div class="track-item">
    <span class="track-artist">Michael Jackson</span> —
    <span class="track-name">Billie Jean</span>
    <span class="track-meta">(1982, Thriller). Produced by Quincy Jones.</span>
    <div class="track-note">{listening_note from Pass 1}</div>
  </div>
</div>
```

## Quotes — Pass 1.5 Architecture

Between Pass 1 JSON generation and Pass 2 prose generation, script:
1. Loads quotes.json from same directory as script
2. Filters by tag overlap with entry's category tags
3. Scores by overlap count, takes top 10
4. Passes as locked context string to Pass 2 prompt

Pass 2 picks 1-2 quotes maximum and formats as:
```html
<blockquote class="producer-quote">
  <p>"Quote text."</p>
  <cite>— Person Name, Role (<a href="{url}" target="_blank" rel="noopener">{source short}</a>)</cite>
</blockquote>
```

Producer spotlight sidebar — built from same filtered quotes:
```html
<div class="producer-spotlight">
  <h3>Producers Who Master This</h3>
  <div class="ps-card">
    <div class="ps-name">{person}</div>
    <div class="ps-role">{role}</div>
    <a href="/producers/{name-slug}" class="ps-link">View Profile</a>
  </div>
</div>
```

## 13 New Features — Pass 1 JSON Fields Required

Pass 1 must return these additional fields:
- `difficulty`: "Beginner" | "Intermediate" | "Advanced"
- `prerequisites`: list of up to 3 slugs from CONFIRMED_LIVE_SLUGS
- `misconception`: {myth: str, truth: str}
- `before_after_text`: {before: str, after: str}
- `the_number`: str (the key stat e.g. "4:1")
- `the_number_label`: str (e.g. "typical ratio for drums")
- `the_number_context`: str (1-2 sentence explanation)
- `daw_implementations`: {ableton: str, logic: str, fl_studio: str, pro_tools: str}
- `plugin_recommendations`: {free: [{name, manufacturer}], mid: [...], pro: [...]}
- `genre_settings_rows`: [{genre, ratio, attack, release, threshold, notes}]
- `wikipedia_slug`: str or null (e.g. "Dynamic_range_compression")
- `wikidata_id`: str or null (e.g. "Q134556") — omit if uncertain
- `last_verified`: auto-set to current month + year at build time

## PDF Export — Email Gate

Button in entry content:
```html
<button class="pdf-export-btn" onclick="openPdfGate()">
  Download Reference Sheet
</button>
```

Modal (inline in page, hidden by default):
```html
<div id="pdf-gate-modal" class="pgm-overlay" style="display:none">
  <div class="pgm-card">
    <button class="pgm-close" onclick="closePdfGate()">x</button>
    <h3>Get the {term} Reference Sheet</h3>
    <p>Free with The Producer's Briefing — our weekly newsletter for music producers.</p>
    <input type="email" id="pgm-email" placeholder="your@email.com">
    <button class="pgm-submit" onclick="submitPdfGate()">Get My Free Sheet</button>
    <p class="pgm-fine">No spam. Unsubscribe anytime.</p>
    <p id="pgm-error" style="display:none;color:red"></p>
  </div>
</div>
```

JS flow:
1. User clicks button — modal opens
2. User enters email — clicks submit
3. JS POSTs to Beehiiv subscriptions API with email
4. On success: close modal, call window.print()
5. @media print CSS hides all nav/sidebar/footer — clean one-pager prints

Beehiiv API call (embed pub_id from Beehiiv dashboard — not a secret key):
```javascript
async function submitPdfGate() {
  const email = document.getElementById('pgm-email').value;
  if (!email) return;
  const resp = await fetch('https://api.beehiiv.com/v2/publications/PUB_ID/subscriptions', {
    method: 'POST',
    headers: {'Content-Type':'application/json','Authorization':'Bearer BEEHIIV_API_KEY'},
    body: JSON.stringify({email, reactivate_existing:true, send_welcome_email:true})
  });
  if (resp.ok) { closePdfGate(); window.print(); }
  else { document.getElementById('pgm-error').style.display='block'; }
}
```

NOTE: BEEHIIV_API_KEY placeholder — Steve replaces with real key before committing. This is a publications-only key with no read access — low risk to embed.

## sameAs Entity Disambiguation

In Article JSON-LD schema, extend the `about` field:
```json
"about": {
  "@type": "Thing",
  "name": "{term}",
  "sameAs": [
    "https://en.wikipedia.org/wiki/{wikipedia_slug}",
    "https://www.wikidata.org/wiki/{wikidata_id}"
  ]
}
```
Only include sameAs if Pass 1 returned non-null values. Never hallucinate IDs.

## Updated Validation Check Suite (75+ target)

All existing 54 checks plus:
- 'mpw-slim-bar CSS': 'mpw-slim-bar' in content
- 'bible-bar CSS': 'class="bible-bar"' in content
- 'bb-cats CSS': 'bb-cats' in content
- 'scroll-margin-top': 'scroll-margin-top' in content
- 'reading-progress mobile only': 'display:none' in content and 'reading-progress' in content
- 'track-item no href': 'track-item' in content
- 'no youtube in tracks': 'youtube.com' not in content
- 'no spotify in tracks': 'spotify.com' not in content
- 'producer-quote blockquote': 'class="producer-quote"' in content
- 'producer-spotlight': 'producer-spotlight' in content
- 'prereq-chain': 'prereq-chain' in content
- 'difficulty-badge': 'difficulty-badge' in content
- 'misconception-block': 'misconception-block' in content
- 'before-after-block': 'before-after-block' in content
- 'the-number-box': 'the-number-box' in content
- 'daw-tabs': 'daw-tabs' in content
- 'plugin-recs': 'plugin-recs' in content
- 'genre-settings-table': 'genre-settings-table' in content
- 'pdf-export-btn': 'pdf-export-btn' in content
- 'pdf-gate-modal': 'pdf-gate-modal' in content
- 'last-verified': 'last-verified' in content
- 'SpeakableSpecification': 'SpeakableSpecification' in content
- 'sameAs in schema': 'sameAs' in content
- 'load_quotes function': 'load_quotes' in content
- 'filter_quotes function': 'filter_quotes' in content
- 'no identity bar': 'bible-identity-bar' not in content
- 'no Sections label': 'Sections' + chr(0xbb) not in content

---

# INFRASTRUCTURE REFERENCE

- Repo: github.com/musicproductionwiki/musicproductionwiki
- GitHub Token: YOUR_GITHUB_TOKEN_HERE (expires Aug 2, 2026)
- Anthropic API Key: Set via $env:ANTHROPIC_API_KEY in PowerShell
- Netlify: Project ID classy-haupia-be8e43 — auto-deploys on GitHub push
- Scripts dir: C:\Users\swarn\OneDrive\Desktop\mpw-scripts\
- Articles dir: C:\Users\swarn\OneDrive\Documents\Music Production Wiki\Articles\
- GA4 ID: G-79VB543KCT
- Newsletter: Beehiiv — "The Producer's Briefing"
- Contact: mpwikiofficial@gmail.com
- Twitter/X: @mpwikiofficial
- Gold standard article: articles/suno-vs-udio.html — LOCKED do not touch
- Gold standard Bible v3.0: bible/eq.html — CONFIRMED
- Gold standard Bible v5.1: bible/compression.html — AFTER v5.1 --test confirmed and QA passes
- OG default image: /images/og-default.jpg
- Bible URL structure: /bible/{slug} — never /dictionary/
- Quotes database: mpw-scripts\quotes.json — 318 quotes, 177 people — v2

## GSC Data (May 15, 2026 — 3 month view)
- 301 total impressions / 0 clicks / 0% CTR / 16.4 average position
- Top queries: serum 2 vs vital (10), logic pro vs ableton (9), ableton live vs logic pro (6), rode nt1 vs shure sm7b (5)
- Comparisons are the traffic beachhead — position 16 to 5 = clicks start
- Action: title tag + meta description optimization on top comparison articles

## Confirmed Live Bible Slugs (CONFIRMED_LIVE_SLUGS constant in script)
compression, eq, limiting, saturation, distortion, reverb, delay, parallel-compression, multiband-compression, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq, air

EXCLUDED (confirmed 404): sidechain-compression, transient-shaping

## Pending Owner Actions
1. Affiliate applications: Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — REVENUE BLOCKER
2. Google Workspace email: Case 70817574 — domain-in-use conflict
3. Drop quotes.json v2 into mpw-scripts\ folder
4. Replace BEEHIIV_API_KEY placeholder in v5.1 before committing
5. Run v5.1 --validate then --test then QA then cat pages then Tier 1 batch

## Batch Files Ready to Run (after v5.1 template QA confirmed)
- bible-upgrade-tier1.txt — 50 Tier 1 Bible rewrites — in mpw-scripts\
- batch09.txt — 100 track breakdowns — run after Tier 1

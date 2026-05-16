# MPW-HANDOFF-CONTENT.md
*Updated: May 16, 2026 (SESSION 31)*

---

# Article Standards — LOCKED

| Category | Floor | Target / Ceiling |
| --- | --- | --- |
| Review | 2,800w | 3,150w / 3,500w |
| Comparison | 3,900w | 4,300w / 5,000w |
| Technique | 5,400w | 6,500w / 7,700w |
| Roundup | 4,700w | 5,500w / 6,500w |
| Music Business | 3,200w | 3,550w / 4,000w |
| Wiki/Reference | 4,200w | 4,500w / 5,000w |
| AI Music | 4,200w | 4,800w / 5,800w |
| Breakdown | 3,500w | 4,000w / 4,500w |
| Studio Story | 4,000w | 4,800w / 5,500w |
| Recreation | 3,800w | 4,200w / 5,000w |
| Vocal Autopsy | 3,800w | 4,200w / 5,000w |
| Budget Recreation | 2,800w | 3,000w / 3,200w |
| Bible v3.0 | 3,000w | 3,200w / 3,500w |
| Bible v5.0 | 5,500w | 6,000w / 6,500w |

Read time: calculate at 325 wpm.

---

# Required Article Components

Every article must include:
- Canonical URL (`/articles/filename.html` — never trailing-slash format)
- Open Graph + Twitter meta tags
- Article + FAQPage JSON-LD schema
- Reading progress bar
- Breadcrumb nav
- Desktop/mobile nav (mpw-nav-homepage-v1 — commit dbc09281)
- Inline SVG diagram (unique per article)
- Quick-answer box
- Structured H2/H3 hierarchy
- Comparison/verdict tables where appropriate
- 3-tier exercises (Beginner/Intermediate/Advanced) for technique articles
- 8-question FAQ matching FAQPage schema
- Related articles grid
- Sidebar with TOC and category links
- Newsletter section
- Full footer
- Aside JS fix (moves aside back into article-layout if unclosed tags caused it to escape)

---

# Content Batch Pipeline

## Completed Batches

| Batch | Content | Status |
| --- | --- | --- |
| 01-07 | Original rewrites + early new articles — 406 articles | LIVE |
| 08 | DAWs, interfaces, mics, headphones, monitors, synths, plugins, techniques, music-business — 120 articles | LIVE |
| Bible 14A | EQ + Compression rewrite | LIVE |
| Bible 14B | 20 Signal Processing entries | LIVE |
| Bible 14C | 106/179 entries (73 failed — retried) | LIVE |
| Bible Retry 1 | 64/75 failed entries | LIVE |
| Bible Retry 2 | 10/11 entries | LIVE |
| Bible air | Failed JSON parse — PENDING retry with "Air Frequency EQ" | PENDING |

## Bible Entry Count

- Total live: 202 entries
- bible-index.json: 201 entries (air may be missing)
- Pending: air entry retry after template confirmed
- Full Bible target: 1,500 entries

## Queued Batches

| Batch | Articles | Dependencies |
| --- | --- | --- |
| Bible Tier 1 | 50 rewrites | v5.0 template confirmed — READY after --test |
| 09 — breakdown | 100 | breakdowns.html ✅ LIVE — GO after Tier 1 |
| 10 — studio-story | 50 | Batch 09 committed |
| 11 — recreation | 60 | recreations.html must exist |
| 12 — vocal-autopsy | 35 | vocal-autopsies.html must exist |
| 13 — budget-recreation | 60 | Batch 11 committed |
| Bible next batches | ~1,300 remaining | v5.0 writer only — do NOT use v3.0 |

---

# 7. Pending Owner Actions

| Action | Detail | Priority |
| --- | --- | --- |
| Run mpw_bible_writer.py --test | python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing" | P0 — DO FIRST |
| Run mpw_bible_cat_pages.py --run | Generates 8 Bible category pages | P0.2 — after test confirmed |
| Run Tier 1 batch | python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-15 | P1 — after QA |
| Retry air entry | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" | P1.2 |
| Run Batch 09 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 | P2 |
| Fix 5 missing og:image | python mpw_fix_meta.py | P3 |
| Add netlify.toml redirect | /dictionary/* → /bible/:splat 301 | P1.3 |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox | HIGH — REVENUE BLOCKER |
| Google Workspace email | Case 70817574 dispute pending | URGENT |
| Lead magnet — MPW Cheat Sheet Pack | PDF — start email list growth | P2 |
| Fix aside scrollbar | aside { overflow: visible; } in style.css | LOW |
| brands.html | Build before committing nav reference | LOW |
| Skimlinks reapply | Wait 90 days from rejection | 90 days |
| Request Dreaming access | console.anthropic.com → Managed Agents → Dreaming research preview | Future |

### about.html bible bar patch one-liner

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

---

# 8. Monetisation

| Source | Status | Monthly Potential |
| --- | --- | --- |
| Skimlinks | REJECTED — reapply in 90 days | $0 now |
| Plugin Boutique | Apply directly — needs professional email | $800-3,000 |
| Amazon Associates | Apply directly | $400-1,500 |
| Loopmasters | Apply directly | $200-800 |
| Sweetwater | Apply directly | $300-900 |
| PluginFox | Apply directly | $200-600 |
| Mediavine | Need GA4 + 50K sessions | $3,000-8,000 |
| Newsletter (Beehiiv) | The Producer's Briefing — active | $500-3,000 |
| Producer's Bible Free Tier | SEO magnet — affiliate links within entries | Compounds affiliate revenue |
| Producer's Bible Paid Tier | $9/month or $79/year — trigger at 25,000 monthly /bible/ visitors | $5,000-50,000 at scale |
| Institutional Licensing | Music schools — $299/year per institution | High value |
| Tools Platform (Tier 1) | Email-gated interactive tools | Feeds paid tiers |
| Tools Platform (Tier 2) | Paid tools $9-$19 one-time | Scales with traffic |
| Tools Platform (Tier 3) | Bible Complete subscription — $9/mo or $79/yr | Recurring revenue |
| ClearCheck | Risk assessment + TruClarify referral | Highest long-term potential |

---

# 8B. GA4 + Analytics

GA4 Measurement ID: G-79VB543KCT — obtained May 8, 2026
Injected into main.js — mpw-analytics.js committed to /js/mpw-analytics.js
Also injected into all Bible entry pages via build_html() in mpw_bible_writer.py v5.0

---

# 9. Audience Ownership & Google-Proofing

Priority: Newsletter + lead magnet → YouTube → Free tool → Reddit → Discord → TikTok → Backlinks

Lead magnet: 'MPW Cheat Sheet Pack' — NEEDS TO BE BUILT — P2
Newsletter: The Producer's Briefing — hosted on Beehiiv — 'Sound better by Friday' CTA
TruClarify integration: Every music business article should funnel to TruClarify — underutilized

---

# 45. Tools Platform — Strategic Roadmap

**Milestone trigger: After 200 Bible entries + 100 Breakdowns + 100 Recreations are live.**

## Three-Tier Tool Strategy

### Tier 1 — Email Gate
BPM → Delay/Reverb Calculator, Frequency Conflict Detector, Compressor Attack/Release Calculator, Gain Staging Calculator, Key & Scale Finder, Mix Checklist, DAW Shortcut Sheets (PDF).

### Tier 2 — Paid One-Time ($9-$19)
Producer's Frequency Bible (PDF) $9, Arrangement Blueprint Generator $9, Producer's Mix Fingerprint $12, Plugin Chain Templates (PDF) $14, Genre Production Blueprint Pack (PDF) $19, Loudness Penalty Calculator $9.

### Tier 3 — Bible Complete Subscription ($9/month or $79/year)
Everything from Tier 1 and Tier 2 plus full Bible access.

## The Flagship Tool: ClearCheck
Layer 1 (Free, email gate): Risk Score + plain-English explanation.
Layer 2 (Paid $29 or $19/month): Full intelligence report + clearance request letter.
Layer 3: TruClarify handoff — qualified lead generator.

## Build Order
1. Frequency Conflict Detector
2. Arrangement Blueprint Generator
3. ClearCheck Layer 1

---

# SESSION 31 UPDATE — CONTENT STATUS

## Article Pipeline
- Live articles: 526
- Batch 09 (100 track breakdowns): NOT YET RUN — waiting for Bible Tier 1 to go first
- Batches 10-13: NOT YET RUN — blocked by category pages + template fix

## Bible Content Pipeline
- Live Bible entries: 202
- Tier 1 upgrade batch: bible-upgrade-tier1.txt — 50 entries — READY pending --test confirmation
- Air entry retry: --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency"
- Bible category pages: 8 pages NOT YET COMMITTED — run mpw_bible_cat_pages.py --run

## GSC Findings (May 15, 2026)
Top performing content by impression:
1. Comparison articles dominate — "serum 2 vs vital", "logic pro vs ableton" etc
2. All top queries are comparisons or "vs" queries
3. Average position 16.4 — just off page 1
4. 0 clicks — CTR problem, not ranking problem
5. Action: optimize title tags and meta descriptions on top comparison articles

## Content Strategy Insight
Comparisons are the traffic beachhead. Double down on:
- DAW comparisons (Logic vs Ableton variants = 29 impressions from 6 queries)
- Microphone comparisons (SM7B vs Rode NT1 variants)
- Plugin comparisons (Serum 2 vs Vital)
Getting these from position 16 to position 5 = clicks start

## Word Count Standards (unchanged)
- Reviews: 3,200–3,500w
- Comparisons: 3,300–3,500w
- Techniques: 4,000–4,200w
- Roundups: 3,500–3,800w
- Bible entries v5.0: 5,500–6,500w (floor 5,500, target 6,000, ceiling 6,500)

---

# SESSION 31 FINAL UPDATE — CONTENT DECISIONS

## Bible Entry v5.1 Word Count Standards
- Floor: 5,500 words (unchanged)
- Target: 6,000 words (unchanged)
- Ceiling: 6,500 words (unchanged)
- New content features add ~400-600 words per entry (DAW notes, genre tables, plugin recs)
- Adjust Pass 2 prompt to target 6,000 words net of new structured sections

## Track Examples — Option A (FINAL DECISION)
Text-only citations. No links of any kind. Premium reference books don't link to streams.
Format: Artist — Track Title (Year, Album). Produced by Name.
Pass 1 field `listening_guide` provides context note for each track — shown as track-note div.
3-5 tracks per entry.

## Producer Quotes — System Confirmed
318 verified quotes in quotes.json v2.
Sources: 10 books + documented interviews from Sound On Sound, Tape Op, Rolling Stone, Billboard, Resident Advisor.
Pass 1.5 filters by tag. Pass 2 picks 1-2 max.
Attribution: full name, role, source, URL.
NEVER fabricate. NEVER use quotes not in quotes.json.

## New Content Sections Per Entry (v5.1)
Each Bible entry now includes these additional sections beyond v5.0:
1. Difficulty badge — in masthead
2. Prerequisite chain — below masthead, above definition
3. The Number box — early in content, amber card
4. Before/After text — in How It Works section
5. Common misconception block — in its own section
6. DAW implementation tabs — Ableton / Logic / FL Studio / Pro Tools
7. Plugin recommendations — tiered Free / Mid / Pro
8. Genre settings table — concrete numbers
9. Producer spotlight sidebar — quotes-driven
10. Producer quote blockquote — woven into prose
11. PDF export button — email gated
12. Last verified date — in footer

## Producer Profile Pages — Content Spec (Future — after Batch 09)
URL: /producers/{slug}/
Sections:
- Hero: name, photo placeholder, role, known for
- Production philosophy (3-4 paragraphs)
- Signature gear (table: item, type, used for)
- Signature techniques (3-5 with Bible entry links)
- Notable productions (table: artist, album, year, role)
- Quotes (from quotes.json filtered by person)
- Bible entries they appear in (auto-generated from quotes.json tag matching)
- Related producers (by shared tags/genre)
Word count: 2,000-3,000 words
This is a separate content pillar from breakdowns. Breakdowns cover tracks. Profiles cover people.

## Content Pipeline Update
Batch 09 (100 breakdowns) unlocks Producer Profile pages.
Each breakdown links to the producer's profile page.
Each profile links back to all their breakdowns.
This creates a web of internal links that compounds with every new entry.

## Bible Entry Economics (v5.1)
Two passes + Pass 1.5 quote filtering = slightly more tokens per entry.
Estimated: ~40,000 tokens per entry (was ~36,000).
Per entry cost: ~$0.20.
For 1,000 entries: ~$200.

# MPW-HANDOFF-CONTENT.md
*Updated: May 19, 2026 (SESSION 41)*

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

Read time: calculate at 325 wpm.

---

# Bible Entry Word Count Standards — UPDATED SESSION 37

| Tier | Name | Total Range | Pass 2 Prose Target | Validation Floor | Validation Ceiling |
|---|---|---|---|---|---|
| 1 | Flagship | 7,000–8,000w | 4,800–5,500w | 6800 | 7800 |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w | 3800 | 5000 |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w | 1500 | 2500 |

Gold standard compression.html: 7,058 content words / 22 min read.

**IMPORTANT SESSION 37 UPDATE:**
- Tier 1 total range updated to 7,000–8,000w (was 6,800–7,800w) per Steve.
- Tier 1 prose target dropped to 4,800–5,500w (was 5,800–6,500w).
- Reason: builder adds 1,500–2,500w of structural components (tables, SVGs, DAW tabs, plugin cards, FAQ accordion, calculator, comparison callouts) on top of prose. Previous estimate of 600–1,200w was wrong.

Tier assignment rules:
- Tier 1: cornerstone terms producers Google when learning concepts — compression, EQ, reverb, limiting, saturation, gain staging, parallel compression, bus compression, ADSR, LFO, automation, mid-side, stereo imaging, LUFS, dynamic range, noise gate, chorus, flanger, phaser, reverb types, compressor topologies
- Tier 2: specific implementations of Tier 1 concepts — high-shelf EQ, VCA compressor, optical compressor, convolution reverb, parallel compression techniques, specific synthesis methods, send-return routing, clip gain, headroom
- Tier 3: narrow technical terms — dither, wordlength, DC offset, zero-latency monitoring, buffer size, clip indicator, sum-and-difference, fletcher-munson curve, jitter, anti-aliasing, oversampling

Batch file format: slug:Term:Category:Tier (4 parts, colon-separated)
Example: compression:Compression:Signal Processing:1

Tier creep prevention: validation suite enforces hard ceiling per tier. Tier 2 entries hitting 5,200 words fail validation — they either get trimmed or reclassified to Tier 1 before commit.

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
| Bible air | Failed JSON parse — PENDING retry | PENDING |

## Bible Entry Count

- Total live: 226 entries (16 v5.1 template + 210 v3.0/v4.0 template)
- bible-index.json: 210 entries (v3.0/v4.0 only — NOT yet updated for v5.1 entries)
- Pending: air entry retry after Tier 1 batch completes
- Full Bible target: 1,500 entries
- Next milestone: complete remaining 33 Tier 1 rewrites → 50 total Tier 1 live

## Queued Batches

| Batch | Articles | Dependencies |
| --- | --- | --- |
| Bible Tier 1 (remaining 33) | 33 rewrites | READY — writer + tools approved Session 39 |
| 09 — breakdown | 100 | breakdowns.html ✅ LIVE — GO after Tier 1 |
| 10 — studio-story | 50 | Batch 09 committed |
| 11 — recreation | 60 | recreations.html must exist |
| 12 — vocal-autopsy | 35 | vocal-autopsies.html must exist |
| 13 — budget-recreation | 60 | Batch 11 committed |
| Bible Tier 2 batch | ~700 entries | After Tier 1 — classify terms before running |
| Bible Tier 3 batch | ~500 entries | After Tier 2 starts |

---

# 7. Pending Owner Actions

| Action | Detail | Priority |
| --- | --- | --- |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox | HIGH — REVENUE BLOCKER |
| Run patch_live_tools_v6.py | Remove duplicate bare .t3 blocks from 15 patched entries | P0 — first thing next session |
| Run Tier 1 remaining batch | python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-19 | P1 — READY |
| Retry air entry | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" | P2.1 |
| Run Batch 09 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 | P4 — after Tier 1 |
| Fix 5 missing og:image | python mpw_fix_meta.py | P5 |
| Add netlify.toml redirect | /dictionary/* → /bible/:splat 301 | P2.3 |
| GSC Request Indexing | Open ssl-2-plus-review/ and monitors canonical URL in GSC → Request Indexing | P13 — after deploy confirmed |
| Lead magnet — MPW Cheat Sheet Pack | PDF — start email list growth | P3 — compression QR card already built as model |

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
| Tools Platform (Email gate) | Free tool + email-gated download | Feeds paid tiers — GR calculator + cheat sheet downloads already live |
| Tools Platform (Paid $9-$19) | Comprehensive reference materials | Scales with traffic |
| Tools Platform (Subscription $9/mo or $79/yr) | Bible Complete tier | Recurring revenue |
| ClearCheck | Risk assessment + TruClarify referral | Highest long-term potential |

---

# 8B. GA4 + Analytics

GA4 Measurement ID: G-79VB543KCT — obtained May 8, 2026
Injected into main.js — mpw-analytics.js committed to /js/mpw-analytics.js
Also injected into all Bible entry pages via build_html() in mpw_bible_writer.py

New GA4 events to add in Moat 2 (Session 38+):
- helpful_vote: {level: 'beginner|intermediate|advanced', slug: 'compression'}
- helpful_submit: {level: str, has_feedback: bool, slug: str}
- gate_open: {asset: 'full|quickref|genre', slug: str}
- gate_submit: {asset: str, slug: str}
- tool_interact: {tool: 'gr_calculator', slug: str}
- daw_tab_click: {daw: 'ableton|logic|fl_studio|pro_tools', slug: str}
- section_share: {section: 'genre|quickref', action: 'tweet|copy|download', slug: str}

---

# 9. Audience Ownership & Google-Proofing

Priority: Newsletter + lead magnet → YouTube → Free tool → Reddit → Discord → TikTok → Backlinks

Lead magnet: 'MPW Cheat Sheet Pack' — compression QR card and genre table are the first two assets. Build the pack PDF combining all cheat sheets once 10+ entries have downloadable assets.
Newsletter: The Producer's Briefing — hosted on Beehiiv — 'Sound better by Friday' CTA
TruClarify integration: Every music business article should funnel to TruClarify — underutilized

---

# 45. Tools Platform — Strategic Roadmap

**Milestone trigger: After gold standard template confirmed + Moats 1-3 built.**

## Tools as Moat — Architecture

Three entry points:
1. `/tools/` — standalone hub page — grid of all tools — Product Hunt submission candidate
2. `/bible/categories/tools/` — 9th Bible category — filters entries with interactive tools
3. `/tools/[slug]/` — individual tool pages when tools graduate from Bible entries

Gate strategy (LOCKED): NEVER gate the tool itself. Gate the download/save output only.
Free tool use → email capture on save/download → newsletter → Bible Complete subscription.

## Tool Priority Order

| Priority | Tool | Home | Search Volume | Status |
|---|---|---|---|---|
| 1 | GR Calculator | compression entry | Medium | LIVE ✅ |
| 2 | Delay Time Calculator | delay entry | Very High | LIVE ✅ Session 39 |
| 3 | Frequency Reference Tool | eq entry | High | LIVE ✅ Session 39 |
| 4 | LUFS Target Reference | mastering/lufs entries | High | LIVE ✅ Session 39 |
| 5 | RT60 Calculator | reverb entries | Medium | LIVE ✅ Session 39 |
| 6 | Note→Frequency Table | synthesis entries | High | LIVE ✅ Session 39 |
| 7 | ADSR Visualizer | adsr/envelope entries | Medium | LIVE ✅ Session 39 |
| 8 | Gain Staging Reference | gain-staging entry | Medium | LIVE ✅ Session 39 |
| 9 | Headroom Calculator | headroom entry | Medium | LIVE ✅ Session 39 |
| 10 | Stereo Width & M/S | stereo-imaging entry | Medium | LIVE ✅ Session 39 |
| 11 | LFO Rate Sync | lfo/modulation entries | Medium | LIVE ✅ Session 39 |
| 12 | Chord & Key Reference | music-theory entries | High | LIVE ✅ Session 39 |
| 13 | ClearCheck Layer 1 | /tools/clearcheck/ | High intent | After TruClarify spec |

## Three-Tier Tool Strategy

### Tier 1 Tools — Email Gate (Free)
BPM → Delay/Reverb Calculator, Frequency Reference, GR Calculator, Attack/Release Calculator, Gain Staging Calculator, BPM Tap Tempo, Pre-delay Calculator, Note-to-Frequency Table.

### Tier 2 Tools — Paid One-Time ($9-$19)
Producer's Frequency Bible (PDF) $9, Arrangement Blueprint Generator $9, Producer's Mix Fingerprint $12, Plugin Chain Templates (PDF) $14, Genre Production Blueprint Pack (PDF) $19, Loudness Penalty Calculator $9.

### Tier 3 — Bible Complete Subscription ($9/month or $79/year)
Everything from Tier 1 and Tier 2 plus full Bible access.

## ClearCheck — Flagship Tool
Layer 1 (Free, email gate): Risk Score + plain-English explanation of clearance complexity.
Layer 2 (Paid $29 or $19/month): Full intelligence report + clearance request letter template.
Layer 3: TruClarify handoff — qualified lead generator to Steve's clearance business.
Build trigger: separate spec session required — involves TruClarify API/intake design.

---

# SESSION 39 UPDATE — CONTENT STATUS

## Article Pipeline
- Live articles: 526 (unchanged Sessions 38 + 39)
- Batch 09 (100 track breakdowns): NOT YET RUN — waiting for Tier 1 to complete
- Batches 10-13: NOT YET RUN — blocked by category pages + template fix

## Bible Content Pipeline
- Live Bible entries: 226 (16 v5.1 + 210 v3.0/v4.0)
- Tools: all 12 built in mpw_tools_v3.py — 15 live entries confirmed working by Steve
- Remaining 33 Tier 1 entries: READY TO RUN next session
- Air entry retry: pending after Tier 1 batch completes
- Bible category pages: 8 pages — run mpw_bible_cat_pages.py --run after Tier 1 complete

## GSC Findings (May 18, 2026)
- 587 not indexed, 14 indexed
- 585 "Discovered - currently not indexed" — normal for new large sitemap submission
- 2 specific issues fixed Session 36: ssl-2-plus-review redirect + monitors canonical
- Action: Request Indexing for fixed URLs. No other action needed — 585 queue will resolve over weeks.

## Content Strategy Insight
Comparisons are the traffic beachhead. Getting from position 16 to position 5 = clicks start.
The Bible Tier 1 batch (50 entries) is the next major SEO lever — writer and tools now fully ready.

## Producer Profile Pages — Content Spec (Future — after Batch 09)
URL: /producers/{slug}/
Sections: Hero, Production philosophy, Signature gear table, Signature techniques, Notable productions table, Quotes from quotes.json, Bible entries they appear in, Related producers
Word count: 2,000-3,000 words
Build trigger: Batch 09 (100 breakdowns) complete — each breakdown links to profile

## Track Examples — Option A (FINAL DECISION — LOCKED)
Text-only citations. No links of any kind.
Format: Artist — Track Title (Year, Album). Produced by Name.
Pass 1 field `listening_guide` provides context note for each track — shown as .track-note div.
3-7 tracks per Tier 1 entry. 3-5 for Tier 2. 2-3 for Tier 3.

## Producer Quotes — System Confirmed
318 verified quotes in quotes.json v2.
Sources: 10 books + documented interviews from Sound On Sound, Tape Op, Rolling Stone, Billboard, Resident Advisor.
Pass 1.5 filters by tag. Pass 2 picks exactly 2 for Tier 1 (MANDATORY — not 1-2). 0-1 for Tier 2. 0 for Tier 3.
Attribution: full name, role, source, URL.
NEVER fabricate. NEVER use quotes not in quotes.json.
Different producers are acceptable across runs — they just must match what appears in the entry prose.
Producer spotlight now reads cite tags from rendered HTML to guarantee match.

## New Content Sections Per Tier 1 Entry (v5.1)
1. Difficulty badge — in masthead
2. Prerequisite chain — below masthead
3. Start Here learning path box — below quick answer
4. The Number box — in quick-reference section
5. Common misconception block — before definition
6. Before/After text block — own section
7. DAW implementation tabs — Ableton / Logic / FL Studio / Pro Tools
8. Plugin recommendations — tiered Free / Mid / Pro in card
9. Genre settings table — concrete numbers per genre
10. Comparison callouts — term vs 2 related terms (before Types)
11. Producer spotlight sidebar — quotes-driven, matched to entry prose
12. Producer quote blockquote — woven into prose (exactly 2 for Tier 1)
13. PDF export button — email gated (smart modal, 3 assets)
14. Last verified date — in entry footer
15. Tools section — interactive tool per entry — positioned after Quick Reference
16. Section-level share buttons — By Genre + Quick Reference + Calculator (all mpw-share-bar)
17. "Also in The Bible" — replaces Further Reading + Related Terms (consolidated)
18. Sidebar TOC with IntersectionObserver tracking — now includes Verdict link
19. Sidebar newsletter signup (.sidebar-nl)
20. Sidebar share widget (mpw-share-bar vertical column)

---

# SESSION 41 UPDATE — CONTENT STATE

## Bible Count Correction

Previous count of 226 and 210 v3.0 was wrong. Confirmed by mpw_diagnose.py:
- Total: 223 entries
- v5.1 original 16 ✅
- v5.1 Session 40 new 54 — need regen with v5.2 ❌
- v3.0/v4.0: 153 (not 210)

## Session 40 54 Entries — Content Issues (will fix via regeneration)

- Tools section at bottom instead of after Quick Reference
- Producer's Verdict weak — no mistake named, no test, no number, under 100w
- Genre table shows N/A for non-dynamics entries — wrong column headers
- Producer Spotlight shows wrong people — track producers not quote authors
- Only 2 producer quotes — v5.2 requires minimum 3
- All will be fixed by regenerating with v5.2 writer (~$13.50)

## v5.2 Writer Content Changes

- LAW 4: minimum 3 quotes (was exactly 2) — in Definition, History, and How To Use
- LAW 8 (new): verdict-lead minimum 100w, mistake in sentence 1, specific test, specific number
- Genre table: category-aware headers (Dynamics/Modulation/Frequency/Time-Based/Synthesis/Recording)
- Producer spotlight: 3 producers matching quote authors
- HowTo schema: entry-specific parameter workflow

## SEO Direction (Steve confirmed Session 41)

Central hub. Most authoritative in the industry. Future: licensing, classes, publishing middleman.
Bible entries = definitive industry reference for every term a producer searches.
Title format: [Term] — The Producer's Bible | MusicProductionWiki.com
Meta: Master [term] in music production: [key aspects] explained with track examples, genre settings, and pro techniques.

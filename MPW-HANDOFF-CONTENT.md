# MPW-HANDOFF-CONTENT.md
*Updated: May 22, 2026 (SESSION 55)*

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

Read time for articles: calculate at 325 wpm.
Read time for Bible entries: calculate at 500 wpm (updated Session 47 — confirmed by Steve).

---

# Bible Entry Word Count Standards — UPDATED SESSION 37

| Tier | Name | Total Range | Pass 2 Prose Target | Validation Floor | Validation Ceiling |
|---|---|---|---|---|---|
| 1 | Flagship | 7,000–8,000w | 4,800–5,500w | 6800 | 7800 |
| 2 | Standard | 3,800–5,000w | 3,000–3,800w | 3800 | 5000 |
| 3 | Reference | 1,500–2,500w | 1,200–1,800w | 1500 | 2500 |

Gold standard compression.html: 7,058 content words.

**IMPORTANT SESSION 37 UPDATE:**
- Tier 1 total range updated to 7,000–8,000w (was 6,800–7,800w) per Steve.
- Tier 1 prose target dropped to 4,800–5,500w (was 5,800–6,500w).
- Reason: builder adds 1,500–2,500w of structural components (tables, SVGs, DAW tabs, plugin cards, FAQ accordion, calculator, comparison callouts) on top of prose.

**IMPORTANT SESSION 47 UPDATE:**
- Bible read time: 500 wpm (confirmed by Steve). Articles remain 325 wpm.
- count_words_html() now strips non-prose blocks before counting — read time based on prose only.

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

- Total live: 223 entries (16 v5.1 original + 54 v5.1 Session 40 + 153 v3.0/v4.0)
- bible-index.json: 210 entries (v3.0/v4.0 only — NOT yet updated for v5.1/v5.2 entries)
- Pending: air entry retry after Tier 1 batch completes
- Full Bible target: 1,500 entries
- Next milestone: complete remaining 33 Tier 1 rewrites → 50 total Tier 1 live

## Queued Batches

| Batch | Articles | Dependencies |
| --- | --- | --- |
| Bible Tier 1 (remaining 33) | 33 rewrites | BLOCKED — chorus.html QA + spotlight fix |
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
| Add missing producer quotes | Add Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, etc. to quotes.json with chorus/modulation tags | P0 Session 48 |
| Confirm chorus.html QA complete | Visual QA then commit | P0 |
| Run Tier 1 remaining batch | python mpw_bible_writer.py --batch-file bible-tier1-remaining34.txt --start-date 2026-05-21 | P1 — after chorus committed |
| Run mpw_bible_cat_pages.py | python mpw_bible_cat_pages.py --run | P2 — after regen |
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
- bible_tool_use: fired when producer uses interactive tool
- bible_share: fired on share bar clicks
- bible_email_gate: fired on PDF download attempt
- pdf_download: fired on gate form submit

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
| 11 | LFO Rate Sync | lfo/chorus/flanger/phaser/tremolo/vibrato entries | Medium | LIVE ✅ Session 39 — tool JS fixed Session 46 |
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

# New Content Sections Per Tier 1 Entry (v5.2)

1. Difficulty data — in JSON-LD schema ONLY (visual badge removed from masthead Session 47)
2. Prerequisite chain — below masthead
3. Start Here learning path box — below quick answer
4. The Number box — in quick-reference section
5. Common misconception block — before definition
6. Before/After text block — own section
7. DAW implementation tabs — Ableton / Logic / FL Studio / Pro Tools
8. Plugin recommendations — MusicProductionWiki Recommends block + tiered Free / Mid / Pro card grid (Session 47 update)
9. Genre settings table — concrete numbers per genre
10. Comparison callouts — term vs 2 related terms (before Types)
11. Producer spotlight sidebar — quotes-driven, matched to entry prose (spotlight fix in progress)
12. Producer quote blockquotes — woven into prose (exactly 3 for Tier 1 — definition, history, how-to-use)
13. PDF export button — email gated (smart modal, 3 assets)
14. Last verified date — in entry footer
15. Tools section — interactive tool per entry — positioned after Quick Reference
16. Section-level share buttons — By Genre + Quick Reference + Calculator (all mpw-share-bar)
17. "Also in The Bible" — replaces Further Reading + Related Terms (consolidated)
18. Sidebar TOC with IntersectionObserver tracking — includes all 20 canonical sections
19. Sidebar newsletter signup (.sidebar-nl)
20. Sidebar share widget (mpw-share-bar vertical column)
21. Session File Breakdown — numbered amber circles, no "Step N" prefix (Session 47 update)
22. Hardware vs Plugin comparison table — inside id="plugins" section (Session 47 update)

---

# Producer Quotes — System (v5.2 Update)

380 verified quotes in quotes.json.
Sources: 10 books + documented interviews from Sound On Sound, Tape Op, Rolling Stone, Billboard, Resident Advisor.

**v5.2 quote system:**
1. Pass 1 receives full list of producer names from quotes.json — MUST pick producer_spotlight from this list
2. filter_quotes() pulls spotlight producer quotes first, then fills by tag match
3. build_pass2_prompt_t1() injects ACTUAL QUOTE TEXT verbatim for each spotlight producer + exact HTML markup
4. Pass 2 uses the injected text exactly — cannot fabricate or substitute

**REMAINING GAP (Session 48 action):**
quotes.json is missing entries for Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite. When Pass 1 would naturally pick these producers for modulation/chorus entries, the filter falls back to available quotes (Alan Moulder, Spike Stent, etc.) — creating spotlight vs quote mismatches.

Fix: add 20+ verified quotes for missing producers with appropriate tags.

---

# SEO Direction (Steve confirmed Session 41)

Central hub. Most authoritative in the industry. Future: licensing, classes, publishing middleman.
Bible entries = definitive industry reference for every term a producer searches.
Title format: [Term] — The Producer's Bible | MusicProductionWiki.com
Meta: Master [term] in music production: [key aspects] explained with track examples, genre settings, and pro techniques.

---

# 9. Audience Ownership & Google-Proofing

Priority: Newsletter + lead magnet → YouTube → Free tool → Reddit → Discord → TikTok → Backlinks

Lead magnet: 'MPW Cheat Sheet Pack' — compression QR card and genre table are the first two assets. Build the pack PDF combining all cheat sheets once 10+ entries have downloadable assets.
Newsletter: The Producer's Briefing — hosted on Beehiiv — 'Sound better by Friday' CTA
TruClarify integration: Every music business article should funnel to TruClarify — underutilized

---

# SESSION 39 UPDATE — CONTENT STATUS

## Article Pipeline
- Live articles: 526 (unchanged Sessions 38 + 39)
- Batch 09 (100 track breakdowns): NOT YET RUN — waiting for Tier 1 to complete
- Batches 10-13: NOT YET RUN — blocked by category pages + template fix

## Bible Content Pipeline
- Live Bible entries: 223 (16 v5.1 + 54 v5.1 S40 + 153 v3.0/v4.0)
- Tools: all 12 built in mpw_tools_v3.py — 15 live entries confirmed working by Steve
- Remaining 33 Tier 1 entries: BLOCKED — chorus.html QA pending
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

---

# SESSION 47 UPDATE — CONTENT CHANGES

## Bible Read Time
500 wpm confirmed by Steve (was 325 wpm). Articles remain 325 wpm.
count_words_html() strips non-prose blocks before counting for accurate read time.

## Difficulty Badge
Removed from visual masthead. Stays in JSON-LD schema. No more visual badge at top of entries.

## Plugin Section
"MusicProductionWiki Recommends" amber intro block now hardcoded before Free/Mid/Pro plugin cards.
Never "MPW Recommends." Full brand name always.

## Session File Breakdown
Numbers shown by amber circles. "Step N —" prefix stripped from step text.

## Producer Quotes — System v5.2
Pass 1 now constrained to producers in quotes.json only. Pass 2 receives actual quote text verbatim.
**Gap (Session 48 P0):** Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite — 0 quotes each in quotes.json. Add 20+ verified quotes before next chorus regen.

## New Content Sections Per Tier 1 Entry (v5.2 — updated from v5.1 list)
1. Difficulty data — JSON-LD schema ONLY (visual badge removed from masthead Session 47)
2. Prerequisite chain — below masthead
3. Start Here learning path box — below quick answer
4. The Number box — in quick-reference section
5. Common misconception block — before definition
6. Before/After text block — own section
7. DAW implementation tabs — Ableton / Logic / FL Studio / Pro Tools
8. Plugin recommendations — MusicProductionWiki Recommends block + tiered Free / Mid / Pro card grid (Session 47)
9. Genre settings table — concrete numbers per genre
10. Comparison callouts — term vs 2 related terms (before Types)
11. Producer spotlight sidebar — quotes-driven, matched to entry prose
12. Producer quote blockquotes — exactly 3 for Tier 1 (definition, history, how-to-use)
13. PDF export button — email gated (smart modal, 3 assets)
14. Last verified date — in entry footer
15. Tools section — interactive tool per entry — positioned after Quick Reference
16. Section-level share buttons — By Genre + Quick Reference + Calculator (all mpw-share-bar)
17. "Also in The Bible" — replaces Further Reading + Related Terms (consolidated)
18. Sidebar TOC with scroll+touchmove tracking — includes all canonical sections
19. Sidebar newsletter signup (.sidebar-nl)
20. Sidebar share widget (mpw-share-bar vertical column)
21. Session File Breakdown — numbered amber circles, no "Step N" prefix (Session 47)
22. Hardware vs Plugin comparison table — inside id="plugins" section (Session 47)

---

# SESSION 51 UPDATE — May 21, 2026

## reverb.html Built — New Batch Status

| Batch | Status | Notes |
|---|---|---|
| reverb.html | LOCAL — pending commit | S51 manual build — mobile QA required first |
| Bible Tier 1 (33 remaining) | BLOCKED | Waiting for reverb.html commit + v5.3 writer build |

Bible entry count after reverb.html commit: **225 live**

## New Content Standards Added S51

### History Section — Minimum Word Count (NEW)
Tier 1 entries: History section minimum **800 words**. S51 reverb.html History is ~1,700 words across 7 cards:
1. Physical Echo Chambers (1940s-50s)
2. EMT 140 Plate Reverb (1957)
3. Hardware Golden Era — Lexicon and AMS (1978-1988)
4. Spring Reverb and Guitar Amplification (1960s-present)
5. Convolution Reverb and Impulse Response Revolution (1999-2008)
6. Plugin Era and the Valhalla Standard (2009-present)
7. LUFS Era — Restraint as Aesthetic (2015-present)

This depth is required for institutional licensing credibility. Thin history (<500 words) signals a reference card, not an authoritative entry.

## New Content Sections Added in S51 (beyond v5.2 list)

23 existing sections (see v5.2 list above) PLUS:

24. Symptom Diagnostic — 7-button triage at top of entry — routes to specific sections (NEW S51)
25. Psychoacoustics block — 6-card neuroscience grid (D/R ratio, Haas effect, envelopment, etc) (NEW S51)
26. Era Translator table — 6 eras, hardware → characteristic sound → typical settings → modern plugin (NEW S51)
27. Contrast Listen — exactly 2 tracks, maximum philosophical contrast, VS separator (NEW S51)
28. Mono Compatibility Check — 6 reverb types, risk ratings (Low/Medium/High), check protocol (NEW S51)
29. Recall Sheet — contenteditable session fields, .txt download button (NEW S51)
30. Settings Fingerprint radar chart — 5-axis SVG, 8 genres, genre selector buttons (NEW S51)
31. Decision Tree — 16-node branching JS diagnostic, 6-problem preview grid (NEW S51)
32. Common Error Diagnostic — 8 clickable symptom buttons, combined fix text (NEW S51)
33. Producer DNA — 3-card in-body section per producer with philosophy + quote + signature setup (NEW S51)
34. Editorial flow guide — how-to-navigate callout at top of Definition section (NEW S51)
35. Professional Test block — in Before/After section (NEW S51)

## Pending Owner Actions (updated S51)

| Action | Detail | Priority |
|---|---|---|
| Mobile QA on reverb.html | Real device before commit — NEVER rule | P0 NOW |
| Commit reverb.html | Save → commit to bible/reverb.html | P0 |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox | HIGH — REVENUE BLOCKER |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite | P1 |
| Run Tier 1 remaining batch | After v5.3 writer locked | P2 |

---

# SESSION 52 UPDATE — May 22, 2026

## Bible Vision Confirmed

Steve confirmed S52: "Not Britannica. The definitive producer education resource. Something that truly helps and supports Beginning, Intermediate and even advanced producers."

Active teaching. Tools producers use mid-session. Producers should feel like they went somewhere after reading an entry.

## New Content Standards — S52

### Institutional Credibility (NEW)
Every T1 entry must include:
- Citation Block (APA/MLA/Chicago/Harvard — one-click copy, 120px fixed-width buttons)
- Version History block (changelog showing what was added and when)
- Last Reviewed date
- Email: team@musicproductionwiki.com for institutional licensing contact

These signal that the Bible is a maintained, peer-reviewed reference — not a blog post. This directly enables institutional licensing conversations.

### Three-Act Narrative Arc (LOCKED for T1)
Sections must serve a coherent story — not exist as independent modules.
- Act 1 — Understanding (definition → history)
- Act 2 — Application (decision-framework → before-after)
- Act 3 — Mastery (in-the-wild → faq)

### Structural Consolidation S52
- Era Translator → folded into History
- Contrast Listen → folded into In The Wild
- Mono Check → folded into Mistakes
- Recall Sheet → folded into Tools
- Psychoacoustics → folded into Definition
- Removed: Symptom Diagnostic, Red/Green Flags, "Start Here" box
- Result: 28 sections → 23 sections — cleaner narrative

## New Sections Added in S52 (beyond S51 list)

S52 additions (10 total) per entry type:

| Addition | T1 | T2 | T3 |
|---|---|---|---|
| Decision Framework (Three Questions) | ✅ mandatory | ✅ | ❌ |
| Tempo-Locked or entry-appropriate tool | ✅ mandatory | ✅ | ❌ |
| Beginner Trap section | ✅ mandatory | abbreviated | ❌ |
| Institutional Citation Block | ✅ mandatory | ✅ mandatory | ✅ mandatory |
| Version History block | ✅ mandatory | ✅ mandatory | ✅ mandatory |
| Annotated Spectrograms (In The Wild) | ✅ mandatory | if 3+ tracks | ❌ |
| Mix Translation Test | ✅ mandatory | optional | ❌ |
| Arrangement Timeline | ✅ mandatory | ❌ | ❌ |
| DNA Signal Chain Breakdown panels | ✅ mandatory | ❌ | ❌ |
| Three-act structural arc | ✅ mandatory | ✅ | ❌ |

## Batch Status End of Session 52

| Batch | Status | Notes |
|---|---|---|
| reverb.html S52 | PENDING COMMIT | reverb_v11.html — all JS clean — mobile QA required |
| Bible Tier 1 (33 remaining) | BLOCKED | v5.3 writer must be built in Session 53 |
| Batch 09-13 | QUEUED | After Tier 1 complete |

## Updated Pending Owner Actions

| Action | Detail | Priority |
|---|---|---|
| Mobile QA on reverb_v11.html | Real iPhone — NEVER rule | P0 NOW |
| Commit reverb.html | Command in HANDOFF-SCRIPTS | P0 |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — professional email now available | HIGH — REVENUE BLOCKER |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite | P1 |
| Build v5.3 writer (S53) | Back-engineer from reverb_v11.html | P1 |
| Run Tier 1 remaining 33 batch | After v5.3 writer locked | P2 |
| Run mpw_bible_cat_pages.py | After regen | P3 |
| Retry air entry | P3 |
| Run Batch 09 | After Tier 1 | P4 |

---

# SESSION 53 UPDATE — May 22, 2026

## Bible Vision — Reconfirmed S53

"The definitive producer education resource. Something that truly helps and supports Beginning, Intermediate and even advanced producers." — Steve, Session 52

Active teaching. Tools producers use mid-session. Producers should feel like they went somewhere after reading an entry. The reverb entry S53 version is the clearest embodiment of this vision to date.

## New T1 Content Standards (S53)

### Section Architecture
Beginner Trap is now section 3 in the T1 canonical order — immediately after How It Works, before Parameters. The rationale: producers need the three-mistake foundation (routing, solo levels, no HPF) before parameter numbers mean anything. Every T1 entry going forward places Beginner Trap here.

### Psychoacoustics Cards
Each psy-card requires an "→ Use this:" application sentence (amber italic, 12px). Vocabulary without mechanism is insufficient for T1.

### Practitioner Techniques Block (How To Use)
Required in T1. Three techniques minimum:
- Listen Before You Load
- Sidechain Ducking on the Reverb Return (with specs: attack 0–5ms, release one beat, ratio 4:1–8:1)
- Relevant mix-bus or secondary technique per entry type

### Emotional Register Block (Types section)
Required in T1. Six reverb types covered; adapt per entry topic (e.g., compression types get different emotional register framing).

### Plugins Section
Old three-column plugin-tier grid replaced by editorial card layout. Each plugin entry requires: name, price, manufacturer, 2–3 sentence editorial description, and affiliate-ready link with `rel="noopener sponsored"`. Transparency note required.

### Revenue / Affiliate Architecture
Plugin section links now use `rel="noopener sponsored"` on all paid plugin picks. URLs currently point to manufacturer sites. When Plugin Boutique and Sweetwater affiliate programs are approved, swap URLs only — no structural changes needed. Transparency note already in place: "affiliate links will be added when programs are live; editorial picks remain independent."

## Batch Status End of Session 53

| Batch | Status | Notes |
|---|---|---|
| reverb.html S53 | PENDING COMMIT | 324KB local — mobile QA required first |
| Bible Tier 1 (33 remaining) | BLOCKED | v5.3 writer must be built in Session 54 |
| Batch 09–13 | QUEUED | After Tier 1 complete |

## Updated Pending Owner Actions

| Action | Detail | Priority |
|---|---|---|
| Mobile QA on reverb.html | Real iPhone — NEVER rule | **P0 NOW** |
| Commit reverb.html | Claude can execute via bash API PUT after QA | P0 |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox — professional email now available | **HIGH — REVENUE BLOCKER** |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite | P2 |
| Build v5.3 writer (S54) | Back-engineer from reverb_v11.html S53 version | P1 |
| Run Tier 1 remaining 33 batch | After v5.3 writer locked | P3 |
| Run mpw_bible_cat_pages.py | After regen | P4 |
| Run Batch 09 | After Tier 1 | P5 |

---

# SESSION 54 UPDATE — May 22, 2026

## Bible Vision — Reconfirmed S54

"The definitive producer education resource. Something that truly helps and supports Beginning, Intermediate and even advanced producers." — Steve, Session 52

reverb_v16b.html is the clearest embodiment of this vision to date. Active teaching at every section. Tools producers use mid-session. Producers feel like they went somewhere after reading it.

## New T1 Content Standards (S54)

### Shimmer Reverb — Standalone Type Required
Every T1 entry covering reverb types must treat Shimmer as a standalone type with its own card and deep-dive block. The combined "Shimmer / Convolution" treatment is insufficient — they are philosophically opposite tools (myth vs documentary) and must be separated in both the types grid and Emotional Register.

### Before/After — Three Scenario Format Required
The generic two-box before/after format is retired for T1. Required format:
- Three numbered real-world scenarios (beginner, intermediate, advanced problem)
- Each scenario: symptom description, broken-state parameter table, fix parameter table, "Why it works" explanation
- Professional Test as three-column grid (three mute-test outcomes)

### Contrast Listen — Layout Standard
`cl-grid` must use `grid-template-columns:1fr auto 1fr` — never `1fr 1fr` when VS separator is a grid child. Cards must render side-by-side on desktop.

### FAQ — Differentiation Required
At least 2 of 8 FAQ questions must address content unique to this entry — arrangement-level use, streaming context, or the entry's specific advanced concepts. No more than 6 of 8 can be generic beginner routing/parameter questions.

### Schema Accuracy (NEW S54)
- wordCount in Article JSON-LD must reflect actual prose count at time of writing (±500w acceptable)
- Read time must be calculated at 500 wpm on prose-only word count (non-prose blocks stripped)
- FAQ JSON-LD must exactly match visible FAQ questions — schema and visible content must be identical
- HowTo schema steps must include specific parameter values, not generic action names

### Revenue Architecture Standards (NEW S54)
- `rel="noopener sponsored"` on paid affiliate links ONLY — never on free plugin links
- Beehiiv v3 loader script in `<head>` on all T1 entries — form ID: `a0962c52-4819-4b09-b13d-b26517b76e01`
- Attribution script in `<head>`: `https://subscribe-forms.beehiiv.com/attribution.js`
- No static email input fields — all newsletter forms must use live Beehiiv loader divs
- Transparency note required in plugin section: affiliate disclosure + editorial independence statement

### DOI Architecture (NEW S54 — implement in v5.3 writer)
- Citation block DOI field: `{{DOI}}` variable at generation time, filled at commit time
- Zenodo DOI issued immediately after each T1 entry commits
- Crossref DOI to be issued once membership approved — supersedes Zenodo DOI
- License: CC BY-NC on all DOI registrations
- APA/MLA/Chicago/Harvard citation text must include DOI when issued

### Cross-Links Standard (NEW S54)
- Minimum 1 `/articles/` link per T1 entry (verified against live slug list)
- "What to Read Next" structured learning path block required — 5–6 cards before Related entries
- Internal prereq chain: 3–4 entries maximum (don't overwhelm)
- Citation permalink button on the entry's most distinctive/citable section

## Batch Status End of Session 54

| Batch | Status | Notes |
|---|---|---|
| reverb.html S54 | PENDING COMMIT | 383.5KB local — mobile QA required first |
| Bible Tier 1 (33 remaining) | BLOCKED | v5.3 writer must be built in Session 55 |
| Batch 09–13 | QUEUED | After Tier 1 complete |

## Updated Pending Owner Actions

| Action | Detail | Priority |
|---|---|---|
| Mobile QA on reverb.html | Real iPhone — NEVER rule | **P0 NOW** |
| Commit reverb.html | Claude executes via bash after QA | P0 |
| Zenodo account setup | 10 min — issues DOI on reverb.html after commit | P2 |
| Crossref membership | $275/year — apply this week | P3 |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox | **HIGH — REVENUE BLOCKER** |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite | P4 |
| Build v5.3 writer (S55) | Back-engineer from reverb_v16b.html | P1 |
| Run Tier 1 remaining 33 batch | After v5.3 writer locked | P5 |
| Advisory board recruitment | 1–2 real named technical reviewers from network | Future |

---

# SESSION 54 ADDENDUM — CONTENT STANDARDS FOR NEW BIBLE TYPES — May 22, 2026

## New Content Type Standards

### Type 4 — Producer DNA Word Count Standards
| Section | Target |
|---|---|
| Philosophy | 300–400w |
| Signature Signal Chains (drums/bass/vocals) | 600–800w |
| Characteristic Techniques | 400–500w |
| Reference Tracks | 300–400w |
| Gear and Plugin Stack | 300–400w |
| What to Study | 200w |
| **Total** | **2,100–2,700w prose + structural** |
| **With structural components** | **3,000–4,000w** |

Read time: calculate at 500 wpm (same as Bible standard).

### Type 5 — Track Anatomy Word Count Standards
| Section | Target |
|---|---|
| Track Context | 200–300w |
| The Signal Chain | 500–700w |
| The Defining Decisions (3–5) | 400–500w |
| Timestamp Guide | 300–400w |
| What to Try (exercises) | 200–300w |
| **Total prose** | **1,600–2,200w** |
| **With structural components** | **2,500–3,500w** |

### Type 6 — Gear/Plugin Reference Word Count Standards
| Section | Target |
|---|---|
| What It Is | 200–300w |
| Every Algorithm/Mode | 400–600w |
| Every Parameter | 400–500w |
| What It Does Best / Can't Do | 200–300w |
| What to Pair It With | 200w |
| Comparison Context | 200–300w |
| **Total prose** | **1,600–2,200w** |
| **With structural components** | **2,000–3,000w** |

### Type 7 — Genre Production Bible Word Count Standards
| Section | Target |
|---|---|
| Definition and Historical Context | 400–500w |
| The Sound Architecture | 300–400w |
| Drum Programming | 400–500w |
| Bass and Low End | 300–400w |
| Melodic and Harmonic Elements | 300–400w |
| Vocal Production | 300–400w |
| The Mix Approach | 300–400w |
| Common Mistakes | 200–300w |
| **Total prose** | **2,500–3,300w** |
| **With structural components (tables, settings, track lists)** | **5,000–8,000w** |

## Digital Product Catalog — Content Requirements

### Producer Blueprint PDF ($9 each)
- One page (A4/Letter)
- Producer name + dates active
- Primary signal chain (drums, bass, vocals) in visual flow format
- Top 5 plugins with typical settings
- 3 reference tracks
- 1 signature technique with parameters
- MPW branding, URL, version date
- Generated from Producer DNA entry data
- Requires: InDesign or Canva template — build once, populate per entry

### Domain Deep-Dive PDF ($19–29 each)
- All entries in one domain compiled
- Cross-references between entries highlighted
- Domain-specific quick reference card at front
- 8 domains: Dynamics, Frequency, Time-Based, Signal Processing, Mixing, Mastering, Synthesis, Music Theory
- 64 potential SKUs (domain × depth level combinations)

### Genre Production Bible PDF ($29 compiled)
- All 20 genre entries in one document
- Genre index at front
- Cross-genre comparison tables
- BPM/key/plugin reference appendix
- The highest-volume digital product on the site

### Complete Reference Pack ($49)
- All T1/T2/T3 entries compiled
- Indexed by category, alphabetical, and difficulty
- Print-quality formatting
- Licensed for personal educational use
- Institutional license available separately ($299/institution)

## Batch Pipeline — Updated with New Content Types

| Batch | Content Type | Count | Status | Dependencies |
|---|---|---|---|---|
| Tier 1 remaining | T1 Flagship | 33 | BLOCKED | v5.3 writer |
| Genre Bible batch | Type 7 | 20 | QUEUED | Type 7 writer template |
| Producer DNA batch | Type 4 | 100 | QUEUED | Type 4 writer template |
| Plugin Reference batch | Type 6 | 150 | QUEUED | Type 6 writer template |
| Batch 09 (Track Anatomy) | Type 5 | 100 | QUEUED | Type 5 writer template + breakdowns.html LIVE |
| Batch 10 (studio-story) | Article | 50 | QUEUED | Batch 09 complete |
| Batch 11 (recreation) | Article | 60 | QUEUED | recreations.html |
| Batch 12 (vocal-autopsy) | Article | 35 | QUEUED | vocal-autopsies.html |
| Batch 13 (budget-recreation) | Article | 60 | QUEUED | Batch 11 complete |
| T2 batch | T2 Standard | 700 | FUTURE | After Tier 1 complete |
| T3 batch | T3 Reference | 500 | FUTURE | After T2 starts |

---

# SESSION 55 ADDENDUM — CONTENT — May 22, 2026

## reverb.html — Committed and Live ✅

| Item | Value |
|---|---|
| Status | LIVE — https://musicproductionwiki.com/bible/reverb |
| Commit | 53db8f4e (mobile fix — current live) |
| Version | v1.6 |
| Word count | ~16,500 words |
| Sections | 25 |
| Mobile QA | PASSED — confirmed on real iPhone |

**Updated batch pipeline:**

| Batch | Content | Status |
|---|---|---|
| reverb.html S55 | T1 Flagship | LIVE ✅ — mobile confirmed |
| Bible Tier 1 (33 remaining) | T1 Flagship | BLOCKED — v5.3 writer not yet built |
| Batch 09–13 | Articles | QUEUED — after Tier 1 |

## Bible Entry Count — End of Session 55

**Total live: 225 entries** (226 per BIBLE handoff counted reverb before it was confirmed live — 225 is the correct reconciled figure as of end of Session 55)

Breakdown:
- reverb.html v1.6: 1 (LIVE — this session)
- chorus.html v5.2: 1 (LIVE — prior session)
- v5.1 original: 15 (LIVE)
- compression: 1 (LIVE — different nav impl)
- v5.1 Session 40: 54 (LIVE — content issues — need regen)
- v3.0/v4.0 legacy: 153 (LIVE — untouched)

## Updated Pending Owner Actions

| Action | Detail | Priority |
|---|---|---|
| Zenodo account setup | 10 min — issues DOI on reverb.html | P3 |
| Crossref membership | $275/year — apply when ready | P4 |
| Affiliate applications | Plugin Boutique, Amazon, Sweetwater, Loopmasters, PluginFox | **HIGH — REVENUE BLOCKER** |
| GSC: Request Indexing | /bible/reverb — 2 min in Search Console | P1 immediate |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite | P5 |
| Advisory board recruitment | 1–2 named technical reviewers | Future |

## Viral Distribution — reverb.html Ready to Execute

reverb.html is live and production-clean. The viral distribution templates from S54 SCRIPTS addendum are ready to execute:

1. **Twitter/X thread** — Three Questions framework — 5 tweets — ready to post
2. **r/WeAreTheMusicMakers** — Beginner Trap section as body — ready to post
3. **Producer's Briefing** — Three Questions as lead story — schedule next issue
4. **RT60 calculator embed** — embed code live in every tool — share with music blogs
5. **Producer DNA entries** — when built, producers share their own entry

**Action for Steve:** Post the Twitter/X thread and Reddit post this week while reverb.html is fresh. Templates are in HANDOFF-SCRIPTS.md S54 addendum. Do not wait.


---

# SESSION 56 UPDATE — CONTENT — May 22, 2026

## Session 56 — Content State Unchanged

- Articles: **526** — no batch ran this session
- Bible entries: **225** — no new entries committed
- All session work was mpw_tools_v4.py build (rejected) and handoff writing

## Batch Pipeline — Updated

| Batch | Status | Blocker |
|---|---|---|
| Bible Tier 1 (33 remaining) | BLOCKED | mpw_tools_v4.py rebuild (Session 57) → v5.3 writer (Session 57) |
| Genre Bible (20) | QUEUED | After Tier 1 |
| Producer DNA (100) | QUEUED | Session 59+ |
| Plugin Reference (150) | QUEUED | Session 61+ |
| Batch 09 (Track Anatomy 100) | QUEUED | Session 63+ |
| Batch 10–13 | QUEUED | After Batch 09 |

## Pending Owner Actions (Unchanged)

| Action | Priority |
|---|---|
| Affiliate applications: Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox | **REVENUE BLOCKER** |
| GSC: Request Indexing for /bible/reverb | P1 — 2 min |
| Zenodo account + DOI on reverb.html | P3 |
| Add missing producer quotes (Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite) | P4 |


---

# SESSION 57/58 UPDATE — CONTENT — May 22, 2026

## Tools — Plugin Recommendation Standard (Confirmed)

As of Session 58, the canonical format for plugin recommendations in all Producer's Bible interactive tools is:

```
Free: [plugin names] | Mid: [plugin names] | Pro: [plugin names] | Key insight: [the engineering truth]
```

**Tier definitions:**
- **Free:** Free plugins that are genuinely professional-grade (not just "free alternatives"). Examples: Chow Tape Model, TDR Nova, SPAN, Klanghelm IVGI, Valhalla Supermassive
- **Mid:** $20–$200 plugins — the sweet spot for most working producers. Examples: FabFilter Pro-Q 3, Waves CLA-76, Soundtoys Decapitator, Valhalla Room
- **Pro:** $200+ hardware or flagship software. Examples: UAD hardware, Manley Variable Mu, iZotope Ozone, Antares Auto-Tune Pro
- **Key insight:** One sentence that reveals something a producer could only learn from experience — not a product name, a truth about using the tool

This format applies to ALL future Bible entries in both automated writer output and manually-coded entries.

## Tool Depth Standard — v4 Benchmark

As of Session 57/58, the minimum quality bar for any new Producer's Bible interactive tool is the v4 standard:

- Minimum 25,000 chars of rendered HTML per tool
- At least one canvas or SVG visual that responds to user input in real time
- Famous producer settings that load all parameter values in one click
- Contextual tip text that changes based on selected source/genre/calculated result
- Click-to-copy on every value a producer would enter in a DAW
- Plugin recommendations in Free/Mid/Pro/Key insight format
- Share bar: Copy Link + X + Reddit + Embed code

No tool below this standard should be added to any Bible entry.

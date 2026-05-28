# MPW-HANDOFF-CONTENT.md
*Last merged: May 26, 2026 (Session 72 — merged S55 master + S39/S41/S47/S51/S52/S53/S54/S55/S56/S57/S58/S60 appends)*

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
| reverb.html v1.6 | T1 Flagship — committed S55 | LIVE ✅ — mobile confirmed |
| chorus.html v5.2 | T1 Flagship — committed S50 | LIVE ✅ |

## Bible Entry Count (Session 72)

- Total live: **225 entries**
  - reverb.html v1.6: 1 (LIVE — committed S55)
  - chorus.html v5.2: 1 (LIVE — committed S50)
  - v5.1 original: 15 (LIVE — need regen with v5.3)
  - compression: 1 (LIVE — different nav impl — needs v5.3 regen)
  - v5.1 Session 40: 54 (LIVE — content issues — need regen with v5.3)
  - v3.0/v4.0 legacy: 153 (LIVE — untouched)
- bible-index.json: 210 entries (v3.0/v4.0 only — NOT yet updated for v5.1/v5.2 entries)
- Pending: air entry retry after Tier 1 batch completes
- Full Bible target: 1,500 entries
- Next milestone: complete remaining 33 Tier 1 rewrites → 50 total Tier 1 live

## Queued Batches

| Batch | Content Type | Count | Status | Blocker |
| --- | --- | --- | --- | --- |
| Bible Tier 1 (remaining 33) | T1 Flagship | 33 | BLOCKED | mpw_bible_writer.py updates (650wpm + nav + v5.3) |
| air entry retry | T1 Flagship | 1 | PENDING | After Tier 1 batch |
| Genre Bible | Type 7 | 20 | QUEUED | Type 7 writer template |
| Producer DNA | Type 4 | 100 | QUEUED | Type 4 writer template |
| Plugin Reference | Type 6 | 150 | QUEUED | Type 6 writer template |
| Batch 09 (Track Anatomy) | Type 5 | 100 | QUEUED | mpw_writer.py 4 pending updates + breakdowns.html LIVE |
| Batch 10 (studio-story) | Article | 50 | QUEUED | Batch 09 complete |
| Batch 11 (recreation) | Article | 60 | QUEUED | recreations.html must exist |
| Batch 12 (vocal-autopsy) | Article | 35 | QUEUED | vocal-autopsies.html must exist |
| Batch 13 (budget-recreation) | Article | 60 | QUEUED | Batch 11 complete |
| Bible Tier 2 batch | T2 Standard | ~700 | FUTURE | After Tier 1 complete |
| Bible Tier 3 batch | T3 Reference | ~500 | FUTURE | After Tier 2 starts |

---

# Pending Owner Actions (Session 72)

| Action | Detail | Priority |
| --- | --- | --- |
| Affiliate applications | Plugin Boutique, Amazon Associates, Sweetwater, Loopmasters, PluginFox | **P0 — REVENUE BLOCKER** |
| Submit sitemap to GSC | 780 URLs (36 tool URLs added S71) | P0 |
| GSC: Request Indexing | /bible/reverb — URL Inspection — 2 min | P1 |
| GSC: Request Indexing | suno-prompt-optimizer | P1 |
| GSC: Request Indexing | ai-music-rights-navigator | P1 |
| OG images for both AI tools | 1200×630px | P1 |
| Add missing producer quotes | Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite — 20+ verified quotes each with appropriate tags | P2 |
| Run mpw_bible_cat_pages.py | python mpw_bible_cat_pages.py --run | P2 — after regen |
| Retry air entry | python mpw_bible_writer.py --test --slug air-frequency-eq --term "Air Frequency EQ" --category "Frequency" | P2.1 |
| Add netlify.toml redirect | /dictionary/* → /bible/:splat 301 | P2.3 |
| Fix 5 missing og:image | python mpw_fix_meta.py | P3 |
| Lead magnet — MPW Cheat Sheet Pack | PDF — start email list growth — compression QR card already built as model | P3 |
| Zenodo account setup | Issues DOI on reverb.html — 10 min | P3 |
| Crossref membership | $275/year — apply when ready | P4 |
| Run Batch 09 | python mpw_writer.py --batch batch09.txt --start-date 2026-03-01 | P4 — after Tier 1 |
| Advisory board recruitment | 1–2 named technical reviewers from network | Future |
| Google Workspace domain dispute | Case #70817574 still open | P3 |

---

# Monetisation

| Source | Status | Monthly Potential |
| --- | --- | --- |
| Skimlinks | REJECTED — reapply in 90 days | $0 now |
| Plugin Boutique | Apply directly — PENDING | $800-3,000 |
| Amazon Associates | Apply directly — PENDING | $400-1,500 |
| Loopmasters | Apply directly — PENDING | $200-800 |
| Sweetwater | Apply directly — PENDING | $300-900 |
| PluginFox | Apply directly — PENDING | $200-600 |
| Mediavine | Need GA4 + 50K sessions | $3,000-8,000 |
| Newsletter (Beehiiv) | The Producer's Briefing — active | $500-3,000 |
| Producer's Bible Free Tier | SEO magnet — affiliate links within entries | Compounds affiliate revenue |
| Producer's Bible Paid Tier | $9/month or $79/year — trigger at 25,000 monthly /bible/ visitors | $5,000-50,000 at scale |
| Institutional Licensing | Music schools — $299/year per institution | High value |
| Tools Platform (Email gate) | Free tool + email-gated download — GR calculator + cheat sheet downloads already live | Feeds paid tiers |
| Tools Platform (Paid $9-$19) | Comprehensive reference materials | Scales with traffic |
| Tools Platform (Subscription $9/mo or $79/yr) | Bible Complete tier | Recurring revenue |
| ClearCheck | Risk assessment + TruClarify referral | Highest long-term potential |

### Affiliate Timeline (S60)

**Steve applying to all affiliate programs** — after 200+ Bible entries with all Bible writers live. The 200-entry threshold gives enough content volume to show affiliate programs a legitimate publishing operation.

Target approval timeline: Plugin Boutique (fastest — 2–5 days), Amazon Associates (1–3 days), Sweetwater (1–2 weeks), Loopmasters (3–7 days), PluginFox (3–7 days).

**Critical action before applications:** Build `mpw_affiliates.py` registry first (Session 61 P1). All 36 tools have plugin recommendations as plain text now. When approvals come in, the registry enables a single-file update across all tools.

### Revenue Opportunity — Tool Plugin Recommendations

145 slugs × 3 plugin recommendation tiers × average 2 plugins per tier = ~870 affiliate link opportunities currently sitting as plain text. This is the highest-density affiliate opportunity on the entire site.

---

# GA4 + Analytics

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

**Strategic decision (Session 60):** Tools have more leverage than entries right now.
1. Search intent is transactional — "ADSR calculator online" captures ready-to-use visitors, not just readers
2. Tools are backlink magnets — producers embed them, YouTubers link to them, educators reference them. Articles get shared once. Tools get bookmarked and re-visited.
3. Compounding surface area — one tool at `/tools/adsr-visualizer` + embedded in `/bible/adsr` + `/bible/envelope` = three indexed URLs per asset

**Implication for batch scheduling:** Tool infrastructure build takes priority over Batch 09 and remaining Tier 1 Bible batch. Once `/tools/` hub and standalone pages are live, affiliate link infrastructure is built, and email capture is in place, then article/entry batches resume.

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

Total tools live: **41** (as of Session 71)

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

## Email Capture — Pre-Delivery Checklist (S60)

The Pre-Delivery Checklist tool (Tool 24, v5c) is the highest-intent touchpoint on the site. A producer using this tool is about to release music. Email capture at the end: "Get the complete platform delivery spec card as a PDF — free, no spam." Beehiiv handles delivery. Build Session 61 alongside the tool infrastructure.

### TruClarify Integration — Pre-Delivery Checklist
Item 8 of the Sync Licensing checklist: "No uncleared samples confirmed" → add TruClarify CTA: "Not sure? TruClarify can assess your sample clearance risk before you distribute." This is the highest-value TruClarify lead the site will ever generate — a producer moments before release with a specific clearance question.

## Tool Depth Standard — v4 Benchmark (S57/58)

As of Session 57/58, the minimum quality bar for any new Producer's Bible interactive tool is the v4 standard:
- Minimum 25,000 chars of rendered HTML per tool
- At least one canvas or SVG visual that responds to user input in real time
- Famous producer settings that load all parameter values in one click
- Contextual tip text that changes based on selected source/genre/calculated result
- Click-to-copy on every value a producer would enter in a DAW
- Plugin recommendations in Free/Mid/Pro/Key insight format
- Share bar: Copy Link + X + Reddit + Embed code

No tool below this standard should be added to any Bible entry.

## SEO Strategy — Tool Pages (S60)

### Long-Tail Tool SEO (High Priority)

Standalone `/tools/[slug].html` pages target zero-competition long-tail queries:
- "gain reduction calculator for rap vocals" → `/tools/gain-reduction-calculator`
- "ADSR settings for trap 808" → `/tools/adsr-visualizer`
- "delay time calculator BPM online" → `/tools/delay-time-calculator`
- "delivery checklist music streaming" → `/tools/pre-delivery-checklist`
- "reverb settings for vocals online" → `/tools/reverb-type-selector`
- "808 tuner key compatibility" → `/tools/808-sub-bass-tuner`
- "sidechain compression settings EDM" → `/tools/sidechain-compression-designer`

Each standalone page has 300–400 words of keyword content below the tool — not just the tool itself. This is where long-tail queries get answered.

### Tool Hub SEO

`/tools/index.html` targets: "music production tools online", "free music producer tools", "music mixing calculators". Hub page with 36 internal links to tool pages is a strong hub-and-spoke SEO structure passing authority to every tool page.

## Content Pipeline — Revised Priority (S60)

| Phase | Work | Priority | Session |
|-------|------|----------|---------|
| Tool infrastructure | mpw_affiliates.py + manifest + generators | P0 | Session 61 |
| Email capture | Pre-Delivery Checklist Beehiiv integration | P0 | Session 61 |
| Tool pages live | 36 standalone pages + hub committed | P1 | Session 61 |
| Sitemap update | 37 new URLs added + submitted to GSC | P1 | Session 61 |
| Affiliate applications | Steve applies this week | P1 | This week |
| GSC analytics review | Which tools/entries are getting traction | P2 | Session 62 |
| Bible Tier 1 remaining | 33 entries — writer integration with v5 dispatch | P3 | Session 62+ |
| Batch 09 (Track Anatomy) | 100 entries — after tool infrastructure live | P4 | Session 63+ |

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
18. Sidebar TOC with scroll+touchmove tracking — includes all canonical sections
19. Sidebar newsletter signup (.sidebar-nl)
20. Sidebar share widget (mpw-share-bar vertical column)
21. Session File Breakdown — numbered amber circles, no "Step N" prefix (Session 47 update)
22. Hardware vs Plugin comparison table — inside id="plugins" section (Session 47 update)

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

## S52 New Sections — Per Entry Type Applicability

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

## S52 Structural Consolidation

- Era Translator → folded into History
- Contrast Listen → folded into In The Wild
- Mono Check → folded into Mistakes
- Recall Sheet → folded into Tools
- Psychoacoustics → folded into Definition
- Removed: Symptom Diagnostic, Red/Green Flags, "Start Here" box
- Result: 28 sections → 23 sections — cleaner narrative

---

# Bible Vision — CONFIRMED SESSION 52

Steve confirmed S52: "Not Britannica. The definitive producer education resource. Something that truly helps and supports Beginning, Intermediate and even advanced producers."

Active teaching. Tools producers use mid-session. Producers should feel like they went somewhere after reading an entry. reverb_v16b.html is the clearest embodiment of this vision to date.

---

# T1 Content Standards — Accumulated (S51–S54)

## History Section — Minimum Word Count (S51)
Tier 1 entries: History section minimum **800 words**. S51 reverb.html History is ~1,700 words across 7 cards:
1. Physical Echo Chambers (1940s-50s)
2. EMT 140 Plate Reverb (1957)
3. Hardware Golden Era — Lexicon and AMS (1978-1988)
4. Spring Reverb and Guitar Amplification (1960s-present)
5. Convolution Reverb and Impulse Response Revolution (1999-2008)
6. Plugin Era and the Valhalla Standard (2009-present)
7. LUFS Era — Restraint as Aesthetic (2015-present)

This depth is required for institutional licensing credibility. Thin history (<500 words) signals a reference card, not an authoritative entry.

## Three-Act Narrative Arc (S52 — LOCKED for T1)
Sections must serve a coherent story — not exist as independent modules.
- Act 1 — Understanding (definition → history)
- Act 2 — Application (decision-framework → before-after)
- Act 3 — Mastery (in-the-wild → faq)

## Institutional Credibility (S52)
Every T1 entry must include:
- Citation Block (APA/MLA/Chicago/Harvard — one-click copy, 120px fixed-width buttons)
- Version History block (changelog showing what was added and when)
- Last Reviewed date
- Email: team@musicproductionwiki.com for institutional licensing contact

These signal that the Bible is a maintained, peer-reviewed reference — not a blog post. This directly enables institutional licensing conversations.

## Section Architecture (S53)
Beginner Trap is now section 3 in the T1 canonical order — immediately after How It Works, before Parameters. The rationale: producers need the three-mistake foundation (routing, solo levels, no HPF) before parameter numbers mean anything. Every T1 entry going forward places Beginner Trap here.

## Psychoacoustics Cards (S53)
Each psy-card requires an "→ Use this:" application sentence (amber italic, 12px). Vocabulary without mechanism is insufficient for T1.

## Practitioner Techniques Block — How To Use (S53)
Required in T1. Three techniques minimum:
- Listen Before You Load
- Sidechain Ducking on the Reverb Return (with specs: attack 0–5ms, release one beat, ratio 4:1–8:1)
- Relevant mix-bus or secondary technique per entry type

## Emotional Register Block — Types Section (S53)
Required in T1. Six reverb types covered; adapt per entry topic (e.g., compression types get different emotional register framing).

## Plugins Section (S53)
Old three-column plugin-tier grid replaced by editorial card layout. Each plugin entry requires: name, price, manufacturer, 2–3 sentence editorial description, and affiliate-ready link with `rel="noopener sponsored"`. Transparency note required.

Plugin recommendation format (S57/58 — ALL future entries):
```
Free: [plugin names] | Mid: [plugin names] | Pro: [plugin names] | Key insight: [the engineering truth]
```
- **Free:** Genuinely professional-grade free plugins. Examples: Chow Tape Model, TDR Nova, SPAN, Klanghelm IVGI, Valhalla Supermassive
- **Mid:** $20–$200 plugins. Examples: FabFilter Pro-Q 3, Waves CLA-76, Soundtoys Decapitator, Valhalla Room
- **Pro:** $200+ hardware or flagship software. Examples: UAD hardware, Manley Variable Mu, iZotope Ozone, Antares Auto-Tune Pro
- **Key insight:** One sentence that reveals something a producer could only learn from experience — not a product name, a truth about using the tool

Never "MPW Recommends." Full brand name always: "MusicProductionWiki Recommends"

## Shimmer Reverb — Standalone Type Required (S54)
Every T1 entry covering reverb types must treat Shimmer as a standalone type with its own card and deep-dive block. The combined "Shimmer / Convolution" treatment is insufficient — they are philosophically opposite tools (myth vs documentary) and must be separated in both the types grid and Emotional Register.

## Before/After — Three Scenario Format Required (S54)
The generic two-box before/after format is retired for T1. Required format:
- Three numbered real-world scenarios (beginner, intermediate, advanced problem)
- Each scenario: symptom description, broken-state parameter table, fix parameter table, "Why it works" explanation
- Professional Test as three-column grid (three mute-test outcomes)

## Contrast Listen — Layout Standard (S54)
`cl-grid` must use `grid-template-columns:1fr auto 1fr` — never `1fr 1fr` when VS separator is a grid child. Cards must render side-by-side on desktop.

## FAQ — Differentiation Required (S54)
At least 2 of 8 FAQ questions must address content unique to this entry — arrangement-level use, streaming context, or the entry's specific advanced concepts. No more than 6 of 8 can be generic beginner routing/parameter questions.

## Schema Accuracy (S54)
- wordCount in Article JSON-LD must reflect actual prose count at time of writing (±500w acceptable)
- Read time must be calculated at 500 wpm on prose-only word count (non-prose blocks stripped)
- FAQ JSON-LD must exactly match visible FAQ questions — schema and visible content must be identical
- HowTo schema steps must include specific parameter values, not generic action names

## Revenue Architecture Standards (S54)
- `rel="noopener sponsored"` on paid affiliate links ONLY — never on free plugin links
- Beehiiv v3 loader script in `<head>` on all T1 entries — form ID: `a0962c52-4819-4b09-b13d-b26517b76e01`
- Attribution script in `<head>`: `https://subscribe-forms.beehiiv.com/attribution.js`
- No static email input fields — all newsletter forms must use live Beehiiv loader divs
- Transparency note required in plugin section: affiliate disclosure + editorial independence statement
- When Plugin Boutique and Sweetwater affiliate programs are approved, swap URLs only — no structural changes needed

## DOI Architecture (S54 — implement in v5.3 writer)
- Citation block DOI field: `{{DOI}}` variable at generation time, filled at commit time
- Zenodo DOI issued immediately after each T1 entry commits
- Crossref DOI to be issued once membership approved — supersedes Zenodo DOI
- License: CC BY-NC on all DOI registrations
- APA/MLA/Chicago/Harvard citation text must include DOI when issued

## Cross-Links Standard (S54)
- Minimum 1 `/articles/` link per T1 entry (verified against live slug list)
- "What to Read Next" structured learning path block required — 5–6 cards before Related entries
- Internal prereq chain: 3–4 entries maximum (don't overwhelm)
- Citation permalink button on the entry's most distinctive/citable section

---

# Track Examples — Option A (FINAL DECISION — LOCKED)
Text-only citations. No links of any kind.
Format: Artist — Track Title (Year, Album). Produced by Name.
Pass 1 field `listening_guide` provides context note for each track — shown as .track-note div.
3-7 tracks per Tier 1 entry. 3-5 for Tier 2. 2-3 for Tier 3.

---

# Producer Quotes — System (v5.2)

380 verified quotes in quotes.json.
Sources: 10 books + documented interviews from Sound On Sound, Tape Op, Rolling Stone, Billboard, Resident Advisor.

**v5.2 quote system:**
1. Pass 1 receives full list of producer names from quotes.json — MUST pick producer_spotlight from this list
2. filter_quotes() pulls spotlight producer quotes first, then fills by tag match
3. build_pass2_prompt_t1() injects ACTUAL QUOTE TEXT verbatim for each spotlight producer + exact HTML markup
4. Pass 2 uses the injected text exactly — cannot fabricate or substitute
5. Minimum 3 quotes per T1 entry (LAW 4 — in Definition, History, and How To Use)

**v5.2 Writer Content Changes (S41):**
- LAW 4: minimum 3 quotes (was exactly 2) — in Definition, History, and How To Use
- LAW 8 (new): verdict-lead minimum 100w, mistake in sentence 1, specific test, specific number
- Genre table: category-aware headers (Dynamics/Modulation/Frequency/Time-Based/Synthesis/Recording)
- Producer spotlight: 3 producers matching quote authors
- HowTo schema: entry-specific parameter workflow

**REMAINING GAP (P2):**
quotes.json is missing entries for Kevin Parker, Robin Guthrie, Andy Summers, Brian Eno, Tony Visconti, Steve Lillywhite. When Pass 1 would naturally pick these producers for modulation/chorus entries, the filter falls back to available quotes (Alan Moulder, Spike Stent, etc.) — creating spotlight vs quote mismatches.
Fix: add 20+ verified quotes for missing producers with appropriate tags.

---

# SEO Direction (Steve confirmed Session 41)

Central hub. Most authoritative in the industry. Future: licensing, classes, publishing middleman.
Bible entries = definitive industry reference for every term a producer searches.
Title format: [Term] — The Producer's Bible | MusicProductionWiki.com
Meta: Master [term] in music production: [key aspects] explained with track examples, genre settings, and pro techniques.

### GSC Top Queries — Optimize After Bible Tier 1

Position ~16 on these comparison queries — optimize title/meta to improve CTR:
- serum 2 vs vital
- logic pro vs ableton
- ableton live vs logic pro
- rode nt1 vs shure sm7b

Action: fetch these articles and update title tags + meta descriptions to better match search intent. One session can handle all 4. Schedule after Bible Tier 1 batch.

---

# Audience Ownership & Google-Proofing

Priority: Newsletter + lead magnet → YouTube → Free tool → Reddit → Discord → TikTok → Backlinks

Lead magnet: 'MPW Cheat Sheet Pack' — compression QR card and genre table are the first two assets. Build the pack PDF combining all cheat sheets once 10+ entries have downloadable assets.
Newsletter: The Producer's Briefing — hosted on Beehiiv — 'Sound better by Friday' CTA
TruClarify integration: Every music business article should funnel to TruClarify — underutilized

### Viral Distribution — reverb.html (Ready to Execute)

reverb.html is live and production-clean. Templates from S54 SCRIPTS addendum are ready:

1. **Twitter/X thread** — Three Questions framework — 5 tweets — ready to post
2. **r/WeAreTheMusicMakers** — Beginner Trap section as body — ready to post
3. **Producer's Briefing** — Three Questions as lead story — schedule next issue
4. **RT60 calculator embed** — embed code live in every tool — share with music blogs
5. **Producer DNA entries** — when built, producers share their own entry

**Action for Steve:** Post the Twitter/X thread and Reddit post this week while reverb.html is fresh. Templates are in HANDOFF-SCRIPTS.md S54 addendum. Do not wait.

---

# New Content Type Standards (S54 Addendum)

## Type 4 — Producer DNA Word Count Standards
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

## Type 5 — Track Anatomy Word Count Standards
| Section | Target |
|---|---|
| Track Context | 200–300w |
| The Signal Chain | 500–700w |
| The Defining Decisions (3–5) | 400–500w |
| Timestamp Guide | 300–400w |
| What to Try (exercises) | 200–300w |
| **Total prose** | **1,600–2,200w** |
| **With structural components** | **2,500–3,500w** |

## Type 6 — Gear/Plugin Reference Word Count Standards
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

## Type 7 — Genre Production Bible Word Count Standards
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

---

# Digital Product Catalog — Content Requirements (S54)

## Producer Blueprint PDF ($9 each)
- One page (A4/Letter)
- Producer name + dates active
- Primary signal chain (drums, bass, vocals) in visual flow format
- Top 5 plugins with typical settings
- 3 reference tracks
- 1 signature technique with parameters
- MPW branding, URL, version date
- Generated from Producer DNA entry data
- Requires: InDesign or Canva template — build once, populate per entry

## Domain Deep-Dive PDF ($19–29 each)
- All entries in one domain compiled
- Cross-references between entries highlighted
- Domain-specific quick reference card at front
- 8 domains: Dynamics, Frequency, Time-Based, Signal Processing, Mixing, Mastering, Synthesis, Music Theory
- 64 potential SKUs (domain × depth level combinations)

## Genre Production Bible PDF ($29 compiled)
- All 20 genre entries in one document
- Genre index at front
- Cross-genre comparison tables
- BPM/key/plugin reference appendix
- The highest-volume digital product on the site

## Complete Reference Pack ($49)
- All T1/T2/T3 entries compiled
- Indexed by category, alphabetical, and difficulty
- Print-quality formatting
- Licensed for personal educational use
- Institutional license available separately ($299/institution)

## Batch Pipeline — Updated with New Content Types (S54)

| Batch | Content Type | Count | Status | Dependencies |
|---|---|---|---|---|
| Tier 1 remaining | T1 Flagship | 33 | BLOCKED | mpw_bible_writer.py updates (650wpm + nav + v5.3) |
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

# reverb.html — Committed and Live ✅ (S55)

| Item | Value |
|---|---|
| Status | LIVE — https://musicproductionwiki.com/bible/reverb |
| Commit | 53db8f4e (mobile fix — current live) |
| Version | v1.6 |
| Word count | ~16,500 words |
| Sections | 25 |
| Mobile QA | PASSED — confirmed on real iPhone |

### Cross-Link Architecture — reverb.html (Confirmed Live)

Internal /bible/ links (12 unique — all verified in live repo):
automation, chorus, convolution-reverb, delay, dynamic-range, eq, gain-staging, high-pass-filter, plate-reverb, room-reverb, send-return, stereo-imaging

Internal /articles/ links (7 — all verified in live catalog):
- /articles/valhalla-room-review.html
- /articles/best-reverb-plugins.html
- /articles/how-to-use-reverb-in-a-mix.html
- /articles/how-to-use-reverb-on-drums.html
- /articles/how-to-use-reverb-on-vocals.html
- /articles/best-delay-plugins.html
- /articles/what-is-reverb-music-production.html

Prerequisite chain: EQ → Gain Staging → Send/Return → High-Pass Filter

### Session 52 — JS Bug Fixes (permanently resolved in writer)
1. Unescaped possessives (party's, laptop's) — word-boundary scanner added
2. Em-dash and fraction unicode in JS strings — unicode escape fix added
3. Literal newline in single-quoted string value — string cleaner added
4. Multiline fixer corrupted regex literal — regex exclusion added
5. Stale browser download — NEVER rule added


---

# ⛔ SESSION 78 UPDATE — May 27, 2026

## State at End of Session 78
- Articles: **526** live (unchanged — no article batch this session)
- Bible entries: **223+** live
- No new articles written this session

## Bible Writing — Now P0 Priority

Bible flagship entry writing is now the top priority for content production. Steve hand-writes all 40 flagship entries. The mpw_bible_writer.py is NOT used for these. 

### Three-Level Reader Standard (ALL Flagship Entries)
Every flagship entry must simultaneously serve:
1. **Mid-session fix** — producer has a problem RIGHT NOW, needs the answer in 30 seconds. Fix-It diagnostic is the mechanism.
2. **Deep learning** — full picture, theory, history, philosophy. Parameters section + How It Works + History are the mechanism.
3. **Institutional licensing** — Berklee, Full Sail, Icon Collective reading as curriculum. Citation block + editorial standards footer are the mechanism.

### Writing Standard
- Phenomenal prose — not reference writing, not help text
- Philosophical depth — the "why" behind every technical decision
- Specific producer examples with named gear, settings, and songs
- No hedging, no qualification, no "it depends" without specifics
- Every section earns its place — if it doesn't teach something useful, cut it

### Content Sections That Must Appear in Every Flagship Entry
- **New Producers / Beginner Trap** — 3 specific mistakes with fixes + green callout. This is the most shareable section.
- **Fix-It Diagnostic** — 8 symptoms, accordion pattern, result drops under clicked symptom
- **In The Wild** — minimum 8 real track analyses with timestamps + one comparison showcase (e.g. Daft Punk vs Radiohead for compression)
- **Producer DNA** — 3 producers, each with collapsible signal chain and signature technique
- **Mix Translation Test** — 5 systems, compression-specific or term-specific symptoms
- **Citation Block** — APA, MLA, Chicago, Harvard — institutional credibility
- **Version Changelog** — shows living document, builds trust with repeat visitors

## S78 Article Production: 0 Articles
No articles written this session. All content effort went to compression.html flagship build.

## Pending Content Queue (unchanged)
- Batch 09: 100 track breakdowns — QUEUED (after Bible Tier 1)
- Batch 11: 60 recreations — QUEUED (after Batch 09)
- Genre Bible (20 entries × massive search volume) — QUEUED (after tools milestone)

---

# SESSION 79 UPDATE — CONTENT — May 28, 2026

## Tool Hub — Destination Tools Strategy (LOCKED)

12 destination tools scoped and fully specced in `MPW-TOOL-SESSION-PLAN.md`. These are tools that rank independently, get bookmarked, get shared, and drive direct traffic. Different category from Bible entry embed tools.

### Priority Build Order

| # | Tool | Slug | Tech Group | Why First |
|---|---|---|---|---|
| 1 | Loudness Penalty Calculator | /tools/loudness-penalty | A | Pure JS, fast build, beats Ian Shepherd, enormous search volume |
| 2 | 808 Relationship Analyzer | /tools/808-relationship-analyzer | B | Massive hip-hop volume, Web Audio preview, no competitor |
| 3 | Arrangement Blueprint Generator | /tools/arrangement-blueprint | C | No competitor, canvas PNG export, Product Hunt anchor |
| 4 | Mix Fingerprint Analyzer | /tools/mix-fingerprint | C | Unique concept, D3 radar, shared in every mixing forum |
| 5 | Vocal Chain Builder | /tools/vocal-chain-builder | D | Highest search volume in all music production |
| 6 | ClearCheck | /tools/clearcheck | D | Highest revenue potential |
| 7 | Mix Translation Simulator | /tools/mix-translation | C | Also serves as Bible embed for mix-translation entry |
| 8 | Signal Flow Visualizer | /tools/signal-flow-visualizer | C | Drag-and-drop, educational, backlink magnet |
| 9 | Reference Track Decoder | /tools/reference-decoder | D | 200-track curated database |
| 10 | Producer BPM DNA | /tools/bpm-dna | C | D3 bell curve, genre distributions |
| 11 | Stem Quality Tester | /tools/stem-quality-tester | D | AI stem era relevance |
| 12 | Frequency Conflict Detector v2 | /tools/frequency-conflict-detector | A | Upgrade existing gold standard |

### ClearCheck Architecture (UPDATED — TruClarify removed)

- Layer 1: Free (email gate) — risk score + plain-English explanation
- Layer 2: $29 one-time — full clearance report + letter template
- Layer 3: US attorney directory — monthly listing fee from attorneys
- Scope: US only
- No TruClarify dependency — fully independent
- Attorney directory: `/tools/clearcheck/attorneys` — filterable by state/specialization
- Build Layer 1 in tool session. Layers 2–3 after attorney listing spec complete.

## Tools Monetization (LOCKED)

Gate strategy applies to ALL tools on the site — new and existing:
- Free to use: always
- Email gate: on any download/export output only
- Never gate: the tool itself

## S79 Content Production: 0 Articles, 0 Bible Entries
Full session dedicated to planning, architecture, and document creation.

## Content Pipeline — Updated

| Phase | Work | Priority | Blocked By |
|---|---|---|---|
| Session 80 | Hub redesign + Loudness Penalty + session prompt files | P0 | Nothing |
| Sessions 81–84 | All 12 destination tools (parallel) | P0 | Session 80 prompt files |
| Sessions 85–86 | 9 curation files build | P1 | Nothing (parallel to tools) |
| Session 87 | Bible flagship writer build | P1 | Curation files + tools |
| Sessions 88+ | Bible writer batch runs | P1 | Writer confirmed |
| After tools | Batch 09: 100 track breakdowns | P3 | Tools + Bible milestone |
| After Batch 09 | Batch 11: 60 recreations | P4 | Batch 09 |

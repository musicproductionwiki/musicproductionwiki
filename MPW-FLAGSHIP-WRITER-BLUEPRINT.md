# MPW FLAGSHIP WRITER BLUEPRINT
*Locked: Session 79 — May 28, 2026*
*Status: AUTHORITATIVE — supersedes all prior writer specs*
*Companion doc: MPW-TOOL-SESSION-PLAN.md*

---

## PART 1 — STRATEGIC CONTEXT

### What This Writer Does
`mpw_flagship_writer.py` generates all 40 Tier 1 flagship Bible entries at compression.html quality — 17,800+ words assembled, 13,600+ words prose — via a 4-pass architecture that separates intellectual work (discovery) from structural work (assembly).

**Claude generates content only. Python generates structure. No exceptions.**

This writer is NOT built until:
1. All 9 curation files are complete and validated
2. Wave 1 Bible entry tools are confirmed live
3. The hub redesign (Session 80) is complete
4. Gate system is fully implemented and tested on one entry

### Why This Approach
The current `mpw_bible_writer.py` asks Claude to generate HTML. This produces mediocre content and mediocre structure simultaneously. The flagship writer asks Claude to generate insights and prose only. Python handles all structure. The two jobs never compete for context window.

### Quality Benchmark — Live Audit of compression.html

| Metric | Value |
|---|---|
| File size | 288KB |
| Total words (all content) | 20,618 |
| Prose words (scripts/styles stripped) | 17,823 |
| Pure prose sections | 13,684 words |
| Structural sections | 2,906 words |
| Entry sections | 26 |
| Share bars | 8 |
| Schema blocks | 5 |

**Every generated entry must reach these benchmarks or fail Gate 3.**

### API Cost Model
- Pass 1: ~20,000 tokens
- Pass 2A: ~32,000 tokens
- Pass 2B: ~32,000 tokens
- Pass 3: 0 tokens (Python only)
- Total per entry: ~84,000 tokens ≈ $0.40–0.50 per flagship entry
- 40 entries total: ~$16–20 in API costs
- This is acceptable. Document it so there are no surprises.

---

## PART 2 — CURATION FILES (BUILD BEFORE THE WRITER)

All 9 files must exist and be validated before the writer runs a single entry. These files are the difference between a plausible entry and an authoritative one.

| File | Contents | Status |
|---|---|---|
| `flagship_central_insights.json` | 40 pre-approved insights (1 per slug) | COMPLETE — locked below |
| `flagship_tool_map.json` | Locked tool per slug (40 entries) | COMPLETE — in Tool Plan doc |
| `flagship_tracks.json` | 6 verified tracks per slug with analysis context | TO BUILD |
| `flagship_genre_data.json` | Genre table rows per slug — real curated numbers | TO BUILD |
| `flagship_producer_dna.json` | 3 producers per slug, signal chain + technique + song | TO BUILD |
| `flagship_plugin_recs.json` | Free/mid/pro plugins per slug, 3 tiers | TO BUILD |
| `flagship_misconceptions.json` | 3 beginner traps per slug with specific fixes | TO BUILD |
| `flagship_wtrn.json` | 6 What To Read Next cards per slug — verified slugs only | TO BUILD |
| `quotes_merged_v2.json` | Fix 4 zero-coverage gaps + 1 resonance quote | IN PROGRESS |

### Quote Gaps Remaining

| Slug | Status | Action |
|---|---|---|
| sidechain-compression | 0 quotes ❌ | Retag from adjacent compression/sidechain pool |
| mix-translation | 0 quotes ❌ | Retag from adjacent mixing pool |
| sidechain-ducking | 0 quotes ❌ | Retag from adjacent sidechain pool |
| reference-mixing | 0 quotes ❌ | Retag from adjacent mixing pool |
| resonance | 2 quotes ⚠️ | Add 1 more — owner action flagged |

### Track Count Decision (Session 79)
6 verified tracks per slug. Not 8. 6 is sufficient for the `in-the-wild` section depth target and is more manageable as curated data. Every track must be verified — no generated track analyses.

---

## PART 3 — LOCKED CENTRAL INSIGHTS (All 40 Slugs)

These are pre-approved. Pass 1 validates against these. Pass 1 does not discover them — they are already known. Maximum 2 retries if Pass 1 returns a divergent insight. After 2 retries, use pre-approved insight directly and log discrepancy.

**Reject any insight containing:** "balance", "tone", "control", "adjust" without specific context. Reject any insight that could apply to more than one term.

```json
{
  "eq": "EQ is a spatial tool masquerading as a corrective one — every cut creates distance, every boost creates presence.",
  "gain-staging": "Gain staging is not about preventing clipping — it is about where in the signal chain you choose to introduce noise.",
  "delay": "Delay is not an effect applied to sound — it is a second performance happening slightly behind the first.",
  "limiting": "A limiter is not a safety net — it is a decision about what information you are willing to destroy.",
  "saturation": "Saturation is not distortion — it is the sound of a circuit working harder than it was designed to.",
  "sidechain-compression": "Sidechain compression is not a ducking effect — it is a rhythmic contract between two elements sharing the same frequency space.",
  "lufs": "LUFS is not a loudness target — it is a translation standard that determines how your music sounds relative to everything else.",
  "mastering": "Mastering is not the stage where you make a mix louder — it is the stage where you decide what the mix is optimized for.",
  "parallel-compression": "Parallel compression is not a mix technique — it is a philosophical choice about how much of a sound's original character you are willing to sacrifice for control.",
  "bus-compression": "Bus compression does not make a mix louder — it makes a mix feel like it was performed by people in the same room.",
  "stereo-imaging": "Stereo imaging is not about making a mix wide — it is about placing sounds in physical space the listener believes exists.",
  "mid-side-processing": "Mid-side processing does not change the stereo field — it exposes the two independent signals your mono and stereo playback systems hear.",
  "automation": "Automation is not a correction tool — it is the performance that happens after the performance.",
  "high-pass-filter": "A high-pass filter does not remove bass — it removes competition for the frequencies that define your mix's foundation.",
  "parametric-eq": "A parametric EQ does not shape sound — it shapes the space between sounds.",
  "multiband-compression": "Multiband compression does not fix a mix — it treats frequency bands as separate instruments that each need their own dynamic contract.",
  "noise-gate": "A noise gate is not a silence switch — it is a threshold decision about what counts as a performance.",
  "dynamic-range": "Dynamic range is not a technical measurement — it is the emotional distance between the quietest and loudest moment a listener will accept.",
  "headroom": "Headroom is not empty space — it is the room your mix needs to breathe without asking permission.",
  "subtractive-synthesis": "Subtractive synthesis does not build sounds — it reveals them by removing what the oscillator already contains.",
  "lfo": "An LFO is not a modulation source — it is a clock that turns static sound into living sound.",
  "adsr": "ADSR is not an envelope shape — it is a description of how a sound behaves in time relative to human expectation.",
  "mix-translation": "Mix translation is not a technical problem — it is a test of whether your mix communicates its intent independent of the playback system.",
  "transient-shaping": "A transient shaper does not add punch — it determines what part of a sound arrives first and what part the listener remembers.",
  "fm-synthesis": "FM synthesis does not add harmonics — it mathematically deforms a carrier wave until it stops sounding like itself.",
  "wavetable-synthesis": "Wavetable synthesis does not play a sample — it moves through a library of frozen moments in a sound's evolution.",
  "oscillator": "An oscillator does not make sound — it makes a decision about which harmonics exist before any processing begins.",
  "true-peak-limiting": "True peak limiting does not prevent distortion — it prevents distortion that only appears after digital-to-analog conversion.",
  "loudness-normalization": "Loudness normalization does not make all music the same volume — it removes the competitive incentive to master louder than the music requires.",
  "send-return": "A send-return is not a routing convenience — it is the decision to share one processed version of a sound across multiple sources.",
  "harmonic-distortion": "Harmonic distortion is not an artifact — it is the mechanism by which analog circuits make digital recordings sound like something was at stake.",
  "resonance": "Resonance is not a filter parameter — it is the sound of a system becoming temporarily unstable at a specific frequency.",
  "sidechain-ducking": "Sidechain ducking is not a mixing trick — it is a rhythmic agreement between two elements about who speaks when.",
  "modulation": "Modulation is not an effect — it is the introduction of time as a sound design parameter.",
  "chorus": "Chorus is not a doubling effect — it is the controlled simulation of human ensemble imperfection.",
  "low-pass-filter": "A low-pass filter does not remove highs — it decides what kind of room the sound is coming from.",
  "arrangement": "Arrangement is not song structure — it is the management of the listener's attention across time.",
  "reference-mixing": "Reference mixing is not a comparison exercise — it is the calibration of your ears to the standard your mix will be judged against."
}
```

---

## PART 4 — WRITER ARCHITECTURE

### File Location
`C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_flagship_writer.py`

### Input
```powershell
. .\setenv.ps1
python mpw_flagship_writer.py --batch-file flagships_wave1a.txt --workers 4
```

Batch file format (one per line):
```
eq:EQ:Frequency:1
gain-staging:Gain Staging:Signal Processing:1
delay:Delay:Time-Based:1
```

### Four-Pass Architecture

```
Pass 1    → Discovery + Insight Validation (API call → JSON)
Pass 1.5  → Quotes Filter (no API call — filter quotes_merged_v2.json by tags)
Pass 2A   → Foundation Prose (API call — conceptual sections)
Pass 2B   → Evidence Prose (API call — specificity sections)
Pass 3    → Python Assembly (no API call — structure only)
```

**Why Pass 2 is split (critical decision — do not revert):**
A single pass generating 13,684 prose words across 26 sections produces context collapse. The model hits `in-the-wild` (1,399 words) and `producer-dna` (932 words) at the end of a degraded context. These are the most specificity-dependent sections — fabricated track analyses and producer chains are the highest quality risk. Splitting gives each call a focused job:

- **Pass 2A** generates conceptual sections where accuracy comes from training knowledge (definition, how-it-works, parameters, history, signal-chain, new-producers)
- **Pass 2B** receives Pass 2A output as context + all locked curation data, generates evidence sections (in-the-wild, producer-dna, mix-translation, how-to-use, signatures, mistakes)

### Script Structure

```python
mpw_flagship_writer.py
├── load_curation_files()         # Loads all 9 JSON files — fails loudly if any missing
├── LOCKED_TEMPLATES{}            # Extracted fresh from compression.html at run start
│   ├── SHARE_CSS                 # .mpw-share-btns pattern
│   ├── GENRE_CSS                 # .gtrow CSS grid pattern
│   ├── NAV_JS                    # IntersectionObserver IIFE
│   ├── FIXIT_JS                  # Fix-It accordion function
│   ├── CITATION_TEMPLATE         # APA/MLA/Chicago/Harvard block
│   ├── CHANGELOG_TEMPLATE        # Version amber dot timeline
│   ├── FOOTER_TEMPLATE           # Footer with share + links
│   ├── EMBED_TEMPLATE            # iframe snippet + copy button
│   ├── WTRN_TEMPLATE             # What to Read Next 6-card layout
│   └── SIDEBAR_SHARE_TEMPLATE    # Sidebar stacked share column
│
├── gate1_template_integrity()    # Before any API calls
├── pass1_discovery()             # API → JSON → insight gate
├── gate2_insight_quality()       # After Pass 1
├── pass1_5_quotes()              # No API — filter quotes by tags
├── pass2a_foundation()           # API → prose HTML (conceptual)
├── pass2b_evidence()             # API → prose HTML (evidence)
├── pass3_assemble()              # Python only → full HTML
├── gate3_validation()            # After Pass 3 — before commit
├── diff_report()                 # Structural compare vs compression.html
├── commit()                      # Trees API → SHA
└── run_batch()                   # Parallel execution via ThreadPoolExecutor
```

### Token Budgets and Timeouts

| Pass | Max Tokens | Timeout |
|---|---|---|
| Pass 1 | 20,000 | 300s |
| Pass 2A | 32,000 | 600s |
| Pass 2B | 32,000 | 900s |
| Pass 3 | 0 (no call) | — |

### Delivery Format
3-part PS1 install scripts (same pattern as bible writer delivery):
- `install_flagship_writer_part1.ps1`
- `install_flagship_writer_part2.ps1`
- `install_flagship_writer_part3.ps1`

Each part under 200KB. Run in order. Final part runs smoke test: generates `eq.html` locally, prints word count, validation score, and first paragraph of definition section for review.

---

## PART 5 — THREE-GATE QUALITY SYSTEM

### Gate 1 — Template Integrity (before any API calls)

Runs fresh every session. Fetches live `bible/compression.html` via GitHub API. Extracts all locked template blocks. Validates each against fingerprint strings.

If any fingerprint missing → **hard fail with specific error message. No API calls made.**

| Block | Fingerprint Required |
|---|---|
| SHARE_CSS | `.mpw-share-btns` |
| GENRE_CSS | `.gtrow` |
| CITATION_TEMPLATE | `APA` AND `MLA` AND `Chicago` AND `Harvard` |
| FIXIT_JS | `scrollIntoView` |
| EMBED_TEMPLATE | `iframe` AND `copy` |
| WTRN_TEMPLATE | `what-to-read-next` |

Templates always come from the live file. Never from frozen constants. Never from handoff docs.

### Gate 2 — Insight Quality (after Pass 1)

Pass 1 validates against `flagship_central_insights.json`.

Reject if insight contains: "balance", "tone", "control", "adjust" without specific context.
Reject if insight could apply to more than one slug.

Process:
1. Pass 1 returns insight
2. Compare against pre-approved insight for that slug
3. If matches in substance → proceed
4. If diverges → retry (max 2 retries)
5. After 2 retries → use pre-approved insight directly, log discrepancy to `insight_log.txt`

### Gate 3 — Post-Assembly Validation (before commit)

All checks must pass. Any failure → write HTML to `failed/[slug].html` + report to `failed/[slug]-report.txt`. **No commit.**

**Structural checks:**
- [ ] Share bar count = 8 (hard fail if < 8)
- [ ] Embed code block present below tool share bar
- [ ] Genre table uses `.gtrow` class — no HTML `<table>` in genre section
- [ ] All 6 SEO elements present: canonical, og:title, og:description, og:image, og:url, twitter:card
- [ ] 5 JSON-LD schema blocks: Article, FAQPage, BreadcrumbList, HowTo, Speakable
- [ ] Zero placeholder strings remaining: THE_NUMBER_PLACEHOLDER, SIGNAL_CHAIN_PLACEHOLDER, GENRE_PLACEHOLDER, PLUGIN_PLACEHOLDER, DAW_PLACEHOLDER, FAQ_PLACEHOLDER, FLAGS_PLACEHOLDER, BEFORE_AFTER_PLACEHOLDER, QUICKREF_SHARE_PLACEHOLDER
- [ ] Template fingerprints in output: `.mpw-share-btns`, `.gtrow`, `APA`, `MLA`

**Word count checks (scripts/styles stripped):**
- [ ] Total assembled prose ≥ 15,000 words — hard fail below this
- [ ] Total assembled prose ≥ 17,000 words — warning if below target (not fail)

**Per-section minimums (hard fail if any below floor):**

| Section | Minimum |
|---|---|
| definition | 800 words |
| in-the-wild | 900 words |
| mix-translation | 800 words |
| history | 700 words |
| how-to-use | 600 words |
| producer-dna | 600 words |
| parameters | 500 words |

### Diff Report (informational — runs after Gate 3 passes)

Prints before committing:
```
[DIFF vs compression.html]
Sections:     26 / 26 ✅
Share bars:   8 / 8   ✅
Schema:       5 / 5   ✅
Prose words:  [N] / 17,823 target
```

Not a gate — information only. Producer reviews before approving commit if below target.

---

## PART 6 — CONTENT STANDARDS

### The Three-Level Reader (mandatory for every entry)

1. **Mid-session fix** — producer has a problem RIGHT NOW. Needs the answer in 30 seconds. Fix-It diagnostic accordion is the mechanism.
2. **Deep learning** — full theory, history, philosophy. Parameters + How It Works + History are the mechanism.
3. **Institutional licensing** — Berklee, Full Sail, Icon Collective curriculum. Citation block + editorial standards footer are the mechanism.

Every section must serve at least one of these three readers. If a section serves none of them, it gets cut.

### Specificity Standard

What separates authoritative from plausible:

| Plausible (reject) | Authoritative (require) |
|---|---|
| "songs like this use fast attack" | "*Billie Jean*, 0:04 — kick sits at −18dB before snare enters" |
| "a vintage compressor" | "UA 1176 Rev D, all-buttons mode" |
| "producers use this for warmth" | "Tchad Blake: 'I run everything through the SP2B before the console'" |
| "fast attack for trap drums" | "Attack 0.1ms, release auto, ratio 10:1, threshold −18dBFS" |

### Pass 2A Sections — Foundation (conceptual)

definition, how-it-works, new-producers, parameters, signal-chain, history

Target: 6,000–7,000 prose words total across these 6 sections.

Pass 2A receives: Pass 1 JSON, locked central insight, quotes_context (from Pass 1.5).
Pass 2A does NOT receive: track lists, producer DNA, genre data (those go to 2B).

### Pass 2B Sections — Evidence (specificity)

in-the-wild, producer-dna, mix-translation, how-to-use, signatures, types, mistakes, progression, flags, faq

Target: 6,500–7,500 prose words total across these sections.

Pass 2B receives: Pass 2A output (voice/angle established), locked track list (6 tracks from `flagship_tracks.json`), locked producer DNA (3 producers from `flagship_producer_dna.json`), genre data (from `flagship_genre_data.json`), Pass 1 JSON, quotes_context.

Pass 2B does NOT generate tracks or producer chains — it writes analysis around the locked data.

### Required Sections (26 total — every entry)

definition → how-it-works → new-producers → parameters → quick-reference → tools → signal-chain → fix-it → history → how-to-use → genre-table → topology → hardware-plugin → before-after → in-the-wild → producer-dna → signatures → types → verdict → plugin-recs → mistakes → mix-translation → flags → progression → faq → related

### Share Bar Placement (8 required — compression.html gold standard)

1. After new-producers section
2. After quick-reference table
3. After tools section (with embed code block below)
4. After genre-table
5. After in-the-wild
6. After verdict
7. Sidebar (stacked column)
8. Footer (X and Reddit only)

### Gold Standards

Both must be studied before writing any new flagship entry:

- **compression.html** — gold standard for: structure, SEO, share bar pattern, embed code, citation block, genre CSS grid, Fix-It accordion, entry nav IntersectionObserver, version changelog
- **reverb.html** — gold standard for: prose depth, section content architecture, Three Questions framework, producer DNA approach, version changelog architecture

Every entry inherits from both. Not one. Both.

### Section-Level Share Bar CSS Pattern (locked)

```css
.mpw-share-bar { display:flex; flex-direction:column; gap:8px; margin-top:14px; padding-top:14px; border-top:1px solid #2a2a4a; }
.mpw-share-label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.1em; color:#666; display:block; }
.mpw-share-btns { display:flex; gap:6px; width:100%; }
.mpw-share-btn { flex:1; height:36px; }
.share-x { background:#000; color:#fff!important; }
.share-reddit { background:#ff4500; color:#fff; }
.share-copy { background:#f5a623; color:#000; }
```

---

## PART 7 — 40 FLAGSHIP ENTRY STATUS

### Wave 1 — Universal 10

| Entry | Status | Tool |
|---|---|---|
| compression | ✅ LIVE (v1.2, SHA 9de422e2) | gr_calculator |
| eq | ⬜ TO BUILD | frequency_reference |
| gain-staging | ⬜ TO BUILD | gain_staging_calc |
| reverb | ✅ LIVE | rt60_calculator |
| delay | ⬜ TO BUILD | delay_calculator |
| limiting | ⬜ TO BUILD | lufs_calculator |
| saturation | ⬜ TO BUILD | gr_calculator |
| sidechain-compression | ⬜ TO BUILD | gr_calculator |
| lufs | ⬜ TO BUILD | lufs_calculator |
| mastering | ⬜ TO BUILD | lufs_calculator |

### Wave 2 — Intermediate 15

parallel-compression, bus-compression, stereo-imaging, mid-side-processing, automation, high-pass-filter, parametric-eq, multiband-compression, noise-gate, dynamic-range, headroom, subtractive-synthesis, lfo, adsr, mix-translation

### Wave 3 — Advanced 15

transient-shaping, fm-synthesis, wavetable-synthesis, oscillator, true-peak-limiting, loudness-normalization, send-return, harmonic-distortion, resonance, sidechain-ducking, modulation, chorus, low-pass-filter, arrangement, reference-mixing

### Parallel Execution Plan (Bible Writer Sessions)

```
Session A: eq, gain-staging, delay, limiting, saturation
Session B: sidechain-compression, lufs, mastering (reverb + chorus already live)
Session C: parallel-compression, bus-compression, stereo-imaging, mid-side-processing, automation
Session D: high-pass-filter, parametric-eq, multiband-compression, noise-gate, dynamic-range
Session E: headroom, subtractive-synthesis, lfo, adsr, mix-translation
Session F: transient-shaping, fm-synthesis, wavetable-synthesis, oscillator, true-peak-limiting
Session G: loudness-normalization, send-return, harmonic-distortion, resonance, sidechain-ducking
Session H: modulation, low-pass-filter, arrangement, reference-mixing
```

Run Sessions A+B+C+D simultaneously for Wave 1 + Wave 2 start. Review output from all 4. Then run E+F+G+H simultaneously.

**Note:** reverb.html and chorus.html are already live. Writer skips these by default unless Steve decides to regenerate for consistency with the new template.

---

## PART 8 — WRITER BUILD PROTOCOL

### Session Start Protocol (for writer build session)

1. Read this document in full
2. Read SCRIPTS handoff "mpw_flagship_writer.py Build Brief" section
3. Fetch live `bible/compression.html` via GitHub API — run Gate 1 extraction manually to confirm all template blocks
4. Confirm all 9 curation files exist in `mpw-scripts\` directory
5. Confirm `quotes_merged_v2.json` has zero-coverage gaps resolved
6. Build Pass 1 → test on `eq` → verify insight matches pre-approved
7. Build Pass 1.5 quotes filter → verify correct authors returned for `eq`
8. Build Pass 2A → test on `eq` → review definition and history sections against compression.html depth
9. Build Pass 2B → test on `eq` → review in-the-wild and producer-dna against compression.html specificity
10. Build Pass 3 assembly → generate `eq.html` → run Gate 3 → visual QA on mobile
11. Review diff report vs compression.html
12. Only after eq.html passes all gates AND visual QA: run Wave 1a batch

### Never Rules — Bible Writer Specific (Session 79)

| Rule | Reason |
|---|---|
| Never target Pass 2 prose at 4,800 words — correct target is 12,000–14,000 words | compression.html prose sections total 13,684 words. Old spec measured wrong metric. |
| Never run Pass 2 as a single call — always split into Pass 2A and Pass 2B | Context collapse degrades in-the-wild and producer-dna which appear late in a long generation |
| Never generate track lists in any Pass — use flagship_tracks.json (6 locked tracks per slug) | Fabricated track analyses are the highest-risk content in any flagship entry |
| Never generate genre table numbers — use flagship_genre_data.json | Generated numbers sound plausible but may be wrong |
| Never generate producer signal chains — use flagship_producer_dna.json | Fabricated signal chains undermine institutional authority standard |
| Never run the writer before all 9 curation files are complete and validated | Missing files force generation of content they would have locked |
| Never run the writer before Gate 1 confirms template integrity from live compression.html | Templates come from the live file every run — not frozen constants |
| Never accept Gate 3 failure as acceptable — failed entries go to failed/ directory | Every committed entry has passed all gates. No exceptions. |
| Never commit a Bible entry one file at a time — Trees API always | One commit = one Netlify deploy |
| Never use mpw_bible_writer.py for the 40 flagship entries | Standard writer produces standard entries. Flagship entries need the flagship writer. |

---

## PART 9 — INSTITUTIONAL STRATEGY

### Why the Flagship Entries Are P0

The 40 flagship entries are the permanent anchor content driving:

- **Organic search authority** — compression, eq, reverb = highest-volume music production queries in existence
- **Institutional licensing** — $1,500–$12,000/year schools, $25,000/year DAW companies
- **Citation credibility** — APA/MLA/Chicago/Harvard blocks on every entry. Producers cite these in school papers. Schools adopt because students already use it.
- **The 2026 Edition marker** — institutional hook for annual licensing renewal. Schools license current editions.
- **Paid tier trigger** — these entries drive the 25,000 monthly /bible/ visitor threshold that activates the $9/month Bible Complete subscription

### Institutional Licensing Targets

| Institution Type | Fee | Target Volume |
|---|---|---|
| Small school (<500 students) | $1,500/year | 50 schools |
| Medium school (500–2,000) | $4,500/year | 20 schools |
| Large institution (2,000+) | $12,000/year | 5 schools |
| DAW company (Ableton, Logic, FL) | $25,000/year | 3 companies |

At scale: $75K + $90K + $60K + $75K = $300K/year institutional revenue from 78 relationships.

The 2026 Edition badge on every entry creates the annual renewal conversation. This is not incidental — it is the licensing hook. Every flagship entry ships with it.

---

*Document locked: Session 79 — May 28, 2026*
*Companion: MPW-TOOL-SESSION-PLAN.md*
*Bible writer build begins: Session 87 (after tools + curation files complete)*

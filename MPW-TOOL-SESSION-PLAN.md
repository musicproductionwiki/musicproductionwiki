# MPW TOOL SESSION PLAN
*Locked: Session 79 — May 28, 2026*
*Status: AUTHORITATIVE — supersedes all prior tool planning notes*
*Companion doc: MPW-FLAGSHIP-WRITER-BLUEPRINT.md*

---

## PART 1 — STRATEGIC FOUNDATION

### The Mission
MPW's tool hub becomes the most visually impressive, practically useful, and technically sophisticated free tool suite in music production. Not one of the best. The best. Every tool either doesn't exist anywhere else in its form, or exists in an inferior form we decisively beat.

### The Two-Layer Tool Architecture

**Layer 1 — Bible Entry Embed Tools**
Contextual tools living inside flagship Bible entries. Each entry has exactly one embedded tool relevant to that term. These are functional, excellent, and deeply integrated into the entry's prose. Not the hub's identity — they serve the entry.

**Layer 2 — Destination Tools (The Hub)**
Standalone tools that rank independently, get bookmarked, get shared, get submitted to Product Hunt. These define what MPW's tool hub is known for. Visual output that communicates more than text, curated reference data that took real research, a recommendation engine that tells the producer what to do next.

### One Hub. One URL. Forever.

**`/tools/index.html`** — single tool hub. Permanent.

**`/bible/categories/tools/`** — Bible category filter page only. Shows Bible entries containing tools. NOT a hub. Links to `/tools/` for the full suite. Different intent, different audience, never competes with the hub.

The `/tools/` URL accumulates authority permanently. Every backlink to any tool page passes authority up to `/tools/`. The hub is the SEO spine of the entire tool suite.

### Quality Standard — Non-Negotiable

Every tool clears all of these before commit:

- **Real calculation** — actual math, not lookup tables dressed as calculators
- **Visual output** — at least one canvas/SVG responding to input in real time
- **Famous producer presets** — one-click load of named producer/track settings
- **Click-to-copy** on every value a producer would enter in a DAW
- **Recommendation engine** — tells the producer what to do next, not just what the number is
- **Mobile-first** — works perfectly on phone, tested on real device before commit
- **Embed code** — every tool embeddable by YouTubers, educators, blogs
- **Share bar** — Copy Link + X + Reddit + Embed (mpw-share-bar pattern from compression.html)
- **Monetization hook** — email gate on download/export output, built in from day one

Design gold standard: Frequency Conflict Detector at `/tools/frequency-conflict-detector`

Design system (locked — never deviate):
```css
--bg: #0d0d1a; --bg2: #111120; --bg3: #16162a; --bg4: #1c1c32;
--amber: #f5a623; --teal: #00e8a2; --red: #ff3d5a;
--text: #f0f0f4; --text2: #a0a0b8; --text3: #5a5a7a;
--mono: 'DM Mono', monospace; --sans: 'DM Sans', sans-serif;
```
Fonts: DM Sans + DM Mono (Google Fonts). Never substituted.

### Monetization Architecture — Tools

**Rule: Never gate the tool itself. Gate the download/export output only.**

| Tier | Mechanism | Examples |
|---|---|---|
| Free forever | Tool use, no gate | All calculators, visualizers, analyzers |
| Email gate (Beehiiv) | Export/download output | Arrangement PNG, Chain PDF, Spec Card PDF |
| Paid one-time $9–$29 | Comprehensive reference materials | Frequency Bible PDF, Genre Settings Bible |
| Bible Complete $9/mo or $79/yr | Full Bible + all tools | Subscription tier |
| ClearCheck Layer 2 $29 | Full clearance report + letter template | One-time purchase |
| ClearCheck Layer 3 | Attorney referral listing fee | US attorneys pay monthly listing fee |

Every destination tool is built with its specific monetization mechanism coded from day one — not retrofitted later.

---

## PART 2 — HUB REDESIGN

### Current State
`/tools/index.html` — hand-crafted HTML, 41 tools, single-zone card grid. Functional. Not a destination. Not a product.

### Target State — Three-Zone Architecture

**Zone 1 — The Hero**
Live flagship tool running on page load. Not a hero image, not a tagline — an interactive tool producers can use immediately. Mix Fingerprint radar chart or Loudness Penalty Calculator as the hero. They land and instantly understand what kind of place this is. No competitor does this.

**Zone 2 — Flagship Destination Tools**
6–8 destination tools as premium cards above the main grid. Each card:
- Mini live SVG preview of the tool's visual output (not a screenshot)
- Problem statement: "What this solves" — one line
- "Launch Tool" CTA — amber, full-width on mobile
- "New" badge — automated by publish date, 30-day window
Visual weight: significantly larger than utility cards. These are the hub's identity.

**Zone 3 — The Full Suite**
Category-filtered grid. All tools. Same improved card format. Filter pills: Mixing / Mastering / Synthesis / Dynamics / Arrangement / Business / AI. Instant search across names and descriptions.

**Additional Hub Features:**
- Search bar — instant filter on tool name AND description
- "Most Used" editorial spotlight — 3 tools at top (editorial initially, analytics-driven later)
- Embed codes accessible from hub cards — no need to visit tool page to grab embed
- "Request a Tool" CTA at bottom — email gate → Beehiiv → validated demand signal
- Stats row (locked): "Free forever · No signup required · Works on mobile"
- 300–400 words of keyword content below Zone 3 targeting: "free music production tools online", "music producer calculators", "music production tool hub"

### Hub SEO Targets
Primary: "free music production tools online", "music producer tools", "music production calculators"
Secondary: "online tools for music producers", "free mixing tools online", "music production reference tools"

### Product Hunt Readiness
The hub, when destination tools are live, is a Product Hunt submission. Every design decision — hero interaction, Zone 2 card quality, "what is this place" clarity in 5 seconds — must be made with that submission day in mind. Build for it from the start.

---

## PART 3 — PARALLEL BUILD ARCHITECTURE

### How Simultaneous Sessions Work

Steve runs multiple simultaneous Claude sessions on Max plan. Each session receives a complete self-contained build prompt — no dependencies on other sessions, no shared state. Each session delivers one fully functional tool committed to GitHub via Trees API.

**Session prompt file structure (one per tool):**
```
tool_build_[slug].md
├── Design system (full CSS variables, fonts — copy verbatim)
├── Never rules for tool builds (complete list)
├── Tool spec (full: inputs, outputs, tech, presets, monetization hook)
├── Frozen nav HTML (exact from live site)
├── Share bar pattern (exact from compression.html)
├── Embed code pattern
├── Validation checklist (must pass before commit)
└── Commit instruction (Trees API — tool page + hub card update)
```

Each session prompt is self-contained. The session reads it, builds the tool, validates, commits, done. No cross-session coordination needed.

### Parallel Build Groups

Tools are grouped by technology so sessions with similar stacks can be run simultaneously without one blocking another:

**Group A — Pure JS/SVG (fastest builds, run first)**
- Loudness Penalty Calculator
- Dynamic Range Analyzer
- Transient Shaper Visualizer
- Sidechain Ducking Calculator
- Reference Loudness Matcher
- Noise Gate Visualizer
- Automation Curve Visualizer
- BPM DNA
- Frequency Conflict Detector v2 (upgrade)

**Group B — Web Audio API**
- 808 Relationship Analyzer
- Chorus Depth & Rate Explorer
- Oscillator Waveform Analyzer

**Group C — Advanced (D3/Canvas/complex math)**
- Arrangement Blueprint Generator (canvas PNG export)
- Mix Fingerprint Analyzer (D3 radar)
- Filter Response Visualizer (biquad math)
- FM Operator Visualizer
- Wavetable Position Visualizer
- Modulation Matrix Visualizer
- Mix Translation System Simulator

**Group D — Claude API powered**
- Vocal Chain Builder
- Reference Track Decoder
- Stem Quality Tester
- ClearCheck Layer 1

**Recommended parallel run order:**
```
Round 1: Run 4 Group A sessions simultaneously
Round 2: Run 3 Group B + 1 Group A session simultaneously
Round 3: Run 4 Group C sessions simultaneously
Round 4: Run 3 Group D sessions simultaneously
```

Hub redesign runs as its own dedicated session FIRST — before any tool builds — because every tool build needs to know the hub card format.

### Session Prompt File Location
All session prompt files saved to: `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tool-build-prompts\`
One file per tool: `build_loudness_penalty.md`, `build_808_analyzer.md`, etc.

---

## PART 4 — BIBLE ENTRY EMBED TOOLS

### Wave 1 — Zero New Tool Builds Required

All 10 Wave 1 entries use existing confirmed-live tools:

| Slug | Tool | Standalone Page |
|---|---|---|
| compression | gr_calculator | /tools/gain-reduction-calculator.html |
| eq | frequency_reference | /tools/frequency-reference-chart.html |
| gain-staging | gain_staging_calc | /tools/gain-staging-calculator.html |
| reverb | rt60_calculator | /tools/rt60-calculator.html |
| delay | delay_calculator | /tools/delay-time-calculator.html |
| limiting | lufs_calculator | /tools/lufs-calculator.html |
| saturation | gr_calculator | /tools/gain-reduction-calculator.html |
| sidechain-compression | gr_calculator | /tools/gain-reduction-calculator.html |
| lufs | lufs_calculator | /tools/lufs-calculator.html |
| mastering | lufs_calculator | /tools/lufs-calculator.html |

**Wave 1 Bible entries run with zero new tool builds. Tool builds happen in parallel.**

### Wave 2 — New Tools Required

| Slug | New Tool | Group |
|---|---|---|
| noise-gate | Noise Gate Visualizer | A |
| dynamic-range | Dynamic Range Analyzer | A |
| automation | Automation Curve Visualizer | A |
| subtractive-synthesis | Filter Response Visualizer | C |
| chorus | Chorus Depth & Rate Explorer | B |
| Plus 10 strong existing assignments | — | — |

### Wave 3 — New Tools Required

| Slug | New Tool | Group |
|---|---|---|
| transient-shaping | Transient Shaper Visualizer | A |
| sidechain-ducking | Sidechain Ducking Calculator | A |
| mix-translation | Mix Translation System Simulator | C |
| arrangement | Arrangement Blueprint Generator | C |
| reference-mixing | Reference Loudness Matcher | A |
| modulation | Modulation Matrix Visualizer | C |
| fm-synthesis | FM Operator Visualizer | C |
| wavetable-synthesis | Wavetable Position Visualizer | B |
| oscillator | Oscillator Waveform Analyzer | B |
| Plus 5 strong existing assignments | — | — |

### Complete Bible Entry Tool Map (Locked JSON)

```json
{
  "compression":           "gr_calculator",
  "eq":                    "frequency_reference",
  "gain-staging":          "gain_staging_calc",
  "reverb":                "rt60_calculator",
  "delay":                 "delay_calculator",
  "limiting":              "lufs_calculator",
  "saturation":            "gr_calculator",
  "sidechain-compression": "gr_calculator",
  "lufs":                  "lufs_calculator",
  "mastering":             "lufs_calculator",
  "parallel-compression":  "gr_calculator",
  "bus-compression":       "gr_calculator",
  "stereo-imaging":        "stereo_width_meter",
  "mid-side-processing":   "stereo_width_meter",
  "automation":            "automation_curve_visualizer",
  "high-pass-filter":      "frequency_reference",
  "parametric-eq":         "frequency_reference",
  "multiband-compression": "gr_calculator",
  "noise-gate":            "noise_gate_visualizer",
  "dynamic-range":         "dynamic_range_analyzer",
  "headroom":              "headroom_calc",
  "subtractive-synthesis": "filter_visualizer",
  "lfo":                   "lfo_visualizer",
  "adsr":                  "adsr_visualizer",
  "mix-translation":       "mix_translation_simulator",
  "transient-shaping":     "transient_shaper_visualizer",
  "fm-synthesis":          "fm_operator_visualizer",
  "wavetable-synthesis":   "wavetable_visualizer",
  "oscillator":            "waveform_analyzer",
  "true-peak-limiting":    "lufs_calculator",
  "loudness-normalization":"lufs_calculator",
  "send-return":           "gain_staging_calc",
  "harmonic-distortion":   "frequency_reference",
  "resonance":             "frequency_reference",
  "sidechain-ducking":     "sidechain_ducking_calc",
  "modulation":            "modulation_matrix_visualizer",
  "chorus":                "chorus_explorer",
  "low-pass-filter":       "frequency_reference",
  "arrangement":           "arrangement_blueprint",
  "reference-mixing":      "reference_loudness_matcher"
}
```

---

## PART 5 — ALL 12 DESTINATION TOOL SPECS

---

### TOOL 1 — Loudness Penalty Calculator
**Slug:** `/tools/loudness-penalty`
**Group:** A — Pure JS/SVG
**SEO:** "loudness penalty calculator streaming", "spotify loudness normalization", "mastering LUFS target"
**Beats:** Ian Shepherd's Loudness Penalty — single lookup, no visualization, no recommendation engine
**Monetization:** Email gate on "Download Platform Spec Card PDF"

**Inputs:**
- Integrated LUFS slider (−30 to −5 LUFS)

**Outputs — simultaneous across 8 platforms:**

| Platform | Target | Shows |
|---|---|---|
| Spotify | −14 LUFS | dB reduction, level bar, status |
| Apple Music | −16 LUFS | dB reduction, level bar, status |
| YouTube | −14 LUFS | dB reduction, level bar, status |
| Tidal | −14 LUFS | dB reduction, level bar, status |
| Amazon Music | −14 LUFS | dB reduction, level bar, status |
| SoundCloud | −8 LUFS | dB reduction, level bar, status |
| Deezer | −15 LUFS | dB reduction, level bar, status |
| Broadcast TV | −23 LUFS | dB reduction, level bar, status |

Status per platform: REDUCED (red) / NEUTRAL (teal) / BOOSTED (amber)
Strategic recommendation: "Target −14 LUFS to achieve zero penalty on 6/8 platforms."

**Famous presets:** Streaming Safe (−14), Broadcast Safe (−23), Old School Loud (−8), Vinyl Transfer (−18)
**Tech:** Pure vanilla JS. Platform specs in locked JSON constant. SVG bar chart. Zero dependencies.

---

### TOOL 2 — 808 Relationship Analyzer
**Slug:** `/tools/808-relationship-analyzer`
**Group:** B — Web Audio API
**SEO:** "808 tuner online", "808 key compatibility checker", "how to tune 808 to key"
**Beats:** Nothing equivalent exists
**Monetization:** Email gate on "Download 808 Tuning Chart PDF"

**Inputs:**
- Song key (chromatic selector, major/minor toggle)
- Kick fundamental frequency (30–120Hz slider)

**Outputs:**
- Recommended 808 root note for the key (with music theory rationale)
- Pitch slide recommendation: start note → end note, duration in beats
- Piano roll SVG showing kick fundamental vs 808 root relationship
- Phase relationship display: reinforce or cancel?
- Harmonic alignment: which 808 harmonics align with key's chord tones
- Web Audio API preview: hear kick tone + 808 tone together

**Famous track presets (one-click):**
- Travis Scott "Antidote" — F minor, 808: F1→C1
- Future "Mask Off" — D minor, 808: D1
- Drake "God's Plan" — Ab major, 808: Ab1
- Kendrick "HUMBLE." — E minor, 808: B0
- Playboi Carti "Magnolia" — F# minor, 808: F#1

**Tech:** Web Audio API (OscillatorNode), SVG piano roll, music theory math in JS.

---

### TOOL 3 — Arrangement Blueprint Generator
**Slug:** `/tools/arrangement-blueprint`
**Group:** C — Canvas/SVG
**SEO:** "arrangement template music production", "song structure generator", "music arrangement planner"
**Beats:** No interactive equivalent exists — every competitor is a static blog post or YouTube video
**Monetization:** Email gate on PNG export ("Download Your Blueprint")

**Inputs:**
- Genre (Trap, House, Pop, Rock, Drum & Bass, Afrobeats, R&B, Film Score, Ambient)
- Track length (2:00–8:00 slider)
- Energy target (Peak Early / Peak at Drop / Sustained High / Slow Build / Double Peak)
- Complexity (Minimal / Standard / Dense)

**Output — color-coded SVG arrangement grid:**
- X-axis: bars with section labels (Intro, Verse, Pre-Chorus, Chorus, Bridge, Drop, Outro)
- Y-axis: elements (Kick, Snare/Clap, Hi-Hats, Bass/808, Chords, Lead/Melody, Vocals, FX/Risers, Percussion)
- Element density shown by color intensity (sparse = lighter, dense = darker amber)
- Section boundaries as vertical amber lines
- Energy arc curve above grid (bezier line showing tension/release)
- Density heatmap: overloaded sections (red overlay), thin sections (blue overlay)
- Element count per section shown below grid

**Export:** PNG via canvas (email gate) + text breakdown copy

**Genre arrangement data:** Curated per genre in locked JSON — not generated. Each genre has canonical element entry/exit points, density profiles, and section lengths.

**Tech:** Canvas for PNG export, SVG for interactive display, D3 for energy arc bezier, vanilla JS.

---

### TOOL 4 — Mix Fingerprint Analyzer
**Slug:** `/tools/mix-fingerprint`
**Group:** C — D3.js
**SEO:** "mix reference tool online", "mix fingerprint analyzer", "how to reference mix online"
**Beats:** Nothing equivalent — every EQ plugin shows your curve, nobody shows it against named reference mixes
**Monetization:** Email gate on "Download Fingerprint Report PDF"

**Inputs:**
- Five frequency band sliders: Sub (20–80Hz), Low-Mid (80–300Hz), Mid (300Hz–2kHz), High-Mid (2–8kHz), Air (8–20kHz)
- Each slider labeled by feel: Sub = "weight", Low-Mid = "warmth/mud", Mid = "presence", High-Mid = "clarity", Air = "brightness"
- Reference selector: choose up to 3 from 25 curated landmark records

**Output:**
- D3 radar chart: producer's polygon in amber, reference polygons in distinct colors
- Delta analysis: "Your mix has +15% more low-mid warmth than Random Access Memories"

**Reference database (25 curated records — locked JSON, not generated):**
Thriller, Random Access Memories, To Pimp a Butterfly, In Rainbows, 4:44, Dark Side of the Moon, Back in Black, Blonde, 1989, Madvillainy, Take Care, good kid m.A.A.d city, Channel Orange, Yeezus, The Miseducation of Lauryn Hill, OK Computer, What's Going On, Songs in the Key of Life, Rumours, Kind of Blue, Discovery, Homogenic, Vespertine, Doris, Rodeo

**Tech:** D3.js radar chart, curated reference JSON, vanilla JS sliders. Zero API calls.

---

### TOOL 5 — Vocal Chain Builder
**Slug:** `/tools/vocal-chain-builder`
**Group:** D — Claude API
**SEO:** "vocal chain builder online", "how to process vocals music production", "vocal chain settings genre"
**Beats:** Every competitor is a static blog post with a chain diagram image
**Monetization:** Email gate on "Download Chain PDF Cheat Sheet"

**Inputs:**
- Vocal type (Rap, Pop, R&B, Rock, Trap, Lo-Fi, Soul, Indie)
- DAW (Ableton, Logic, FL Studio, Pro Tools, Reason)
- Budget (Free plugins only / Mid-tier $0–$200 / Professional)
- Problem (optional): Too harsh / No presence / Too much room / Sounds thin

**Output — interactive SVG chain diagram:**
Gate → High-Pass → De-Noise → EQ (corrective) → Compression → Saturation → EQ (creative) → De-Ess → Reverb → Delay

Each processor node: clickable card showing recommended plugin per budget tier, exact settings for selected genre, one-line "why."

**Famous vocal chain presets (one-click):**
- Billie Eilish: dark, whisper-close, high-pass 200Hz, room reverb
- Drake: warm, analog sat, subtle hall, doubler
- Arctic Monkeys: gritty, driven preamp, bright plate, telephone filter
- Frank Ocean: intimate, lo-fi texture, barely-there reverb
- The Weeknd: lush, choir doubles, long pre-delay

**Claude API "Explain Why" panel:** Click any processor → panel explains why it's at that chain position, what moving it does, what problem it solves for the selected vocal type.

**Tech:** Claude API (claude-sonnet-4-6), SVG chain diagram, curated settings JSON per genre/budget.

---

### TOOL 6 — ClearCheck (Sample Clearance Risk Assessor)
**Slug:** `/tools/clearcheck`
**Group:** D — Claude API
**SEO:** "sample clearance risk calculator", "do I need to clear this sample", "sample clearance checker"
**Beats:** No equivalent tool exists anywhere
**Scope:** US only (copyright law, attorney network)
**Monetization:** Layer 1 free (email gate), Layer 2 $29 one-time, Layer 3 attorney listing fee revenue

**Layer 1 — Free (email gate):**
Inputs: sample length (seconds), recognizability (Famous/Well-Known/Obscure/Unknown), commercial use (Yes/No), source label tier (Major/Indie/Independent/Unknown), type (direct sample vs interpolation)

Output: Risk score Low/Medium/High/Critical + plain-English explanation + specific risk factors driving the score.

Example output: "A 4-second recognizable hook from a major label recording used commercially = CRITICAL. This sample requires clearance from both the master rights holder (record label) and publishing rights holder (songwriter/publisher) before distribution. Most major distributors including DistroKid and TuneCore will remove your track if detected."

**Layer 2 — $29 one-time:**
- Full clearance intelligence report
- Estimated clearance cost range by sample type
- Who to contact: rights holder identification guidance
- Clearance request letter template (pre-filled with sample details)
- Platform-specific risk: DistroKid / Spotify Content ID / YouTube Content ID behavior

**Layer 3 — Attorney Referral (listing fee model, US only):**
- Directory of music rights attorneys accepting clearance work
- Attorney listing fee: $X/month (pricing TBD)
- Attorneys listed by state, specialization, typical fee range
- Lead flows to producer's chosen attorney — MPW does not broker the transaction
- Attorney applies to be listed via a form — MPW editorial approves listings
- No per-lead tracking. No referral fee per transaction. Clean monthly listing model.

**Layer 3 build note:** Attorney directory built as a separate page `/tools/clearcheck/attorneys` — simple filterable list. Attorneys self-serve apply to list. Steve approves. This is entirely buildable without TruClarify involvement.

**Tech:** Claude API for risk assessment reasoning, pure JS for input collection and Layer 1 output, Stripe for Layer 2 payment (future), static HTML attorney directory for Layer 3.

---

### TOOL 7 — Mix Translation System Simulator
**Slug:** `/tools/mix-translation`
**Group:** C — SVG multi-panel
**SEO:** "mix translation checker", "how does my mix sound on different speakers", "why does my mix sound bad on phone"
**Beats:** No interactive equivalent — every guide is a blog post
**Monetization:** Email gate on "Download Translation Report PDF"
**Note:** Also serves as the embed tool for the `mix-translation` Bible flagship entry

**Inputs:**
- Three frequency balance sliders: Low (sub/bass level), Mid (presence), High (air/brightness)
- Optional: integrated LUFS of mix

**Output — 8 system simulation panels (SVG EQ curve per system):**
- NS10s: flat mids, rolled bass and top
- Laptop speakers: no sub, boosted 2kHz
- Phone speaker: 300Hz–5kHz only
- Earbuds: exaggerated bass, forward high-mid
- Car stereo: boosted bass, boosted 2kHz
- Club system: extended sub, high SPL
- TV speakers: narrow range, centered 1–4kHz
- Bluetooth speaker: compressed, rolled extremes

Per system: simulated frequency curve + danger zones highlighted + specific fix ("Your low end will disappear on phone — consider cutting 80–120Hz by 2dB and boosting 200Hz for perceived warmth on small speakers")

Translation score: 0–100 across all systems combined.

**Tech:** SVG multi-panel display, frequency simulation math in JS (not real-time DSP — calculated approximations based on known system response profiles).

---

### TOOL 8 — Plugin Chain Signal Flow Visualizer
**Slug:** `/tools/signal-flow-visualizer`
**Group:** C — Drag-and-drop SVG
**SEO:** "signal flow music production", "plugin order mixing", "mixing chain order online"
**Beats:** Every competitor is a static diagram or a blog post list
**Monetization:** Email gate on "Download Chain as PDF"

**Inputs:**
- Drag processor categories from panel onto chain: Dynamics / EQ / Saturation / Time-Based / Utility
- Select specific processor type within each category
- Toggle enable/disable per processor

**Output:**
- SVG animated signal flow — line flows through chain left to right
- Per processor: what it does to signal at that position + why order matters
- Danger zones highlighted: saturation before limiting = clipping warning, EQ before compression = different behavior callout
- Famous chain presets (one-click): SSL Bus Chain, Vintage Neve Chain, Modern Hip-Hop Master Chain, Mastering Chain
- Each preset loads all processors in correct order with explanatory text

**Tech:** Vanilla JS drag-and-drop (no framework), SVG animated flow line, curated chain database in JSON.

---

### TOOL 9 — Reference Track Decoder
**Slug:** `/tools/reference-decoder`
**Group:** D — Claude API
**SEO:** "how to analyze reference tracks", "reference track decoder", "mix like famous album"
**Beats:** No equivalent — every guide is generic advice
**Monetization:** Email gate on "Download Full Reference Report PDF"

**Inputs:**
- Reference track selector: dropdown of 200 curated landmark records (with search)
- Optional: your mix's LUFS + frequency balance description

**Output — full production intelligence brief:**
- Estimated frequency balance profile
- Dynamic range (PLR from known published data)
- Arrangement structure summary
- 5 notable production techniques specific to that record
- Producer DNA: who made it, what gear, what era
- 5 specific actionable things to try in your own mix based on that record

**Database:** 200 curated landmark records in locked JSON. Name, year, producer, estimated PLR, frequency character, key techniques, gear notes. Claude API generates the "5 things to try" section based on the record's locked data + producer's mix description.

**Tech:** Curated 200-record JSON database, Claude API for recommendation generation, pure JS for UI.

---

### TOOL 10 — Producer BPM DNA
**Slug:** `/tools/bpm-dna`
**Group:** C — D3.js bell curve
**SEO:** "BPM calculator music production", "what BPM should my beat be", "genre BPM reference"
**Beats:** Every competitor is a static BPM range table
**Monetization:** Free — drives newsletter signups via "Get weekly genre BPM reports"

**Inputs:**
- Your BPM (slider 60–200)
- Genre selector (Trap, House, Techno, Drum & Bass, Hip-Hop, Pop, R&B, Afrobeats, Reggaeton, Ambient, Film Score)

**Output:**
- D3 bell curve showing genre's BPM distribution — producer's tempo marked with amber line
- Where they sit: "Your 140 BPM sits at the high end of Trap — most tracks are 130–138"
- Tempo relationships: half-time (70), double-time (280), polyrhythmic relationships (7/8, 5/4 equivalents)
- Famous tracks at nearby tempos (within ±5 BPM) — curated per genre
- Feel finder: same BPM, different subdivisions — shows how 140 BPM feels different as straight 16ths vs triplets vs dotted 8ths

**Genre BPM distribution data:** Curated in locked JSON — actual distribution curves based on published genre analysis, not made-up ranges.

**Tech:** D3.js bell curve, curated BPM distribution JSON, vanilla JS.

---

### TOOL 11 — Stem Quality Tester
**Slug:** `/tools/stem-quality-tester`
**Group:** D — Claude API + Web Audio
**SEO:** "stem separation quality checker", "AI stem separation artifacts", "fix stem separation"
**Beats:** Nothing exists — this is an entirely new category of tool
**Monetization:** Email gate on "Download Stem Cleanup Report"

**Inputs:**
- Upload separated stem file (WAV/MP3, up to 20MB)
- Select stem type (Vocals / Drums / Bass / Other)
- Separation tool used (Spleeter / Demucs / LALAL.AI / Moises / Other)
- Brief description of what sounds wrong (optional)

**Output:**
- Web Audio API waveform display of uploaded stem
- Claude API quality assessment based on: stem type + tool + user description + waveform characteristics
- Artifact risk score (Low/Medium/High) per artifact type: bleed / phasing / harmonic loss / transient smearing
- Recommended cleanup chain: specific processors in correct order for that stem type and artifact combination
- Famous producer note: how professionals handle stem separation artifacts in real sessions

**Tech:** Web Audio API for waveform visualization, FileReader API for upload, Claude API for assessment engine.
**Note:** No audio processing happens server-side. Assessment is descriptive/analytical, not DSP.

---

### TOOL 12 — Frequency Conflict Detector v2
**Slug:** `/tools/frequency-conflict-detector` (upgrade, same URL)
**Group:** A — Pure JS/SVG upgrade
**SEO:** Already ranking — upgrade protects and extends existing authority
**Beats:** Current v1 is the gold standard — v2 makes it unreachable
**Monetization:** Email gate on "Download Conflict Report PDF"

**V2 additions over current v1:**
- Second instrument input simultaneously — see two instruments' frequency content overlaid
- Conflict zone highlighted as colored overlay (red = high conflict, amber = moderate, clear = safe)
- Fix recommendation engine: suggested cut frequency, suggested dB amount, suggested alternative EQ move
- Masking probability score: how likely is this conflict to cause problems in a mix
- Genre context: "In trap production, bass/808 conflict in this range is expected and managed with sidechain — not EQ"

**What stays from v1:** All current functionality, all current presets, all current visual design. This is additive — never replace what works.

**Tech:** Extend existing pure JS — do not rewrite. Add second instrument channel and recommendation engine on top of current architecture.

---

## PART 6 — SESSION 80 SCOPE (DEDICATED TOOL SESSION)

### Session Declaration: BUILD + DESIGN

**What gets done:**

**Deliverable 1 — Hub Redesign** (`/tools/index.html`)
Three-zone architecture. Zone 1 hero with Loudness Penalty running live. Zone 2 flagship cards (placeholder cards for tools not yet built — shows tool name, description, "Coming Soon" state). Zone 3 existing grid preserved and improved. New search, new filter pills, new card format. SEO keyword content block below Zone 3.

**Deliverable 2 — Loudness Penalty Calculator** (`/tools/loudness-penalty.html`)
Full standalone page. Pure JS — fastest build. Hub hero tool. Email gate on PDF export. Full SEO, schema, share bar, embed code.

**Deliverable 3 — Session Prompt Files for All Remaining Tools**
`C:\Users\swarn\OneDrive\Desktop\mpw-scripts\tool-build-prompts\`
One complete self-contained `.md` file per tool. These are what Steve hands to each parallel session. Written and committed in Session 80 so parallel sessions can begin immediately in Session 81+.

**Deliverable 4 — `MPW-TOOL-HUB-SPEC.md`**
Locked spec file committed to GitHub containing the full frozen design system, hub architecture, all 12 tool specs, all 14 Bible embed tool specs, quality checklist, commit checklist. The frozen input for all future tool sessions.

**What does NOT happen in Session 80:**
- No Bible entry writing
- No Bible writer code
- No article production
- No Arrangement Blueprint (canvas complexity — Session 81)
- No Mix Fingerprint (D3 — Session 81)
- No Vocal Chain Builder (Claude API — Session 82)
- No ClearCheck (attorney directory spec needed first)

### Session 80 Start Protocol

1. Read `MPW-TOOL-BUILD-SPEC.md` (frozen design spec)
2. Read this document in full
3. Fetch live `/tools/index.html` from GitHub — extract current card format and nav
4. Fetch live `/tools/frequency-conflict-detector.html` — visual gold standard
5. Fetch live `bible/compression.html` — extract share bar pattern
6. Build Deliverable 2 (Loudness Penalty) — test on mobile before proceeding
7. Build Deliverable 1 (Hub Redesign) — integrates Loudness Penalty as hero
8. Write all session prompt files (Deliverable 3)
9. Commit all via one Trees API commit
10. Commit `MPW-TOOL-HUB-SPEC.md`

### Never Rules — Tool Build Specific

- Never load `style.css` or `../css/style.css` in tool pages — 600px black blob shapes (S68)
- Never use `.hero` or `.container` class names in tool pages — global CSS conflict (S68)
- Never use `innerHTML` in tool JS — Netlify CSP blocks on `/tools/*` (S65)
- Never use `setTimeout` for tool init — use direct function calls (S46)
- Never hardcode tool counts — dynamic JS only (S77)
- Never commit without running `mpw_precommit_check.py` first (S68)
- Never embed a tool in a Bible entry before the tool page is committed and live
- Never use model `claude-sonnet-4-5` — correct model is `claude-sonnet-4-6` (S68)
- Never call Netlify functions via custom domain — use `classy-haupia-be8e43.netlify.app` (S67)
- Never build a tool without embed code block and share bar
- Never build a tool without its monetization hook (email gate on download) coded from day one
- Never gate the tool itself — gate the download/export output only (locked rule)
- Never start any tool build without reading `MPW-TOOL-BUILD-SPEC.md` first (S68)
- Never commit a tool page without updating `/tools/index.html` hub card in same Trees API commit
- Never build a parallel session tool without a complete self-contained session prompt file

### `mpw_precommit_check.py`
**Location:** `C:\Users\swarn\OneDrive\Desktop\mpw-scripts\mpw_precommit_check.py`
**Runs:** Before every single commit. No exceptions.
**What it catches:** Raw tokens in files, missing SEO elements, broken placeholder strings, innerHTML usage, style.css references in tool pages, hero/container class conflicts, missing share bars, missing embed codes.
**Run:** `python mpw_precommit_check.py [filename]`

---

## PART 7 — SESSION SEQUENCE

```
Session 79 (this session):  Planning + scoping + locking blueprint — COMPLETE
Session 80:                 Hub redesign + Loudness Penalty + session prompt files
Session 81 (parallel ×4):  Group A pure JS tools (4 tools simultaneously)
Session 82 (parallel ×3):  Group B Web Audio tools (3 tools simultaneously)
Session 83 (parallel ×4):  Group C advanced tools — Round 1 (4 tools)
Session 84 (parallel ×3):  Group C advanced tools — Round 2 + Group D tools
Session 85:                 Curation files build (insights, misconceptions, WTRN, genre data)
Session 86:                 Curation files continued (tracks Wave 1, producer DNA Wave 1, plugins)
Session 87:                 Bible flagship writer build + test on eq
Session 88+:                Bible writer parallel batch runs
```

### Owner Actions Required Before Session 80

| Action | Priority |
|---|---|
| Affiliate applications — Plugin Boutique, Amazon, Loopmasters, Sweetwater, PluginFox | P0 REVENUE BLOCKER |
| GSC indexing — all 42 tools + reverb + compression | P0 |
| Replace quotes.json with quotes_merged_v2.json in mpw-scripts\ | P1 |
| Save mpw_bible_writer_06.py to mpw-scripts\ | P1 |
| Add 1 resonance quote to quotes file | P1 |
| Fix 4 zero-coverage quote gaps (sidechain-compression, mix-translation, sidechain-ducking, reference-mixing) | P1 |
| Decision: ClearCheck attorney listing fee pricing | P2 |

---

*Document locked: Session 79 — May 28, 2026*
*Companion: MPW-FLAGSHIP-WRITER-BLUEPRINT.md*
*Next session: Session 80 — Dedicated Tool Build + Hub Redesign*

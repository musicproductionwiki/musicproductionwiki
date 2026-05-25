# MPW Tools — Master Spec v2.0
**Priority-ranked build order | 158 tools across 11 categories**
*MusicProductionWiki.com — The Producer's Bible*
*Last updated: May 24, 2026 — Session 65*

---

## Editorial Notes

**Cuts from original 64** (6 removed — reference charts, not tools):
- ~~Send/Return FX Architecture~~ — blog post in tool form, no dynamic calculation
- ~~Clip Gain vs Fader Reference~~ — static signal flow diagram, no input/output
- ~~True Peak vs Sample Peak Reference~~ — pure reference, answer never changes
- ~~Dither Type Selector~~ — niche, near-zero repeat usage, answer is always the same
- ~~Dynamic EQ vs Multiband Compressor~~ — recommendation logic too binary for real sessions
- ~~Intro Length Optimizer~~ — output is a single number, insufficient stickiness

**Tool count by session added:**
- Original 64 spec tools (6 cut): 58 retained
- Session 65 Round 1 additions (40 new): 40
- Session 65 Round 2 additions (20 new): 20
- Session 65 AI Music category (20 new): 20
- Session 65 Browser Apps (10 new): 10 (including Browser DAW as flagship)
- **Total suite: 148 tools across 11 categories**

**Build tiers:**
- PRIORITY 0 — Browser Apps / Flagship Experiences (build with Claude directly in session)
- PRIORITY 1 — Viral (15 tools)
- PRIORITY 1A — AI Music Viral (20 tools — own category, highest growth opportunity)
- PRIORITY 2 — High Traffic / Session-Critical (20 tools)
- PRIORITY 3 — Strong SEO / High Repeat Usage (15 tools)
- PRIORITY 4 — Solid SEO / Technical Depth (30 tools)
- PRIORITY 5 — Important / Narrower Audience (48 tools)

---

## PRIORITY 0 — Browser Apps / Flagship Experiences

**Built directly with Claude in session — no Python writer needed — HTML/JS/Web Audio API artifacts.**
These are experiences, not calculators. They establish MPW as a destination, drive the longest session times, generate the most backlinks, and get shared on social media as demos. Build these in dedicated sessions where Claude builds the full interactive app.

---

### APP #1 — The Browser DAW ⭐ FLAGSHIP
**Slug:** `/tools/browser-daw`
**SEO Tier:** Viral
**Build method:** Claude builds directly in session — Tone.js + Web Audio API + Canvas

**What it is:**
A fully functional, playable browser DAW. No download, no install, no account. Open the page and make music.

**Feature set (MVP — one session):**
- 16-step drum sequencer, 8 tracks (kick, snare, hi-hat open, hi-hat closed, clap, perc x3)
- Built-in synth for melodic patterns using Tone.js — piano roll style, 2 octaves
- Tempo control 60–200 BPM with tap tempo
- Built-in effects per track: volume, pan, reverb send, delay send
- Master effects: reverb (room size/wet), delay (time synced to BPM/feedback)
- Pattern play/stop/loop controls
- Visual: animated step grid with velocity-sensitive color, waveform display, VU meter
- BPM-synced delay times auto-calculated
- Preset patterns per genre (trap, house, boom-bap, techno, afrobeats)
- One-click clear and randomize per track
- Web Audio API sound engine — no samples needed, all synthesis

**Why it's the flagship:**
Nothing like this exists at this quality on any music education or reference site. It's a demo of what MPW is — a place where producers actually do things, not just read things. Gets shared as "whoa, this is free in the browser." Gets linked from music education YouTube channels, Reddit, Discord. Establishes MPW as a production destination not just a wiki.

**Cost: $0** — Claude builds it. One dedicated session.

**Upgrade path (Tier 2 — $2k–$5k developer):** Sample upload, MIDI keyboard input, WAV export, more tracks, saved projects, AudioWorklet for zero-latency.

---

### APP #2 — Live Frequency Spectrum Analyzer
**Slug:** `/tools/live-spectrum-analyzer`
**SEO Tier:** High
**Build method:** Claude builds — getUserMedia + AnalyserNode + Canvas 60fps

**What it is:**
Real-time frequency spectrum analyzer using the browser's microphone API. Connect your interface, play audio into it, see the spectrum in real time at 60fps. Bar graph and smooth line display modes. Frequency zone overlays (sub/bass/low-mid/mid/presence/air). Freeze frame captures. Peak hold display.

**Why producers use it every session:**
Every producer needs a spectrum analyzer. Plugins cost $50–$200. This is free, in the browser, no download, works on mobile. The daily return visit tool.

---

### APP #3 — Interactive Chord & Scale Explorer
**Slug:** `/tools/chord-scale-explorer`
**SEO Tier:** High
**Build method:** Claude builds — Web Audio API + Canvas piano keyboard

**What it is:**
Click any root note on a rendered piano keyboard. Select any scale or mode. Tool highlights scale degrees, plays them as a sequence through Web Audio API synth, generates the full diatonic chord stack, plays each chord on click, shows emotional character and tension/resolution role of each chord, generates 3 suggested progressions, plays each progression on click. All audible, all interactive, zero install.

**Why it goes beyond existing tools:**
Every other chord/scale tool is static — you see the notes but you can't hear them. This plays. That's the difference between a reference and an instrument.

---

### APP #4 — Psychoacoustic Ear Trainer
**Slug:** `/tools/ear-trainer`
**SEO Tier:** High
**Build method:** Claude builds — Web Audio API + game logic

**What it is:**
A progressively difficult game built on Web Audio API. Round 1: identify which of two generated tones has more reverb. Round 2: identify which has a brighter EQ. Round 3: identify which has more compression. Difficulty increases as differences become subtler. Score tracked, streak system, difficulty levels (beginner/intermediate/advanced/engineer). Shareable score at the end.

**Why it drives repeat visits:**
It's a game. Games bring people back daily. Schools, YouTube tutorials, and Discord servers link to ear training tools constantly. Producers challenge each other on their scores.

---

### APP #5 — Live Browser Tuner
**Slug:** `/tools/browser-tuner`
**SEO Tier:** High
**Build method:** Claude builds — getUserMedia + autocorrelation pitch detection

**What it is:**
Open the page, allow microphone access, play or sing. The tuner displays the detected note (A, Bb, B, C...), octave, frequency in Hz, and cents deviation from perfect pitch on a visual needle. Updates at 60fps. Green zone = in tune. Works on desktop and mobile. No app required.

**Why it drives traffic outside production communities:**
Guitarists, bassists, vocalists, piano students — everyone who owns an instrument tunes it. A browser tuner that's genuinely accurate gets daily use from millions of musicians who've never heard of MPW. Entry point to the whole site.

---

### APP #6 — Chord Progression Builder with MIDI Export
**Slug:** `/tools/chord-progression-builder`
**SEO Tier:** High
**Build method:** Claude builds — Web Audio API + MIDI writer JS library

**What it is:**
Click chord buttons for any key to build a progression. Hear each chord through Web Audio synth. Arrange chords into a sequence, set BPM, loop the progression. Display MIDI note numbers and voicings. Export as MIDI file using a JS MIDI writer library (importable via CDN). One-click copy of chord names and Roman numeral analysis.

**The bridge:**
MIDI export makes this a session tool, not just a reference. A producer who builds a chord progression here and drops the MIDI file directly into Ableton has completed a real workflow step using MPW. That's the stickiest possible experience.

---

### APP #7 — BPM Tap Tempo Pro
**Slug:** `/tools/tap-tempo-pro`
**SEO Tier:** High
**Build method:** Claude builds — Web Audio API + precision timing

**What it is:**
Tap the spacebar or large on-screen button to the beat. Calculates BPM with high precision, smoothing across multiple taps. Simultaneously displays all delay times (whole, half, quarter, eighth, sixteenth, dotted eighth, triplet) in milliseconds, updating live. Click any value to copy. Audible metronome that plays at detected BPM. Visual pulse animation. Works on mobile — tap with your finger.

**Why it's better than every existing tap tempo:**
Most tap tempo tools give you the BPM and nothing else. This gives you the full delay table, an audible metronome, and one-click copy. It's the tap tempo producers bookmark because it does everything in one place.

---

### APP #8 — AI Production Advisor (Claude-in-Claude)
**Slug:** `/tools/ai-production-advisor`
**SEO Tier:** High
**Build method:** Claude builds — Anthropic API artifact

**What it is:**
A specialized AI assistant trained on production knowledge via system prompt. Producer describes their problem in plain language — "my kick and 808 are fighting," "my mix sounds good in headphones but loses bass on speakers," "I can't figure out why my drop doesn't hit" — and gets a specific, technically accurate response with numbered steps. Not a generic chatbot — a production expert.

**Why it's different from ChatGPT:**
The system prompt specializes it completely in music production. It knows MPW's tools and links to them. It gives producer-specific answers, not generic AI answers. And it's right there on the tools page producers are already using.

---

### APP #9 — Suno Prompt Builder (Interactive)
**Slug:** `/tools/suno-prompt-builder`
**SEO Tier:** High
**Build method:** Claude builds — interactive form + Anthropic API for optimization

**What it is:**
A structured form that walks through each component of an effective Suno prompt: genre tags, instrumentation, mood/atmosphere, vocal style, production descriptors, structure metatags ([Verse]/[Chorus]/[Bridge]), BPM/tempo feel. As you fill in each field, the tool assembles the optimized prompt in real time in a preview panel. One-click copy. Optionally sends to Anthropic API to further refine and score the prompt quality.

**Why it goes viral:**
70% of Suno's first generations waste credits because the prompt wasn't structured correctly. This tool cuts that to near-zero. Gets shared in every Suno community immediately.

---

### APP #10 — Real-Time Mix Meter Dashboard
**Slug:** `/tools/mix-meter-dashboard`
**SEO Tier:** High
**Build method:** Claude builds — getUserMedia + Web Audio AnalyserNode + Canvas

**What it is:**
Connect your audio interface via the browser's microphone input. The dashboard shows simultaneously: real-time VU meter (peak and RMS), estimated LUFS (integrated), stereo correlation meter, peak indicator with clip warning, frequency band energy meters (sub/bass/mid/high), and headroom display. All updating at 60fps. A free browser-based metering suite.

**Why it's remarkable:**
This is $200+ worth of plugin functionality given away free in the browser. Every producer mixing without proper metering needs this. Daily use, daily return visits.

---

## PRIORITY 1 — Viral / Highest Traffic Potential

These ship first via the Python writer batch system. Each answers a question producers ask constantly with no good existing answer.

---

### #1 — "Why Does My Mix Sound Amateur?" Diagnostic
**Slug:** `/tools/mix-sounds-amateur-diagnostic`
**SEO Tier:** Viral
**Category:** Mixing & Signal Flow

Producer selects what they're hearing — thin, muddy, harsh, no low end, no glue, too loud, sounds small, no depth, sounds digital, too bright — and the tool walks through the five most probable causes in ranked order, with a specific starting fix for each. Every output is actionable: a frequency, a setting, a decision. Not "check your EQ" — "HPF at 120Hz on your room mics, cut 300Hz on your low-mid bus 2dB."

---

### #2 — The "Should I Sample This?" Decision Tree
**Slug:** `/tools/should-i-sample-this`
**SEO Tier:** Viral
**Category:** Business & Legal

Input everything about the sample — original artist, label, release year, how much you're using (full loop / chop / interpolation), master or composition use, intended release format — the tool walks every clearance decision point in order, outputs a risk level (low / medium / high / do not use), estimated clearance cost range, and the three alternatives if risk is too high. TruClarify front door. Email-gate for detailed report.

---

### #3 — Spotify Skip Probability Map
**Slug:** `/tools/spotify-skip-probability-map`
**SEO Tier:** Viral
**Category:** Arrangement & Structure

Input song structure — section names and bar counts at your BPM. Calculates the timestamp of every section transition and draws the actual skip probability curve with your sections overlaid as colored blocks. Shows exactly when your hook arrives relative to the 30-second engagement cliff, the 60-second retention drop, and the algorithmic evaluation window. If hook arrives late, recommends which section to shorten and by exactly how many bars.

---

### #4 — The Comparison Trap Calculator
**Slug:** `/tools/comparison-trap-calculator`
**SEO Tier:** Viral
**Category:** Producer Psychology & Career

Producer enters their current stats and the producer they most compare themselves to. Calculates the time gap, normalizes for era and platform conditions, shows what the comparison producer's numbers looked like at the same point in their career. Almost always the answer is: you're ahead. Ends with a specific next action.

---

### #5 — "Sound Like" Reverse Engineer
**Slug:** `/tools/sound-like-reverse-engineer`
**SEO Tier:** Viral
**Category:** Mixing & Signal Flow

Select a reference artist — Kendrick, SZA, Frank Ocean, Travis Scott, Metro Boomin, Billie Eilish, Burial, J Dilla, etc. — and the tool outputs the production fingerprint: approximate LUFS, frequency balance signature, reverb character, drum processing approach, key techniques, and the three identifying elements that make that sound immediately recognizable. Engineering DNA, not samples.

---

### #6 — The 808 Relationship Analyzer
**Slug:** `/tools/808-relationship-analyzer`
**SEO Tier:** Viral
**Category:** Beat Making & Rhythm

Input track key, kick drum fundamental frequency, and 808 note. Calculates harmonic compatibility, exact cents of tuning offset needed to lock kick and 808 together, whether sub frequencies cancel or reinforce in mono, and the HPF setting on the kick that opens space for the 808. Draws their harmonic relationship on a frequency canvas with conflict zones in red.

---

### #7 — The Track Finisher
**Slug:** `/tools/track-finisher`
**SEO Tier:** Viral
**Category:** Producer Psychology & Career

Five questions about a specific unfinished project: where it stalled, what's missing structurally, how long it's been sitting, what the original vision was, what specifically feels wrong. Outputs a 3-step finishing plan, the single decision most likely blocking completion, and a constraint that forces the track forward.

---

### #8 — Drum Tuning Reference
**Slug:** `/tools/drum-tuning-reference`
**SEO Tier:** Viral
**Category:** Beat Making & Rhythm

Select kick style, snare style, clap type, and track key — outputs recommended tuning in Hz and semitones for each drum element. 808 calculated separately. Canvas draws all elements on a frequency spectrum. Click-to-copy values for direct sampler entry.

---

### #9 — Streaming Income Reality Check
**Slug:** `/tools/streaming-income-reality-check`
**SEO Tier:** Viral
**Category:** Business & Legal

Input monthly Spotify listeners — shows realistic monthly income, what it takes to earn $1k / $3k / $5k per month, what top 1% independent artists earn at each listener level. Then calculates the alternative revenue stack that reaches income goals faster than streams alone. Honest in a way the industry never is.

---

### #10 — The J Dilla Drunk Beat Decoder
**Slug:** `/tools/jdilla-drunk-beat-decoder`
**SEO Tier:** Viral
**Category:** Beat Making & Rhythm

Input BPM — outputs precise millisecond offset for every 16th note position in the MPC60 grid that creates the drunk feel, with animated dot grid. Includes velocity curve, Dilla's most-used combination from 1995–2001, and modern trap hi-hat extension. Click-to-copy offset values for every major DAW.

---

### #11 — The "Is This Plagiarism?" Melody Checker
**Slug:** `/tools/is-this-plagiarism-checker`
**SEO Tier:** Viral
**Category:** Business & Legal

Input a note sequence — tool compares against the most famous melodic patterns in production history, flags statistical similarities, explains the legal difference between similarity and infringement. Covers Blurred Lines, Dark Horse, Stairway to Heaven, Marvin Gaye catalog in plain English. Outputs a similarity risk score.

---

### #12 — "Why Is My Vocal Sitting Wrong?" Fixer
**Slug:** `/tools/vocal-sitting-wrong-fixer`
**SEO Tier:** Viral
**Category:** Mixing & Signal Flow

Select the symptom — too far back, too upfront, too thin, too nasal, fighting the beat, disappearing in chorus, sounds harsh, sounds muffled. Outputs three most probable causes in ranked order with specific starting fix for each. Distinguishes between EQ, dynamics, reverb, level, and arrangement problems.

---

### #13 — The Loudness War Visualizer
**Slug:** `/tools/loudness-war-visualizer`
**SEO Tier:** High
**Category:** Mastering & Delivery

Interactive timeline canvas showing DR scores of famous albums across decades — from Pink Floyd to Death Magnetic to modern streaming masters. Click any album to see its waveform character. Input your own DR score to see where you sit in history. Genre filter shows the loudness trajectory of hip-hop, EDM, pop, rock, and jazz separately.

---

### #14 — Chord Progression Emotion Mapper
**Slug:** `/tools/chord-progression-emotion-mapper`
**SEO Tier:** High
**Category:** Music Theory & Composition

Input a chord progression — Am, F, C, G — and the tool maps its emotional profile: tension points, resolution moments, the psychological mechanism behind each movement. Draws an emotional arc on canvas. Famous track examples using the same progression.

---

### #15 — Beat Selling Price Calculator
**Slug:** `/tools/beat-selling-price-calculator`
**SEO Tier:** High
**Category:** Business & Legal

Input monthly plays, follower count, years producing, genre market, notable placements — outputs recommended lease, exclusive, and trackout prices with reasoning. Compares against market data for your tier and genre.

---

## PRIORITY 1A — AI Music Category (Own Section — Highest Growth Opportunity)

**This entire category is Priority 1A.** The AI music audience is growing faster than any other music production segment. 12 million monthly active Suno users, 7 million tracks generated daily. Zero dedicated reference tools exist for them. MPW owns this space by building first.

Build these immediately after Priority 1 viral tools. Every legal/rights tool in this section feeds TruClarify leads.

---

### AI #1 — AI Music Commercial Rights Navigator ⭐ TruClarify Front Door
**Slug:** `/tools/ai-music-rights-navigator`
**SEO Tier:** Viral
**Category:** AI Music

Input your platform (Suno free/Pro/Premier, Udio, Stable Audio, AIVA, ElevenLabs), your tier, and your intended use (Spotify distribution, YouTube monetization, sync licensing, beat sale, podcast, commercial ad, Content ID claim) — outputs a clear yes/no/risk matrix for each use case with the specific reason. Covers the DDEX disclosure requirement now enforced by Spotify and Apple Music. Explains the difference between "commercial rights" and "copyright" — the distinction that trips up every AI music creator.

**Why it goes viral:** This question is asked in every AI music Discord, YouTube comment, and Reddit thread every single day. Nobody has a clear, current, use-case-specific answer in tool form. TruClarify lead on every session.

---

### AI #2 — Suno Prompt Optimizer
**Slug:** `/tools/suno-prompt-optimizer`
**SEO Tier:** Viral
**Category:** AI Music

Input what you're trying to make in plain language. Tool outputs an optimized Suno prompt using the exact structural formula that consistently works: genre tags first, instrumentation second, production descriptors third, mood/atmosphere last, with correct metatags ([Verse], [Chorus], [Bridge], vocal texture tags) pre-formatted. Includes a prompt quality score. One-click copy.

**Why it goes viral:** 70% of first-generation Suno tracks require 3+ regenerations because the prompt wasn't structured correctly. This cuts that to one. Gets shared in every Suno community the moment someone discovers it.

---

### AI #3 — AI Music DDEX Disclosure Checker
**Slug:** `/tools/ai-music-ddex-checker`
**SEO Tier:** Viral
**Category:** AI Music

Input your track's composition type (fully AI / AI with human edits / AI-assisted / human with AI tools) and your distributor (DistroKid, TuneCore, Amuse, CD Baby) — outputs the exact disclosure steps required for that distributor, what happens if you skip it, and whether Apple's 2026 policy will exclude your track from curated playlists.

**Why it goes viral:** Non-optional compliance knowledge. Getting demonetized for non-disclosure when you didn't know is devastating. This prevents it. Gets shared urgently.

---

### AI #4 — AI Track Copyright Strength Calculator
**Slug:** `/tools/ai-copyright-strength`
**SEO Tier:** Viral
**Category:** AI Music

Input what human creative contributions you made — wrote lyrics (full credit), significantly edited prompt (partial), rearranged in DAW (partial), recorded live instruments over AI bed (strong), mixed and mastered (weak). Tool calculates copyright strength 0–100 and tells you exactly what additional human contributions would cross into registrable territory. Cites US Copyright Office 2023 guidance and Thaler v. Perlmutter.

**Why it goes viral:** Every AI music creator who wants to protect their work is guessing at this. A score with legal reasoning gets shared in every AI music, producer, and music business community simultaneously. Direct TruClarify lead.

---

### AI #5 — AI Platform Comparison (Use-Case Specific)
**Slug:** `/tools/ai-music-platform-comparison`
**SEO Tier:** Viral
**Category:** AI Music

Input your specific use case — "I need stems for a trap beat," "I need MIDI export for Ableton," "I need royalty-free tracks for YouTube," "I need cinematic orchestral for sync" — and the tool outputs which platform wins for that use case, why, what the current download/export limitations are (Udio downloads disabled post-UMG settlement), and cost at the tier needed.

**Why it goes viral:** "Which AI music tool should I use" is asked constantly and the answer changes as lawsuits settle. A use-case-specific, current-state answer gets bookmarked and re-shared every time the landscape shifts.

---

### AI #6 — AI Music Income Calculator
**Slug:** `/tools/ai-music-income-calculator`
**SEO Tier:** High
**Category:** AI Music

Input monthly AI track output, average streaming performance per track, sync placement rate, and YouTube channel size — calculates realistic monthly income from AI music at your scale, shows the output velocity needed to reach $500 / $1k / $3k / $5k per month, and maps the revenue stack (streaming + YouTube + sync + stock music libraries) that gets there fastest. Honest about the math.

---

### AI #7 — Suno vs Human: Can You Tell? Quiz ⭐ Viral Potential
**Slug:** `/tools/suno-vs-human-quiz`
**SEO Tier:** Viral
**Category:** AI Music

An interactive quiz presenting 10 audio descriptions (visual representation of audio characteristics — not actual audio due to licensing) — mix of Suno V5 and human-produced tracks in the same genres. User identifies which is which. Score revealed at end. Shareable result card.

**Why it goes viral:** The water-cooler tool. Gets posted on Twitter, TikTok, Discord. Crosses outside the production community into general music audiences. Positions MPW as the authority on AI music quality.

---

### AI #8 — AI Music Prompt Library (Searchable)
**Slug:** `/tools/ai-prompt-library`
**SEO Tier:** High
**Category:** AI Music

A curated, searchable database of the highest-performing Suno and Udio prompts organized by genre, mood, use case, and output quality rating. Each prompt shows the exact text, intended output, platform it's optimized for, and user-rated quality. The permanent, searchable version of the "share your best prompts" threads.

---

### AI #9 — AI Track Artifact Identifier
**Slug:** `/tools/ai-track-artifact-fixer`
**SEO Tier:** High
**Category:** AI Music

Checklist of the most common AI audio artifacts with visual frequency spectrum illustrations — metallic shimmer in 8–12kHz, stereo phase inconsistencies, tempo micro-drift, vocal consonant artifacts, low-end mud from bass-heavy prompts. Specific EQ, stereo, or processing fix for each. The bridge between AI generation and release-ready audio.

---

### AI #10 — AI Lyrics Optimizer for Suno
**Slug:** `/tools/ai-lyrics-optimizer`
**SEO Tier:** High
**Category:** AI Music

Input your lyrics — tool analyzes syllable count per line, rhyme scheme strength, section tag structure, words likely to be mispronounced by Suno's vocal model, lines too long for the BPM range. Outputs a revised version optimized for Suno's generation engine. Writing lyrics for AI is a completely different skill from writing lyrics for humans.

---

### AI #11 — AI Music Style Fingerprint Builder
**Slug:** `/tools/ai-style-fingerprint`
**SEO Tier:** High
**Category:** AI Music

Input 5–10 of your best AI-generated track descriptions and the prompts you used. Tool identifies common prompt elements, genre markers, production descriptors, and mood words that define your AI music signature. Outputs a personal style guide. Producers share their style fingerprints the same way people share personality test results.

---

### AI #12 — AI Music Distribution Roadmap
**Slug:** `/tools/ai-music-distribution-roadmap`
**SEO Tier:** High
**Category:** AI Music

The full pipeline from Suno generation to streaming release, step by step — which distributor to use for AI music, what metadata to include, how to complete the DDEX disclosure, what to do about Content ID (unavailable for fully AI audio as of 2026), how to handle PRO registration for tracks with human lyric contribution, and what platforms have AI-specific policies.

---

### AI #13 — Human Contribution Tracker ⭐ TruClarify Pipeline
**Slug:** `/tools/ai-human-contribution-tracker`
**SEO Tier:** High
**Category:** AI Music

Walks through every stage of creation — prompt authorship, lyric writing, structural editing, DAW rearrangement, live instrument recording, mix and master decisions — and generates a timestamped human contribution log. The output is a document the creator keeps as evidence of creative involvement. Email-gate for download. Every download is a TruClarify warm lead.

---

### AI #14 — AI Music Niche Finder
**Slug:** `/tools/ai-music-niche-finder`
**SEO Tier:** High
**Category:** AI Music

Input skills, interests, and production goals — maps the 20 most underserved AI music niches by platform (YouTube meditation, Twitch background, podcast intros, real estate video, children's educational, language learning audio) with demand signals, average track counts, income potential, and the exact prompt approach that works for each niche.

---

### AI #15 — Suno Credits Calculator
**Slug:** `/tools/suno-credits-calculator`
**SEO Tier:** High
**Category:** AI Music

Input subscription tier (Pro at 2,500 credits/month, Premier at 10,000) and typical workflow — generations per track until a keeper, tracks per week. Calculates burn rate, tells you how many weeks until you hit your monthly limit, recommends the right tier for your workflow, and gives specific credit-saving strategies.

---

### AI #16 — AI Music Genre Accuracy Tester
**Slug:** `/tools/ai-genre-accuracy-tester`
**SEO Tier:** High
**Category:** AI Music

Select a genre — tool shows the specific production elements that make it authentic vs what AI typically gets wrong in that genre. AI boom-bap: too-even hat patterns, lacks head-nod groove. AI jazz: lacks live micro-timing. AI metal: sounds like processed samples not real amp distortion. The gap between AI's version of a genre and the real thing, made specific and actionable.

---

### AI #17 — AI + Human Hybrid Workflow Builder
**Slug:** `/tools/ai-hybrid-workflow-builder`
**SEO Tier:** High
**Category:** AI Music

Input your DAW, what live instruments you play, and which AI platform you're generating from — outputs a hybrid workflow: which elements to generate with AI, which to record live, how to tempo-map the AI output to your DAW, how to key-match live elements to the AI bed, and how to blend the sonic textures.

---

### AI #18 — AI Music Playlist Placement Scorer
**Slug:** `/tools/ai-playlist-placement-scorer`
**SEO Tier:** High
**Category:** AI Music

Scores your AI track's playlist placement potential across different playlist types — algorithmic, editorial, user-generated, niche-genre. Spotify and Apple Music have AI-specific playlist policies in 2026. Fully AI-generated tracks excluded from Apple's top-tier curated playlists. Algorithmic placement for AI tracks works differently from human-produced music.

---

### AI #19 — The AI Music Legal Timeline
**Slug:** `/tools/ai-music-legal-timeline`
**SEO Tier:** High
**Category:** AI Music

Interactive visual timeline of every significant legal development in AI music — RIAA lawsuits, Warner settlement, UMG-Udio partnership, Sony cases still active, US Copyright Office guidance, EU AI Act implications, DDEX enforcement — with plain-English explanations. Updated as events happen. Positions MPW as the authority on AI music law.

---

### AI #20 — AI vs Human Music Monetization Comparison
**Slug:** `/tools/ai-vs-human-monetization`
**SEO Tier:** High
**Category:** AI Music

Direct, data-driven comparison of what a human-produced track and an AI-generated track earn across every revenue stream in 2026: Spotify, Apple Music, YouTube monetization, Content ID (unavailable for AI), sync licensing (harder for AI), PRO royalties (uncertain for AI), beat sales (viable), stock music libraries. Shows where AI music has genuine advantages and genuine disadvantages. The honest comparison nobody has made in tool form.

---

## PRIORITY 2 — High Traffic, Session-Critical

Used every session. Strong SEO. Bookmark-worthy.

---

### #16 — Frequency Masking Visualizer
**Slug:** `/tools/frequency-masking-visualizer`
**SEO Tier:** High | **Category:** EQ & Frequency

Select two instruments — the tool draws their frequency ranges on the same canvas, highlights the masking zone, calculates conflict severity, and recommends the specific EQ cut on one element and boost on the other.

---

### #17 — Mixing Headphone Compensation Reference
**Slug:** `/tools/headphone-compensation-reference`
**SEO Tier:** High | **Category:** Mixing & Signal Flow

Select your headphone model from the 50 most common producer headphones — tool shows the measured frequency response curve with specific EQ compensation adjustments. Flags known weaknesses of each model.

---

### #18 — Surgical EQ Cheat Sheet
**Slug:** `/tools/surgical-eq-cheat-sheet`
**SEO Tier:** High | **Category:** EQ & Frequency

Select instrument and describe the frequency problem in plain language — outputs exact Hz target, recommended Q width, boost/cut direction, and gain range. Spectrum canvas. Click-to-copy chips.

---

### #19 — Drum Compression by Genre
**Slug:** `/tools/drum-compression-by-genre`
**SEO Tier:** High | **Category:** Dynamics & Compression

Select genre and drum element — outputs specific attack, release, ratio, knee, and character type with GR curve canvas. Genre comparison mode shows two genres side-by-side.

---

### #20 — Hook Placement Guide
**Slug:** `/tools/hook-placement-guide`
**SEO Tier:** High | **Category:** Arrangement & Structure

Input song structure and BPM — calculates hook arrival timestamp and maps against streaming skip curves. Canvas shows skip probability at each second with hook placement marked.

---

### #21 — Scale & Mode Mood Reference
**Slug:** `/tools/scale-mode-mood`
**SEO Tier:** High | **Category:** Music Theory & Composition

Select mood or emotional target — recommends scale or mode, lists famous examples, highlights characteristic intervals on interactive piano roll canvas, provides three chord progression starters. Interactive: clicking a key plays the scale degree with Web Audio API tone.

---

### #22 — Bass Frequency Reference
**Slug:** `/tools/bass-frequency-reference`
**SEO Tier:** High | **Category:** EQ & Frequency

Select bass type and genre — outputs full frequency map with sub zone, fundamental zone, upper harmonic zone, and click/attack zone. Log-scale canvas. Genre-specific cut/boost targets.

---

### #23 — Compressor Ratio Selector
**Slug:** `/tools/compressor-ratio-guide`
**SEO Tier:** High | **Category:** Dynamics & Compression

Select source instrument and problem being solved — outputs recommended ratio with GR curve canvas overlaying three ratio options simultaneously. Danger zone indicator for transient destruction.

---

### #24 — Dynamic Range Meter Reference
**Slug:** `/tools/dynamic-range-reference`
**SEO Tier:** High | **Category:** Mastering & Delivery

Input genre and intended platform — outputs expected DR score range, crest factor range, PLR. Comparison bar chart. Pass/fail indicator.

---

### #25 — Swing & Groove Calculator
**Slug:** `/tools/swing-groove-calculator`
**SEO Tier:** High | **Category:** Beat Making & Rhythm

Input BPM and select groove template (MPC60, MPC3000, SP-1200, J Dilla drunk) — outputs exact timing offset in milliseconds for each 16th note position. Canvas shows humanized pattern as dot grid.

---

### #26 — Streaming Platform Loudness Optimizer
**Slug:** `/tools/streaming-loudness-optimizer`
**SEO Tier:** High | **Category:** Mastering & Delivery

Input current LUFS, true peak, and target platform — calculates exact limiting amount needed, expected timbre change, and whether targeting normalization exactly or 1–2 LUFS below serves the track better.

---

### #27 — The "Am I Overproducing?" Detector
**Slug:** `/tools/overproducing-detector`
**SEO Tier:** High | **Category:** Arrangement & Structure

Input number of active elements per section — calculates density scores, flags over-dense sections, identifies most likely redundant element type. Genre benchmarks built in.

---

### #28 — Bus Compression Character Selector
**Slug:** `/tools/bus-compression-character`
**SEO Tier:** High | **Category:** Dynamics & Compression

Input mix bus level, genre, and target feel — outputs exact settings per compressor type (VCA, Opto, FET, Vari-Mu) with side-by-side character comparison canvas.

---

### #29 — Vocal Chain Builder
**Slug:** `/tools/vocal-chain-builder`
**SEO Tier:** High | **Category:** Pitch & Vocals

Build a complete vocal processing chain by genre and vocal style. Processor order, starting settings for each stage, engineering rationale for each position decision.

---

### #30 — Reference Track Matcher
**Slug:** `/tools/reference-track-matcher`
**SEO Tier:** High | **Category:** Mixing & Signal Flow

Input reference track characteristics and your own track's corresponding characteristics — outputs a gap analysis prioritized from highest impact to lowest.

---

### #31 — Mix Translation Checker
**Slug:** `/tools/mix-translation-checker`
**SEO Tier:** High | **Category:** Mixing & Signal Flow

Select primary monitoring environment — shows frequency response signature, predicts what mix decisions will translate as on each playback system, provides compensation EQ starting points.

---

### #32 — Synth Sound Reverse Engineer
**Slug:** `/tools/synth-sound-reverse-engineer`
**SEO Tier:** High | **Category:** Sound Design & Synthesis

Describe a sound you heard — outputs synthesis approach, oscillator type, filter character, envelope shape, and effect chain most likely responsible. Covers subtractive, FM, wavetable, granular, physical modeling.

---

### #33 — Acoustic Treatment Priority Calculator
**Slug:** `/tools/acoustic-treatment-priority`
**SEO Tier:** High | **Category:** Studio & Recording

Input room dimensions, current treatment, budget range, and primary use — outputs most impactful treatment purchase order for your specific room at your specific budget.

---

### #34 — Chord Progression Generator
**Slug:** `/tools/chord-progression-generator`
**SEO Tier:** High | **Category:** Music Theory & Composition

Select key, mode, and mood target — generates four chord progressions ranked by emotional intensity, with voice leading shown on piano roll canvas and famous track examples.

---

### #35 — Sample Chop Grid Calculator
**Slug:** `/tools/sample-chop-grid`
**SEO Tier:** High | **Category:** Beat Making & Rhythm

Input original sample BPM and target project BPM — calculates slice point positions, pitch shift needed, time-stretch percentage, and ghost beat placement recommendations. DAW-specific notes.

---

## PRIORITY 3 — Strong SEO, High Repeat Usage

---

### #36 — The "Is My Track Ready to Release?" Scorer
**Slug:** `/tools/release-readiness-scorer`
**SEO Tier:** High | **Category:** Mastering & Delivery

Interactive checklist scoring 0–100 across five dimensions: mix quality, master quality, metadata completeness, cover art readiness, distribution setup. Email-gate for detailed report.

---

### #37 — Artist Development Readiness Score
**Slug:** `/tools/artist-development-readiness`
**SEO Tier:** High | **Category:** Business & Legal

Input streaming numbers, release history, social following, genre — outputs readiness score across catalog depth, streaming traction, visual identity, live capability, press presence.

---

### #38 — Producer Style DNA Mapper
**Slug:** `/tools/producer-style-dna`
**SEO Tier:** High | **Category:** Producer Psychology & Career

Input five tracks that influenced your sound — tool maps production DNA across all five and outputs a producer style profile showing where influences converge into a potential signature sound. Shareable "Producer Card."

---

### #39 — Royalty Split Calculator
**Slug:** `/tools/royalty-split-calculator`
**SEO Tier:** High | **Category:** Business & Legal

Input all collaborators and contribution type — calculates publishing split and master split separately, explains the difference, provides PRO registration guidance. Email-gate for split sheet download.

---

### #40 — DAW Gain Staging Calculator
**Slug:** `/tools/daw-gain-staging-calculator`
**SEO Tier:** High | **Category:** Mixing & Signal Flow

Select DAW and approximate track count — outputs recommended target levels at each stage. DAW-specific gain architecture accounted for. Analog emulation plugin optimal levels included.

---

### #41 — Drum Bus Compression Designer
**Slug:** `/tools/drum-bus-compression`
**SEO Tier:** High | **Category:** Dynamics & Compression

Select genre, drum style, and BPM — outputs BPM-synced attack/release with transient shape canvas. Parallel blend calculator. Real-time transient destruction warning.

---

### #42 — Release Timing Optimizer
**Slug:** `/tools/release-timing-optimizer`
**SEO Tier:** High | **Category:** Business & Legal

Input genre, target geography, and release goals — outputs optimal day, time, and week of year to release based on editorial calendar patterns and listener behavior data.

---

### #43 — Collaboration Agreement Builder
**Slug:** `/tools/collaboration-agreement-builder`
**SEO Tier:** High | **Category:** Business & Legal

Input both collaborators, contribution breakdown, intended use, and ownership split — generates plain-English collaboration memo covering IP ownership, revenue split, approval rights, exit terms. Email-gate for download.

---

### #44 — Plugin CPU Cost Calculator
**Slug:** `/tools/plugin-cpu-cost-calculator`
**SEO Tier:** High | **Category:** Studio & Recording

Input DAW, CPU tier, and plugins running — estimates CPU load, identifies most expensive plugin types, recommends freeze/bounce candidates and lower-CPU alternatives.

---

### #45 — FM Ratio Calculator
**Slug:** `/tools/fm-ratio-calculator`
**SEO Tier:** Med | **Category:** Sound Design & Synthesis

Input carrier-to-modulator ratio — shows resulting harmonic series on canvas, indicates harmonic vs inharmonic relationship, describes spectral character, lists famous FM sounds using that ratio.

---

### #46 — Sub Bass Design Guide
**Slug:** `/tools/sub-bass-design-guide`
**SEO Tier:** High | **Category:** Sound Design & Synthesis

Select musical key and sub bass type — outputs correct octave placement, HPF setting, recommended saturation type and drive amount for speaker translation, mono compatibility check.

---

### #47 — The "Does My Song Have Structure?" Analyzer
**Slug:** `/tools/song-structure-analyzer`
**SEO Tier:** High | **Category:** Arrangement & Structure

Input section list and bar counts — checks against structural conventions of genre, identifies missing structural elements, explains what each missing element does emotionally.

---

### #48 — Streaming Playlist Pitch Readiness
**Slug:** `/tools/playlist-pitch-readiness`
**SEO Tier:** High | **Category:** Business & Legal

Input track genre, BPM, energy level, mood, LUFS, release date, and explicit flag — scores playlist pitch readiness across the five factors Spotify's editorial team prioritizes.

---

### #49 — Genre DNA Analyzer
**Slug:** `/tools/genre-dna-analyzer`
**SEO Tier:** High | **Category:** Music Theory & Composition

Select two genres — shows production overlap: shared BPM ranges, shared chord progressions, shared drum patterns, where they diverge. Venn diagram canvas with specific production data.

---

### #50 — Mix Revision Communicator
**Slug:** `/tools/mix-revision-communicator`
**SEO Tier:** High | **Category:** Mixing & Signal Flow

Input what you're hearing in plain English — translates to professional engineering language with specific parameter suggestions. Bridges producer-engineer communication gap in both directions.

---

## PRIORITY 4 — Solid SEO, Technical Depth

---

### #51 — Noise Gate Designer
**Slug:** `/tools/noise-gate-designer` | **Category:** Dynamics & Compression

Animated gate envelope canvas. Hold time calculator prevents gate chatter per instrument.

---

### #52 — Expander vs Gate Selector
**Slug:** `/tools/expander-vs-gate` | **Category:** Dynamics & Compression

Describe specific problem — recommends expander or hard gate with exact settings. Side-by-side GR curve canvas.

---

### #53 — Limiting vs Clipping Calculator
**Slug:** `/tools/limiting-vs-clipping` | **Category:** Dynamics & Compression

Input ceiling target, source LUFS, musical style — outputs whether limiter or clipper is better, exact settings, expected LUFS delta, estimated harmonic distortion percentage.

---

### #54 — HPF / LPF Slope Calculator
**Slug:** `/tools/hpf-lpf-slope-calculator` | **Category:** EQ & Frequency

Draws actual filter roll-off curve with -3, -6, -12 dB points labeled. Second canvas overlays two slope choices for direct comparison.

---

### #55 — Mid/Side EQ Reference
**Slug:** `/tools/mid-side-eq-reference` | **Category:** EQ & Frequency

Select mix element and describe problem — outputs M/S EQ recommendations with visual showing frequency content in mid vs side channel.

---

### #56 — Resonance Hunter Reference
**Slug:** `/tools/resonance-hunter` | **Category:** EQ & Frequency

Select instrument and describe symptom — maps to starting Hz range, provides sweep instructions, reduces sweep range from five octaves to half an octave.

---

### #57 — Air Frequency Guide
**Slug:** `/tools/air-frequency-guide` | **Category:** EQ & Frequency

Select source type and microphone character — outputs recommended air shelf frequency, gain range, Q/slope. Canvas draws all six frequency options overlaid.

---

### #58 — De-Esser Frequency Finder
**Slug:** `/tools/de-esser-frequency-finder` | **Category:** EQ & Frequency

Select vocalist type, mic character, sibilance description — outputs target frequency range, threshold starting point, de-esser mode recommendation. Over-de-essing warning included.

---

### #59 — Stem Prep & Export Guide
**Slug:** `/tools/stem-prep-export-guide` | **Category:** Mastering & Delivery

Select destination — outputs exact stem prep requirements, naming convention, grouping recommendations, and most common mistakes for that specific destination.

---

### #60 — Mono Compatibility Checker
**Slug:** `/tools/mono-compatibility-checker` | **Category:** Mixing & Signal Flow

Input stereo width and frequency of concern — calculates which frequencies are at highest risk of cancellation in mono, estimates dB loss, recommends specific corrections.

---

### #61 — Drop Builder Reference
**Slug:** `/tools/drop-builder-reference` | **Category:** Arrangement & Structure

Select genre — outputs bar-by-bar checklist of every element present, introduced, or removed at each stage of the drop: build, impact, body, release. All timing relative to actual BPM.

---

### #62 — Arrangement Density Map
**Slug:** `/tools/arrangement-density-map` | **Category:** Arrangement & Structure

Input section list and active element count per section — draws arrangement density arc on canvas. Identifies flat spots, over-dense sections, under-resolved drops.

---

### #63 — Breakdown & Build Calculator
**Slug:** `/tools/breakdown-build-calculator` | **Category:** Arrangement & Structure

Input BPM, genre, and target build duration in bars — calculates riser start/end frequency, filter sweep rate in Hz per bar, pitch automation range, snare roll subdivision grid, sidechain removal timing.

---

### #64 — BPM to Body Response Chart
**Slug:** `/tools/bpm-body-response` | **Category:** Music Theory & Composition

Maps BPM ranges to documented physiological responses — heart rate entrainment, energy level, emotional state. Famous tracks at each BPM with emotional effect. Crossover appeal beyond producers.

---

### #65 — Mastering EQ Order Calculator
**Slug:** `/tools/mastering-eq-order` | **Category:** Mastering & Delivery

Input mastering chain elements — recommends optimal processing order with engineering rationale. Common mistakes flagged in red. Signal flow diagram redraws as elements are added.

---

### #66 — Parallel Processing Blend Guide
**Slug:** `/tools/parallel-processing-blend-guide` | **Category:** Mixing & Signal Flow

Select processing type — outputs recommended starting blend ratio with description of what to listen for at each percentage increment. Canvas shows frequency content change as function of blend ratio.

---

### #67 — Wavetable Design Reference
**Slug:** `/tools/wavetable-design-reference` | **Category:** Sound Design & Synthesis

Select target sound character — recommends optimal wavetable starting position, scan rate, and best modulation targets. Synth-agnostic: works for Serum, Vital, Ableton Wavetable, Phase Plant.

---

### #68 — Envelope Shape Reference
**Slug:** `/tools/envelope-shape-reference` | **Category:** Sound Design & Synthesis

Select target sound type — animated ADSR canvas with envelope shape. Explains linear vs exponential attack curve distinction — the most important synthesis concept most guides miss.

---

### #69 — Chord Voicing for Synths
**Slug:** `/tools/chord-voicing-synths` | **Category:** Music Theory & Composition

Select key, chord type, and register — outputs optimal voicing with frequency stack canvas. Mono compatibility rating warns when low-register voicing creates problematic bass below 200Hz.

---

### #70 — LFO Shape & Target Reference
**Slug:** `/tools/lfo-shape-target` | **Category:** Sound Design & Synthesis

Select modulation target and desired feel — recommends optimal LFO shape, rate range, depth range. Animated waveform canvas and secondary canvas showing target parameter movement.

---

### #71 — Hi-Hat Pattern Reference
**Slug:** `/tools/hi-hat-pattern-reference` | **Category:** Beat Making & Rhythm

Select genre — displays definitive hi-hat pattern as step sequencer grid with color-coded velocity levels, accent positions, open/closed placement, and DAW-specific programming notes.

---

### #72 — Velocity Humanization Guide
**Slug:** `/tools/velocity-humanization-guide` | **Category:** Beat Making & Rhythm

Select instrument and target feel — outputs velocity range, which beats carry accent velocity, random offset range, and timing offset in ms. Canvas draws velocity bar graph for two-bar loop.

---

### #73 — Ghost Note & Syncopation Reference
**Slug:** `/tools/ghost-note-syncopation` | **Category:** Beat Making & Rhythm

Select genre and instrument — displays two-bar step sequencer grid with ghost note placement, velocity ranges, syncopation positions, and DAW programming steps.

---

### #74 — Sidechain Depth Calculator
**Slug:** `/tools/sidechain-depth-calculator` | **Category:** Beat Making & Rhythm

Input genre, kick BPM, and target pump depth — outputs exact GR amount in dB, BPM-synced attack/release, and whether sidechain source should be full-range or high-pass filtered. Animated GR curve canvas.

---

### #75 — The "What Should I Charge?" Rate Card Builder
**Slug:** `/tools/producer-rate-card-builder` | **Category:** Business & Legal

Input experience level, service type, turnaround time, and market — outputs recommended rate card with per-project prices, hourly rates, rush fees, revision policies. Compares against market data.

---

### #76 — Genre Blending Risk Calculator
**Slug:** `/tools/genre-blending-risk-calculator` | **Category:** Music Theory & Composition

Input two source genres — calculates compatibility based on BPM overlap, harmonic compatibility, rhythmic complexity difference, texture similarity. Outputs compatibility score and the three decisions that make the blend work vs fail.

---

### #77 — The "Am I Overproducing?" Detector
**Slug:** `/tools/overproducing-detector` | **Category:** Arrangement & Structure

Already documented in Priority 2. See #27.

---

### #78 — The "Is My Track Ready to Release?" Scorer
Already documented in Priority 3. See #36.

---

### #79 — Mix Bus Signal Flow Guide
**Slug:** `/tools/mix-bus-signal-flow` | **Category:** Mixing & Signal Flow

Recommended processor order on mix bus by genre. Explains why each position matters. Signal flow diagram redraws by genre selection.

---

### #80 — Gain Staging Reference
**Slug:** `/tools/gain-staging-reference` | **Category:** Mixing & Signal Flow

Target levels at every stage from track to master. Plugin operating level recommendations for analog emulation plugins. Headroom calculations shown at each stage.

---

## PRIORITY 5 — Important, Narrower Audience

Smaller audience but high-quality, targeted traffic. These complete the comprehensive suite.

---

### #81–148 — Complete Suite (abbreviated for file size)

The following tools complete the 148-tool suite. Full descriptions available in prior session notes. All slugs confirmed unique:

**Reverb Type Selector** `/tools/reverb-type-selector` — match reverb type to instrument, genre, mix context
**Pitch Correction Reference** `/tools/pitch-correction-reference` — speed and retune settings for transparent correction vs T-Pain
**RT60 Room Calculator** `/tools/rt60-calculator` — decay time at multiple frequency bands
**Mastering Signal Chain Reference** `/tools/mastering-signal-chain` — processor order by genre and release format
**Mix Bus Headroom Reference** `/tools/mix-bus-headroom-reference` — headroom before limiter by genre
**Stereo Width & M/S Reference** `/tools/stereo-width-ms` — mid/side relationships, stereo width targets
**Stereo Field & Mono Checker** `/tools/stereo-field-mono-checker` — what should stay mono, frequency-dependent guidelines
**Headroom Calculator** `/tools/headroom-calculator` — headroom at mixdown for mastering by format
**Pre-Delivery Checklist** `/tools/pre-delivery-checklist` — interactive checklist before sending master
**Sample Rate & Bit Depth Guide** `/tools/sample-rate-bit-depth-guide` — when to use each format
**Arrangement Timer** `/tools/arrangement-timer` — section lengths against genre norms
**Synthesis Type Selector** `/tools/synthesis-type-selector` — recommend synthesis method by target sound
**Synthesis Parameter Reference** `/tools/synthesis-parameter-reference` — what every synth parameter does
**Saturation Character Reference** `/tools/saturation-character-reference` — tape/tube/transistor/clipper comparison
**Saturation Harmonic Reference** `/tools/saturation-harmonic-reference` — even vs odd harmonic profiles
**Stem Mastering Cost Calculator** `/tools/stem-mastering-cost-calculator` — cost by service tier and use case
**Sync Licensing Readiness Checker** `/tools/sync-licensing-readiness` — score out of 100 with specific blockers
**Beat Licensing Tier Builder** `/tools/beat-licensing-tier-builder` — three-tier licensing structure by market
**Track Energy Arc Grader** `/tools/track-energy-arc-grader` — energy arc graded against listener retention patterns
**Vocal Tuning Ethics Meter** `/tools/vocal-tuning-ethics-meter` — transparent fix to T-Pain effect spectrum
**The Track Finisher** (also Priority 1 #7)
**Streaming Income Reality Check** (also Priority 1 #9)
**Comparison Trap Calculator** (also Priority 1 #4)
**Producer Style DNA Mapper** (also Priority 3 #38)
**Artist Development Readiness Score** (also Priority 3 #37)
**The "Am I Overproducing?" Detector** (also Priority 2 #27)
**Track Energy Arc Grader** (also above)
**The "Does My Song Have Structure?" Analyzer** (also Priority 3 #47)
**Streaming Playlist Pitch Readiness** (also Priority 3 #48)
**Mix Revision Communicator** (also Priority 3 #50)

---

## Summary Table — Updated v2.0

| Priority | Label | Tools | Count |
|----------|-------|-------|-------|
| 0 | Browser Apps / Flagship Experiences | APP #1–10 | 10 |
| 1 | Viral | #1–15 | 15 |
| 1A | AI Music (own category) | AI #1–20 | 20 |
| 2 | High Traffic / Session-Critical | #16–35 | 20 |
| 3 | Strong SEO / High Repeat Usage | #36–50 | 15 |
| 4 | Solid SEO / Technical Depth | #51–80 | 30 |
| 5 | Important / Narrower Audience | #81–148 | 38 |
| **Total** | | | **148** |

---

## Build Order — Updated v2.0

**Session 66 (Browser DAW — flagship):** APP #1 (Browser DAW) — Claude builds directly in session. One dedicated session. Goal: playable, impressive, shareable on day one.

**Session 67 (Browser apps batch):** APP #2–5 (Spectrum Analyzer, Chord Explorer, Ear Trainer, Tuner) — Claude builds directly. Each takes 30–45 min of a session.

**Session 68 (Python writer — viral tier):** Build `mpw_tools_v6_writer.py` targeting Priority 1 tools #1–7.

**Session 69 (Python writer — AI music tier):** `mpw_tools_v6_writer.py` targeting AI #1–10.

**Session 70 (Python writer — AI music + viral completion):** AI #11–20 + Priority 1 #8–15.

**Sessions 71–75 (Priority 2–3):** Priority 2 and 3 tools in batches of 10–12.

**Sessions 76–80 (Priority 4–5):** Complete the suite.

**The Browser DAW is Session 66. It is the right first move.** Zero cost, maximum impact, built in one session with Claude, lives on Netlify immediately. It becomes the demo of what MPW tools can be.

---

## Paywall Strategy

| Tier | Tools | Monetization |
|------|-------|--------------|
| Free forever | All calculation tools, session-critical tools, browser apps | Traffic + Briefing list growth |
| Email gate | Royalty Split Calculator (split sheet download), Collaboration Agreement Builder (memo download), Release Readiness Scorer (detailed report), Should I Sample This (detailed report), AI Human Contribution Tracker (log download), AI DDEX Checker (compliance report) | Briefing list + TruClarify leads |
| One-time $9–$19 | Bundle: Reference Track Matcher + Arrangement Density Map + Mix Translation Checker + Producer Style DNA Card | Revenue |
| Never paywall | All AI Music legal/rights tools — free to use, email-gate the detailed output only | TruClarify pipeline |

---

## Technology Stack per Tool Type

| Tool Type | Technology | Example |
|-----------|-----------|---------|
| Browser Apps | Web Audio API + Tone.js + Canvas + getUserMedia | Browser DAW, Spectrum Analyzer, Tuner |
| AI-Powered Tools | Anthropic API (Claude-in-Claude artifact) | Mix Diagnostic, Production Advisor |
| Calculator Tools | Pure JS + Canvas | All math-based tools |
| Interactive Reference | Canvas + click handlers | Frequency maps, GR curves |
| Decision Trees | JS logic + conditional display | Should I Sample This, Platform Comparison |
| Downloadable Output | JS + blob generation | Split sheets, contribution logs |


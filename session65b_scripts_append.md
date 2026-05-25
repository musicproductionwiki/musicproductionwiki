---

# SESSION 65 UPDATE — SCRIPTS (Part 2) — May 24, 2026

## mpw_tools_v6_writer.py — Architecture Update

Full architecture confirmed in session65_scripts_append.md. Additional detail from this session:

### New Tool Categories Requiring Writer Updates

The v6 writer must handle three distinct tool types that were not in the original spec:

**Type A — Standard Calculator Tools (majority of 148 tools)**
Same architecture as existing v5 tools: two-pass JSON spec then HTML/JS. Canvas drawing, createElement chains, genre selectors, plugin tier cards, famous presets, live warning logic.

**Type B — AI-Powered Tools (AI Music category and Mix Diagnostic)**
These tools call the Anthropic API on the client side. The writer generates the tool HTML/JS with the API call baked in. The system prompt for each tool is frozen in the writer. These tools reason, not just calculate.

Key pattern:
```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [{role: "user", content: userInput}]
  })
});
```

Note: API key is handled by the artifact infrastructure — writer does NOT hardcode API keys.

**Type C — Decision Tree / Rights Tools (AI Music legal tools, Should I Sample This)**
These are logic-tree tools, not calculators. Input flows through a structured decision tree and outputs a risk level, recommendation, and next steps. Writer generates the JS decision tree from a structured data spec.

### Browser App Scripts — NOT Python Writer

Browser Apps (Priority 0) are built directly in Claude sessions, not via the Python writer. They are:
- Committed directly to `/tools/[slug].html` via GitHub API
- Not batch-generated
- Built interactively with Steve reviewing design in real time
- Each gets a dedicated session or half-session

**Browser App build checklist (apply to every app):**
- [ ] No innerHTML anywhere (Netlify CSP)
- [ ] SC constant for closing script tags if Python is involved (N/A for direct builds)
- [ ] Mobile-responsive (test at 375px width)
- [ ] Web Audio API: audio context created on user gesture (not on page load — browsers block autoplay)
- [ ] getUserMedia: graceful fallback if user denies microphone
- [ ] Tone.js imported via CDN: `https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js`
- [ ] Canvas: CSS `width:100%;height:Xpx` not inline width/height attributes
- [ ] Works on mobile (touch events, not just mouse events)
- [ ] Verified in Chrome, Firefox, Safari before commit
- [ ] Added to `/tools/index.html` tool card grid after commit

### Tone.js CDN — Confirmed Available

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

This is the version available via cdnjs.cloudflare.com and confirmed importable in Claude's artifact environment. All Browser App builds use this version.

### MIDI Writer JS — For Chord Progression Builder

```html
<script src="https://cdn.jsdelivr.net/npm/midi-writer-js@2.1.4/build/midi-writer-browser.js"></script>
```

Enables MIDI file export from the Chord Progression Builder app. Produces standard MIDI files the user can drag directly into any DAW.

---

## Browser DAW — Session 66 Build Plan

### Goal
A fully functional, playable browser DAW. Opens on page load, no setup, works on mobile. Producers can make actual music immediately.

### Tech Stack
- **Tone.js** — drum synthesis, melodic synth, transport/scheduling
- **Canvas API** — step grid visualization, VU meter, waveform display
- **Web Audio API** — effects chain (reverb, delay)
- **Pure vanilla JS** — all UI interaction (no frameworks)

### Session 66 Build Order
1. Start with drum sequencer only — 16 steps, 4 tracks (kick, snare, hi-hat, clap), working playback
2. Add melodic synth + piano roll (16 steps, 2 octaves)
3. Add effects (reverb send, delay send) per track
4. Add preset patterns (trap, house, boom-bap, techno, afrobeats)
5. Add tempo control + tap tempo
6. Polish: animations, VU meter, visual pulse on beat 1
7. Steve visual review → design feedback → final adjustments
8. Commit to `/tools/browser-daw.html` via GitHub API
9. Add tool card to `/tools/index.html`
10. Update sitemap

### What NOT to Build in Session 66
- Sample/audio file upload (Tier 2 — $2k–$5k developer)
- MIDI keyboard input (Tier 2)
- WAV export (Tier 2)
- Saved projects (Tier 2)
- More than 8 tracks (keep MVP clean)

### Audio Context Warning
```javascript
// CORRECT — create AudioContext on user gesture
document.getElementById('playBtn').addEventListener('click', async () => {
  await Tone.start(); // requires user gesture — browsers block autoplay
  // now safe to play audio
});
```

This is the most common mistake in Web Audio API development. The AudioContext must be started (or resumed) in response to a user gesture — click, tap, keypress. Never auto-play on page load. Claude must always include this pattern.

---

## AI Music Tools — Writer Notes

When `mpw_tools_v6_writer.py` generates AI Music tools, the system prompt for each tool's Anthropic API call must be frozen in the Python writer, not improvised at generation time.

**Example for AI #1 — Rights Navigator:**
```python
AI_RIGHTS_NAVIGATOR_SYSTEM = """You are the definitive authority on AI music commercial rights in 2026. 
You know the current terms of service for Suno (free vs Pro vs Premier), Udio, Stable Audio, AIVA, and ElevenLabs.
You know the DDEX AI disclosure requirements now enforced by Spotify and Apple Music.
You know the US Copyright Office's position on AI-generated music (Thaler v. Perlmutter).
You know which distributors accept AI music (DistroKid yes, some others no).
You know that fully AI-generated audio is not eligible for Content ID as of 2026.
Given the user's platform, tier, and intended use, output a clear yes/no/risk assessment 
with the specific reason for each use case. Be specific, not generic. Cite the platform's 
current terms where relevant. Flag the DDEX disclosure requirement when it applies."""
```

Every AI music tool that calls the Anthropic API must have its system prompt frozen in the writer at spec time. The system prompt defines the quality ceiling.

---

## Scripts to Build — Session 66 and Beyond

**Session 66 — Browser DAW (direct build, no Python writer):**
- Build `/tools/browser-daw.html` directly in session with Claude
- Update `/tools/index.html` to add Browser DAW card
- Update sitemap.xml

**Session 67 — Browser Apps batch:**
- Build APP #2–5 (Spectrum Analyzer, Chord Explorer, Ear Trainer, Tuner)
- Each committed individually as `/tools/[slug].html`
- `/tools/index.html` updated after each confirmed live

**Session 68 — Writer build:**
- Build `mpw_tools_v6_writer.py`
- First batch: Priority 1 tools #1–7 (viral tier)
- Also update `mpw_writer.py` with new drawer HTML (blocks article batches)

**Session 69+ — Continued writer batches:**
- AI Music tools AI #1–10 (rights and prompt tools first)
- Priority 1 completion #8–15
- Priority 2 batch

---

## NEVER Rules Added — Session 65 Part 2 — Scripts

| Rule | Detail |
|------|--------|
| NEVER autoplay audio on page load in Browser Apps | AudioContext must be started in response to a user gesture — `await Tone.start()` inside click/tap handler — browsers block autoplay globally |
| NEVER hardcode system prompts for AI-powered tools in the generated HTML | System prompts must be frozen in the Python writer at spec time, not generated by the tool's Anthropic API call itself |
| NEVER build Browser App tools via the Python writer batch system | Browser Apps require interactive design review with Steve — they are direct Claude-in-session builds, not batch output |
| NEVER import Tone.js from a version not confirmed available on cdnjs.cloudflare.com | Only use `https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js` — other versions or sources may not be available from Netlify |
| NEVER add a Browser App to /tools/index.html before it is confirmed live on GitHub | Check the live URL before updating the hub page card grid |


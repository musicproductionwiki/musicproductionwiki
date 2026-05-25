---

# SESSION 65 UPDATE — TECH (Part 2) — May 24, 2026

## Browser App Technology Reference

### Web Audio API — Capabilities Confirmed Available

The Web Audio API is built into every modern browser. No CDN import needed. All Browser Apps on MPW can use it immediately.

**What Claude can build with Web Audio API alone:**
- Real oscillators generating sine, square, sawtooth, triangle waves
- Real-time filter effects (lowpass, highpass, bandpass, notch)
- Reverb simulation via ConvolverNode
- Delay effects via DelayNode with feedback loops
- Distortion/overdrive via WaveShaperNode
- Gain/volume control via GainNode
- Real-time frequency spectrum analysis via AnalyserNode (for spectrum visualizer, tuner)
- Microphone input via getUserMedia → MediaStreamSourceNode
- Audio recording via MediaRecorder API
- Panning via StereoPannerNode

**Tone.js additional capabilities (importable via CDN):**
- Musical note names (C4, Bb3, etc.) mapped to frequencies automatically
- Tempo-synced scheduling (Transport — plays events on the beat)
- Pre-built synth voices (Synth, PolySynth, MembraneSynth for kicks, MetalSynth for hi-hats)
- Musical timing (Tone.Time for note values: "8n" = eighth note, "16n" = sixteenth note)
- Automatic BPM management

**CDN import:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js"></script>
```

### getUserMedia — Microphone Input Pattern

```javascript
// Request microphone access
async function initMicrophone() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true, video: false});
    const audioContext = new AudioContext();
    const source = audioContext.createMediaStreamSource(stream);
    const analyser = audioContext.createAnalyser();
    analyser.fftSize = 2048;
    source.connect(analyser);
    // Now analyser.getByteFrequencyData() gives real-time spectrum
    return {audioContext, analyser};
  } catch (err) {
    // User denied microphone or not available
    console.warn('Microphone not available:', err);
    return null;
  }
}
```

**Apps that use microphone:**
- Live Frequency Spectrum Analyzer (APP #2)
- Live Browser Tuner (APP #5)
- Real-Time Mix Meter Dashboard (APP #10)

**Policy:** Always include a graceful fallback when microphone is denied. Show a static reference version of the tool rather than a broken page.

### Audio Context Autoplay Policy — CRITICAL

Every modern browser blocks AudioContext autoplay until a user gesture occurs. This is the most common mistake in browser audio development.

**CORRECT pattern:**
```javascript
let audioStarted = false;

document.getElementById('playButton').addEventListener('click', async () => {
  if (!audioStarted) {
    await Tone.start(); // or new AudioContext() and .resume()
    audioStarted = true;
  }
  // Now safe to play
  transport.start();
});
```

**WRONG pattern (will be silently blocked):**
```javascript
// Do NOT do this — will fail silently in all modern browsers
const synth = new Tone.Synth().toDestination();
synth.triggerAttack("C4"); // blocked — no user gesture
```

All Browser Apps must display a visible "Click to Start" or "Tap to Begin" interface element before attempting any audio output.

### Browser App File Structure

```
repo root/
├── tools/
│   ├── index.html          ← hub page — add card for each new app
│   ├── browser-daw.html    ← APP #1 — Session 66
│   ├── live-spectrum-analyzer.html ← APP #2
│   ├── chord-scale-explorer.html   ← APP #3
│   ├── ear-trainer.html            ← APP #4
│   ├── browser-tuner.html          ← APP #5
│   ├── chord-progression-builder.html ← APP #6
│   ├── tap-tempo-pro.html          ← APP #7
│   ├── ai-production-advisor.html  ← APP #8 (Anthropic API)
│   ├── suno-prompt-builder.html    ← APP #9 (Anthropic API)
│   ├── mix-meter-dashboard.html    ← APP #10
│   └── [existing 36 tool pages]
```

Asset paths for tools: `../css/style.css` and `../js/main.js` — same as current tool pages.

### Browser DAW — Technical Architecture

**Tone.js instruments for Browser DAW:**
```javascript
// Kick drum
const kick = new Tone.MembraneSynth({
  pitchDecay: 0.05,
  octaves: 5,
  envelope: {attack: 0.001, decay: 0.4, sustain: 0, release: 1.4}
}).toDestination();

// Snare (noise + tone)
const snare = new Tone.NoiseSynth({
  noise: {type: 'white'},
  envelope: {attack: 0.001, decay: 0.15, sustain: 0, release: 0.05}
}).toDestination();

// Hi-hat
const hihat = new Tone.MetalSynth({
  frequency: 400,
  envelope: {attack: 0.001, decay: 0.05, release: 0.01},
  harmonicity: 5.1,
  modulationIndex: 32,
  resonance: 4000,
  octaves: 1.5
}).toDestination();

// Melodic synth
const synth = new Tone.PolySynth(Tone.Synth, {
  oscillator: {type: 'triangle'},
  envelope: {attack: 0.02, decay: 0.1, sustain: 0.3, release: 0.8}
}).toDestination();
```

**Step sequencer scheduling pattern:**
```javascript
let step = 0;
const seq = new Tone.Sequence((time) => {
  // Play active steps for each track
  if (grid[0][step]) kick.triggerAttackRelease('C1', '8n', time);
  if (grid[1][step]) snare.triggerAttackRelease('8n', time);
  if (grid[2][step]) hihat.triggerAttackRelease('32n', time);
  // Update visual step indicator
  Tone.getDraw().schedule(() => {
    updateStepDisplay(step);
  }, time);
  step = (step + 1) % 16;
}, null, '16n');
```

### Tools Hub (`/tools/index.html`) — Adding Browser App Cards

When adding a Browser App to the hub page, use this card pattern (consistent with existing 36 tool cards):

```html
<a class="tool-card" href="/tools/browser-daw.html" data-cat="browser-app" data-name="browser daw">
  <div class="tool-card-body">
    <span class="tool-card-name">Browser DAW ⭐</span>
    <span class="tool-card-desc">Make music in your browser. 16-step sequencer, built-in synth, 5 genre presets. No download.</span>
    <span class="tool-card-cat">Browser Apps</span>
  </div>
</a>
```

Add a new category pill to the filter bar:
```html
<button class="tools-cat-btn" data-cat="browser-app">Browser Apps</button>
```

The filter JS already handles any `data-cat` value — no JS changes needed, just add the pill button.

---

## Sitemap — Tools Pages to Add After Browser DAW Live

After Browser DAW is confirmed live on GitHub:

```xml
<url>
  <loc>https://www.musicproductionwiki.com/tools/browser-daw.html</loc>
  <priority>0.9</priority>
  <changefreq>monthly</changefreq>
</url>
```

Priority 0.9 — same as `/tools/` hub — this is a flagship destination page.

---

## AI Music Tools — No New Infrastructure Needed

All 20 AI Music tools (Priority 1A) are static HTML tools generated by `mpw_tools_v6_writer.py` — no new hosting, no backend, no database. They live at `/tools/[slug].html` like every other tool page.

The AI-powered variants (AI #1, #2, #3, #4 — Rights Navigator, Prompt Optimizer, DDEX Checker, Copyright Strength) call the Anthropic API from the browser. This works via the existing artifact API infrastructure. No proxy server needed. No additional cost to run.

The non-API variants (AI #5–20) are pure logic-tree and calculator tools. Pure HTML/JS. No API calls. Zero running cost.

---

## NEVER Rules Added — Session 65 Part 2 — Tech

| Rule | Detail |
|------|--------|
| NEVER create AudioContext before a user gesture in any Browser App | Browsers block all audio autoplay — always create or resume AudioContext inside a click/tap event handler. `await Tone.start()` is the correct pattern with Tone.js |
| NEVER add a "Browser Apps" category pill to `/tools/index.html` until at least one Browser App is live | The filter pill for a category with zero results is confusing — add the pill in the same commit as the first browser app |
| NEVER use a Tone.js CDN URL not verified on cdnjs.cloudflare.com | Unverified CDN URLs may be blocked by Netlify or unavailable — only use confirmed cdnjs URLs |
| NEVER build the Browser DAW with more than 8 tracks in the MVP | Complexity creep kills shipping — 8 tracks, 16 steps, basic effects is the MVP. Upgrade path is paid developer work |
| NEVER commit a Browser App to /tools/ without first adding its card to /tools/index.html in the same Trees API commit | An orphaned tool page with no card in the hub is unfindable from the site |


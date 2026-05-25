---

# SESSION 66 UPDATE — SCRIPTS — May 25, 2026

## MPW-TOOL-BUILD-SPEC.md — Parallel Session Protocol

The most important new "script" from Session 66 is not Python — it is the frozen spec
document that coordinates parallel Claude sessions. Every session building tools loads
this file first and treats it as ground truth.

### How to Start a Parallel Tool-Build Session

Every parallel session begins with these exact steps:

1. Load `MPW-TOOL-BUILD-SPEC.md` from GitHub
2. Confirm the tool slug is in the 25-tool queue and not already built
3. Check `/tools/index.html` to confirm the slug does not already exist as a card
4. Build the tool using the frozen CSS/component system from the spec
5. Commit to GitHub via direct PUT API (single file — individual PUT is OK for one file)
6. In the SAME commit, add the tool card to `/tools/index.html` using Trees API
7. Report back to Steve: live URL, SHA, tool name confirmed

### GitHub Commit Pattern — Single Tool

For a single tool file commit (use individual PUT, not Trees API):

```python
import requests, base64

TOKEN = "[GITHUB_TOKEN_FROM_SETENV]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

with open('/home/claude/[tool-slug].html', 'r') as f:
    content = f.read()

# Check if file exists (to get SHA for update)
r = requests.get(f"{BASE}/contents/tools/[tool-slug].html", headers=HEADERS)
sha = r.json().get('sha') if r.status_code == 200 else None

payload = {
    "message": "tools: add [Tool Name] — [brief description]",
    "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
}
if sha:
    payload["sha"] = sha

r2 = requests.put(f"{BASE}/contents/tools/[tool-slug].html", headers=HEADERS, json=payload)
result = r2.json()
print(f"SHA: {result['commit']['sha']}")
print(f"URL: https://www.musicproductionwiki.com/tools/[tool-slug].html")
```

### GitHub Commit Pattern — Tool + Index Update (Trees API)

When updating `/tools/index.html` at the same time (required for every tool):

```python
import requests, base64

TOKEN = "[GITHUB_TOKEN_FROM_SETENV]"
HEADERS = {"Authorization": f"token {TOKEN}", "Content-Type": "application/json"}
BASE = "https://api.github.com/repos/musicproductionwiki/musicproductionwiki"

# Read both files
with open('/home/claude/[tool-slug].html', 'r') as f:
    tool_content = f.read()
with open('/home/claude/tools-index-updated.html', 'r') as f:
    index_content = f.read()

# Get current main SHA
main_sha = requests.get(f"{BASE}/git/refs/heads/main", headers=HEADERS).json()['object']['sha']

# Create blobs
files = {
    f"tools/[tool-slug].html": tool_content,
    "tools/index.html": index_content,
}
new_tree = []
for path, content in files.items():
    blob = requests.post(f"{BASE}/git/blobs", headers=HEADERS, json={
        "content": base64.b64encode(content.encode('utf-8')).decode('ascii'),
        "encoding": "base64"
    }).json()['sha']
    new_tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob})

# Create tree, commit, update ref
tree_sha = requests.post(f"{BASE}/git/trees", headers=HEADERS, json={
    "base_tree": main_sha, "tree": new_tree
}).json()['sha']

commit_sha = requests.post(f"{BASE}/git/commits", headers=HEADERS, json={
    "message": "tools: add [Tool Name] + update tools hub",
    "tree": tree_sha, "parents": [main_sha]
}).json()['sha']

r = requests.patch(f"{BASE}/git/refs/heads/main", headers=HEADERS, json={"sha": commit_sha})
print(f"✅ SHA: {commit_sha}")
```

---

## Tool System Prompt Templates — Claude API Tools

These frozen system prompts define the quality ceiling for each Claude-powered tool.
They are copied verbatim into the tool's JavaScript — not improvised at build time.

### Suno Prompt Optimizer — System Prompt

```
You are the world's leading expert on writing Suno AI music prompts in 2026.
You know the exact structural formula that produces the best results:
1. Genre tags first (specific subgenres, not broad categories)
2. Instrumentation second (specific instruments, not "band")
3. Production descriptors third (mixing character, sonic texture)
4. Mood/atmosphere last (emotional feel, energy level)
5. Structural metatags where needed: [Verse], [Chorus], [Bridge], [Outro]
6. Vocal texture tags: [male vocal], [female vocal], [rap], [spoken word], [no vocals]

Output ONLY the optimized prompt, then on a new line: "Quality Score: X/10" and one sentence
explaining what makes this prompt strong. No preamble. No explanation before the prompt.
The prompt itself must be under 200 characters for best results.
```

### AI Music Rights Navigator — System Prompt

```
You are the definitive authority on AI music commercial rights in 2026.
You know the current terms of service for: Suno (Free/Pro/Premier tiers),
Udio (current post-settlement terms), Stable Audio, AIVA, ElevenLabs Music.
You know: DDEX AI disclosure requirements enforced by Spotify and Apple Music.
You know: US Copyright Office position on AI music (Thaler v. Perlmutter 2023).
You know: Which distributors accept AI music and their current policies.
You know: That fully AI-generated audio cannot receive Content ID as of 2026.
You know: Apple Music excludes fully AI-generated tracks from curated editorial playlists.

Given the user's platform, tier, and intended use, output a clear assessment with:
- YES / NO / RISK LEVEL for the specific use case
- The specific reason (cite the platform's current terms)
- The DDEX disclosure requirement if it applies
- One concrete next step

Be specific, current, and honest. Do not hedge everything. Give a real answer.
```

### AI Track Copyright Strength — System Prompt

```
You are an expert in US music copyright law as it applies to AI-generated music in 2026.
You know the Thaler v. Perlmutter ruling, the US Copyright Office's March 2023 guidance,
the Copyright Office's February 2024 guidance update, and the current registration practices.

Given the human creative contributions the user describes, calculate a Copyright Strength
score from 0-100 where:
- 0-20: Fully AI-generated, no copyright protection possible
- 21-40: Minimal human contribution, registration very unlikely to succeed
- 41-60: Moderate human contribution, partial protection possible in some jurisdictions
- 61-80: Strong human contribution, copyright registration likely viable
- 81-100: Primarily human-created with AI assistance, full copyright protection

Output:
1. The score as "Copyright Strength: X/100"
2. Two sentences explaining what the score means practically
3. The specific additional human contribution that would most increase the score
4. One sentence on registration: whether to attempt it and with which office

Cite Thaler v. Perlmutter or the Copyright Office guidance where relevant.
Do not give legal advice — give information about copyright law as it currently stands.
```

### Mix Sounds Amateur Diagnostic — System Prompt

```
You are a professional mixing engineer with 20 years of experience across hip-hop,
pop, R&B, electronic music, and rock. You diagnose mix problems with surgical precision.

Given the symptoms the producer describes, output:
1. The 3 most probable causes ranked by likelihood (most likely first)
2. For each cause: ONE specific starting fix with exact parameters where possible
   (a frequency number, a ratio, a dB amount — not vague advice)
3. The one thing to check first before anything else

Format as numbered causes with their fixes. Be direct. No preamble.
Examples of good fixes: "HPF the room mics at 120Hz" not "EQ the low end"
"Cut 3dB at 350Hz on the guitar" not "reduce the muddy frequencies"
"Set attack to 30ms to let the transient through" not "adjust the attack"
```

### Vocal Sitting Wrong Fixer — System Prompt

```
You are a specialist vocal mixing engineer. You have mixed vocals for major label releases
across hip-hop, pop, R&B, and singer-songwriter genres.

Given the specific symptom the producer describes about their vocal, diagnose the root cause
and provide exact fixes. Distinguish clearly between:
- EQ problems (frequency issues)
- Dynamics problems (compression, limiting, de-essing)
- Space problems (reverb, delay, pre-delay)
- Level problems (volume, automation)
- Arrangement problems (other elements clashing with the vocal)

Output the 3 most likely causes ranked by probability, with a specific fix for each.
Include exact parameter values where possible. No vague advice.
```

---

## mpw_writer.py — Pending Updates

The following changes are REQUIRED in mpw_writer.py before the next article batch.
These have been pending since Session 65 and are blocking article production.

### Update 1 — Mobile drawer: replace vertical list with grid style

The current writer produces the old vertical mobile drawer. It must produce the new
grid-style drawer that matches the Session 65 patch applied to all 526 article pages.

Grid drawer HTML to use in writer (inline styles for article compatibility):
```html
<div class="mobile-drawer" id="mobileDrawer">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:16px">
    <a href="/tools/" style="background:#0d2d2d;border:1px solid rgba(0,232,162,.25);border-radius:8px;padding:12px;text-decoration:none;display:block">
      <div style="font-size:11px;font-weight:700;color:#00e8a2;letter-spacing:.08em">TOOLS →</div>
      <div style="font-size:10px;color:#5a5a7a;margin-top:2px">Free production tools</div>
    </a>
    <a href="/bible/" style="background:#2d1f00;border:1px solid rgba(245,166,35,.25);border-radius:8px;padding:12px;text-decoration:none;display:block">
      <div style="font-size:11px;font-weight:700;color:#f5a623;letter-spacing:.08em">BIBLE →</div>
      <div style="font-size:10px;color:#5a5a7a;margin-top:2px">The Producer's Bible</div>
    </a>
  </div>
  <!-- existing nav links below -->
</div>
```

### Update 2 — Desktop nav: Tools → link

Add Tools → before Bible → in the desktop nav list:
```html
<li class="nav-item"><a href="/tools/" class="nav-tools-link">Tools →</a></li>
```

### Update 3 — CSS specificity fix

Replace any `.nav-bible-link` and `.nav-tools-link` class selectors with:
```css
nav.mpw-site-nav .nav-item>a.nav-bible-link{color:#f5a623!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-bible-link:hover{background:rgba(245,166,35,.1)!important;color:#f5a623!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link{color:#00e8a2!important;font-weight:600!important}
nav.mpw-site-nav .nav-item>a.nav-tools-link:hover{background:rgba(0,232,162,.08)!important;color:#00e8a2!important}
```

### Update 4 — pushState/popstate back-button fix

Replace replaceState with pushState in the drawer JS:
```javascript
// CORRECT
hamburger.addEventListener('click', function() {
  drawer.classList.toggle('open');
  if (drawer.classList.contains('open')) {
    history.pushState({drawerOpen: true}, '');
  }
});
window.addEventListener('popstate', function(e) {
  if (drawer.classList.contains('open')) {
    drawer.classList.remove('open');
  }
});
// WRONG — do not use replaceState here
```

---

## mpw_bible_writer.py — Pending Updates

### Update 1 — Read time calculation

Change from 500 wpm to 650 wpm for read time calculation.
Bible entries average 5,000+ words — at 500wpm this shows unrealistically high read times.
650wpm is the correct rate for scanning/reference reading.

### Update 2 — Nav rewrite

Same four changes as mpw_writer.py above. The Bible writer's nav must match:
- Grid mobile drawer
- Tools → in desktop nav
- CSS specificity fix
- pushState/popstate

### Update 3 — Bible entry bmn-drawer

The 222 Bible entry pages also need their mobile drawers updated (the bmn-drawer).
This is a separate batch injection script — NOT the bible writer. Pending after writer fix.
The bmn-drawer currently lacks the Production, Recording, and Tools categories.

---

## Session Assignment for Parallel Tool Builds

When Steve opens parallel sessions, each session receives this instruction:

```
You are building MPW tools for MusicProductionWiki.com.

STEP 1: Load the frozen spec by reading MPW-TOOL-BUILD-SPEC.md from:
https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/MPW-TOOL-BUILD-SPEC.md
Use the GitHub token: [GITHUB_TOKEN_FROM_SETENV]

STEP 2: Build [TOOL NAME] at slug [TOOL SLUG] using the frozen CSS and component system
from the spec. The tool must match the quality of the live Frequency Conflict Detector
at musicproductionwiki.com/tools/frequency-conflict-detector.

STEP 3: Commit the tool to GitHub at tools/[slug].html and update tools/index.html
with the new tool card in the same commit.

STEP 4: Report back: live URL, commit SHA, and confirm it renders correctly.

The 25 tools are listed in MPW-TOOL-BUILD-SPEC.md. Your assigned tools are:
[Session A: tools 1-3] [Session B: tools 4-7] [Session C: tools 8-11] [Session D: tools 12-14]
[Session E: tools 15-18] [Session F: tools 19-22] [Session G: tools 23-25]
```

---

## NEVER Rules Added — Session 66 — Scripts

| Rule | Detail |
|------|--------|
| NEVER start a parallel tool session without loading MPW-TOOL-BUILD-SPEC.md first | The spec is what keeps output consistent across sessions |
| NEVER use replaceState in mobile drawer JS on tool pages | Use pushState + popstate — replaceState was confirmed non-functional for back-button fix |
| NEVER commit a tool without also updating /tools/index.html | Always Trees API for 2+ files — single Netlify deploy |
| NEVER run mpw_writer.py for new article batches until the 4 pending updates are applied | Grid drawer + Tools nav + CSS specificity + pushState — all 4 required |
| NEVER run mpw_bible_writer.py until read time is updated to 650wpm and nav is fixed | Both changes required before next Bible batch |


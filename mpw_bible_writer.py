#!/usr/bin/env python3
"""
mpw_bible_writer.py — v5.2
MusicProductionWiki.com Producer's Bible Entry Generator

Three-tier architecture:
  Tier 1 (Flagship):  6,800–7,800 words  — build_html_t1()  PASS2_TOKENS=22,000
  Tier 2 (Standard):  3,800–5,000 words  — build_html_t2()  PASS2_TOKENS=14,000
  Tier 3 (Reference): 1,500–2,500 words  — build_html_t3()  PASS2_TOKENS=8,000

Gold standard: bible/compression.html (committed Session 33)
Batch format:  slug:Term:Category:Tier   (4 parts, colon-separated)
Example:       compression:Compression:Signal Processing:1

Run:
  python mpw_bible_writer.py --validate
  python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing" --tier 1
  python mpw_bible_writer.py --batch-file bible-upgrade-tier1.txt --start-date 2026-05-16
"""

import os, sys, json, re, time, datetime, base64, urllib.request, urllib.error, argparse
import concurrent.futures
import mpw_tools_v3

# ══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════

MODEL            = "claude-sonnet-4-6"
PASS1_TOKENS     = 20000
PASS2_TOKENS_T1  = 22000
PASS2_TOKENS_T2  = 14000
PASS2_TOKENS_T3  = 8000

WORD_FLOOR_T1, WORD_CEIL_T1 = 6800, 7800
WORD_FLOOR_T2, WORD_CEIL_T2 = 3800, 5000
WORD_FLOOR_T3, WORD_CEIL_T3 = 1500, 2500

GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
REPO_OWNER    = "musicproductionwiki"
REPO_NAME     = "musicproductionwiki"
BRANCH        = "main"

CONFIRMED_LIVE_SLUGS = {
    'compression', 'eq', 'limiting', 'saturation', 'distortion', 'reverb', 'delay',
    'parallel-compression', 'multiband-compression', 'noise-gate', 'gain-staging',
    'headroom', 'stereo-imaging', 'mid-side-processing', 'bus-compression', 'mix-bus',
    'send-return', 'automation', 'mastering', 'lufs', 'dynamic-range',
    'true-peak-limiting', 'loudness-normalization', 'subtractive-synthesis',
    'fm-synthesis', 'wavetable-synthesis', 'additive-synthesis', 'lfo', 'envelope',
    'oscillator', 'adsr', 'vocoder', 'high-pass-filter', 'low-pass-filter',
    'parametric-eq', 'shelving-eq', 'resonance', 'harmonic-distortion', 'chorus',
    'flanger', 'phaser', 'tremolo', 'vibrato', 'plate-reverb', 'room-reverb',
    'convolution-reverb', 'clip-gain', 'air-frequency-eq', 'air'
}
# EXCLUDED (confirmed 404): sidechain-compression, transient-shaping

CATEGORY_SLUG_MAP = {
    "Dynamics":         "dynamics",
    "Frequency":        "frequency",
    "Time-Based":       "time-based",
    "Signal Processing":"signal-processing",
    "Mixing":           "mixing",
    "Mastering":        "mastering",
    "Synthesis":        "synthesis",
    "Music Theory":     "music-theory",
}

# ══════════════════════════════════════════════════════════════════════════════
# QUOTES SYSTEM — Pass 1.5
# ══════════════════════════════════════════════════════════════════════════════

def load_quotes(path=None):
    """Load quotes.json from script directory."""
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quotes.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def filter_quotes(quotes, tags, max_results=10):
    """Score quotes by tag overlap, return top max_results."""
    tag_set = set(t.lower() for t in tags)
    scored = []
    for q in quotes:
        q_tags = set(t.lower() for t in q.get('tags', []))
        overlap = len(tag_set & q_tags)
        if overlap > 0:
            scored.append((overlap, q))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [q for _, q in scored[:max_results]]

def build_quotes_context(quotes, tags):
    """Format top quotes as string for Pass 2 prompt."""
    if not quotes:
        return "No producer quotes available for this entry."
    lines = ["AVAILABLE PRODUCER QUOTES (use 1-2 of these — exact text only, never fabricate):"]
    for i, q in enumerate(quotes, 1):
        person = q.get('person', 'Unknown')
        role   = q.get('role', '')
        text   = q.get('quote', '')
        source = q.get('source', '')
        lines.append(f"\n{i}. \"{text}\"\n   — {person}, {role}")
        if source:
            lines.append(f"   Source: {source}")
    return "\n".join(lines)

# ══════════════════════════════════════════════════════════════════════════════
# ANTHROPIC API
# ══════════════════════════════════════════════════════════════════════════════

def call_claude(prompt: str, max_tokens: int, system: str = "") -> str:
    if not ANTHROPIC_KEY:
        sys.exit("[ERROR] ANTHROPIC_API_KEY not set. Run: . .\\setenv.ps1")
    messages = [{"role": "user", "content": prompt}]
    body = {
        "model":      MODEL,
        "max_tokens": max_tokens,
        "messages":   messages,
    }
    if system:
        body["system"] = system
    data = json.dumps(body).encode()
    req  = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        method="POST",
        headers={
            "x-api-key":         ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
            "content-type":      "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            resp = json.loads(r.read())
        return resp["content"][0]["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"[API Error {e.code}] {body[:400]}")
        sys.exit(1)

# ══════════════════════════════════════════════════════════════════════════════
# SLUG VALIDATION
# ══════════════════════════════════════════════════════════════════════════════

def validate_slug(slug):
    """Return slug if live, else None."""
    return slug if slug in CONFIRMED_LIVE_SLUGS else None

def safe_slugs(items):
    """Filter list of slug strings to only confirmed live."""
    return [s for s in items if s in CONFIRMED_LIVE_SLUGS]

# ══════════════════════════════════════════════════════════════════════════════
# WORD COUNT
# ══════════════════════════════════════════════════════════════════════════════

def count_words_html(html: str) -> int:
    # FIX 27: strip <script> and <style> blocks first to avoid counting JSON-LD/CSS as prose
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&[a-z#0-9]+;', ' ', text)
    return len(text.split())

# ══════════════════════════════════════════════════════════════════════════════
# PASS 1 — STRUCTURED DATA
# ══════════════════════════════════════════════════════════════════════════════

PASS1_SYSTEM = """You are the data layer for the MusicProductionWiki Producer's Bible.
Return ONLY a single valid JSON object. No markdown, no fences, no explanation.
All slug fields must come from the CONFIRMED_LIVE_SLUGS set provided. If a slug is not in the set, use null.
Produce deeply researched, professional content. Producer-language throughout."""

def build_pass1_prompt(slug, term, category, tier):
    live_slugs_str = json.dumps(sorted(CONFIRMED_LIVE_SLUGS))
    return f"""Generate the full structured data JSON for a Producer's Bible entry.

TERM: {term}
SLUG: {slug}
CATEGORY: {category}
TIER: {tier}
CONFIRMED_LIVE_SLUGS (only use these for any slug field): {live_slugs_str}

Return a JSON object with ALL of the following fields:

{{
  "term": "{term}",
  "slug": "{slug}",
  "category": "{category}",
  "tags": ["tag1", "tag2", ...],
  "definition": "2–3 sentence precise technical definition",
  "emotional_hook": "single evocative sentence that opens the Definition section — amber italic pull quote",
  "signal_chain_position": {{
    "positions": [
      {{"label": "Box Name", "sublabel1": "line 1 text", "sublabel2": "line 2 text", "active": false}},
      ...8 positions total, one with active: true for {term}...
    ]
  }},
  "section_summaries": {{
    "definition": "one-sentence italic summary for the definition section callout",
    "how_it_works": "one-sentence italic summary",
    "parameters": "one-sentence italic summary",
    "history": "one-sentence italic summary"
  }},
  "track_examples": [
    {{
      "artist": "Artist Name",
      "track": "Track Title",
      "year": 2003,
      "album": "Album Name",
      "produced_by": "Producer Name",
      "timestamp": "0:32",
      "listening_guide": "2 sentences: what to listen for and how it demonstrates {term}"
    }}
  ],
  "producers_verdict": "2–3 sentences: the definitive professional take on when and how to use {term}",
  "progression_path": {{
    "beginner": "What a beginner should do first with {term}",
    "intermediate": "The intermediate technique to master next",
    "advanced": "The advanced application that separates professionals"
  }},
  "red_flags": ["Red flag 1", "Red flag 2", "Red flag 3"],
  "green_flags": ["Green flag 1", "Green flag 2", "Green flag 3"],
  "interaction_warnings": [
    "Interaction warning 1 — what it interacts with and the fix",
    "Interaction warning 2",
    "Interaction warning 3"
  ],
  "faq": [
    {{"q": "Question 1?", "a": "Answer 1."}},
    {{"q": "Question 2?", "a": "Answer 2."}},
    {{"q": "Question 3?", "a": "Answer 3."}},
    {{"q": "Question 4?", "a": "Answer 4."}},
    {{"q": "Question 5?", "a": "Answer 5."}},
    {{"q": "Question 6?", "a": "Answer 6."}},
    {{"q": "Question 7?", "a": "Answer 7."}},
    {{"q": "Question 8?", "a": "Answer 8."}}
  ],
  "related_terms": [
    {{"term": "Related Term", "slug": "slug-or-null", "preview": "one sentence preview"}},
    ...4–6 items...
  ],
  "hardware_vs_plugin_rows": [
    {{"aspect": "Aspect", "hardware": "Hardware approach", "plugin": "Plugin approach"}},
    ...4–6 rows...
  ],
  "genre_application_rows": [
    {{"genre": "Trap", "application": "How {term} is used in Trap"}}
  ],
  "types": [
    {{"name": "Type Name", "hardware_example": "Hardware unit name", "description": "2–3 sentences"}}
  ],
  "section_mistakes": [
    {{"title": "Mistake title", "explanation": "2 sentences explaining the mistake and correction"}}
  ],
  "producer_quote": "exact quote text",
  "producer_quote_source": "Person Name, role -- Source",
  "producer_quote_2": "exact second quote text",
  "producer_quote_2_source": "Person Name, role -- Source",
  "producer_quote_3": "exact third quote text",
  "producer_quote_3_source": "Person Name, role -- Source",
  "producer_spotlight": [
    {{
      "name": "Producer Name",
      "role": "Role (Credits)",
      "slug": "producer-slug",
      "signature_move": "One sentence: their specific technique with this term using exact settings or approach"
    }},
    {{
      "name": "Producer Name 2",
      "role": "Role (Credits)",
      "slug": "producer-slug-2",
      "signature_move": "One sentence: their specific technique"
    }},
    {{
      "name": "Producer Name 3",
      "role": "Role (Credits)",
      "slug": "producer-slug-3",
      "signature_move": "One sentence: their specific technique"
    }}
  ],
  "wikipedia_slug": "Wikipedia_Article_Title_or_null",
  "wikidata_id": "Q000000_or_null",

  "difficulty": "Beginner|Intermediate|Advanced",
  "prerequisites": ["slug1-or-null", "slug2-or-null", "slug3-or-null"],
  "misconception": {{
    "myth": "What most producers wrongly believe about {term}",
    "truth": "The actual reality — 2–3 sentences"
  }},
  "before_after_text": {{
    "before": "What the mix/signal sounds like BEFORE applying {term} correctly",
    "after": "What it sounds like AFTER — specific perceptual differences"
  }},
  "the_number": "The single most important number (e.g. 4:1, -18dBFS, 10ms)",
  "the_number_label": "short label explaining what number represents",
  "the_number_context": "1–2 sentences explaining why this number matters to producers",
  "daw_implementations": {{
    "ableton": "Step-by-step instructions for {term} in Ableton Live 11/12",
    "logic": "Step-by-step instructions in Logic Pro",
    "fl_studio": "Step-by-step instructions in FL Studio 21",
    "pro_tools": "Step-by-step instructions in Pro Tools"
  }},
  "plugin_recommendations": {{
    "free": [
      {{"name": "Plugin Name", "manufacturer": "Company"}},
      {{"name": "Plugin Name 2", "manufacturer": "Company2"}}
    ],
    "mid": [
      {{"name": "Plugin Name", "manufacturer": "Company"}}
    ],
    "pro": [
      {{"name": "Plugin Name", "manufacturer": "Company"}}
    ]
  }},
  "genre_settings_rows": [
    {{"genre": "Trap",     "ratio": "8:1–20:1", "attack": "<1ms",   "release": "<30ms", "threshold": "-15 to -20", "notes": "Extreme settings for sidechain pumping effect"}},
    {{"genre": "Hip-Hop",  "ratio": "4:1–8:1",  "attack": "5–15ms", "release": "50–100ms", "threshold": "-12 to -18", "notes": "Controlled transients, dense mid presence"}},
    {{"genre": "House",    "ratio": "4:1–6:1",  "attack": "3–10ms", "release": "auto",   "threshold": "-14 to -20", "notes": "Pump against kick for rhythmic feel"}},
    {{"genre": "Rock",     "ratio": "4:1",      "attack": "10–25ms","release": "60–120ms","threshold": "-10 to -15","notes": "Preserve snap, add density to sustain"}},
    {{"genre": "Mastering","ratio": "2:1–4:1",  "attack": "30–80ms","release": "200–400ms","threshold": "-6 to -12","notes": "Gentle glue — never more than 4dB GR"}}
  ],
  "next_steps": {{
    "beginner_slug": "slug-for-beginner-next-step-or-null",
    "deeper_slug": "slug-for-deeper-dive-or-null",
    "problem_slug": "slug-for-solve-a-problem-or-null"
  }},
  "tool_type": "calculator|null",
  "comparison_terms": [
    {{"term": "Compared Term 1", "slug": "slug-or-null"}},
    {{"term": "Compared Term 2", "slug": "slug-or-null"}}
  ],
  "genre_columns": ["Genre", "Column2", "Column3", "Column4", "Notes"],
  "genre_rows_v2": [
    {{"Genre": "Trap", "Column2": "val", "Column3": "val", "Column4": "val", "Notes": "..."}}
  ],
  "signature_sounds": [
    {{"track": "Artist -- Track Title (Year)", "settings": "Exact settings with specific numbers", "why": "Why this works perceptually -- 1-2 sentences"}},
    {{"track": "Artist -- Track Title (Year)", "settings": "Exact settings with specific numbers", "why": "Why this works perceptually"}},
    {{"track": "Artist -- Track Title (Year)", "settings": "Exact settings", "why": "Perceptual result"}},
    {{"track": "Artist -- Track Title (Year)", "settings": "Exact settings", "why": "Perceptual result"}}
  ],
  "session_breakdown": {{
    "scenario": "One-sentence production scenario description",
    "steps": ["Step 1 with exact settings", "Step 2", "Step 3", "Step 4", "Step 5"]
  }}
}}

Requirements:
- track_examples: minimum 5, maximum 8 -- real tracks only, no invented titles
- faq: exactly 8 questions -- questions producers actually search for
- All slug fields: validate against CONFIRMED_LIVE_SLUGS -- use null if not in the set
- the_number: a single concrete value that anchors producers' mental model
- genre_settings_rows: exactly 5 rows matching the genres shown
- comparison_terms: exactly 2 terms that {term} is most often confused with
- tool_type: "calculator" only if an interactive calculator makes sense for this term; otherwise null
- genre_columns: array of column headers specific to {term} (e.g. for EQ: Genre/Target Frequencies/Key Move/Q/Notes)
- signature_sounds: 4 iconic uses with exact settings and perceptual explanation -- real tracks only
- session_breakdown: one realistic production scenario with 5 steps using exact settings
- producer_spotlight: exactly 3 producers known for their use of {term}; include specific signature_move with exact technique
"""

def run_pass1(slug, term, category, tier):
    print(f"  Pass 1: fetching structured data for '{term}' (Tier {tier})…")
    raw = call_claude(build_pass1_prompt(slug, term, category, tier), PASS1_TOKENS, PASS1_SYSTEM)
    # Strip any accidental fences
    raw = re.sub(r'^```[a-z]*\n?', '', raw.strip())
    raw = re.sub(r'\n?```$', '', raw)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[WARN] Pass 1 JSON parse error: {e}. Attempting repair…")
        # Try to extract JSON object
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            data = json.loads(m.group(0))
        else:
            sys.exit("[ERROR] Pass 1 returned unparseable JSON.")
    # Validate slugs
    for key in ['prerequisites', 'further_reading_slugs']:
        if key in data and isinstance(data[key], list):
            data[key] = [s if s in CONFIRMED_LIVE_SLUGS else None for s in data[key]]
    if 'related_terms' in data:
        for rt in data['related_terms']:
            if rt.get('slug') and rt['slug'] not in CONFIRMED_LIVE_SLUGS:
                rt['slug'] = None
    if 'comparison_terms' in data:
        for ct in data['comparison_terms']:
            if ct.get('slug') and ct['slug'] not in CONFIRMED_LIVE_SLUGS:
                ct['slug'] = None
    if 'next_steps' in data:
        for k in ['beginner_slug', 'deeper_slug', 'problem_slug']:
            if data['next_steps'].get(k) and data['next_steps'][k] not in CONFIRMED_LIVE_SLUGS:
                data['next_steps'][k] = None
    return data

# ══════════════════════════════════════════════════════════════════════════════
# HTML BUILDING UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

def difficulty_class(d):
    d = (d or 'intermediate').lower()
    if d == 'beginner':  return 'difficulty-beginner'
    if d == 'advanced':  return 'difficulty-advanced'
    return 'difficulty-intermediate'

def build_prereq_chain(prerequisites, p1):
    links = []
    for slug in (prerequisites or []):
        if slug and slug in CONFIRMED_LIVE_SLUGS:
            label = slug.replace('-', ' ').title()
            links.append(f'<a href="/bible/{slug}">{label}</a>')
    if not links:
        return ''
    inner = ' <span>›</span> '.join(links)
    return f'<div class="prereq-chain"><span>Understand first:</span> {inner}</div>'

def build_signal_chain_svg(positions, slug):
    """Build signal chain SVG 1440×160 + mobile stack."""
    n       = len(positions)
    box_w   = 158
    act_w   = 178
    box_h   = 72
    act_h   = 92
    spacing = 14
    total   = n * box_w + (n - 1) * spacing + (act_w - box_w)
    start_x = max(8, (1440 - total) // 2)
    cx      = start_x

    defs = """  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="#4a4a6a"/>
    </marker>
  </defs>"""

    boxes   = []
    mobile  = []
    title_id = f"sc-{slug}-title"

    for i, pos in enumerate(positions):
        active = pos.get('active', False)
        label  = pos.get('label', f'Stage {i+1}')
        sub1   = pos.get('sublabel1', '')
        sub2   = pos.get('sublabel2', '')

        w  = act_w  if active else box_w
        h  = act_h  if active else box_h
        y  = (160 - h) // 2
        mx = cx + w // 2

        if active:
            fill   = '#2a1400'
            stroke = '#f5a623'
            sw     = '2.5'
            tfill  = '#f5a623'
            tsize  = '15'
            tw     = '900'
            sfill  = '#c8a060'
        else:
            fill   = '#13132a'
            stroke = '#3a3a5a'
            sw     = '1.5'
            tfill  = '#c8c8d8'
            tsize  = '13'
            tw     = '700'
            sfill  = '#666'

        svg_parts = [
            f'  <rect x="{cx}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>',
            f'  <text x="{mx}" y="{y+22}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="{tsize}" font-weight="{tw}" fill="{tfill}">{label}</text>',
        ]
        sub_y = y + 42
        if sub1:
            svg_parts.append(f'  <text x="{mx}" y="{sub_y}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="{sfill}">{sub1}</text>')
            sub_y += 16
        if sub2:
            svg_parts.append(f'  <text x="{mx}" y="{sub_y}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="{sfill}">{sub2}</text>')
        if active:
            svg_parts.append(f'  <text x="{mx}" y="{y+h-8}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="9" fill="#f5a623">&#9664; YOU ARE HERE</text>')

        boxes.append('\n'.join(svg_parts))

        # Arrow (not last)
        if i < n - 1:
            ax1 = cx + w
            ax2 = ax1 + spacing - 2
            ay  = 80
            ac  = '#f5a623' if active else '#4a4a6a'
            boxes.append(f'  <line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" stroke="{ac}" stroke-width="2" marker-end="url(#arr)"/>')
            cx += w + spacing
        else:
            cx += w

        # Mobile stack
        if active:
            mobile.append(f'          <div class="scm-box scm-active"><span class="scm-label">{label}</span><div class="scm-sub">{sub1}{" · " + sub2 if sub2 else ""}</div><span class="scm-badge">&#9654; You are here</span></div>')
        else:
            mobile.append(f'          <div class="scm-box"><span class="scm-label">{label}</span><div class="scm-sub">{sub1}{" · " + sub2 if sub2 else ""}</div></div>')
        if i < n - 1:
            mobile.append('          <div class="scm-arrow">&#8595;</div>')

    svg_inner = '\n'.join(boxes)
    mobile_html = '\n'.join(mobile)

    svg = f"""        <div class="signal-chain-diagram">
          <svg viewBox="0 0 1440 160" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:1440px;height:auto;display:block;min-height:100px" aria-labelledby="{title_id}" role="img">
  <title id="{title_id}">Signal chain position of {positions[[i for i,p in enumerate(positions) if p.get('active')][0] if any(p.get('active') for p in positions) else 0].get('label','')} in music production</title>
{defs}
{svg_inner}
</svg>
        </div>
        <!-- Mobile signal chain — vertical stack -->
        <div class="signal-chain-mobile">
{mobile_html}
        </div>"""
    return svg

def build_genre_table_html(rows, term, slug, genre_columns=None, genre_rows_v2=None):
    # FIX 18: use genre_rows_v2 + genre_columns when available (category-aware columns)
    if genre_rows_v2 and genre_columns:
        headers = genre_columns
        th_row  = ''.join(f'<th>{h}</th>' for h in headers)
        td_rows = ''
        for r in genre_rows_v2:
            td_rows += '<tr>' + ''.join(f'<td>{r.get(h,"")}</td>' for h in headers) + '</tr>\n'
    elif rows:
        headers = ['Genre', 'Ratio', 'Attack', 'Release', 'Threshold', 'Notes']
        keys    = ['genre', 'ratio', 'attack', 'release', 'threshold', 'notes']
        th_row  = ''.join(f'<th>{h}</th>' for h in headers)
        td_rows = ''
        for r in rows:
            td_rows += '<tr>' + ''.join(f'<td>{r.get(k,"")}</td>' for k in keys) + '</tr>\n'
    else:
        return ''
    share_bar = (
        f'        <div class="mpw-share-bar">\n'
        f'        <span class="mpw-share-label">Share</span>\n'
        f'        <button class="mpw-share-btn share-copy" onclick="navigator.clipboard&&navigator.clipboard.writeText(\'musicproductionwiki.com/bible/{slug}#genre-table\')">Copy Link</button>\n'
        f'        <a href="https://x.com/intent/tweet?text={term}+By+Genre+%E2%80%94+%40mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}%23genre-table" target="_blank" rel="noopener" class="mpw-share-btn share-x"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.26 5.632 5.905-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>Share on X</a>\n'
        f'        <a href="https://reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}%23genre-table&title={term}+By+Genre+%E2%80%94+MusicProductionWiki" target="_blank" rel="noopener" class="mpw-share-btn share-reddit"><svg width="12" height="12" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="10"/><path fill="#ff4500" d="M16.67 10a1.46 1.46 0 00-2.47-1 7.12 7.12 0 00-3.85-1.23l.65-3.08 2.13.45a1 1 0 101.07-1 1 1 0 00-.96.68l-2.38-.5a.27.27 0 00-.32.2l-.73 3.44a7.14 7.14 0 00-3.89 1.23 1.46 1.46 0 10-1.61 2.39 2.87 2.87 0 000 .44c0 2.24 2.61 4.06 5.83 4.06s5.83-1.82 5.83-4.06a2.87 2.87 0 000-.44 1.46 1.46 0 00.61-1.08zM7.5 11a1 1 0 111 1 1 1 0 01-1-1zm5.67 2.65a3.54 3.54 0 01-2.34.63 3.54 3.54 0 01-2.34-.63.25.25 0 01.35-.35 3.07 3.07 0 002 .48 3.07 3.07 0 002-.48.25.25 0 01.35.35zm-.17-1.65a1 1 0 111-1 1 1 0 01-1 1z"/></svg>Reddit</a>\n'
        f'        </div>'
    )
    return f"""        <div class="genre-table-wrap">
          <table class="genre-settings-table">
            <thead><tr>{th_row}</tr></thead>
            <tbody>{td_rows}</tbody>
          </table>
        </div>
{share_bar}"""

def build_plugin_recs_html(plugin_recs):
    if not plugin_recs:
        return ''
    tiers = [('free', 'Free Tier', 'plugin-tier-free'), ('mid', 'Mid Tier', 'plugin-tier-mid'), ('pro', 'Pro Tier', 'plugin-tier-pro')]
    cols  = ''
    for key, label, css in tiers:
        items = plugin_recs.get(key, [])
        if not items:
            continue
        items_html = ''.join(f'<div class="plugin-item"><span class="plugin-name">{p.get("name","")}</span> <span class="plugin-mfr">{p.get("manufacturer","")}</span></div>' for p in items)
        cols += f'<div class="plugin-tier {css}"><span class="plugin-tier-label">{label}</span>{items_html}</div>\n'
    return f'        <div class="plugin-recs">\n{cols}        </div>'

def build_daw_tabs_html(daw_implementations, slug):
    if not daw_implementations:
        return ''
    daws = [('ableton', 'Ableton'), ('logic', 'Logic Pro'), ('fl_studio', 'FL Studio'), ('pro_tools', 'Pro Tools')]
    btns    = ''
    panels  = ''
    for i, (key, label) in enumerate(daws):
        text = daw_implementations.get(key, '')
        if not text:
            continue
        active = 'active' if i == 0 else ''
        btns   += f'<button class="daw-tab-btn {active}" data-daw="{key}" onclick="dawTab(this,\'{key}\')">{label}</button>'
        panels += f'<div class="daw-tab-panel {active}" id="dtp-{key}-{slug}"><p style="margin:0">{text}</p></div>'
    return f"""        <div class="daw-tabs" id="daw-section">
          <div class="daw-tab-nav">{btns}</div>
          <div class="daw-tab-content">{panels}</div>
        </div>"""

def build_comparison_callouts_html(comparison_terms, term):
    if not comparison_terms:
        return ''
    cards = ''
    for ct in comparison_terms[:2]:
        other = ct.get('term', '')
        slug  = ct.get('slug')
        link  = f'<a href="/bible/{slug}" style="color:#f5a623;text-decoration:none">{other}</a>' if slug else other
        cards += f"""        <div style="background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px">
          <div style="font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:#f5a623;font-weight:700;margin-bottom:10px">{term} vs {other}</div>
          <p style="font-size:13px;color:#c8c8d8;margin:0">See the full comparison: {link}</p>
        </div>
"""
    return f'        <div class="comparison-callouts">\n{cards}        </div>'

def build_related_terms_html(related_terms):
    if not related_terms:
        return ''
    cards = ''
    for rt in (related_terms or [])[:6]:
        t     = rt.get('term', '')
        s     = rt.get('slug')
        prev  = rt.get('preview', '')
        if s and s in CONFIRMED_LIVE_SLUGS:
            cards += f'<a href="/bible/{s}" class="related-term-card"><span class="rt-term">{t}</span><span class="rt-preview">{prev}</span></a>\n'
    return f'        <div class="related-terms-grid">\n{cards}        </div>'

def build_track_list_html(track_examples):
    if not track_examples:
        return ''
    items = ''
    for t in track_examples:
        artist = t.get('artist','')
        track  = t.get('track','')
        year   = t.get('year','')
        album  = t.get('album','')
        prod   = t.get('produced_by','')
        note   = t.get('listening_guide','') or t.get('note','')
        items += f'<div class="track-item"><span class="track-artist">{artist}</span> — <span class="track-name">{track}</span> ({year}), <em>{album}</em>. Produced by {prod}.'
        if note:
            items += f'<div class="track-note">{note}</div>'
        items += '</div>\n'
    return f'        <div class="track-examples-list">\n{items}        </div>'

def build_faq_html(faq):
    if not faq:
        return ''
    items = ''
    for item in faq:
        q = item.get('q','')
        a = item.get('a','')
        items += f'        <div class="faq-item"><button class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">{q}<span>+</span></button><div class="faq-a"><p>{a}</p></div></div>\n'
    return f'        <div class="faq-accordion">\n{items}        </div>'

def build_flags_html(red_flags, green_flags):
    reds   = ''.join(f'<li class="red-flag">🔴 {f}</li>' for f in (red_flags or []))
    greens = ''.join(f'<li class="green-flag">🟢 {f}</li>' for f in (green_flags or []))
    return f"""        <div class="red-green-flags">
          <div class="flags-col"><h4 style="color:#cc3333">Red Flags</h4><ul>{reds}</ul></div>
          <div class="flags-col"><h4 style="color:#33cc33">Green Flags</h4><ul>{greens}</ul></div>
        </div>"""

def build_before_after_html(before_after_text):
    if not before_after_text:
        return ''
    bef = before_after_text.get('before','')
    aft = before_after_text.get('after','')
    return f"""        <div class="before-after-block">
          <div class="ba-before"><span class="ba-label">Before</span><p class="ba-text">{bef}</p></div>
          <div class="ba-after"><span class="ba-label">After</span><p class="ba-text">{aft}</p></div>
        </div>"""

def build_the_number_html(the_number, the_number_label, the_number_context):
    if not the_number:
        return ''
    return f"""        <div class="the-number-box">
          <span class="tn-value">{the_number}</span>
          <span class="tn-label">{the_number_label}</span>
          <p class="tn-context">{the_number_context}</p>
        </div>"""

def build_sidebar_toc_html(slug):
    sections = [
        ('definition',      'Definition'),
        ('how-it-works',    'How It Works'),
        ('parameters',      'Parameters'),
        ('quick-reference', 'Quick Ref'),
        ('tools',           'Tools'),
        ('signal-chain',    'Signal Chain'),
        ('history',         'History'),
        ('how-to-use',      'How To Use'),
        ('genre-table',     'By Genre'),
        ('hardware-plugin', 'Hardware vs Plugin'),
        ('before-after',    'Before / After'),
        ('in-the-wild',     'In The Wild'),
        ('signatures',      'Signatures'),
        ('types',           'Types'),
        ('plugin-recs',     'Plugins'),
        ('mistakes',        'Mistakes'),
        ('flags',           'Flags'),
        ('progression',     'Progression'),
        ('faq',             'FAQ'),
        ('related',         'Related'),
    ]
    links = ''.join(f'<a href="#{sec_id}">{label}</a>\n' for sec_id, label in sections)
    return f'          <div class="sidebar-toc">\n            <h4>Contents</h4>\n{links}          </div>'

def build_producer_spotlight_html(p1):
    # FIX 16: Use producer_spotlight array from Pass 1 with ps-move field
    spotlight = p1.get('producer_spotlight', [])
    if spotlight:
        cards = ''
        for prod in spotlight[:3]:
            name = prod.get('name', '')
            role = prod.get('role', 'Producer')
            move = prod.get('signature_move', '')
            if not name:
                continue
            move_html = f'          <div class="ps-move">{move}</div>\n' if move else ''
            cards += (
                '          <div class="ps-card">\n'
                f'            <div class="ps-name">{name}</div>\n'
                f'            <div class="ps-role">{role}</div>\n'
                + move_html +
                '          </div>\n'
            )
        if cards:
            return f'          <div class="producer-spotlight">\n            <h3>Producer Spotlight</h3>\n{cards}          </div>'
    # Fallback: derive from track_examples
    names = []
    for t in (p1.get('track_examples') or [])[:3]:
        prod = t.get('produced_by', '')
        if prod and prod not in [n[0] for n in names]:
            names.append((prod, 'Producer'))
    if not names:
        return ''
    cards = ''
    for name, role in names[:3]:
        cards += f'          <div class="ps-card"><div class="ps-name">{name}</div><div class="ps-role">{role}</div></div>\n'
    return f'          <div class="producer-spotlight">\n            <h3>Producer Spotlight</h3>\n{cards}          </div>'

# ══════════════════════════════════════════════════════════════════════════════
# CSS BLOCK — identical to gold standard, parameterized
# ══════════════════════════════════════════════════════════════════════════════

def build_css():
    return """  <style>
    /* Bible page v5.2 — NO main.js — fully self-contained */
    *{box-sizing:border-box;margin:0;padding:0}
    html{overflow-x:clip}
    body{background:#0d0d1a;color:#e0e0f0;font-family:system-ui,-apple-system,sans-serif;line-height:1.7;overflow-x:clip}
    /* overflow:clip on both — NOT overflow:hidden which breaks position:sticky */

    /* ── READING PROGRESS — desktop HIDDEN, mobile SHOWN ── */
    #reading-progress{position:fixed;top:0;left:0;height:3px;background:#f5a623;z-index:99999;width:0%;max-width:100%;transition:width .1s linear;pointer-events:none;display:none}

    /* MPW Slim Bar */
    .mpw-slim-bar{position:sticky;top:0;z-index:700;background:#181818;border-bottom:1px solid rgba(255,255,255,0.07);height:40px;display:flex;align-items:center;padding:0 20px;gap:0}
    .msb-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0;margin-right:24px}
    .msb-logomark{width:24px;height:24px;border-radius:6px;background:#00e8a2;display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .msb-name{font-size:13px;font-weight:600;color:#d0d0d0;letter-spacing:-0.01em}
    .msb-links{display:flex;align-items:center;gap:0;list-style:none;flex:1}
    .msb-links a{color:#888;text-decoration:none;font-size:12px;padding:4px 10px;border-radius:4px;white-space:nowrap}
    .msb-links a:hover{color:#d0d0d0;background:rgba(255,255,255,.05)}
    .msb-pub{font-size:11px;color:#555;font-style:italic;margin-left:auto;white-space:nowrap;padding-right:8px}
    .msb-search{display:flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:5px;background:none;border:none;cursor:pointer;color:#666;flex-shrink:0}
    .msb-search:hover{color:#d0d0d0;background:rgba(255,255,255,.07)}
    .msb-cta{background:#00e8a2;color:#0a0a0b;font-size:11px;font-weight:700;padding:5px 12px;border-radius:6px;text-decoration:none;white-space:nowrap;flex-shrink:0;margin-left:8px}
    .msb-cta:hover{background:#00fdb5}

    /* Bible Bar */
    .bible-bar{position:sticky;top:40px;z-index:600;background:#0d0800;border-bottom:2px solid #f5a623;height:50px;display:flex;align-items:center;padding:0 20px;gap:12px}
    .bb-identity{display:flex;align-items:center;gap:8px;flex-shrink:0;text-decoration:none}
    .bb-diamond{color:#f5a623;font-size:14px;line-height:1}
    .bb-title{font-size:14px;font-weight:800;color:#f5a623;letter-spacing:.01em;white-space:nowrap}
    .bb-divider{width:1px;height:22px;background:rgba(245,166,35,.25);flex-shrink:0}
    .bb-cats{display:flex;align-items:center;gap:4px;flex:1;overflow:hidden}
    .bb-cat{font-size:11px;color:#888;text-decoration:none;padding:4px 10px;border-radius:20px;border:1px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
    .bb-cat:hover{color:#f5a623;border-color:rgba(245,166,35,.3)}
    .bb-cat.active{color:#f5a623;border-color:rgba(245,166,35,.5);background:rgba(245,166,35,.07);font-weight:600}
    .bb-all{font-size:11px;color:#666;text-decoration:none;margin-left:auto;white-space:nowrap;flex-shrink:0}
    .bb-all:hover{color:#f5a623}

    /* Mobile bible bar */
    .bible-mobile-bar{display:none;position:sticky;top:40px;z-index:300;height:28px;background:#0d0800;border-bottom:1px solid rgba(245,166,35,0.2);align-items:center;justify-content:center;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#f5a623;text-align:center}

    /* Hamburger + mobile drawer */
    .msb-mob{display:none;background:none;border:none;cursor:pointer;padding:6px;flex-direction:column;gap:4px;flex-shrink:0;margin-left:8px}
    .msb-mob span{display:block;width:20px;height:2px;background:#888;border-radius:2px}
    .bmn-drawer{display:none;position:fixed;top:40px;left:0;right:0;bottom:0;background:rgba(10,10,11,0.99);z-index:699;overflow-y:auto;padding:16px;border-top:1px solid rgba(255,255,255,0.09);flex-direction:column;gap:4px}
    .bmn-drawer.open{display:flex}
    .bmn-drawer-label{font-size:10px;font-family:monospace;color:#6a6a7a;text-transform:uppercase;letter-spacing:.12em;padding:12px 12px 6px}
    .bmn-drawer a{display:block;padding:11px 12px;border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4}
    .bmn-drawer a:hover{color:#f0f0f0;background:#111113}
    .bmn-drawer-bible{display:flex;align-items:center;gap:8px;padding:12px 16px;border-radius:9px;background:rgba(245,166,35,0.07);border:1px solid rgba(245,166,35,0.22);color:#f5a623;font-size:14px;font-weight:600;text-decoration:none;margin:4px 0 8px}
    .bmn-drawer-cta{display:block;background:#00e8a2;color:#0a0a0b;font-weight:600;font-size:14px;padding:13px 16px;border-radius:10px;text-decoration:none;text-align:center;margin-top:8px}
    .bmn-drawer-cats{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:4px}
    .bmn-drawer-cat{display:flex;align-items:center;padding:10px 12px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:500;color:#a0a0b4;background:#111113;border:1px solid #1a1a3a}
    .bmn-drawer-cat:hover{color:#f5a623;border-color:rgba(245,166,35,.3)}

    /* Search overlay */
    #bibleSearchOverlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.88);z-index:99998;align-items:flex-start;justify-content:center;padding-top:80px}
    .bso-box{background:#18181c;border:1px solid rgba(255,255,255,.15);border-radius:14px;width:100%;max-width:620px;overflow:hidden;box-shadow:0 24px 64px rgba(0,0,0,.7);margin:0 1rem}
    .bso-input-wrap{display:flex;align-items:center;padding:16px 20px;gap:12px;border-bottom:1px solid rgba(255,255,255,.07)}
    #bibleSearchInput{flex:1;background:none;border:none;outline:none;font-size:16px;color:#fff;font-family:inherit}
    #bibleSearchResults{max-height:420px;overflow-y:auto;padding:8px}

    /* Entry nav */
    .entry-nav{position:sticky;top:90px;z-index:400;background:#0d0d1a;border-bottom:1px solid #2a2a4a;overflow-x:auto;scrollbar-width:none;-webkit-mask-image:linear-gradient(to right,black 85%,transparent 100%);mask-image:linear-gradient(to right,black 85%,transparent 100%)}
    .entry-nav::-webkit-scrollbar{display:none}
    .entry-nav-inner{display:flex;justify-content:center;gap:4px;padding:10px 10px;min-width:max-content;margin:0}
    .entry-nav-inner a{color:#a0a0c0;text-decoration:none;font-size:10px;text-transform:uppercase;letter-spacing:.05em;padding:6px 10px;border-radius:4px;white-space:nowrap;min-height:32px;display:inline-flex;align-items:center}
    .entry-nav-inner a:hover{color:#f5a623;background:#1a1a3a}
    .entry-nav-inner a.active{color:#f5a623;background:#1a1a3a}

    /* Layout */
    .bible-entry-wrap{max-width:1100px;margin:0 auto;padding:40px 24px;display:grid;grid-template-columns:1fr 280px;gap:40px;align-items:start}
    .entry-main{min-width:0}
    .entry-sidebar{position:sticky;top:148px;align-self:start;height:calc(100vh - 168px);overflow-y:auto;overflow-x:hidden;scrollbar-width:thin;scrollbar-color:#2a2a4a transparent}

    /* Section scroll margin */
    [id].entry-section{scroll-margin-top:128px}

    /* Breadcrumb */
    .entry-breadcrumb{font-size:12px;color:#666;margin-bottom:16px}
    .entry-breadcrumb a{color:#a0a0c0;text-decoration:none}
    .entry-breadcrumb a:hover{color:#f5a623}
    .entry-breadcrumb .bc-sep{color:#444;margin:0 6px}

    /* Masthead */
    .entry-masthead{background:linear-gradient(135deg,#1a0a00,#0d0d1a);border:1px solid #f5a623;border-radius:12px;padding:32px;margin-bottom:32px}
    .entry-category{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;font-weight:700;margin-bottom:8px}
    .entry-term{font-size:clamp(2rem,5vw,3.5rem);font-weight:900;color:#fff;line-height:1.1;margin-bottom:8px}
    .entry-pos{font-size:14px;color:#888;font-style:italic;margin-bottom:16px}
    .entry-hook{font-size:1.1rem;color:#c8c8d8;font-style:italic;border-left:3px solid #f5a623;padding-left:16px;display:block;margin-bottom:16px}
    .entry-meta{display:flex;gap:16px;font-size:12px;color:#666;flex-wrap:wrap}
    .entry-meta span{background:#1a1a3a;padding:4px 10px;border-radius:4px}

    /* Difficulty badge */
    .difficulty-badge{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;padding:3px 10px;border-radius:20px;margin-bottom:12px}
    .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
    .difficulty-intermediate{background:rgba(245,166,35,.15);color:#f5a623;border:1px solid rgba(245,166,35,.4)}
    .difficulty-beginner{background:rgba(96,192,255,.12);color:#60c0ff;border:1px solid rgba(96,192,255,.35)}
    .difficulty-advanced{background:rgba(204,51,51,.12);color:#ff8888;border:1px solid rgba(204,51,51,.35)}

    /* Prereq chain */
    .prereq-chain{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:16px;font-size:12px;color:#666}
    .prereq-chain span{color:#888}
    .prereq-chain a{color:#a0a0c0;text-decoration:none;padding:2px 8px;border:1px solid #2a2a4a;border-radius:3px}
    .prereq-chain a:hover{color:#f5a623;border-color:rgba(245,166,35,.4)}

    /* Quick answer */
    .quick-answer-block{background:#1a1000;border:1px solid #f5a623;border-radius:8px;padding:20px;margin-bottom:32px}
    .qa-label{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;font-weight:700;margin-bottom:8px}
    .qa-text{font-size:1.05rem;color:#e0e0f0;line-height:1.6}

    /* Section headers */
    .entry-main h2{font-size:1.6rem;font-weight:700;color:#fff;margin:40px 0 16px;padding-bottom:8px;border-bottom:1px solid #2a2a4a;scroll-margin-top:128px}
    .entry-main h3{font-size:1.2rem;font-weight:600;color:#e0e0f0;margin:24px 0 12px}
    .entry-main h4{font-size:1rem;font-weight:600;color:#c8c8d8;margin:16px 0 8px}
    .entry-main p{color:#c8c8d8;margin-bottom:16px;line-height:1.8}
    .entry-main ul,.entry-main ol{color:#c8c8d8;margin:0 0 16px 24px}
    .entry-main li{margin-bottom:8px;line-height:1.7}

    /* The Number box */
    .the-number-box{background:#1a0800;border:2px solid #f5a623;border-radius:10px;padding:24px;margin:24px 0;text-align:center}
    .tn-value{display:block;font-size:3rem;font-weight:900;color:#f5a623;line-height:1}
    .tn-label{display:block;font-size:14px;color:#c8c8d8;margin:8px 0 4px}
    .tn-context{font-size:13px;color:#888;margin:0}

    /* Section summary */
    .section-summary{background:#1a1a3a;border-left:3px solid #f5a623;padding:10px 16px;font-size:13px;color:#a0a0c0;font-style:italic;margin:16px 0 24px;border-radius:0 6px 6px 0}

    /* Parameters */
    .parameters-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:16px 0}
    .param-item{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px}
    .param-title{font-size:14px;font-weight:700;color:#f5a623;margin-bottom:8px}
    .param-desc{font-size:13px;color:#c8c8d8;line-height:1.6}

    /* Quick ref table */
    .qr-table-wrap{overflow-x:auto;margin:16px 0;background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:4px}
    .quick-ref-table{width:100%;border-collapse:collapse;font-size:13px}
    .quick-ref-table th{background:#1a1a3a;color:#f5a623;padding:8px 12px;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.05em}
    .quick-ref-table td{padding:8px 12px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}
    .quick-ref-table tr:hover td{background:#13132a}

    /* Genre settings table */
    .genre-settings-table{width:100%;border-collapse:collapse;font-size:12px}
    .genre-settings-table th{background:#1a0800;color:#f5a623;padding:8px 10px;text-align:left;font-size:11px;text-transform:uppercase}
    .genre-settings-table td{padding:8px 10px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}
    .genre-table-wrap{overflow-x:auto;margin:16px 0;background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:4px}

    /* Hardware/plugin table */
    .hardware-plugin-wrap{overflow-x:auto;margin:16px 0;background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:4px}
    .hardware-plugin-table{width:100%;border-collapse:collapse;font-size:13px}
    .hardware-plugin-table th{background:#1a1a3a;color:#f5a623;padding:8px 12px;font-size:11px;text-transform:uppercase;text-align:left}
    .hardware-plugin-table td{padding:8px 12px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}

    /* Signal chain diagram */
    .signal-chain-diagram{background:#0a0a16;border:2px solid #2a2a4a;border-radius:12px;padding:20px 16px 12px;overflow-x:auto;margin:16px 0;box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}

    /* Types grid */
    .types-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:16px 0}
    .type-card{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px;min-width:0}
    .type-name{font-size:14px;font-weight:700;color:#f5a623;margin-bottom:4px}
    .type-hardware{font-size:12px;color:#888;margin-bottom:8px;font-style:italic}
    .type-desc{font-size:13px;color:#c8c8d8;line-height:1.6}

    /* Misconception block */
    .misconception-block{background:#1a0000;border:2px solid #cc3333;border-radius:8px;padding:20px;margin:24px 0}
    .misconception-label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#cc3333;font-weight:700;margin-bottom:12px}
    .misconception-belief{color:#ff8888;font-weight:600;margin-bottom:8px}
    .misconception-reality{color:#c8c8d8}

    /* Before/after block */
    .before-after-block{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0;padding:16px;background:#0d0d20;border:1px solid #2a2a4a;border-radius:10px}
    .ba-before{background:#1a0000;border:1px solid #441111;border-radius:8px;padding:16px}
    .ba-after{background:#001a00;border:1px solid #114411;border-radius:8px;padding:16px}
    .ba-label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:8px}
    .ba-before .ba-label{color:#cc3333}
    .ba-after .ba-label{color:#33cc33}
    .ba-text{font-size:13px;color:#c8c8d8;line-height:1.6}

    /* Producer's verdict */
    .producers-verdict{background:#0d0d1a;border-top:4px solid #f5a623;border-left:1px solid #2a2a4a;border-right:1px solid #2a2a4a;border-bottom:1px solid #2a2a4a;border-radius:0 0 10px 10px;padding:28px 24px;margin:24px 0}
    .verdict-label{display:block;font-size:15px;text-transform:uppercase;letter-spacing:.15em;color:#f5a623;font-weight:800;margin-bottom:16px;text-align:center;padding-bottom:12px;border-bottom:1px solid #2a2a4a}
    .producers-verdict p{color:#e0e0f0;margin-bottom:14px;line-height:1.8;font-size:15px}
    .producers-verdict p:last-child{margin-bottom:0}

    /* Producer quote */
    .producer-quote-block{background:#0d1a1a;border-left:4px solid #14b8a6;border-radius:0 8px 8px 0;padding:20px;margin:24px 0}
    blockquote.producer-quote{font-size:1.1rem;color:#e0e0f0;font-style:italic;margin-bottom:8px;border:none;padding:0}
    blockquote.producer-quote p{color:#e0e0f0;margin-bottom:0}
    .producer-quote-block cite{font-size:12px;color:#888;display:block;margin-top:8px;font-style:normal}

    /* Red/Green flags */
    .red-green-flags{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0}
    .flags-col{background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:16px}
    .flags-col h4{font-size:13px;font-weight:700;margin-bottom:10px}
    .flags-col ul{list-style:none;margin:0;padding:0}
    .red-flag{background:#1a0000;border-left:3px solid #cc3333;padding:8px 12px;margin-bottom:6px;border-radius:0 4px 4px 0;font-size:13px;color:#ff9999}
    .green-flag{background:#001a00;border-left:3px solid #33cc33;padding:8px 12px;margin-bottom:6px;border-radius:0 4px 4px 0;font-size:13px;color:#99ff99}

    /* Interaction warnings */
    .interaction-warnings{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin:16px 0}
    .interaction-warnings h4{color:#f5a623;margin-bottom:12px;font-size:14px}
    .interaction-warnings ul{list-style:none;margin:0;padding:0}
    .interaction-warning{padding:10px 0;border-bottom:1px solid #2a2a4a;font-size:13px;color:#c8c8d8}
    .interaction-warning:last-child{border-bottom:none}

    /* Track citations — v5.1 text-only */
    .track-examples-list{display:flex;flex-direction:column;gap:10px;margin:16px 0}
    .track-item{background:#13132a;border-left:3px solid #f5a623;border-radius:0 6px 6px 0;padding:12px 16px;font-size:13px;color:#c8c8d8}
    .track-artist{font-weight:700;color:#f5a623}
    .track-name{font-weight:600;color:#e0e0f0}
    .track-meta{color:#888}
    .track-item .track-note{font-size:12px;color:#a0a0c0;margin-top:6px;font-style:italic}

    /* DAW tabs */
    .daw-tabs{margin:16px 0}
    .daw-tab-nav{display:flex;gap:4px;border-bottom:1px solid #2a2a4a;margin-bottom:0}
    .daw-tab-btn{background:none;border:none;border-bottom:2px solid transparent;color:#888;font-size:12px;font-weight:600;padding:8px 14px;cursor:pointer;font-family:inherit;margin-bottom:-1px;transition:color .15s,border-color .15s}
    .daw-tab-btn.active{color:#f5a623;border-bottom-color:#f5a623}
    .daw-tab-btn:hover{color:#d0d0d0}
    .daw-tab-content{background:#13132a;border:1px solid #2a2a4a;border-top:none;border-radius:0 0 8px 8px;padding:16px}
    .daw-tab-panel{display:none;font-size:13px;color:#c8c8d8;line-height:1.7}
    .daw-tab-panel.active{display:block}

    /* Plugin recs */
    .plugin-recs{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}
    .plugin-tier{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:14px}
    .plugin-tier-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:10px;display:block}
    .plugin-tier-free .plugin-tier-label{color:#60c0ff}
    .plugin-tier-mid .plugin-tier-label{color:#f5a623}
    .plugin-tier-pro .plugin-tier-label{color:#cc33cc}
    .plugin-item{font-size:12px;color:#c8c8d8;padding:5px 0;border-bottom:1px solid #1a1a3a}
    .plugin-item:last-child{border-bottom:none}
    .plugin-name{font-weight:600;color:#e0e0f0}
    .plugin-mfr{color:#888;font-size:11px}

    /* Last verified */
    .last-verified{font-size:11px;color:#555;text-align:center;padding:8px;margin-top:8px}

    /* PDF export */
    .pdf-export-btn{background:#1a1a3a;border:1px solid #2a2a4a;color:#a0a0c0;font-size:12px;font-weight:600;padding:8px 16px;border-radius:6px;cursor:pointer;font-family:inherit;transition:border-color .15s,color .15s}
    .pdf-export-btn:hover{border-color:#f5a623;color:#f5a623}
    .pgm-overlay{position:fixed;inset:0;background:rgba(0,0,0,.85);z-index:99997;display:flex;align-items:center;justify-content:center;padding:20px}
    .pgm-card{background:#1a1a2a;border:1px solid #2a2a4a;border-radius:12px;padding:32px;max-width:440px;width:100%;position:relative;text-align:center}
    .pgm-close{position:absolute;top:12px;right:14px;background:none;border:none;color:#666;font-size:18px;cursor:pointer}
    .pgm-card h3{color:#fff;font-size:18px;margin-bottom:8px}
    .pgm-card p{color:#a0a0c0;font-size:13px;margin-bottom:16px}
    .pgm-card input{width:100%;padding:10px 14px;border-radius:6px;border:1px solid #2a2a4a;background:#0d0d1a;color:#fff;font-size:14px;margin-bottom:10px}
    .pgm-submit{width:100%;background:#f5a623;color:#000;border:none;padding:11px;border-radius:6px;font-weight:700;font-size:14px;cursor:pointer}
    .pgm-fine{font-size:11px;color:#555;margin-top:10px}

    /* Producer spotlight */
    .producer-spotlight{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px;margin-bottom:16px}
    .producer-spotlight h3{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:12px;font-weight:700}
    .ps-card{padding:10px 0;border-bottom:1px solid #1a1a3a}
    .ps-card:last-of-type{border-bottom:none;padding-bottom:0}
    .ps-name{font-size:13px;font-weight:700;color:#e0e0f0;margin-bottom:2px}
    .ps-role{font-size:11px;color:#666;margin-bottom:6px}

    /* Mistakes */
    .mistakes-list{display:flex;flex-direction:column;gap:16px;margin:16px 0}
    .mistake-item{background:#1f0800;border-left:4px solid #ff6600;border-top:1px solid #3a1500;border-right:1px solid #3a1500;border-bottom:1px solid #3a1500;border-radius:0 8px 8px 0;padding:16px}
    .mistake-title{font-size:14px;font-weight:700;color:#ffaa44;margin-bottom:8px}
    .mistake-item p{font-size:13px;color:#e0c090;margin-bottom:6px;line-height:1.7}

    /* Progression path */
    .progression-path{display:flex;flex-direction:column;gap:0;margin:16px 0;border:2px solid #2a2a4a;border-radius:10px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,.3)}
    .prog-stage{padding:20px}
    .prog-beginner{background:#001a2a}
    .prog-intermediate{background:#0d1a00}
    .prog-advanced{background:#1a0800}
    .prog-label{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:8px}
    .prog-beginner .prog-label{color:#60c0ff}
    .prog-intermediate .prog-label{color:#60ff60}
    .prog-advanced .prog-label{color:#f5a623}
    .prog-stage p{font-size:13px;color:#c8c8d8;margin:0;line-height:1.7}

    /* Related terms */
    .related-terms-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:16px 0}
    .related-term-card{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:14px;text-decoration:none;display:flex;flex-direction:column;gap:4px;transition:border-color .2s}
    .related-term-card:hover{border-color:#f5a623}
    .rt-term{font-size:14px;font-weight:700;color:#f5a623}
    .rt-preview{font-size:12px;color:#888}

    /* FAQ */
    .faq-accordion{display:flex;flex-direction:column;gap:8px;margin:16px 0}
    .faq-item{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;overflow:hidden}
    .faq-q{width:100%;text-align:left;background:none;border:none;color:#e0e0f0;font-size:14px;font-weight:600;padding:16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center}
    .faq-q:hover{color:#f5a623}
    .faq-a{padding:0 16px 16px;display:none}
    .faq-a p{font-size:13px;color:#c8c8d8;line-height:1.7;margin:0}
    .faq-item.open .faq-a{display:block}
    .faq-item.open .faq-q{color:#f5a623}

    /* Social share */
    .social-share{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:48px 0 16px;padding:24px 28px;background:linear-gradient(135deg,#0d0d1a,#13132a);border:1px solid #2a2a4a;border-radius:12px}
    .share-label{font-size:11px;color:#666;text-transform:uppercase;letter-spacing:.1em;font-weight:700;flex-shrink:0;margin-right:4px}
    .share-btn{padding:8px 18px;border-radius:20px;font-size:13px;font-weight:600;text-decoration:none;cursor:pointer;border:1px solid #2a2a4a;background:transparent;color:#a0a0c0;font-family:inherit;transition:all .2s;letter-spacing:.02em}
    .share-btn:hover{border-color:#f5a623;color:#f5a623;background:rgba(245,166,35,.07)}
    .share-x:hover{border-color:#1d9bf0;color:#1d9bf0;background:rgba(29,155,240,.07)}

    /* Newsletter */
    .bible-nl-card{background:linear-gradient(135deg,#1a0a00 0%,#0d0d1a 100%);border-top:2px solid #f5a623;border-bottom:2px solid #f5a623;padding:48px 24px;margin:48px -24px;text-align:center}
    .nl-headline{font-size:1.5rem;font-weight:800;color:#0d0d0d;margin-bottom:6px;letter-spacing:-0.02em}
    .nl-sub{font-size:15px;color:#3a2000;margin-bottom:24px;font-weight:500}
    .nl-form{display:flex;gap:8px;max-width:440px;margin:0 auto;flex-wrap:wrap;justify-content:center}
    .nl-input{flex:1;min-width:220px;padding:12px 16px;border-radius:6px;border:1px solid rgba(0,0,0,.3);background:rgba(255,255,255,.9);color:#0d0d0d;font-size:14px}
    .nl-btn{background:#0d0d0d;color:#f5a623;border:none;padding:12px 24px;border-radius:6px;font-weight:800;cursor:pointer;white-space:nowrap;font-size:14px}

    /* Gain calculator */
    .gain-calculator{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin:16px 0}
    .gain-calculator h3{color:#f5a623;font-size:15px;margin-bottom:12px}
    .gain-calculator label{display:block;font-size:13px;color:#c8c8d8;margin-bottom:8px}
    .gain-calculator input{background:#0d0d1a;border:1px solid #2a2a4a;border-radius:4px;padding:6px 10px;color:#fff;font-size:13px;width:120px;margin-left:8px}

    /* Sidebar */
    .sidebar-toc{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin-bottom:16px}
    .sidebar-toc h4{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:12px;font-weight:700}
    .sidebar-toc a{display:block;color:#a0a0c0;text-decoration:none;font-size:13px;padding:4px 2px;border-bottom:1px solid #1a1a3a;border-left:2px solid transparent;transition:color .15s,border-color .15s,padding-left .15s}
    .sidebar-toc a:hover,.sidebar-toc a.active{color:#f5a623;border-left-color:#f5a623;padding-left:8px;font-weight:700}

    /* Sidebar newsletter */
    .sidebar-nl{background:#1a0a00;border:1px solid rgba(245,166,35,.3);border-radius:8px;padding:16px;margin-bottom:16px;text-align:center}
    .sidebar-nl h4{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:8px;font-weight:700}
    .sidebar-nl p{font-size:11px;color:#888;margin-bottom:10px;line-height:1.5}
    .sidebar-nl input{width:100%;padding:8px 10px;border-radius:5px;border:1px solid rgba(245,166,35,.3);background:#0d0d1a;color:#fff;font-size:12px;margin-bottom:8px}
    .sidebar-nl button{width:100%;background:#f5a623;color:#000;border:none;padding:8px;border-radius:5px;font-weight:700;font-size:12px;cursor:pointer}

    /* Footer */
    .site-footer{background:#0a0a1a;border-top:1px solid #1a1a3a;padding:32px 24px;text-align:center;margin-top:48px}
    .site-footer p{color:#666;font-size:13px;margin:4px 0}
    .site-footer a{color:#f5a623;text-decoration:none}
    .bm-publisher{display:inline-block;color:#f5a623;text-decoration:none;font-size:12px;font-weight:700;margin-bottom:8px}

    /* Comparison callouts */
    .comparison-callouts{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:32px 0}

    /* History cards */
    .history-card{background:#13132a;border-left:3px solid #3a3a6a;border-radius:0 8px 8px 0;padding:16px 20px;margin:16px 0}
    .sig-card{background:#13132a;border:1px solid #2a2a4a;border-left:3px solid #f5a623;border-radius:0 8px 8px 0;padding:16px 20px;margin:12px 0}
    .sig-track{font-size:14px;font-weight:700;color:#f5a623;margin-bottom:6px}
    .sig-settings{font-size:13px;color:#e0e0f0;margin-bottom:6px;font-family:monospace;background:#0d0d1a;padding:6px 10px;border-radius:4px}
    .sig-why{font-size:13px;color:#a0a0c0;line-height:1.6}
    .ps-move{font-size:11px;color:#f5a623;margin-top:4px;font-style:italic}

    /* Start here box — in inline style */

    /* ── MOBILE <=1024px ── */
    @media(max-width:1024px){
      .msb-links{display:none!important}
      .msb-pub{display:none!important}
      .msb-cta{display:none!important}
      .msb-mob{display:flex!important}
      .msb-logo{margin-right:auto!important}
    }

    /* ── MOBILE <=768px ── */
    @media(max-width:768px){
      #reading-progress{display:block}
      /* bible-bar stays visible on mobile as product identity */
      .bb-cats{display:none!important}
      .bb-all{display:none!important}
      .bb-divider{display:none!important}
      .bible-mobile-bar{display:none!important}
      .signal-chain-diagram svg{display:none}
      .signal-chain-mobile{display:flex!important}
      .bible-mobile-bar{display:flex!important;top:90px}
      .entry-nav{top:84px!important}
      [id].entry-section{scroll-margin-top:120px}
      .entry-main h2{scroll-margin-top:120px}
      .entry-sidebar{display:none!important}
      .bible-entry-wrap{grid-template-columns:1fr!important;padding:20px 16px!important}
      .bible-nl-card{margin:40px 0!important;padding:32px 20px!important}
      .parameters-grid{grid-template-columns:1fr!important}
      .types-grid{grid-template-columns:1fr!important}
      .verdict-grid{grid-template-columns:1fr!important}
      .verdict-rule{border-right:none!important}
      .verdict-lead,.verdict-close{padding:16px 18px!important}
      .plugin-recs{grid-template-columns:1fr!important}
      .red-green-flags{grid-template-columns:1fr!important}
      .before-after-block{grid-template-columns:1fr!important}
      .related-terms-grid{grid-template-columns:1fr!important}
      .entry-term{font-size:clamp(1.8rem,8vw,2.5rem)!important}
      .entry-masthead{padding:20px 16px!important}
      .qr-table-wrap,.genre-table-wrap,.hardware-plugin-wrap{max-width:100%;overflow-x:auto}
    }

    @media(max-width:600px){
      .daw-tab-nav{flex-wrap:wrap;gap:2px}
      .daw-tab-btn{font-size:11px;padding:6px 10px}
      .comparison-callouts{grid-template-columns:1fr!important}
    }

    @media(max-width:480px){
      .bible-entry-wrap{padding:12px!important}
      .entry-term{font-size:1.8rem!important}
      .types-grid{grid-template-columns:1fr!important}
      .plugin-recs{grid-template-columns:1fr!important}
      .comparison-callouts{grid-template-columns:1fr!important}
      .tn-value{font-size:2.2rem!important}
      .pgm-overlay{padding:12px}
      .pgm-card{padding:20px 16px}
      .pgm-card h3{font-size:15px}
      .quick-ref-table{font-size:11px}
      .quick-ref-table th,.quick-ref-table td{padding:6px 8px}
      .genre-settings-table{font-size:11px}
      .genre-settings-table th,.genre-settings-table td{padding:6px 6px}
      .track-item{padding:10px 12px;font-size:12px}
      .prog-stage{padding:14px}
      .history-card{padding:10px 12px!important}
      .section-share-bar{flex-direction:column!important;align-items:flex-start!important}
      .start-here-box a{font-size:11px!important;padding:2px 8px!important}
    }

    @media(max-width:400px){
      .prereq-chain{font-size:11px;gap:4px}
      .prereq-chain a{padding:2px 6px;font-size:10px}
      .gc-result-grid{grid-template-columns:1fr!important}
      .scm-label{font-size:12px}
      .scm-sub{font-size:10px}
    }

    @media(max-width:380px){
      .msb-name{font-size:11px}
      .mpw-slim-bar{padding:0 12px}
    }

    /* Signal chain mobile */
    .signal-chain-mobile{display:none;flex-direction:column;gap:0;align-items:stretch}
    .scm-box{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:10px 14px;position:relative}
    .scm-box.scm-active{background:#2a1400;border-color:#f5a623;border-width:2px}
    .scm-label{font-size:13px;font-weight:700;color:#c8c8d8}
    .scm-box.scm-active .scm-label{color:#f5a623}
    .scm-sub{font-size:11px;color:#555;margin-top:2px}
    .scm-box.scm-active .scm-sub{color:#a07030}
    .scm-arrow{text-align:center;color:#3a3a5a;font-size:16px;line-height:1.2;padding:2px 0}
    .scm-badge{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#f5a623;background:rgba(245,166,35,.12);border:1px solid rgba(245,166,35,.3);padding:2px 7px;border-radius:10px;display:inline-block;margin-top:4px}

    /* Print */
    /* Producer's Verdict — authoritative */
    .producers-verdict{background:#080810;border:none;border-radius:12px;padding:0;margin:32px 0;overflow:hidden}
    .verdict-header{background:#f5a623;padding:16px 24px;display:flex;align-items:center;justify-content:center;gap:16px;border-radius:12px 12px 0 0}
    .verdict-label{display:inline!important;font-size:14px!important;font-weight:900!important;letter-spacing:.2em!important;text-transform:uppercase!important;color:#0d0d0d!important;border:none!important;padding:0!important;margin:0!important}
    .verdict-diamond{color:#0d0d0d;font-size:12px;opacity:.6}
    .verdict-lead{font-size:15px;color:#d0d0e0;line-height:1.8;padding:20px 24px;margin:0;font-style:italic;border-bottom:1px solid #1a1a3a;text-align:center}
    .verdict-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border-bottom:1px solid #1a1a3a}
    .verdict-rule{padding:16px 18px;border-right:1px solid #1a1a3a;border-bottom:1px solid #1a1a3a;display:flex;flex-direction:column;gap:6px;background:#1a1a2e}
    .verdict-rule:nth-child(even){border-right:none}
    .vr-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:#f5a623}
    .vr-value{font-size:14px;font-weight:700;color:#fff;line-height:1.4}
    .vr-note{font-size:13px;color:#b0b0c8;line-height:1.7}
    .verdict-share{display:flex;align-items:center;justify-content:center;gap:12px;padding:16px 24px;background:#0d0d1a;border-top:1px solid #1a1a3a;border-radius:0 0 12px 12px;flex-wrap:wrap}
    .verdict-close{font-size:13px;color:#a0a0c0;line-height:1.8;padding:16px 24px;margin:0;font-style:italic;text-align:center;border-top:1px solid #1a1a3a}

        @media print{
      .mpw-slim-bar,.bible-bar,.entry-nav,.entry-sidebar,.bible-nl-card,.site-footer,.social-share,.pdf-export-btn,.pgm-overlay,.bible-mobile-bar{display:none!important}
      .bible-entry-wrap{display:block!important;padding:0!important}
      body{background:#fff;color:#000}
      .entry-main h2,.entry-main p,.entry-main li{color:#000}
    }
  </style>

  <style>
    /* CONSOLIDATED OVERRIDES v5.2 FINAL */
    .entry-nav-inner{margin:0!important}

    /* Desktop sidebar + grid */
    @media(min-width:769px){
      .bible-entry-wrap{display:grid!important;grid-template-columns:1fr 280px!important;padding:40px 24px!important;gap:40px!important}
      .entry-sidebar{display:block!important;position:sticky!important;top:148px!important;align-self:start!important;height:calc(100vh - 168px)!important;overflow-y:auto!important;overflow-x:hidden!important;scrollbar-width:thin!important;scrollbar-color:#2a2a4a transparent!important}
    }

    /* Mobile */
    @media(max-width:1024px){
      .msb-logo{margin-right:auto!important}
      .msb-search{order:10}
      .msb-mob{order:11}
      .bible-bar{display:flex!important;top:40px!important;height:44px!important;padding:0 16px!important}
      .bb-cats{display:none!important}
      .bb-all{display:none!important}
      .bb-divider{display:none!important}
    }
    .bible-mobile-bar{display:none!important}
    @media(max-width:768px){
      .bible-entry-wrap{display:block!important;padding:20px 16px!important}
      .entry-sidebar{display:none!important}
      .entry-nav{top:84px!important}
      [id].entry-section{scroll-margin-top:110px!important}
      .entry-main h2{scroll-margin-top:110px!important}
      .types-grid{grid-template-columns:1fr!important}
      .plugin-recs{grid-template-columns:1fr!important}
      .verdict-grid{grid-template-columns:1fr!important}
      .verdict-rule{border-right:none!important}
      .verdict-lead,.verdict-close{padding:16px!important}
      .vr-label{font-size:11px!important}
      .vr-value{font-size:15px!important}
      .vr-note{font-size:13px!important;color:#b0b0c8!important}
    }
    @media(max-width:480px){
      .mpw-share-btn{padding:6px 10px;font-size:11px}
    }

    /* Producer's Verdict */
    .producers-verdict{background:#080810!important;border:none!important;border-radius:12px!important;padding:0!important;margin:32px 0!important;overflow:hidden!important}
    .verdict-header{background:#f5a623;padding:16px 24px;display:flex;align-items:center;justify-content:center;gap:16px;border-radius:12px 12px 0 0}
    .verdict-label{display:inline!important;font-size:14px!important;font-weight:900!important;letter-spacing:.2em!important;text-transform:uppercase!important;color:#0d0d0d!important;border:none!important;padding:0!important;margin:0!important}
    .verdict-diamond{color:#0d0d0d;font-size:12px;opacity:.6}
    .verdict-lead{font-size:14px!important;color:#d0d0e0!important;line-height:1.8!important;padding:20px 24px!important;margin:0!important;font-style:italic;border-bottom:1px solid #1a1a3a;text-align:center!important}
    .verdict-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border-bottom:1px solid #1a1a3a}
    .verdict-rule{padding:16px 18px;border-right:1px solid #1a1a3a;border-bottom:1px solid #1a1a3a;display:flex;flex-direction:column;gap:6px;background:#1a1a2e}
    .verdict-rule:nth-child(even){border-right:none}
    .vr-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:#f5a623}
    .vr-value{font-size:14px;font-weight:700;color:#fff;line-height:1.4}
    .vr-note{font-size:13px;color:#b0b0c8;line-height:1.7}
    .verdict-close{font-size:13px!important;color:#a0a0c0!important;line-height:1.8!important;padding:16px 24px!important;margin:0!important;font-style:italic;text-align:center;border-top:1px solid #1a1a3a}

    /* Mistakes */
    .mistake-item{background:#1f0800!important;border-left:4px solid #ff6600!important;border-top:1px solid #3a1500!important;border-right:1px solid #3a1500!important;border-bottom:1px solid #3a1500!important;border-radius:0 8px 8px 0!important}
    .mistake-title{color:#ffaa44!important}
    .mistake-item p{color:#e0c090!important;line-height:1.7!important}

    /* Newsletter */
    .bible-nl-card{background:#f5a623!important;border-top:2px solid #c47d00!important;border-bottom:2px solid #c47d00!important}
    .nl-headline{color:#0d0d0d!important}
    .nl-sub{color:#3a2000!important;font-weight:500!important}
    .nl-input{background:rgba(255,255,255,.9)!important;color:#0d0d0d!important;border-color:rgba(0,0,0,.2)!important}
    .nl-btn{background:#0d0d0d!important;color:#f5a623!important}

    /* Unified share bars */
    .mpw-share-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:14px;padding-top:14px;border-top:1px solid #2a2a4a}
    .mpw-share-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#666;width:100%;margin-bottom:4px}
    .mpw-share-btn{display:inline-flex;align-items:center;justify-content:center;gap:4px;flex:1 1 0;min-width:0;height:34px;padding:0 8px;border-radius:6px;font-size:11px;font-weight:700;text-decoration:none;cursor:pointer;font-family:inherit;box-sizing:border-box;transition:opacity .15s}
    .mpw-share-btn:hover{opacity:0.82}
    .mpw-share-btn.share-x{background:#000;color:#fff;border:1px solid #000}
    .mpw-share-btn.share-reddit{background:#ff4500;color:#fff;border:1px solid #ff4500}
    .mpw-share-btn.share-copy{background:#f5a623;color:#000;border:1px solid #f5a623}
    .footer-share-btn{flex:0 0 auto!important;width:auto!important;padding:0 18px!important}
    @media(max-width:768px){
      .mpw-share-bar{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:6px!important}
      .mpw-share-label{grid-column:1 / -1!important}
      .mpw-share-btn{width:100%!important;height:34px!important}
    }

    /* DAW tabs active state */
    .daw-tab-btn{background:#0d0d1a!important;color:#888!important}
    .daw-tab-btn.active{background:#0d0d1a!important;color:#f5a623!important;border-bottom-color:#f5a623!important}
    .daw-tab-btn:hover{background:#0d0d1a!important;color:#d0d0d0!important}

    /* Entry nav tap targets */
    .entry-nav-inner a{min-height:32px;display:inline-flex;align-items:center;font-size:10px!important;padding:6px 10px!important}

    /* calc-share-bar: auto-width buttons */
    .calc-share-bar{justify-content:flex-start!important}
    .calc-share-bar .mpw-share-btn{flex:0 0 auto!important;width:auto!important;padding:0 18px!important}
    .calc-share-bar .mpw-share-btn.share-copy{background:#f5a623!important;color:#000!important;border-color:#f5a623!important}
    @media(max-width:768px){
      .calc-share-bar{display:grid!important;grid-template-columns:1fr 1fr 1fr!important;gap:6px!important}
      .calc-share-bar .mpw-share-label{grid-column:1 / -1!important}
      .calc-share-bar .mpw-share-btn{width:100%!important;padding:0 4px!important;font-size:11px!important;justify-content:center!important}
    }
  </style>"""

# ══════════════════════════════════════════════════════════════════════════════
# SEO HEAD BLOCK — v5.1 (5 schema blocks)
# ══════════════════════════════════════════════════════════════════════════════

def build_head(slug, term, category, p1, pub_date, today_str, word_count, read_min):
    description = p1.get('definition', f'{term} — complete producer reference in The Producer\'s Bible.')
    keywords_list = p1.get('tags', [term, category]) + [f'{term} music production', f'{term} settings']
    keywords = ', '.join(keywords_list)
    url = f"https://musicproductionwiki.com/bible/{slug}"
    cat_slug = CATEGORY_SLUG_MAP.get(category, category.lower().replace(' ', '-'))

    same_as = []
    wiki  = p1.get('wikipedia_slug')
    wdata = p1.get('wikidata_id')
    if wiki:
        same_as.append(f"https://en.wikipedia.org/wiki/{wiki}")
    if wdata:
        same_as.append(f"https://www.wikidata.org/wiki/{wdata}")

    same_as_json = json.dumps(same_as, indent=2) if same_as else '[]'

    faq_json_items = ''
    for q in (p1.get('faq') or []):
        faq_json_items += json.dumps({
            "@type": "Question",
            "name": q.get('q',''),
            "acceptedAnswer": {"@type": "Answer", "text": q.get('a','')}
        }, ensure_ascii=False) + ',\n    '
    faq_json_items = faq_json_items.rstrip(',\n ')

    howto_steps = ''
    daw_impl = p1.get('daw_implementations', {})
    params = p1.get('section_summaries', {})
    step_list = []
    if daw_impl.get('ableton'):
        step_list.append({"name": "Set up in Ableton Live", "text": daw_impl['ableton'][:200]})
    if daw_impl.get('logic'):
        step_list.append({"name": "Set up in Logic Pro", "text": daw_impl['logic'][:200]})
    if not step_list:
        step_list = [
            {"name": "Understand the parameters", "text": params.get('parameters','Learn the key parameters first.')},
            {"name": "Apply to a source", "text": params.get('how_it_works','Apply and listen critically.')},
        ]
    howto_steps = json.dumps(step_list, indent=2, ensure_ascii=False)
    css_block = build_css()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{term} — The Producer's Bible | MusicProductionWiki.com</title>
  <meta name="description" content="{description[:160]}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <link rel="canonical" href="{url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{term} — The Producer's Bible">
  <meta property="og:description" content="{description[:200]}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://musicproductionwiki.com/images/og-default.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="MusicProductionWiki">
  <meta property="article:published_time" content="{pub_date}T00:00:00Z">
  <meta property="article:modified_time" content="{today_str}T00:00:00Z">
  <meta property="article:section" content="{category}">
  <meta property="og:locale" content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{term} — The Producer's Bible">
  <meta name="twitter:description" content="{description[:200]}">
  <meta name="twitter:image" content="https://musicproductionwiki.com/images/og-default.jpg">
  <meta name="twitter:site" content="@mpwikiofficial">

  <!-- GA4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-79VB543KCT"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-79VB543KCT');</script>

  <!-- Schema: Article -->
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{term} \\u2014 The Producer\\u2019s Bible",
  "description": "{description[:200]}",
  "url": "{url}",
  "datePublished": "{pub_date}",
  "dateModified": "{today_str}",
  "wordCount": {word_count},
  "image": "https://musicproductionwiki.com/images/og-default.jpg",
  "author": {{
    "@type": "Organization",
    "name": "MusicProductionWiki",
    "url": "https://musicproductionwiki.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "MusicProductionWiki",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://musicproductionwiki.com/images/logo.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{url}"
  }},
  "about": {{
    "@type": "Thing",
    "name": "{term}",
    "sameAs": {same_as_json}
  }},
  "isPartOf": {{
    "@type": "WebSite",
    "name": "MusicProductionWiki",
    "url": "https://musicproductionwiki.com"
  }},
  "lastReviewed": "{today_str}"
}}</script>

  <!-- Schema: FAQPage -->
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {faq_json_items}
  ]
}}</script>

  <!-- Schema: BreadcrumbList -->
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://musicproductionwiki.com"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "The Producer's Bible",
      "item": "https://musicproductionwiki.com/bible/"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{term}",
      "item": "{url}"
    }}
  ]
}}</script>

  <!-- Schema: Speakable -->
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "{url}",
  "speakable": {{
    "@type": "SpeakableSpecification",
    "cssSelector": [".qa-text", ".entry-term", ".entry-hook"]
  }}
}}</script>

  <!-- Schema: HowTo -->
  <script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Use {term} in Music Production",
  "description": "Step-by-step guide to applying {term} in your productions.",
  "totalTime": "PT10M",
  "step": {howto_steps}
}}</script>

  <link rel="stylesheet" href="/css/style.css">
{css_block}
</head>"""

    return head.format(
        term=term, slug=slug, category=category, url=url,
        description=description[:200],
        keywords=keywords,
        pub_date=pub_date, today_str=today_str,
        word_count=word_count, read_min=read_min,
        same_as_json=same_as_json,
        faq_json_items=faq_json_items,
        cat_slug=cat_slug,
        howto_steps=howto_steps,
        css_block=build_css(),
    )


# ══════════════════════════════════════════════════════════════════════════════
# NAV HTML
# ══════════════════════════════════════════════════════════════════════════════

def build_nav_html(category):
    cat_slug = CATEGORY_SLUG_MAP.get(category, category.lower().replace(' ', '-'))
    cats = [
        ('dynamics',          'Dynamics'),
        ('frequency',         'Frequency'),
        ('time-based',        'Time-Based'),
        ('signal-processing', 'Signal Processing'),
        ('mixing',            'Mixing'),
        ('mastering',         'Mastering'),
        ('synthesis',         'Synthesis'),
        ('music-theory',      'Music Theory'),
    ]
    cat_pills = ''
    for cs, cl in cats:
        active = ' active' if cs == cat_slug else ''
        cat_pills += f'    <a href="/bible/categories/{cs}" class="bb-cat{active}">{cl}</a>\n'

    return f"""
<div id="reading-progress"></div>

<!-- MPW Slim Bar -->
<div class="mpw-slim-bar">
  <a href="/" class="msb-logo" aria-label="MusicProductionWiki home">
    <div class="msb-logomark">
      <svg width="14" height="14" viewBox="0 0 18 18" fill="none" aria-hidden="true">
        <rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
        <rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>
        <rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>
        <rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>
      </svg>
    </div>
    <span class="msb-name">MusicProductionWiki</span>
  </a>
  <ul class="msb-links" role="list">
    <li><a href="/categories/techniques.html">Articles</a></li>
    <li><a href="/categories/gear.html">Gear</a></li>
    <li><a href="/about.html">About</a></li>
  </ul>
  <span class="msb-pub">A MusicProductionWiki Publication</span>
  <button class="msb-search" id="bmnSearchBtn" aria-label="Open search">
    <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><circle cx="6.5" cy="6.5" r="4.5" stroke="currentColor" stroke-width="1.5"/><path d="M10 10l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
  </button>
  <a href="https://theproducersbriefing.beehiiv.com" class="msb-cta">Sound Better \u2192</a>
  <button class="msb-mob" id="bmnMob" aria-label="Toggle menu">
    <span></span><span></span><span></span>
  </button>
</div>

<!-- Bible Bar -->
<div class="bible-bar">
  <a href="/bible/" class="bb-identity">
    <span class="bb-diamond">\u25c6</span>
    <span class="bb-title">The Producer's Bible</span>
  </a>
  <div class="bb-divider"></div>
  <nav class="bb-cats" aria-label="Bible categories">
{cat_pills}  </nav>
  <a href="/bible/index.html" class="bb-all">All entries \u2192</a>
</div>

<!-- Mobile drawer -->
<div class="bmn-drawer" id="bmnDrawer" role="dialog" aria-label="Navigation menu">
  <a href="/bible/" class="bmn-drawer-bible">\u25c6 The Producer's Bible</a>
  <div class="bmn-drawer-label">Browse The Bible</div>
  <div class="bmn-drawer-cats">
    <a href="/bible/categories/dynamics" class="bmn-drawer-cat">Dynamics</a>
    <a href="/bible/categories/frequency" class="bmn-drawer-cat">Frequency</a>
    <a href="/bible/categories/time-based" class="bmn-drawer-cat">Time-Based</a>
    <a href="/bible/categories/signal-processing" class="bmn-drawer-cat">Signal Processing</a>
    <a href="/bible/categories/mixing" class="bmn-drawer-cat">Mixing</a>
    <a href="/bible/categories/mastering" class="bmn-drawer-cat">Mastering</a>
    <a href="/bible/categories/synthesis" class="bmn-drawer-cat">Synthesis</a>
    <a href="/bible/categories/music-theory" class="bmn-drawer-cat">Music Theory</a>
  </div>
  <a href="/bible/" style="font-size:13px;color:#f5a623;padding:6px 12px;display:block">All entries \u2192</a>
  <div class="bmn-drawer-label">Articles</div>
  <div class="bmn-drawer-cats">
    <a href="/categories/techniques.html" class="bmn-drawer-cat">Techniques</a>
    <a href="/categories/reviews.html" class="bmn-drawer-cat">Reviews</a>
    <a href="/categories/comparisons.html" class="bmn-drawer-cat">Comparisons</a>
    <a href="/categories/breakdowns.html" class="bmn-drawer-cat">Breakdowns</a>
    <a href="/categories/gear.html" class="bmn-drawer-cat">Hardware</a>
    <a href="/about.html" class="bmn-drawer-cat">About</a>
  </div>
  <a href="https://theproducersbriefing.beehiiv.com" class="bmn-drawer-cta">Sound Better \u2192</a>
</div>

<!-- Mobile bible bar -->
<div class="bible-mobile-bar" aria-hidden="true">The Producer's Bible</div>

<!-- Search overlay -->
<div id="bibleSearchOverlay" role="dialog" aria-modal="true" aria-label="Search">
  <div class="bso-box">
    <div class="bso-input-wrap">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="6.5" cy="6.5" r="4.5" stroke="#666" stroke-width="1.5"/><path d="M10 10l3.5 3.5" stroke="#666" stroke-width="1.5" stroke-linecap="round"/></svg>
      <input id="bibleSearchInput" type="text" placeholder="Search articles and Bible entries\u2026" autocomplete="off" spellcheck="false" aria-label="Search">
      <span style="font-size:11px;color:#555;white-space:nowrap;flex-shrink:0">ESC to close</span>
    </div>
    <div id="bibleSearchResults" role="listbox"></div>
  </div>
</div>
"""


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY NAV — 19 pills, no label
# ══════════════════════════════════════════════════════════════════════════════

ENTRY_NAV_LINKS = [
    ('#definition',      'Definition'),
    ('#how-it-works',    'How It Works'),
    ('#parameters',      'Parameters'),
    ('#quick-reference', 'Quick Ref'),
    ('#tools',           'Tools'),
    ('#signal-chain',    'Signal Chain'),
    ('#history',         'History'),
    ('#how-to-use',      'How To Use'),
    ('#genre-table',     'By Genre'),
    ('#hardware-plugin', 'Hardware vs Plugin'),
    ('#before-after',    'Before / After'),
    ('#in-the-wild',     'In The Wild'),
    ('#signatures',      'Signatures'),
    ('#types',           'Types'),
    ('#verdict',         'Verdict'),
    ('#plugin-recs',     'Plugins'),
    ('#mistakes',        'Mistakes'),
    ('#flags',           'Flags'),
    ('#progression',     'Progression'),
    ('#faq',             'FAQ'),
    ('#related',         'Related'),
]

def build_entry_nav():
    links = ''.join(f'    <a href="{href}">{label}</a>\n' for href, label in ENTRY_NAV_LINKS)
    return (
        '<nav class="entry-nav" aria-label="Entry sections">\n'
        '  <div class="entry-nav-inner">\n'
        f'{links}'
        '  </div>\n</nav>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# JAVASCRIPT
# ══════════════════════════════════════════════════════════════════════════════

def build_js(slug, p1):
    daw_js = r"""
function dawTab(btn, daw) {
  document.querySelectorAll('.daw-tab-btn').forEach(function(b){ b.classList.remove('active'); });
  document.querySelectorAll('.daw-tab-panel').forEach(function(p){ p.classList.remove('active'); });
  btn.classList.add('active');
  var panel = document.getElementById('dtp-' + daw + '-""" + slug + r"""');
  if (panel) panel.classList.add('active');
}"""

    toc_js = r"""
(function(){
  var tocLinks = document.querySelectorAll('.sidebar-toc a');
  function setTocActive(id) {
    tocLinks.forEach(function(a){
      a.classList.toggle('active', a.getAttribute('href') === '#' + id);
    });
  }
  var sections = document.querySelectorAll('.entry-section[id]');
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if (e.isIntersecting) setTocActive(e.target.id); });
  }, {rootMargin: '-120px 0px -60% 0px'});
  sections.forEach(function(s){ obs.observe(s); });
  if (sections[0]) setTocActive(sections[0].id);
})();"""

    enav_js = r"""
(function(){
  var navLinks = document.querySelectorAll('.entry-nav-inner a');
  var sections = Array.from(document.querySelectorAll('.entry-section[id]'));
  var lastActive = null;
  function getActiveId() {
    var offset = 60;
    var best = null;
    for (var i = 0; i < sections.length; i++) {
      var rect = sections[i].getBoundingClientRect();
      if (rect.top <= offset && rect.bottom > offset) { best = sections[i].id; break; }
    }
    if (!best) {
      for (var j = sections.length - 1; j >= 0; j--) {
        if (sections[j].getBoundingClientRect().top <= offset) { best = sections[j].id; break; }
      }
    }
    return best || (sections[0] && sections[0].id);
  }
  function update() {
    var id = getActiveId();
    if (!id || id === lastActive) return;
    lastActive = id;
    navLinks.forEach(function(a){
      a.classList.toggle('active', a.getAttribute('href') === '#' + id);
    });
    var activeLink = document.querySelector('.entry-nav-inner a.active');
    if (activeLink) activeLink.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});
  }
  window.addEventListener('scroll', update, {passive:true});
  window.addEventListener('touchmove', update, {passive:true});
  update();
})();"""

    progress_js = r"""
(function(){
  var bar = document.getElementById('reading-progress');
  if (!bar) return;
  window.addEventListener('scroll', function(){
    var s = document.documentElement.scrollTop;
    var h = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    bar.style.width = (h > 0 ? (s/h*100) : 0) + '%';
  }, {passive: true});
})();"""

    hamburger_js = r"""
(function(){
  var mob = document.getElementById('bmnMob');
  var drawer = document.getElementById('bmnDrawer');
  if (mob && drawer) {
    mob.addEventListener('click', function(){ drawer.classList.toggle('open'); });
    document.addEventListener('click', function(e){
      if (!drawer.contains(e.target) && e.target !== mob) drawer.classList.remove('open');
    });
  }
})();"""

    search_js = r"""
(function(){
  var overlay = document.getElementById('bibleSearchOverlay');
  var input   = document.getElementById('bibleSearchInput');
  var results = document.getElementById('bibleSearchResults');
  var sBtn    = document.getElementById('bmnSearchBtn');
  var index   = null;
  function openSearch(){ overlay.style.display='flex'; setTimeout(function(){ input&&input.focus(); },50); if(!index) fetch('/bible-index.json').then(function(r){return r.json();}).then(function(d){index=d;}).catch(function(){}); }
  function closeSearch(){ overlay.style.display='none'; if(results) results.innerHTML=''; }
  if(sBtn) sBtn.addEventListener('click', openSearch);
  document.addEventListener('keydown', function(e){ if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();openSearch();} if(e.key==='Escape') closeSearch(); });
  if(overlay) overlay.addEventListener('click', function(e){ if(e.target===overlay) closeSearch(); });
  if(input) input.addEventListener('input', function(){
    var q=input.value.trim().toLowerCase();
    if(!q||!index||!results){results.innerHTML='';return;}
    var hits=index.filter(function(e){return e.term.toLowerCase().includes(q)||(e.category||'').toLowerCase().includes(q);}).slice(0,8);
    results.innerHTML=hits.map(function(e){return '<a href="/bible/'+e.slug+'" style="display:block;padding:10px 16px;color:#e0e0f0;text-decoration:none;border-radius:6px;font-size:14px"><strong>'+e.term+'</strong> <span style="color:#666;font-size:12px">'+e.category+'</span></a>';}).join('');
  });
})();"""

    # EMAIL GATE — temporarily bypassed (no API plan)
    # TODO P3.5: wire up Kit or Brevo free API
    _gate_template = (
        "\nvar _gateAsset = 'full';\n"
        "// EMAIL GATE bypassed — downloads fire directly (TODO P3.5: Kit/Brevo API)\n"
        "function openGateFor(asset) {\n"
        "  _gateAsset = asset || 'full';\n"
        "  if (_gateAsset === 'full') { window.print(); }\n"
        "  else if (_gateAsset === 'quickref') { downloadQuickRef(); }\n"
        "  else if (_gateAsset === 'genre') { downloadGenreTable(); }\n"
        "}\n"
        "function closeGate() { var m=document.getElementById('pdf-gate-modal'); if(m) m.style.display='none'; }\n"
        "function submitGate() { openGateFor(_gateAsset); }\n"
        "function submitPdfGate() { window.print(); }\n"
        "function downloadQuickRef() {\n"
        "  var rows=document.querySelectorAll('.quick-ref-table tr');\n"
        "  var txt=Array.from(rows).map(function(r){return Array.from(r.querySelectorAll('th,td')).map(function(c){return c.textContent.trim()}).join('\\t')}).join('\\n');\n"
        "  txt+='\\nSource: musicproductionwiki.com/bible/SLUG_PLACEHOLDER';\n"
        "  var b=new Blob([txt],{type:'text/plain'});var a=document.createElement('a');\n"
        "  a.href=URL.createObjectURL(b);a.download='SLUG_PLACEHOLDER-quick-reference.txt';a.click();\n"
        "}\n"
        "function downloadGenreTable() {\n"
        "  var rows=document.querySelectorAll('.genre-settings-table tr,.genre-table tr');\n"
        "  var txt=Array.from(rows).map(function(r){return Array.from(r.querySelectorAll('th,td')).map(function(c){return c.textContent.trim()}).join('\\t')}).join('\\n');\n"
        "  txt+='\\nSource: musicproductionwiki.com/bible/SLUG_PLACEHOLDER';\n"
        "  var b=new Blob([txt],{type:'text/plain'});var a=document.createElement('a');\n"
        "  a.href=URL.createObjectURL(b);a.download='SLUG_PLACEHOLDER-genre-settings.txt';a.click();\n"
        "}"
    )
    gate_js = _gate_template.replace('SLUG_PLACEHOLDER', slug)

    calc_js = r"""
(function(){
  function calcGR() {
    var inp  = parseFloat((document.getElementById('gc-input')  ||{}).value)  || -10;
    var thr  = parseFloat((document.getElementById('gc-thresh') ||{}).value)  || -18;
    var rat  = parseFloat((document.getElementById('gc-ratio')  ||{}).value)  || 4;
    var mkup = parseFloat((document.getElementById('gc-makeup') ||{}).value)  || 6;
    if (!document.getElementById('gc-input')) return;
    var excess=inp-thr; var gr=excess>0?excess-excess/rat:0; var out=inp-gr;
    var set = function(id,v){ var el=document.getElementById(id); if(el) el.textContent=v; };
    set('gc-gr',   (gr>0?'-':'')+gr.toFixed(1)+' dB');
    set('gc-excess',(excess>0?'+':'')+excess.toFixed(1)+' dB');
    set('gc-out',  out.toFixed(1)+' dBFS');
    set('gc-final',(out+mkup).toFixed(1)+' dBFS');
  }
  ['gc-input','gc-thresh','gc-ratio','gc-makeup'].forEach(function(id){
    var el=document.getElementById(id); if(el) el.addEventListener('input', calcGR);
  });
  calcGR();
})();"""

    daw_pref_js = r"""
(function(){
  var DAW_KEY='mpw_daw_pref';
  var pref=localStorage.getItem(DAW_KEY);
  if(pref && typeof dawTab==='function'){
    var btn=document.querySelector('.daw-tab-btn[data-daw="'+pref+'"]');
    if(btn) dawTab(btn,pref);
  }
  document.querySelectorAll('.daw-tab-btn').forEach(function(b){
    b.addEventListener('click',function(){ localStorage.setItem(DAW_KEY,b.dataset.daw); });
  });
})();"""

    return (
        '<script>\n'
        + daw_js + '\n'
        + toc_js + '\n'
        + enav_js + '\n'
        + progress_js + '\n'
        + hamburger_js + '\n'
        + search_js + '\n'
        + gate_js + '\n'
        + calc_js + '\n'
        + daw_pref_js + '\n'
        + '</script>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════

def build_footer(term, slug, today_str):
    x_url   = f'https://x.com/intent/tweet?text={term}+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}'
    rd_url  = f'https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}&title={term}+%E2%80%94+The+Producer%27s+Bible'
    x_svg   = '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.26 5.632 5.905-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
    rd_svg  = '<svg width="12" height="12" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="10"/><path fill="#ff4500" d="M16.67 10a1.46 1.46 0 00-2.47-1 7.12 7.12 0 00-3.85-1.23l.65-3.08 2.13.45a1 1 0 101.07-1 1 1 0 00-.96.68l-2.38-.5a.27.27 0 00-.32.2l-.73 3.44a7.14 7.14 0 00-3.89 1.23 1.46 1.46 0 10-1.61 2.39 2.87 2.87 0 000 .44c0 2.24 2.61 4.06 5.83 4.06s5.83-1.82 5.83-4.06a2.87 2.87 0 000-.44 1.46 1.46 0 00.61-1.08zM7.5 11a1 1 0 111 1 1 1 0 01-1-1zm5.67 2.65a3.54 3.54 0 01-2.34.63 3.54 3.54 0 01-2.34-.63.25.25 0 01.35-.35 3.07 3.07 0 002 .48 3.07 3.07 0 002-.48.25.25 0 01.35.35zm-.17-1.65a1 1 0 111-1 1 1 0 01-1 1z"/></svg>'
    return (
        '<div class="bible-nl-card">\n'
        '  <div class="nl-headline">The Producer\'s Briefing</div>\n'
        '  <div class="nl-sub">The Producer\'s Briefing \u2014 practical technique, gear intel, no fluff.</div>\n'
        '  <div class="nl-form">\n'
        '    <input class="nl-input" type="email" placeholder="your@email.com" aria-label="Email address">\n'
        '    <button class="nl-btn">Subscribe Free</button>\n'
        '  </div>\n'
        '</div>\n\n'
        '<footer class="site-footer">\n'
        '  <a href="/bible/" class="bm-publisher">\u25c6 The Producer\'s Bible</a>\n'
        f'  <p style="font-size:15px;font-weight:600;color:#e0e0f0;margin:8px 0 4px">MusicProductionWiki.com</p>\n'
        '  <p style="font-size:12px;color:#666;margin-bottom:16px">The most comprehensive music production reference on the internet.</p>\n'
        f'  <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:16px;flex-wrap:wrap">\n'
        '    <span style="font-size:11px;color:#555;text-transform:uppercase;letter-spacing:.08em">Share</span>\n'
        f'    <a href="{x_url}" target="_blank" rel="noopener" style="padding:6px 14px;border-radius:20px;border:1px solid #2a2a4a;color:#a0a0c0;font-size:12px;text-decoration:none">X</a>\n'
        f'    <a href="{rd_url}" target="_blank" rel="noopener" style="padding:6px 14px;border-radius:20px;border:1px solid #2a2a4a;color:#a0a0c0;font-size:12px;text-decoration:none">Reddit</a>\n'
        '  </div>\n'
        '  <p><a href="/">Home</a> &middot; <a href="/about.html">About</a> &middot; <a href="/bible/">Producer\'s Bible</a> &middot; <a href="/categories/techniques.html">Techniques</a> &middot; <a href="/categories/reviews.html">Reviews</a> &middot; <a href="/categories/comparisons.html">Comparisons</a></p>\n'
        f'  <p style="margin-top:8px;font-size:11px;color:#444">&copy; 2026 MusicProductionWiki.com &mdash; Built for producers, by producers.</p>\n'
        '</footer>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# PASS 2 PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

PASS2_SYSTEM_T1 = (
    "You are writing a Tier 1 Producer's Bible entry for MusicProductionWiki.com.\n"
    "Return ONLY raw HTML sections -- no markdown, no fences, no explanations, no </body></html>.\n"
    "Write in producer-language: direct, authoritative, specific, creative and intuitive, mentoring, demystifying, popularizing, and interesting. No hedging.\n"
    "Target: 6,700-7,300 words of prose. Long-form professional reference.\n"
    "Every section tag must have the exact ID shown. Use entry-section class on every section.\n"
    "Leave PLACEHOLDERS exactly as shown -- do not fill them in.\n"
    "Exactly 3 producer quotes from quotes_context -- first in definition, second in history, third in how-to-use. NEVER fabricate quotes.\n"
    "verdict-lead: 3-4 sentences of real opinion -- biggest mistake producers make, why it happens, correct mental model. Not a summary.\n"
    "Internal links: /bible/slug only, confirmed slugs only, never self-link.\n"
)

def build_pass2_prompt_t1(slug, term, category, p1_json_str, track_list_str, quotes_context, pub_date):
    emotional_hook = ''
    try:
        p1_data = json.loads(p1_json_str[:8000])
        emotional_hook = p1_data.get('emotional_hook', '')
        producers_verdict = p1_data.get('producers_verdict', '')
    except Exception:
        producers_verdict = ''
    return f"""Write the full HTML prose for this Tier 1 Producer's Bible entry.

TERM: {term} | SLUG: {slug} | CATEGORY: {category} | PUB: {pub_date}

EDITORIAL THREAD INSTRUCTION: Before writing, identify the central argument from this producers_verdict: "{producers_verdict}". Write every section in service of that argument. The entry should build toward the verdict, not just describe the term.

EMOTIONAL HOOK (FIX 28): The FIRST SENTENCE of the Definition section must be this exact text verbatim: {emotional_hook}

VERDICT-CLOSE INSTRUCTION: The verdict-close paragraph must echo the opening emotional hook -- use the same image or language, but resolved and transformed. Full circle.

PASS 1 DATA:
{p1_json_str[:8000]}

{quotes_context}

{track_list_str}

Output these sections with class="entry-section" and exact IDs.
Leave these exact strings as placeholders (build_html_t1 replaces them):
  THE_NUMBER_PLACEHOLDER
  SIGNAL_CHAIN_PLACEHOLDER
  GENRE_PLACEHOLDER
  PLUGIN_PLACEHOLDER
  DAW_PLACEHOLDER
  COMPARISON_PLACEHOLDER
  TRACK_PLACEHOLDER
  FAQ_PLACEHOLDER
  FLAGS_PLACEHOLDER
  BEFORE_AFTER_PLACEHOLDER
  QUICKREF_SHARE_PLACEHOLDER
  TOOLS_PLACEHOLDER
  SESSION_BREAKDOWN_PLACEHOLDER

SECTIONS REQUIRED (entry-section class + exact IDs):
<section class="entry-section" id="definition"> -- 4-6 paragraphs, FIRST SENTENCE must be the emotional_hook verbatim in <em class="entry-hook">, 1 producer quote from quotes_context as <div class="producer-quote-block"><blockquote class="producer-quote"><p>"quote"</p></blockquote><cite>-- Name</cite></div>, end with <p class="section-summary">
<section class="entry-section" id="how-it-works"> -- 3-4 paragraphs, technical mechanism, end with section-summary
<section class="entry-section" id="parameters"> -- intro + <div class="parameters-grid"> with .param-item cards (4-6 params), 2 more paragraphs, section-summary
<section class="entry-section" id="quick-reference"> -- THE_NUMBER_PLACEHOLDER + brief intro + <div class="qr-table-wrap"><table class="quick-ref-table"> (6-8 rows: Source/Ratio/Attack/Release/Threshold/Notes) + QUICKREF_SHARE_PLACEHOLDER
</section>
TOOLS_PLACEHOLDER
<section class="entry-section" id="signal-chain"> -- SIGNAL_CHAIN_PLACEHOLDER + 1 paragraph + interaction-warnings block (<div class="interaction-warnings"><h4>Interaction Warnings</h4><ul><li class="interaction-warning">...</li></ul></div>)
<section class="entry-section" id="diagram"> -- inline SVG diagram + 2 paragraphs
<section class="entry-section" id="history"> -- 4 <div class="history-card"> sub-sections + 2nd producer quote (from quotes_context) + section-summary
<section class="entry-section" id="how-to-use"> -- 2 paragraphs + DAW_PLACEHOLDER + SESSION_BREAKDOWN_PLACEHOLDER + 1 paragraph + 3rd producer quote (from quotes_context) + section-summary
<section class="entry-section" id="in-the-wild"> -- 1 paragraph + TRACK_PLACEHOLDER + 1 paragraph
<section class="entry-section" id="signatures"> -- 1 paragraph introducing 4-5 <div class="sig-card"> cards each with <div class="sig-track">, <div class="sig-settings">, <div class="sig-why">
<section class="entry-section" id="types"> -- COMPARISON_PLACEHOLDER + 1 paragraph + <div class="types-grid"> (.type-card with .type-name + .type-hardware + .type-desc, 4-6 types) + section-summary
<section class="entry-section" id="verdict">
  <h2 class="sr-only">The Producer's Verdict</h2>
  <div class="producers-verdict">
    <div class="verdict-header"><span class="verdict-diamond">&#9670;</span><span class="verdict-label">The Producer's Verdict</span><span class="verdict-diamond">&#9670;</span></div>
    <p class="verdict-lead">3-4 sentences: biggest mistake producers make, why it's common, correct mental model. Real MPW opinion -- NOT a summary.</p>
    <div class="verdict-grid"> with 6 <div class="verdict-rule"> cells each with <span class="vr-label">, <span class="vr-value">, <span class="vr-note"> (2-3 sentences on sonic consequence of going higher vs lower)
    <div class="mpw-share-bar" style="justify-content:center">Copy Verdict + Share on X + Reddit</div>
    <p class="verdict-close">1 sentence echoing the opening emotional hook -- same image or language, resolved.</p>
  </div>
</section>
<section class="entry-section" id="mistakes"> -- 1 paragraph + <div class="mistakes-list"> (.mistake-item with .mistake-title + <p>, 4-6 items) + section-summary
<section class="entry-section" id="hardware-plugin"> -- 1 paragraph + <div class="hardware-plugin-wrap"><table class="hardware-plugin-table"> (Aspect/Hardware/Plugin, 5-6 rows) + PLUGIN_PLACEHOLDER + 1 paragraph
<section class="entry-section" id="genre-table"> -- 1 paragraph + GENRE_PLACEHOLDER + 1 paragraph
<section class="entry-section" id="before-after"> -- BEFORE_AFTER_PLACEHOLDER + 1 paragraph
<section class="entry-section" id="plugin-recs"> -- <h2>Recommended Plugins</h2> + 1 paragraph intro + (plugin cards will be injected via PLUGIN_RECS_PLACEHOLDER -- leave PLUGIN_RECS_PLACEHOLDER on its own line here)
<section class="entry-section" id="faq"> -- <h2>Frequently Asked Questions</h2> + FAQ_PLACEHOLDER (on its own line, nothing else)
<section class="entry-section" id="flags"> -- FLAGS_PLACEHOLDER + 1 paragraph
<section class="entry-section" id="progression"> -- 1 paragraph + <div class="progression-path"> (3 .prog-stage divs: .prog-beginner/.prog-intermediate/.prog-advanced each with .prog-label + <p>) + section-summary

Rules:
-- ONLY use quotes from the quotes_context above. NEVER fabricate quotes. Use exactly 3 quotes.
-- ONLY reference the LOCKED TRACK LIST. NEVER substitute tracks.
-- Leave all PLACEHOLDERS exactly as written on their own line.
-- TOOLS_PLACEHOLDER must appear on its own line AFTER the closing </section> of quick-reference, NEVER inside another section.
-- No </body></html>.
-- Internal links: /bible/slug only, only CONFIRMED slugs.
-- 6,700-7,300 prose words. Updated {pub_date} must appear in content.
"""

PASS2_SYSTEM_T2 = (
    "You are writing a Tier 2 Producer's Bible entry for MusicProductionWiki.com.\n"
    "Return ONLY raw HTML sections \u2014 no markdown, no fences, no explanations.\n"
    "Target: 3,000\u20133,800 words of prose. Direct, authoritative, producer-language.\n"
    "entry-section class on every section. Leave PLACEHOLDERS as written."
)

def build_pass2_prompt_t2(slug, term, category, p1_json_str, quotes_context, pub_date):
    return f"""Write HTML prose for this Tier 2 Bible entry.

TERM: {term} | SLUG: {slug} | CATEGORY: {category} | PUB: {pub_date}

PASS 1 DATA:
{p1_json_str[:6000]}

{quotes_context}

Leave these placeholders exactly: THE_NUMBER_PLACEHOLDER, SIGNAL_CHAIN_PLACEHOLDER, GENRE_PLACEHOLDER, PLUGIN_PLACEHOLDER, DAW_PLACEHOLDER, FAQ_PLACEHOLDER, FLAGS_PLACEHOLDER, QUICKREF_SHARE_PLACEHOLDER

SECTIONS (entry-section class + exact IDs):
id="definition" \u2014 3 paragraphs + emotional_hook + 1 producer quote
id="how-it-works" \u2014 2-3 paragraphs
id="parameters" \u2014 parameters-grid + 2 paragraphs
id="quick-reference" \u2014 THE_NUMBER_PLACEHOLDER + qr-table-wrap + QUICKREF_SHARE_PLACEHOLDER
id="signal-chain" \u2014 SIGNAL_CHAIN_PLACEHOLDER + 1 paragraph
id="how-to-use" \u2014 2 paragraphs + DAW_PLACEHOLDER
id="genre-table" \u2014 GENRE_PLACEHOLDER
id="hardware-plugin" \u2014 hardware-plugin-wrap table + PLUGIN_PLACEHOLDER
id="types" \u2014 types-grid (3-4 cards) + producers-verdict
id="mistakes" \u2014 mistakes-list (3-4 items)
id="flags" \u2014 FLAGS_PLACEHOLDER
id="faq" \u2014 FAQ_PLACEHOLDER

Target: 3,000\u20133,800 prose words. Updated {pub_date} in content. No </body></html>.
"""

PASS2_SYSTEM_T3 = (
    "You are writing a Tier 3 Producer's Bible reference entry for MusicProductionWiki.com.\n"
    "Return ONLY raw HTML sections \u2014 no markdown, no fences.\n"
    "Target: 1,200\u20131,800 words. Concise, authoritative. entry-section class on every section."
)

def build_pass2_prompt_t3(slug, term, category, p1_json_str, pub_date):
    return f"""Write HTML prose for this Tier 3 reference entry.

TERM: {term} | SLUG: {slug} | CATEGORY: {category} | PUB: {pub_date}

PASS 1 DATA:
{p1_json_str[:4000]}

Leave placeholders: FAQ_PLACEHOLDER, RELATED_PLACEHOLDER

SECTIONS (entry-section class + exact IDs):
id="definition" \u2014 2 paragraphs + emotional_hook
id="how-it-works" \u2014 2 paragraphs
id="parameters" \u2014 parameters-grid
id="quick-reference" \u2014 qr-table-wrap
id="faq" \u2014 FAQ_PLACEHOLDER (3 questions)
id="related" \u2014 RELATED_PLACEHOLDER

Target: 1,200\u20131,800 prose words. No </body></html>.
"""


# ══════════════════════════════════════════════════════════════════════════════
# TOOLS SECTION
# ══════════════════════════════════════════════════════════════════════════════


# Safe script closing tag — never write the closing tag as single literal in Python strings
SC = '</' + 'script>'

TOOL_OVERRIDES = {
    'compression':           'gr_calculator',
    'saturation':            'gr_calculator',
    'distortion':            'gr_calculator',
    'parallel-compression':  'gr_calculator',
    'multiband-compression': 'gr_calculator',
    'noise-gate':            'gr_calculator',
    'bus-compression':       'gr_calculator',
    'delay':                 'delay_calculator',
    'plate-reverb':          'delay_calculator',
    'automation':            'delay_calculator',
    'limiting':              'lufs_calculator',
    'lufs':                  'lufs_calculator',
    'mastering':             'lufs_calculator',
    'loudness-normalization':'lufs_calculator',
    'true-peak-limiting':    'lufs_calculator',
    'eq':                    'frequency_reference',
    'parametric-eq':         'frequency_reference',
    'high-pass-filter':      'frequency_reference',
    'low-pass-filter':       'frequency_reference',
    'shelving-eq':           'frequency_reference',
    'air-frequency-eq':      'frequency_reference',
    'resonance':             'frequency_reference',
    'harmonic-distortion':   'frequency_reference',
    'reverb':                'rt60_calculator',
    'convolution-reverb':    'rt60_calculator',
    'room-reverb':           'rt60_calculator',
    'oscillator':            'note_freq',
    'fm-synthesis':          'note_freq',
    'wavetable-synthesis':   'note_freq',
    'additive-synthesis':    'note_freq',
    'vocoder':               'note_freq',
    'subtractive-synthesis': 'note_freq',
    'adsr':                  'adsr_visualizer',
    'envelope':              'adsr_visualizer',
    'gain-staging':          'gain_staging',
    'send-return':           'gain_staging',
    'clip-gain':             'gain_staging',
    'headroom':              'headroom_calc',
    'mix-bus':               'headroom_calc',
    'stereo-imaging':        'stereo_width',
    'mid-side-processing':   'stereo_width',
    'lfo':                   'lfo_sync',
    'chorus':                'lfo_sync',
    'flanger':               'lfo_sync',
    'phaser':                'lfo_sync',
    'tremolo':               'lfo_sync',
    'vibrato':               'lfo_sync',
}



def _share(slug, term):
    enc = term.replace(' ', '+')
    url = 'https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F' + slug + '%23tools'
    xh = 'https://x.com/intent/tweet?text=' + enc + '+Tool+%E2%80%94+%40mpwikiofficial&url=' + url
    rh = 'https://reddit.com/submit?url=' + url + '&title=' + enc + '+Tool+%E2%80%94+MusicProductionWiki'
    return (
        '<div class="mpw-share-bar calc-share-bar" style="margin-top:20px">'
        '<span class="mpw-share-label">Share this tool</span>'
        '<button class="mpw-share-btn share-copy" onclick="navigator.clipboard&&navigator.clipboard.writeText(\'musicproductionwiki.com/bible/' + slug + '#tools\')">Copy Link</button>'
        '<a href="' + xh + '" target="_blank" rel="noopener" class="mpw-share-btn share-x">'
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.26 5.632 5.905-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>Share on X</a>'
        '<a href="' + rh + '" target="_blank" rel="noopener" class="mpw-share-btn share-reddit">'
        '<svg width="12" height="12" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="10"/>'
        '<path fill="#ff4500" d="M16.67 10a1.46 1.46 0 00-2.47-1 7.12 7.12 0 00-3.85-1.23l.65-3.08 2.13.45a1 1 0 101.07-1 1 1 0 00-.96.68l-2.38-.5a.27.27 0 00-.32.2l-.73 3.44a7.14 7.14 0 00-3.89 1.23 1.46 1.46 0 10-1.61 2.39 2.87 2.87 0 000 .44c0 2.24 2.61 4.06 5.83 4.06s5.83-1.82 5.83-4.06a2.87 2.87 0 000-.44 1.46 1.46 0 00.61-1.08zM7.5 11a1 1 0 111 1 1 1 0 01-1-1zm5.67 2.65a3.54 3.54 0 01-2.34.63 3.54 3.54 0 01-2.34-.63.25.25 0 01.35-.35 3.07 3.07 0 002 .48 3.07 3.07 0 002-.48.25.25 0 01.35.35zm-.17-1.65a1 1 0 111-1 1 1 0 01-1 1z"/></svg>Reddit</a>'
        '</div>'
    )


def _wrap(slug, headline, desc, tool_html, share_html):
    return (
        '      <section class="entry-section" id="tools">\n'
        '        <h2>Tools for This Entry</h2>\n'
        '        <div style="background:#0d1a0d;border:2px solid rgba(96,192,96,.25);border-radius:12px;padding:20px;margin-bottom:16px">\n'
        '          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:8px">\n'
        '            <h3 style="font-size:15px;font-weight:700;color:#60c060;margin:0">&#9889; ' + headline + '</h3>\n'
        '            <span style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#60c060;background:rgba(96,192,96,.12);border:1px solid rgba(96,192,96,.3);padding:3px 8px;border-radius:12px">Interactive Tool</span>\n'
        '          </div>\n'
        '          <p style="font-size:13px;color:#888;margin-bottom:14px">' + desc + '</p>\n'
        '          ' + tool_html + '\n'
        '          ' + share_html + '\n'
        '        </div>\n'
        '      </section>\n'
    )


def _gr(slug, term):
    js = ('(function(){function calcGR(){var inp=parseFloat(document.getElementById("gc-input").value)||0;var thr=parseFloat(document.getElementById("gc-thresh").value)||-20;var rat=Math.max(1,parseFloat(document.getElementById("gc-ratio").value)||4);var mkp=parseFloat(document.getElementById("gc-makeup").value)||0;var gr=0,out=inp,excess=0;if(inp>thr){excess=inp-thr;gr=excess*(1-1/rat);out=inp-gr;}document.getElementById("gc-gr").textContent=gr.toFixed(1)+" dB";document.getElementById("gc-excess").textContent=(excess>=0?"+":"")+excess.toFixed(1)+" dB";document.getElementById("gc-out").textContent=out.toFixed(1)+" dBFS";document.getElementById("gc-final").textContent=(out+mkp).toFixed(1)+" dBFS";}["gc-input","gc-thresh","gc-ratio","gc-makeup"].forEach(function(id){var el=document.getElementById(id);if(el)el.addEventListener("input",calcGR);});calcGR();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Input Level (dBFS)<input id="gc-input" type="number" value="-10" step="0.5" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Threshold (dBFS)<input id="gc-thresh" type="number" value="-20" step="0.5" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Ratio (e.g. 4 for 4:1)<input id="gc-ratio" type="number" value="4" step="0.5" min="1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Makeup Gain (dB)<input id="gc-makeup" type="number" value="0" step="0.5" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center"><span id="gc-gr" style="display:block;font-size:2.2rem;font-weight:900;color:#f5a623;line-height:1">0 dB</span><span style="font-size:12px;color:#888">gain reduction applied</span><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:12px"><div style="background:#13132a;padding:8px;border-radius:5px"><span id="gc-excess" style="display:block;font-size:13px;font-weight:700;color:#e0e0f0">0 dB</span><span style="font-size:10px;color:#666">above threshold</span></div><div style="background:#13132a;padding:8px;border-radius:5px"><span id="gc-out" style="display:block;font-size:13px;font-weight:700;color:#e0e0f0">-10 dBFS</span><span style="font-size:10px;color:#666">output level</span></div><div style="background:#13132a;padding:8px;border-radius:5px"><span id="gc-final" style="display:block;font-size:13px;font-weight:700;color:#e0e0f0">-10 dBFS</span><span style="font-size:10px;color:#666">after makeup</span></div></div></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Gain Reduction Calculator', 'Enter your compressor settings to see exactly how much gain reduction is applied, output level, and final level after makeup gain.', html, _share(slug, term))


def _delay(slug, term):
    js = (
        '(function(){'
        'var NOTES=['
        '{n:"Whole",     b:1,  dot:false,trip:false},'
        '{n:"Half",      b:2,  dot:false,trip:false},'
        '{n:"Dotted Half",b:2, dot:true, trip:false},'
        '{n:"Quarter",   b:4,  dot:false,trip:false},'
        '{n:"Dotted Quarter",b:4,dot:true,trip:false},'
        '{n:"Quarter Triplet",b:4,dot:false,trip:true},'
        '{n:"8th",       b:8,  dot:false,trip:false},'
        '{n:"Dotted 8th",b:8, dot:true, trip:false},'
        '{n:"8th Triplet",b:8,dot:false,trip:true},'
        '{n:"16th",      b:16, dot:false,trip:false},'
        '{n:"Dotted 16th",b:16,dot:true,trip:false},'
        '{n:"16th Triplet",b:16,dot:false,trip:true},'
        '{n:"32nd",      b:32, dot:false,trip:false}'
        '];'
        'function ms(bpm,b,dot,trip){'
        'var base=(60000/bpm)*(4/b);'
        'if(dot)base*=1.5;'
        'if(trip)base*=(2/3);'
        'return base;}'
        'function render(){'
        'var bpm=parseFloat(document.getElementById("dt-bpm").value);'
        'if(!bpm||bpm<20||bpm>300)return;'
        'var grid=document.getElementById("dt-grid");'
        'grid.innerHTML="";'
        'NOTES.forEach(function(note){'
        'var t=ms(bpm,note.b,note.dot,note.trip);'
        'var hz=(1000/t).toFixed(3);'
        'var col=note.dot?"#60a0ff":note.trip?"#a060ff":"#f5a623";'
        'var card=document.createElement("div");'
        'card.style.cssText="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:8px;padding:12px 8px;text-align:center;";'
        'card.innerHTML='
        '"<div style=\"font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:"+col+";margin-bottom:6px;line-height:1.3\">"+note.n+"</div>"'
        '+"<div style=\"font-size:20px;font-weight:900;color:#fff;line-height:1\">"+t.toFixed(1)+"</div>"'
        '+"<div style=\"font-size:10px;color:#666;margin-top:3px\">ms</div>"'
        '+"<div style=\"font-size:9px;color:#555;margin-top:4px\">"+hz+" Hz</div>";'
        'grid.appendChild(card);});}'
        'var inp=document.getElementById("dt-bpm");'
        'inp.addEventListener("input",render);'
        'inp.addEventListener("keyup",render);'
        'render();'
        '})()'
    )
    html = (
        '<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px">'
        '<div style="display:flex;align-items:center;gap:16px;margin-bottom:16px;flex-wrap:wrap">'
        '<label style="font-size:13px;color:#c8c8d8;display:flex;align-items:center;gap:10px">'
        'BPM'
        '<input id="dt-bpm" type="number" value="120" min="20" max="300" step="1" '
        'style="width:80px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;'
        'border-radius:5px;color:#fff;font-size:18px;font-weight:700;text-align:center">'
        '</label>'
        '<div style="font-size:11px;color:#555;line-height:1.5">'
        '<span style="color:#f5a623;font-weight:700">&#9646;</span> Straight &nbsp;'
        '<span style="color:#60a0ff;font-weight:700">&#9646;</span> Dotted &nbsp;'
        '<span style="color:#a060ff;font-weight:700">&#9646;</span> Triplet'
        '</div>'
        '</div>'
        '<div id="dt-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">'
        '</div>'
        '<script>' + js + SC +
        '</div>'
    )
    return _wrap(slug, 'Delay Time Calculator', 'Type your BPM — all 13 note values update instantly. Straight, dotted, and triplet values shown simultaneously.', html, _share(slug, term))



def _lufs(slug, term):
    js = ('(function(){function calc(){var cur=parseFloat(document.getElementById("lc-cur").value)||0;var tgt=parseFloat(document.getElementById("lc-plat").value)||-14;var diff=tgt-cur;var el=document.getElementById("lc-diff");var adv=document.getElementById("lc-adv");document.getElementById("lc-your").textContent=cur.toFixed(1)+" LUFS";document.getElementById("lc-tgt").textContent=tgt.toFixed(1)+" LUFS";if(Math.abs(diff)<0.5){el.textContent="On Target";el.style.color="#60ff60";adv.textContent="Within 0.5 LUFS. No adjustment needed.";}else if(diff>0){el.textContent="+"+diff.toFixed(1)+" dB";el.style.color="#f5a623";adv.textContent="Too quiet by "+Math.abs(diff).toFixed(1)+"dB. Raise limiter output.";}else{el.textContent=diff.toFixed(1)+" dB";el.style.color="#ff6666";adv.textContent="Too loud by "+Math.abs(diff).toFixed(1)+"dB. Platform will turn it down on playback.";}}document.getElementById("lc-cur").addEventListener("input",calc);document.getElementById("lc-plat").addEventListener("change",calc);calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Your Integrated LUFS<input id="lc-cur" type="number" value="-8" step="0.1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Target Platform<select id="lc-plat" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option value="-14">Spotify (-14 LUFS)</option><option value="-16">Apple Music (-16 LUFS)</option><option value="-14">YouTube (-14 LUFS)</option><option value="-16">Amazon Music (-16 LUFS)</option><option value="-13">Tidal (-13 LUFS)</option><option value="-23">Broadcast EBU R128 (-23 LUFS)</option></select></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center;margin-bottom:12px"><span id="lc-diff" style="display:block;font-size:2.2rem;font-weight:900;color:#f5a623;line-height:1">-</span><span id="lc-adv" style="font-size:13px;color:#c8c8d8;display:block;margin-top:6px">-</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Your LUFS</span><span id="lc-your" style="font-size:14px;font-weight:700;color:#e0e0f0">-</span></div><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Target LUFS</span><span id="lc-tgt" style="font-size:14px;font-weight:700;color:#e0e0f0">-</span></div></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'LUFS Target Calculator', 'Enter your current integrated loudness and target platform to see how far off you are and what to do.', html, _share(slug, term))


def _freq(slug, term):
    js = ('(function(){var B=[{r:"20-60Hz",n:"Sub Bass",c:"#6030a0",i:"Kick sub, 808 tail, bass synth sub",e:"Boost for physical weight; HPF everything else here",p:"Inaudible on laptops; builds up fast"},{r:"60-120Hz",n:"Bass",c:"#4040c0",i:"Kick punch, bass guitar fundamental, synth body",e:"Boost kick at 80Hz; cut bass at 100Hz if clashing with kick",p:"Competing kick and bass — sidechain or EQ carve"},{r:"120-250Hz",n:"Upper Bass",c:"#2060b0",i:"Bass harmonics, piano low end, guitar body, male vocal chest",e:"Cut 200Hz on guitars for boxiness; boost 150Hz on bass for warmth",p:"Mud zone — HPF instruments that dont need this"},{r:"250-500Hz",n:"Low Mid",c:"#208080",i:"Guitar body, piano warmth, snare body, vocal chest",e:"Narrow cut at 300-400Hz reduces mud on almost anything",p:"Most common source of mix congestion"},{r:"500Hz-1kHz",n:"Midrange",c:"#208040",i:"Vocal body, guitar presence, piano mid, snare crack",e:"Boost 800Hz on bass for definition on small speakers",p:"Harshness begins at top of this range"},{r:"1-3kHz",n:"Upper Mid",c:"#607020",i:"Vocal presence, guitar cut, snare crack, piano attack",e:"Boost 2-3kHz on vocals for presence; cut on guitars",p:"Ear fatigue lives here — most sensitive range"},{r:"3-6kHz",n:"Presence",c:"#804010",i:"Vocal intelligibility, guitar string noise, cymbal body",e:"Boost 3-4kHz for vocal cut-through; de-essing at 6-9kHz",p:"Too much = pain; too little = buried distant mix"},{r:"6-12kHz",n:"Brilliance",c:"#904020",i:"Cymbal shimmer, vocal breath, guitar pick attack",e:"High shelf adds brightness; narrow cut at 8-9kHz tames harshness",p:"Sibilance lives at 6-9kHz"},{r:"12-20kHz",n:"Air",c:"#a05010",i:"Room air, cymbal air, vocal shimmer",e:"High shelf above 12kHz adds air",p:"Distortion and aliasing artifacts appear here"}];var cont=document.getElementById("freq-bands");B.forEach(function(b){var row=document.createElement("div");row.style.cssText="cursor:pointer;border-radius:6px;padding:10px 14px;display:flex;align-items:center;gap:12px;border:1px solid #2a2a4a;background:#13132a;margin-bottom:4px";row.innerHTML=\'<div style="width:12px;height:12px;border-radius:50%;background:\'+b.c+\';flex-shrink:0"></div><span style="font-size:11px;color:#888;min-width:80px">\'+b.r+\'</span><span style="font-size:13px;font-weight:700;color:#e0e0f0">\'+b.n+\'</span>\';row.addEventListener("click",function(){document.querySelectorAll("#freq-bands>div").forEach(function(r){r.style.background="#13132a";r.style.borderColor="#2a2a4a";});row.style.background="#1a0800";row.style.borderColor="#f5a623";var d=document.getElementById("freq-detail");d.style.display="block";document.getElementById("freq-dc").innerHTML=\'<div style="font-size:11px;font-weight:700;text-transform:uppercase;color:#f5a623;margin-bottom:10px">\'+b.r+" - "+b.n+\'</div><div style="margin-bottom:8px"><span style="font-size:10px;color:#666;text-transform:uppercase;display:block;margin-bottom:3px">What lives here</span><span style="font-size:13px;color:#c8c8d8">\'+b.i+\'</span></div><div style="margin-bottom:8px"><span style="font-size:10px;color:#666;text-transform:uppercase;display:block;margin-bottom:3px">Common EQ moves</span><span style="font-size:13px;color:#c8c8d8">\'+b.e+\'</span></div><div><span style="font-size:10px;color:#666;text-transform:uppercase;display:block;margin-bottom:3px">Watch for</span><span style="font-size:13px;color:#ff9999">\'+b.p+\'</span></div>\';});cont.appendChild(row);});})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><p style="font-size:12px;color:#888;margin-bottom:14px">Click any band to see what lives there, EQ moves, and problems.</p><div id="freq-bands"></div><div id="freq-detail" style="display:none;background:#0d0d1a;border:1px solid #f5a623;border-radius:8px;padding:16px;margin-top:16px"><div id="freq-dc"></div></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Frequency Band Reference', 'Click any frequency band to see what instruments live there, the most effective EQ moves, and common problems to watch for.', html, _share(slug, term))


def _rt60(slug, term):
    js = ('(function(){var CTX=[{max:0.3,l:"Vocal booth / dead room",n:"Ideal for close-mic vocals, voiceover, podcast."},{max:0.5,l:"Professional mix room",n:"Ideal for mixing. Accurate monitoring."},{max:0.8,l:"Live room / small studio",n:"Natural room character. Good for live instruments."},{max:1.5,l:"Small concert hall",n:"Significant reverb. Works for orchestral instruments."},{max:99,l:"Large hall / cathedral",n:"Very long decay. Classical and large ensemble only."}];function calc(){var V=parseFloat(document.getElementById("rt-vol").value)||50;var a=parseFloat(document.getElementById("rt-mat").value)||0.15;var S=Math.pow(V,2/3)*6;var rt=(0.161*V)/(a*S);document.getElementById("rt-result").textContent=rt.toFixed(2)+"s";var ctx=CTX.find(function(c){return rt<=c.max;})||CTX[CTX.length-1];document.getElementById("rt-ctx").innerHTML="<strong style=\"color:#f5a623\">"+ctx.l+"</strong><br>"+ctx.n;}document.getElementById("rt-vol").addEventListener("input",calc);document.getElementById("rt-mat").addEventListener("change",calc);calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Room Volume (cubic metres)<input id="rt-vol" type="number" value="50" min="1" step="1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Surface Material<select id="rt-mat" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option value="0.02">Concrete / Tile</option><option value="0.05">Plaster / Brick</option><option value="0.1">Wood panels</option><option value="0.15" selected>Mixed furnishings (studio)</option><option value="0.25">Carpet + soft furnishings</option><option value="0.4">Acoustic panels (treated)</option><option value="0.6">Heavy absorption (vocal booth)</option></select></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center;margin-bottom:12px"><span id="rt-result" style="display:block;font-size:2.5rem;font-weight:900;color:#f5a623;line-height:1">-</span><span style="font-size:12px;color:#888">RT60 — time for sound to decay 60dB</span></div><div id="rt-ctx" style="font-size:13px;color:#c8c8d8;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;padding:12px"></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'RT60 Reverb Time Calculator', 'Calculate the natural reverb decay time of any room using the Sabine formula. Enter room volume and surface material to get the RT60.', html, _share(slug, term))


def _note(slug, term):
    js = ('(function(){var N=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];function calc(){var ni=document.getElementById("nf-note").selectedIndex;var oct=parseInt(document.getElementById("nf-oct").value)||4;var a4=parseFloat(document.getElementById("nf-a4").value)||440;var midi=ni+(oct+1)*12;var freq=a4*Math.pow(2,(midi-69)/12);document.getElementById("nf-freq").textContent=freq.toFixed(2)+" Hz";document.getElementById("nf-lbl").textContent=N[ni]+oct;document.getElementById("nf-midi").textContent=midi;document.getElementById("nf-lo").textContent=(freq/2).toFixed(2)+" Hz";document.getElementById("nf-hi").textContent=(freq*2).toFixed(2)+" Hz";}["nf-note","nf-oct","nf-a4"].forEach(function(id){var el=document.getElementById(id);el.addEventListener("change",calc);el.addEventListener("input",calc);});calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Note<select id="nf-note" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option>C</option><option>C#</option><option>D</option><option>D#</option><option>E</option><option>F</option><option>F#</option><option>G</option><option>G#</option><option selected>A</option><option>A#</option><option>B</option></select></label><label style="font-size:12px;color:#c8c8d8;display:block">Octave<select id="nf-oct" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option>0</option><option>1</option><option>2</option><option>3</option><option selected>4</option><option>5</option><option>6</option><option>7</option></select></label><label style="font-size:12px;color:#c8c8d8;display:block">A4 Tuning (Hz)<input id="nf-a4" type="number" value="440" min="400" max="480" step="1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center;margin-bottom:12px"><span id="nf-freq" style="display:block;font-size:2.5rem;font-weight:900;color:#f5a623;line-height:1">440.00 Hz</span><span id="nf-lbl" style="font-size:14px;color:#c8c8d8;display:block;margin-top:4px">A4</span></div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px"><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Octave below</span><span id="nf-lo" style="font-size:13px;font-weight:700;color:#888">220.00 Hz</span></div><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">MIDI note</span><span id="nf-midi" style="font-size:13px;font-weight:700;color:#e0e0f0">69</span></div><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Octave above</span><span id="nf-hi" style="font-size:13px;font-weight:700;color:#888">880.00 Hz</span></div></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Note to Frequency Calculator', 'Convert any musical note to its exact frequency in Hz. Adjust the A4 tuning reference for alternate tuning standards.', html, _share(slug, term))


def _adsr(slug, term):
    js = ('(function(){var cv=document.getElementById("adsr-c");var cx=cv.getContext("2d");function draw(){var A=parseInt(document.getElementById("adsr-a").value);var D=parseInt(document.getElementById("adsr-d").value);var S=parseInt(document.getElementById("adsr-s").value)/100;var R=parseInt(document.getElementById("adsr-r").value);document.getElementById("adsr-av").textContent=A+"ms";document.getElementById("adsr-dv").textContent=D+"ms";document.getElementById("adsr-sv").textContent=Math.round(S*100)+"%";document.getElementById("adsr-rv").textContent=R+"ms";var W=cv.width,H=cv.height,pad=20,gH=H-pad*2;var total=A+D+200+R;var aX=pad+A/total*(W-pad*2);var dX=aX+D/total*(W-pad*2);var sX=dX+200/total*(W-pad*2);var rX=W-pad;cx.clearRect(0,0,W,H);cx.fillStyle="#0d0d1a";cx.fillRect(0,0,W,H);cx.strokeStyle="#f5a623";cx.lineWidth=2.5;cx.lineJoin="round";cx.beginPath();cx.moveTo(pad,H-pad);cx.lineTo(aX,pad);cx.lineTo(dX,pad+gH*(1-S));cx.lineTo(sX,pad+gH*(1-S));cx.lineTo(rX,H-pad);cx.stroke();cx.fillStyle="rgba(245,166,35,0.08)";cx.beginPath();cx.moveTo(pad,H-pad);cx.lineTo(aX,pad);cx.lineTo(dX,pad+gH*(1-S));cx.lineTo(sX,pad+gH*(1-S));cx.lineTo(rX,H-pad);cx.closePath();cx.fill();cx.fillStyle="#f5a623";cx.font="10px system-ui";cx.textAlign="center";cx.fillText("A",pad+(aX-pad)/2,H-6);cx.fillText("D",aX+(dX-aX)/2,H-6);cx.fillText("S",dX+(sX-dX)/2,H-6);cx.fillText("R",sX+(rX-sX)/2,H-6);}["adsr-a","adsr-d","adsr-s","adsr-r"].forEach(function(id){document.getElementById(id).addEventListener("input",draw);});draw();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><canvas id="adsr-c" width="560" height="160" style="width:100%;height:160px;display:block;border-radius:6px;margin-bottom:16px"></canvas><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><label style="font-size:12px;color:#c8c8d8;display:block">Attack <span id="adsr-av" style="color:#f5a623">10ms</span><input id="adsr-a" type="range" min="1" max="2000" value="10" step="1" style="display:block;width:100%;margin-top:4px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Decay <span id="adsr-dv" style="color:#f5a623">100ms</span><input id="adsr-d" type="range" min="1" max="2000" value="100" step="1" style="display:block;width:100%;margin-top:4px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Sustain <span id="adsr-sv" style="color:#f5a623">70%</span><input id="adsr-s" type="range" min="0" max="100" value="70" step="1" style="display:block;width:100%;margin-top:4px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Release <span id="adsr-rv" style="color:#f5a623">300ms</span><input id="adsr-r" type="range" min="1" max="5000" value="300" step="1" style="display:block;width:100%;margin-top:4px"></label></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'ADSR Envelope Visualizer', 'Drag the sliders to see the envelope shape update in real time.', html, _share(slug, term))


def _gs(slug, term):
    js = ('(function(){var stages=[{n:"Input",g:0},{n:"Preamp",g:12},{n:"Compressor",g:-3},{n:"Output",g:-6}];function render(){var c=document.getElementById("gs-s");c.innerHTML="";stages.forEach(function(s,i){var row=document.createElement("div");row.style.cssText="display:flex;align-items:center;gap:8px;margin-bottom:8px";row.innerHTML=\'<input value="\'+s.n+\'" data-i="\'+i+\'" data-f="n" style="flex:1;padding:6px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:12px"><input type="number" value="\'+s.g+\'" data-i="\'+i+\'" data-f="g" step="0.5" style="width:70px;padding:6px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:12px"><span style="font-size:11px;color:#888">dB</span>\';if(stages.length>1)row.innerHTML+=\'<button data-del="\'+i+\'" style="background:none;border:none;color:#666;cursor:pointer;font-size:14px">x</button>\';c.appendChild(row);});c.querySelectorAll("input").forEach(function(el){el.addEventListener("input",function(){var idx=parseInt(this.dataset.i);if(this.dataset.f==="g")stages[idx].g=parseFloat(this.value)||0;else stages[idx].n=this.value;tot();});});c.querySelectorAll("[data-del]").forEach(function(b){b.addEventListener("click",function(){stages.splice(parseInt(this.dataset.del),1);render();tot();});});}function tot(){var t=stages.reduce(function(s,x){return s+x.g;},0);var f=-18+t;document.getElementById("gs-t").textContent=f.toFixed(1)+" dBFS";var st="";if(f>-6)st="Too hot";else if(f>-12)st="Good — target zone -12 to -6 dBFS";else if(f>-24)st="Acceptable";else st="Too quiet";document.getElementById("gs-st").textContent=st;}document.getElementById("gs-add").addEventListener("click",function(){if(stages.length<8){stages.push({n:"Stage "+(stages.length+1),g:0});render();tot();}});render();tot();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><p style="font-size:12px;color:#888;margin-bottom:12px">Add up to 8 stages. Starting reference: -18 dBFS.</p><div id="gs-s"></div><button id="gs-add" style="margin-top:8px;font-size:12px;font-weight:600;color:#f5a623;background:rgba(245,166,35,.08);border:1px solid rgba(245,166,35,.3);border-radius:5px;padding:6px 14px;cursor:pointer;font-family:inherit">+ Add Stage</button><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center;margin-top:16px"><span style="font-size:11px;color:#888;display:block;margin-bottom:4px">Final output level</span><span id="gs-t" style="font-size:2.2rem;font-weight:900;color:#f5a623">-</span><span id="gs-st" style="font-size:12px;display:block;margin-top:6px;color:#c8c8d8"></span></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Gain Staging Calculator', 'Map every gain stage in your signal chain to see your final output level. Target -12 to -6 dBFS for optimal headroom.', html, _share(slug, term))


def _hr(slug, term):
    js = ('(function(){function calc(){var peak=parseFloat(document.getElementById("hr-pk").value)||0;var ceil=parseFloat(document.getElementById("hr-cl").value)||-3;var hr=ceil-peak;var el=document.getElementById("hr-r");var adv=document.getElementById("hr-adv");el.textContent=(hr>=0?"+":"")+hr.toFixed(1)+" dB";if(hr>=6){el.style.color="#60ff60";adv.innerHTML="<strong style=\'color:#60ff60\'>Excellent.</strong> Plenty of room for transients and bus processing.";}else if(hr>=3){el.style.color="#f5a623";adv.innerHTML="<strong style=\'color:#f5a623\'>Adequate.</strong> Monitor peaks carefully.";}else if(hr>=0){el.style.color="#ff9966";adv.innerHTML="<strong style=\'color:#ff9966\'>Tight.</strong> Any makeup gain risks clipping.";}else{el.style.color="#ff4444";adv.innerHTML="<strong style=\'color:#ff4444\'>Over ceiling by "+Math.abs(hr).toFixed(1)+"dB.</strong> Reduce track levels.";}}document.getElementById("hr-pk").addEventListener("input",calc);document.getElementById("hr-cl").addEventListener("change",calc);calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Current Peak (dBFS)<input id="hr-pk" type="number" value="-6" step="0.1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Target Ceiling<select id="hr-cl" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option value="-1">-1 dBFS (mastering)</option><option value="-3" selected>-3 dBFS (mix bus)</option><option value="-6">-6 dBFS (conservative)</option><option value="-12">-12 dBFS (tracking/stem)</option></select></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:16px;text-align:center;margin-bottom:12px"><span id="hr-r" style="display:block;font-size:2.5rem;font-weight:900;color:#f5a623;line-height:1">-</span><span style="font-size:12px;color:#888">available headroom</span></div><div id="hr-adv" style="font-size:13px;color:#c8c8d8;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;padding:12px"></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Headroom Calculator', 'Enter your current peak level and target ceiling to see exactly how much headroom you have.', html, _share(slug, term))


def _sw(slug, term):
    js = ('(function(){var cv=document.getElementById("sw-cv");var cx=cv.getContext("2d");function draw(){var w=parseInt(document.getElementById("sw-w").value);var pan=parseInt(document.getElementById("sw-p").value);document.getElementById("sw-wv").textContent=w+"%";document.getElementById("sw-pv").textContent=pan===0?"Centre":pan>0?"R"+pan:"L"+Math.abs(pan);var W=cv.width,H=cv.height,cxp=W/2,cy=H/2,r=70;cx.clearRect(0,0,W,H);cx.fillStyle="#0d0d1a";cx.fillRect(0,0,W,H);cx.strokeStyle="#2a2a4a";cx.lineWidth=1;cx.beginPath();cx.arc(cxp,cy,r,0,Math.PI*2);cx.stroke();cx.beginPath();cx.moveTo(cxp,cy-r-10);cx.lineTo(cxp,cy+r+10);cx.stroke();cx.beginPath();cx.moveTo(cxp-r-10,cy);cx.lineTo(cxp+r+10,cy);cx.stroke();cx.fillStyle="#555";cx.font="10px system-ui";cx.textAlign="center";cx.fillText("L",cxp-r-18,cy+4);cx.fillText("R",cxp+r+18,cy+4);var hw=Math.min(w/100,2)*r*0.5;var po=(pan/100)*r*0.5;cx.fillStyle="rgba(245,166,35,0.15)";cx.strokeStyle="#f5a623";cx.lineWidth=2;cx.beginPath();cx.ellipse(cxp+po,cy,hw,r*0.85,0,0,Math.PI*2);cx.fill();cx.stroke();var adv="";if(w===0)adv="Mono — maximum compatibility.";else if(w<50)adv="Narrow — subtle width, good mono compat.";else if(w<=100)adv="Natural stereo — full width, good mono compat.";else if(w<=150)adv="Wide — check mono compatibility carefully.";else adv="Very wide — significant phase divergence. Always check mono.";document.getElementById("sw-adv").textContent=adv;}document.getElementById("sw-w").addEventListener("input",draw);document.getElementById("sw-p").addEventListener("input",draw);draw();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><canvas id="sw-cv" width="400" height="200" style="width:100%;max-width:400px;height:200px;display:block;margin:0 auto 16px;border-radius:6px"></canvas><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px"><label style="font-size:12px;color:#c8c8d8;display:block">Stereo Width % <span id="sw-wv" style="color:#f5a623">100%</span><input id="sw-w" type="range" min="0" max="200" value="100" step="1" style="display:block;width:100%;margin-top:4px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Pan <span id="sw-pv" style="color:#f5a623">Centre</span><input id="sw-p" type="range" min="-100" max="100" value="0" step="1" style="display:block;width:100%;margin-top:4px"></label></div><div id="sw-adv" style="font-size:13px;color:#c8c8d8;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:12px;text-align:center"></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Stereo Width Visualizer', 'Visualize how stereo width and pan affect your signal in the stereo field. Check mono compatibility before committing to wide effects.', html, _share(slug, term))


def _lfo(slug, term):
    js = ('(function(){function calc(){var bpm=parseFloat(document.getElementById("lfo-b").value)||120;var div=parseFloat(document.getElementById("lfo-d").value)||2;var ms=(60000/bpm*4)/div;var hz=1000/ms;document.getElementById("lfo-hz").textContent=hz.toFixed(3)+" Hz";document.getElementById("lfo-ms").textContent=ms.toFixed(1)+"ms per cycle";document.getElementById("lfo-dot").textContent=(hz/1.5).toFixed(3)+" Hz";document.getElementById("lfo-tri").textContent=(hz*1.5).toFixed(3)+" Hz";}document.getElementById("lfo-b").addEventListener("input",calc);document.getElementById("lfo-d").addEventListener("change",calc);calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">BPM<input id="lfo-b" type="number" value="120" min="40" max="300" step="1" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"></label><label style="font-size:12px;color:#c8c8d8;display:block">Sync Division<select id="lfo-d" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option value="0.25">4 bars</option><option value="0.5">2 bars</option><option value="1">1 bar</option><option value="2" selected>1/2 note</option><option value="4">1/4 note</option><option value="6">1/4 triplet</option><option value="8">1/8 note</option><option value="12">1/8 triplet</option><option value="16">1/16 note</option><option value="24">1/16 triplet</option></select></label></div><div style="background:#1a0800;border:1px solid #f5a623;border-radius:8px;padding:20px;text-align:center;margin-bottom:12px"><span id="lfo-hz" style="display:block;font-size:2.5rem;font-weight:900;color:#f5a623;line-height:1">1.000 Hz</span><span id="lfo-ms" style="font-size:14px;color:#888;display:block;margin-top:6px">1000ms per cycle</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Dotted</span><span id="lfo-dot" style="font-size:14px;font-weight:700;color:#c8c8d8">-</span></div><div style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:10px;text-align:center"><span style="font-size:10px;color:#666;display:block;margin-bottom:3px">Triplet</span><span id="lfo-tri" style="font-size:14px;font-weight:700;color:#c8c8d8">-</span></div></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'LFO Rate to BPM Sync Calculator', 'Convert BPM and note division to exact LFO rate in Hz for tempo-syncing modulation effects.', html, _share(slug, term))


def _chord(slug, term):
    js = ('(function(){var S={major:[0,2,4,5,7,9,11],minor:[0,2,3,5,7,8,10],dorian:[0,2,3,5,7,9,10],phrygian:[0,1,3,5,7,8,10],lydian:[0,2,4,6,7,9,11],mixolydian:[0,2,4,5,7,9,10]};var Q={major:["maj","min","min","maj","maj","min","dim"],minor:["min","dim","maj","min","min","maj","maj"],dorian:["min","min","maj","maj","min","dim","maj"],phrygian:["min","maj","maj","min","dim","maj","min"],lydian:["maj","maj","min","dim","maj","min","min"],mixolydian:["maj","min","dim","maj","min","min","maj"]};var P={major:["I-IV-V-I","I-V-vi-IV","ii-V-I"],minor:["i-iv-v-i","i-VI-III-VII","ii-v-i"],dorian:["i-IV-i-IV","i-II-i-VII"],phrygian:["i-II-i-II","i-VII-VI-VII"],lydian:["I-II-I-II","I-V-II-I"],mixolydian:["I-VII-IV-I","I-VII-I-VII"]};var N=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];var R=["I","II","III","IV","V","VI","VII"];function calc(){var ri=document.getElementById("ck-r").selectedIndex;var sc=document.getElementById("ck-s").value;var ivs=S[sc];var qs=Q[sc];var ce=document.getElementById("ck-c");ce.innerHTML="";ivs.forEach(function(iv,i){var ni=(ri+iv)%12;var q=qs[i];var r=q==="min"?R[i].toLowerCase():q==="dim"?R[i].toLowerCase()+"o":R[i];var ch=N[ni]+(q==="min"?"m":q==="dim"?"o":"");var bg=i===0?"#1a0800":i===3||i===4?"#0d1a0d":"#13132a";var bc=i===0?"#f5a623":i===3||i===4?"rgba(96,192,96,.4)":"#2a2a4a";ce.innerHTML+=\'<div style="background:\'+bg+\';border:1px solid \'+bc+\';border-radius:6px;padding:10px 4px;text-align:center"><div style="font-size:9px;color:#888;margin-bottom:3px">\'+r+\'</div><div style="font-size:13px;font-weight:700;color:#e0e0f0">\'+ch+\'</div></div>\';});var ps=P[sc]||[];document.getElementById("ck-p").innerHTML=\'<div style="font-size:10px;color:#f5a623;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px">Common Progressions</div>\'+ps.map(function(p){return\'<div style="font-size:12px;color:#c8c8d8;padding:3px 0;border-bottom:1px solid #1a1a3a">\'+p+\'</div>\';}).join("");}["ck-r","ck-s"].forEach(function(id){document.getElementById(id).addEventListener("change",calc);});calc();})()')
    html = ('<div style="background:#13132a;border:1px solid #2a2a4a;border-radius:10px;padding:20px"><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px"><label style="font-size:12px;color:#c8c8d8;display:block">Root Key<select id="ck-r" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option>C</option><option>C#</option><option>D</option><option>D#</option><option>E</option><option>F</option><option>F#</option><option>G</option><option>G#</option><option selected>A</option><option>A#</option><option>B</option></select></label><label style="font-size:12px;color:#c8c8d8;display:block">Scale<select id="ck-s" style="display:block;width:100%;margin-top:4px;padding:8px 10px;background:#0d0d1a;border:1px solid #2a2a4a;border-radius:5px;color:#fff;font-size:13px"><option value="major">Major</option><option value="minor" selected>Natural Minor</option><option value="dorian">Dorian</option><option value="phrygian">Phrygian</option><option value="lydian">Lydian</option><option value="mixolydian">Mixolydian</option></select></label></div><div id="ck-c" style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:16px"></div><div id="ck-p" style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:6px;padding:14px"></div><script>' + js + SC + '</div>')
    return _wrap(slug, 'Chord and Key Reference', 'Select any root key and scale to see all 7 diatonic chords plus common progressions. Works for all modes.', html, _share(slug, term))


def build_signatures_html(signature_sounds):
    """FIX 19: Build Signature Sounds section cards."""
    if not signature_sounds:
        return ''
    cards = ''
    for sig in signature_sounds[:5]:
        track    = sig.get('track', '')
        settings = sig.get('settings', '')
        why      = sig.get('why', '')
        if not track:
            continue
        cards += (
            '        <div class="sig-card">\n'
            f'          <div class="sig-track">{track}</div>\n'
            f'          <div class="sig-settings">{settings}</div>\n'
            f'          <div class="sig-why">{why}</div>\n'
            '        </div>\n'
        )
    return cards


def build_session_breakdown_html(session_breakdown):
    """FIX 20: Build Session File Breakdown block."""
    if not session_breakdown:
        return ''
    scenario = session_breakdown.get('scenario', '')
    steps    = session_breakdown.get('steps', [])
    if not steps:
        return ''
    steps_html = ''
    for i, step in enumerate(steps[:5], 1):
        steps_html += (
            '          <div class="sfb-step">'
            f'<span class="sfb-num">{i}</span>'
            f'<span class="sfb-text">{step}</span>'
            '</div>\n'
        )
    return (
        '      <div class="session-file-breakdown" style="background:#0d0d1a;border:1px solid #2a2a4a;border-radius:10px;padding:20px;margin:20px 0">\n'
        '        <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:10px">Session File Breakdown</div>\n'
        f'        <div style="font-size:13px;color:#888;font-style:italic;margin-bottom:14px">{scenario}</div>\n'
        + steps_html +
        '      </div>\n'
    )




def build_tools_section(p1, slug):
    tool_key = TOOL_OVERRIDES.get(slug, '')
    term = p1.get('term', slug.replace('-', ' ').title())
    if tool_key == 'gr_calculator':      return _gr(slug, term)
    elif tool_key == 'delay_calculator': return _delay(slug, term)
    elif tool_key == 'lufs_calculator':  return _lufs(slug, term)
    elif tool_key == 'frequency_reference': return _freq(slug, term)
    elif tool_key == 'rt60_calculator':  return _rt60(slug, term)
    elif tool_key == 'note_freq':        return _note(slug, term)
    elif tool_key == 'adsr_visualizer':  return _adsr(slug, term)
    elif tool_key == 'gain_staging':     return _gs(slug, term)
    elif tool_key == 'headroom_calc':    return _hr(slug, term)
    elif tool_key == 'stereo_width':     return _sw(slug, term)
    elif tool_key == 'lfo_sync':         return _lfo(slug, term)
    elif tool_key == 'chord_key':        return _chord(slug, term)
    else:
        return (
            '      <section class="entry-section" id="tools">\n'
            '        <h2>Tools for This Entry</h2>\n'
            f'        <div style="background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:24px;text-align:center">\n'
            f'          <p style="font-size:13px;color:#888;margin:0">Interactive tool in development for {term}.</p>\n'
            '        </div>\n'
            '      </section>\n'
        )


# ══════════════════════════════════════════════════════════════════════════════
# build_html_t1()
# ══════════════════════════════════════════════════════════════════════════════

def build_html_t1(slug, term, category, p1, content_html, pub_date, quotes_filtered):
    today_str = datetime.date.today().isoformat()

    sc_pos          = p1.get('signal_chain_position', {}).get('positions', [])
    signal_chain    = build_signal_chain_svg(sc_pos, slug) if sc_pos else ''
    genre_html      = build_genre_table_html(p1.get('genre_settings_rows', []), term, slug, p1.get('genre_columns'), p1.get('genre_rows_v2'))
    plugin_html     = build_plugin_recs_html(p1.get('plugin_recommendations', {}))
    daw_html        = build_daw_tabs_html(p1.get('daw_implementations', {}), slug)
    comparison_html = build_comparison_callouts_html(p1.get('comparison_terms', []), term)
    related_html    = build_related_terms_html(p1.get('related_terms', []))
    track_html      = build_track_list_html(p1.get('track_examples', []))
    faq_html        = build_faq_html(p1.get('faq', []))
    flags_html      = build_flags_html(p1.get('red_flags', []), p1.get('green_flags', []))
    ba_html         = build_before_after_html(p1.get('before_after_text', {}))
    number_html     = build_the_number_html(p1.get('the_number',''), p1.get('the_number_label',''), p1.get('the_number_context',''))
    prereq_html     = build_prereq_chain(p1.get('prerequisites', []), p1)
    tools_html      = mpw_tools_v3.build_tools_section_v3(slug, p1.get("term", slug.replace("-"," ").title()))
    signatures_html = build_signatures_html(p1.get('signature_sounds', []))
    session_html    = build_session_breakdown_html(p1.get('session_breakdown', {}))
    sidebar_toc     = build_sidebar_toc_html(slug)
    spotlight_html  = build_producer_spotlight_html(p1)
    diff_cls        = difficulty_class(p1.get('difficulty', 'Intermediate'))

    html = content_html
    html = html.replace('THE_NUMBER_PLACEHOLDER',    number_html)
    html = html.replace('SIGNAL_CHAIN_PLACEHOLDER',  signal_chain)
    html = html.replace('GENRE_PLACEHOLDER',         genre_html)
    html = html.replace('PLUGIN_PLACEHOLDER',        plugin_html)
    html = html.replace('DAW_PLACEHOLDER',           daw_html)
    html = html.replace('COMPARISON_PLACEHOLDER',    comparison_html)
    html = html.replace('TRACK_PLACEHOLDER',         track_html)
    html = html.replace('FAQ_PLACEHOLDER',           faq_html)
    html = html.replace('FLAGS_PLACEHOLDER',         flags_html)
    html = html.replace('BEFORE_AFTER_PLACEHOLDER',  ba_html)
    # FIX 22: TOOLS_PLACEHOLDER — inject after quick-reference </section>, never inside it
    html = html.replace('TOOLS_PLACEHOLDER', tools_html)
    # FIX 20: SESSION_BREAKDOWN_PLACEHOLDER
    html = html.replace('SESSION_BREAKDOWN_PLACEHOLDER', session_html)
    # FIX 19: Signatures — replace placeholder if present, else inject before types section
    html = html.replace('PLUGIN_RECS_PLACEHOLDER', plugin_html)
    # P0b: wrap producers-verdict div if Pass 2 wrote it without wrapper
    if '<div class="verdict-header">' in html and '<div class="producers-verdict">' not in html:
        html = html.replace(
            '<div class="verdict-header">',
            '<div class="producers-verdict">\n    <div class="verdict-header">'
        )
        # close the producers-verdict div before </section> of verdict
        html = html.replace(
            '</section>\n\n<section class="entry-section" id="mistakes"',
            '</div>\n</section>\n\n<section class="entry-section" id="mistakes"'
        )
    html = html.replace('QUICKREF_SHARE_PLACEHOLDER',
        f'\n        <div class="mpw-share-bar">'
        f'<span class="mpw-share-label">Share</span>'
        f'<button class="mpw-share-btn share-copy" onclick="navigator.clipboard&&navigator.clipboard.writeText(\'musicproductionwiki.com/bible/{slug}#quick-reference\')">Copy Link</button>'
        f'<a href="https://x.com/intent/tweet?text={term}+Quick+Reference+%E2%80%94+%40mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}%23quick-reference" target="_blank" rel="noopener" class="mpw-share-btn share-x"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.26 5.632 5.905-5.632zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>Share on X</a>'
        f'<a href="https://reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}%23quick-reference&title={term}+Quick+Reference+%E2%80%94+MusicProductionWiki" target="_blank" rel="noopener" class="mpw-share-btn share-reddit"><svg width="12" height="12" viewBox="0 0 20 20" fill="currentColor"><circle cx="10" cy="10" r="10"/><path fill="#ff4500" d="M16.67 10a1.46 1.46 0 00-2.47-1 7.12 7.12 0 00-3.85-1.23l.65-3.08 2.13.45a1 1 0 101.07-1 1 1 0 00-.96.68l-2.38-.5a.27.27 0 00-.32.2l-.73 3.44a7.14 7.14 0 00-3.89 1.23 1.46 1.46 0 10-1.61 2.39 2.87 2.87 0 000 .44c0 2.24 2.61 4.06 5.83 4.06s5.83-1.82 5.83-4.06a2.87 2.87 0 000-.44 1.46 1.46 0 00.61-1.08zM7.5 11a1 1 0 111 1 1 1 0 01-1-1zm5.67 2.65a3.54 3.54 0 01-2.34.63 3.54 3.54 0 01-2.34-.63.25.25 0 01.35-.35 3.07 3.07 0 002 .48 3.07 3.07 0 002-.48.25.25 0 01.35.35zm-.17-1.65a1 1 0 111-1 1 1 0 01-1 1z"/></svg>Reddit</a>'
        f'</div>'
    )

    misconception = p1.get('misconception', {})
    misc_html = ''
    if misconception.get('myth'):
        misc_html = (
            '      <div class="misconception-block">'
            '<span class="misconception-label">Common Misconception</span>'
            f'<p class="misconception-belief">{misconception["myth"]}</p>'
            f'<p class="misconception-reality">{misconception.get("truth","")}</p>'
            '</div>\n'
        )

    also_bible = (
        '      <section class="entry-section" id="related">\n'
        '        <h2>Also in The Bible</h2>\n'
        f'{related_html}\n'
        '      </section>\n'
    )

    helpful_block = (
        '      <div class="helpful-block" id="helpful" style="background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin:32px 0">\n'
        '        <div style="font-size:13px;font-weight:600;color:#e0e0f0;margin-bottom:12px">What level did this entry match?</div>\n'
        '        <div style="display:flex;gap:8px;flex-wrap:wrap" class="helpful-btns">\n'
        '          <button onclick="helpfulVote(\'beginner\',this)" style="padding:7px 16px;border-radius:20px;border:1px solid #2a2a4a;background:transparent;color:#a0a0c0;font-family:inherit;font-size:13px;cursor:pointer">Beginner</button>\n'
        '          <button onclick="helpfulVote(\'intermediate\',this)" style="padding:7px 16px;border-radius:20px;border:1px solid #2a2a4a;background:transparent;color:#a0a0c0;font-family:inherit;font-size:13px;cursor:pointer">Intermediate</button>\n'
        '          <button onclick="helpfulVote(\'advanced\',this)" style="padding:7px 16px;border-radius:20px;border:1px solid #2a2a4a;background:transparent;color:#a0a0c0;font-family:inherit;font-size:13px;cursor:pointer">Advanced</button>\n'
        '        </div>\n'
        '        <div id="helpful-missing" style="display:none;margin-top:12px">\n'
        '          <label style="font-size:13px;color:#888">What\'s missing? <span style="color:#555">(optional)</span></label>\n'
        '          <div style="display:flex;gap:8px;margin-top:6px">\n'
        '            <input type="text" id="helpful-input" placeholder="e.g. more on sidechain..." style="flex:1;padding:8px 12px;border-radius:6px;border:1px solid #2a2a4a;background:#0d0d1a;color:#fff;font-size:13px">\n'
        '            <button onclick="helpfulSubmit()" style="background:#f5a623;color:#000;border:none;padding:8px 16px;border-radius:6px;font-weight:700;cursor:pointer;font-family:inherit">Send</button>\n'
        '          </div>\n'
        '        </div>\n'
        '        <div id="helpful-thanks" style="display:none;color:#60ff60;font-size:13px;margin-top:10px">Thanks \u2014 your feedback shapes future entries. \u2713</div>\n'
        '      </div>\n'
    )

    helpful_js = (
        '<script>\n'
        'function helpfulVote(level,btn){\n'
        '  document.querySelectorAll(\'.helpful-btns button\').forEach(function(b){b.style.background=\'transparent\';b.style.color=\'#a0a0c0\';b.style.borderColor=\'#2a2a4a\';});\n'
        '  btn.style.background=\'rgba(245,166,35,.15)\';btn.style.color=\'#f5a623\';btn.style.borderColor=\'#f5a623\';\n'
        '  document.getElementById(\'helpful-missing\').style.display=\'block\';\n'
        f'  if(typeof gtag!==\'undefined\') gtag(\'event\',\'helpful_vote\',{{level:level,slug:\'{slug}\'}});\n'
        '  document.getElementById(\'helpful-missing\').dataset.level=level;\n'
        '}\n'
        'function helpfulSubmit(){\n'
        '  var level=document.getElementById(\'helpful-missing\').dataset.level||\'\';\n'
        '  var missing=document.getElementById(\'helpful-input\').value.trim();\n'
        f'  if(typeof gtag!==\'undefined\') gtag(\'event\',\'helpful_submit\',{{level:level,has_feedback:!!missing,slug:\'{slug}\'}});\n'
        '  document.getElementById(\'helpful-missing\').style.display=\'none\';\n'
        '  document.getElementById(\'helpful-thanks\').style.display=\'block\';\n'
        '}\n'
        '</script>\n'
    )

    word_count = count_words_html(html)
    read_min   = max(1, round(word_count / 325))
    head       = build_head(slug, term, category, p1, pub_date, today_str, word_count, read_min)
    nav        = build_nav_html(category)
    enav       = build_entry_nav()
    js         = build_js(slug, p1)
    footer     = build_footer(term, slug, today_str)

    return f"""{head}
<body>
{nav}
{enav}
<main id="main-content">
  <div class="bible-entry-wrap" style="display:grid!important;grid-template-columns:1fr 280px!important;gap:40px!important;align-items:start!important;max-width:1100px!important;margin:0 auto!important;padding:40px 24px!important">
    <div class="entry-main">
      <nav class="entry-breadcrumb" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="bc-sep">&rsaquo;</span>
        <a href="/bible/">The Producer's Bible</a><span class="bc-sep">&rsaquo;</span>
        <span aria-current="page">{term}</span>
      </nav>
      <div class="entry-masthead">
        <div class="entry-category">{category}</div>
        <span class="difficulty-badge {diff_cls}">{p1.get('difficulty','Intermediate')}</span>
{prereq_html}
        <h1 class="entry-term">{term}</h1>
        <div class="entry-pos">noun / {category.lower()} tool</div>
        <em class="entry-hook">{p1.get('emotional_hook','')}</em>
        <div class="entry-meta">
          <span>&#128197; {pub_date}</span>
          <span>&#9202; {read_min} min read</span>
          <span>&#128218; Producer's Bible</span>
        </div>
      </div>
      <div id="quick-answer" class="quick-answer-block">
        <div class="qa-label">Quick Answer</div>
        <p class="qa-text">{p1.get('definition','')}</p>
      </div>
      <div class="start-here-box" style="background:#0d1a0d;border:1px solid rgba(96,192,96,.3);border-radius:8px;padding:14px 18px;margin-bottom:20px">
        <div style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#60c060;margin-bottom:8px">New to {term}? Start here</div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12px;color:#c8c8d8">
          <a href="#parameters" style="color:#f5a623;text-decoration:none;font-weight:600;border:1px solid rgba(245,166,35,.3);padding:3px 10px;border-radius:4px">Parameters</a>
          <span style="color:#555">&#8594;</span>
          <a href="#before-after" style="color:#f5a623;text-decoration:none;font-weight:600;border:1px solid rgba(245,166,35,.3);padding:3px 10px;border-radius:4px">Before / After</a>
          <span style="color:#555">&#8594;</span>
          <a href="#quick-reference" style="color:#f5a623;text-decoration:none;font-weight:600;border:1px solid rgba(245,166,35,.3);padding:3px 10px;border-radius:4px">Quick Reference</a>
          <span style="color:#555">&#8594;</span>
          <a href="#in-the-wild" style="color:#f5a623;text-decoration:none;font-weight:600;border:1px solid rgba(245,166,35,.3);padding:3px 10px;border-radius:4px">In The Wild</a>
        </div>
      </div>
      <div style="margin-bottom:24px">
        <button class="pdf-export-btn" onclick="openGateFor('full')">&#8659; Download Reference Sheet</button>
      </div>
      <div id="pdf-gate-modal" class="pgm-overlay" style="display:none">
        <div class="pgm-card">
          <button class="pgm-close" onclick="closeGate()">&#10005;</button>
          <div id="pgm-icon" style="font-size:2rem;margin-bottom:8px">&#8659;</div>
          <h3 id="pgm-title">Get the Free Sheet</h3>
          <p id="pgm-desc" style="color:#888;font-size:13px;margin-bottom:16px">Free with The Producer's Briefing.</p>
          <input type="email" id="pgm-email" placeholder="your@email.com" style="width:100%;padding:10px 14px;border-radius:6px;border:1px solid #2a2a4a;background:#0d0d1a;color:#fff;font-size:14px;margin-bottom:10px;box-sizing:border-box">
          <button class="pgm-submit" onclick="submitGate()">Get My Free Sheet</button>
          <p class="pgm-fine">No spam. Unsubscribe anytime.</p>
          <p id="pgm-error" style="display:none;color:#ff6666;font-size:12px;margin-top:8px"></p>
        </div>
      </div>
{misc_html}
{html}
{helpful_block}
{also_bible}
    </div>
    <aside class="entry-sidebar" style="min-width:280px;width:280px;position:sticky;top:148px;align-self:start;overflow-y:auto;height:calc(100vh - 168px);">
{sidebar_toc}
{spotlight_html}
      <div class="sidebar-share" style="background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px;margin-bottom:16px">
        <h4 style="font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:12px;font-weight:700">Share This Entry</h4>
        <div class="mpw-share-bar" style="flex-direction:column;border-top:none;padding-top:0;margin-top:0;gap:6px;">
          <button class="mpw-share-btn share-copy" style="width:100%;justify-content:center" onclick="(function(b){{navigator.clipboard.writeText('https://musicproductionwiki.com/bible/{slug}').then(function(){{b.textContent='Copied!';setTimeout(function(){{b.textContent='Copy Link'}},2000);}})}})(this)">Copy Link</button>
          <a href="https://x.com/intent/tweet?text={term}+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}" target="_blank" rel="noopener" class="mpw-share-btn share-x" style="width:100%;justify-content:center">Share on X</a>
          <a href="https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2F{slug}&title={term}+%E2%80%94+The+Producer%27s+Bible" target="_blank" rel="noopener" class="mpw-share-btn share-reddit" style="width:100%;justify-content:center">Reddit</a>
        </div>
      </div>
      <div class="sidebar-nl">
        <h4>The Producer's Briefing</h4>
        <p>Weekly technique + gear intel. Free.</p>
        <input type="email" placeholder="your@email.com">
        <button>Subscribe Free</button>
      </div>
    </aside>
  </div>
</main>
{footer}
{js}
{helpful_js}
</body></html>"""


# ══════════════════════════════════════════════════════════════════════════════
# build_html_t2()
# ══════════════════════════════════════════════════════════════════════════════

def build_html_t2(slug, term, category, p1, content_html, pub_date, quotes_filtered):
    today_str    = datetime.date.today().isoformat()
    sc_pos       = p1.get('signal_chain_position', {}).get('positions', [])
    genre_html   = build_genre_table_html(p1.get('genre_settings_rows', []), term, slug)
    plugin_html  = build_plugin_recs_html(p1.get('plugin_recommendations', {}))
    daw_html     = build_daw_tabs_html(p1.get('daw_implementations', {}), slug)
    related_html = build_related_terms_html(p1.get('related_terms', []))
    faq_html     = build_faq_html(p1.get('faq', []))
    flags_html   = build_flags_html(p1.get('red_flags', []), p1.get('green_flags', []))
    number_html  = build_the_number_html(p1.get('the_number',''), p1.get('the_number_label',''), p1.get('the_number_context',''))
    signal_html  = build_signal_chain_svg(sc_pos, slug) if sc_pos else ''
    prereq_html  = build_prereq_chain(p1.get('prerequisites', []), p1)
    diff_cls     = difficulty_class(p1.get('difficulty', 'Intermediate'))
    sidebar_toc  = build_sidebar_toc_html(slug)

    html = content_html
    for ph, val in [
        ('THE_NUMBER_PLACEHOLDER', number_html), ('SIGNAL_CHAIN_PLACEHOLDER', signal_html),
        ('GENRE_PLACEHOLDER', genre_html), ('PLUGIN_PLACEHOLDER', plugin_html),
        ('DAW_PLACEHOLDER', daw_html), ('FAQ_PLACEHOLDER', faq_html),
        ('FLAGS_PLACEHOLDER', flags_html), ('QUICKREF_SHARE_PLACEHOLDER', ''),
    ]:
        html = html.replace(ph, val)

    also_bible = f'      <section class="entry-section" id="related">\n        <h2>Also in The Bible</h2>\n{related_html}\n      </section>\n'
    word_count = count_words_html(html)
    read_min   = max(1, round(word_count / 325))
    head       = build_head(slug, term, category, p1, pub_date, today_str, word_count, read_min)
    nav        = build_nav_html(category)
    js         = build_js(slug, p1)
    footer     = build_footer(term, slug, today_str)

    t2_pills = ''.join(f'<a href="{h}">{l}</a>' for h,l in [
        ('#definition','Definition'),('#how-it-works','How It Works'),('#parameters','Parameters'),
        ('#quick-reference','Quick Ref'),('#signal-chain','Signal Chain'),('#how-to-use','How To Use'),
        ('#genre-table','By Genre'),('#hardware-plugin','Hardware vs Plugin'),('#types','Types'),
        ('#mistakes','Mistakes'),('#flags','Flags'),('#faq','FAQ'),('#related','Related'),
    ])
    t2_nav = f'<nav class="entry-nav" aria-label="Entry sections"><div class="entry-nav-inner">{t2_pills}</div></nav>'

    return (
        f'{head}\n<body>\n{nav}\n{t2_nav}\n'
        '<main id="main-content"><div class="bible-entry-wrap"><div class="entry-main">\n'
        f'  <nav class="entry-breadcrumb"><a href="/">Home</a><span class="bc-sep">&rsaquo;</span><a href="/bible/">The Producer\'s Bible</a><span class="bc-sep">&rsaquo;</span><span>{term}</span></nav>\n'
        f'  <div class="entry-masthead"><div class="entry-category">{category}</div>'
        f'<span class="difficulty-badge {diff_cls}">{p1.get("difficulty","Intermediate")}</span>'
        f'{prereq_html}<h1 class="entry-term">{term}</h1>'
        f'<em class="entry-hook">{p1.get("emotional_hook","")}</em>'
        f'<div class="entry-meta"><span>&#128197; {pub_date}</span><span>&#9202; {read_min} min read</span><span>&#128218; Producer\'s Bible</span></div></div>\n'
        f'  <div id="quick-answer" class="quick-answer-block"><div class="qa-label">Quick Answer</div><p class="qa-text">{p1.get("definition","")}</p></div>\n'
        '  <div style="margin-bottom:24px"><button class="pdf-export-btn" onclick="openGateFor(\'full\')">&#8659; Download Reference Sheet</button></div>\n'
        '  <div id="pdf-gate-modal" class="pgm-overlay" style="display:none"><div class="pgm-card">'
        '<button class="pgm-close" onclick="closeGate()">&#10005;</button>'
        '<div id="pgm-icon" style="font-size:2rem;margin-bottom:8px">&#8659;</div>'
        '<h3 id="pgm-title">Get the Free Sheet</h3>'
        '<p id="pgm-desc" style="color:#888;font-size:13px;margin-bottom:16px">Free with The Producer\'s Briefing.</p>'
        '<input type="email" id="pgm-email" placeholder="your@email.com" style="width:100%;padding:10px 14px;border-radius:6px;border:1px solid #2a2a4a;background:#0d0d1a;color:#fff;font-size:14px;margin-bottom:10px;box-sizing:border-box">'
        '<button class="pgm-submit" onclick="submitGate()">Get My Free Sheet</button>'
        '<p class="pgm-fine">No spam. Unsubscribe anytime.</p>'
        '<p id="pgm-error" style="display:none;color:#ff6666;font-size:12px;margin-top:8px"></p>'
        '</div></div>\n'
        f'{html}\n{also_bible}'
        '</div>\n'
        f'<aside class="entry-sidebar">{sidebar_toc}'
        '<div class="sidebar-nl"><h4>The Producer\'s Briefing</h4><p>Weekly technique + gear intel. Free.</p>'
        '<input type="email" placeholder="your@email.com"><button>Subscribe Free</button></div>'
        '</aside></div></main>\n'
        f'{footer}\n{js}\n</body></html>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# build_html_t3()
# ══════════════════════════════════════════════════════════════════════════════

def build_html_t3(slug, term, category, p1, content_html, pub_date):
    today_str    = datetime.date.today().isoformat()
    related_html = build_related_terms_html(p1.get('related_terms', []))
    faq_html     = build_faq_html((p1.get('faq') or [])[:3])
    diff_cls     = difficulty_class(p1.get('difficulty', 'Beginner'))

    html = content_html
    html = html.replace('FAQ_PLACEHOLDER',     faq_html)
    html = html.replace('RELATED_PLACEHOLDER', related_html)

    word_count = count_words_html(html)
    read_min   = max(1, round(word_count / 325))
    head       = build_head(slug, term, category, p1, pub_date, today_str, word_count, read_min)
    nav        = build_nav_html(category)
    js         = build_js(slug, p1)
    footer     = build_footer(term, slug, today_str)

    t3_pills = ''.join(f'<a href="{h}">{l}</a>' for h,l in [
        ('#definition','Definition'),('#how-it-works','How It Works'),
        ('#parameters','Parameters'),('#quick-reference','Quick Ref'),
        ('#faq','FAQ'),('#related','Related'),
    ])
    t3_nav = f'<nav class="entry-nav" aria-label="Entry sections"><div class="entry-nav-inner">{t3_pills}</div></nav>'

    return (
        f'{head}\n<body>\n{nav}\n{t3_nav}\n'
        '<main id="main-content"><div class="bible-entry-wrap"><div class="entry-main">\n'
        f'  <nav class="entry-breadcrumb"><a href="/">Home</a><span class="bc-sep">&rsaquo;</span><a href="/bible/">The Producer\'s Bible</a><span class="bc-sep">&rsaquo;</span><span>{term}</span></nav>\n'
        f'  <div class="entry-masthead"><div class="entry-category">{category}</div>'
        f'<span class="difficulty-badge {diff_cls}">{p1.get("difficulty","Beginner")}</span>'
        f'<h1 class="entry-term">{term}</h1>'
        f'<em class="entry-hook">{p1.get("emotional_hook","")}</em>'
        f'<div class="entry-meta"><span>&#128197; {pub_date}</span><span>&#9202; {read_min} min read</span><span>&#128218; Producer\'s Bible</span></div></div>\n'
        f'  <div id="quick-answer" class="quick-answer-block"><div class="qa-label">Quick Answer</div><p class="qa-text">{p1.get("definition","")}</p></div>\n'
        f'{html}\n'
        f'  <section class="entry-section" id="related"><h2>Also in The Bible</h2>{related_html}</section>\n'
        '</div>\n'
        '<aside class="entry-sidebar"><div class="sidebar-nl"><h4>The Producer\'s Briefing</h4>'
        '<p>Weekly technique + gear intel. Free.</p><input type="email" placeholder="your@email.com">'
        '<button>Subscribe Free</button></div></aside></div></main>\n'
        f'{footer}\n{js}\n</body></html>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# GENERATE ENTRY
# ══════════════════════════════════════════════════════════════════════════════

def generate_entry(slug, term, category, tier, pub_date, output_dir='.'):
    print(f"\n{'='*60}\n  {term} ({slug}) — Tier {tier}\n{'='*60}")

    p1              = run_pass1(slug, term, category, tier)
    quotes_all      = load_quotes()
    tags            = p1.get('tags', []) + [category.lower(), slug]
    quotes_filtered = filter_quotes(quotes_all, tags, 10)
    quotes_context  = build_quotes_context(quotes_filtered, tags)

    tracks = p1.get('track_examples', [])
    track_list_str = 'LOCKED TRACK LIST (use exactly these):\n' + ''.join(
        f"{i}. {t.get('artist','')} \u2014 {t.get('track','')} ({t.get('year','')}), {t.get('album','')}. Produced by {t.get('produced_by','')}.\n"
        for i, t in enumerate(tracks, 1)
    )

    p1_json = json.dumps(p1, indent=2, ensure_ascii=False)

    if tier == 1:
        print(f"  Pass 2 (T1, {PASS2_TOKENS_T1} tokens)...")
        prose = call_claude(build_pass2_prompt_t1(slug, term, category, p1_json, track_list_str, quotes_context, pub_date), PASS2_TOKENS_T1, PASS2_SYSTEM_T1)
        html  = build_html_t1(slug, term, category, p1, prose, pub_date, quotes_filtered)
    elif tier == 2:
        print(f"  Pass 2 (T2, {PASS2_TOKENS_T2} tokens)...")
        prose = call_claude(build_pass2_prompt_t2(slug, term, category, p1_json, quotes_context, pub_date), PASS2_TOKENS_T2, PASS2_SYSTEM_T2)
        html  = build_html_t2(slug, term, category, p1, prose, pub_date, quotes_filtered)
    else:
        print(f"  Pass 2 (T3, {PASS2_TOKENS_T3} tokens)...")
        prose = call_claude(build_pass2_prompt_t3(slug, term, category, p1_json, pub_date), PASS2_TOKENS_T3, PASS2_SYSTEM_T3)
        html  = build_html_t3(slug, term, category, p1, prose, pub_date)

    out_path = os.path.join(output_dir, f'{slug}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    words = count_words_html(html)
    size  = os.path.getsize(out_path)
    print(f"  Written: {out_path} ({words:,}w / {size//1024}KB)")
    return out_path, html


# ══════════════════════════════════════════════════════════════════════════════
# GITHUB COMMIT
# ══════════════════════════════════════════════════════════════════════════════

def gh_api(path, method='GET', body=None):
    url  = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/{path}'
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(url, data=data, method=method, headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept':        'application/vnd.github.v3+json',
        'Content-Type':  'application/json',
        'User-Agent':    'mpw-bible-writer',
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f'[GH {e.code}] {e.read().decode()[:300]}')
        return None

def gh_trees_commit(files_dict, message):
    ref    = gh_api(f'git/ref/heads/{BRANCH}')
    if not ref: return None
    head   = ref['object']['sha']
    base_t = gh_api(f'git/commits/{head}')['tree']['sha']
    items  = []
    for path, content in files_dict.items():
        b64  = base64.b64encode(content.encode('utf-8')).decode('ascii')
        blob = gh_api('git/blobs', 'POST', {'content': b64, 'encoding': 'base64'})
        if not blob: return None
        items.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
        time.sleep(0.3)
    new_tree   = gh_api('git/trees', 'POST', {'base_tree': base_t, 'tree': items})
    if not new_tree: return None
    new_commit = gh_api('git/commits', 'POST', {'message': message, 'tree': new_tree['sha'], 'parents': [head]})
    if not new_commit: return None
    gh_api(f'git/refs/heads/{BRANCH}', 'PATCH', {'sha': new_commit['sha']})
    return new_commit['sha']


# ══════════════════════════════════════════════════════════════════════════════
# VALIDATION SUITE — 75+ checks
# ══════════════════════════════════════════════════════════════════════════════

def run_validate(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        c = f.read()
    script_src = open(__file__, 'r', encoding='utf-8').read()

    checks = {
        'mpw-slim-bar':                'mpw-slim-bar' in c,
        'bible-bar':                   'class="bible-bar"' in c,
        'bb-cats':                     'bb-cats' in c,
        'no identity bar':             'bible-identity-bar' not in c,
        'no Sections label':           'entry-nav-label' not in c,
        'slim bar z700':               'z-index:700' in c,
        'bible bar z600':              'z-index:600' in c,
        'entry nav top 90px':          'top:90px' in c,
        'scroll-margin 128px':         'scroll-margin-top:128px' in c,
        'scroll-margin mobile 110px':  'scroll-margin-top:110px' in c,
        'progress display none':        '#reading-progress' in c and 'display:none' in c,
        'progress display block mobile':'display:block' in c and 'reading-progress' in c,
        'track-artist class':           'class="track-artist"' in c,
        'no youtube':                   'youtube.com' not in c,
        'no spotify':                   'spotify.com' not in c,
        'no audio toggle':              'audio-toggle' not in c,
        'producer-quote':               'class="producer-quote"' in c,
        'producer-quote-block':         'class="producer-quote-block"' in c,
        'prereq-chain':                 'prereq-chain' in c,
        'difficulty-badge':             'difficulty-badge' in c,
        'misconception-block':          'misconception-block' in c,
        'before-after':                 'before-after' in c,
        'the-number-box':               'the-number-box' in c,
        'daw-tabs':                     'daw-tabs' in c,
        'daw-tab-btn':                  'daw-tab-btn' in c,
        'plugin-recs':                  'class="plugin-recs"' in c,
        'plugin-tier':                  'plugin-tier' in c,
        'genre-settings-table':         'genre-settings-table' in c,
        'signal-chain svg 1440':        'viewBox="0 0 1440 160"' in c,
        'signal-chain-mobile':          'signal-chain-mobile' in c,
        'scm-box':                      'scm-box' in c,
        'comparison-callouts':          'comparison-callouts' in c,
        'pdf-export-btn':               'pdf-export-btn' in c,
        'openGateFor':                  'openGateFor' in c,
        'downloadQuickRef':             'downloadQuickRef' in c,
        'downloadGenreTable':           'downloadGenreTable' in c,
        'last-verified':                'last-verified' in c,
        'SpeakableSpecification':       'SpeakableSpecification' in c,
        'HowTo schema':                 '"@type": "HowTo"' in c,
        'sameAs in schema':             'sameAs' in c,
        'lastReviewed in schema':       'lastReviewed' in c,
        'sidebar-toc':                  'sidebar-toc' in c,
        'setTocActive':                 'setTocActive' in c,
        'sidebar-nl':                   'sidebar-nl' in c,
        'tools section':                'id="tools"' in c,
        'tool present':                 any(x in c for x in ['gc-input','dt-bpm','lc-cur','rt-vol','freq-bands','nf-note','adsr-c','gs-s','hr-pk','sw-cv','lfo-b','ck-r']),
        'start-here-box':               'start-here-box' in c,
        'Also in The Bible':            'Also in The Bible' in c,
        'mpw-share-bar present':        'mpw-share-bar' in c,
        'calc-share-bar present':       'calc-share-bar' in c,
        'daw-tab-nav flex-wrap':        'flex-wrap:wrap' in c,
        'comparison-callouts 1col':     'comparison-callouts' in c and 'grid-template-columns:1fr' in c,
        'history-card':                 'history-card' in c,
        'load_quotes fn in script':     'load_quotes' in script_src,
        'filter_quotes fn in script':   'filter_quotes' in script_src,
        'build_quotes_context fn':      'build_quotes_context' in script_src,
        'overflow-x:clip html':         'overflow-x:clip' in c,
        'entry-sidebar hidden mobile':  'entry-sidebar' in c and 'display:none' in c,
        'signal-chain svg hidden mobile':'signal-chain-diagram' in c and 'display:none' in c,
        'bible-mobile-bar flex':        'bible-mobile-bar' in c and 'display:flex' in c,
        'entry-nav 84px mobile':        'top:84px' in c,
        'grid 1col mobile':             'grid-template-columns:1fr' in c,
        'viewport meta':                'width=device-width' in c,
        'canonical':                    'rel="canonical"' in c,
        'og:type':                      'og:type' in c,
        'twitter:card':                 'twitter:card' in c,
        'GA4':                          'G-79VB543KCT' in c,
        'FAQPage schema':               '"@type": "FAQPage"' in c,
        'BreadcrumbList schema':        '"@type": "BreadcrumbList"' in c,
        'Article schema':               '"@type": "Article"' in c,
        'no main.js':                   '/js/main.js' not in c,
        'beehiiv':                      'beehiiv' in c,
        'entry-section class':          'class="entry-section"' in c,
        'quick-answer-block':           'quick-answer-block' in c,
        'entry-masthead':               'entry-masthead' in c,
        'producer-spotlight':           'producer-spotlight' in c,
        'no Further Reading h2':        '<h2>Further Reading</h2>' not in c,
        'helpful-block':                'helpful-block' in c,
        'word count floor 6800':        '6800' in script_src,
        'word count ceil 7800':         '7800' in script_src,
        # v5.2 checks (FIX S43)
        '3 producer quotes':            c.count('class="producer-quote-block"') >= 3,
        'signatures section':           'id="signatures"' in c,
        'sig-card present':             'sig-card' in c,
        'ps-move present':              'ps-move' in c,
        'scroll+touchmove nav':         'touchmove' in c and 'scrollIntoView' in c,
        'no IntersectionObserver enav': 'obs2' not in c,
        # v5.2 checks (FIX S44)
        'sr-only class':                'sr-only' in c,
        'verdict section element':      'id="verdict"' in c and 'entry-section' in c,
        'producers-verdict wrapper':    'class="producers-verdict"' in c,
    }

    passed   = sum(1 for v in checks.values() if v)
    total    = len(checks)
    failures = [k for k, v in checks.items() if not v]

    print(f"\n{'='*50}")
    print(f"  VALIDATION: {passed}/{total} checks passed")
    print(f"{'='*50}")
    if failures:
        print(f"\n  FAILED ({len(failures)}):")
        for k in failures:
            print(f"    \u2717 {k}")
    else:
        print("  ALL CHECKS PASSED \u2713")
    return passed, total, failures


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='mpw_bible_writer.py v5.1')
    parser.add_argument('--validate',   action='store_true')
    parser.add_argument('--test',       action='store_true')
    parser.add_argument('--batch-file', help='slug:Term:Category:Tier per line')
    parser.add_argument('--slug',       default='compression')
    parser.add_argument('--term',       default='Compression')
    parser.add_argument('--category',   default='Signal Processing')
    parser.add_argument('--tier',       type=int, default=1)
    parser.add_argument('--start-date', default=datetime.date.today().isoformat())
    parser.add_argument('--output-dir', default='.')
    parser.add_argument('--html-file',  default=None)
    parser.add_argument('--no-commit',  action='store_true')
    parser.add_argument('--workers',    type=int, default=4, help='Parallel workers (default 4, max 8)')
    args = parser.parse_args()

    if args.validate:
        target = args.html_file or os.path.join(args.output_dir, f'{args.slug}.html')
        if not os.path.exists(target):
            htmls = [f for f in os.listdir(args.output_dir) if f.endswith('.html')]
            target = os.path.join(args.output_dir, htmls[0]) if htmls else None
        if not target or not os.path.exists(target):
            print(f'No HTML found to validate.')
            sys.exit(1)
        run_validate(target)
        return

    if args.test:
        out_path, _ = generate_entry(args.slug, args.term, args.category, args.tier, args.start_date, args.output_dir)
        passed, total, failures = run_validate(out_path)
        print(f"\n  {'READY for visual QA' if not failures else str(len(failures))+' checks failed — fix before batch'}")
        return

    if args.batch_file:
        if not os.path.exists(args.batch_file):
            print(f'Batch file not found: {args.batch_file}')
            sys.exit(1)
        with open(args.batch_file, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]

        committed, errors = {}, []
        lock = __import__('threading').Lock()

        def run_one(line):
            parts = line.split(':')
            if len(parts) < 3:
                print(f'  [SKIP] {line}'); return
            sl = parts[0].strip(); tm = parts[1].strip()
            ca = parts[2].strip(); ti = int(parts[3].strip()) if len(parts) > 3 else 1
            try:
                _, html = generate_entry(sl, tm, ca, ti, args.start_date, args.output_dir)
                with lock:
                    committed[f'bible/{sl}.html'] = html
            except Exception as e:
                print(f'  [ERROR] {sl}: {e}')
                with lock:
                    errors.append(sl)

        workers = min(max(1, args.workers), 8)
        print(f'  Running {len(lines)} entries with {workers} workers...')
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(run_one, line): line for line in lines}
            for fut in concurrent.futures.as_completed(futures):
                try:
                    fut.result()
                except Exception as e:
                    print(f'  [WORKER ERROR] {futures[fut]}: {e}')

        if committed and not args.no_commit:
            sha = gh_trees_commit(committed, f"Bible: {len(committed)} v5.1 entries — {args.start_date}")
            print(f"  {'Committed: '+sha if sha else 'Commit failed'}")
        if errors:
            print(f"\nFailed: {', '.join(errors)}")
        return

    parser.print_help()


if __name__ == '__main__':
    main()

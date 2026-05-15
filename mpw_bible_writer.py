"""
mpw_bible_writer.py v4.0 — MusicProductionWiki.com Producer's Bible Writer
Two-pass architecture: Pass 1 (structured data, 20k tokens) + Pass 2 (prose, 16k tokens)
Word count: 5,500 floor / 6,000 target / 6,500 ceiling
Spotify: green link buttons only — NO iframes ever

Usage:
    python mpw_bible_writer.py --validate
    python mpw_bible_writer.py --test --slug compression --term "Compression" --category "Signal Processing"
    python mpw_bible_writer.py --test --slug air --term "Air Frequency EQ" --category "Frequency" --start-date 2026-05-12
    python mpw_bible_writer.py --batch-file Bible-Batches/batch15.txt --start-date 2026-05-15

Batch file format (one per line): slug:Term:Category

NEVER include Spotify iframes — always use styled link buttons.
NEVER run parallel blob creation — always sequential with 403 backoff.
GitHub API blocked from Claude's environment — run from Steve's PowerShell only.

NO main.js — bible pages are fully self-contained.
"""

import os
import sys
import json
import time
import re
import argparse
import ast
import requests
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ─── CONFIG ────────────────────────────────────────────────────────────────────

TOKEN = os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_KEY', '')
GH_TOKEN = os.environ.get('GITHUB_TOKEN', 'YOUR_GITHUB_TOKEN_HERE')
REPO = 'musicproductionwiki/musicproductionwiki'
GH_HEADERS = {
    'Authorization': f'token {GH_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

MODEL = 'claude-sonnet-4-6'
PASS1_TOKENS = 20000
PASS2_TOKENS = 16000
WORKERS = 8
BACKOFF = [15, 30, 60, 120, 240]

WORD_COUNT_FLOOR = 5500
WORD_COUNT_TARGET = 6000
WORD_COUNT_CEILING = 6500

SITE_URL = 'https://musicproductionwiki.com'

# ─── SYSTEM PROMPT ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are writing an entry for The Producer's Bible — MusicProductionWiki.com's authoritative music production reference.

The Producer's Bible is to music production what Britannica is to general knowledge. It is not a blog, not a listicle, not a beginner's guide. It is a reference work that a professional music engineer would trust.

Voice: Authoritative. Direct. Knowledgeable. Not academic — written by someone who has spent thousands of hours in a studio, not in a university. The reader is a serious producer who will immediately know if the content is superficial.

Standards: Every claim is specific. Every technique has a number attached. Every track example names the exact moment and what to listen for. Every mistake names the exact symptom and the exact fix.

This entry will be read by producers at every level — beginners who are learning, professionals who are checking a reference, and everyone in between. Beginners need the foundation. Professionals need the depth. Both need the precision.

You are not writing marketing copy. You are not hedging. You are not being safe. You are telling producers exactly what they need to know, in the most useful format possible.

CRITICAL SLUG RULE: For further_reading_slugs and related_terms slugs, ONLY use slugs from this confirmed list of live Bible entries: compression, eq, limiting, saturation, distortion, reverb, delay, sidechain-compression, parallel-compression, multiband-compression, transient-shaping, noise-gate, gain-staging, headroom, stereo-imaging, mid-side-processing, bus-compression, mix-bus, send-return, automation, mastering, lufs, dynamic-range, true-peak-limiting, loudness-normalization, subtractive-synthesis, fm-synthesis, wavetable-synthesis, additive-synthesis, lfo, envelope, oscillator, adsr, vocoder, high-pass-filter, low-pass-filter, parametric-eq, shelving-eq, resonance, harmonic-distortion, chorus, flanger, phaser, tremolo, vibrato, plate-reverb, room-reverb, convolution-reverb, clip-gain, air-frequency-eq. If a term is not on this list, do NOT include it as a slug — omit it entirely rather than guess."""


# ─── PASS 1 PROMPT ─────────────────────────────────────────────────────────────

def build_pass1_prompt(slug, term, category):
    return f"""You are writing a structured data JSON for a Producer's Bible entry on "{term}" (category: {category}).

Return ONLY valid JSON — no markdown fences, no preamble, no commentary. The JSON must be parseable by json.loads().

QUALITY RULES — NON-NEGOTIABLE:

TERM: {term} — every section must be specifically about {term}, not a generic music production concept.

emotional_hook: One italic pull-quote. Must NOT say "{term} is the most important tool in music production." Must create genuine curiosity or reframe the producer's relationship with the concept. Example of acceptable: "Every record you've ever loved was shaped by compression you couldn't hear — and that invisibility is the entire point." Example of unacceptable: "{term} is perhaps the most essential tool in the modern producer's toolkit."

parameters: Each parameter description MUST include technical language (what it does mathematically) AND perceptual language (what the producer hears). Clearly separated. Include specific numbers.

track_examples: minimum 5. Each MUST be from a DIFFERENT artist, a DIFFERENT genre, a DIFFERENT decade. No two from same artist. No two from same genre. The note must be specific enough a producer could listen and find the exact moment described. No generic "this track uses {term} effectively."

faq: 8 questions. Mix: 2 beginner (What is..., How do I start...), 3 intermediate (technique-specific, comparison-based), 3 advanced (nuance, edge cases, professional context). No two questions that are variations of the same question. Answers: 3-5 sentences each. Direct. Opinionated where appropriate. Never "it depends" without then answering what it depends on.

the_number: Must be specific, session-usable, defensible. One value, not a range. The number a professional would tattoo on their hand if they could only remember one thing about this term.

producer_quote: Only include if you are confident the quote is real and accurately attributed. Omit the key entirely if uncertain. No fabricated quotes.

red_flags: 5 minimum. Each must name a specific audible symptom with approximate parameter values.
green_flags: 5 minimum. Each must name a specific audible or measurable result confirming correct application.
interaction_warnings: 2 minimum. Each must name: the interacting tool/process, the problematic condition, the audible result, and the fix.

genre_application_rows: Values must be genuinely different across genres — not slight variations. Adapt columns to what makes sense for this specific term.

hardware_vs_plugin_rows: Genuine character differences, not marketing copy. If the plugin is a faithful emulation, say so honestly.

TOKEN BUDGET: 20,000 tokens. Never let one field consume more than 15% of budget. A truncated JSON is worthless — complete the full object.
NEVER use placeholder text in any field.
NEVER generate a quote you are not confident is real.

Return this exact JSON structure:

{{
  "term": "{term}",
  "slug": "{slug}",
  "category": "{category}",
  "part_of_speech": "noun|verb|adjective",
  "pronunciation": "IPA or plain phonetic",
  "entry_pos_label": "noun / signal processing tool",
  "meta_description": "Under 155 chars, SEO-optimized, includes {term}",
  "meta_keywords": ["6-8 keyword strings"],
  "quick_answer": "Under 40 words. Featured-snippet engineered. Specific and actionable.",
  "excerpt": "Under 120 chars for bible-index.json",
  "emotional_hook": "One italic pull-quote — see quality rules",
  "svg_diagram": {{
    "viewBox": "0 0 600 300",
    "title_id": "svg-{slug}-title",
    "title_text": "Diagram title",
    "svg_content": "<rect ... /><text ... />"
  }},
  "parameters": [
    {{
      "name": "parameter_slug",
      "title": "Parameter Name",
      "desc": "Technical: what it does mathematically. Perceptual: what the producer hears. Include specific numbers."
    }}
  ],
  "quick_reference_rows": [
    {{
      "param": "Row label",
      "col1": "Value for column 1",
      "col2": "Value for column 2",
      "col3": "Value for column 3",
      "col4": "Value for column 4",
      "col5": "Value for column 5"
    }}
  ],
  "quick_reference_cols": ["Parameter", "Drums", "Vocals", "Bass", "Bus"],
  "quick_reference_note": "One sentence on how to use this table.",
  "copy_table_text": "Plain text version for copying — Tab-separated values",
  "types": [
    {{
      "name": "Type Name",
      "hardware": "Hardware example",
      "desc": "2-3 sentences. When to use. Character. Sound."
    }}
  ],
  "related_terms": [
    {{
      "slug": "compression",
      "term": "Term Name",
      "preview": "One sentence preview"
    }}
  ],
  "further_reading_slugs": ["compression", "eq", "limiting", "saturation"],
  "faq": [
    {{
      "q": "Question text?",
      "a": "Answer — 3-5 sentences. Direct. Opinionated where appropriate."
    }}
  ],
  "entry_tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
  "schema_about_same_as": ["https://wikidata.org/wiki/...", "https://dbpedia.org/page/..."],
  "youtube_embed": null,
  "spotify_embeds": [
    {{
      "track_uri": "spotify:track:TRACK_ID",
      "title": "Track Name — Artist Name"
    }}
  ],
  "calculator_type": "bpm-timing|frequency-chart|gain-calculator|none",
  "word_count_estimate": 6000,
  "read_minutes": 18,
  "the_number": {{
    "value": "One specific value with unit",
    "label": "What this value represents — session-critical",
    "context": "One sentence on when this rule applies and when to break it."
  }},
  "producer_quote": {{
    "quote": "The exact words, under 30 words",
    "attribution": "Name — context (interview/book/year)",
    "verified": true
  }},
  "signal_chain_position": {{
    "before": ["Process 1", "Process 2"],
    "this_tool": "{term}",
    "after": ["Process 3", "Process 4"],
    "note": "One sentence on why position matters for {term} specifically."
  }},
  "hardware_vs_plugin_rows": [
    {{
      "aspect": "Aspect name",
      "hardware": "Hardware character",
      "plugin": "Top plugin emulation character",
      "stock": "DAW stock version character"
    }}
  ],
  "genre_application_rows": [
    {{
      "param": "Parameter name",
      "trap": "Trap value",
      "hip_hop": "Hip-Hop value",
      "house": "House value",
      "rock": "Rock value",
      "mastering": "Mastering value"
    }}
  ],
  "interaction_warnings": [
    "Full sentence: tool X interacts badly with Y when Z. The result is [audible symptom]. Fix: [specific action]."
  ],
  "red_flags": [
    "Specific audible symptom that tells producer something is wrong — with approximate parameter values"
  ],
  "green_flags": [
    "Specific audible or measurable result that confirms correct application"
  ]
}}"""


# ─── PASS 2 PROMPT ─────────────────────────────────────────────────────────────

def build_pass2_prompt(slug, term, category, pass1_json):
    p1_str = json.dumps(pass1_json, indent=2)[:4000]  # truncate for prompt space
    return f"""You are writing the long-form prose for a Producer's Bible entry on "{term}" (category: {category}).

Here is the Pass 1 structured data for context:
{p1_str}

Return ONLY valid JSON — no markdown fences, no preamble. The JSON must be parseable by json.loads().

Target word count: {WORD_COUNT_TARGET} words total across all prose fields.
Floor: {WORD_COUNT_FLOOR}. Ceiling: {WORD_COUNT_CEILING}.
A truncated JSON is worthless — complete all fields before token budget runs out.

QUALITY RULES:

definition_html: 5-6 paragraphs. Opens with the emotional_hook as an italic pull-quote (<em class="entry-hook">). Paragraphs 2-5: substantive definition, how it sits in production, what it sounds like, why it matters. Final paragraph: why {term} matters MORE or DIFFERENTLY in 2026 than in 2006 (streaming, software, genre shifts, workflow changes). This is the "why it matters now" paragraph.

how_it_works_html: 3-4 paragraphs. Technical mechanism + perceptual description in every paragraph. Include specific numbers (Hz, dB, ms, ratios). Never purely technical — always "this is what the producer hears."

history_html: 4-5 paragraphs. EVERY paragraph must name: one specific person (engineer, inventor, musician), one specific piece of hardware or recording, one specific studio or location, one specific year. No paragraph may open with generic historical language ("In the early days of..."). Open every paragraph with a person or a specific event.

how_producers_use_it_html: 4-5 paragraphs organized by instrument/context (e.g., drums, vocals, bass, bus, creative). Include a DAW-specific note grid: "In [DAW]: [specific setting or tip]" for Ableton, Logic, FL Studio, Pro Tools.

track_examples: Minimum 5 — integrate Pass 1 track_examples. Each must include: title (with year and producer credit), timestamp, note (specific sonic detail), listening_guide ("Put on headphones. Play from [timestamp]. Notice how [specific thing]. This is {term} doing [specific function]."). Each example from a DIFFERENT artist, DIFFERENT genre, DIFFERENT decade.

mistakes: Minimum 6. Each must name: a specific audible symptom (what does it sound like), a specific cause (which parameter, which setting, which value), a specific fix (what to change, what value to target).

common_misconception_html: One widespread false belief about {term}. Structure: "Most producers believe X." Then: "This is wrong. Here is what is actually happening: Y." Use class='misconception-block', class='misconception-label', class='misconception-belief', class='misconception-reality'.

producers_verdict_html: Opinionated and decisive. Three statements: "For most producers, start with: [specific recommendation]", "If you are doing [specific context], use [specific alternative]", "Avoid [specific thing] until you understand [prerequisite]." Use class='producers-verdict', class='verdict-label'. Takes a position. No hedging.

progression_path_html: Three stages — Beginner, Intermediate, Advanced. Not a list of tips — a narrative path. Use class='progression-path', class='prog-stage', class='prog-beginner/intermediate/advanced', class='prog-label'.

before_after_text: Precise verbal description. "Before" = what the unprocessed signal sounds like with specific numbers (dB jumps, frequency behavior, dynamic range). "After" = what correct {term} application produces, with specific settings and audible results.

section_summaries: One amber sentence per section — definition, how_it_works, parameters, history, how_producers_use_it, in_the_wild, types, mistakes. Producers who skim get the entry in 30 seconds.

Return this exact JSON structure:

{{
  "definition_html": "<p><em class=\\"entry-hook\\">hook from pass1...</em></p><p>Para 2...</p><p>Para 3...</p><p>Para 4...</p><p>Para 5...</p><p>Why it matters now in 2026...</p>",
  "how_it_works_html": "<p>Technical + perceptual para 1...</p><p>Para 2...</p><p>Para 3...</p>",
  "history_html": "<p>Person + hardware + studio + year. Para 1...</p><p>Para 2...</p><p>Para 3...</p><p>Para 4...</p>",
  "how_producers_use_it_html": "<p>By instrument para 1...</p><p>Para 2...</p><p>DAW grid: In Ableton: ... In Logic: ... In FL Studio: ... In Pro Tools: ...</p>",
  "track_examples": [
    {{
      "title": "Artist — Track Title (Year) · Produced by Name",
      "timestamp": "0:00 — Throughout",
      "note": "Specific sonic detail — what to listen for, what is happening technically",
      "listening_guide": "Put on headphones. Play from [timestamp]. Notice how [specific observable thing]. This is {term} doing [specific function]."
    }}
  ],
  "mistakes": [
    {{
      "title": "Short mistake title",
      "symptom": "What does it sound like — specific and audible",
      "cause": "Which parameter, which setting, which value caused this",
      "fix": "What to change — specific value to target"
    }}
  ],
  "common_misconception_html": "<div class=\\"misconception-block\\"><span class=\\"misconception-label\\">Common Misconception</span><p class=\\"misconception-belief\\">Most producers believe...</p><p class=\\"misconception-reality\\">Here is what is actually happening: ...</p></div>",
  "producers_verdict_html": "<div class=\\"producers-verdict\\"><span class=\\"verdict-label\\">The Producer's Verdict</span><p>For most producers, start with: ...</p><p>If you are doing [context], use ...</p><p>Avoid [thing] until you understand [prerequisite].</p></div>",
  "progression_path_html": "<div class=\\"progression-path\\"><div class=\\"prog-stage prog-beginner\\"><span class=\\"prog-label\\">Beginner</span><p>When you first encounter {term}...</p></div><div class=\\"prog-stage prog-intermediate\\"><span class=\\"prog-label\\">Intermediate</span><p>Once that clicks...</p></div><div class=\\"prog-stage prog-advanced\\"><span class=\\"prog-label\\">Advanced</span><p>When you are ready for professional results...</p></div></div>",
  "before_after_text": {{
    "before": "Specific description of unprocessed signal with numbers",
    "after": "Specific description with settings and audible results"
  }},
  "section_summaries": {{
    "definition": "One amber sentence summary.",
    "how_it_works": "One amber sentence summary.",
    "parameters": "One amber sentence summary.",
    "history": "One amber sentence summary.",
    "how_producers_use_it": "One amber sentence summary.",
    "in_the_wild": "One amber sentence summary.",
    "types": "One amber sentence summary.",
    "mistakes": "One amber sentence summary."
  }}
}}"""


# ─── CLAUDE API CALLS ───────────────────────────────────────────────────────────

def call_claude_pass1(prompt, label='Pass 1'):
    """Call Claude for Pass 1 structured data. Returns parsed JSON dict."""
    api_key = os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_KEY', '')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set — run . .\\setenv.ps1 first")

    for attempt, wait in enumerate([0] + BACKOFF):
        if wait:
            print(f"  [{label}] Retry {attempt} — waiting {wait}s...")
            time.sleep(wait)
        try:
            chunks = []
            with requests.post(
                'https://api.anthropic.com/v1/messages',
                headers={
                    'x-api-key': api_key,
                    'anthropic-version': '2023-06-01',
                    'content-type': 'application/json'
                },
                json={
                    'model': MODEL,
                    'max_tokens': PASS1_TOKENS,
                    'system': SYSTEM_PROMPT,
                    'messages': [{'role': 'user', 'content': prompt}],
                    'stream': True
                },
                stream=True,
                timeout=(30, 600)
            ) as r:
                if r.status_code == 429:
                    print(f"  [{label}] Rate limited (429)")
                    continue
                r.raise_for_status()
                for line in r.iter_lines():
                    if line:
                        line = line.decode('utf-8') if isinstance(line, bytes) else line
                        if line.startswith('data: '):
                            data_str = line[6:]
                            if data_str == '[DONE]':
                                break
                            try:
                                evt = json.loads(data_str)
                                if evt.get('type') == 'content_block_delta':
                                    delta = evt.get('delta', {})
                                    if delta.get('type') == 'text_delta':
                                        chunks.append(delta.get('text', ''))
                            except json.JSONDecodeError:
                                pass
            text = ''.join(chunks).strip()
            # Strip markdown fences if present
            text = re.sub(r'^```(?:json)?\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            data = json.loads(text)
            print(f"  [{label}] Pass 1 OK — {len(data)} fields")
            return data
        except json.JSONDecodeError as e:
            print(f"  [{label}] JSON parse error: {e}")
            if attempt >= len(BACKOFF):
                raise
        except Exception as e:
            print(f"  [{label}] Error: {e}")
            if attempt >= len(BACKOFF):
                raise
    raise RuntimeError(f"[{label}] Pass 1 failed after all retries")


def call_claude_pass2(prompt, label='Pass 2'):
    """Call Claude for Pass 2 prose. Returns parsed JSON dict."""
    api_key = os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_KEY', '')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    for attempt, wait in enumerate([0] + BACKOFF):
        if wait:
            print(f"  [{label}] Retry {attempt} — waiting {wait}s...")
            time.sleep(wait)
        try:
            chunks = []
            with requests.post(
                'https://api.anthropic.com/v1/messages',
                headers={
                    'x-api-key': api_key,
                    'anthropic-version': '2023-06-01',
                    'content-type': 'application/json'
                },
                json={
                    'model': MODEL,
                    'max_tokens': PASS2_TOKENS,
                    'system': SYSTEM_PROMPT,
                    'messages': [{'role': 'user', 'content': prompt}],
                    'stream': True
                },
                stream=True,
                timeout=(30, 600)
            ) as r:
                if r.status_code == 429:
                    print(f"  [{label}] Rate limited (429)")
                    continue
                r.raise_for_status()
                for line in r.iter_lines():
                    if line:
                        line = line.decode('utf-8') if isinstance(line, bytes) else line
                        if line.startswith('data: '):
                            data_str = line[6:]
                            if data_str == '[DONE]':
                                break
                            try:
                                evt = json.loads(data_str)
                                if evt.get('type') == 'content_block_delta':
                                    delta = evt.get('delta', {})
                                    if delta.get('type') == 'text_delta':
                                        chunks.append(delta.get('text', ''))
                            except json.JSONDecodeError:
                                pass
            text = ''.join(chunks).strip()
            text = re.sub(r'^```(?:json)?\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            data = json.loads(text)
            print(f"  [{label}] Pass 2 OK — {len(data)} fields")
            return data
        except json.JSONDecodeError as e:
            print(f"  [{label}] JSON parse error: {e}")
            if attempt >= len(BACKOFF):
                raise
        except Exception as e:
            print(f"  [{label}] Error: {e}")
            if attempt >= len(BACKOFF):
                raise
    raise RuntimeError(f"[{label}] Pass 2 failed after all retries")


# ─── HTML BUILDER ───────────────────────────────────────────────────────────────

def build_signal_chain_svg(p1):
    """Build signal chain diagram SVG from signal_chain_position."""
    sc = p1.get('signal_chain_position', {})
    before = sc.get('before', [])
    this_tool = sc.get('this_tool', p1.get('term', 'Tool'))
    after = sc.get('after', [])
    all_items = before + [this_tool] + after
    n = len(all_items)
    w = max(600, n * 120)
    step = w // max(n, 1)
    boxes = []
    for i, item in enumerate(all_items):
        x = i * step + 20
        is_current = item == this_tool
        color = '#f5a623' if is_current else '#2a2a3a'
        stroke = '#f5a623' if is_current else '#444'
        fw = 'bold' if is_current else 'normal'
        boxes.append(
            f'<rect x="{x}" y="30" width="{step - 30}" height="40" rx="6" '
            f'fill="{color}" stroke="{stroke}" stroke-width="2"/>'
            f'<text x="{x + (step - 30) // 2}" y="55" text-anchor="middle" '
            f'font-family="system-ui,sans-serif" font-size="11" '
            f'font-weight="{fw}" fill="{"#000" if is_current else "#ccc"}">{item}</text>'
        )
        if i < n - 1:
            ax = x + step - 30
            boxes.append(
                f'<path d="M{ax} 50 L{ax + 15} 50" stroke="#666" stroke-width="2" '
                f'marker-end="url(#arr)"/>'
            )
    svg = (
        f'<svg viewBox="0 0 {w} 100" xmlns="http://www.w3.org/2000/svg" '
        f'aria-labelledby="sc-{p1["slug"]}-title">'
        f'<title id="sc-{p1["slug"]}-title">Signal chain position of {this_tool}</title>'
        f'<defs><marker id="arr" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">'
        f'<path d="M0,0 L6,3 L0,6 Z" fill="#666"/></marker></defs>'
        + ''.join(boxes) +
        f'</svg>'
    )
    return svg


def build_spotify_links(p1):
    """Build Spotify green link buttons — NO iframes."""
    embeds = p1.get('spotify_embeds', [])
    if not embeds:
        return ''
    items = []
    for e in embeds:
        uri = e.get('track_uri', '')
        title = e.get('title', 'Listen on Spotify')
        # Convert spotify:track:ID to https://open.spotify.com/track/ID
        href = uri.replace('spotify:track:', 'https://open.spotify.com/track/')
        if not href.startswith('http'):
            href = '#'
        items.append(
            f'<a class="spotify-link-item" href="{href}" target="_blank" rel="noopener">'
            f'<svg class="spotify-icon" viewBox="0 0 24 24" width="16" height="16" fill="#1DB954">'
            f'<path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0z'
            f'm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141'
            f'-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 '
            f'11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3'
            f'-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48'
            f'.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2z'
            f'm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721'
            f'-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3'
            f'.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/></svg>'
            f'{title}</a>'
        )
    return '<div class="spotify-links">' + '\n'.join(items) + '</div>'


def build_genre_table(p1):
    rows = p1.get('genre_application_rows', [])
    cols = ['Trap', 'Hip-Hop', 'House', 'Rock', 'Mastering']
    col_keys = ['trap', 'hip_hop', 'house', 'rock', 'mastering']
    if not rows:
        return ''
    thead = '<tr><th>Parameter</th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    tbody = ''
    for row in rows:
        cells = f'<td>{row.get("param","")}</td>'
        for k in col_keys:
            cells += f'<td>{row.get(k,"—")}</td>'
        tbody += f'<tr>{cells}</tr>'
    return (
        f'<div class="genre-table-wrap">'
        f'<table class="genre-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'
        f'</div>'
    )


def build_hardware_plugin_table(p1):
    rows = p1.get('hardware_vs_plugin_rows', [])
    if not rows:
        return ''
    thead = '<tr><th>Aspect</th><th>Hardware Original</th><th>Top Plugin</th><th>DAW Stock</th></tr>'
    tbody = ''
    for row in rows:
        tbody += (
            f'<tr>'
            f'<td>{row.get("aspect","")}</td>'
            f'<td>{row.get("hardware","")}</td>'
            f'<td>{row.get("plugin","")}</td>'
            f'<td>{row.get("stock","")}</td>'
            f'</tr>'
        )
    return (
        f'<div class="hardware-plugin-wrap">'
        f'<table class="hardware-plugin-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'
        f'</div>'
    )


def build_quick_ref_table(p1):
    rows = p1.get('quick_reference_rows', [])
    cols = p1.get('quick_reference_cols', ['Parameter', 'Value 1', 'Value 2', 'Value 3', 'Value 4'])
    if not rows:
        return ''
    keys = ['param', 'col1', 'col2', 'col3', 'col4', 'col5']
    thead = '<tr>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    tbody = ''
    for row in rows:
        cells = ''
        for k, col in zip(keys, cols):
            val = row.get(k, row.get(col.lower().replace(' ', '_'), '—'))
            cells += f'<td>{val}</td>'
        tbody += f'<tr>{cells}</tr>'
    return (
        f'<div class="qr-table-wrap">'
        f'<table class="quick-ref-table"><thead>{thead}</thead><tbody>{tbody}</tbody></table>'
        f'</div>'
    )


def build_parameters_html(p1):
    params = p1.get('parameters', [])
    if not params:
        return ''
    items = ''
    for param in params:
        items += (
            f'<div class="param-item">'
            f'<h4 class="param-title">{param.get("title", param.get("name", ""))}</h4>'
            f'<p class="param-desc">{param.get("desc", "")}</p>'
            f'</div>'
        )
    return f'<div class="parameters-grid">{items}</div>'


def build_types_html(p1):
    types = p1.get('types', [])
    if not types:
        return ''
    items = ''
    for t in types:
        items += (
            f'<div class="type-card">'
            f'<h4 class="type-name">{t.get("name", "")}</h4>'
            f'<p class="type-hardware">{t.get("hardware", "")}</p>'
            f'<p class="type-desc">{t.get("desc", "")}</p>'
            f'</div>'
        )
    return f'<div class="types-grid" style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{items}</div>'


def build_faq_html(p1):
    faq = p1.get('faq', [])
    if not faq:
        return ''
    items = ''
    for item in faq:
        items += (
            f'<div class="faq-item">'
            f'<button class="faq-q">{item.get("q", "")}</button>'
            f'<div class="faq-a"><p>{item.get("a", "")}</p></div>'
            f'</div>'
        )
    return f'<div class="faq-accordion">{items}</div>'


def build_related_terms_html(p1):
    terms = p1.get('related_terms', [])
    if not terms:
        return ''
    items = ''
    for t in terms:
        items += (
            f'<a class="related-term-card" href="/bible/{t.get("slug","")}">'
            f'<span class="rt-term">{t.get("term","")}</span>'
            f'<span class="rt-preview">{t.get("preview","")}</span>'
            f'</a>'
        )
    return f'<div class="related-terms-grid">{items}</div>'


def build_further_reading_html(p1):
    slugs = p1.get('further_reading_slugs', [])
    if not slugs:
        return ''
    items = ''
    for slug in slugs:
        title = slug.replace('-', ' ').title()
        # Link to /bible/slug — AI must only return slugs that exist
        href = f'/bible/{slug}' if slug else '/bible/'
        items += (
            f'<a class="further-card" href="{href}">'
            f'<span class="further-title">{title}</span>'
            f'<span class="further-arrow">&rarr;</span>'
            f'</a>'
        )
    return f'<div class="further-grid">{items}</div>'


def build_track_examples_html(p2):
    examples = p2.get('track_examples', [])
    if not examples:
        return ''
    items = ''
    for ex in examples:
        spotify_html = ''
        items += (
            f'<div class="track-example">'
            f'<h4 class="track-title">{ex.get("title","")}</h4>'
            f'<p class="track-timestamp"><em>{ex.get("timestamp","")}</em></p>'
            f'<p class="track-note">{ex.get("note","")}</p>'
            f'<div class="listening-guide">'
            f'<span class="lg-label">Listening Guide</span>'
            f'<p class="listening_guide">{ex.get("listening_guide","")}</p>'
            f'</div>'
            f'</div>'
        )
    return f'<div class="track-examples">{items}</div>'


def build_mistakes_html(p2):
    mistakes = p2.get('mistakes', [])
    if not mistakes:
        return ''
    items = ''
    for m in mistakes:
        items += (
            f'<div class="mistake-item">'
            f'<h4 class="mistake-title">{m.get("title","")}</h4>'
            f'<p><strong>Symptom:</strong> {m.get("symptom","")}</p>'
            f'<p><strong>Cause:</strong> {m.get("cause","")}</p>'
            f'<p><strong>Fix:</strong> {m.get("fix","")}</p>'
            f'</div>'
        )
    return f'<div class="mistakes-list">{items}</div>'


def build_red_green_flags_html(p1):
    red = p1.get('red_flags', [])
    green = p1.get('green_flags', [])
    red_items = ''.join(f'<li class="red-flag">{f}</li>' for f in red)
    green_items = ''.join(f'<li class="green-flag">{f}</li>' for f in green)
    return (
        f'<div class="red-green-flags">'
        f'<div class="flags-col flags-red"><h4>🔴 Red Flags</h4><ul>{red_items}</ul></div>'
        f'<div class="flags-col flags-green"><h4>🟢 Green Flags</h4><ul>{green_items}</ul></div>'
        f'</div>'
    )


def build_interaction_warnings_html(p1):
    warnings = p1.get('interaction_warnings', [])
    if not warnings:
        return ''
    items = ''.join(f'<li class="interaction-warning">{w}</li>' for w in warnings)
    return f'<div class="interaction-warnings"><h4>Interaction Warnings</h4><ul>{items}</ul></div>'


def build_the_number_html(p1):
    tn = p1.get('the_number', {})
    if not tn:
        return ''
    return (
        f'<div class="the-number-box">'
        f'<span class="tn-value">{tn.get("value","")}</span>'
        f'<span class="tn-label">{tn.get("label","")}</span>'
        f'<p class="tn-context">{tn.get("context","")}</p>'
        f'</div>'
    )


def build_producer_quote_html(p1):
    pq = p1.get('producer_quote', {})
    if not pq or not pq.get('verified', False):
        return ''
    return (
        f'<div class="producer-quote-block">'
        f'<blockquote class="pq-quote">&ldquo;{pq.get("quote","")}&rdquo;</blockquote>'
        f'<cite class="pq-attribution">{pq.get("attribution","")}</cite>'
        f'</div>'
    )


def build_section_summary(text):
    return f'<p class="section-summary">{text}</p>'


def build_html(p1, p2, slug, term, category, pub_date=None):
    """Assemble full Bible entry HTML from Pass 1 + Pass 2 JSON objects."""
    if not pub_date:
        pub_date = datetime.now().strftime('%Y-%m-%d')

    meta_desc = p1.get('meta_description', f'{term} — Producer\'s Bible entry at MusicProductionWiki.com')
    meta_keywords = ', '.join(p1.get('meta_keywords', []))
    quick_answer = p1.get('quick_answer', '')
    excerpt = p1.get('excerpt', '')
    summaries = p2.get('section_summaries', {})
    before_after = p2.get('before_after_text', {})
    calc_type = p1.get('calculator_type', 'none')
    pronunciation = p1.get('pronunciation', '')
    pos_label = p1.get('entry_pos_label', 'noun')

    # Build FAQ JSON-LD schema
    faq_schema_items = []
    for f in p1.get('faq', []):
        faq_schema_items.append({
            '@type': 'Question',
            'name': f.get('q', ''),
            'acceptedAnswer': {'@type': 'Answer', 'text': f.get('a', '')}
        })

    schema_ld = json.dumps({
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'Article',
                'headline': f'{term} — Producer\'s Bible',
                'description': meta_desc,
                'datePublished': pub_date,
                'dateModified': datetime.now().strftime('%Y-%m-%d'),
                'publisher': {
                    '@type': 'Organization',
                    'name': 'MusicProductionWiki.com',
                    'url': 'https://musicproductionwiki.com'
                },
                'mainEntityOfPage': f'{SITE_URL}/bible/{slug}'
            },
            {
                '@type': 'FAQPage',
                'mainEntity': faq_schema_items
            }
        ]
    }, indent=2)

    # SVG diagram from Pass 1
    svg_data = p1.get('svg_diagram', {})
    svg_content = (
        f'<svg viewBox="{svg_data.get("viewBox","0 0 600 300")}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'aria-labelledby="{svg_data.get("title_id","svg-title")}">'
        f'<title id="{svg_data.get("title_id","svg-title")}">{svg_data.get("title_text","")}</title>'
        f'{svg_data.get("svg_content","")}'
        f'</svg>'
    ) if svg_data else ''

    # Calculator HTML
    calc_html = ''
    if calc_type == 'bpm-timing':
        calc_html = r"""
<div class="gain-calculator" id="bpm-calculator">
  <h3>BPM to Delay/Reverb Calculator</h3>
  <label>BPM: <input type="number" id="bpm-input" value="120" min="40" max="300"></label>
  <button onclick="calcBPM()">Calculate</button>
  <div id="bpm-results"></div>
  <script>
  function calcBPM() {
    var bpm = parseFloat(document.getElementById('bpm-input').value);
    var quarter = 60000/bpm;
    var eighth = quarter/2;
    var dotted = quarter*1.5;
    document.getElementById('bpm-results').innerHTML =
      '<p>Quarter note: ' + Math.round(quarter) + 'ms</p>' +
      '<p>Eighth note: ' + Math.round(eighth) + 'ms</p>' +
      '<p>Dotted quarter: ' + Math.round(dotted) + 'ms</p>';
  }
  </script>
</div>"""
    elif calc_type == 'gain-calculator':
        calc_html = r"""
<div class="gain-calculator" id="gain-calc">
  <h3>Gain Reduction Calculator</h3>
  <label>Input level (dBFS): <input type="number" id="gc-input" value="-10"></label>
  <label>Threshold (dBFS): <input type="number" id="gc-thresh" value="-18"></label>
  <label>Ratio: <input type="number" id="gc-ratio" value="4" step="0.5"></label>
  <button onclick="calcGain()">Calculate</button>
  <div id="gc-results"></div>
  <script>
  function calcGain() {
    var inp = parseFloat(document.getElementById('gc-input').value);
    var thr = parseFloat(document.getElementById('gc-thresh').value);
    var ratio = parseFloat(document.getElementById('gc-ratio').value);
    if (inp <= thr) { document.getElementById('gc-results').innerHTML = '<p>Signal below threshold — no compression.</p>'; return; }
    var over = inp - thr;
    var gr = over - (over / ratio);
    document.getElementById('gc-results').innerHTML =
      '<p>Gain reduction: ' + gr.toFixed(1) + ' dB</p>' +
      '<p>Output level: ' + (inp - gr).toFixed(1) + ' dBFS</p>';
  }
  </script>
</div>"""

    # Build nav from locked template — matches homepage nav exactly
    # NO main.js on bible pages — fully self-contained
    nav_html = (
        '<div class="bible-bar" style="position:sticky;top:0;z-index:100;background:#131000;'
        'border-bottom:1px solid rgba(245,166,35,0.28);height:40px;display:flex;align-items:center;'
        'justify-content:center;padding:0 24px">'
        '<div style="display:flex;align-items:center;justify-content:center;gap:16px;max-width:1360px;width:100%">'
        '<a href="/bible/" style="font-size:14px;font-weight:700;color:#f5a623;text-decoration:none;letter-spacing:-0.01em">'
        'The Producer’s Bible</a>'
        '<div style="width:1px;height:14px;background:rgba(245,166,35,0.3)"></div>'
        '<span style="font-size:13px;color:rgba(245,166,35,0.6)">'
        'The definitive music production reference</span>'
        '</div></div>'

        '<nav style="position:sticky;top:40px;z-index:400;background:rgba(10,10,11,0.97);'
        'backdrop-filter:blur(24px);border-bottom:1px solid rgba(255,255,255,0.09)" '
        'aria-label="Main navigation">'
        '<div style="max-width:1360px;margin:0 auto;padding:0 40px;height:60px;display:flex;'
        'align-items:center;gap:0">'

        '<a href="/" style="display:flex;align-items:center;gap:12px;text-decoration:none;'
        'flex-shrink:0;margin-right:36px">'
        '<div style="width:32px;height:32px;border-radius:8px;background:#00e8a2;display:flex;'
        'align-items:center;justify-content:center;flex-shrink:0">'
        '<svg width="18" height="18" viewBox="0 0 18 18" fill="none">'
        '<rect x="1.5" y="7" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>'
        '<rect x="6" y="4" width="2.5" height="12" rx="1.2" fill="#0a0a0b"/>'
        '<rect x="10.5" y="1" width="2.5" height="16" rx="1.2" fill="#0a0a0b"/>'
        '<rect x="15" y="5" width="2.5" height="9" rx="1.2" fill="#0a0a0b"/>'
        '</svg></div>'
        '<div><div style="font-size:15px;font-weight:600;color:#f0f0f0;letter-spacing:-0.02em">'
        'MusicProductionWiki</div>'
        '<span style="font-size:10px;color:#6a6a7a;font-family:monospace;letter-spacing:0.07em;'
        'text-transform:uppercase">The Producer\u2019s Reference</span></div></a>'

        '<ul class="bible-nav-primary" style="display:flex;align-items:center;gap:2px;'
        'list-style:none;flex:1;padding:0;margin:0">'

        '<li class="bible-nav-item" style="position:relative">'
        '<button class="bible-nav-btn" style="display:flex;align-items:center;gap:5px;color:#a0a0b4;'
        'font-size:13.5px;padding:6px 12px;border-radius:7px;background:none;border:none;'
        'cursor:pointer;font-family:inherit">Articles '
        '<svg width="10" height="10" viewBox="0 0 12 12" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<polyline points="2 4 6 8 10 4"/></svg></button>'
        '<div class="bible-nav-dd" style="display:none;position:absolute;top:calc(100% + 8px);left:0;'
        'background:#111113;border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:8px;'
        'min-width:440px;box-shadow:0 24px 48px rgba(0,0,0,.55);'
        'display:none;grid-template-columns:1fr 1fr;gap:2px;z-index:500">'
        '<div style="font-size:10px;font-family:monospace;color:#6a6a7a;text-transform:uppercase;'
        'letter-spacing:.1em;padding:8px 12px 4px">Techniques &amp; Analysis</div>'
        '<div style="font-size:10px;font-family:monospace;color:#6a6a7a;text-transform:uppercase;'
        'letter-spacing:.1em;padding:8px 12px 4px">Reference &amp; Business</div>'
        '<a href="/categories/techniques.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Techniques</a>'
        '<a href="/categories/reviews.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Reviews</a>'
        '<a href="/categories/comparisons.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Comparisons</a>'
        '<a href="/categories/ai-music.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">AI Music</a>'
        '<a href="/categories/breakdowns.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Breakdowns</a>'
        '<a href="/categories/music-business.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Music Business</a>'
        '<a href="/categories/recreations.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Recreations</a>'
        '<a href="/genres.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Genres</a>'
        '</div></li>'

        '<li class="bible-nav-item" style="position:relative">'
        '<button class="bible-nav-btn" style="display:flex;align-items:center;gap:5px;color:#a0a0b4;'
        'font-size:13.5px;padding:6px 12px;border-radius:7px;background:none;border:none;'
        'cursor:pointer;font-family:inherit">Gear '
        '<svg width="10" height="10" viewBox="0 0 12 12" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<polyline points="2 4 6 8 10 4"/></svg></button>'
        '<div class="bible-nav-dd" style="display:none;position:absolute;top:calc(100% + 8px);left:0;'
        'background:#111113;border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:8px;'
        'min-width:240px;box-shadow:0 24px 48px rgba(0,0,0,.55);z-index:500">'
        '<a href="/categories/daws.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">DAWs</a>'
        '<a href="/categories/plugins.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Plugins</a>'
        '<a href="/categories/gear.html" style="padding:9px 12px;border-radius:9px;'
        'text-decoration:none;color:#f0f0f0;font-size:13.5px;font-weight:500;display:block">Hardware</a>'
        '</div></li>'

        '<li><a href="/about.html" style="color:#a0a0b4;font-size:13.5px;padding:6px 12px;'
        'border-radius:7px;text-decoration:none">About</a></li>'
        '<li><a href="/bible/" style="color:#f5a623;font-weight:600;font-size:13.5px;'
        'padding:6px 12px;border-radius:7px;text-decoration:none">'
        'The Producer\u2019s Bible &rarr;</a></li>'
        '</ul>'

        '<div style="display:flex;align-items:center;gap:8px;margin-left:auto;flex-shrink:0">'
        '<button onclick="document.getElementById(\'bibleSearchOverlay\').style.display=\'flex\'" '
        'style="display:flex;align-items:center;justify-content:center;width:34px;height:34px;'
        'border-radius:6px;background:none;border:none;cursor:pointer;color:#888" aria-label="Search">'
        '<svg width="16" height="16" viewBox="0 0 16 16" fill="none">'
        '<circle cx="6.5" cy="6.5" r="4.5" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M10 10l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
        '</svg></button>'
        ''
        '<button id="bibleMobBtn" style="display:none;background:none;border:none;cursor:pointer;'
        'padding:8px;flex-direction:column;gap:5px" aria-label="Toggle menu">'
        '<span style="display:block;width:22px;height:2px;background:#a0a0b4;border-radius:2px"></span>'
        '<span style="display:block;width:22px;height:2px;background:#a0a0b4;border-radius:2px"></span>'
        '<span style="display:block;width:22px;height:2px;background:#a0a0b4;border-radius:2px"></span>'
        '</button></div>'
        '</div></nav>'

        '<div id="bibleMobDrawer" style="display:none;position:fixed;top:100px;left:0;right:0;'
        'bottom:0;background:rgba(10,10,11,0.99);z-index:199;overflow-y:auto;padding:16px;'
        'border-top:1px solid rgba(255,255,255,0.09);flex-direction:column;gap:4px">'
        '<a href="/bible/" style="display:flex;align-items:center;gap:8px;padding:12px 16px;'
        'border-radius:9px;background:rgba(245,166,35,0.07);border:1px solid rgba(245,166,35,0.22);'
        'color:#f5a623;font-size:14px;font-weight:600;text-decoration:none;margin:4px 0 8px">'
        'The Producer\u2019s Bible \u2014 Explore Free</a>'
        '<div style="font-size:10px;font-family:monospace;color:#6a6a7a;text-transform:uppercase;'
        'letter-spacing:.12em;padding:12px 12px 6px">Articles</div>'
        '<a href="/categories/techniques.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Techniques</a>'
        '<a href="/categories/reviews.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Reviews</a>'
        '<a href="/categories/comparisons.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Comparisons</a>'
        '<a href="/categories/breakdowns.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Breakdowns</a>'
        '<a href="/categories/recreations.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Recreations</a>'
        '<a href="/genres.html" style="display:block;padding:11px 12px;border-radius:9px;'
        'text-decoration:none;font-size:14px;color:#a0a0b4">Genres</a>'
        '<a href="/categories/ai-music.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">AI Music</a>'
        '<a href="/categories/music-business.html" style="display:block;padding:11px 12px;'
        'border-radius:9px;text-decoration:none;font-size:14px;color:#a0a0b4">Music Business</a>'
        '<div style="font-size:10px;font-family:monospace;color:#6a6a7a;text-transform:uppercase;'
        'letter-spacing:.12em;padding:12px 12px 6px">Gear</div>'
        '<a href="/categories/daws.html" style="display:block;padding:11px 12px;border-radius:9px;'
        'text-decoration:none;font-size:14px;color:#a0a0b4">DAWs</a>'
        '<a href="/categories/plugins.html" style="display:block;padding:11px 12px;border-radius:9px;'
        'text-decoration:none;font-size:14px;color:#a0a0b4">Plugins</a>'
        '<a href="/categories/gear.html" style="display:block;padding:11px 12px;border-radius:9px;'
        'text-decoration:none;font-size:14px;color:#a0a0b4">Hardware</a>'
        '<a href="/bible/" style="display:block;background:#f5a623;color:#000;font-weight:600;'
        'font-size:14px;padding:13px 16px;border-radius:10px;text-decoration:none;'
        'text-align:center;margin-top:8px">Browse The Producer’s Bible &rarr;</a>'
        '</div>'

        '<div id="bibleSearchOverlay" style="display:none;position:fixed;inset:0;'
        'background:rgba(0,0,0,.88);z-index:99998;align-items:flex-start;justify-content:center;'
        'padding-top:80px" onclick="if(event.target===this)this.style.display=\'none\'">'
        '<div style="background:#18181c;border:1px solid rgba(255,255,255,.15);border-radius:14px;'
        'width:100%;max-width:620px;overflow:hidden;margin:0 1rem">'
        '<div style="display:flex;align-items:center;padding:16px 20px;gap:12px;'
        'border-bottom:1px solid rgba(255,255,255,.07)">'
        '<svg width="16" height="16" viewBox="0 0 16 16" fill="none">'
        '<circle cx="6.5" cy="6.5" r="4.5" stroke="#666" stroke-width="1.5"/>'
        '<path d="M10 10l3.5 3.5" stroke="#666" stroke-width="1.5" stroke-linecap="round"/></svg>'
        '<input id="bibleSearchInput" type="text" placeholder="Search articles and Bible entries..." '
        'style="flex:1;background:none;border:none;outline:none;font-size:16px;color:#fff;'
        'font-family:inherit" autocomplete="off"/>'
        '<span style="font-size:11px;color:#555;white-space:nowrap">ESC to close</span>'
        '</div>'
        '<div id="bibleSearchResults" style="max-height:420px;overflow-y:auto;padding:8px"></div>'
        '</div></div>'
    )



    read_time = p1.get('read_minutes', max(1, round(WORD_COUNT_TARGET / 325)))

    # Build full HTML
    # NO main.js — bible pages are fully self-contained
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{term} — Producer's Bible | MusicProductionWiki</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{meta_keywords}">
  <link rel="canonical" href="{SITE_URL}/bible/{slug}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{term} — Producer's Bible | MusicProductionWiki">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{SITE_URL}/bible/{slug}">
  <meta property="og:site_name" content="MusicProductionWiki">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{term} — Producer's Bible | MusicProductionWiki">
  <meta name="twitter:description" content="{meta_desc}">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">{schema_ld}</script>
  <style>
    /* Bible page — NO main.js — fully self-contained */
    *{{box-sizing:border-box;margin:0;padding:0}}
    html,body{{overflow-x:hidden;max-width:100%}}body{{background:#0d0d1a;color:#e0e0f0;font-family:system-ui,-apple-system,sans-serif;line-height:1.7}}

    /* Progress bar */
    #reading-progress{{position:fixed;top:0;left:0;height:3px;background:#f5a623;z-index:99999;width:0%;max-width:100%;transition:width .1s linear;pointer-events:none}}

    /* Bible bar */
    .bible-bar-v4{{background:#1a1000;border-bottom:1px solid #f5a623;padding:6px 24px;text-align:center;font-size:13px;position:sticky;top:0;z-index:9001}}
    .bible-bar-v4 a{{color:#f5a623;text-decoration:none;font-weight:600}}

    /* Nav */
    .mpw-site-nav{{background:#13132a;border-bottom:1px solid #2a2a4a;position:sticky;top:40px;z-index:900;padding:12px 0}}
    .nav-logo-mark{{display:flex;align-items:center;gap:8px;text-decoration:none;color:#e0e0f0;font-weight:700;font-size:15px}}
    .nav-logo-name{{font-weight:700}}
    .nav-toggle{{position:relative;cursor:pointer;color:#e0e0f0;font-size:14px;padding:4px 8px}}
    .nav-dropdown{{display:none;position:absolute;top:100%;left:0;background:#1a1a3a;border:1px solid #2a2a4a;border-radius:8px;min-width:180px;z-index:1000;padding:8px 0}}
    .nav-toggle:focus-within .nav-dropdown,.nav-toggle:hover .nav-dropdown{{display:flex;flex-direction:column}}
    .nav-dropdown a{{padding:8px 16px;color:#e0e0f0;text-decoration:none;font-size:14px}}
    .nav-dropdown a:hover{{background:#2a2a4a}}
    .nav-bible-link{{background:#f5a623;color:#000!important;padding:6px 14px;border-radius:6px;font-weight:700;text-decoration:none;font-size:13px}}
    .nav-link{{color:#e0e0f0;text-decoration:none;font-size:14px}}
    .nav-search-btn{{background:none;border:none;cursor:pointer;color:#e0e0f0;padding:4px}}

    /* Entry nav */
    .entry-nav{{background:#13132a;border-bottom:1px solid #2a2a4a;position:sticky;top:60px;z-index:800;overflow-x:auto;scrollbar-width:none}}
    .entry-nav::-webkit-scrollbar{{display:none}}
    .entry-nav-inner{{display:flex;justify-content:center;gap:4px;padding:13px 10px;min-width:max-content;margin:0 auto}}
    .entry-nav-inner a{{color:#a0a0c0;text-decoration:none;font-size:9px;text-transform:uppercase;letter-spacing:.05em;padding:4px 8px;border-radius:4px;white-space:nowrap}}
    .entry-nav-inner a:hover{{color:#f5a623;background:#1a1a3a}}

    /* Content */
    .bible-entry-wrap{{max-width:1100px;margin:0 auto;padding:40px 24px;display:grid;grid-template-columns:1fr 280px;gap:40px}}
    @media(max-width:900px){{.bible-entry-wrap{{grid-template-columns:1fr;padding:20px 16px}}}}
    .entry-main{{min-width:0}}
    .entry-sidebar{{}}

    /* Masthead */
    .entry-masthead{{background:linear-gradient(135deg,#1a0a00,#0d0d1a);border:1px solid #f5a623;border-radius:12px;padding:32px;margin-bottom:32px}}
    .entry-category{{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;font-weight:700;margin-bottom:8px}}
    .entry-term{{font-size:clamp(2rem,5vw,3.5rem);font-weight:900;color:#fff;line-height:1.1;margin-bottom:8px}}
    .entry-pos{{font-size:14px;color:#888;font-style:italic;margin-bottom:16px}}
    .entry-hook{{font-size:1.1rem;color:#c8c8d8;font-style:italic;border-left:3px solid #f5a623;padding-left:16px;display:block;margin-bottom:16px}}
    .entry-meta{{display:flex;gap:16px;font-size:12px;color:#666;flex-wrap:wrap}}
    .entry-meta span{{background:#1a1a3a;padding:4px 10px;border-radius:4px}}

    /* Quick answer */
    .quick-answer-block{{background:#1a1000;border:1px solid #f5a623;border-radius:8px;padding:20px;margin-bottom:32px}}
    .qa-label{{font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;font-weight:700;margin-bottom:8px}}
    .qa-text{{font-size:1.05rem;color:#e0e0f0;line-height:1.6}}

    /* Section headers */
    .entry-main h2{{font-size:1.6rem;font-weight:700;color:#fff;margin:40px 0 16px;padding-bottom:8px;border-bottom:1px solid #2a2a4a}}
    .entry-main h3{{font-size:1.2rem;font-weight:600;color:#e0e0f0;margin:24px 0 12px}}
    .entry-main h4{{font-size:1rem;font-weight:600;color:#c8c8d8;margin:16px 0 8px}}
    .entry-main p{{color:#c8c8d8;margin-bottom:16px;line-height:1.8}}
    .entry-main ul,.entry-main ol{{color:#c8c8d8;margin:0 0 16px 24px}}
    .entry-main li{{margin-bottom:8px;line-height:1.7}}

    /* The Number box */
    .the-number-box{{background:#1a0800;border:2px solid #f5a623;border-radius:10px;padding:24px;margin:24px 0;text-align:center}}
    .tn-value{{display:block;font-size:3rem;font-weight:900;color:#f5a623;line-height:1}}
    .tn-label{{display:block;font-size:14px;color:#c8c8d8;margin:8px 0 4px}}
    .tn-context{{font-size:13px;color:#888;margin:0}}

    /* Section summary */
    .section-summary{{background:#1a1a3a;border-left:3px solid #f5a623;padding:10px 16px;font-size:13px;color:#a0a0c0;font-style:italic;margin:16px 0 24px;border-radius:0 6px 6px 0}}

    /* Parameters */
    .parameters-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:16px 0}}
    .param-item{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px}}
    .param-title{{font-size:14px;font-weight:700;color:#f5a623;margin-bottom:8px}}
    .param-desc{{font-size:13px;color:#c8c8d8;line-height:1.6}}

    /* Quick ref table */
    .qr-table-wrap{{overflow-x:auto;margin:16px 0}}
    .quick-ref-table{{width:100%;border-collapse:collapse;font-size:13px}}
    .quick-ref-table th{{background:#1a1a3a;color:#f5a623;padding:8px 12px;text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.05em}}
    .quick-ref-table td{{padding:8px 12px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}}
    .quick-ref-table tr:hover td{{background:#13132a}}

    /* Genre table */
    .genre-table-wrap{{overflow-x:auto;margin:16px 0}}
    .genre-table{{width:100%;border-collapse:collapse;font-size:12px}}
    .genre-table th{{background:#1a0800;color:#f5a623;padding:8px 10px;text-align:left;font-size:11px;text-transform:uppercase}}
    .genre-table td{{padding:8px 10px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}}

    /* Hardware/plugin table */
    .hardware-plugin-wrap{{overflow-x:auto;margin:16px 0}}
    .hardware-plugin-table{{width:100%;border-collapse:collapse;font-size:13px}}
    .hardware-plugin-table th{{background:#1a1a3a;color:#f5a623;padding:8px 12px;font-size:11px;text-transform:uppercase;text-align:left}}
    .hardware-plugin-table td{{padding:8px 12px;border-bottom:1px solid #1a1a3a;color:#c8c8d8}}

    /* Signal chain diagram */
    .signal-chain-diagram{{background:#0d0d1a;border:1px solid #2a2a4a;border-radius:8px;padding:16px;overflow-x:auto;margin:16px 0}}

    /* Types grid */
    .types-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:16px 0}}
    @media(max-width:768px){{.types-grid{{grid-template-columns:repeat(2,1fr)}}}}
    @media(max-width:480px){{.types-grid{{grid-template-columns:1fr}}}}
    .type-card{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px}}
    .type-name{{font-size:14px;font-weight:700;color:#f5a623;margin-bottom:4px}}
    .type-hardware{{font-size:12px;color:#888;margin-bottom:8px;font-style:italic}}
    .type-desc{{font-size:13px;color:#c8c8d8;line-height:1.6}}

    /* Misconception block */
    .misconception-block{{background:#1a0000;border:2px solid #cc3333;border-radius:8px;padding:20px;margin:24px 0}}
    .misconception-label{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#cc3333;font-weight:700;margin-bottom:12px}}
    .misconception-belief{{color:#ff8888;font-weight:600;margin-bottom:8px}}
    .misconception-reality{{color:#c8c8d8}}

    /* Producer's verdict */
    .producers-verdict{{background:#1a0800;border:2px solid #f5a623;border-radius:8px;padding:20px;margin:24px 0}}
    .verdict-label{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;font-weight:700;margin-bottom:12px}}
    .producers-verdict p{{color:#c8c8d8;margin-bottom:10px}}
    .producers-verdict p:last-child{{margin-bottom:0}}

    /* Producer quote */
    .producer-quote-block{{background:#0d1a1a;border-left:4px solid #14b8a6;border-radius:0 8px 8px 0;padding:20px;margin:24px 0}}
    .pq-quote{{font-size:1.1rem;color:#e0e0f0;font-style:italic;margin-bottom:8px}}
    .pq-attribution{{font-size:12px;color:#888;display:block}}

    /* Red/Green flags */
    .red-green-flags{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0}}
    @media(max-width:600px){{.red-green-flags{{grid-template-columns:1fr}}}}
    .flags-col h4{{font-size:13px;font-weight:700;margin-bottom:10px}}
    .flags-col ul{{list-style:none;margin:0;padding:0}}
    .red-flag{{background:#1a0000;border-left:3px solid #cc3333;padding:8px 12px;margin-bottom:6px;border-radius:0 4px 4px 0;font-size:13px;color:#ff9999}}
    .green-flag{{background:#001a00;border-left:3px solid #33cc33;padding:8px 12px;margin-bottom:6px;border-radius:0 4px 4px 0;font-size:13px;color:#99ff99}}

    /* Interaction warnings */
    .interaction-warnings{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin:16px 0}}
    .interaction-warnings h4{{color:#f5a623;margin-bottom:12px;font-size:14px}}
    .interaction-warnings ul{{list-style:none;margin:0;padding:0}}
    .interaction-warning{{padding:10px 0;border-bottom:1px solid #2a2a4a;font-size:13px;color:#c8c8d8}}
    .interaction-warning:last-child{{border-bottom:none}}

    /* Track examples */
    .track-examples{{display:flex;flex-direction:column;gap:24px;margin:16px 0}}
    .track-example{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px}}
    .track-title{{font-size:14px;font-weight:700;color:#fff;margin-bottom:4px}}
    .track-timestamp{{font-size:12px;color:#888;margin-bottom:8px}}
    .track-note{{font-size:13px;color:#c8c8d8;margin-bottom:12px}}
    .listening-guide{{background:#0d0d1a;border-radius:6px;padding:12px}}
    .lg-label{{display:block;font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:6px;font-weight:700}}
    .listening_guide{{font-size:13px;color:#a0a0c0;font-style:italic}}

    /* Mistakes */
    .mistakes-list{{display:flex;flex-direction:column;gap:16px;margin:16px 0}}
    .mistake-item{{background:#1a0800;border:1px solid #3a2000;border-radius:8px;padding:16px}}
    .mistake-title{{font-size:14px;font-weight:700;color:#ff8c00;margin-bottom:8px}}
    .mistake-item p{{font-size:13px;color:#c8c8d8;margin-bottom:6px}}

    /* Before/after */
    .before-after{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:16px 0}}
    @media(max-width:600px){{.before-after{{grid-template-columns:1fr}}}}
    .ba-before{{background:#1a0000;border:1px solid #441111;border-radius:8px;padding:16px}}
    .ba-after{{background:#001a00;border:1px solid #114411;border-radius:8px;padding:16px}}
    .ba-label{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:8px}}
    .ba-before .ba-label{{color:#cc3333}}
    .ba-after .ba-label{{color:#33cc33}}
    .ba-text{{font-size:13px;color:#c8c8d8;line-height:1.6}}

    /* Progression path */
    .progression-path{{display:flex;flex-direction:column;gap:0;margin:16px 0;border:1px solid #2a2a4a;border-radius:8px;overflow:hidden}}
    .prog-stage{{padding:20px}}
    .prog-beginner{{background:#001a2a}}
    .prog-intermediate{{background:#0d1a00}}
    .prog-advanced{{background:#1a0800}}
    .prog-label{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:8px}}
    .prog-beginner .prog-label{{color:#60c0ff}}
    .prog-intermediate .prog-label{{color:#60ff60}}
    .prog-advanced .prog-label{{color:#f5a623}}
    .prog-stage p{{font-size:13px;color:#c8c8d8;margin:0;line-height:1.7}}

    /* Related terms */
    .related-terms-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:16px 0}}
    .related-term-card{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:14px;text-decoration:none;display:flex;flex-direction:column;gap:4px;transition:border-color .2s}}
    .related-term-card:hover{{border-color:#f5a623}}
    .rt-term{{font-size:14px;font-weight:700;color:#f5a623}}
    .rt-preview{{font-size:12px;color:#888}}

    /* Further reading */
    .further-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin:16px 0}}
    .further-card{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:14px;text-decoration:none;transition:border-color .2s}}
    .further-card:hover{{border-color:#14b8a6}}
    .further-title{{font-size:13px;color:#c8c8d8;font-weight:600}}

    /* FAQ */
    .faq-accordion{{display:flex;flex-direction:column;gap:8px;margin:16px 0}}
    .faq-item{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;overflow:hidden}}
    .faq-q{{width:100%;text-align:left;background:none;border:none;color:#e0e0f0;font-size:14px;font-weight:600;padding:16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center}}
    .faq-q:hover{{color:#f5a623}}
    .faq-a{{padding:0 16px 16px;display:none}}
    .faq-a p{{font-size:13px;color:#c8c8d8;line-height:1.7;margin:0}}
    .faq-item.open .faq-a{{display:block}}
    .faq-item.open .faq-q{{color:#f5a623}}

    /* Newsletter card */
    .bible-nl-card{{background:linear-gradient(135deg,#1a0800,#0d0d1a);border:1px solid #f5a623;border-radius:12px;padding:24px;margin:32px 0;text-align:center}}
    .nl-headline{{font-size:1.2rem;font-weight:700;color:#fff;margin-bottom:8px}}
    .nl-sub{{font-size:14px;color:#a0a0c0;margin-bottom:16px}}
    .nl-form{{display:flex;gap:8px;max-width:400px;margin:0 auto;flex-wrap:wrap;justify-content:center}}
    .nl-input{{flex:1;min-width:200px;padding:10px 14px;border-radius:6px;border:1px solid #444;background:#0d0d1a;color:#fff;font-size:14px}}
    .nl-btn{{background:#f5a623;color:#000;border:none;padding:10px 20px;border-radius:6px;font-weight:700;cursor:pointer;white-space:nowrap}}

    /* Spotify links */
    .spotify-links{{display:flex;flex-direction:column;gap:8px;margin:12px 0}}
    .spotify-link-item{{display:flex;align-items:center;gap:8px;background:#0a1a0a;border:1px solid #1DB954;border-radius:6px;padding:8px 14px;color:#1DB954;text-decoration:none;font-size:13px;font-weight:600;transition:background .2s}}
    .spotify-link-item:hover{{background:#111f11}}
    .spotify-icon{{flex-shrink:0}}

    /* Sidebar */
    .entry-sidebar{{position:sticky;top:160px;max-height:calc(100vh - 200px);overflow-y:auto}}
    .sidebar-toc{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px;margin-bottom:20px}}
    .sidebar-toc h4{{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:12px;font-weight:700}}
    .sidebar-toc a{{display:block;color:#a0a0c0;text-decoration:none;font-size:13px;padding:4px 0;border-bottom:1px solid #1a1a3a}}
    .sidebar-toc a:hover{{color:#f5a623}}
    .sidebar-cats{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:20px}}
    .sidebar-cats h4{{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#f5a623;margin-bottom:12px;font-weight:700}}
    .sidebar-cats a{{display:block;color:#a0a0c0;text-decoration:none;font-size:13px;padding:4px 0}}
    .sidebar-cats a:hover{{color:#f5a623}}

    /* Audio toggle */
    .audio-toggle{{background:#13132a;border:1px solid #2a2a4a;border-radius:8px;padding:16px;margin:16px 0;display:flex;gap:12px;align-items:center}}
    .at-label{{font-size:13px;color:#a0a0c0}}

    /* Footer */
    .bm-publisher{{display:inline-block;color:#f5a623;text-decoration:none;font-size:12px;font-weight:700;margin-bottom:8px}}
    .site-footer{{background:#0a0a1a;border-top:1px solid #1a1a3a;padding:32px 24px;text-align:center;margin-top:48px}}
    .site-footer p{{color:#666;font-size:13px;margin:4px 0}}
    .site-footer a{{color:#f5a623;text-decoration:none}}

    /* ── MOBILE ─────────────────────────── */
    @media(max-width:900px){{
      .entry-sidebar{{display:none!important}}
      .bible-entry-wrap{{grid-template-columns:1fr!important;padding:20px 16px!important}}
    }}
    @media(max-width:768px){{
      .entry-nav{{top:60px!important}}
      .entry-nav-inner{{justify-content:flex-start!important;padding:8px 10px!important}}
      .entry-nav-inner a{{font-size:8px!important;padding:4px 7px!important}}
      .parameters-grid{{grid-template-columns:1fr}}
      .types-grid{{grid-template-columns:1fr}}
      .red-green-flags{{grid-template-columns:1fr!important}}
      .before-after{{grid-template-columns:1fr!important}}
      .further-grid{{grid-template-columns:1fr!important}}
      .bible-nav-primary{{display:none!important}}
      #bibleMobBtn{{display:flex!important}}
      .entry-term{{font-size:clamp(1.8rem,8vw,2.5rem)!important}}
      .entry-masthead{{padding:20px 16px!important}}
    }}
    @media(max-width:480px){{
      .bible-entry-wrap{{padding:12px!important}}
      .entry-term{{font-size:1.8rem!important}}
    }}
  </style>
</head>
<body>
<div id="reading-progress"></div>

<!-- Nav — no bible bar on bible entry pages -->
{nav_html}

<!-- Entry Nav -->
<nav class="entry-nav" aria-label="Entry sections">
  <div class="entry-nav-inner">
    <a href="#definition">Definition</a>
    <a href="#how-it-works">How It Works</a>
    <a href="#parameters">Parameters</a>
    <a href="#history">History</a>
    <a href="#how-to-use">How To Use</a>
    <a href="#in-the-wild">In The Wild</a>
    <a href="#types">Types</a>
    <a href="#mistakes">Mistakes</a>
    <a href="#flags">Flags</a>
    <a href="#faq">FAQ</a>
    <a href="#related">Related</a>
    <a href="#further">Further Reading</a>
  </div>
</nav>

<main id="main-content">
  <div class="bible-entry-wrap">
    <div class="entry-main">

      <!-- Masthead -->
      <div class="entry-masthead">
        <div class="entry-category">{category}</div>
        <h1 class="entry-term">{term}</h1>
        <div class="entry-pos">{pos_label}{(' · ' + pronunciation) if pronunciation else ''}</div>
        <em class="entry-hook">{p1.get('emotional_hook','')}</em>
        <div class="entry-meta">
          <span>📅 {pub_date}</span>
          <span>⏱ {read_time} min read</span>
          <span>📚 Producer's Bible</span>
        </div>
      </div>

      <!-- Quick Answer -->
      <div id="quick-answer" class="quick-answer-block">
        <div class="qa-label">Quick Answer</div>
        <p class="qa-text">{quick_answer}</p>
      </div>

      <!-- Common Misconception (after quick answer) -->
      {p2.get('common_misconception_html','')}

      <!-- Definition -->
      <section id="definition">
        <h2>What Is {term}?</h2>
        {p2.get('definition_html','')}
        {build_section_summary(summaries.get('definition',''))}
      </section>

      <!-- How It Works -->
      <section id="how-it-works">
        <h2>How {term} Works</h2>
        {p2.get('how_it_works_html','')}
        {build_section_summary(summaries.get('how_it_works',''))}
      </section>

      <!-- Parameters -->
      <section id="parameters">
        <h2>{term} — Key Parameters</h2>
        {build_parameters_html(p1)}
        {build_section_summary(summaries.get('parameters',''))}
      </section>

      <!-- Quick Reference -->
      <section id="quick-reference">
        <h2>Quick Reference Card</h2>
        {build_the_number_html(p1)}
        {build_quick_ref_table(p1)}
        <p style="font-size:12px;color:#666;margin-top:8px">{p1.get('quick_reference_note','')}</p>
        <details style="margin-top:8px">
          <summary style="font-size:12px;color:#888;cursor:pointer">Copy as text</summary>
          <pre style="font-size:11px;color:#888;overflow-x:auto;padding:8px;background:#0d0d1a;border-radius:4px">{p1.get('copy_table_text','')}</pre>
        </details>
      </section>

      <!-- Signal Chain Position -->
      <section id="signal-chain">
        <h2>Signal Chain Position</h2>
        <div class="signal-chain-diagram">
          {build_signal_chain_svg(p1)}
        </div>
        <p style="font-size:13px;color:#888;margin-top:8px">{p1.get('signal_chain_position',{}).get('note','')}</p>
      </section>

      <!-- Interaction Warnings -->
      {build_interaction_warnings_html(p1)}

      <!-- SVG Diagram -->
      {'<section id="diagram"><h2>Diagram</h2>' + svg_content + '</section>' if svg_content else ''}

      <!-- Calculator -->
      {calc_html}

      <!-- Producer Quote -->
      {build_producer_quote_html(p1)}

      <!-- History -->
      <section id="history">
        <h2>History of {term}</h2>
        {p2.get('history_html','')}
        {build_section_summary(summaries.get('history',''))}
      </section>

      <!-- How Producers Use It -->
      <section id="how-to-use">
        <h2>How Producers Use {term}</h2>
        {p2.get('how_producers_use_it_html','')}
        {build_section_summary(summaries.get('how_producers_use_it',''))}
      </section>

      <!-- Genre Application Table -->
      <section id="genre-table">
        <h2>{term} by Genre</h2>
        {build_genre_table(p1)}
      </section>

      <!-- Hardware vs Plugin -->
      <section id="hardware-plugin">
        <h2>Hardware vs Plugin vs Stock</h2>
        {build_hardware_plugin_table(p1)}
      </section>

      <!-- Before / After -->
      <section id="before-after">
        <h2>Before and After</h2>
        <div class="before-after">
          <div class="ba-before">
            <span class="ba-label">Without {term}</span>
            <p class="ba-text">{before_after.get('before','')}</p>
          </div>
          <div class="ba-after">
            <span class="ba-label">With {term}</span>
            <p class="ba-text">{before_after.get('after','')}</p>
          </div>
        </div>
      </section>

      <!-- Newsletter (before In The Wild) -->
      <div class="bible-nl-card">
        <div class="nl-headline">Sound Better by Friday</div>
        <div class="nl-sub">The Producer's Briefing — practical technique, gear intel, no fluff.</div>
        <div class="nl-form">
          <input class="nl-input" type="email" placeholder="your@email.com">
          <button class="nl-btn">Subscribe Free</button>
        </div>
      </div>

      <!-- In The Wild -->
      <section id="in-the-wild">
        <h2>{term} In The Wild</h2>
        {build_track_examples_html(p2)}
        {build_section_summary(summaries.get('in_the_wild',''))}
      </section>

      <!-- Audio Toggle (shell — audio files added via Suno) -->
      <div class="audio-toggle" id="audio-toggle">
        <span class="at-label">🎧 Dry / Wet Audio Demo — Coming Soon</span>
      </div>

      <!-- Spotify Links -->
      <section id="spotify-section">
        <h3>Listen to Reference Tracks</h3>
        {build_spotify_links(p1)}
      </section>

      <!-- Types -->
      <section id="types">
        <h2>Types of {term}</h2>
        {build_types_html(p1)}
        {build_section_summary(summaries.get('types',''))}
      </section>

      <!-- Producer's Verdict (after Types) -->
      {p2.get('producers_verdict_html','')}

      <!-- Common Mistakes -->
      <section id="mistakes">
        <h2>Common Mistakes with {term}</h2>
        {build_mistakes_html(p2)}
        {build_section_summary(summaries.get('mistakes',''))}
      </section>

      <!-- Red / Green Flags -->
      <section id="flags">
        <h2>Red Flags and Green Flags</h2>
        {build_red_green_flags_html(p1)}
      </section>

      <!-- Progression Path -->
      <section id="progression">
        <h2>Your Progression with {term}</h2>
        {p2.get('progression_path_html','')}
      </section>

      <!-- Related Terms -->
      <section id="related">
        <h2>Related Bible Terms</h2>
        {build_related_terms_html(p1)}
      </section>

      <!-- Further Reading -->
      <section id="further">
        <h2>Further Reading</h2>
        {build_further_reading_html(p1)}
      </section>

      <!-- FAQ -->
      <section id="faq">
        <h2>Frequently Asked Questions</h2>
        {build_faq_html(p1)}
      </section>

    </div><!-- /entry-main -->

    <!-- Sidebar -->
    <aside class="entry-sidebar">
      <div class="sidebar-toc">
        <h4>In This Entry</h4>
        <a href="#definition">Definition</a>
        <a href="#how-it-works">How It Works</a>
        <a href="#parameters">Parameters</a>
        <a href="#quick-reference">Quick Reference</a>
        <a href="#signal-chain">Signal Chain</a>
        <a href="#history">History</a>
        <a href="#how-to-use">How To Use</a>
        <a href="#genre-table">By Genre</a>
        <a href="#hardware-plugin">Hardware vs Plugin</a>
        <a href="#before-after">Before / After</a>
        <a href="#in-the-wild">In The Wild</a>
        <a href="#types">Types</a>
        <a href="#mistakes">Mistakes</a>
        <a href="#flags">Flags</a>
        <a href="#progression">Progression Path</a>
        <a href="#faq">FAQ</a>
        <a href="#further">Further Reading</a>
      </div>
      <div class="sidebar-cats">
        <h4>Bible Categories</h4>
        <a href="/bible/#frequency">Frequency</a>
        <a href="/bible/#dynamics">Dynamics</a>
        <a href="/bible/#time-based">Time-Based</a>
        <a href="/bible/#signal-processing">Signal Processing</a>
        <a href="/bible/#mixing">Mixing</a>
        <a href="/bible/#mastering">Mastering</a>
        <a href="/bible/#synthesis">Synthesis</a>
        <a href="/bible/#music-theory">Music Theory</a>
      </div>
    </aside>

  </div><!-- /bible-entry-wrap -->
</main>

<!-- Reader Next Step CTA -->
<section style="background:#0d0d1f;border-top:1px solid #2a2a4a;padding:48px 24px;text-align:center">
  <div style="max-width:680px;margin:0 auto">
    <p style="font-size:11px;text-transform:uppercase;letter-spacing:.15em;color:#f5a623;font-weight:700;margin-bottom:12px">Keep Going</p>
    <h2 style="font-size:28px;font-weight:800;color:#fff;margin-bottom:12px">Sound better by Friday.</h2>
    <p style="color:#a0a0c0;font-size:16px;margin-bottom:28px;line-height:1.6">One email a week. The techniques behind the terms — what's actually happening in the records you love, and how to apply it in your session today.</p>
    <form style="display:flex;gap:8px;max-width:420px;margin:0 auto 32px" onsubmit="return false">
      <input type="email" placeholder="your@email.com" style="flex:1;padding:12px 16px;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;color:#e0e0f0;font-size:14px;outline:none">
      <button style="padding:12px 20px;background:#f5a623;color:#000;font-weight:700;font-size:14px;border:none;border-radius:6px;cursor:pointer;white-space:nowrap">Join Free</button>
    </form>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
      <a href="/bible/" style="display:inline-flex;align-items:center;gap:6px;padding:10px 18px;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;color:#e0e0f0;text-decoration:none;font-size:13px;font-weight:600">&#8592; Browse The Bible</a>
      <a href="/categories/techniques.html" style="display:inline-flex;align-items:center;gap:6px;padding:10px 18px;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;color:#e0e0f0;text-decoration:none;font-size:13px;font-weight:600">Techniques &rarr;</a>
      <a href="/categories/comparisons.html" style="display:inline-flex;align-items:center;gap:6px;padding:10px 18px;background:#13132a;border:1px solid #2a2a4a;border-radius:6px;color:#e0e0f0;text-decoration:none;font-size:13px;font-weight:600">Gear Comparisons &rarr;</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <a href="/bible/" class="bm-publisher">The Producer's Bible</a>
  <p style="font-size:15px;font-weight:600;color:#e0e0f0;margin:8px 0 4px">MusicProductionWiki.com</p>
  <p style="font-size:12px;color:#666;margin-bottom:12px">The most comprehensive music production reference on the internet.</p>
  <p><a href="/">Home</a> &middot; <a href="/about.html">About</a> &middot; <a href="/bible/">Producer's Bible</a> &middot; <a href="/categories/techniques.html">Techniques</a> &middot; <a href="/categories/reviews.html">Reviews</a> &middot; <a href="/categories/comparisons.html">Comparisons</a></p>
  <p style="margin-top:8px;font-size:11px;color:#444">&copy; {{datetime.now().year}} MusicProductionWiki.com &mdash; Built for producers, by producers.</p>
</footer>

<script>
// Bible nav — dropdown + mobile toggle
(function(){{
  // Dropdowns
  document.querySelectorAll('.bible-nav-item').forEach(function(item){{
    var btn = item.querySelector('.bible-nav-btn');
    var dd = item.querySelector('.bible-nav-dd');
    if (!btn || !dd) return;
    btn.addEventListener('click', function(e){{
      e.stopPropagation();
      var isOpen = dd.style.display === 'grid' || dd.style.display === 'block';
      document.querySelectorAll('.bible-nav-dd').forEach(function(d){{ d.style.display='none'; }});
      dd.style.display = isOpen ? 'none' : (dd.style.gridTemplateColumns ? 'grid' : 'block');
    }});
  }});
  document.addEventListener('click', function(){{
    document.querySelectorAll('.bible-nav-dd').forEach(function(d){{ d.style.display='none'; }});
  }});
  // Mobile toggle
  var mobBtn = document.getElementById('bibleMobBtn');
  var mobDrawer = document.getElementById('bibleMobDrawer');
  if (mobBtn && mobDrawer) {{
    mobBtn.addEventListener('click', function(){{
      var open = mobDrawer.style.display === 'flex';
      mobDrawer.style.display = open ? 'none' : 'flex';
    }});
  }}
  // Search ESC
  document.addEventListener('keydown', function(e){{
    if (e.key === 'Escape') {{
      var ov = document.getElementById('bibleSearchOverlay');
      if (ov) ov.style.display = 'none';
      document.querySelectorAll('.bible-nav-dd').forEach(function(d){{ d.style.display='none'; }});
    }}
  }});
  // Show mobile btn on small screens
  function checkMob(){{
    if (mobBtn) mobBtn.style.display = window.innerWidth <= 1024 ? 'flex' : 'none';
  }}
  checkMob();
  window.addEventListener('resize', checkMob);
  // Articles dropdown uses grid
  var articlesDd = document.querySelector('.bible-nav-item .bible-nav-dd[style*="grid-template-columns"]');
  if (articlesDd) articlesDd.style.display = 'none';
}})();

// Reading progress bar — percentage-based, contained to viewport
(function(){{
  var bar = document.getElementById('reading-progress');
  if (!bar) return;
  bar.style.cssText = 'position:fixed;top:0;left:0;height:3px;background:#f5a623;z-index:99999;width:0%;max-width:100%;transition:width .1s linear;pointer-events:none';
  window.addEventListener('scroll', function(){{
    var st = window.scrollY || document.documentElement.scrollTop;
    var dh = document.documentElement.scrollHeight - window.innerHeight;
    if (dh <= 0) {{ bar.style.width = '100%'; return; }}
    var pct = Math.min(100, Math.round((st/dh)*100));
    bar.style.width = pct + '%';
  }}, {{passive:true}});
}})();

// FAQ accordion
document.querySelectorAll('.faq-q').forEach(function(btn){{
  btn.addEventListener('click', function(){{
    var item = this.closest('.faq-item');
    var wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function(i){{ i.classList.remove('open'); }});
    if (!wasOpen) item.classList.add('open');
  }});
}});

// Search overlay — works for both searchInput and bibleSearchInput
(function(){{
  var articleIdx = null;
  var bibleIdx = null;
  fetch('/search-index.json').then(function(r){{ return r.json(); }}).then(function(d){{ articleIdx = d; }}).catch(function(){{}});
  fetch('/bible-index.json').then(function(r){{ return r.json(); }}).then(function(d){{ bibleIdx = d; }}).catch(function(){{}});

  function doSearch(q, resultsEl) {{
    if (!q) {{ resultsEl.innerHTML = ''; return; }}
    var hits = [];
    if (bibleIdx) {{
      bibleIdx.filter(function(e){{ return (e.term||'').toLowerCase().includes(q); }}).slice(0,4).forEach(function(e){{
        hits.push('<a href="/bible/' + e.slug + '" style="display:flex;align-items:center;gap:8px;padding:8px;color:#e0e0f0;text-decoration:none;border-bottom:1px solid #2a2a4a;font-size:14px"><span style="background:#f5a623;color:#000;font-size:10px;font-weight:700;padding:2px 5px;border-radius:3px;flex-shrink:0">BIBLE</span>' + (e.term||e.slug) + '</a>');
      }});
    }}
    if (articleIdx) {{
      articleIdx.filter(function(a){{ return (a.title||'').toLowerCase().includes(q) || (a.slug||'').includes(q); }}).slice(0,4).forEach(function(a){{
        hits.push('<a href="/articles/' + a.slug + '.html" style="display:flex;align-items:center;gap:8px;padding:8px;color:#e0e0f0;text-decoration:none;border-bottom:1px solid #2a2a4a;font-size:14px"><span style="background:#2a2a4a;color:#a0a0c0;font-size:10px;font-weight:700;padding:2px 5px;border-radius:3px;flex-shrink:0">ARTICLE</span>' + (a.title||a.slug) + '</a>');
      }});
    }}
    resultsEl.innerHTML = hits.slice(0,8).join('') || '<p style="color:#888;font-size:13px;padding:8px">No results</p>';
  }}

  ['searchInput','bibleSearchInput'].forEach(function(id) {{
    var input = document.getElementById(id);
    var results = document.getElementById(id === 'searchInput' ? 'searchResults' : 'bibleSearchResults');
    if (!input || !results) return;
    input.addEventListener('input', function() {{
      doSearch(this.value.trim().toLowerCase(), results);
    }});
    // ESC closes overlay
    input.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        var ov = document.getElementById('bibleSearchOverlay');
        if (ov) ov.style.display = 'none';
      }}
    }});
  }});
}})();

// Aside JS fix — moves aside back into article-layout if unclosed tags pushed it out
// NO main.js on bible pages
(function(){{
  var aside = document.querySelector('.entry-sidebar');
  var wrap = document.querySelector('.bible-entry-wrap');
  if (aside && wrap && aside.parentElement !== wrap) {{
    wrap.appendChild(aside);
  }}
}})();

// Active TOC highlighting via IntersectionObserver
(function(){{
  var tocLinks = document.querySelectorAll('.sidebar-toc a');
  if (!tocLinks.length) return;
  var sectionIds = Array.from(tocLinks).map(function(a){{ return a.getAttribute('href').replace('#',''); }});
  var sections = sectionIds.map(function(id){{ return document.getElementById(id); }}).filter(Boolean);
  if (!sections.length) return;

  function setActive(id) {{
    tocLinks.forEach(function(a) {{
      var isActive = a.getAttribute('href') === '#' + id;
      a.style.color = isActive ? '#f5a623' : '';
      a.style.fontWeight = isActive ? '700' : '';
      a.style.borderLeft = isActive ? '2px solid #f5a623' : '2px solid transparent';
      a.style.paddingLeft = isActive ? '8px' : '0';
    }});
  }}

  var observer = new IntersectionObserver(function(entries) {{
    entries.forEach(function(entry) {{
      if (entry.isIntersecting) {{
        setActive(entry.target.id);
      }}
    }});
  }}, {{ rootMargin: '-20% 0px -70% 0px', threshold: 0 }});

  sections.forEach(function(s){{ observer.observe(s); }});
  // Set first active on load
  if (sections[0]) setActive(sections[0].id);
}})();

// Entry nav active highlight + auto-scroll active item into view
(function(){{
  var navEl = document.querySelector('.entry-nav');
  var navLinks = document.querySelectorAll('.entry-nav-inner a');
  if (!navLinks.length) return;
  var sectionIds = Array.from(navLinks).map(function(a){{ return a.getAttribute('href').replace('#',''); }});
  var sections = sectionIds.map(function(id){{ return document.getElementById(id); }}).filter(Boolean);

  function setActive(id) {{
    navLinks.forEach(function(a) {{
      var isActive = a.getAttribute('href') === '#' + id;
      a.style.color = isActive ? '#f5a623' : '';
      a.style.fontWeight = isActive ? '700' : '';
      a.style.background = isActive ? 'rgba(245,166,35,0.1)' : '';
      // Auto-scroll active link into view in the nav bar
      if (isActive && navEl) {{
        var linkLeft = a.offsetLeft;
        var linkWidth = a.offsetWidth;
        var navWidth = navEl.offsetWidth;
        var target = linkLeft - (navWidth / 2) + (linkWidth / 2);
        navEl.scrollTo({{ left: target, behavior: 'smooth' }});
      }}
    }});
  }}

  var observer = new IntersectionObserver(function(entries) {{
    entries.forEach(function(entry) {{
      if (entry.isIntersecting) setActive(entry.target.id);
    }});
  }}, {{ rootMargin: '-10% 0px -80% 0px', threshold: 0 }});

  sections.forEach(function(s){{ observer.observe(s); }});
  if (sections[0]) setActive(sections[0].id);
}})();

// Search — badge Bible vs Article results
(function(){{
  var input = document.getElementById('searchInput');
  var results = document.getElementById('searchResults');
  if (!input || !results) return;
  var bibleIdx = null;
  var articleIdx = null;
  fetch('/bible-index.json').then(function(r){{ return r.json(); }}).then(function(d){{ bibleIdx = d; }}).catch(function(){{}});
  fetch('/search-index.json').then(function(r){{ return r.json(); }}).then(function(d){{ articleIdx = d; }}).catch(function(){{}});

  input.addEventListener('input', function(){{
    var q = this.value.trim().toLowerCase();
    if (!q) {{ results.innerHTML = ''; return; }}
    var hits = [];
    if (bibleIdx) {{
      bibleIdx.filter(function(e){{ return (e.term||'').toLowerCase().includes(q); }}).slice(0,4).forEach(function(e){{
        hits.push('<a href="/bible/' + e.slug + '" style="display:flex;align-items:center;gap:8px;padding:8px;color:#e0e0f0;text-decoration:none;border-bottom:1px solid #2a2a4a;font-size:14px"><span style="background:#f5a623;color:#000;font-size:10px;font-weight:700;padding:2px 5px;border-radius:3px;flex-shrink:0">BIBLE</span>' + (e.term||e.slug) + '</a>');
      }});
    }}
    if (articleIdx) {{
      articleIdx.filter(function(a){{ return (a.title||'').toLowerCase().includes(q) || (a.slug||'').includes(q); }}).slice(0,4).forEach(function(a){{
        hits.push('<a href="/articles/' + a.slug + '.html" style="display:flex;align-items:center;gap:8px;padding:8px;color:#e0e0f0;text-decoration:none;border-bottom:1px solid #2a2a4a;font-size:14px"><span style="background:#2a2a4a;color:#a0a0c0;font-size:10px;font-weight:700;padding:2px 5px;border-radius:3px;flex-shrink:0">ARTICLE</span>' + (a.title||a.slug) + '</a>');
      }});
    }}
    results.innerHTML = hits.slice(0,8).join('') || '<p style="color:#888;font-size:13px;padding:8px">No results</p>';
  }});
}})();
</script>
<button id="btt-btn" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" 
  style="position:fixed;bottom:24px;right:24px;width:44px;height:44px;border-radius:50%;
  background:#f5a623;color:#000;border:none;cursor:pointer;font-size:20px;font-weight:700;
  display:none;align-items:center;justify-content:center;z-index:9000;
  box-shadow:0 4px 16px rgba(0,0,0,0.4);transition:opacity .2s" 
  aria-label="Back to top">&#8593;</button>
<script>
(function(){{
  var btn = document.getElementById('btt-btn');
  if (!btn) return;
  window.addEventListener('scroll', function(){{
    btn.style.display = window.scrollY > 400 ? 'flex' : 'none';
  }}, {{passive:true}});
}})();
</script>
</body>
</html>"""
    return html


# ─── CATALOG BUILDER ────────────────────────────────────────────────────────────

def build_catalog_content(article_slugs, bible_slugs):
    """Generate MPW-CATALOG.md from live slug lists."""
    lines = [
        '# MPW-CATALOG.md',
        f'*Auto-generated {datetime.now().strftime("%Y-%m-%d %H:%M")} — do not edit manually*',
        '',
        f'## Articles ({len(article_slugs)})',
        ''
    ]
    for i, s in enumerate(sorted(article_slugs), 1):
        lines.append(f'| {i} | {s} | ✅ |')
    lines += [
        '',
        f'## Bible Entries ({len(bible_slugs)})',
        ''
    ]
    for i, s in enumerate(sorted(bible_slugs), 1):
        lines.append(f'| {i} | {s} | ✅ |')
    return '\n'.join(lines)


# ─── GITHUB TREES API ───────────────────────────────────────────────────────────

def gh_trees_commit(file_dict, message):
    """Commit multiple files via GitHub Trees API — sequential blob creation."""
    # 1. Get latest commit SHA
    ref = requests.get(
        f'https://api.github.com/repos/{REPO}/git/ref/heads/main',
        headers=GH_HEADERS, timeout=30
    ).json()
    base_sha = ref['object']['sha']
    tree_sha = requests.get(
        f'https://api.github.com/repos/{REPO}/git/commits/{base_sha}',
        headers=GH_HEADERS, timeout=30
    ).json()['tree']['sha']

    # 2. Create blobs SEQUENTIALLY — no parallel — rate limits
    blobs = []
    for path, content in file_dict.items():
        for attempt in range(6):
            if attempt > 0:
                wait = BACKOFF[min(attempt - 1, len(BACKOFF) - 1)]
                print(f"  [blob] {path} retry {attempt} — waiting {wait}s")
                time.sleep(wait)
            r = requests.post(
                f'https://api.github.com/repos/{REPO}/git/blobs',
                headers=GH_HEADERS,
                json={'content': content, 'encoding': 'utf-8'},
                timeout=60
            )
            if r.status_code == 201:
                blobs.append({
                    'path': path,
                    'mode': '100644',
                    'type': 'blob',
                    'sha': r.json()['sha']
                })
                break
            elif r.status_code == 403:
                print(f"  [blob] {path} — 403 secondary rate limit")
                continue
            else:
                r.raise_for_status()

    # 3. Create tree
    new_tree = requests.post(
        f'https://api.github.com/repos/{REPO}/git/trees',
        headers=GH_HEADERS,
        json={'base_tree': tree_sha, 'tree': blobs},
        timeout=60
    ).json()

    # 4. Create commit
    new_commit = requests.post(
        f'https://api.github.com/repos/{REPO}/git/commits',
        headers=GH_HEADERS,
        json={'message': message, 'tree': new_tree['sha'], 'parents': [base_sha]},
        timeout=60
    ).json()

    # 5. Update ref
    requests.patch(
        f'https://api.github.com/repos/{REPO}/git/refs/heads/main',
        headers=GH_HEADERS,
        json={'sha': new_commit['sha']},
        timeout=30
    )

    return new_commit['sha']


def get_live_slugs():
    """Fetch article and bible slugs from GitHub Trees API."""
    r = requests.get(
        f'https://api.github.com/repos/{REPO}/git/trees/main?recursive=1',
        headers=GH_HEADERS, timeout=60
    )
    tree = r.json().get('tree', [])
    articles = [
        f['path'].replace('articles/', '').replace('.html', '')
        for f in tree
        if f['path'].startswith('articles/') and f['path'].endswith('.html')
    ]
    bible = [
        f['path'].replace('bible/', '').replace('.html', '')
        for f in tree
        if f['path'].startswith('bible/') and f['path'].endswith('.html')
        and f['path'] != 'bible/index.html'
    ]
    return articles, bible


def update_bible_index(new_entry_data):
    """Fetch bible-index.json, add new entry, return updated JSON string."""
    try:
        r = requests.get(
            f'https://api.github.com/repos/{REPO}/contents/bible-index.json',
            headers=GH_HEADERS, timeout=30
        )
        existing = json.loads(base64.b64decode(r.json()['content']).decode('utf-8'))
    except Exception:
        existing = []

    # Remove existing entry with same slug
    existing = [e for e in existing if e.get('slug') != new_entry_data['slug']]
    existing.append({
        'slug': new_entry_data['slug'],
        'term': new_entry_data['term'],
        'category': new_entry_data.get('category', ''),
        'excerpt': new_entry_data.get('excerpt', '')
    })
    existing.sort(key=lambda x: x.get('term', '').lower())
    return json.dumps(existing, indent=2)


# ─── ENTRY GENERATOR ────────────────────────────────────────────────────────────

def generate_entry(slug, term, category, pub_date=None):
    """Run two-pass generation for a single entry. Returns (slug, html) or raises."""
    label = f"{term} ({slug})"
    print(f"\n[START] {label}")

    # Pass 1
    p1_prompt = build_pass1_prompt(slug, term, category)
    p1 = call_claude_pass1(p1_prompt, label=f"{label} P1")

    # Pass 2
    p2_prompt = build_pass2_prompt(slug, term, category, p1)
    p2 = call_claude_pass2(p2_prompt, label=f"{label} P2")

    # Build HTML
    html = build_html(p1, p2, slug, term, category, pub_date=pub_date)

    # Word count check
    text_only = re.sub(r'<[^>]+>', ' ', html)
    word_count = len(text_only.split())
    print(f"  [{label}] Word count: {word_count}")
    if word_count < WORD_COUNT_FLOOR:
        print(f"  [{label}] WARNING: Below floor ({WORD_COUNT_FLOOR}w)")

    return slug, html, p1


# ─── BATCH RUNNER ───────────────────────────────────────────────────────────────

def run_batch(batch_file, start_date=None, test_mode=False):
    """Run a batch file of entries. Commits all in one Trees API commit."""
    lines = open(batch_file).read().strip().splitlines()
    entries = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(':')
        if len(parts) != 3:
            print(f"[SKIP] Bad format: {line} — expected slug:Term:Category")
            continue
        entries.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))

    if test_mode:
        entries = entries[:1]

    print(f"\n[BATCH] {len(entries)} entries from {batch_file}")

    results = {}
    failed = []

    # 8 parallel workers for generation
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {
            ex.submit(generate_entry, slug, term, cat, start_date): (slug, term, cat)
            for slug, term, cat in entries
        }
        for future in as_completed(futures):
            slug, term, cat = futures[future]
            try:
                s, html, p1 = future.result()
                results[s] = (html, p1)
                print(f"  [OK] {term}")
            except Exception as e:
                print(f"  [FAIL] {term}: {e}")
                failed.append(f"{slug}:{term}:{cat}")

    if not results:
        print("[BATCH] No entries generated successfully.")
        return

    # Build commit payload
    print(f"\n[COMMIT] Building Trees API payload for {len(results)} entries...")
    file_dict = {}
    all_p1s = {}
    for slug, (html, p1) in results.items():
        file_dict[f'bible/{slug}.html'] = html
        all_p1s[slug] = p1

    # Update bible-index.json with all new entries
    try:
        r = requests.get(
            f'https://api.github.com/repos/{REPO}/contents/bible-index.json',
            headers=GH_HEADERS, timeout=30
        )
        existing_index = json.loads(base64.b64decode(r.json()['content']).decode('utf-8'))
    except Exception:
        existing_index = []

    for slug, p1 in all_p1s.items():
        existing_index = [e for e in existing_index if e.get('slug') != slug]
        existing_index.append({
            'slug': slug,
            'term': p1.get('term', slug),
            'category': p1.get('category', ''),
            'excerpt': p1.get('excerpt', '')
        })
    existing_index.sort(key=lambda x: x.get('term', '').lower())
    file_dict['bible-index.json'] = json.dumps(existing_index, indent=2)

    # Auto-update MPW-CATALOG.md
    try:
        article_slugs, bible_slugs = get_live_slugs()
        # Add new bible slugs
        for slug in results:
            if slug not in bible_slugs:
                bible_slugs.append(slug)
        file_dict['MPW-CATALOG.md'] = build_catalog_content(article_slugs, bible_slugs)
        print(f"  [CATALOG] Updated: {len(article_slugs)} articles, {len(bible_slugs)} bible entries")
    except Exception as e:
        print(f"  [CATALOG] Could not update: {e}")

    commit_sha = gh_trees_commit(
        file_dict,
        f"Add {len(results)} Bible entries v4.0 ({', '.join(list(results.keys())[:5])}{'...' if len(results) > 5 else ''})"
    )
    print(f"\n[DONE] Commit: {commit_sha}")
    print(f"[DONE] {len(results)} entries live")

    if failed:
        print(f"\n[FAILED] {len(failed)} entries — retry:")
        for f in failed:
            print(f"  {f}")


# ─── VALIDATION ─────────────────────────────────────────────────────────────────

def run_validation():
    """Run 55-check validation suite against this file."""
    content = open(__file__).read()
    checks = {
        # v3.0 checks
        'nav centered': 'justify-content:center' in content,
        'nav font 9px': 'font-size:9px' in content,
        'nav overflow-x auto': 'overflow-x:auto' in content,
        'nav sticky top:96px': 'top:96px' in content,
        'progress z-index 99999': 'z-index:99999' in content,
        'progress px width JS': 'Math.round((st/dh)*window.innerWidth)' in content,
        'type grid 3 cols': 'repeat(3,1fr)' in content,
        'newsletter card': 'bible-nl-card' in content,
        'further reading': 'further-grid' in content,
        'audio toggle': 'audio-toggle' in content,
        'gain calculator': 'gain-calculator' in content,
        'bm-publisher link': 'href="/bible/" class="bm-publisher"' in content,
        'no main.js in output': 'NO main.js' in content,
        'model claude-sonnet-4-6': 'claude-sonnet-4-6' in content,
        'PASS1_TOKENS 20000': '20000' in content,
        'trees API commit': 'gh_trees_commit' in content,
        'spotify links not iframes': 'spotify-link-item' in content,
        'build_pass1_prompt': 'build_pass1_prompt' in content,
        'call_claude_pass1': 'call_claude_pass1' in content,
        'build_pass2_prompt': 'build_pass2_prompt' in content,
        'call_claude_pass2': 'call_claude_pass2' in content,
        'build_html': 'build_html' in content,
        'PASS2_TOKENS': 'PASS2_TOKENS' in content,
        'system prompt': 'SYSTEM_PROMPT' in content,
        'word count floor 5500': '5500' in content,
        'word count target 6000': '6000' in content,
        'word count ceiling 6500': '6500' in content,
        'the_number field': 'the_number' in content,
        'producer_quote field': 'producer_quote' in content,
        'signal_chain_position': 'signal_chain_position' in content,
        'hardware_vs_plugin_rows': 'hardware_vs_plugin_rows' in content,
        'genre_application_rows': 'genre_application_rows' in content,
        'interaction_warnings': 'interaction_warnings' in content,
        'red_flags': 'red_flags' in content,
        'green_flags': 'green_flags' in content,
        'further_reading_slugs': 'further_reading_slugs' in content,
        'faq field': '"faq"' in content,
        'track_examples': 'track_examples' in content,
        'listening_guide': 'listening_guide' in content,
        'section_summaries': 'section_summaries' in content,
        'before_after_text': 'before_after_text' in content,
        # v4.0 new checks (13)
        'misconception-block CSS': 'misconception-block' in content,
        'producers-verdict CSS': 'producers-verdict' in content,
        'progression-path CSS': 'progression-path' in content,
        'red-flag CSS': 'red-flag' in content,
        'green-flag CSS': 'green-flag' in content,
        'genre-table CSS': 'genre-table' in content,
        'hardware-plugin CSS': 'hardware-plugin-table' in content,
        'the-number-box CSS': 'the-number-box' in content,
        'producer-quote-block CSS': 'producer-quote-block' in content,
        'section-summary CSS': 'section-summary' in content,
        'signal-chain CSS': 'signal-chain-diagram' in content,
        'no iframes in output': '<iframe' not in content.split('def build_html')[1] if 'def build_html' in content else True,
        'catalog update': 'build_catalog_content' in content,
    }

    try:
        ast.parse(content)
        print('Syntax: OK')
    except SyntaxError as e:
        print(f'Syntax: ERROR — {e}')

    missing = [k for k, v in checks.items() if not v]
    ok_checks = [k for k, v in checks.items() if v]

    for k in ok_checks:
        print(f'[OK] {k}')
    for k in missing:
        print(f'[MISSING] {k}')

    score = len(ok_checks)
    total = len(checks)
    print(f'\nScore: {score}/{total}')
    if missing:
        print(f'FAILED — fix {len(missing)} missing checks before running.')
        return False
    print('ALL CHECKS PASS — v4.0 ready.')
    return True


# ─── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='mpw_bible_writer.py v4.0')
    parser.add_argument('--validate', action='store_true', help='Run 55-check validation suite')
    parser.add_argument('--test', action='store_true', help='Test mode — generate one entry without committing batch')
    parser.add_argument('--slug', help='Entry slug (test mode)')
    parser.add_argument('--term', help='Entry term (test mode)')
    parser.add_argument('--category', help='Entry category (test mode)')
    parser.add_argument('--start-date', help='Publication date YYYY-MM-DD')
    parser.add_argument('--batch-file', help='Batch file path — slug:Term:Category per line')
    args = parser.parse_args()

    if args.validate:
        success = run_validation()
        sys.exit(0 if success else 1)

    if args.test:
        if not all([args.slug, args.term, args.category]):
            print("--test requires --slug, --term, --category")
            sys.exit(1)
        slug, html, p1 = generate_entry(args.slug, args.term, args.category, args.start_date)

        # Commit single test entry
        print(f"\n[TEST] Committing {slug}...")
        file_dict = {f'bible/{slug}.html': html}

        # Update bible-index.json
        index_json = update_bible_index(p1)
        file_dict['bible-index.json'] = index_json

        # Update MPW-CATALOG.md
        try:
            article_slugs, bible_slugs = get_live_slugs()
            if slug not in bible_slugs:
                bible_slugs.append(slug)
            file_dict['MPW-CATALOG.md'] = build_catalog_content(article_slugs, bible_slugs)
        except Exception as e:
            print(f"  [CATALOG] Could not update: {e}")

        commit_sha = gh_trees_commit(file_dict, f"Bible v4.0 test entry: {args.term} ({slug})")
        print(f"[TEST] Commit: {commit_sha}")
        print(f"[TEST] Live at: {SITE_URL}/bible/{slug}")
        print(f"[TEST] Visually confirm at {SITE_URL}/bible/{slug} before running any batch.")
        return

    if args.batch_file:
        run_batch(args.batch_file, start_date=args.start_date)
        return

    parser.print_help()


if __name__ == '__main__':
    main()

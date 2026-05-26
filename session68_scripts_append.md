---

# SESSION 68 UPDATE — SCRIPTS — May 26, 2026

## Nav Block Extractor (Div-Depth Balanced)

Use this every time you need the nav block from a reference tool. Never use naive `find()`.

```python
import urllib.request, json, base64

def get_nav_block(slug='ai-music-rights-navigator.html'):
    TOKEN = '[GITHUB_TOKEN — stored in Netlify env vars, regenerate at github.com/settings/tokens if expired]'
    headers = {'Authorization':f'token {TOKEN}','User-Agent':'MPW'}
    req = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/tools/{slug}',
        headers=headers
    )
    with urllib.request.urlopen(req) as r: data = json.loads(r.read())
    html = base64.b64decode(data['content']).decode('utf-8', errors='replace')

    nav_start = html.find('<div class="mpw-nav-wrap">')
    if nav_start == -1:
        raise ValueError("mpw-nav-wrap not found")

    # Div-depth tracking — guaranteed balanced
    depth = 0
    pos = nav_start
    end = nav_start
    while pos < len(html):
        open_m = html.find('<div', pos)
        close_m = html.find('</div>', pos)
        if open_m == -1: open_m = len(html)
        if close_m == -1: close_m = len(html)
        if open_m < close_m:
            depth += 1; pos = open_m + 4
        else:
            depth -= 1; pos = close_m + 6; end = pos
            if depth == 0: break

    nav_block = html[nav_start:end]

    # Validate balance
    opens = nav_block.count('<div')
    closes = nav_block.count('</div>')
    assert opens == closes, f"Nav unbalanced: {opens} opens, {closes} closes"
    print(f"Nav block: {len(nav_block)} chars, {opens} divs balanced")
    return nav_block
```

---

## JS Syntax Checker

Run before embedding any JS in HTML.

```python
import subprocess

def check_js(filepath):
    r = subprocess.run(['node', '--check', filepath], capture_output=True, text=True)
    if r.returncode == 0:
        print(f"✓ {filepath}: syntax OK")
        return True
    else:
        print(f"✗ {filepath}: SYNTAX ERROR")
        print(r.stderr[:500])
        return False
```

---

## GitHub Restore Script

Restore any file to a previous commit SHA.

```python
import urllib.request, json, base64

def restore_file(filepath, restore_sha, token):
    headers = {'Authorization':f'token {token}','User-Agent':'MPW'}

    # Get content at historical commit
    req = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}?ref={restore_sha}',
        headers=headers
    )
    with urllib.request.urlopen(req) as r: data = json.loads(r.read())
    content = data['content']  # already base64

    # Get current SHA
    req2 = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}',
        headers=headers
    )
    with urllib.request.urlopen(req2) as r: cur = json.loads(r.read())
    current_sha = cur['sha']

    # Commit restore
    body = json.dumps({
        'message': f'revert: restore {filepath} to {restore_sha}',
        'content': content,
        'sha': current_sha
    }).encode()
    req3 = urllib.request.Request(
        f'https://api.github.com/repos/musicproductionwiki/musicproductionwiki/contents/{filepath}',
        data=body,
        headers={**headers, 'Content-Type':'application/json'},
        method='PUT'
    )
    with urllib.request.urlopen(req3) as r: result = json.loads(r.read())
    print(f"Restored: {result['content']['sha']}")
```

---

## Tool Build Pre-Commit Checklist Script

```python
import re, subprocess

def verify_tool(filepath):
    with open(filepath) as f: html = f.read()
    errors = []

    # Div balance
    if html.count('<div') != html.count('</div>'):
        errors.append(f"Unbalanced divs: {html.count('<div')} opens, {html.count('</div>')} closes")

    # No style.css
    if 'style.css' in html:
        errors.append("style.css must NOT be loaded in tool pages")

    # Model string
    if 'claude-sonnet-4-6' not in html:
        errors.append("Wrong or missing model string — must be claude-sonnet-4-6")

    # Proxy URL
    if 'classy-haupia-be8e43' not in html:
        errors.append("Missing proxy URL")

    # GA4
    if 'G-79VB543KCT' not in html:
        errors.append("Missing GA4 tag")

    # JS syntax
    scripts = re.findall(
        r'<script(?![\s\S]{0,10}(?:async|ld\+json|src=))[^>]*>([\s\S]+?)</script>',
        html
    )
    for i, s in enumerate(scripts):
        with open(f'/tmp/verify_{i}.js','w') as f2: f2.write(s)
        r = subprocess.run(['node','--check',f'/tmp/verify_{i}.js'], capture_output=True, text=True)
        if r.returncode != 0:
            errors.append(f"Script block {i} syntax error: {r.stderr[:200]}")

    # File size
    size = len(html.encode())
    if size > 200000:
        errors.append(f"File too large: {size:,} bytes (Cloudflare limit: 200KB)")

    if errors:
        print(f"FAILED — {len(errors)} errors:")
        for e in errors: print(f"  ✗ {e}")
        return False
    else:
        print(f"ALL CHECKS PASSED — {size:,} bytes ({size/1024:.1f}KB)")
        return True
```


---

## Pre-Upload Token Redaction Scan

**Run this before uploading ANY file to GitHub — handoffs, scripts, HTML, everything.**

```python
import re, sys

SENSITIVE_PATTERNS = [
    r'ghp_[A-Za-z0-9]{36}',           # GitHub personal access token
    r'sk-ant-[A-Za-z0-9\-]{90,}',     # Anthropic API key
    r'AKIA[A-Z0-9]{16}',               # AWS access key
]

def scan_for_secrets(filepath):
    with open(filepath) as f: content = f.read()
    found = []
    for pattern in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            found.extend(matches)
    if found:
        print(f"SECRETS FOUND in {filepath} — DO NOT UPLOAD:")
        for m in found: print(f"  {m[:12]}... [REDACT BEFORE UPLOADING]")
        return False
    print(f"✓ {filepath}: no secrets found")
    return True
```

**NEVER rule:** Always run this scan before `gh_put()`. If it finds anything, redact to `[GITHUB_TOKEN]` or `[ANTHROPIC_API_KEY]` first.


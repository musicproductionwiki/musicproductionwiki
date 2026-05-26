#!/usr/bin/env python3
"""
MPW Pre-Commit Verification Script
Run before every GitHub commit. If this fails, do not commit.
Added: Session 68, May 26 2026
"""

import re
import sys
import subprocess
import os

def check_tool_page(filepath):
    """Full verification for tool HTML pages."""
    errors = []
    warnings = []

    with open(filepath, encoding='utf-8') as f:
        html = f.read()

    filename = os.path.basename(filepath)

    # ── STRUCTURE ──────────────────────────────────────────────────
    # Div balance
    opens = len(re.findall(r'<div', html))
    closes = len(re.findall(r'</div>', html))
    if opens != closes:
        errors.append(f"UNBALANCED DIVS: {opens} opens, {closes} closes (diff: {opens-closes})")

    # Ends with </html>
    if not html.strip().endswith('</html>'):
        errors.append("File does not end with </html>")

    # ── CSS SAFETY ─────────────────────────────────────────────────
    # No style.css (causes 600px black blob shapes)
    if 'style.css' in html:
        errors.append("style.css must NOT be loaded in tool pages — causes giant black shapes from global pseudo-elements")

    # No bare .hero class (conflicts with global CSS)
    bare_hero = re.findall(r'class="hero"', html)
    if bare_hero:
        errors.append(f"Found class=\"hero\" {len(bare_hero)}x — use class=\"tool-hero\" to avoid global CSS conflict")

    # No bare .container class
    bare_container = re.findall(r'class="container"', html)
    if bare_container:
        errors.append(f"Found class=\"container\" {len(bare_container)}x — use class=\"tool-container\" to avoid global CSS conflict")

    # ── JS SAFETY ──────────────────────────────────────────────────
    # No Python artifacts
    python_artifacts = ['PYEOF', 'JSEOF', 'HTMLEOF', "f'", 'f"', '.format(', '% (']
    for artifact in python_artifacts:
        if artifact in html:
            errors.append(f"Python artifact found: '{artifact}' — Python must never touch JS/HTML content")

    # No double main.js
    main_js_count = html.count('main.js')
    if main_js_count > 1:
        errors.append(f"main.js referenced {main_js_count}x — should be exactly 1")

    # Syntax check all inline script blocks
    scripts = re.findall(
        r'<script(?![\s\S]{0,10}(?:async|application/ld\+json|src=))[^>]*>([\s\S]+?)</script>',
        html
    )
    for i, script in enumerate(scripts):
        tmp = f'/tmp/mpw_check_script_{i}.js'
        with open(tmp, 'w') as f:
            f.write(script)
        result = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        if result.returncode != 0:
            errors.append(f"JS SYNTAX ERROR in script block {i}: {result.stderr.strip()[:300]}")
        try:
            os.remove(tmp)
        except:
            pass

    # ── API/MODEL ──────────────────────────────────────────────────
    # Check if this is a Claude API tool
    if 'claude-proxy' in html or 'anthropic' in html.lower():
        # Correct model string
        if 'claude-sonnet-4-6' not in html:
            if 'claude-sonnet-4-5' in html:
                errors.append("Wrong model: claude-sonnet-4-5 found — must be claude-sonnet-4-6")
            elif 'claude-sonnet-4-20250514' in html:
                errors.append("Wrong model: claude-sonnet-4-20250514 found — must be claude-sonnet-4-6")
            else:
                errors.append("Model string claude-sonnet-4-6 not found in API tool")

        # Correct proxy URL
        if 'classy-haupia-be8e43' not in html:
            errors.append("Correct proxy URL not found — must use classy-haupia-be8e43.netlify.app/.netlify/functions/claude-proxy")

        # No assistant prefill
        if '"assistant"' in html and 'prefill' in html.lower():
            errors.append("Assistant prefill detected — this returns empty response body")

    # ── SEO ────────────────────────────────────────────────────────
    # GA4
    if 'G-79VB543KCT' not in html:
        warnings.append("GA4 tag G-79VB543KCT not found")

    # Canonical URL
    if 'rel="canonical"' not in html:
        warnings.append("No canonical URL found")

    # Favicon
    if '/favicon.svg' not in html:
        warnings.append("Favicon link not found")

    # ── FILE SIZE ──────────────────────────────────────────────────
    size = len(html.encode('utf-8'))
    if size > 200000:
        errors.append(f"File too large: {size:,} bytes — Cloudflare blocks files over 200KB (will save as HTML not deploy)")
    elif size > 180000:
        warnings.append(f"File approaching 200KB limit: {size:,} bytes")

    # ── RESULTS ────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"MPW PRE-COMMIT CHECK: {filename}")
    print(f"{'='*60}")
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
    print(f"Div balance: {opens} opens, {closes} closes")
    print(f"Script blocks checked: {len(scripts)}")

    if warnings:
        print(f"\n⚠  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"   {w}")

    if errors:
        print(f"\n✗  ERRORS ({len(errors)}) — DO NOT COMMIT:")
        for e in errors:
            print(f"   {e}")
        print(f"\n{'='*60}")
        print("COMMIT BLOCKED — fix all errors before committing")
        print(f"{'='*60}\n")
        return False
    else:
        print(f"\n✓  ALL CHECKS PASSED")
        print(f"{'='*60}")
        print("Safe to commit.")
        print(f"{'='*60}\n")
        return True


def check_article_page(filepath):
    """Lighter verification for article HTML pages."""
    errors = []

    with open(filepath, encoding='utf-8') as f:
        html = f.read()

    filename = os.path.basename(filepath)

    # Div balance
    opens = len(re.findall(r'<div', html))
    closes = len(re.findall(r'</div>', html))
    if opens != closes:
        errors.append(f"UNBALANCED DIVS: {opens} opens, {closes} closes")

    # Ends with </html>
    if not html.strip().endswith('</html>'):
        errors.append("File does not end with </html>")

    # No Python artifacts
    for artifact in ['PYEOF', 'JSEOF', 'HTMLEOF']:
        if artifact in html:
            errors.append(f"Python artifact found: '{artifact}'")

    # File size
    size = len(html.encode('utf-8'))
    if size > 200000:
        errors.append(f"File too large: {size:,} bytes (Cloudflare 200KB limit)")

    # GA4
    if 'G-79VB543KCT' not in html:
        errors.append("GA4 tag not found")

    print(f"\nARTICLE CHECK: {filename} — {size:,} bytes")
    if errors:
        for e in errors: print(f"  ✗ {e}")
        return False
    else:
        print(f"  ✓ All checks passed")
        return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 mpw_precommit_check.py <filepath> [filepath2 ...]")
        print("       python3 mpw_precommit_check.py --tool tools/suno-prompt-optimizer.html")
        print("       python3 mpw_precommit_check.py --article articles/my-article.html")
        sys.exit(1)

    all_passed = True
    mode = '--tool'  # default

    files = []
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            mode = arg
        else:
            files.append(arg)

    for filepath in files:
        if not os.path.exists(filepath):
            print(f"✗ File not found: {filepath}")
            all_passed = False
            continue

        if mode == '--article':
            result = check_article_page(filepath)
        else:
            result = check_tool_page(filepath)

        if not result:
            all_passed = False

    sys.exit(0 if all_passed else 1)


def scan_secrets(filepath):
    """Scan any file for raw API tokens before GitHub upload. Run on ALL files."""
    import re
    with open(filepath, encoding='utf-8', errors='replace') as f:
        content = f.read()

    patterns = [
        (r'ghp_[A-Za-z0-9]{36}', 'GitHub personal access token'),
        (r'sk-ant-[A-Za-z0-9\-]{90,}', 'Anthropic API key'),
        (r'AKIA[A-Z0-9]{16}', 'AWS access key'),
    ]

    found = []
    for pattern, name in patterns:
        for match in re.finditer(pattern, content):
            found.append((name, match.group()[:16] + '...'))

    if found:
        print(f"\n⛔ SECRETS DETECTED in {filepath} — DO NOT UPLOAD TO GITHUB:")
        for name, preview in found:
            print(f"   {name}: {preview} [redact to placeholder first]")
        return False

    print(f"✓ No secrets in {filepath}")
    return True


if __name__ == '__main__' and '--scan' in sys.argv:
    # Usage: python3 mpw_precommit_check.py --scan file1 file2 ...
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    all_clean = all(scan_secrets(f) for f in files)
    sys.exit(0 if all_clean else 1)

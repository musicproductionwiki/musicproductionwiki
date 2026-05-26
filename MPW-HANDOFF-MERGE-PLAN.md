# MPW Handoff Merge Plan
## Sessions 69–73: Consolidating All Documents Into Living Masters

*Written: May 26, 2026 (Session 68)*
*Author: Claude (Co-CEO, MPW)*

---

## Why We Are Doing This

Every session Claude starts cold. The handoff documents are the only memory. Right now those documents are fragmented — masters plus session appends spread across GitHub — and Claude has to reconcile them mentally every session. This causes mistakes, missed context, and wasted time (Session 68 is a direct example: the wrong design system, the wrong model string, the CSS conflicts — all things that were documented but not consolidated).

After this merge project, Claude will have six clean, authoritative, fully current master documents. No appends. No reconciliation. One read per document, complete picture.

---

## Ground Rules for All Merge Sessions

1. **One file per session. No exceptions.** The context window is finite. Splitting focus across files risks dropping content.
2. **Read everything first, write nothing.** Every source file gets read and understood before a single line of the merged master is written.
3. **Flag every conflict.** If two sources contradict each other (e.g. model string changed, rule updated), flag it explicitly and ask Steve to decide — never resolve silently.
4. **No truncation tolerance.** Every merged file gets a byte count and line count compared against the sum of its sources. If numbers don't add up, stop and investigate.
5. **Write in sections to disk, concatenate as raw bytes.** Never write a 200KB file in one Python string operation.
6. **Steve approves before upload.** Present each file, wait for approval, then commit. Never auto-commit a merged master.
7. **After upload, delete the merged appends from GitHub.** Clean repo is the goal.
8. **Leave `mpw_tools_master_spec_v2.md` completely alone.**
9. **Leave S53/S56 snapshots in place** — clearly labeled historical reference, not deleted.

---

## Source Files Inventory

### Master Documents (merge targets)
| File | Size | Priority | Status |
|------|------|----------|--------|
| `MPW-HANDOFF-CORE.md` | 238KB | 1 — most critical | ✅ MERGED Session 69 |
| `MPW-HANDOFF-TECH.md` | 158KB | 2 | ✅ MERGED Session 70 |
| `MPW-HANDOFF-SCRIPTS.md` | 126KB | 3 | ✅ MERGED Session 71 |
| `MPW-HANDOFF-CONTENT.md` | 49KB | 4 | ✅ MERGED Session 72 |
| `MPW-HANDOFF-ARTICLES.md` | 24KB | 5 | ✅ MERGED Session 72 |
| `MPW-HANDOFF-BIBLE.md` | 127KB | 6 — largest, most stable | ✅ MERGED Session 73 |
| `MPW-NEVER-RULES.md` | 26KB | 7 — canonical never rules | ✅ BUILT Session 75 |

### Session Appends to Merge (GitHub root)
| File | Size | Target Master |
|------|------|---------------|
| `session65_core_append.md` | 9.3KB | CORE |
| `session65_tech_append.md` | 10KB | TECH |
| `session65_scripts_append.md` | 6.3KB | SCRIPTS |
| `session65b_core_append.md` | 7.6KB | CORE |
| `session65b_tech_append.md` | 8.2KB | TECH |
| `session65b_scripts_append.md` | 8.1KB | SCRIPTS |
| `session66_core_append.md` | 10.2KB | CORE |
| `session66_tech_append.md` | 15KB | TECH |
| `session66_scripts_append.md` | 13.6KB | SCRIPTS |
| `session68_core_append.md` | 4.5KB | CORE |
| `session68_tech_append.md` | 2.5KB | TECH |
| `session68_scripts_append.md` | 1.3KB | SCRIPTS |

### Session Appends (project files only — not yet on GitHub)
| File | Size | Target Master |
|------|------|---------------|
| `session67_core_append.md` | 8KB | CORE |
| `session67_tech_append.md` | 8KB | TECH |
| `session67_scripts_append.md` | 8KB | SCRIPTS |

### Historical Snapshots (read for diff, do not delete)
| File | Purpose |
|------|---------|
| `MPW-HANDOFF-CORE-S53.md` | State at Session 53 — reference for what changed since |
| `MPW-HANDOFF-CORE-S56.md` | State at Session 56 — reference for what changed since |
| `MPW-HANDOFF-TECH-S53.md` | Same |
| `MPW-HANDOFF-TECH-S56.md` | Same |
| `MPW-HANDOFF-SCRIPTS-S53.md` | Same |
| `MPW-HANDOFF-SCRIPTS-S56.md` | Same |
| `MPW-HANDOFF-CONTENT-S53.md` | Same |
| `MPW-HANDOFF-CONTENT-S56.md` | Same |
| `MPW-HANDOFF-ARTICLES-S53.md` | Same |
| `MPW-HANDOFF-ARTICLES-S56.md` | Same |
| `MPW-HANDOFF-BIBLE-S53.md` | Same |
| `MPW-HANDOFF-BIBLE-S56.md` | Same |

---

## Session 69 — CORE Merge ✅ COMPLETE

**Result:** MPW-HANDOFF-CORE.md — 238KB — merged S65/S65b/S66/S67/S68 core appends
**Target:** `MPW-HANDOFF-CORE.md` (208KB)
**Sources:** Current CORE + S53 snapshot + S56 snapshot + session65/65b/66/67/68 core appends

### Step-by-Step Plan

**Step 1: Read all sources**
- Read `MPW-HANDOFF-CORE.md` in full — note all major sections
- Read `MPW-HANDOFF-CORE-S56.md` — diff against current, note anything in S56 not in current
- Read `MPW-HANDOFF-CORE-S53.md` — diff against S56, note anything in S53 not carried forward
- Read all 5 core appends (65, 65b, 66, 67, 68) in order — build a list of every addition

**Step 2: Conflict resolution**
Flag and resolve before writing:
- Model string history: `claude-sonnet-4-5` → `claude-sonnet-4-6` (current: `claude-sonnet-4-6`)
- Tool count: carried forward from most recent append
- Any NEVER rules that were modified across sessions
- Any pending actions that were completed and should be removed

**Step 3: Write merged CORE in sections to disk**
Write each major section as a separate file:
- `core_s1_state.md` — Current state table (articles, Bible, tools, model, proxy URL)
- `core_s2_never_rules.md` — ALL never rules consolidated, deduped, latest version wins
- `core_s3_tools.md` — All tools built, URLs, SHAs, features
- `core_s4_pending.md` — Single canonical pending actions list
- `core_s5_architecture.md` — Site architecture, paths, infrastructure
- `core_s6_queue.md` — Priority queue for next sessions
- `core_s7_history.md` — Session history log

**Step 4: Concatenate as raw bytes → verify**
- Compare byte count against sum of sources (merged should be >= current master)
- Check line count
- Verify no section headers from source files are missing

**Step 5: Present to Steve for approval**

**Step 6: Commit to GitHub, delete merged appends**
Files to delete after merge: `session65_core_append.md`, `session65b_core_append.md`, `session66_core_append.md`, `session67_core_append.md` (from project), `session68_core_append.md`

---

## Session 70 — TECH Merge ✅ COMPLETE

**Result:** MPW-HANDOFF-TECH.md — 158KB — merged S65/S65b/S66/S67/S68 tech appends
**Target:** `MPW-HANDOFF-TECH.md` (124KB)
**Sources:** Current TECH + S53/S56 snapshots + session65/65b/66/67/68 tech appends

### Key content to integrate:
- CSS safety rules (append-only, fingerprint strings, mobile rendering fixes)
- JS writing rules (never Python interpolation, always heredoc + node --check)
- Nav block extraction pattern (div-depth tracking)
- style.css conflict rules (never load on tool pages)
- API/proxy patterns (model string, proxy URL, response parsing)
- Bible page technical fixes (Compression Bible, EQ Bible mobile rendering)
- Pre-commit verification checklist
- File size limits (Cloudflare 200KB)
- Upload methods (GitHub token vs web uploader)

### Same 6-step process as Session 69.

---

## Session 71 — SCRIPTS Merge ✅ COMPLETE

**Result:** MPW-HANDOFF-SCRIPTS.md — 126KB — SHA 806ac1bd
**Appends deleted:** session65/65b/66/67/68 scripts appends — all confirmed deleted
**Bonus:** sitemap.xml fixed — 36 missing tool URLs added — 744→780 — SHA 218d8bda
**Key conflicts resolved:**
- Model string: `claude-sonnet-4-6` locked (S67 had wrong string)
- v3/v4/v5 tools: equal weight — v5 dispatch is unified entry point
- Tool count corrected to 41 live
- mpw_tools_v6_writer.py: clearly marked NOT YET BUILT
- mpw_writer.py 4 pending updates: still blocking article batches — flagged URGENT
- mpw_bible_writer.py: 650wpm + nav + v5.3 — still blocking T1 batch — flagged URGENT
- Tool/Bible card nav sync: both sides broken — flagged as open action item

**Target:** `MPW-HANDOFF-SCRIPTS.md` (83KB)
**Sources:** Current SCRIPTS + S53/S56 snapshots + session65/65b/66/67/68 scripts appends

### Key content to integrate:
- Nav block extractor (div-depth balanced version)
- JS syntax checker
- GitHub restore script
- Tool build pre-commit checklist script
- Bible writer scripts
- Upload scripts
- Delay calculator script
- Any new utility functions added in sessions 65–68

### Same 6-step process.

---

## Session 72 — CONTENT + ARTICLES Merge ✅ COMPLETE

**Result:** MPW-HANDOFF-CONTENT.md (38KB) + MPW-HANDOFF-ARTICLES.md (14KB) — SHA 346e9a11 / df11f348
**Appends integrated:** S39/S41/S47/S51/S52/S53/S54/S55/S56/S57/S58/S60 (CONTENT); S39/S41/S46/S51/S52/S53/S54/S55/S56/S57/S58/S60 (ARTICLES)
**Key conflicts resolved:**
- Bible entry count: corrected to 225 (reverb.html v1.6 + chorus.html v5.2 both confirmed LIVE)
- Batch pipeline: S60 state used as canonical (tools-over-entries strategy + full type catalog)
- Content standards: S52 consolidation (28→23 sections) + S53/S54 additions layered on top
- Pending owner actions: deduplicated across all sessions — single table per doc
- Article count: unanimous 526 — confirmed unchanged since Batch 08

**Target:** Both `MPW-HANDOFF-CONTENT.md` (49KB) and `MPW-HANDOFF-ARTICLES.md` (24KB)
**Sources:** Current files + S53/S56 snapshots + any content/article appends

These two files are smaller and more stable — combining them into one session is reasonable. If either turns out to have significant conflicts, split into two sessions.

### Key content to integrate (CONTENT):
- Article word count standards
- Bible entry word count standards
- Read time calculations
- Gold standard template references
- Content queue updates

### Key content to integrate (ARTICLES):
- Article catalog (verify count matches GitHub)
- Any new articles added in sessions 65–68
- Quality audit notes

---

## Session 73 — BIBLE Merge ✅ COMPLETE

**Result:** MPW-HANDOFF-BIBLE.md — 127KB — GitHub audit + corrections pass — no appends existed
**Corrections:** entry count 226→223 (GitHub confirmed), S61 count 231→223, gold standard updated to reverb.html v1.6
**Target:** `MPW-HANDOFF-BIBLE.md` (128KB) — largest doc, most stable
**Sources:** Current BIBLE + S53/S56 snapshots

**Note:** The Bible handoff is the most stable — no session appends target it directly. This session is primarily about integrating S53/S56 snapshot content that may not have made it into the current master, and doing a full audit of the Bible entry catalog.

### Key things to verify:
- Bible entry count (currently 223)
- All entry slugs present and correct
- Batch history accurate
- Priority queue for next Bible entries current

---

## Session 75 — MPW-NEVER-RULES.md Build ✅ COMPLETE

**Result:** MPW-NEVER-RULES.md — 26KB — 95 rules — 7 categories — sourced from CORE, TECH, SCRIPTS, BIBLE, SESSION-START, CONTINUITY-MASTER-PLAN, chat history
**Changes applied:** SESSION-START top 20 summary updated. MERGE-PLAN marked complete.

**Goal:** Create the 7th master document — a single canonical source for every never rule ever added to this project.

**Why:** Never rules are currently scattered across CORE, TECH, SCRIPTS, BIBLE, SESSION-START, and session history. Claude must reconcile them mentally every session. One file eliminates that entirely.

**Sources to read (in order):**
1. `MPW-HANDOFF-CORE.md` — GitHub
2. `MPW-HANDOFF-TECH.md` — GitHub
3. `MPW-HANDOFF-SCRIPTS.md` — GitHub
4. `MPW-HANDOFF-BIBLE.md` — project file
5. `MPW-SESSION-START.md` — current
6. `MPW-SESSION-CONTINUITY-MASTER-PLAN.md` — project file
7. **Chat history search** — `conversation_search` for "never rule", "NEVER", "added rule", "new rule" — catches anything discussed but never documented

**Structure of MPW-NEVER-RULES.md:**
- Each rule: the rule, session added, reason it exists, enforcement (script vs manual)
- Grouped by category: CSS/JS | API/Proxy | Commits | Content | Bible | Tools | General
- `mpw_precommit_check.py` enforcement column — mechanical rules flagged as SCRIPT-ENFORCED
- Load order: every session, after SESSION-START, before any other master

**Changes to other documents after S75:**
- SESSION-START: never rules table becomes top 20 summary — links to MPW-NEVER-RULES.md
- CORE: never rules section replaced with "See MPW-NEVER-RULES.md"
- TECH/SCRIPTS/BIBLE: never rules sections marked "See MPW-NEVER-RULES.md"
- SESSION-CONTINUITY-MASTER-PLAN: never rules layer updated to reference new file

**Session end protocol addition (permanent from S75):**
If a new never rule is identified this session → update MPW-NEVER-RULES.md before presenting files for approval. SESSION-START summary updated second. Nowhere else.


---

## Post-Merge Rules (Permanent, Starting Session 74)

Once all merges are complete, these rules apply forever:

1. **No more append files.** Every session ends by updating the masters directly in the project. Steve uploads the updated masters at session end.

2. **State table updated every session.** First thing Claude writes in any session: update the state table in CORE (article count, Bible count, tool count, last commit SHA, model string). Last thing: update it again with session results.

3. **Never rules are maintained in MPW-NEVER-RULES.md only.** If a never rule is added this session, it goes into MPW-NEVER-RULES.md first. SESSION-START summary updated second. Never anywhere else.

4. **Pending actions live in CORE only.** One list, one place, always current.

5. **Session start protocol:**
   - Read CORE first (state table, pending actions)
   - Read MPW-NEVER-RULES.md (every session — non-negotiable)
   - Read relevant specialist file (TECH for tool work, BIBLE for Bible work, etc.)
   - Confirm state with Steve before beginning work

6. **Session end protocol:**
   - Update state table in CORE
   - Add any new never rules to CORE never rules section
   - Update pending actions in CORE
   - Update specialist file if tech/script patterns changed
   - Present updated files to Steve
   - Steve uploads to project and GitHub

---

## Risk Register

| Risk | Mitigation |
|------|------------|
| Context window overflow reading all sources | Read in order, summarize each before reading next |
| Truncation when writing large merged file | Write in sections, concatenate as raw bytes, verify byte count |
| Content lost in conflict resolution | Flag every conflict, Steve decides, never resolve silently |
| Wrong content merged into wrong file | Each section written to named temp file, reviewed before concatenation |
| Appends deleted before confirmed in master | Never delete appends until merged master is committed and verified on GitHub |
| Session interrupted mid-merge | All temp section files preserved on disk, resumable next session |

---

## Success Criteria

Each merge session is complete when:
- [ ] Merged master byte count >= current master + appends combined
- [ ] All section headers from all sources present in merged file
- [ ] All never rules from all appends present in merged never rules section
- [ ] All tool entries from all appends present
- [ ] All pending actions reconciled (completed ones removed, new ones added)
- [ ] Steve has approved the file
- [ ] File committed to GitHub
- [ ] Source appends deleted from GitHub
- [ ] No other files modified


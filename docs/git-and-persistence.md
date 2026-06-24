# Git Workflow & Persistence

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: one-time host setup; branching & auto-merge-to-main; per-EA save/persistence; checkpointing & failure recovery; safe reset; and version-control use.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## ONE-TIME SETUP (run once on the host before the first scheduled run)

Assumes the repo is initialized with **at least one commit**. The START-OF-RUN procedure creates
the `vetting/` tree on first run if absent.

### 1. Authentication

**Option A — SSH deploy key (recommended for scheduled/CI runs)**

```bash
ssh-keygen -t ed25519 -C "gauntlet-ea-agent" -f ~/.ssh/gauntlet_agent
# Add ~/.ssh/gauntlet_agent.pub as a Write-access deploy key:
# GitHub repo → Settings → Deploy keys → Add deploy key
cat ~/.ssh/gauntlet_agent.pub
# Register the custom key so git uses it automatically (else SSH ignores it):
cat >> ~/.ssh/config << 'SSHEOF'
Host github.com
  IdentityFile ~/.ssh/gauntlet_agent
  IdentitiesOnly yes
SSHEOF
chmod 600 ~/.ssh/config
git remote set-url origin git@github.com:<org>/<repo>.git
ssh -T git@github.com
```

**Option B — Personal Access Token (PAT)**

```bash
# Fine-grained PAT, Contents: read+write, at
# https://github.com/settings/personal-access-tokens
git remote set-url origin https://<PAT>@github.com/<org>/<repo>.git
git ls-remote origin
```

Do not store credentials in any tracked file. Confirm auth before the first run:

```bash
git push --dry-run origin HEAD   # expect "Everything up-to-date" or a push plan, not an auth error
```

### 2. Git identity

```bash
git config user.name "Gauntlet EA Agent"
git config user.email "gauntlet-agent@your-org.com"
git config user.name && git config user.email   # empty output → commit will fail
```

### 3. .gitignore

```
.DS_Store
Thumbs.db
*.swp
*.swo
.env
*.pem
*.key
.claude/
*.tmp
*.log
vetting/.run.lock
```

### 4. Manual scoring and validation

There are **no required external scoring or validation scripts**. Score and validate manually from
this `CLAUDE.md` file:

- Use **SCORING** as the single source of truth for weights, multipliers, Gate-B ceilings, ROR
  suppression, rounding, bands, and Overall calculation.
- Use **MANUAL VALIDATION CHECKLIST** as the commit gate before every commit and again at end of
  run.
- Do not rely on separate scoring scripts, separate validation scripts, spreadsheets, calculators, or hidden helper code
  as an authority. If you use arithmetic scratch work, reproduce the final calculation in the EA file so a
  human can audit it.
- Manual validation failure has the same effect as a failed commit gate: **fix the issue
  before committing**.

### 5. Scheduling (Claude Code Desktop)

Use the Scheduled Tasks sidebar; prompt `Run today's vetting pass`; daily cadence recommended.

> **Headless permission note:** unattended runs may pause on tool-use approval if permissions are
> `prompt`. Configure auto-approve, or pass `--dangerously-skip-permissions` only in a controlled
> environment you trust. With the manual validation checklist gating commits (item 4), the agent is instructed to stop before pushing a
> structurally broken index, even under auto-approve.

**Linux alternative (wrapper script so cron has PATH + key):**

```bash
#!/bin/bash
# /usr/local/bin/run-gauntlet.sh  (chmod +x)
for f in ~/.bash_profile ~/.profile; do [ -f "$f" ] && source "$f" && break; done
# export ANTHROPIC_API_KEY="your-key-here"   # if profile loading is unreliable
cd /path/to/repo
claude -p "Run today's vetting pass" --max-turns 50 2>&1 | tee /var/log/gauntlet-agent.log
```

```
# /etc/cron.d/gauntlet-agent
0 7 * * * youruser /usr/local/bin/run-gauntlet.sh
```

> **`--max-turns` sizing:** one EA end-to-end (search, fetch, rulebook check, gate, profile, ROR,
> score, manual-validate, commit, push, verify) is many tool calls. If runs stop mid-EA, raise it.

---

## BRANCHING MODEL: AUTO-MERGE TO MAIN (MANDATORY)

`main` is canonical. Every completed, **manually validated** EA lands on `main` automatically — the agent
merges; it never waits for human approval. Detect the environment in the START-OF-RUN GIT
PROCEDURE:

> **PREFER DIRECT-TO-`main` — branches and PRs are a last resort, not a default.** Whenever the
> environment permits committing to `main` (test once with `git push --dry-run origin HEAD:main`,
> or simply attempt the direct push), **write directly to `main`**: complete the work, run all
> required validation checks, commit, `git push origin HEAD:main`, and verify the content is present
> on `origin/main`. **Do not create feature branches, working branches, or pull requests when a
> direct push works** — they are unnecessary overhead and leave stale refs to clean up. Use a branch
> **only** when (a) the environment/workflow *forbids* direct pushes to `main`, or (b) a
> `recovery-YYYY-MM-DD-HHMM` branch is needed to preserve unresolved work (START-OF-RUN GIT
> PROCEDURE). If a branch is created for reason (a), it must be **merged, verified on `origin/main`,
> and then deleted** once its purpose is fulfilled (BRANCH CLEANUP RULE).

- **Direct-push (preferred default)** — push completed vetting directly to `main` (`git push origin
  HEAD:main`), then verify by slug/content on `origin/main`. No branch, no PR.
- **Branch + PR (only if direct push is blocked)** — if and only if the environment refuses a direct
  push to `main`, push each completed EA to a single working branch, then auto-merge it into `main`
  (open a PR only if the workflow requires one), verify on `origin/main`, and **delete the working
  branch** afterward.

Invariant: **a completed, manually validated EA is on `main` before the next EA begins.** Never strand
completed vetting on a working branch. Do not create daily branches or extra feature branches; the
only other branches are `recovery-YYYY-MM-DD-HHMM` (start-of-run recovery only).

**The rule (mandatory, no exceptions):**
- All completed work that has passed every validation check must be pushed **directly to `main`**
  in accordance with this workflow. It must **not** remain on a feature branch, a working branch,
  or an unmerged pull request.
- Once validation passes: **commit → push → verify the changes are present on `origin/main`**
  (grep the slug / content on `origin/main`, not local SHA equality) **before continuing with the
  next EA.**
- If a **merge conflict, synchronization issue, or validation failure** occurs at any point,
  **STOP and report the issue** — preserve the work (recovery branch per the START-OF-RUN GIT
  PROCEDURE) and hand off to the operator. **Never bypass, force, or skip the process** to push
  work through, and never proceed to the next EA on stale or unverified state.

### BRANCH CLEANUP RULE (mandatory — keep the repository clean)

`main` is the single source of truth; **no stale or abandoned branches may accumulate over time.**

- **Once all completed work has been validated, merged into `main`, and verified present on
  `origin/main`, delete the corresponding working branch — both locally and remotely (if it was
  pushed).** A working branch that has been fully merged has served its purpose and must not be
  retained.
- **Do the deletion only AFTER the `origin/main` content verification passes** (grep the
  slug/content on `origin/main`, not SHA equality). Never delete a branch whose work is not yet
  confirmed on `main` — that would strand or lose the work, violating HARD RULE 14.
- **Exception — branches to KEEP:** `recovery-YYYY-MM-DD-HHMM` branches created to preserve
  unresolved/unfinished work or to investigate an issue. These are retained until the operator
  resolves them; do not auto-delete a recovery branch.
- Cleanup commands (only after verification on `origin/main`):
  ```bash
  git checkout main                                  # never delete the branch you are on
  git branch -d <working-branch>                     # local; -d (not -D) so an unmerged branch is refused
  git push origin --delete <working-branch>          # remote, if it was pushed
  git remote prune origin                            # drop stale remote-tracking refs
  ```
  Use `git branch -d` (lowercase) deliberately: it **refuses** to delete a branch that is not fully
  merged into `main`, which is a final safety check that the work really landed. If `-d` refuses,
  treat it as a STOP-and-report signal — do **not** force with `-D`.

---

## PER-EA EXECUTION & SAVE WORKFLOW + PERSISTENCE (MANDATORY)

Vet EXACTLY ONE EA at a time. No batching, no parallel vetting, no delayed persistence. Each EA is
an atomic transaction:

**`Gate → Profile → Score → Verdict → Manual Validate → Commit → Push → Verify → Continue`**

### Sequence

1. Select ONE EA from `queue.jsonl` (state → `vetting`).
2. **Gate A** (pre-screen). If excluded: write `excluded/<slug>.md`, add an index row with
   `verdict:"Excluded"`, set queue state `excluded`, run **Manual Validate → Commit → Push → Verify**,
   continue. (Steps 3–9 skipped.)
3. **Gate B** (mechanism transparency) and **Gate C** (per-firm legality), computing each per-firm
   verdict against the **current** rulebook version (refresh first if stale).
4. Build the **profile from fetched public pages only**; complete the Evidence Matrix, Source
   Reliability Assessment, Mechanism Inference Confidence, Unverified Claims, evidence tiers, and
   `best_tier` per the EA-level rule.
5. Run the **risk-of-ruin** analysis, defaulting to `NON-ESTIMABLE` unless public **real-money**
   Tier 0/1/2A
   trade-level history supports estimation.
6. **Steelman the skeptic** — write `## Why This Will Probably Fail` *before* scoring.
7. **Score** — latent public-evidence assessment × multiplier / Gate ceilings → adjusted dimensions
   → weighted Overall + band.
8. Assign the **Deployment Verdict** (buckets), set the binding criterion.
9. **Duplicate detection.**
10. **Update files** (order): `eas/<slug>.md` (or `excluded/<slug>.md`) → `master_index.jsonl` →
    `rankings/*` (re-sort buckets) → `deployable/` (only if Deployable) → `queue.jsonl` (state
    `completed`/`excluded`) → `source_archive/YYYY-MM-DD.md` → `daily/YYYY-MM-DD.md` →
    `README.md` (refresh counts, shortlist top picks, and latest-pass link).

### Manual Validate → Commit → Push → Verify (the canonical persistence procedure)

**Manual Validate (gates the commit):**

Complete **MANUAL VALIDATION CHECKLIST** for the EA and current tree. If any item fails, fix the
inconsistency and repeat the checklist until it passes. Do not commit a failing tree. Also confirm
markdown links resolve and cross-references are intact.

**Commit:**

```bash
git add vetting/
git commit -m "vet: <ea-name> — <verdict>" --trailer "Gauntlet-Host:$(hostname)"
```


`nothing to commit` is **not** a failure — continue. Message examples:

```bash
git commit -m "vet: add <ea-name> — Watchlist (lacks funded-account evidence only)"
git commit -m "vet: exclude <ea-name> — disguised martingale (zone recovery)"
git commit -m "vet: re-check <ea-name> after FundedNext rulebook v3"
git commit -m "rulebook: refresh funding-pips to v2 (trailing max-DD change)"
```

**Push, then auto-merge to `main`:**

```bash
# Direct-push:
git push origin HEAD:main
# Branch + PR:
git push -u origin <working-branch>
# then merge the working branch's PR into main (open one if none exists)
```

**Verify (mandatory) — confirm the EA's row reached `main`, not just that the file exists:**

```bash
git fetch origin
git show origin/main:vetting/master_index.jsonl | grep -q "\"slug\":\"<slug>\"" \
  && echo "verified on main" \
  || { echo "EA row NOT on main — repository sync/merge failure."; }
```

A squash/merge commit gives `main` a different SHA than `HEAD`, so verify by the **grep for the
slug on `origin/main`**, not by SHA equality. If verification fails: STOP vetting, report a
sync/merge failure, do not continue.

Persistence is mandatory before selecting the next EA. Every verified push is a recovery
checkpoint; every merge to `main` is the canonical record. Never accumulate unpushed/unmerged work.

---

## CHECKPOINTING & FAILURE RECOVERY

Sessions can terminate anytime (API failure, context limit, network drop, power loss). Because each
completed EA is committed, pushed, and merged before the next begins, interruption is safe:

- **After every completed EA:** persist immediately; never postpone saves; never rely on in-memory
  state.
- **If interrupted mid-EA:** partial work is lost — acceptable, since completed EAs are already on
  `main`.
- **The next run resumes from GitHub:** it reads the JSONL index, refreshes stale rulebooks,
  reviews outcomes, and picks up from the next un-vetted EA. Never reconstruct an interrupted run
  from memory.

Session priority during long runs: (1) complete and save the current EA, (2) keep the database
valid (manual validation passes), (3) preserve evidence and source links, (4) continue only after
persistence succeeds.

---

## SAFE RESET POLICY

Use `git reset --hard origin/main` only when ALL hold: explicitly configured for this scenario;
remote integrity guaranteed; unfinished work already preserved (stash or recovery branch). Never
silently destroy potentially valuable vetting.

---

## VERSION CONTROL UTILIZATION

Preserve, in history: verdict evolution and score changes as evidence/rules change; rulebook
version history and the re-checks each version triggered; community-sentiment shifts and emerging
red-flag patterns; exclusion history (which mechanisms recur across vendors and rebrands); and
**outcome records** (predicted vs realized). When a rulebook change flips a legality verdict, keep
the prior verdict in the file's history with the rulebook version that produced it — the change is
itself a finding.

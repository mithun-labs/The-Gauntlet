# Changelog — The Gauntlet

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: version history (v2 → v2.6).**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

> **v2.6 (modular documentation refactor).** Split the monolithic manual into `CLAUDE.md` (entry point: role, hard rules, run lifecycle, documentation map, pointers) plus nine single-source-of-truth docs under `docs/` (changelog, research protocol, rulebooks, scoring & verdicts, output standard, data model, validation, git & persistence, outcomes). Every rule, workflow, threshold, and template was moved **verbatim** — no behavior, scoring, gate, or wording change. Added a documentation map/index and per-section pointers so an agent reading only `CLAUDE.md` still understands the architecture and can locate every rule.
>
> **What changed in v2 (audit fixes folded in).** Hard score caps replaced by graduated
> **evidence multipliers** so the highest-weighted dimensions discriminate again; **eligibility
> gates** (mechanism legality, unverifiable-mechanism ceiling, per-firm legality) separated from
> graded scoring; **Consistency** is now evidence-weighted; rankings are **bucketed by verdict**
> with defined Overall bands; the deployment max-drawdown threshold is **calibrated to firm
> limits**; canonical memory is **structured JSONL with a manual commit-gate checklist**; rulebook
> re-checks are **tiered and bounded**; an **outcome-tracking** loop provides calibration; and
> **multi-host concurrency** and **rebase/stash conflict** recovery are handled. Full-quality
> **Deployable** now requires funded-account evidence, so an *autonomously*-vetted EA tops out at
> **Watchlist** by design — the honest ceiling for what this agent can conclude alone.
>
> **v2.1 (maintenance).** Repaired corrupted instruction text caused by stray line-endings; added
> **latent score anchors** for run-to-run consistency; added a **Risk control-evidence ceiling** so
> vendor-*claimed* hard controls cannot earn full Risk credit (the un-multiplied dimensions were the
> soft spot); added a **drawdown metric-definition reconciliation** step; tightened the Myfxbook
> **attribution** caveat; and added a **target-firm relevance** flag. Gate A was reviewed and
> deliberately left aggressive: for an exclusionary screen, wrongly excluding a maybe-good EA is
> cheap, while wrongly keeping a disguised martingale is the failure this agent exists to prevent.
>
> **v2.1.1 (consistency pass).** Reconciled the Risk control-evidence ceiling with the
> adjusted-score formula and the dimensions table (it now appears in both, not just the scoring
> steps); clarified that the index summary fields are **required**, not optional, to match the
> validator; added a validator check that an `ESTIMABLE` ROR must carry a Tier 0/1
> `ror_evidence_tier`; and tightened two end-of-run wordings (ranking scope and the score formula).
>
> **v2.2 (firm-set expansion).** Added **The 5%ers** as a primary target firm and **Alpha Capital
> Group** and **Goat Funded Trader** as secondary/reference firms, and introduced the **primary vs
> reference** distinction: primaries gate the verdict (legality, permitted-at-/prohibited-at-all,
> and the tightest-firm ROR floor); reference firms are recorded but never gate, because they bar
> the commercial third-party EAs this agent mostly vets for procedural reasons (Alpha requires EA
> source code; Goat bans commercial challenge EAs). FTMO remains the one notable absent primary.
>
> **v2.2.1.** Added **leverage**, **max-lot / position-size limits**, and **weekend / overnight
> holding** fields to the per-firm rulebook extraction and template — sizing and holding
> constraints that bound EA viability and ROR (Alpha Capital's lot caps are the motivating case).
>
> **v2.2.2 (merge-reconciliation).** Re-applied three rules that an earlier-based v2.2/v2.2.1 draft
> had inadvertently dropped: **HARD RULE 14** (completed, validated work goes directly to `main` —
> never stranded; stop-and-report on conflict/sync/validation failure), the matching **BRANCHING
> MODEL "mandatory, no exceptions"** block, and the **forexcracked.com / cracked-"nulled" EA-site**
> discovery-source rule (low-trust: discovery + negative signals only, never positive evidence,
> cannot raise tier, malware caveat, ≤ weakest community tier). No other v2.2.x content changed.
>
> **v2.3 (Tier-2 over-restriction fix).** Closed the structural flaw where the entire Tier-2
> evidence band collapsed to **Avoid**, making genuine investigate-further candidates invisible
> (they were excluded from rankings). Three coupled changes: (1) **split Tier 2 into Tier 2A**
> (real-money, publicly inspectable trade-level record, demoted only by short track / low deposit /
> small sample) **and Tier 2B** (demo-only, hidden-history, or curve-fit) — both keep the Tier-2
> multiplier; (2) **narrowed Avoid criterion 4** so a `NON-ESTIMABLE` ROR forces Avoid only at
> Tier 2B/3/4 — real-money Tier 2A now lands on **Watchlist** with a binding criterion naming the
> evidence to chase; (3) **decoupled ROR-estimability from deposit/tier** — ROR is estimable from
> any real-money trade-level history (Tier 0/1/**2A**) at a tagged confidence (`ROR-High` for
> Tier 0/1, `ROR-Low` for Tier 2A), so a short/small real-money record no longer gets its Survival
> multiplier crushed to 0.20. **Deployable is unchanged and still unreachable autonomously:**
> gates 2, 3, and 7 continue to require a full ≥6-month Tier 0/1 record and `ROR-High`; Tier 2A and
> `ROR-Low` inform the score but never clear Deployable. Demo-only/hidden/curve-fit (Tier 2B) is
> still Avoided — the fix surfaces real-money candidates without loosening the demo distrust.
> Schema gains `TIER2A`/`TIER2B` and a `ror_confidence` field; the validator and the Overall-≥6.0
> contradiction-guard wording were reconciled to match.
>
> **v2.4 (architecture & consistency pass).** Eight fixes from a full-framework audit, mostly in the
> operational layer: (1) **Gate B Watchlist ceiling made reachable** — its definition no longer
> folds in "no risk-control evidence," so a black box with documented controls is constrained to
> Watchlist (not swallowed by Avoid criterion 3, which now does real work); (2) **multi-host guard
> fixed** — it compared the *shared* committer email (which can never distinguish two instances of
> this agent) and now compares the committing **host** via a `Gauntlet-Host:` commit trailer, with
> the committed heartbeat lock elevated to required for strict multi-host safety; (3)
> **duplicate-detection fingerprint reordered** to lead with mechanism (`mechanism|type|instruments|
> vendor`) so a rebrand under a new vendor name is caught as a variant, matching the stated intent;
> (4) **`best_tier` definition reconciled with Tier 2A** — the ≥6-month window is now a Tier-1
> requirement, not a clause that contradicted the <6-month Tier-2A sub-tier; (5) **re-check backlog
> drain** — the per-run N=10 cap no longer leaks: a Deployable/Watchlist backlog is drained before
> new discovery and the cap escalates if it persists; (6) **operator notification on halt** — a
> STOP-and-report now writes a committed `vetting/NEEDS_ATTENTION.md` that gates the next run, so an
> unattended halt is visible instead of silent; (7) **stale `vetting` queue rows reset** to
> `pending` at START-OF-RUN, recovering the queue state machine after an interrupted EA; (8)
> **`dimensions` made required and its Overall recompute exact** (Overall lands on a 0.05 grid), so
> every Overall is independently re-derived at commit time. No scoring weights or multipliers changed.
>
> **v2.5 (output presentation redesign).** Made the *generated pages* clean, consistent, and
> scannable without changing any scoring, gate, or verdict logic. Added an **OUTPUT PRESENTATION
> STANDARD** (answer-first inverted pyramid, one consistent page header + breadcrumb nav, a fixed
> verdict/evidence status-marker set with a no-emoji bracket fallback, tables for anything
> comparable, three-level hierarchy with dividers, and progressive disclosure via `<details>`).
> Added a **`vetting/README.md` landing page** (counts, shortlist top picks, legend, latest-pass
> link) as the navigation home. Redesigned the **per-EA page** to open with an **At-a-Glance card**
> and a **binding-criterion callout**, group the body into Profile / Evidence / Eligibility /
> Verdict zones, render **Scores as a transparent table**, and collapse the audit-trail tail into an
> appendix — the five mandatory pre-scoring sections stay H2 and in order, so the validator is
> unaffected. Redesigned the **daily report** (scoreboard + headline + grouped verdict tables) and
> the **rankings** (one consistent ranked table per list, formula in a callout, EAs as `[[slug]]`).
> Validator and checklist gained presentation checks (landing page fresh + links resolve, per-EA
> At-a-Glance card present and matching the verdict, rankings are tables).

# Validation Checklists

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: the manual validation checklist (commit gate) and the end-of-run checklist.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## MANUAL VALIDATION CHECKLIST (commit gate)

Before every commit, manually validate the current tree. A failed item aborts the commit until fixed.
Record any intentional exception in the relevant EA file and today's daily report.

### Repository and structure

- `vetting/master_index.jsonl` and `vetting/queue.jsonl` exist, parse as JSONL, and contain no
  duplicate `slug` values.
- Required directories exist: `daily/`, `eas/`, `excluded/`, `rulebooks/`, `rankings/`,
  `deployable/`, `outcomes/`, and `source_archive/`.
- Every non-excluded index row has `eas/<slug>.md`; every `Excluded` row has `excluded/<slug>.md`.
- Every EA/excluded file has exactly one matching `master_index.jsonl` row.
- Queue state matches the index: completed EAs are `completed`, excluded EAs are `excluded`, and no
  stale `vetting` row remains from an interrupted run.

### Index row requirements

For every non-excluded EA row, confirm:

- Required fields exist: `slug`, `ea_name`, `vendor`, `fingerprint`, `best_tier`, `overall`,
  `verdict`, `binding_criterion`, `firm_verdicts`, `ror_status`, `funded_evidence`,
  `mechanism_confidence`, source counts, `evidence_summary`, `dimensions`, and `updated`.
- `best_tier ∈ {TIER0, TIER1, TIER2A, TIER2B, TIER3, TIER4}`.
- `verdict ∈ {Deployable, Watchlist, Avoid, Excluded}`.
- `ror_status ∈ {ESTIMABLE, NON_ESTIMABLE}`.
- If `ror_status` is `ESTIMABLE`, `ror_evidence_tier` and `ror_confidence` are present, with
  `ror_evidence_tier ∈ {TIER0, TIER1, TIER2A}` and `ror_confidence` = `High` for Tier 0/1 or `Low`
  for Tier 2A (ROR is estimable only from real-money trade-level history; an `ESTIMABLE` claim
  resting on Tier 2B/3/4 is a contradiction and aborts the commit).
- `mechanism_confidence ∈ {High, Medium, Low, Unknown}`.
- Source counts are non-negative integers.
- `dimensions` is present with all seven adjusted scores, and the weighted sum recomputes to the
  stated Overall **exactly** (Overall lands on a 0.05 grid, so after half-up one-decimal rounding
  the recompute must equal the stated value — any difference is an arithmetic error and aborts).

### Rulebooks and firm verdicts

- All four primary rulebooks (FundedNext, Funding Pips, The 5%ers, The Funded Trader) exist with
  primary source URL, retrieval timestamp, agent-assigned version, and change note; any reference
  rulebook in use (Alpha Capital, Goat Funded Trader) likewise.
- Every non-excluded EA has firm verdicts for all four primary firms (FundedNext, Funding Pips,
  The 5%ers, The Funded Trader). Reference-firm verdicts (Alpha Capital, Goat Funded Trader) are
  recorded when assessed but are not required and never gate the verdict.
- Each firm verdict is `Permitted`, `Prohibited`, or `Conditional`, and cites the current rulebook
  version.
- No Deployable verdict depends on an `UNCONFIRMED` rule.

### Research-only evidence requirements

- Every surviving EA file includes `## Evidence Matrix`, `## Source Reliability Assessment`,
  `## Mechanism Inference Confidence`, `## Unverified Claims`, and `## Why This Will Probably Fail`
  before scoring.
- Every surviving EA file opens with the breadcrumb nav, one-line summary, `## At a Glance` card,
  and the binding-criterion blockquote; the card's verdict and Overall match `## Deployment Verdict`
  and the index row (OUTPUT PRESENTATION STANDARD).
- Every material performance metric has a tier and source, or `NOT REPORTED`.
- At least one negative-case search ran and is recorded.
- Affiliate/vendor/independent status is flagged for every source used.
- `source_archive/YYYY-MM-DD.md` rows include URL, retrieved timestamp, used-for target, and
  affiliate flag (`yes`, `no`, `n/a`, or `unknown`).

### Verdict and ranking requirements

- `Deployable` requires all Deployable quality gates, `funded_evidence:true`, `best_tier` TIER0 or
  TIER1, and `ror_status:ESTIMABLE` with `ror_confidence:High` from Tier 0/1 public trade-level or
  operator evidence. (Tier 2A / `ror_confidence:Low` never clears Deployable.)
- `NON_ESTIMABLE` ROR bars Deployable.
- A `Watchlist` EA may rest on Tier 2A real-money evidence with `ror_confidence:Low`; its
  `binding_criterion` names the caveat blocking Deployable (e.g. sub-6-month track, low deposit).
- `Avoid` with Overall ≥6.0 has been rechecked and either rescored or documented as a hard-gate
  Avoid.
- Rankings include only `Deployable` and `Watchlist` EAs, referenced as `[[slug]]`, and sorted by
  the stated purpose-specific formula.
- Today's daily report summarizes sources, best evidence found, major unverifiable claims, and why
  no Deployable verdict was assigned if none qualified.

---


## End-of-run checklist

*Run at run close (END-OF-RUN PROCEDURE, in `CLAUDE.md`): every box must be ticked before releasing the run lock.*

- [ ] Rulebook freshness check ran (72h); refreshed rulebooks versioned; re-check backlog recorded.
- [ ] Outcomes ledger reviewed; contradictions surfaced.
- [ ] Manual validation checklist completed on the final tree.
- [ ] Today's daily report written, grouped by verdict, with the scoreboard table and headline callout (OUTPUT PRESENTATION STANDARD).
- [ ] `vetting/README.md` refreshed: current counts, shortlist top picks, latest-pass link, legend; all relative links resolve.
- [ ] Every surviving EA page opens with the breadcrumb nav, one-line summary, **At-a-Glance card**, and the **binding-criterion blockquote** — and the card's verdict matches `## Deployment Verdict`.
- [ ] Every ranking file uses the shared header, states its composite formula in the callout, and is a ranked table listing EAs via `[[slug]]`.
- [ ] Every EA file: `NOT REPORTED` in unsourced fields; tier tag on every performance figure.
- [ ] Every surviving EA has `## Evidence Matrix`, `## Source Reliability Assessment`, `## Mechanism Inference Confidence`, and `## Unverified Claims` before scoring.
- [ ] At least one negative-case search ran for every EA (`scam`, `blown account`, `refund`, `losing`, or equivalent) and the result was recorded.
- [ ] Affiliate/vendor/independent status is flagged for every source used.
- [ ] Every surviving EA has `## Why This Will Probably Fail` before its scores.
- [ ] Every EA records a ROR result (estimate only from real-money Tier 0/1/2A trade-level history with a High/Low confidence grade, else `NON-ESTIMABLE`).
- [ ] Every per-firm verdict records the rulebook version judged against.
- [ ] Scores recorded as `latent × multiplier (or ceiling) = adjusted`; only adjusted Overall surfaced.
- [ ] `master_index.jsonl` and `queue.jsonl` updated and valid JSONL.
- [ ] No Deployable verdict without funded evidence; no Deployable with NON-ESTIMABLE ROR.
- [ ] No Avoid EA with Overall ≥ 6.0 **unless** rechecked and documented as a hard-gate Avoid (contradiction guard; matches the Index-row rule — a hard-gate Avoid may legitimately carry a high Overall).
- [ ] Rankings reference only `Deployable`/`Watchlist` EAs via `[[slug]]`, sorted within buckets.
- [ ] Source URLs preserved with retrieval date + affiliate flag.
- [ ] Every completed EA pushed and auto-merged to `main`, each verified by slug on `origin/main`.
- [ ] Working branch deleted (local + remote) after merge verified on `origin/main` — only recovery branches retained (BRANCH CLEANUP RULE); no stale branches left behind.
- [ ] `vetting/.run.lock` removed.

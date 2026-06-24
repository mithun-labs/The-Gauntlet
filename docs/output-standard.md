# Output Pages & Presentation Standard

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: the output presentation standard and every per-run page template (README, daily report, per-EA page, rankings).**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## OUTPUT PRESENTATION STANDARD (applies to every generated page)

These pages are read by a person deciding where to risk money. Design them so the **answer is
visible in seconds** and the **audit trail is one click away** — clean, consistent, scannable. The
rules below are mandatory and identical across pages; the checklist enforces them.

**1. Answer first (inverted pyramid).** Every page opens with a breadcrumb nav line, an H1 title, a
one-line plain-language summary, then a compact **At-a-Glance card** (a two-column table of the few
facts that decide the matter) and a **blockquote callout** carrying the single most important
takeaway. Detail follows; the deep audit trail goes last.

**2. One consistent header on every page**, in this exact order:
```
[← Index](../README.md) · [<sibling page>](…) · [<sibling page>](…)
# <Title>
*<one-line plain-language summary>*
```

**3. Status markers (fixed set — lead with them; never decorate prose).**
- Verdict: ✅ Deployable · 🟡 Watchlist · ⛔ Avoid · 🚫 Excluded
- Evidence basis: ◉ real-money · ◐ demo/partial · ○ unverified / claim-only

Use a marker only as the **first token** of a status field or table cell. If a workflow prefers no
emoji, replace each with its bracket label — `[DEPLOYABLE]` `[WATCHLIST]` `[AVOID]` `[EXCLUDED]` —
applied consistently everywhere.

**4. Tables for anything repeated or comparable** (rankings, metrics, per-firm legality, evidence).
One row per item, key columns only, the deciding column (Verdict / Overall) first or second. Tag
every figure with its evidence tier inline as `[T0]…[T4]`; unsourced stays `NOT REPORTED`.

**5. Visual hierarchy & spacing.** H1 = page; H2 = major zone; H3 = subsection; **never deeper**. A
`---` divider between major zones, one blank line between blocks, **bold** only for field labels.
Never stack two headings with no content between them.

**6. Progressive disclosure.** Wrap deep audit-trail / appendix sections in
`<details><summary>…</summary>` so the page reads as a clean narrative. **Never collapse** the
At-a-Glance card, the verdict, the skeptic steelman, or the mandatory pre-scoring evidence sections.

**7. Highlight, don't repeat.** State each fact once in its home section; elsewhere, link to it. The
three things to make impossible to miss are the **verdict**, the **Overall**, and the **binding
criterion**.

**8. Navigation home.** `vetting/README.md` is the landing page; every page's breadcrumb links back
to it. Keep links relative and resolving (checklist-enforced).

---

## OUTPUTS PER RUN

### 0. Landing page → `vetting/README.md` (refresh whenever counts or shortlists change)

The home page. Answers "what's in here and what's the best candidate" before any click.

```
[Rankings](rankings/) · [Latest pass](daily/<latest>.md) · [Rulebooks](rulebooks/)

# The Gauntlet — EA Vetting Index
*Adversarial vetting of MT5 EAs for prop-firm challenges and funded-account survival.*

> **State of the database:** ✅ <d> Deployable · 🟡 <w> Watchlist · ⛔ <a> Avoid · 🚫 <e> Excluded.
> Best candidate: [[<slug>]] — <verdict>, Overall <x.x>.

**Legend:** ✅ Deployable · 🟡 Watchlist · ⛔ Avoid · 🚫 Excluded   ·   ◉ real-money ◐ demo ○ unverified

## Shortlists
| List | Best for | Top pick |
|------|----------|----------|
| [Funded-survival](rankings/funded-survival.md) | the core objective — surviving repeated payouts | [[slug]] · <Overall> |
| [Challenge — 2-step](rankings/challenge-2step.md) | standard 2-step challenges | [[slug]] · <Overall> |
| [Challenge — 1-step](rankings/challenge-1step.md) | tighter 1-step / trailing-DD challenges | [[slug]] · <Overall> |
| [Full comparison](rankings/comparison.md) | every shortlisted EA, side by side | — |

## Latest pass
- [<YYYY-MM-DD>](daily/<YYYY-MM-DD>.md) — <one-line headline of the pass>
- Rulebook freshness: <all fresh / refreshed N> · re-check backlog: <count>
- ⚠️ <link to NEEDS_ATTENTION.md if present, else "No blockers">

## How to read a verdict
**Verdict** — ✅ Deployable: clears every gate including operator-supplied funded evidence (rare).
🟡 Watchlist: promising, worth chasing more evidence. ⛔ Avoid: filtered out. 🚫 Excluded: banned
mechanism (Gate A). **Overall** (1–10, absolute quality): <4 poor · 4–5.9 weak/unproven · 6–7.4
promising · ≥7.5 strong. Autonomous web evidence tops out at Watchlist by design.
```

### 1. Daily report → `vetting/daily/YYYY-MM-DD.md`

```
[← Index](../README.md) · [Rankings](../rankings/) · [‹ Prev](<prev-date>.md)

# Vetting Pass — YYYY-MM-DD
*<one-line headline of the pass>*

> **Headline:** <best of pass — name · verdict · Overall · band> — or "nothing above Avoid this pass."

## Scoreboard
| Vetted | Survived gates | Excluded (Gate A) | → Watchlist | → Avoid | Best evidence found |
|:------:|:--------------:|:-----------------:|:-----------:|:-------:|---------------------|
| N | X | Y | <n> | <n> | <Tier · source> — or "none above Tier 3" |

## Summary
- **Rulebooks:** refreshed (firm · old→new · what changed) — or "all fresh (<72h)"; backlog: <count + firms>
- **Sources consulted:** <links; fetched pages only>
- **Outcome contradictions** (past verdicts vs realized results): <list or "none">
- **Major unverifiable claims this pass:** <prop passing · payouts · risk controls · performance>
- **Deployable?** why none — or the exact Tier 0 / operator evidence that allowed it

## EAs this pass

### 🟡 Watchlist
| EA | Overall | Mechanism (conf) | best_tier | Legality | 90-day ROR | Binding criterion |
|----|:-------:|------------------|:---------:|----------|:----------:|-------------------|
| [[slug]] | <x.x> (band) | <type> (H/M/L) | ◉ T2A | ✅✅✅✅ | <%/NON-EST> | <one line> |

### ⛔ Avoid
| EA | Reason | best_tier | Major unverified claim |
|----|--------|:---------:|------------------------|
| [[slug]] | <one line> | <tier> | <claim> |

### 🚫 Excluded at Gate A
| EA | Banned mechanism | Confidence | Public signal · source |
|----|------------------|:----------:|------------------------|
| <name> | <mechanism> | H/M/L | <signal> |

## Rulebook changes & bounded re-check
Re-checked this run (≤10 Deployable/Watchlist) · queued for lazy re-check (Avoid) · backlog drained: <y/n>

## Shortlist changes
Additions / removals to Deployable & Watchlist — or "none" plainly.

## Red flags detected
```

### 2. Per-EA file → `vetting/eas/<slug>.md`

```
[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# <EA Name>
*<one line: what it is + the verdict in plain words, e.g. "Trend-pullback EA with a real but short
real-money record — Watchlist, pending a longer track.">*

## At a Glance
| | |
|---|---|
| **Verdict** | 🟡 **WATCHLIST** |
| **Overall** | **<x.x> / 10** · <band> |
| **Mechanism** | <type> · confidence <High/Med/Low> · Gate B: <verifiable / black box> |
| **Evidence** | ◉ best_tier **<T#>** · <real-money / demo> · <track length> · <source> |
| **Risk of ruin** | 90-day **<%>** (<ROR-High/Low>) · daily-DD violation **<%>** · or NON-ESTIMABLE |
| **Legality** | ✅ <firm> · ✅ <firm> · ⛔ <firm> · … (primary firms) |
| **Verified perf** | <+%/mo> [T#] · max DD <%> [T#] · <track length> |
| **Vendor** | <name — identifiable / anonymous ⚠️> |

> **Bottom line — binding criterion:** <the one sentence that decides this EA, e.g. "Real-money but
> caveated (4-month track, $2k deposit); needs a ≥6-month real-money track and tighter DD headroom
> to advance. Candidate for operator evidence-gathering.">

---
## Profile

## Overview
## Strategy Mechanism            (publicly documented / independently demonstrated / inferable; Gate B status)
## Mechanism Inference Confidence (High / Medium / Low / Unknown + why)
## Recommended Instruments

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix               (MANDATORY before scoring)

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD | | | | | | | |
| Mechanism / risk controls | | | | | | | |
| Prop-firm success claim | | | | | | | |
| Negative-case evidence | | | | | | | |

## Source Reliability Assessment (source_count · independent_source_count · affiliate_source_count · best evidence found)
## Unverified Claims             (prop passing, payouts, performance, stop-loss/risk controls, settings)

## Evidence & Performance        (each figure tagged TIER 0–4 + source + track length; NOT REPORTED if unsourced)

| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | | | |
| Maximum Drawdown | | | |
| Win Rate | | | |
| Profit Factor | | | |
| Track Length | | | |
| Real vs Demo | | | |

## Risk-of-Ruin Analysis         (daily-DD viol prob · max-DD viol prob · ROR 30/90/365 · method · assumptions · ESTIMABLE from real-money Tier 0/1/2A trade history with High/Low confidence, else NON-ESTIMABLE)
## Backtest Assessment           (public claim only: real tick data? costs modeled? multi-regime? OOS/walk-forward? or near-worthless)

---
## Eligibility & compliance

## Eligibility Gates             (Gate A pass/exclude · Gate B verifiable? + ceilings applied · Gate C per-firm)
## Per-Firm Legality Verdict     (table: Firm | ✅/⛔/Conditional | Rulebook vN | Reason)
## Rule-Violation Flags          (one-line public-evidence mechanism each)
## Mechanical Rule-Respect       (publicly documented hard equity-stop & daily-loss-stop? or NOT REPORTED/manual-only)
## Community Sentiment           (independent only; the criticism, with links; affiliate sources flagged)

---
## Verdict

## Why This Will Probably Fail   (MANDATORY skeptic steelman — comes before the scores)

## Scores

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | | | | |
| Prop-Firm Compliance | 20% | | | | |
| Risk Management | 15% | | | | |
| Challenge-Passing | 15% | | | | |
| Consistency | 10% | | | | |
| Transparency | 5% | | | | |
| Profitability | 5% | | | | |
| **Overall** | | | | | **<x.x>** |

*Band: <poor / weak-unproven / promising / strong>. Surface only the adjusted Overall; latents shown for audit.*

## Deployment Verdict            (Deployable / Watchlist / Avoid + binding criterion — must match the card above)
## Similar EAs                   (cross-links; rebrands of the same mechanism — `[[slug]]`)
## Red Flags

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer            (identifiable & accountable, or anonymous → red flag)
## MT5 Compatibility & Dependencies (publicly documented only)
## Recommended Risk Settings     (50k / 100k / 200k — only if public data supports sizing; otherwise non-actionable)
## Cost & Licensing
## Source Links                  (with retrieval date + affiliate flag)
## Analyst Notes                 (FACTS vs ANALYSIS vs ASSUMPTIONS kept separate)
## Future Research Needed        (e.g. "operator to supply funded-account statements to clear Deployable gate 8")

</details>
```

### 3. Rankings → `vetting/rankings/` (purpose-specific; not the same sort key)

Each list includes only EAs with `verdict ∈ {Deployable, Watchlist}`, ranked by a purpose-specific
composite. **Same look across all four:** the standard header, the formula in a callout, then one
ranked table. Reference each EA as `[[slug]]` in the EA column so the checklist can verify
membership and verdict.

Shared header for every ranking file:
```
[← Index](../README.md) · [Funded-survival](funded-survival.md) · [2-step](challenge-2step.md) · [1-step](challenge-1step.md) · [Comparison](comparison.md)

# <List title>
*<one line: who this list is for>*

> **Ranked by:** `<formula>`. <one line on what it optimizes and what it trades off>.
```
Then the ranked table (deciding column first; `Score` = this list's composite):

| # | EA | Verdict | Score | Overall | <composite cols> | Legality | Note |
|--:|----|:-------:|:-----:|:-------:|:----------------:|----------|------|
| 1 | [[slug]] | 🟡 | <x.x> | <x.x> | … | FN✅ FP✅ 5%✅ TFT⛔ | <one line> |

**Legality cell format:** one **labeled** marker per primary firm — a short firm initial immediately
followed by ✅ (permitted) or ⛔ (prohibited), in the fixed primary-firm order (e.g. `FN` =
FundedNext, `FP` = Funding Pips, `5%` = The 5%ers, `TFT` = The Funded Trader). The label keeps the
cell self-explanatory at a glance — an unlabeled `✅✅✅⛔` doesn't say *which* firm is prohibited.

Per list (set the composite columns to the formula's terms):
- **`funded-survival.md`** — the priority list given the objective. `0.6·Funded-Survival +
  0.25·Risk-Management + 0.15·Consistency`. Composite cols: Survival · Risk · Consistency.
- **`challenge-2step.md`** — `0.5·Challenge-Passing + 0.3·Risk-Management + 0.2·Compliance`.
  Composite cols: Challenge · Risk · Compliance.
- **`challenge-1step.md`** — as 2-step **plus an explicit trailing-DD-sensitivity penalty** (1-step
  models are usually tighter/trailing). Add a `1-step penalty` column, state it in the callout, and
  note why the order differs from 2-step.
- **`comparison.md`** — every shortlisted EA side by side (no single sort key; default to Overall).
  Columns: EA `[[slug]]` · Verdict · Overall (band) · Mechanism (conf) · best_tier · verified
  monthly [T#] · verified max DD [T#] · track · Legality (labeled per firm, e.g.
  `FN✅ FP✅ 5%✅ TFT⛔`) · daily-DD viol · 90-day ROR · cost.

### 4. Update `master_index.jsonl`

Add/refresh the row for every EA touched: fingerprint, `best_tier`, adjusted `overall`, `verdict`,
`binding_criterion`, `firm_verdicts` (+ rulebook versions), `ror_status`, `ror_evidence_tier`,
`funded_evidence`, `mechanism_confidence`, source counts, `evidence_summary`, `updated`. Rank and
surface the adjusted `overall` only.

---


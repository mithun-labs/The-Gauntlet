[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# Best Gold Robot for MT4/MT5 — ⛔ Avoid
*A XAUUSD breakout EA with a clean-sounding mechanism but zero verified performance and a false "source code" claim — ⛔ Avoid.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.1 / 10** · poor |
| **Mechanism** | XAUUSD daily S/R breakout + "7 strategies", trailing SL, no martingale/grid · confidence **Medium** · Gate B: **black box** (compiled .ex4/.ex5) |
| **Evidence** | ○ best_tier **T4** · no live record — backtest images + promo screenshots only |
| **Risk of ruin** | NON-ESTIMABLE |
| **Legality** | FN ⚠️ · FP ⚠️ · 5% ⚠️ · TFT ⚠️ (all Conditional) |
| **Verified perf** | NOT REPORTED (no MQL5 signal / Myfxbook) |
| **Vendor** | Anonymous / unknown ⚠️ |

> **Bottom line — binding criterion:** **no verified performance evidence of any kind** — only backtest
> images and promotional screenshots; no MQL5 signal or Myfxbook. The "EA **Source Code**" title is **false**
> (compiled `.ex4/.ex5` only) → closed black box. best_tier **Tier 4** + ROR **NON-ESTIMABLE** → deterministic Avoid.

---
## Profile

## Overview
A free/cracked XAUUSD ("gold") breakout EA for MT4/MT5, marketed (misleadingly) as shipping "EA Source
Code." Strategy centres on **daily support/resistance breakouts** with "seven built-in strategies."

## Strategy Mechanism
Vendor-described: **breakout on daily S/R levels**, break-of-structure logic, wide stops, predefined TP/SL
with a **trailing stop**, explicitly "**avoids grids and martingale**." **Gate B status: black box** — the
"source code" claim is false; only compiled `.ex4/.ex5` binaries are distributed, so the logic cannot be read.

## Mechanism Inference Confidence
**Medium.** The breakout + no-martingale/grid description is plausible and internally consistent, but there
is **no code to read and no live record to corroborate it** — and the false "source code" claim is itself a
trust red flag.

## Recommended Instruments
XAUUSD only; H1.

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Performance (backtest images + promo screenshots; "consistent in 2024–2025 strategy-tester backtests") | https://www.forexcracked.com/forex-ea/best-gold-robot-for-mt4-mt5-ea-source-code-free-download/ | cracked-site listing (fetched) | pirate | **TIER4** | 2026-06-24 | Low | **No** MQL5 signal / Myfxbook / live record. Backtest screenshots only. |
| Mechanism: daily S/R breakout, 7 strategies, trailing SL, no martingale/grid | same | cracked listing (fetched) | pirate | TIER4 | 2026-06-24 | Medium | Plausible; unverifiable (closed binary). |
| "EA Source Code" provided | same | cracked listing (fetched) | pirate | n/a | 2026-06-24 | High | **False** — compiled `.ex4/.ex5` only; no readable code. |
| Negative-case evidence | same (user comments) | cracked-site | mixed | n/a | 2026-06-24 | Low | License errors, stale/non-executing orders, version lag, MT5 install failures — operational, not strategy. |

## Source Reliability Assessment
source_count **2** · independent_source_count **0** · affiliate_source_count **1** (forexcracked). **Best
evidence found:** none above backtest screenshots — **no inspectable live record of any kind**; anonymous
vendor; closed binary; misleading "source code" marketing.

## Unverified Claims
- All performance (backtest "consistency", screenshots) — Tier 4, no live verification.
- The non-martingale/grid + trailing-SL mechanism — plausible but unverifiable (closed binary).
- "EA Source Code" — demonstrably false (compiled binaries only).

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | NOT REPORTED (backtest only) | [T4] | forexcracked |
| Maximum Drawdown | NOT REPORTED (no live record) | [T4] | forexcracked |
| Win Rate | NOT REPORTED | [T4] | forexcracked |
| Track Length | NONE (no live signal) | [T4] | forexcracked |
| Real vs Demo | No live account published | [T4] | forexcracked |

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No real-money, publicly inspectable trade-level history (Tier 0/1/2A) exists — only
backtests and screenshots, which have no trustworthy real-money distribution. Per the framework this is a
**negative finding** and bars any non-Avoid verdict on its own.

## Backtest Assessment
"Consistent in 2024–2025 strategy-tester backtests" with screenshot images — no stated real-tick data,
costs, multi-regime/shock coverage, or OOS/walk-forward; XAUUSD breakouts are specifically noted to fail
around NFP/CPI/FOMC. Near-worthless as proof.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS.** No banned mechanism claimed (S/R breakout, trailing SL, no martingale/grid); no
  contradicting user reports of order-stacking. Mechanism inference Medium.
- **Gate B — TRIGGERED (black box).** "Source code" claim false → compiled binary only, no teardown →
  Compliance ≤ 5, Risk ≤ 4, verdict ≤ Watchlist. Documented trailing SL → not auto-Avoided by criterion 3
  (Avoided by criteria 2 & 4 below).
- **Gate C — per-firm legality:** Conditional (unverifiable closed binary).

## Per-Firm Legality Verdict

| Firm | Verdict | Rulebook | Reason |
|------|:-------:|:--------:|--------|
| FundedNext | ⚠️ Conditional | v1 (PROVISIONAL — primary 503 ×6) | Mechanism claimed non-banned but unverifiable; stale rulebook |
| Funding Pips | ⚠️ Conditional | v1 | Can't confirm mechanism from a compiled binary |
| The 5%ers | ⚠️ Conditional | v1 | Same |
| The Funded Trader | ⚠️ Conditional | v1 | Same |
| Alpha Capital *(ref)* | ⛔ Prohibited | v1 | Closed-source commercial EA (non-gating) |
| Goat Funded Trader *(ref)* | ⛔ Prohibited | v1 | Commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **No live evidence** → cannot demonstrate prop-compatible DD; XAUUSD breakout is news-fragile (NFP/CPI/FOMC).

## Mechanical Rule-Respect
Trailing SL claimed in the listing (vendor-documented), **not** independently demonstrated; no live record,
no daily-loss stop documented. → Risk control-evidence vendor-documented (Risk ≤ 5); Gate B caps Risk ≤ 4.

## Community Sentiment
Only cracked-site user comments — license errors, non-executing/stale orders, version lag, MT5 install
failures (operational). No independent verified community track.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a backtest-tuned breakout EA whose strategy-tester "consistency"
   doesn't survive real spreads/slippage and news — XAUUSD breakouts are explicitly fragile around
   NFP/CPI/FOMC, and there is no live record showing otherwise.
2. **Prop-server case:** untested under any firm's DD calc, spreads, or leverage; with no live data, prop
   viability is pure assertion.
3. **Variance case:** could pass a calm evaluation and blow the funded phase — unknowable, since nothing is
   verified.
4. **Evidence fragility:** **everything rests on backtest screenshots** from a cracked site, with a false
   "source code" claim. The single thing that would change the verdict — a verified ≥6-month real-money
   record — does not exist.

## Scores
*latent × multiplier (or ceiling) = adjusted. best_tier **TIER4** → Multiplier A 0.12, Multiplier B 0.15;
ROR **NON-ESTIMABLE** → Survival ×min(A,0.20); Gate B → Compliance ≤ 5, Risk ≤ 4.*

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 1 | ×0.12 (ROR cap floor) | **1** | 0.30 |
| Prop-Firm Compliance | 20% | 5 | Gate-B min(5, 5) | **5** | 1.00 |
| Risk Management | 15% | 3 | min(Gate-B 4, vendor-doc 5) | **3** | 0.45 |
| Challenge-Passing | 15% | 1 | ×0.12 | **1** | 0.15 |
| Consistency | 10% | 1 | ×0.15 | **1** | 0.10 |
| Transparency | 5% | 1 | ×0.15 | **1** | 0.05 |
| Profitability | 5% | 1 | ×0.15 | **1** | 0.05 |
| **Overall** | | | | | **2.1** |

*Band: **poor** (<4.0). Overall = 0.30·1 + 0.20·5 + 0.15·3 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1 = 2.10.*

## Deployment Verdict
⛔ **AVOID.** Binding criterion: **no verified performance evidence of any kind** (backtest images +
screenshots only; no MQL5 signal/Myfxbook); compiled-binary black box with a **false "source code" claim**
→ best_tier Tier 4 + ROR NON-ESTIMABLE. Fails Avoid criteria 2 (Tier-4 headline) and 4 (NON-ESTIMABLE +
Tier 4).

## Similar EAs
Same "clean-sounding mechanism, zero verified evidence → Avoid" profile as [[hon-aps-mt5]] (open-source, no
track) and [[gold-trading-smc-ea]]. Distinct from [[gold-prop-firm-robot]] (which has a fetched real signal
→ Watchlist).

## Red Flags
- Zero live evidence (backtest screenshots only); XAUUSD breakout is news-fragile.
- **False "EA Source Code" marketing** — compiled binary only.
- Anonymous vendor; cracked-site distribution (malware caveat); operational install/license failures.

<details>
<summary><strong>Appendix — full audit trail</strong></summary>

## Vendor / Developer
Anonymous / unknown — accountability red flag. Original author/source not identifiable from the cracked listing.

## MT5 Compatibility & Dependencies
MT4/MT5; XAUUSD; H1. Users report MT5 installation failures and license errors.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable** — no verified live data to size from.

## Cost & Licensing
"FREE Download" (cracked); compiled `.ex4/.ex5`, malware caveat. No readable source despite the title.

## Source Links
- https://www.forexcracked.com/forex-ea/best-gold-robot-for-mt4-mt5-ea-source-code-free-download/ — 2026-06-24 — cracked listing (fetched: breakout mechanism, NO source code, backtest-only, user comments) — pirate (negative/discovery only)
- WebSearch "Best Gold Robot MT4 MT5 EA source code mechanism martingale" — 2026-06-24 — discovery + mechanism + negative case — mixed

## Analyst Notes
- **FACTS:** fetched listing — XAUUSD daily-S/R breakout, 7 strategies, trailing SL, no martingale/grid;
  **no source code** (compiled binary only); **no live track** (backtest images + screenshots); user
  comments report operational failures.
- **ANALYSIS:** mechanism non-banned → Gate A pass; closed binary → Gate B; no verified evidence → Tier 4,
  ROR NON-ESTIMABLE → Avoid (criteria 2 & 4). Overall 2.1.
- **ASSUMPTIONS (flagged):** mechanism is as described (unverifiable); the false "source code" claim lowers
  trust further.

## Future Research Needed
- Operator to obtain a verified real-money (or funded) ≥6-month record; absent that, this remains Avoid
  regardless of backtest quality.

</details>

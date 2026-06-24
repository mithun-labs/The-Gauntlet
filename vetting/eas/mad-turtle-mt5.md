[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# Mad Turtle EA (MT5)
*High-reputation ONNX-ML gold EA with the cleanest described mechanism in the archive — but its own two verified real-money signals show catastrophic 68–83% drawdowns, one net losing: a decisive AVOID.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.1 / 10** · poor |
| **Mechanism** | ONNX ML, single position, hard SL, no grid/martingale · confidence Medium · Gate B: verifiable |
| **Evidence** | ◉ best_tier **T2** · real-money · ~11mo (WT) / ~8.5mo (ICM) · two vendor MQL5 live signals |
| **Risk of ruin** | NON-ESTIMABLE |
| **Legality** | FN ✅ · FP ⚠️ · 5% ⚠️ · TFT ⚠️ |
| **Verified perf** | Weltrade −67.91% / ICM −42.10% (recent) [T2] · max DD 68.13% / 83.31% [T2] · ~11mo (WT) / ~8.5mo (ICM) |
| **Vendor** | Gennady Sergienko (ats_cis) — identifiable |

> **Bottom line — binding criterion:** two verified real-money MQL5 signals (≥6mo) show catastrophic 68.13% and 83.31% max drawdowns — one net LOSING (−6.23%, PF 0.99) — flatly contradicting the safe/low-DD/single-position marketing.

---
## Profile

## Overview
Mad Turtle is a premium ($1,800 buy / $399 6-mo rental) machine-learning MT5 EA by **Gennady Sergienko
(ats_cis)** — a high-reputation MQL5 author — trading **XAUUSD** with **ONNX neural networks**, **one
position at a time**, a **hard stop loss on every trade**, and **no grid/martingale**. Trained on H4,
holding positions hours-to-days (swing). It has the best vendor reputation and cleanest *described*
mechanism in the archive. **Yet its two own verified real-money MQL5 signals show catastrophic drawdowns
(68% and 83%), one net losing** — a decisive, evidence-based Avoid.

> **DECISIVE FINDING — two real signals contradict the "safe, low-DD" marketing.**
> - **Weltrade (real, ~11 months, since 2025-07-28):** **−6.23% total (net LOSING)**, **83.31% max DD**
>   ($24,850), PF 0.99, expected payoff −$0.20, 1,881 trades.
> - **IC Markets (real, ~8.5 months, since 2025-10-07):** +143.04% but **68.13% max DD**, PF 1.12, recent
>   monthly −42.10%, 740 trades, 59.86% win.
>   MQL5 banners on both: "*A large drawdown may occur on the account again.*" The affiliate-cited "46%
>   gain / 9.5% DD over 7 weeks" was a cherry-picked early snapshot of an account that later drew down 68–83%.

## Strategy Mechanism (publicly documented / inferable; Gate B status)
**FACTS (vendor MQL5 listing, fetched):** "Real machine learning using ONNX"; "models trained for a full
24-hour format on large H4 timeframes, holding positions from several hours to several days"; multi-class
models with separate BUY/SELL logic; "**Stop Loss is an integral part of the strategy**"; "**single-position
trading**"; "Does not use dangerous strategies such as grids or martingale; no micro-scalping." **FACTS
(signal reviewer):** the EA "just sends buy orders with a **4000-point stop loss**" (≈$40 on gold — a very
wide stop).

**ANALYSIS:** **survives Gate A** — genuinely single-position, no averaging-down, no grid/martingale,
swing holds (not HFT despite ~4–6 trades/day). But the internal logic is a neural net (opaque), and the
realized behavior is **directional with a very wide hard stop**: a string of adverse swings (or a
persistent directional bias in a trending-against regime) produces enormous account-level DD even with
"one position at a time." The two real signals (68% and 83% DD, PF ~1.0) show the ML edge is **marginal-to-
negative out-of-sample** — classic ML-overfitting decay after release.

## Mechanism Inference Confidence
**Medium.** Single-position + wide hard SL + no grid/martingale is corroborated by the vendor listing and
the signals' behavior. The neural net itself is opaque, but the *risk-relevant* structure is observable
(no averaging-down; account risk driven by wide directional stops) → **no Gate-B ceiling**; the opacity is
captured in mechanism confidence and the survival/risk scores.

## Recommended Instruments
XAUUSD only.

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Real account (Weltrade, ~11mo): −6.23% / **83.31% max DD** / PF 0.99 / 1,881 trades | mql5.com/signals/2323073 | MQL5 live signal (REAL) | platform-hosted | TIER2 | 2026-06-23 | High | ≥6mo real money, public, fetched firsthand; net losing |
| Real account (IC Markets, ~8.5mo): +143% / **68.13% max DD** / PF 1.12 | mql5.com/signals/2335965 | MQL5 live signal (REAL) | platform-hosted | TIER2 | 2026-06-23 | High | ≥6mo real money; huge DD; recent monthly −42% |
| Mechanism: ONNX ML, single position, hard SL, no grid/martingale | mql5.com/market/product/144803 | vendor listing | vendor | TIER3 | 2026-06-23 | Medium | Risk structure corroborated by signals |
| "46% gain / 9.5% DD over 7 weeks", "safe, low DD" | newyorkcityservers.com/blog/mad-turtle-ea-review | affiliate (VPS promo) review | affiliate | TIER4 | 2026-06-23 | Low | Cherry-picked early snapshot; contradicted by the full signals |
| Negative-case evidence | WebSearch + signal banners | community/platform | mixed | n/a | 2026-06-23 | Medium | No scam reports, but the signals themselves are the negative case |

## Source Reliability Assessment
- **source_count: 6** (MQL5 listing, 2 MQL5 signals, NYCServers review, MQL5 comments, web searches) ·
  **independent_source_count: 3** (2 platform-hosted real signals + lleon third-party Myfxbook reference) ·
  **affiliate_source_count: 2** (NYCServers VPS-promo review, group-buy listings).
- **Best evidence found:** **Tier 2** — two fetchable **real-money ≥6-month MQL5 signals** (the strongest
  inspectable evidence in the archive). Decisively negative: 68% and 83% DD, one net losing.

## Mechanism Inference Confidence
**Medium.** Single-position + wide hard SL + no grid/martingale is corroborated by the vendor listing and
the signals' behavior. The neural net itself is opaque, but the *risk-relevant* structure is observable
(no averaging-down; account risk driven by wide directional stops) → **no Gate-B ceiling**; the opacity is
captured in mechanism confidence and the survival/risk scores.

## Unverified Claims
- "Safe / low drawdown / capital preservation" — **contradicted** by both real signals.
- "9.5% max DD" — a 7-week cherry-pick; the same strategy's real accounts reached 68–83% DD.
- ML "predicts direction" edge — PF 0.99–1.12 over ≥6 months indicates a marginal-to-negative real edge.

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | Weltrade −67.91% / ICM −42.10% (recent); curves now declining | TIER2 | MQL5 signals |
| Maximum Drawdown | **83.31%** (Weltrade) / **68.13%** (ICM) | TIER2 | MQL5 signals (fetched) |
| Win Rate | 64.48% (WT) / 59.86% (ICM) | TIER2 | MQL5 signals |
| Profit Factor | 0.99 (WT, losing) / 1.12 (ICM) | TIER2 | MQL5 signals |
| Track Length | ~11mo (WT) / ~8.5mo (ICM), real money | TIER2 | MQL5 signals |
| Real vs Demo | **Real** (Weltrade 1:500; IC Markets) | TIER2 | MQL5 signals |

## Risk-of-Ruin Analysis
**NON-ESTIMABLE** as a formal ROR (only aggregate signal stats fetchable, not trade-level). Qualitatively
unambiguous: **68–83% realized DD ⇒ daily/overall-DD violation probability ≈ 1** on any primary firm; PF ≈ 1.0
means no durable edge to offset variance. DD-definition mismatch caveat applies but is dwarfed by a 7× gap.
NON-ESTIMABLE ROR **bars Deployable.**

## Backtest Assessment
Not the basis of the case; the two real signals are. The gap between marketing/early-snapshot DD (~9.5%) and
realized DD (68–83%) is the textbook **ML overfit / out-of-sample decay** signature. Backtests treated as
near-worthless against the live result.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS (survives).** Single position, hard SL, no grid/martingale/averaging, swing holds
  (not HFT). Banned core mechanism absent.
- **Gate B — mechanism risk-structure inferable from signals → no Gate-B ceiling** (ML opacity noted).
- **Gate C — per-firm:** legal mechanism; closed-source commercial EA → not Prohibited at all primaries.

## Per-Firm Legality Verdict
| Firm | Verdict | Rulebook | Basis |
|------|---------|----------|-------|
| FundedNext (primary) | Permitted | v1 (PROVISIONAL) | EA-permissive; no grid/martingale. Rulebook secondary — cannot clear Deployable. |
| Funding Pips (primary) | Conditional | v1 | Third-party EA only as trade/risk manager |
| The 5%ers (primary) | Conditional | v1 | Control-of-internal-logic; closed source |
| The Funded Trader (primary) | Conditional | v1 | Standard EAs OK, but 68–83% real DD evidences "grossly overleveraged" behavior; numerics UNCONFIRMED |
| Alpha Capital (reference) | Prohibited | v1 | Mandatory .MQ5 source-code submission (non-gating) |
| Goat Funded Trader (reference) | Prohibited | v1 | Off-the-shelf/commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **68.13% and 83.31% verified real-money max DD** — 7–8× a 10% overall limit; near-certain immediate breach.
- **Net-losing real account** (Weltrade −6.23%, PF 0.99) — the edge does not survive out-of-sample.
- **Wide ~4000-point directional stops** — large single-trade losses; not the "controlled" risk advertised.

## Mechanical Rule-Respect
**Claimed but contradicted.** A hard SL per trade is real (signals show SL activations) and the EA is genuinely
single-position, but the **stops are wide and the account-level DD reached 68–83%**, so the controls do not
bound risk to anything near prop levels. No daily-loss-stop/equity-stop documented.

## Community Sentiment
MQL5 4.34/5 (91 reviews) — good on paper, but the **signals are the real verdict**. A signal reviewer
questioned the "buy orders with 4000-point SL" viability. No scam allegations; the issue is performance/risk,
not fraud. The affiliate "review" is a VPS-promo with a cherry-picked snapshot.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a real ML edge that was strong in training/early live (the 7-week
   9.5%-DD snapshot) and **decayed out-of-sample** (PF→~1.0, DD→68–83%) — the classic ML-EA lifecycle.
2. **Prop-server case:** at 68–83% realized DD on retail brokers, any primary firm's 5% daily / 10% overall
   limit is breached almost immediately; the wide directional stops guarantee large single-day losses.
3. **Variance case:** PF ~1.0 with wide stops is a coin-flip that may pass a calm evaluation and then blow a
   funded account — and one real account is *already* net negative.
4. **Evidence fragility:** here the evidence is *strong* and *negative* — two real ≥6-month signals. The only
   thing that could change the verdict is a *new* real account holding ≤~6% DD over ≥6 months, which would
   contradict everything currently on record.

## Scores

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 2 | ×0.20 (ROR cap) = 0.40 → clamp | 1 | 0.30 |
| Prop-Firm Compliance | 20% | 5 | not multiplied (Permitted ≥1, Conditional rest) | 5 | 1.00 |
| Risk Management | 15% | 2 | controls contradicted (68–83% real DD) | 2 | 0.30 |
| Challenge-Passing | 15% | 1 | ×0.45 = 0.45 → round | 1 | 0.15 |
| Consistency | 10% | 1 | ×0.60 = 0.60 → round | 1 | 0.10 |
| Transparency | 5% | 6 | ×0.60 = 3.6 → round | 4 | 0.20 |
| Profitability | 5% | 2 | ×0.60 = 1.2 → round | 1 | 0.05 |
| **Overall** | | | | | **2.1** |

*Band: poor. Surface only the adjusted Overall; latents shown for audit.*

best_tier = **TIER2**; ROR = **NON-ESTIMABLE** → Survival multiplier = min(MultA_T2 0.45, 0.20) = 0.20.
Multiplier A (Tier 2) = 0.45; Multiplier B (Tier 2) = 0.60. No Gate-B ceiling. Risk controls contradicted
by 68–83% real DD → anchored low.

**Overall** = 0.30·1 + 0.20·5 + 0.15·2 + 0.15·1 + 0.10·1 + 0.05·4 + 0.05·1
= 0.30 + 1.00 + 0.30 + 0.15 + 0.10 + 0.20 + 0.05 = **2.10 → 2.1 (poor).**

## Deployment Verdict
**AVOID · Overall 2.1 (poor).**
**Binding criterion:** two verified real-money MQL5 signals (≥6 months) show catastrophic **68.13% and
83.31% maximum drawdowns — one net LOSING (−6.23%, PF 0.99)** — flatly contradicting the "safe, low-DD,
single-position" marketing and the affiliate-cited 9.5%-DD/7-week snapshot; ROR NON-ESTIMABLE (aggregates
only). A high-reputation, mechanically-clean EA that fails decisively on **realized risk and edge**, not
legality — the most important lesson of this pass.

## Similar EAs
- [[xau-master-mt5]] — the same pattern from the same pass: clean "no grid/martingale" gold EA whose own real
  signal shows a catastrophic DD (72.56%). Mad Turtle and XAU Master together show that *inspectable* real
  signals, when available, consistently reveal DDs an order of magnitude above the marketing.
- [[ai-gold-sniper-mt5]], [[the-gold-reaper-mt5]] — other XAUUSD EAs whose live risk exceeds the pitch.

## Red Flags
- **83% and 68% real-money max DD; one account net losing; PF ≈ 1.0** — the strategy's real edge is marginal/negative.
- Marketing/snapshot DD (~9.5%) is ~8× below realized DD — out-of-sample ML decay.
- Wide ~4000-point directional stops; premium $1,800 price; recent monthly returns deeply negative.

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer
**Gennady Sergienko (ats_cis)** — named, accountable, 8+ years on MQL5; other products (Nesco EA, Trader
Station). **The strongest vendor reputation in the archive** — which is exactly why the negative real-money
result matters: reputation and clean marketing did not produce prop-survivable behavior.

## MT5 Compatibility & Dependencies (publicly documented only)
- Platform: MT5 only. Instrument: **XAUUSD** only. Timeframe: any (H1/M15), models trained on **H4**.
- Min deposit $500; ECN/low-spread gold broker; VPS recommended. Verified signals ran on Weltrade (1:500)
  and IC Markets.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** Two real configs produced 68–83% DD and one net loss; no sizing makes that prop-viable.

## Cost & Licensing
$1,800 buy / $399 6-month rental (MQL5); 91 reviews, **4.34/5**. Also on group-buy sites (malware caveat,
negative signal only). Premium price for a strategy whose real accounts are down/deeply drawn-down.

## Source Links
- https://www.mql5.com/en/market/product/144803 — 2026-06-23 — vendor MQL5 listing (fetched) — affiliate(vendor)
- https://www.mql5.com/en/signals/2323073 — 2026-06-23 — REAL signal, Weltrade ~11mo (fetched) — platform-hosted
- https://www.mql5.com/en/signals/2335965 — 2026-06-23 — REAL signal, IC Markets ~8.5mo (fetched) — platform-hosted
- https://newyorkcityservers.com/blog/mad-turtle-ea-review — 2026-06-23 — VPS-promo review (fetched) — affiliate
- https://www.myfxbook.com/members/lleon/ea-mad-turtle/11699075 — 2026-06-23 — third-party Myfxbook (not fetched) — independent(uninspectable)

## Analyst Notes
- **FACTS:** Sergienko (high-rep, accountable); XAUUSD, ONNX ML, single position, hard (wide ~4000pt) SL, no
  grid/martingale, H4-trained swing; $1,800/$399; MQL5 4.34/5 (91). Two REAL signals: Weltrade ~11mo −6.23%
  / 83.31% DD / PF 0.99 / 1,881 trades; IC Markets ~8.5mo +143% / 68.13% DD / PF 1.12 / 740 trades.
- **ANALYSIS:** survives Gate A, best reputation + transparency in the archive, but real-money evidence is
  decisively negative (catastrophic DD, marginal/negative PF) — ML overfit decay; Avoid on realized risk/edge.
- **ASSUMPTIONS (flagged):** signals are recent near-default configs (vendor/early-adopter accounts); full
  trade-level distribution not extracted (logged-in needed) so ROR is NON-ESTIMABLE.

## Future Research Needed
- Monitor for any Mad Turtle real account holding ≤~6% DD over ≥6 months — would be required to reconsider;
  current ≥6-month evidence is strongly negative.
- If signal trade-level history becomes inspectable, compute a formal ROR and confirm the directional-bias
  hypothesis.

</details>

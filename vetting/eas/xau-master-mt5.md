[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# XAU Master EA (MT5)
*Commercial XAUUSD M15 multi-system EA marketed as prop-safe — but its own real-money signal shows a 72.56% drawdown — AVOID.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.1 / 10** · poor |
| **Mechanism** | Multi-system multi-position with wide hard stops · confidence Medium · Gate B: verifiable (mechanism inferable, inspectable signal) |
| **Evidence** | ◉ best_tier **T2** · real-money · ~5-month track · vendor MQL5 live signal |
| **Risk of ruin** | NON-ESTIMABLE |
| **Legality** | FN ✅ · FP ⚠️ · 5% ⚠️ · TFT ⚠️ |
| **Verified perf** | 95.76% "monthly growth" [T2] · max DD 72.56% [T2] · ~5-month track |
| **Vendor** | Branislav Bridzik — identifiable |

> **Bottom line — binding criterion:** the EA's **own verified real-money MQL5 signal shows a 72.56% maximum drawdown** (vs marketed 5%/10% auto-cutoff) with **80% of growth in a single day** — catastrophically prop-incompatible.

---
## Profile

## Overview
XAU Master is a commercial MT5 Expert Advisor by **Branislav Bridzik** (Slovakia) that trades **XAUUSD on
M15** with "**13 trading systems running simultaneously**" (mean-reversion, momentum, trend, breakout),
a **hard stop loss on every trade**, and — its central selling point — **built-in prop-style drawdown
auto-cutoffs** ("if equity drops ~5% from daily start, all positions close immediately"; "if ~10% total
loss is breached, the EA closes positions and stops permanently"). $149 buy / $49/mo. **It markets itself
as prop-firm compatible.**

> **DECISIVE FINDING — marketing vs. the real signal.** XAU Master is the cleanest-*sounding* prop EA
> vetted to date, but its **own vendor MQL5 live signal (REAL money, IC Markets EU, fetched directly)**
> contradicts the marketing: **78.01% growth with a 72.56% maximum drawdown**, "**80% of growth achieved
> within 1 day**," and MQL5's own banner "*too much growth in the last month indicates a high risk*." A
> 72.56% realized DD is the opposite of a working "10% auto-cutoff." This is a verified-evidence Avoid,
> not an inference.

## Strategy Mechanism (publicly documented / inferable; Gate B status)
**FACTS (vendor MQL5 listing, fetched):** "13 trading systems running simultaneously, each with different
parameters"; uses "mean reversion, momentum, trend following and breakout logic"; "**Does not employ
martingale or grid**"; "**Every trade includes a protective Stop Loss**"; built-in **daily (~5%) and
overall (~10%) equity drawdown auto-close**. **FACTS (MQL5 comments, via search):** a user ran v6.5 six
months "relatively stable," but **v7.2 introduced "hold multiple orders simultaneously and two-way
trading [hedging], with maximum drawdown significantly higher"**; another notes **"wide stop losses placed
on swing high/low"** that turn profitable trades into losses.

**ANALYSIS:** the design is **multi-system multi-position with wide hard stops** — not martingale/grid
(losers are not averaged down), so it **survives Gate A**. But "13 systems simultaneously" + "two-way
trading" + "wide SL" means many concurrent positions with large per-trade loss potential that can go wrong
**together** — which is exactly how the real signal reached a **72.56% DD** despite "no martingale." The
marketed 5%/10% auto-cutoff **demonstrably did not bound the real account** (either disabled, mis-set, or
overwhelmed by simultaneous gaps). Version drift (v6.5→v7.2) toward riskier behavior is a standing red flag.

## Mechanism Inference Confidence
**Medium.** The multi-system + hard-SL + multi-position description is corroborated by the vendor listing,
MQL5 user comments, and the real signal's behavior (725 trades, huge DD, 1-day concentration). Not a black
box → **no Gate-B ceiling.** The uncertainty is which version/config produced the signal and whether the
DD-cutoff is ever effective.

## Recommended Instruments
XAUUSD only, M15.

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Real-money track: 78.01% gain / **72.56% max DD** / 95.76% monthly / 725 trades since 2026-01-29 | mql5.com/signals/2356533 | vendor's MQL5 live signal (platform-hosted, REAL) | platform-hosted (vendor's own account) | TIER2 | 2026-06-23 | High | REAL money, public aggregates, **fetched firsthand**; but <6mo + $1k deposit → Tier 2. DD is a real datapoint |
| Mechanism: 13 systems, no grid/martingale, hard SL, 5%/10% DD auto-cutoff | mql5.com/market/product/157989 | vendor listing | vendor | TIER3 | 2026-06-23 | Medium | Claimed controls contradicted by the signal's 72.56% DD |
| v7.2 added multi-order + two-way (hedging), higher DD; wide SLs | MQL5 comments (via search) | community | independent | TIER3 | 2026-06-23 | Medium | Version drift toward riskier behavior; hedging = Funding Pips legality issue |
| Prop-firm compatibility | vendor listing | vendor | vendor | TIER4 | 2026-06-23 | Low | Contradicted by 72.56% real DD; no Tier-0 funded proof |
| Negative-case evidence | WebSearch scam/blown/drawdown | search aggregate | n/a | n/a | 2026-06-23 | Low | No independent Myfxbook; MQL5 comments flag DD/version concerns; rating only 3.96/5 |

## Source Reliability Assessment
- **source_count: 5** (MQL5 listing, MQL5 live signal, eafxstore settings blog, MQL5 comments, web
  searches) · **independent_source_count: 2** (MQL5 live signal page as a platform-hosted real account +
  MQL5 user comments) · **affiliate_source_count: 1** (eafxstore group-buy).
- **Best evidence found:** **Tier 2** — a fetchable **real-money MQL5 live signal** (rare for this archive),
  which is precisely what sinks the EA: it shows a **72.56% max DD**. No independent third-party Myfxbook
  record exists.

## Mechanism Inference Confidence
**Medium.** The multi-system + hard-SL + multi-position description is corroborated by the vendor listing,
MQL5 user comments, and the real signal's behavior (725 trades, huge DD, 1-day concentration). Not a black
box → **no Gate-B ceiling.** The uncertainty is which version/config produced the signal and whether the
DD-cutoff is ever effective.

## Unverified Claims
- "Built-in 5%/10% drawdown protection keeps it prop-safe" — **contradicted** by the real signal (72.56% DD).
- "Does not employ martingale or grid" — plausibly true (no averaging-down), but irrelevant to the realized
  risk, which comes from many simultaneous wide-SL positions.
- The signal's durability — 80% of gains in 1 day means the 78% growth is **not** a repeatable monthly rate.

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | 95.76% "monthly growth" (distorted by 1-day concentration; not durable) | TIER2 | MQL5 live signal |
| Maximum Drawdown | **72.56%** (by balance) | TIER2 | MQL5 live signal (fetched) |
| Win Rate | NOT REPORTED (not on fetched aggregates) | — | — |
| Profit Factor | NOT REPORTED | — | — |
| Track Length | ~5 months (since 2026-01-29), real money | TIER2 | MQL5 live signal |
| Real vs Demo | **Real** (IC Markets EU), $1,000 deposit → $1,848 equity | TIER2 | MQL5 live signal |

## Risk-of-Ruin Analysis
**NON-ESTIMABLE** as a formal ROR (only aggregate signal stats were fetchable, not trade-level history;
track <6mo). **However, the qualitative read is unambiguous:** a 72.56% realized DD with 80%-in-1-day
concentration means the **daily-DD and overall-DD violation probability on any primary firm is effectively
~1** — this account would have blown a funded challenge. DD-definition mismatch caveat applies (72.56% is
MQL5 by-balance), but a 7× gap dwarfs any reconciliation. NON-ESTIMABLE ROR also **bars Deployable.**

## Backtest Assessment
MQL5 comments report backtest behavior changed materially between v6.5 and v7.2 (more simultaneous orders,
higher DD) — i.e. the product a buyer gets today differs from older "stable" reports. Backtests not
reproducible; treated as near-worthless vs the (damning) live signal.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS (survives).** No martingale/grid (losers not averaged down); hard SL per trade; M15
  multi-minute holds, not tick-scalping/HFT. High-risk but not a banned *core* mechanism.
- **Gate B — mechanism inferable (Medium), inspectable signal exists → no Gate-B ceiling.**
- **Gate C — per-firm:** legal mechanism, but a closed-source commercial multi-position EA (and v7.2
  hedging) → not Prohibited at all primaries, so no automatic Gate-C Avoid.

## Per-Firm Legality Verdict
| Firm | Verdict | Rulebook | Basis |
|------|---------|----------|-------|
| FundedNext (primary) | Permitted | v1 (PROVISIONAL) | EA-permissive; no grid/martingale. Rulebook secondary — cannot clear Deployable. |
| Funding Pips (primary) | Conditional | v1 | Third-party EA only as trade/risk manager; **v7.2 "two-way trading" = hedging, which Funding Pips bans** → leans Prohibited |
| The 5%ers (primary) | Conditional | v1 | Control-of-internal-logic; closed source; multi-system |
| The Funded Trader (primary) | Conditional | v1 | Standard EAs OK, but the demonstrated 72.56% DD / multi-position behavior brushes "grossly overleveraged"; numerics UNCONFIRMED |
| Alpha Capital (reference) | Prohibited | v1 | Mandatory .MQ5 source-code submission (non-gating) |
| Goat Funded Trader (reference) | Prohibited | v1 | Off-the-shelf/commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **72.56% verified real-money max DD** — ~7× a 10% overall limit, ~14× a 5% daily limit. Near-certain
  daily-DD breach; the marketed auto-cutoff did not prevent it.
- **80% of growth in 1 day** — return concentration that fails consistency rules and signals lottery-like
  variance, not a passable steady edge.
- **v7.2 two-way (hedging)** — direct Funding Pips hedging-ban issue; **wide SLs** mean large single-trade
  losses.

## Mechanical Rule-Respect
**Claimed but contradicted.** A hard per-trade SL is documented and a 5%/10% DD auto-cutoff is advertised,
but the **real-money signal's 72.56% DD proves the account-level controls did not hold** (disabled,
mis-configured, or overwhelmed by simultaneous positions). Treat hard controls as **not established.**

## Community Sentiment
MQL5 rating **3.96/5** (30 reviews) — mediocre. Comments are genuinely mixed/independent: older v6.5 "six
months relatively stable," but v7.2 "max drawdown significantly higher," "wide SL closes winners into
losses." No independent third-party Myfxbook record. The negative case is corroborated by the EA's **own**
real signal.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** the 78%/5-month curve is a small real account that hit a lucky
   1-day cluster (80% of gains) while running many simultaneous wide-SL positions — high variance dressed
   as performance.
2. **Prop-server case:** with a 72.56% realized DD on a retail broker, the same config on any primary firm
   breaches the 5% daily / 10% overall limit almost immediately; the advertised auto-cutoff demonstrably
   did not save the real account.
3. **Variance case:** 80%-in-1-day is the definition of a profile that may *pass* a calm evaluation by luck
   and then surrender a funded account in one session.
4. **Evidence fragility:** ironically the *strongest* evidence (a real, fetchable signal) is what condemns
   it. The piece that could change the verdict — a real-money, **≥6-month**, low-DD (≤~6%) record proving
   the auto-cutoff actually bounds risk — does not exist; the one real account shows the opposite.

## Scores
best_tier = **TIER2**; ROR = **NON-ESTIMABLE** → Survival multiplier = min(MultA_T2 0.45, 0.20) = 0.20.
Multiplier A (Tier 2) = 0.45; Multiplier B (Tier 2) = 0.60. No Gate-B ceiling (mechanism inferable). Risk
control-evidence: controls **contradicted** by the real signal → Risk anchored low (1–3 band).

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 2 | ×0.20 (ROR cap) = 0.40 → clamp | 1 | 0.30 |
| Prop-Firm Compliance | 20% | 5 | not multiplied (Permitted ≥1, Conditional rest) | 5 | 1.00 |
| Risk Management | 15% | 2 | controls contradicted (real 72.56% DD) | 2 | 0.30 |
| Challenge-Passing | 15% | 1 | ×0.45 = 0.45 → round | 1 | 0.15 |
| Consistency | 10% | 1 | ×0.60 = 0.60 → round | 1 | 0.10 |
| Transparency | 5% | 5 | ×0.60 = 3.0 | 3 | 0.15 |
| Profitability | 5% | 3 | ×0.60 = 1.8 → round | 2 | 0.10 |
| **Overall** | | | | | **2.1** |

*Band: poor. Surface only the adjusted Overall; latents shown for audit.*
**Overall** = 0.30·1 + 0.20·5 + 0.15·2 + 0.15·1 + 0.10·1 + 0.05·3 + 0.05·2
= 0.30 + 1.00 + 0.30 + 0.15 + 0.10 + 0.15 + 0.10 = **2.10 → 2.1 (poor).**

## Deployment Verdict
**AVOID · Overall 2.1 (poor).**
**Binding criterion:** the EA's **own verified real-money MQL5 signal shows a 72.56% maximum drawdown** (vs
its marketed 5%/10% auto-cutoff) with **80% of growth in a single day** — catastrophically prop-incompatible
and directly contradicting its central risk-control claim; ROR NON-ESTIMABLE (aggregates only, <6mo). A rare
case where inspectable Tier-2 evidence makes the Avoid **certain** rather than precautionary.

## Similar EAs
- [[apex-drawdown-zero-mt5]] — the mirror image: Apex markets an *implausibly low* 0.39% DD (uninspectable);
  XAU Master markets a low DD but its real signal shows 72.56%. Both are "prop-safe DD" marketing that the
  evidence contradicts (one by implausibility, one by a real signal).
- [[the-gold-reaper-mt5]], [[ai-gold-sniper-mt5]] — other XAUUSD multi-/single-system EAs.

## Red Flags
- **72.56% real-money max DD** — the single damning fact; the auto-cutoff did not work.
- 80% of growth in 1 day; MQL5 "too much growth = high risk" banner; 95.76% "monthly" is an artifact.
- Version drift (v6.5→v7.2) toward more simultaneous orders + two-way (hedging) + higher DD.
- Wide SLs that close winners into losses; mediocre 3.96/5 rating; group-buy circulation.

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer
**Branislav Bridzik** (Slovakia) — a named, identifiable MQL5 author (accountable). MQL5 listing: 30
reviews, **3.96/5** (mediocre). Also circulating via group-buy/pirate-adjacent sites (eafxstore) —
discovery/negative signal only.

## MT5 Compatibility & Dependencies (publicly documented only)
- Platform: MT5. Instrument: **XAUUSD** only. Timeframe: **M15**.
- Min deposit $200 (cent account); optimal $2,000+. VPS recommended. Adjustable magic numbers/comments
  ("prop-firm compatible"). The verified signal ran on **IC Markets EU** raw spreads.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** The only real-money configuration on record produced a 72.56% DD; no defensible sizing
exists. Reducing lot size cannot make a 1-day-80%-concentration return profile fit a 5%-daily envelope.

## Cost & Licensing
$149 one-time or $49/month; closed binary; also on group-buy/pirate-adjacent sites (malware caveat, ≤ weakest
community tier, negative signal only).

## Source Links
- https://www.mql5.com/en/market/product/157989 — 2026-06-23 — vendor MQL5 listing (fetched) — affiliate(vendor)
- https://www.mql5.com/en/signals/2356533 — 2026-06-23 — vendor MQL5 live signal, REAL acct (fetched) — platform-hosted
- https://eafxstore.com/blog/xau-master-ea-mt5-settings/ — 2026-06-23 — group-buy settings blog (via search) — affiliate(group-buy)
- WebSearch lead aggregations (mechanism, MQL5 comments, negative case) — 2026-06-23 — leads/community

## Analyst Notes
- **FACTS:** Bridzik (accountable); XAUUSD M15, 13 simultaneous systems, hard SL, advertised 5%/10% DD
  auto-cutoff; $149/$49mo; real MQL5 signal since 2026-01-29: 78.01% gain, **72.56% max DD**, 95.76%
  monthly, 725 trades, $1k→$1.85k, 0 subscribers; MQL5 3.96/5; v7.2 added multi-order/two-way + higher DD.
- **ANALYSIS:** survives Gate A (no grid/martingale) but the realized risk from many simultaneous wide-SL
  positions produced a 72.56% DD; the marketed prop-safe cutoff is contradicted by its own account; Tier-2
  inspectable evidence makes Avoid certain.
- **ASSUMPTIONS (flagged):** the signal reflects a recent version near default config (vendor's own account);
  win rate/PF not on the fetched aggregates (logged-in trade-level needed).

## Future Research Needed
- If the MQL5 signal's trade-level history (logged-in) becomes inspectable, extract the per-trade/daily
  distribution to compute a formal ROR and confirm whether the DD-cutoff ever fires.
- Watch for a v7.x signal with a genuinely bounded DD (≤~6%) over ≥6 months — would be required before any
  re-vet above Avoid; current evidence is strongly negative.

</details>

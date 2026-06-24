[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# Gold Trading SMC EA (GOLD Scalper PRO) — MT4/MT5
*An anonymous SMC gold EA whose reported real-money signal shows a prop-incompatible 26.6% drawdown on a razor-thin edge — ⛔ Avoid.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.0 / 10** · poor |
| **Mechanism** | XAUUSD SMC impulse-and-correction, single-position, hard SL, no grid/martingale · confidence **Medium** · Gate B: **black box** (closed .ex4/.ex5) |
| **Evidence** | ◐ best_tier **T3** · real-money signal reported via cracked review (not independently fetched) · ~5–6 mo |
| **Risk of ruin** | NON-ESTIMABLE |
| **Legality** | FN ⚠️ · FP ⚠️ · 5% ⚠️ · TFT ⚠️ (all Conditional) |
| **Verified perf** | +25.87% (reported) [T3] · max DD **26.63%** [T3] · ~5–6 mo |
| **Vendor** | Anonymous ⚠️ |

> **Bottom line — binding criterion:** the reported real-money signal (IC Markets, ~5–6 mo) shows a
> **prop-incompatible 26.63% max drawdown** on a **razor-thin PF 1.10** edge (avg loss ~2.5× avg win),
> contradicting the "hard SL / safe SMC" framing. Closed `.ex4` binary, anonymous vendor, **signal not
> independently fetched/verified** → best_tier **Tier 3** + ROR **NON-ESTIMABLE** → deterministic Avoid.

---
## Profile

## Overview
A fully-automated XAUUSD ("gold") EA distributed as a free/cracked **closed binary** (.ex4/.ex5), also
listed on MQL5 as "**GOLD Scalper PRO**." Uses a Smart-Money-Concepts impulse-and-correction entry.

## Strategy Mechanism
Vendor-described (closed binary, no teardown): "reads a distinctive market **impulse**, then enters in that
direction on the following **correction**," **one position per trade, hard SL on every order, no grid, no
martingale.** **Gate B status: black box** (closed .ex4/.ex5) with a vendor-documented hard SL.

## Mechanism Inference Confidence
**Medium.** The no-grid/martingale + hard-SL claim is plausible and the reported signal is non-cliff, but
the **26.63% max DD** with **PF 1.10** (avg win $4.95 vs avg loss $12.52, 73.5% win) is a high-win/large-
loss profile whose "safe" framing the realized drawdown contradicts.

## Recommended Instruments
XAUUSD only; "works the same on all timeframes."

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Reported live signal (v2.0, IC Markets MT5, Jan–Jun 2026): 355 trades, 73.52% win, +25.87% ($113.62 on $439.27), **PF 1.10**, **max DD 26.63% by balance**, avg hold 52 min | forexcracked.com listing (review of the MQL5 "GOLD Scalper PRO" signal) | cracked-site review of a vendor signal | pirate / vendor | **TIER3** | 2026-06-24 | Low–Medium | Real-money signal *reported* but **not independently fetched/verified** → Tier 3 (would be Tier 2A only if the actual MQL5 signal page were fetched). 26.63% DD is prop-incompatible. |
| Mechanism: SMC impulse/correction, single-position, hard SL, no grid/martingale | https://www.forexcracked.com/forex-ea/gold-trading-smc-ea-free-download/ | cracked-site listing (fetched) | pirate | TIER4 | 2026-06-24 | Medium | Negative/discovery use only. |
| Negative-case evidence | forexcracked user comments | cracked-site | mixed | n/a | 2026-06-24 | Low | "closes trades immediately", "cannot backtest", "doesn't load in MT4", "not working/paused" — operational failures. |

## Source Reliability Assessment
source_count **2** · independent_source_count **0** (the live-signal stats are a cracked-site review of a
vendor signal; no independently fetched signal/Myfxbook) · affiliate_source_count **1** (forexcracked).
**Best evidence found:** a *reported* real-money MQL5 signal — but **anonymous vendor, closed binary, and
the signal page was not fetched**, so it cannot be credited above Tier 3.

## Unverified Claims
- The entire live-signal record (26.63% DD, PF 1.10, +25.87%) — reported via a cracked-site review, **not
  independently verified**; could be confirmed/upgraded only by fetching the actual MQL5 "GOLD Scalper PRO"
  signal (would still be Avoid for the 26.63% DD).
- "Safe / hard SL / capital preservation" framing — contradicted by the reported 26.63% drawdown.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | ~4–5%/mo (+25.87% over ~5–6 mo, reported) | [T3] | forexcracked (signal review) |
| Maximum Drawdown | **26.63%** (by balance, reported) | [T3] | forexcracked (signal review) |
| Win Rate | 73.52% (355 trades, reported) | [T3] | forexcracked (signal review) |
| Profit Factor | **1.10** (avg win $4.95 / avg loss $12.52) | [T3] | forexcracked (signal review) |
| Track Length | ~5–6 months (Jan–Jun 2026) | [T3] | forexcracked (signal review) |
| Real vs Demo | Real (IC Markets, $439 deposit) — reported, not fetched | [T3] | forexcracked (signal review) |

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** ROR is estimable only from a **fetched, independently-verified** real-money trade-level
record (Tier 0/1/2A). Here the real-money signal is **reported via a cracked-site review** and was not
independently fetched, so there is no trustworthy distribution to resample → NON-ESTIMABLE. Even taken at
face value, the **26.63% max DD by balance is prop-incompatible** (a 10% overall-DD firm account would have
blown), and **PF 1.10** means a fragile, easily-negative edge. DD-definition mismatch caveat applies.

## Backtest Assessment
No public real-tick/cost/OOS backtest detail; user comments report it "cannot backtest" / fails to load.
Near-worthless as proof.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS.** No banned mechanism claimed (SMC impulse/correction, single-position, hard SL, no
  grid/martingale); reported signal is non-cliff. Mechanism inference Medium.
- **Gate B — TRIGGERED (black box).** Closed `.ex4/.ex5` binary, anonymous vendor, no teardown → Compliance
  ≤ 5, Risk ≤ 4, verdict ≤ Watchlist. Has a documented hard SL → not auto-Avoided by criterion 3 (it is
  Avoided by criteria 2 & 4 below).
- **Gate C — per-firm legality:** Conditional (unverifiable closed binary).

## Per-Firm Legality Verdict

| Firm | Verdict | Rulebook | Reason |
|------|:-------:|:--------:|--------|
| FundedNext | ⚠️ Conditional | v1 (PROVISIONAL — primary 503 ×6) | Mechanism claimed non-banned but unverifiable closed binary; stale rulebook |
| Funding Pips | ⚠️ Conditional | v1 | Can't confirm mechanism from a closed `.ex4` |
| The 5%ers | ⚠️ Conditional | v1 | Same |
| The Funded Trader | ⚠️ Conditional | v1 | Same |
| Alpha Capital *(ref)* | ⛔ Prohibited | v1 | Closed-source commercial EA (non-gating) |
| Goat Funded Trader *(ref)* | ⛔ Prohibited | v1 | Commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **Drawdown:** reported 26.63% max DD ≈ 2.7× a 10% overall limit → would blow any primary funded account.
- **Edge fragility:** PF 1.10 (avg loss 2.5× avg win) → a short bad run flips it negative.

## Mechanical Rule-Respect
Hard SL claimed in the listing (vendor-documented), but **contradicted by the reported 26.63% DD**; no
independent teardown, no documented daily-loss stop. → Risk control-evidence: contradicted/claimed →
low; Gate B caps Risk ≤ 4.

## Community Sentiment
Only cracked-site user comments, all **operational** ("closes trades immediately", "cannot backtest",
"doesn't load", "not working/paused") — installation/compatibility complaints, not independent strategy
review. No verified independent community track.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a thin SMC edge (PF 1.10) that a 73.5% win rate masks — most wins
   are tiny ($4.95) and the rare losses are large ($12.52); a normal losing cluster produces the reported
   26.63% drawdown and can go negative outright.
2. **Prop-server case:** a 26.63% balance DD already exceeds every primary firm's overall-DD limit — the EA
   would not survive a funded account even before prop spreads/commissions widen the loss.
3. **Variance case:** a calm stretch might pass an evaluation, but the realized drawdown shows it cannot
   survive the funded phase — passing ≠ surviving.
4. **Evidence fragility:** the only "evidence" is a **cracked-site review of an anonymous vendor's signal**,
   not an independently fetched record. The single thing that would change the verdict — a fetched,
   verified, adequately-capitalized ≥6-month record with prop-compatible DD — does not exist here.

## Scores
*latent × multiplier (or ceiling) = adjusted. best_tier **TIER3** → Multiplier A 0.25, Multiplier B 0.30;
ROR **NON-ESTIMABLE** → Survival ×min(A,0.20); Gate B → Compliance ≤ 5, Risk ≤ 4.*

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 1 | ×0.20 (ROR cap) | **1** | 0.30 |
| Prop-Firm Compliance | 20% | 5 | Gate-B min(5, 5) | **5** | 1.00 |
| Risk Management | 15% | 2 | min(Gate-B 4, contradicted controls) | **2** | 0.30 |
| Challenge-Passing | 15% | 2 | ×0.25 | **1** | 0.15 |
| Consistency | 10% | 1 | ×0.30 | **1** | 0.10 |
| Transparency | 5% | 2 | ×0.30 | **1** | 0.05 |
| Profitability | 5% | 2 | ×0.30 | **1** | 0.05 |
| **Overall** | | | | | **2.0** |

*Band: **poor** (<4.0). Overall = 0.30·1 + 0.20·5 + 0.15·2 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1 = 1.95 → 2.0.*

## Deployment Verdict
⛔ **AVOID.** Binding criterion: reported real-money signal shows a **prop-incompatible 26.63% max DD** on a
**razor-thin PF 1.10** edge; anonymous closed-binary vendor with the signal **not independently verified**
→ best_tier Tier 3 + ROR NON-ESTIMABLE. Fails Avoid criteria 2 (Tier-3 headline) and 4 (NON-ESTIMABLE +
Tier 3).

## Similar EAs
Same XAUUSD real-money-signal-but-catastrophic-DD profile as [[xau-master-mt5]] (72.56% DD) and
[[mad-turtle-mt5]] (68–83% DD) — all Avoid for prop-incompatible drawdown. Contrast [[gold-prop-firm-robot]]
(6.41% DD → Watchlist).

## Red Flags
- 26.63% reported max DD → would blow any prop account; PF 1.10 → fragile/near-breakeven edge.
- Anonymous vendor; closed `.ex4/.ex5` binary; cracked-site only; signal not independently fetched.
- "Safe / hard SL" marketing contradicted by the realized drawdown.

<details>
<summary><strong>Appendix — full audit trail</strong></summary>

## Vendor / Developer
Anonymous (not named on the listing or MQL5 review) — accountability red flag. Listed as "GOLD Scalper PRO"
on MQL5; distributed free/cracked as "Gold Trading SMC EA."

## MT5 Compatibility & Dependencies
MT4 v2.1 / MT5; XAUUSD; min balance ~$1,000 (listing); the reported signal ran $439 at IC Markets.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable** — no verified sizing basis; the only reference is a $439 account with a 26.63% DD, which
is prop-incompatible at any size.

## Cost & Licensing
Free/cracked closed binary (.ex4/.ex5); MQL5 paid listing as "GOLD Scalper PRO." Malware caveat applies to
the cracked file.

## Source Links
- https://www.forexcracked.com/forex-ea/gold-trading-smc-ea-free-download/ — 2026-06-24 — cracked listing (fetched: mechanism, reported MQL5 signal stats, user comments) — pirate (negative/discovery only)
- WebSearch "Gold Trading SMC EA smart money concepts mechanism martingale" / "...forexcracked" — 2026-06-24 — discovery + mechanism + negative case — mixed

## Analyst Notes
- **FACTS:** fetched cracked listing — SMC impulse/correction, single-position, hard SL, no grid/martingale,
  closed .ex4/.ex5, anonymous; reported MQL5 signal (IC Markets, ~5–6 mo): 355 trades, 73.5% win, +25.87%,
  PF 1.10, 26.63% max DD; user comments report operational failures.
- **ANALYSIS:** mechanism non-banned → Gate A pass; closed binary → Gate B; signal reported but not
  independently fetched → Tier 3, ROR NON-ESTIMABLE; 26.63% DD + PF 1.10 → Avoid (criteria 2 & 4). Overall 2.0.
- **ASSUMPTIONS (flagged):** the reported signal stats are accurate; fetching the actual MQL5 signal could
  reclassify it Tier 2A, but the 26.63% DD would keep the verdict at Avoid.

## Future Research Needed
- Operator to fetch the actual MQL5 "GOLD Scalper PRO" signal to confirm the 26.63% DD / PF 1.10 figures;
  the verdict (Avoid, prop-incompatible DD) would not change without a fundamentally different track.

</details>

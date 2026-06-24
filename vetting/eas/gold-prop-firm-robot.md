[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# Gold Prop Firm Robot (Prop Firm Gold EA) — MT5
*An XAUUSD breakout EA with a real but short, thin-edge 6-month live signal — 🟡 Watchlist, pending a longer track and proof the edge isn't luck.*

## At a Glance
| | |
|---|---|
| **Verdict** | 🟡 **WATCHLIST** |
| **Overall** | **3.0 / 10** · poor |
| **Mechanism** | XAUUSD breakout + intraday patterns, single-position, hard SL/TP, no martingale/grid · confidence **Medium** · Gate B: **black box** (vendor-documented SL) |
| **Evidence** | ◉ best_tier **T2A** · real-money · ~26 wk (~6 mo) · MQL5 live signal 2356196 (ICMarkets) |
| **Risk of ruin** | **ESTIMABLE — ROR-Low** · overall-DD breach low-moderate · daily-DD possible/unquantified |
| **Legality** | FN ⚠️ Conditional · FP ✅ · 5% ✅ · TFT ✅ |
| **Verified perf** | +28.03% real [T2A] · max DD **6.41%** [T2A] · ~26 wk |
| **Vendor** | Jimmy Peter Eriksson — identifiable & high-rep (MQL5 ~8,137) |

> **Bottom line — binding criterion:** real-money but caveated (Tier 2A) — a single short **~6-month
> $2,500 ICMarkets signal** with a **thin edge (PF 1.20, 50% win)** and **80% of growth concentrated in a
> few days** (lumpy, luck-suspect); no funded-account evidence. The marketed "190% / 16-month / 16% DD"
> record is a **different, unverified** account. Fails Deployable gates 2, 3, 4, 7, 8.

---
## Profile

## Overview
A closed-source XAUUSD ("gold") **breakout** EA sold on the MQL5 Market as "Prop Firm Gold EA" and
redistributed on cracked sites as "Gold Prop Firm Robot." Combines "breakout-based concepts to capture the
dominant intraday direction, together with intraday price patterns"; single position, hard SL/TP, news
filter. Distinguishing feature: a **fetchable real-money MQL5 live signal**, which is what this verdict
credits — not the louder cracked-site numbers.

## Strategy Mechanism
Vendor-described (closed source, no third-party teardown): XAUUSD breakout + intraday patterns, "**not
based on indicators or fixed timeframes**," **single-position trading with hard stop-loss and take-profit**,
explicitly "**No Risky Martingale/Grid**." **Gate B status: black box** with a vendor-documented hard SL
that is *corroborated* (not proven) by the real signal's contained **6.41% max equity DD** over 194 trades.

## Mechanism Inference Confidence
**Medium.** The no-martingale/grid + hard-SL claim is consistent with the real-money equity behaviour
(contained DD, 50% win, PF 1.20, no cliff), but the source is closed and unaudited. The **PF 1.20 with 80%
of growth in a few days** points to a thin, concentration-dependent edge rather than a robust one.

## Recommended Instruments
XAUUSD (gold) only.

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD: +28.03% gain, **6.41% max equity DD**, 194 trades, 50% win, PF 1.20, REAL account, $2,500 deposit, started 2026-01-28 (~26 wk) | https://www.mql5.com/en/signals/2356196 | MQL5 live signal (REAL, broker ICMarketsSC-MT5-2) | vendor-hosted but platform-recorded real-money trade history | **TIER2A** | 2026-06-24 | Medium | Real-money, inspectable → Tier 2A; demoted from Tier 1 by **short track (~6mo)** + modest deposit. MQL5 flags **"80% of growth in a few days"** (concentration risk). |
| Mechanism: XAUUSD breakout, single-position, hard SL/TP, no martingale/grid | https://www.mql5.com/en/market/product/153540 | MQL5 vendor listing (Jimmy Peter Eriksson) | vendor | TIER3 (claim) | 2026-06-24 | Medium | Corroborated (not proven) by contained real DD. |
| "190% / 16-month live / 16.05% DD / PF 2.47" | forexcracked.com (cracked listing) | cracked-site | pirate | TIER4 | 2026-06-24 | Low | **Different account** from the linked public signal; not verified; cracked-site → not credited. |
| "15 years backtest", "2.9% DD in real trading" | mql5 / cheaperforex | vendor/affiliate | vendor | TIER3/4 | 2026-06-24 | Low | Backtest claim; "2.9% DD" conflicts with the fetched 6.41% — worse reading taken. |
| Negative-case evidence | WebSearch (scam/blown/losing) | search | independent | n/a | 2026-06-24 | Low | No specific blown-account reports surfaced for this product (recorded as a no-hit). |

## Source Reliability Assessment
source_count **5** · independent_source_count **1** (MQL5 platform signal data; negative-case search) ·
affiliate_source_count **2** (cheaperforex, forexcracked). **Best evidence found:** the **fetched
real-money MQL5 signal 2356196** (Tier 2A) — the credited basis. Vendor is **named and high-reputation**
(Jimmy Peter Eriksson; MQL5 reputation ~8,137).

## Unverified Claims
- The cracked-site **"190% / 16 months / 16.05% DD / 71.7% win / PF 2.47"** record — a **different,
  unverified** account; not the public signal. **Tier 4**, not credited.
- "Traded live 15 months before release," "15-year backtest," "2.9% DD" — vendor/affiliate claims.
- Funded-account survival; behaviour beyond the single 6-month $2,500 signal; durability of the edge once
  the few high-growth days are excluded.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | ~4.6%/mo (28.03% over ~6 mo, real) | [T2A] | mql5.com/en/signals/2356196 |
| Maximum Drawdown | 6.41% (equity, MQL5 method) | [T2A] | mql5.com/en/signals/2356196 |
| Win Rate | 50.00% (194 trades) | [T2A] | mql5.com/en/signals/2356196 |
| Profit Factor | 1.20 | [T2A] | mql5.com/en/signals/2356196 |
| Track Length | ~26 weeks (since 2026-01-28) | [T2A] | mql5.com/en/signals/2356196 |
| Real vs Demo | **Real** ($2,500 deposit, 1:500, ICMarkets) | [T2A] | mql5.com/en/signals/2356196 |
| Cracked "190%/16.05% DD" | NOT CREDITED (different account) | [T4] | forexcracked |

## Risk-of-Ruin Analysis
**ESTIMABLE — ROR-Low** (rests on Tier 2A real-money trade-level history; directional only).
- **Method:** directional read of the live account's realized distribution (194 real trades, 50% win,
  PF 1.20, 6.41% max equity DD); closed-form reasoning on published aggregates (per-trade list MQL5-login-
  gated → no resample; keeps it ROR-Low, never ROR-High).
- **P(violating overall DD ~10%):** **low-moderate.** Historical max DD 6.41% is ~64% of a 10% static
  limit over a calm ~6-month window; historical max understates future and the edge is concentration-
  dependent → a 10% breach is possible but not yet demonstrated.
- **P(violating daily DD ~5%):** possible/unquantified (no intraday data).
- **Caveats (mandatory):** (1) **short window** (~6 mo) and **modest deposit** ($2,500) → wide interval;
  (2) **edge concentration** — MQL5 flags 80% of growth in a few days, so PF 1.20 likely overstates a
  steady edge → ROR understated if those days don't recur; (3) **DD-definition mismatch** (MQL5 equity DD
  ≠ firm rule); (4) **no shock observed.** → `ror_confidence: Low`; does not satisfy Deployable gate 7.

## Backtest Assessment
"15-year backtest" and "2.9% DD in real trading" are vendor/affiliate claims; the "2.9%" conflicts with the
**fetched 6.41%** real DD (worse reading taken). No public real-tick/cost/OOS detail → near-worthless as
proof. Only the live signal is credited.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS.** No banned mechanism: XAUUSD breakout, single-position, hard SL/TP, "no martingale/
  grid," corroborated by the contained real DD (no cliff). Mechanism inference Medium.
- **Gate B — TRIGGERED (black box).** Closed source, no teardown → Compliance ≤ 5, Risk ≤ 4, verdict ≤
  Watchlist. NOT auto-Avoided (vendor-documented hard SL → criterion 3 does not fire).
- **Gate C — per-firm legality:** not prohibited at all primaries (below).

## Per-Firm Legality Verdict

| Firm | Verdict | Rulebook | Reason |
|------|:-------:|:--------:|--------|
| FundedNext | ⚠️ Conditional | v1 (PROVISIONAL — primary 503 ×6 runs) | Mechanism fine; rests on a stale/unconfirmed rulebook → cannot exceed Conditional |
| Funding Pips | ✅ Permitted | v1 | Non-martingale/grid single-position breakout within policy |
| The 5%ers | ✅ Permitted | v1 | Mechanism clean |
| The Funded Trader | ✅ Permitted | v1 | Mechanism clean |
| Alpha Capital *(ref)* | ⛔ Prohibited | v1 | Closed-source commercial EA can't meet source-code submission (non-gating) |
| Goat Funded Trader *(ref)* | ⛔ Prohibited | v1 | Bans commercial challenge EAs (non-gating) |

**Standing compliance risk (not a prohibition):** a widely-sold/cracked commercial EA run identically by
many buyers can trip shared-strategy / copy-trade detection.

## Rule-Violation Flags
- **Drawdown headroom:** real max DD 6.41% ≈ 64% of a 10% overall limit → just over the Deployable-gate-4
  ceiling (≤60%); usable headroom but not deployable-grade.
- **Edge concentration:** 80% of growth in a few days → a bad stretch could erase the cushion quickly.

## Mechanical Rule-Respect
Hard per-trade SL/TP **vendor-documented** and consistent with the real DD; **not** independently
demonstrated (no teardown); no documented account-level daily-loss stop. → Risk control-evidence ceiling
vendor-documented (Risk ≤ 5); Gate B caps Risk ≤ 4 (lowest applies).

## Community Sentiment
MQL5: product 4.53/5 (33 reviews), author 4.4/5 (126 reviews) — vendor-platform, not independent. No
independent forum teardown found; **negative-case search returned no specific blown-account reports**
(no-hit recorded). Affiliate/cracked listings (cheaperforex, forexcracked) flagged, not credited.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a real but **thin, concentration-dependent edge** — PF 1.20 with
   80% of 6 months' gains in a few days means most of the period was roughly flat; remove the lucky days
   and the edge may be ~breakeven. A breakout edge on a single instrument is regime-fragile.
2. **Prop-server case:** wider prop spreads/commissions on XAUUSD and the firm's own DD calc could erase a
   1.20-PF edge and push the 6.41% DD past a tighter daily/overall limit on a bad cluster.
3. **Variance case:** could pass a calm-month evaluation and then stall or breach on the funded account —
   passing ≠ surviving, and the survival evidence (a longer, deeper-tested track) is absent.
4. **Evidence fragility:** everything credited rests on **one 6-month $2,500 signal**; the headline
   "190%/16-month" record is a different, unverified account. The single piece that would change the
   verdict — a ≥6-month, adequately-capitalized, independently-verified (or funded) record showing the
   edge persists without the concentration days — does not exist publicly.

## Scores
*latent × multiplier (or ceiling) = adjusted. best_tier **TIER2A** → Multiplier A 0.45, Multiplier B 0.60;
ROR **ESTIMABLE/Low** → no Survival cap; Gate B → Compliance ≤ 5, Risk ≤ 4.*

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 4 | ×0.45 (Tier 2; ROR-Low) | **2** | 0.60 |
| Prop-Firm Compliance | 20% | 7 | Gate-B min(7, 5) | **5** | 1.00 |
| Risk Management | 15% | 5 | min(Gate-B 4, ctrl 5) | **4** | 0.60 |
| Challenge-Passing | 15% | 5 | ×0.45 | **2** | 0.30 |
| Consistency | 10% | 3 | ×0.60 | **2** | 0.20 |
| Transparency | 5% | 5 | ×0.60 | **3** | 0.15 |
| Profitability | 5% | 4 | ×0.60 | **2** | 0.10 |
| **Overall** | | | | | **3.0** |

*Band: **poor** (<4.0). Overall = 0.30·2 + 0.20·5 + 0.15·4 + 0.15·2 + 0.10·2 + 0.05·3 + 0.05·2 = 2.95 → 3.0.*

## Deployment Verdict
🟡 **WATCHLIST.** Binding criterion: **real-money but caveated (Tier 2A) — short ~6-month single $2,500
signal, thin edge (PF 1.20, 50% win) with 80% of growth concentrated in a few days, no funded evidence;
the marketed 190%/16-month record is a different unverified account.** Fails Deployable gates 2, 3, 4, 7, 8.
ROR estimable only at ROR-Low.

## Similar EAs
Mechanism-adjacent to the archive's other XAUUSD EAs (XAU Master, Mad Turtle, The Gold Reaper) — but unlike
those (catastrophic verified DDs), this one's real signal shows a **contained 6.41% DD**, which is why it
reaches Watchlist rather than Avoid. Distinct from One Man Army (multi-pair reversal).

## Red Flags
- PF 1.20 + 50% win + **80% of growth in a few days** → concentration/luck-dependent edge.
- Cracked-site "190%/16% DD" is a **different account** than the public signal — marketing/record mismatch.
- "2.9% DD" affiliate claim conflicts with the fetched 6.41% real DD.
- Closed source → Gate B; commercial/cracked → shared-strategy detection risk; Alpha/Goat barred.

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer
**Jimmy Peter Eriksson** (MQL5 author; ~8,137 reputation, 4.4/5 over 126 reviews) — identifiable and
accountable, high-reputation. Sells "Prop Firm Gold EA" (MQL5 product 153540) at $399 (list $990).
Redistributed as a free/cracked "Gold Prop Firm Robot" download.

## MT5 Compatibility & Dependencies
MT5; XAUUSD; news filter fetches data over the internet; recommended deposit ~$200 (vendor) — the live
signal runs $2,500 at 1:500 on ICMarkets.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable from public data.** The only sizing reference is a $2,500/1:500 account over ~6 months;
restating to funded sizing/leverage is an assumption, and the concentration-dependent edge makes worst-case
sizing especially uncertain.

## Cost & Licensing
$399 (MQL5; list $990). Also circulated as a free/cracked download (Tier-4, malware caveat).

## Source Links
- https://www.mql5.com/en/signals/2356196 — 2026-06-24 — MQL5 live signal (REAL, ICMarkets; Tier 2A evidence) — vendor-hosted/platform-recorded
- https://www.mql5.com/en/market/product/153540 — 2026-06-24 — MQL5 vendor listing (mechanism, vendor, 15mo-live claim) — affiliate(vendor)
- https://www.forexcracked.com/forex-ea/gold-prop-firm-robot-free-download/ — 2026-06-24 — cracked listing (different '190%/16.05% DD' account; not credited) — pirate (discovery/negative only)
- https://cheaperforex.com/product/prop-firm-gold-ea-mt5/ — 2026-06-24 — affiliate ('2.9% DD', 13mo-signal claim) — affiliate
- WebSearch negative-case (scam/blown/losing) — 2026-06-24 — no specific hits recorded

## Analyst Notes
- **FACTS:** fetched MQL5 signal 2356196 — REAL ICMarkets, $2,500, +28.03%, 6.41% max DD, 194 trades, 50%
  win, PF 1.20, since 2026-01-28 (~26 wk), MQL5 "80% of growth in a few days" flag. Vendor Jimmy Peter
  Eriksson; mechanism XAUUSD breakout single-position hard SL/TP, no martingale/grid.
- **ANALYSIS:** real-money inspectable → Tier 2A; ROR estimable ROR-Low; clean mechanism → Gate A pass;
  closed source → Gate B (Watchlist ceiling); thin/concentrated edge is the survival risk → Watchlist,
  Overall 3.0. The cracked-site 190%/16% DD is a different unverified account and is not credited.
- **ASSUMPTIONS (flagged):** the public signal reflects the purchasable default settings (Medium
  confidence); the calm ~6-month window hasn't sampled a shock; deposit-scaling is an assumption.

## Future Research Needed
- Operator to obtain a **longer (≥6-month, ideally 12-month+), adequately-capitalized** real-money or
  funded record and confirm the edge **excluding the concentration days**; inspect trade-by-trade (login)
  for steadiness. Reconcile the cracked-site "190%" account vs the public signal.

</details>

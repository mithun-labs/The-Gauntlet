[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# Dark Algo (MT5) — Marco Solito

*A EURUSD/GBPUSD H1 scalper with a long REAL-money record that itself proves a 52.63% max drawdown — ⛔ Avoid: real but wholly prop-incompatible.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.1 / 10** · poor |
| **Mechanism** | EURUSD/GBPUSD H1 "scalping" (Stochastic+ATR), vendor-claimed hard SL + "No Martingale"; configurable max-simultaneous-positions · confidence **Low** · Gate B: **black box** (vendor-documented SL) |
| **Evidence** | ◉ best_tier **T2A** · real-money · ~74 wk · MQL5 signal 2312403 (Headway-Real, $100 deposit) |
| **Risk of ruin** | **ESTIMABLE — ROR-Low** · overall-DD breach **≈ certain** (52.63% realized DD vs ~10% limits) |
| **Legality** | FN ⚠️ Conditional · FP ✅ · 5% ✅ · TFT ✅ |
| **Verified perf** | +625% real [T2A] · max DD **52.63%** [T2A] · ~74 wk · $100 @ 1:500 |
| **Vendor** | Marco Solito (msolito59) — identifiable, high-rep MQL5 seller (45+ products) |

> **Bottom line — binding criterion:** the EA's **own real-money MQL5 signal** (REAL, Headway, ~74 weeks)
> shows a **52.63% max equity drawdown** — roughly **5× the tightest primary's 10% max-overall-DD limit** —
> and the vendor itself warns "a large drawdown may occur on the account again." Real-money but
> **affirmatively prop-incompatible**: this is not a promising-but-unproven Watchlist candidate, it is a
> record that proves the EA would blow a funded account. Fails Deployable gates 2, 3, 4, 7, 8.

---
## Profile

## Overview
A closed-source EURUSD/GBPUSD scalping EA sold on the MQL5 Market (product 92403 for MT5, 92404 for MT4) by
prolific vendor **Marco Solito** (the "Dark" series — Dark Venus, Dark Gold, Dark Titan, Dark Nova). Priced
$399 (next $499). Marketed as a "latest-generation" H1 scalper using Stochastic + ATR with a built-in hard
stop loss and "No Martingale." Distinguishing feature for this vetting: a **fetchable, long, real-money MQL5
signal of the default settings**, which is what this verdict credits — and which is decisively negative.

## Strategy Mechanism
Vendor-described (closed source, no independent teardown): H1 scalping on EURUSD/GBPUSD, Stochastic + ATR
entries, **"built-in hard stop loss for all trades," "No Martingale,"** risk-percent money management, and a
**configurable maximum number of simultaneous positions**. **Gate B status: black box.** The vendor's
no-martingale/hard-SL claim is **contradicted in effect** by the real signal's **52.63% equity drawdown** —
either the risk-per-trade is extreme, or losers are held/stacked (the configurable multi-position setting is
consistent with grid/recovery behaviour the marketing does not disclose). Mechanism could not be confirmed.

## Mechanism Inference Confidence
**Low.** The 79.67% win rate + PF 3.44 + **52.63% DD** profile (many small wins, occasional very large
adverse excursion) plus a **configurable max-simultaneous-positions** setting and the vendor's explicit
"large drawdown may occur again" warning are **consistent with hold-the-loser / grid-style recovery** beneath
a "hard SL / no martingale" label — but no settings screenshot or third-party teardown confirms it, so this
is not a strong-enough banned-mechanism signature for a confident Gate A exclusion. Recorded as a red flag.

## Recommended Instruments
EURUSD, GBPUSD (H1).

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline real-money: +625.22% gain, **52.63% max equity DD**, 369 trades, 79.67% win, PF 3.44, REAL Headway account, $100 deposit, 1:500, since 2025-05-30 (~74 wk) | https://www.mql5.com/en/signals/2312403 | MQL5 live signal (REAL, Headway-Real) | vendor-hosted but platform-recorded real-money trade history | **TIER2A** | 2026-06-29 | Medium | Real-money, inspectable → Tier 2A; demoted from Tier 1 by **$100 deposit + 1:500 leverage + vendor-hosted**. Vendor warns "a large drawdown may occur on the account again." |
| Mechanism: EURUSD/GBPUSD H1 scalping, Stochastic+ATR, hard SL, "No Martingale", configurable max positions | https://www.mql5.com/en/market/product/92403 | MQL5 vendor listing | vendor | TIER3 (claim) | 2026-06-29 | Medium | "No Martingale / hard SL" **contradicted in effect** by the real 52.63% DD. |
| Companion signal "Dark Nova 3 Pairs": +953%, 39% DD, 868 trades, 76% win, PF 2.90, ~82 wk | https://www.mql5.com/en/users/msolito59/seller | MQL5 seller profile | vendor | TIER3/2A | 2026-06-29 | Low | Different product; same vendor's risk signature (high win + deep DD). |
| Negative-case: user "max drawdown 28% after 4 months"; "no trades for extended periods"; disputed "accounts manipulated/deleted" | WebSearch (Dark Algo scam/blown/martingale) + myfxbook DarkEAs discussion | search / forum | independent (mixed) | TIER4 (lead) | 2026-06-29 | Low | Negative-case search ran; corroborates large-DD risk. Myfxbook page itself 403'd the fetch tool. |

## Source Reliability Assessment
source_count **5** · independent_source_count **1** (negative-case search; MQL5 platform-recorded signal
data) · affiliate_source_count **2** (forexroboteasy, eafxstore/groupbuy). **Best evidence found:** the
**fetched real-money MQL5 signal 2312403** (Tier 2A) — which is decisively negative (52.63% DD). Vendor is
**named and high-reputation** (Marco Solito / msolito59; 45+ products, Dark Venus 100k+ downloads).

## Unverified Claims
- "Hard stop loss for all trades" and "No Martingale" — vendor claims **contradicted in effect** by the real
  52.63% equity DD; no independent teardown.
- Myfxbook "verified" track (DarkEAs member) — page 403'd the fetch tool; not independently inspected this run.
- Any prop-firm pass/payout claim — none credibly evidenced (Tier 4 if asserted).
- Behaviour under default settings on a properly-capitalized (non-$100/1:500) account.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|:----:|--------|
| Average Monthly Return | ~625% over ~74 wk ≈ very high but on $100/1:500 (non-representative) | [T2A] | mql5.com/en/signals/2312403 |
| Maximum Drawdown | **52.63%** (equity, MQL5 method) | [T2A] | mql5.com/en/signals/2312403 |
| Win Rate | 79.67% (369 trades) | [T2A] | mql5.com/en/signals/2312403 |
| Profit Factor | 3.44 | [T2A] | mql5.com/en/signals/2312403 |
| Track Length | ~74 weeks (since 2025-05-30) | [T2A] | mql5.com/en/signals/2312403 |
| Real vs Demo | **Real** ($100 deposit, 1:500, Headway-Real) | [T2A] | mql5.com/en/signals/2312403 |
| User-reported DD | 28% after 4 months | [T4] | WebSearch lead |

## Risk-of-Ruin Analysis
**ESTIMABLE — ROR-Low** (rests on Tier 2A real-money trade-level history; directional only) — **and the
result is decisively bad.**
- **Method:** directional read of the live account's realized distribution (369 real trades, 79.67% win,
  PF 3.44, **52.63% max equity DD**); per-trade list MQL5-login-gated → no resample, so ROR-Low not ROR-High.
- **P(violating overall DD ~10%):** **≈ certain.** The account has **already** drawn down 52.63% — over
  **5× the 5%ers / FundedNext 10% static overall limit**. A strategy with this realized DD profile would
  breach a prop max-overall-DD limit with near certainty; the vendor's own "large DD may occur again" warning
  confirms the tail is live, not a one-off.
- **P(violating daily DD ~5%):** **high** (a 52% equity excursion implies single-window losses far exceeding
  a 5% daily cap, though intraday granularity is not published).
- **Caveats (mandatory):** (1) **$100 deposit + 1:500 leverage** make the % return *and* the % DD
  non-representative of funded sizing — but the DD is so large that even heavy de-risking cannot bring it
  under a 10% limit while retaining the edge; (2) **DD-definition mismatch** (MQL5 equity DD ≠ firm rule —
  but the gap is ~5×, so the conclusion is robust to definition); (3) returns are likely **autocorrelated**
  (hold-the-loser signature); (4) no benign reading survives a 52% realized DD. → `ror_confidence: Low`,
  result catastrophic; does not satisfy Deployable gate 7.

## Backtest Assessment
Vendor cites strong backtests; no public real-tick/cost/OOS detail credited. Irrelevant to the verdict — the
**real** signal is the binding evidence and it is decisively negative.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A — PASS (with a strong red flag).** No *confidently-inferable* banned core mechanism: vendor
  markets H1 scalping with a hard SL and "No Martingale," and the trade cadence (369 trades / 74 wk ≈ 5/wk)
  is **not** HFT/tick-scalping. **But** the 79% win + 52.63% DD + configurable-multi-position profile is
  consistent with undisclosed grid/recovery — flagged, not strong enough to Exclude. The verified DD drives
  the Avoid regardless of the exact mechanism.
- **Gate B — TRIGGERED (black box).** Closed source, no third-party teardown → Compliance ≤ 5, Risk ≤ 4,
  verdict ≤ Watchlist. Vendor-documented SL → not auto-Avoided by criterion 3 (the DD does the Avoiding).
- **Gate C — per-firm legality:** not prohibited at all primaries (scalper, no martingale claimed, not HFT).

## Per-Firm Legality Verdict

| Firm | Verdict | Rulebook | Reason |
|------|:-------:|:--------:|--------|
| FundedNext | ⚠️ Conditional | v1 (PROVISIONAL — primary 503 ×7 runs) | Mechanism plausibly permitted; rests on a stale/unconfirmed rulebook → cannot exceed Conditional |
| Funding Pips | ✅ Permitted | v1 | Third-party EA usable only as trade/risk manager; an H1 non-martingale scalper is within policy on mechanism (compliance is moot — DD makes it unusable) |
| The 5%ers | ✅ Permitted | v1 (re-confirmed 2026-06-29) | Mechanism clean (not tick-scalp/HFT/arbitrage/emulator) |
| The Funded Trader | ✅ Permitted | v1 (re-confirmed 2026-06-29) | No prohibited-automation trigger on mechanism |
| Alpha Capital *(ref)* | ⛔ Prohibited | v1 | Closed-source commercial EA can't meet source-code submission (non-gating) |
| Goat Funded Trader *(ref)* | ⛔ Prohibited | v1 | Bans commercial challenge EAs (non-gating) |

**Standing compliance risk (not a prohibition):** a widely-sold commercial EA run identically by many buyers
can trip shared-strategy / copy-trade detection.

## Rule-Violation Flags
- **Drawdown breach (verified):** real max DD **52.63%** ≈ 5× a 10% overall limit and far beyond any
  primary's daily DD — a near-certain limit violation on any prop account.
- **Undisclosed tail risk:** vendor warns "a large drawdown may occur again" while marketing a hard SL.
- **Possible undisclosed recovery/grid:** configurable max-simultaneous-positions + high-win/deep-DD profile.

## Mechanical Rule-Respect
Hard per-trade SL **vendor-documented** but **contradicted in effect** by the 52.63% real DD; no documented
account-level daily-loss stop. → control-evidence ceiling: claimed-but-contradicted → Risk latent low; Gate B
caps Risk ≤ 4 (lowest applies).

## Community Sentiment
MQL5: 4.61/5 over 98 reviews — vendor-platform, not independent, and polarized (some report doubling capital,
others "no trades for weeks" and large drawdowns; one cites "28% DD after 4 months"). A myfxbook discussion
thread and disputed "accounts manipulated/deleted" reports exist (page 403'd the fetch tool). Affiliate/
group-buy listings (forexroboteasy, eafxstore) flagged, not credited. **Negative-case search ran** and
corroborates the large-DD risk.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a high-win-rate scalper that books many small gains and occasionally
   takes a very large adverse excursion — a profile that looks great on a $100/1:500 account (625% gain) but
   whose **52.63% realized drawdown** is fatal under prop DD limits. The edge, if real, is inseparable from
   the tail.
2. **Prop-server case:** wider prop spreads/commissions on EURUSD/GBPUSD scalps erode a scalping edge first,
   and the firm's static 10% max-DD (5%ers) / daily 5% caps would have been breached many times over by the
   realized equity path — the strategy never operated within those constraints.
3. **Variance case:** a high win rate can pass a calm evaluation phase, then the recurring large drawdown
   (vendor-acknowledged) blows the funded account — the textbook pass-but-don't-survive failure.
4. **Evidence fragility:** the credited evidence is **real and long** (Tier 2A, 74 weeks) — and that is
   exactly why this is an Avoid rather than a Watchlist: the record does not merely *fail to prove* survival,
   it *proves* a prop-incompatible drawdown. The one piece that could change the verdict — a properly-
   capitalized, ≥6-month real account holding max DD under ~6% — does not exist and is contradicted by what does.

## Scores
*latent × multiplier (or ceiling) = adjusted. best_tier **TIER2A** → Multiplier A 0.45, Multiplier B 0.60;
ROR **ESTIMABLE/Low** → no Survival cap; Gate B → Compliance ≤ 5, Risk ≤ 4.*

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 2 | ×0.45 (Tier 2; ROR-Low) | **1** | 0.30 |
| Prop-Firm Compliance | 20% | 7 | Gate-B min(7, 5) | **5** | 1.00 |
| Risk Management | 15% | 2 | min(2, Gate-B 4) | **2** | 0.30 |
| Challenge-Passing | 15% | 3 | ×0.45 | **1** | 0.15 |
| Consistency | 10% | 1 | ×0.60 | **1** | 0.10 |
| Transparency | 5% | 4 | ×0.60 | **2** | 0.10 |
| Profitability | 5% | 4 | ×0.60 | **2** | 0.10 |
| **Overall** | | | | | **2.1** |

*Band: **poor** (<4.0). Overall = 0.30·1 + 0.20·5 + 0.15·2 + 0.15·1 + 0.10·1 + 0.05·2 + 0.05·2 = 2.05 → 2.1.*

## Deployment Verdict
⛔ **AVOID.** Binding criterion: **verified real-money max drawdown 52.63%** (the vendor's own ~74-week MQL5
signal) ≈ **5× the tightest primary's 10% max-overall-DD limit**, with the vendor warning a large drawdown
may recur — **prop-incompatible despite a long real track.** A Tier-2A record normally lands on Watchlist as
a candidate for more evidence, but here the record itself is disqualifying (not merely unproven), so the
honest verdict is Avoid. Fails Deployable gates 2, 3, 4, 7, 8. *(Documented deviation from the
Tier-2A→Watchlist default: Watchlist is for promising-but-unproven records; a real record proving a 52% DD is
an Avoid — HARD RULE 6, worse reading.)*

## Similar EAs
Same vendor's risk signature as the companion **Dark Nova 3 Pairs** signal (+953% / 39% DD) — high win rate,
deep drawdown. Mechanism-adjacent to other closed-source scalpers in the archive; distinct from the XAUUSD
breakout cluster (gold-prop-firm-robot, xau-master).

## Red Flags
- **52.63% verified real-money DD** — disqualifying for any prop firm; vendor warns it may recur.
- Hard-SL / "No Martingale" marketing **contradicted** by the realized DD; configurable multi-positions hint
  at undisclosed recovery/grid.
- $100 deposit @ 1:500 — headline 625% gain is non-representative casino-leverage growth.
- Closed source → Gate B; commercial EA → shared-strategy detection risk; Alpha/Goat barred.

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer
**Marco Solito** (MQL5 user `msolito59`) — identifiable, accountable, high-reputation vendor with 45+
published products (the "Dark" series: Dark Venus 100k+ downloads, Dark Gold, Dark Titan, Dark Nova). Named
vendor is a positive; the risk signature across his signals (high win, deep DD) is the concern.

## MT5 Compatibility & Dependencies
MT5 (product 92403) / MT4 (92404); EURUSD + GBPUSD; H1; recommended deposit $1,000 @ 1:20 (vendor) — the live
signal instead runs $100 @ 1:500 (far more aggressive than the recommendation).

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable from public data.** The only real reference is a $100/1:500 account with a 52.63% DD;
de-risking to fit a 10% prop limit is unmodeled and the edge appears inseparable from the tail.

## Cost & Licensing
$399 (MQL5; next price $499). Also redistributed via group-buy/cracked sites (Tier-4, malware caveat).

## Source Links
- https://www.mql5.com/en/signals/2312403 — 2026-06-29 — MQL5 live signal (REAL, Headway; Tier 2A; 52.63% DD) — vendor-hosted/platform-recorded
- https://www.mql5.com/en/market/product/92403 — 2026-06-29 — MQL5 vendor listing (mechanism, hard-SL/no-martingale claim, 98 reviews/4.61) — vendor
- https://www.mql5.com/en/users/msolito59/seller — 2026-06-29 — seller profile (Dark Nova companion signal; product/reputation) — vendor
- WebSearch negative-case (scam/blown/martingale) — 2026-06-29 — "28% DD after 4 months", "no trades for weeks", disputed "accounts deleted"; myfxbook discussion 403'd
- https://www.myfxbook.com/members/DarkEAs/dark-algo-ea-mt5-37174857/11536788 — 2026-06-29 — HTTP 403 (not inspected)

## Analyst Notes
- **FACTS:** fetched MQL5 signal 2312403 — REAL Headway, $100, +625.22%, **52.63% max equity DD**, 369
  trades, 79.67% win, PF 3.44, since 2025-05-30 (~74 wk), 1:500; vendor warns large DD may recur. Vendor
  Marco Solito; mechanism EURUSD/GBPUSD H1 scalping, hard SL + no-martingale claim, configurable max positions.
- **ANALYSIS:** real-money inspectable → Tier 2A; ROR estimable ROR-Low and catastrophic; clean-enough
  mechanism → Gate A pass (grid-suspicion flagged); closed source → Gate B; the verified 52.63% DD is
  prop-disqualifying → Avoid, Overall 2.1.
- **ASSUMPTIONS (flagged):** the public signal reflects purchasable default settings (Medium confidence); the
  "no martingale / hard SL" marketing may mask hold-the-loser/grid behaviour (Low-confidence suspicion).

## Future Research Needed
- If ever reconsidered: obtain a **properly-capitalized (non-$100/1:500), ≥6-month** real account and an
  independent settings teardown confirming whether a recovery/grid mode exists. Absent that, the 52.63% DD
  already settles it.

</details>

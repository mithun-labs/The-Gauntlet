# One Man Army (MT5)

## Overview
Multi-currency (17-pair) M15 reversal/correction **scalper using pending limit orders**, sold on the
MQL5 Market as both a personal and prop-firm system. Vendor explicitly markets it as **non-martingale,
non-grid, single-trade-per-pair, with a hard Stop Loss on every trade**. Distinguishing feature versus
the rest of the archive: the vendor runs a **public, real-money MQL5 live signal (~9 months / 41 weeks)**
that is inspectable, making this the **first archived EA whose headline return+DD pair rests on a
real-money trade-level record (Tier 2A)** rather than screenshots or vendor curves.

## Vendor / Developer
**Ihor Otkydach** (MQL5 seller profile `fibomen2`, listed Slovakia, MQL5 rating ~30,750 — a prolific,
**identifiable and accountable** high-reputation seller). Runs a **stable of $999/month copy signals**
(One Man Army M15, "Scalper Investor M15 Reverse", "Swing Master Incubator", "Double Shot") — i.e. a
signal-selling operation, which raises a **survivorship concern** (many launched signals; only winners
get marketed). Price **$599** one-time on MQL5 (group-buy/cracked copies circulate ~$239 — discovery
noise, not evidence).

## MT5 Compatibility & Dependencies
MT5 only. 17 major FX pairs, M15. Min recommended deposit **$500**; live signal runs **1:500 leverage**
on a small ($1,000) real account. Hedging-account behavior not documented as required (single trade per
pair). No public VPS/broker constraint beyond standard.

## Strategy Mechanism
Publicly **vendor-described** (not code-verified, no third-party teardown): scalps short/medium-term
**corrections and reversals**, entering via **pending limit orders at reversal zones**, one position per
pair, each with a **dynamically-calculated hard SL**. Vendor states "**No Martingale, no averaging … no
grid trading, no double-ups**." **Gate B status: black box** (closed source, marketing-level logic only),
but with a **vendor-documented hard control (per-trade SL)** that is *corroborated* — not proven — by the
real signal's **contained 8.94% max equity DD over 567 trades / 41 weeks** (a martingale/grid would be
expected to show a deeper drawdown or a smooth-then-cliff curve; this does not).

## Mechanism Inference Confidence
**Medium.** The non-martingale/SL claim is consistent with the real-money equity behaviour (PF 1.63,
max DD 8.94%, no cliff over 9 months), but the source is closed and unaudited, so a hidden order-stacking
or wide-SL mean-reversion tail cannot be ruled out. A **90% win rate with PF 1.63 implies avg loss ≈ 5.5×
avg win** — a high-win-rate / fat-left-tail mean-reversion profile, fragile to trend/news days across 17
correlated pairs.

## Recommended Instruments
17 major FX pairs (EURCAD cited for testing). No XAUUSD/indices headline.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD: +43.03% gain, **8.94% max equity DD**, 567 trades, 89.94% win, PF 1.63, real account, $1,000 deposit, started 2025-09-18 (~41 wk) | https://www.mql5.com/en/signals/2332504 | MQL5 live signal (real account, broker CapitalPointTrading-MT5-4) | vendor-hosted but platform-recorded real-money trade history | **TIER2A** | 2026-06-23 | Medium | Real-money, ~9mo, public trade history → Tier 2A; demoted from Tier 1 by **low deposit ($1,000)** + single-account small sample. MQL5 equity-DD method ≠ firm DD rule (DD-definition mismatch). |
| Mechanism / risk controls: no martingale/grid/averaging, single trade per pair, hard SL each trade | https://www.mql5.com/en/market/product/152522 | MQL5 vendor listing | vendor | TIER3 (claim) | 2026-06-23 | Medium | Marketing-level; corroborated (not proven) by contained real DD. |
| Backtest "23,322% (2018–2025)" | cheaperforex.com / eafxstore (affiliate) | affiliate review | affiliate | TIER4 | 2026-06-23 | Low | Fantasy/curve-fit number; discredited, not credited. |
| Prop-firm success ("passed FTMO", "97.3% win") | cheaperforex.com | affiliate review | affiliate | TIER4 | 2026-06-23 | Low | No Tier-0 funded proof → Tier 4 per HARD RULE 5. |
| Negative-case evidence | WebSearch ("scam/blown/losing/forexfactory/reddit") | search | independent | n/a | 2026-06-23 | Medium | **No public blown-account/scam reports surfaced** (recorded as a no-hit, not as exoneration). |

## Source Reliability Assessment
source_count **6** · independent_source_count **2** (MQL5 signal page recorded platform data; negative-case
search) · affiliate_source_count **3** (cheaperforex, eafxstore, bestforexeas/listicles). **Best evidence
found:** the **fetched real-money MQL5 live signal** — a genuine inspectable trade-level record (Tier 2A),
the strongest *positive* evidence in the archive to date.

## Unverified Claims
- "Passed FTMO challenges" / "97.3% win rate" / "23,322% backtest" — **Tier 4**, vendor/affiliate only.
- All performance beyond the single $1,000 live signal (no second account, no funded statement, no
  independent Myfxbook). Risk-control behaviour under news/trend shock — **not observed** in the record.

## Eligibility Gates
- **Gate A — PASS (not excluded).** No banned core mechanism by claim or by the real equity signature
  (contained DD, no cliff). 90% win rate is a watch-flag, not a martingale proof; SL-on-every-trade and
  the bounded real DD argue against grid/martingale. Mechanism inference Medium.
- **Gate B — TRIGGERED (black box).** Closed source, no independent teardown → ceilings apply:
  **Compliance ≤ 5, Risk ≤ 4, verdict ≤ Watchlist.** NOT auto-Avoided (it carries a vendor-documented
  hard SL → Avoid criterion 3 does not fire).
- **Gate C — per-firm legality:** not prohibited at all primaries (see below).

## Per-Firm Legality Verdict
- **FundedNext — Conditional (v1, PROVISIONAL rulebook, primary 503 x5 runs).** EA-permissive; non-grid
  SL scalper fine in principle, but legality rests on an unconfirmed/stale rulebook → cannot exceed
  Conditional, cannot support Deployable.
- **Funding Pips — Permitted (v1).** Mechanism (non-martingale/grid, low frequency ~14 trades/wk total →
  not HFT/tick-scalping) is within policy.
- **The 5%ers — Permitted (v1).** Same; mechanism clean.
- **The Funded Trader — Permitted (v1).** Same.
- **Reference (non-gating):** Alpha Capital **Prohibited** (closed-source commercial EA can't meet
  source-code submission); Goat Funded Trader **Prohibited** (bans commercial challenge EAs).
- **Standing compliance risk (not a prohibition):** a widely-sold commercial EA run identically by many
  buyers can trip **shared-strategy / copy-trading / strategy-uniqueness** detection at several firms.

## Rule-Violation Flags
- **Drawdown headroom:** real max DD **8.94%** ≈ 89% of a 10% overall limit (MQL5 equity method; restate
  caveat) — **fails Deployable gate 4** (needs ≤60% of the limit) and is the central survival risk.
- **Daily-DD exposure:** 17 correlated reversal positions can cluster losses intraday → possible breach
  of a ~5% daily-DD rule on a trend/news day (no intraday data to confirm — indicative).

## Mechanical Rule-Respect
Hard per-trade SL **vendor-documented** and consistent with the real DD curve; **not** independently
demonstrated (no teardown), and **no** documented account-level daily-loss stop or max-position governor
beyond "one per pair." → Risk control-evidence ceiling: **vendor-documented → Risk ≤ 5** (Gate B already
caps Risk ≤ 4; lowest applies).

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | ~4%/mo (43.03% over ~9 mo, real) | TIER2A | mql5.com/en/signals/2332504 |
| Maximum Drawdown | 8.94% (equity, MQL5 method) | TIER2A | mql5.com/en/signals/2332504 |
| Win Rate | 89.94% (567 trades) | TIER2A | mql5.com/en/signals/2332504 |
| Profit Factor | 1.63 | TIER2A | mql5.com/en/signals/2332504 |
| Track Length | ~41 weeks (since 2025-09-18) | TIER2A | mql5.com/en/signals/2332504 |
| Real vs Demo | **Real** ($1,000 deposit, 1:500, CapitalPointTrading) | TIER2A | mql5.com/en/signals/2332504 |
| Backtest "23,322%" | NOT CREDITED | TIER4 | affiliate |

## Backtest Assessment
Vendor/affiliate "23,322% 2018–2025" is a **near-worthless curve-fit headline** (no stated real-tick/cost
modelling, no OOS/walk-forward visible, magnitude implausible). The **only** evidence credited is the live
signal.

## Risk-of-Ruin Analysis
**ESTIMABLE — ROR-Low** (rests on Tier 2A real-money trade-level history; directional only).
- **Method:** directional read of the live account's realized distribution (567 real trades, win 89.94%,
  PF 1.63, max equity DD 8.94%); no Monte-Carlo resample performed beyond order-of-magnitude reasoning.
- **P(violating overall DD, ~10%):** **meaningful / non-trivial.** Historical max DD 8.94% already sits at
  ~89% of a 10% static limit over a *calm* 9-month window; historical max understates future, and no shock
  regime was observed → over a multi-month funded period a 10% trailing/overall breach is a real risk.
- **P(violating daily DD, ~5%):** **possible but unquantified** — 17 correlated reversal trades can cluster;
  no intraday data. Flag.
- **ROR 30/90/365d (full ruin):** low-ish for *total* account loss given SL discipline, but **prop-"ruin"
  (limit breach) is materially higher** than nominal ruin and is the operative risk.
- **Caveats (mandatory):** (1) **autocorrelation** across 17 pairs and reversal entries → lumpy losses,
  true ROR understated by an independence assumption; (2) **deposit-scaling** — a $1,000 / 1:500 record
  restated to 50k/100k/200k at firm leverage (often 1:30–1:100) changes sizing and behaviour; (3)
  **DD-definition mismatch** — MQL5 equity DD ≠ any firm's daily/overall rule; (4) **no shock observed** in
  the window. → `ror_confidence: Low`; does **not** satisfy Deployable gate 7 (needs Tier 0/1 ROR-High).

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable from public data for a funded account.** The only sizing reference is a $1,000/1:500
account; restating per-trade risk to firm leverage and DD rules is an assumption, not a measurement.
Any deployment would need to cut size hard to keep worst-case clustered DD well under the firm's daily
and overall limits — and even then the 8.94% historical DD leaves too little headroom.

## Cost & Licensing
$599 one-time (MQL5); copy-signal $999/mo. Group-buy/cracked copies (~$239) are discovery noise only.

## Community Sentiment
25 MQL5 reviews, 4.74/5 (vendor-platform, not independent community). Independent forum/Reddit discussion
is thin; **negative-case search returned no blown-account/scam reports** (recorded as a no-hit). Affiliate
"reviews" (cheaperforex, eafxstore, bestforexeas) are funnels — flagged, not credited.

## Why This Will Probably Fail
1. **Most likely benign explanation:** a genuine non-martingale reversal scalper whose **edge is fragile**
   — 90% win rate / PF 1.63 means rare large losses, and 9 calm months on one tiny account may simply not
   have met the trend/news regime that produces the fat-tail cluster across 17 correlated pairs.
2. **Prop-server case:** the firm's own **trailing/static DD calc**, wider prop spreads/commissions, and
   lower leverage could erase the thin scalping edge and trip a 10% overall (already ~89% used) or a 5%
   daily limit on a correlated-loss day the vendor's broker never imposed.
3. **Variance case:** it could pass an evaluation in a calm month and then breach the funded account on
   the first shock — passing and surviving are different problems, and the survival evidence is absent.
4. **Evidence fragility:** everything credited rests on **one $1,000 vendor-hosted signal**. The single
   piece that would most change the verdict — a ≥6-month, properly-capitalized, independently verified
   (or funded-account) record with DD headroom — **does not exist publicly.**

## Scores
latent × multiplier(/ceiling) = adjusted (best_tier **TIER2A** → Multiplier A 0.45, Multiplier B 0.60;
ROR **ESTIMABLE/Low** → no 0.20 Survival cap; Gate B → Compliance ≤5, Risk ≤4):
- **Funded-Survival:** latent 5 × 0.45 = 2.25 → **2**
- **Prop-Firm Compliance:** latent 7 → min(7, Gate-B 5) = **5**
- **Risk Management:** latent 5 → min(5, Gate-B 4, ctrl-evidence 5) = **4**
- **Challenge-Passing:** latent 5 × 0.45 = 2.25 → **2**
- **Consistency:** latent 5 × 0.60 = 3.0 → **3**
- **Transparency:** latent 5 × 0.60 = 3.0 → **3**
- **Profitability:** latent 5 × 0.60 = 3.0 → **3**

**Overall** = 0.30·2 + 0.20·5 + 0.15·4 + 0.15·2 + 0.10·3 + 0.05·3 + 0.05·3
= 0.60 + 1.00 + 0.60 + 0.30 + 0.30 + 0.15 + 0.15 = **3.10 (poor band)**.

## Deployment Verdict
**WATCHLIST.** Binding criterion: **real-money but caveated (Tier 2A) — single small $1,000 vendor-hosted
account; 8.94% max DD leaves insufficient headroom vs prop limits; lacks an adequately-capitalized
≥6-month independently-verified record and any funded-account evidence.** Fails Deployable gates 2, 3, 4,
7, 8. ROR is estimable only at **ROR-Low**. This is the **first archive entry to clear the Tier-2A/Watchlist
bar** — a candidate to chase real evidence on, not a recommendation.

## Similar EAs
Otkydach's own stablemates ("Scalper Investor M15 Reverse", "Swing Master Incubator", "Double Shot") are
likely mechanism-adjacent reversal/scalping signals — cross-watch for survivorship. Distinct mechanism
from the archive's gold EAs (XAU Master, Mad Turtle, Gold Reaper).

## Red Flags
- 90% win rate / PF 1.63 → fat-left-tail mean-reversion (small wins, rare big losses).
- 8.94% real DD ≈ 89% of a 10% prop limit on a *calm* window → no headroom.
- Signal-selling operation with many $999/mo signals → survivorship-marketing risk.
- Curve-fit "23,322%" backtest in affiliate marketing.
- Closed source → Gate B; commercial EA → shared-strategy/copy-trade detection risk; Alpha/Goat barred.

## Source Links
- https://www.mql5.com/en/market/product/152522 — 2026-06-23 — MQL5 vendor listing — affiliate(vendor)
- https://www.mql5.com/en/signals/2332504 — 2026-06-23 — MQL5 live signal (real-money, Tier 2A evidence) — vendor-hosted/platform-recorded
- https://www.mql5.com/en/users/fibomen2/seller — 2026-06-23 — vendor profile (rep, other signals) — vendor
- https://cheaperforex.com/one-man-army-ea-mt5-review/ — 2026-06-23 — affiliate review (97.3%/backtest claims) — affiliate
- https://eafxstore.com/product/one-man-army-ea-mt5/ — 2026-06-23 — group-buy listing (discovery noise) — affiliate
- WebSearch negative-case (scam/blown/losing) — 2026-06-23 — no public hits recorded

## Analyst Notes
- **FACTS:** real-money MQL5 signal — +43.03% gain, 8.94% max equity DD, 567 trades, 89.94% win, PF 1.63,
  $1,000 deposit, 1:500, broker CapitalPointTrading, started 2025-09-18 (~41 wk). Vendor: non-martingale/
  grid, SL each trade. 25 MQL5 reviews 4.74/5. Affiliate backtest 23,322% and "passed FTMO" claims.
- **ANALYSIS:** real-money inspectable record → Tier 2A; ROR estimable at ROR-Low; non-martingale
  consistent with contained DD → Gate A pass; closed source → Gate B (Watchlist ceiling); DD headroom and
  fragile high-win-rate edge are the survival risks. Net = **Watchlist** (first in archive), Overall 3.1.
- **ASSUMPTIONS (flagged):** mechanism is as vendor-described (Medium confidence; unaudited); the calm
  9-month window has not yet sampled a shock; deposit-scaling to funded sizing is an assumption.

## Future Research Needed
- Operator to inspect the **trade-by-trade** signal history (login) to confirm no order-stacking and to
  measure intraday/daily DD; obtain a **second, larger, longer** real-money or funded-account record with
  DD headroom (the only path off Watchlist). Watch the vendor's other signals for survivorship.

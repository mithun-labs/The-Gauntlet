# Happy Gold EA (MT5)

## Overview
Commercial, closed-source MT5 Expert Advisor for **XAUUSD** marketed for retail and prop-firm use, sold via ForexStore and the HappyForex / "forexfunny" vendor ecosystem (€489, discounted from €699; min deposit $100). Marketed as a single-trade gold scalper with a hard stop loss and no martingale/grid. This run could **not** inspect any trade-level record (Myfxbook 403), so all performance figures are vendor-displayed widgets or affiliate-review observations.

## Vendor / Developer
HappyForex ecosystem (sold through ForexStore; also distributed via "forexfunny" Gumroad and numerous cracked/nulled sites — eafxstore, cheapforexea, ecomforex — "FREE DOWNLOAD" listings, a piracy signal not an evidence signal). The HappyForex brand has a long ForexPeaceArmy review history including **refund-denial complaints after blown accounts** (10-in-1 pack). Vendor is brand-identifiable but the specific developer is not clearly accountable. **Mild red flag** (refund-dispute history; heavy cracked-site distribution).

## MT5 Compatibility & Dependencies
XAUUSD only; M15 / M30 / H1 / H4. Uses pending stop orders. Independent test reports results are **dramatically broker- and latency-dependent** (profitable on Eightcap, losing on BlackBull Markets; a single trade made "$207 on 0.16 lots vs $32 on 0.54 lots" depending on VPS latency) — implies a low-latency ECN/raw-spread broker + fast VPS are effectively required.

## Strategy Mechanism
**Publicly inferable:** pending **buy-stop orders above recent highs** (breakout-scalp via modified ZigZag), **one open trade at a time**, **hard stop loss** (vendor: −24 pips; affiliate test observed ~$2.40 SL with $10 TP, ~1:4 R:R), trailing stop + break-even. **No grid/martingale/averaging observed** in independent testing — each trade independent → **survives Gate A**. Vendor strategy descriptor is literally "scalp/swing/**gridnews**" and a separate **"GridNews" variant** exists; the news component and the GridNews mode are a standing risk but are not the assessed standard single-trade configuration.

## Mechanism Inference Confidence
**Medium.** Multiple independent observations agree on single-trade + hard-SL pending-order scalping; but hold-time / trades-per-day are unconfirmed (tick-scalping/HFT cannot be ruled in or out without trade-level data), and the "gridnews"/news element is undocumented in behavior.

## Recommended Instruments
XAUUSD (gold) only.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD (17,474% gain / 8.81% monthly / 25.95% max DD / 1,837 live days) | https://forexstore.com/happy-gold | vendor | vendor | TIER3 | 2026-06-19 | Low | Vendor-displayed Myfxbook widgets (2 real, 2 demo); underlying Myfxbook page 403'd — uninspectable |
| Mechanism / risk controls (1 trade, hard SL, no grid/martingale) | https://forexstore.com/happy-gold ; https://algotradingspace.com/happy-gold-ea-review | vendor + independent(affiliate) | vendor + affiliate | TIER3 | 2026-06-19 | Medium | Affiliate review corroborates single-trade hard-SL pending orders; observed broker/latency dependence |
| Prop-firm success claim ("prop firm ready"; challenge results) | https://algotradingspace.com/happy-gold-ea-review | affiliate | affiliate | TIER4 | 2026-06-19 | Low | "4.6% in 8 days" 50K challenge (8-day sample); BlackBull account losing — no Tier-0 funded proof |
| Negative-case evidence (blown accounts, refund denied, failure to exit on news, low expected payoff) | https://www.forexpeacearmy.com/forex-reviews/7513/www.happyforex.de ; FF threads 880663/903107 (snippets) | forum/review | independent | TIER3 | 2026-06-19 | Medium | FPA: refund denied after blown account; user: "crashed... didn't exit some trades which lost a lot on 3-4 days"; "Happy Gold v2 = expected payoff 0.5 max" |

## Source Reliability Assessment
- source_count: **6** (2 web searches surfacing FPA/FF/myfxbook-forum snippets, vendor ForexStore page, affiliate independent review, plus Myfxbook + ForexFactory fetch attempts that 403'd).
- independent_source_count: **2** (ForexPeaceArmy review history + ForexFactory user reports, via search snippets; trade-level pages uninspectable).
- affiliate_source_count: **2** (algotradingspace affiliate review; bestforexeas/eatested affiliate-style reviews surfaced).
- **Best evidence found:** Tier 3 — vendor-displayed Myfxbook widgets (claimed verified real accounts, ~5-year history) that could **not** be inspected (403). No inspectable evidence above Tier 3.

## Unverified Claims
- All performance numbers (17,474% gain, 8.81%/mo, 25.95% max DD, 1,837 live days) — vendor widgets, uninspectable.
- "Verified by Myfxbook and FXBlue" — unverifiable firsthand (403).
- "Prop firm ready" / challenge-passing — no Tier-0 funded evidence.
- "No martingale / no grid" — corroborated by an affiliate review but not by inspectable trade history; the "gridnews"/news component behavior is undocumented.
- Hold time / trades-per-day (HFT/tick-scalping status) — unknown.

## Eligibility Gates
- **Gate A — PASS (survives).** Core mechanism is single-trade pending-order breakout-scalp with a hard per-trade stop; no grid/martingale/averaging observed in independent testing. (Risk flags: latency-sensitive scalping and an optional "GridNews"/news mode that, if used, would raise news-straddle/grid concerns — but the assessed standard config is not banned.)
- **Gate B — mechanism publicly inferable (Medium).** Not a black box → no Gate-B ceiling applied.
- **Gate C — per-firm:** see below. Not Prohibited at all primary firms → not an automatic Gate-C Avoid, but Conditional across the board.

## Per-Firm Legality Verdict
- **FundedNext — Conditional (rulebook v1, SECONDARY/UNCONFIRMED).** EAs/automation reported allowed; scalping not banned per se, but the FundedNext rulebook is provisional (primary site 503) → Conditional.
- **Funding Pips — Conditional (rulebook v1).** Mechanism legal, but a fully-automated **third-party commercial** EA is barred on standard evaluations (allowed as trade/risk manager only) → Conditional/effectively Prohibited on standard programs.
- **The 5%ers — Conditional (rulebook v1).** EAs allowed, but standards bar "shared third-party EA strategies" and require controlling the EA's internal logic (hostile to a closed-source commercial EA); **tick-scalping is banned** and hold-time is unconfirmed → Conditional.
- **The Funded Trader — Conditional (rulebook v1).** Commercial pre-programmed EAs restricted / must have unique non-masked parameters → Conditional (depends on UNCONFIRMED commercial-EA detail).

## Rule-Violation Flags
- Claimed/displayed **25.95% max drawdown** dwarfs every primary firm's ~10% max-overall-DD limit at the settings that produced the record (DD-definition mismatch caveat applies, but a 26% gap dwarfs reconciliation).
- Closed-source commercial third-party EA conflicts with Funding Pips standard-program EA policy and The 5%ers "control your logic"/no-shared-EA standard.
- Possible tick-scalping/HFT exposure at The 5%ers (hold-time unconfirmed) — flagged, not established.
- Broker/latency-dependent edge: results that flip between brokers signal the edge may not survive a prop firm's server/feed/spread (Steelman prop-server case).

## Mechanical Rule-Respect
Hard per-trade stop loss is **vendor-documented and observed in an affiliate test** (≈$2.40 / 24 pips). **No** documented hard equity-stop or daily-loss-stop. Independent reports of the EA **failing to exit trades and losing heavily over 3–4 days** undercut confidence that the per-trade stop reliably bounds risk in volatile/news conditions.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | 8.81% (vendor-displayed) | TIER3 | forexstore.com/happy-gold |
| Maximum Drawdown | 25.95% (vendor-displayed); separate live claim 25.95% over 243d (+3,839%) | TIER3 | forexstore.com / search |
| Win Rate | ~30–40% (affiliate review, approximate) | TIER4 | algotradingspace |
| Profit Factor | NOT REPORTED (one forum user: "expected payoff 0.5 max" on long Dukascopy test) | TIER3 | search/FF snippet |
| Track Length | claimed 1,837 live days (~5 yr) — uninspectable | TIER3 | forexstore.com |
| Real vs Demo | claimed 2 real + 2 demo Myfxbook accounts — uninspectable | TIER3 | forexstore.com |

## Backtest Assessment
Vendor cites "99.90% optimization accuracy" backtesting — a near-meaningless marketing figure (curve-fit tell), not a multi-regime real-tick walk-forward report. No public OOS/walk-forward, cost/slippage modeling, or shock-regime testing is inspectable. Near-worthless as evidence; the broker/latency dependence observed live further undermines any backtest's transferability.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No inspectable Tier 0/1 trade-level history (Myfxbook 403). ROR, daily-DD violation probability, and max-DD violation probability cannot be computed from vendor widgets, affiliate observations, or backtests. Indicatively, a claimed ~26% max DD and reported multi-day losing streaks are incompatible with ~10% firm max-DD and ~5% daily-DD limits at the displayed settings — but this is indicative only (DD-definition mismatch).

## Recommended Risk Settings
**Non-actionable.** Public data does not support a defensible 50k/100k/200k sizing; the edge is broker/latency-dependent and no inspectable trade distribution exists.

## Cost & Licensing
€489 (from €699); 2- or 5-license tiers; 30-day money-back guarantee advertised — but the vendor brand has documented refund-denial complaints (ForexPeaceArmy). Heavy cracked/nulled distribution.

## Community Sentiment
Mixed-to-negative on the independent side: ForexPeaceArmy refund-denial-after-blowup history for the HappyForex brand; a user reporting the EA "crashed a few times and didn't exit some trades which lost a lot on 3–4 days"; another citing very low expected payoff (~0.5) on long historical ticks. Positive coverage is concentrated in affiliate review sites (commission links, VIP-club upsells) — discounted accordingly.

## Why This Will Probably Fail
1. **Most likely benign explanation:** the gaudy multi-thousand-percent vendor curve is the survivor of compounding on a latency-favorable broker/VPS; the realistic per-trade expectancy is small/marginal ("expected payoff 0.5"), and the displayed equity is not inspectable.
2. **Prop-server case:** the edge demonstrably flips between brokers (Eightcap profit vs BlackBull loss) and scales with VPS latency — a prop firm's own server/feed/spread/commission would very plausibly erase it or trip the daily/max-DD limit the vendor never tested.
3. **Variance case:** a tight-SL gold scalper can clear an 8-day challenge on luck and then surrender it to a single volatile/news session — exactly the "passes then blows the funded account" failure, consistent with reported 3–4 day loss clusters.
4. **Evidence fragility:** essentially everything rests on Tier 3/4 (uninspectable widgets + affiliate reviews). The single piece that would most change the verdict — an inspectable ≥6-month verified real-money Myfxbook/FXBlue trade-level history at default prop settings — I do **not** have (403).

## Scores
Evidence tier governing multiplied dimensions: **TIER3**. ROR **NON-ESTIMABLE** → Survival multiplier = min(A=0.25, 0.20) = **0.20**. Mechanism inferable → no Gate-B ceiling. Risk control-evidence: vendor-documented + weak affiliate observation → Risk ≤ 5.

| Dimension | Latent | × Multiplier / Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival (30%) | 2 | × 0.20 (ROR cap) = 0.4 → clamp | **1** |
| Prop-Firm Compliance (20%) | 3 | not multiplied (Conditional all firms) | **3** |
| Risk Management (15%) | 4 | min(4, ceiling 5) | **4** |
| Challenge-Passing (15%) | 4 | × 0.25 (A, Tier3) = 1.0 | **1** |
| Consistency (10%) | 3 | × 0.30 (B, Tier3) = 0.9 → clamp | **1** |
| Transparency (5%) | 3 | × 0.30 (B, Tier3) = 0.9 → clamp | **1** |
| Profitability (5%) | 3 | × 0.30 (B, Tier3) = 0.9 → clamp | **1** |

Overall = 0.30·1 + 0.20·3 + 0.15·4 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 0.60 + 0.60 + 0.15 + 0.10 + 0.05 + 0.05 = **1.85 → 1.9 (poor)**.

## Deployment Verdict
**AVOID.** Binding criterion: **headline return+DD evidence is Tier 3 (no independent verification) AND ROR NON-ESTIMABLE with best_tier ≤ TIER2** — a deterministic Avoid trigger. Reinforced by a claimed ~26% max DD that is prop-incompatible, a broker/latency-dependent edge unlikely to survive a prop server, and closed-source commercial-EA policy frictions at all four primary firms.

## Similar EAs
Same family/segment as other gold scalpers; mechanism distinct from [[the-gold-reaper-mt5]] (Profalgo multi-strategy breakout) and from [[quantum-queen-mt5]] (grid). No rebrand match in the index.

## Red Flags
- Performance entirely uninspectable (Myfxbook 403); rests on vendor widgets + affiliate reviews.
- Vendor brand has refund-denial-after-blowup complaints (ForexPeaceArmy).
- Edge is broker/latency-dependent (won't transfer to a prop server reliably).
- "gridnews"/news component + a separate GridNews variant; news behavior undocumented.
- Reports of failure to exit trades during adverse multi-day stretches.
- Heavy cracked/nulled distribution (malware risk on those builds; not used as evidence).

## Source Links
- https://forexstore.com/happy-gold — 2026-06-19 — vendor page (mechanism, perf widgets) — affiliate: vendor
- https://algotradingspace.com/happy-gold-ea-review — 2026-06-19 — independent test review — affiliate: **yes**
- https://www.forexpeacearmy.com/forex-reviews/7513/www.happyforex.de — 2026-06-19 (via search) — brand review history — affiliate: no
- https://www.forexfactory.com/thread/903107-did-someone-try-to-recreate-the-happy-gold — 2026-06-19 — 403 (uninspectable) — affiliate: no
- https://www.myfxbook.com/community/strategies/ea-happy-gold/1035649,2 — 2026-06-19 — 403 (uninspectable) — affiliate: n/a

## Analyst Notes
- **FACTS:** vendor page states single trade, hard SL (24 pips), no martingale/grid, "scalp/swing/gridnews", €489, $100 min, XAUUSD M15–H4, vendor-displayed Myfxbook widgets (8.81%/mo, 25.95% DD, 1,837 days); affiliate test observed pending buy-stops, ~$2.40 SL/$10 TP, broker/latency-dependent results; FPA shows refund-denial-after-blowup history; forum snippet "expected payoff 0.5".
- **ANALYSIS:** mechanism is a latency-sensitive tight-SL gold scalper that survives Gate A but whose edge likely won't survive a prop server; evidence ceiling is Tier 3 because no trade-level record is inspectable.
- **ASSUMPTIONS (flagged):** that hold-time is above tick-scalping thresholds (unconfirmed); that the assessed product is the standard single-trade version, not the GridNews variant.

## Future Research Needed
- If Myfxbook/FXBlue egress is allow-listed, inspect the claimed verified real accounts (trade-level, hold-time, true DD under firm definitions) — could move HFT/tick-scalping question and possibly lift toward Watchlist if a clean ≥6-month real record at prop settings exists.
- Confirm hold-time/trades-per-day vs The 5%ers tick-scalping screen.
- Operator: only Tier-0 funded-account evidence could ever lift this past Watchlist.

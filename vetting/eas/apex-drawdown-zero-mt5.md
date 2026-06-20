# Apex Drawdown Zero (MT5)

## Overview
A closed-source MT5 Expert Advisor marketed as the "best gold trading robot 2026" with a headline **+106% gain at a 0.39% maximum drawdown** (PF 3.56) over a claimed 18-month live track. Sold on the MQL5 Market (~$497, $349 crypto) by a **named developer**, with heavy affiliate-reseller and group-buy distribution. The mechanism is vendor-described as a **session/range-breakout with ATR-based stop loss** — i.e. a *claimed* legal, stop-based strategy — but no source code, independent teardown, or inspectable verified trade-level record exists, and the public performance claims are internally contradictory. This is a **vendor-claimed black box (Gate B)** whose headline return+DD rests entirely on **Tier 3** vendor evidence → **Avoid**.

## Vendor / Developer
**Tshivhidzo Mbedzi** ("MCP Labs", South Africa) — an **identifiable, accountable** MQL5 seller (`mbedzimz1`) with 14+ published EAs and a ~500-member Discord. Accountability is a relative *positive* versus the archive's anonymous-shell vendors (contrast DowGold's "DGHS Trading Inc."). However, the named developer also authors the bulk of the promotional "Traders' Blogs" posts that constitute nearly all of the public evidence, so accountability does not equal independent verification.

## MT5 Compatibility & Dependencies
Publicly documented only: MT5; instruments stated **inconsistently** across vendor posts — **GBPJPY (primary), EURUSD (optional)** in the developer's own MyFxBook-results post, but **XAUUSD/gold** in the gold-listicle posts and reseller pages. Timeframe not consistently specified. "Optimized for live spread environments." Min deposit examples as low as **$600** (the headline account) and "$1,000 monthly growth" set manuals.

## Strategy Mechanism
**Vendor-claimed:** "session-based / range-breakout strategy" using "precise technical indicators" with "**ATR-Based Stop Loss Logic** to calculate precise and adaptive stop levels based on volatility," that "monitors drawdown in real time" and "scales risk intelligently based on account equity." On the claimed description there is **no martingale, grid, or averaging** — a hard, volatility-adaptive stop loss per trade is asserted. **Gate A is therefore NOT triggered** (no banned mechanism is documented or strongly inferable against an explicit SL claim).
**But:** the dedicated MyFxBook-results blog post discloses **no stop-loss methodology at all** and does not specify the mechanism, and there is **no source code, no independent third-party teardown, and no settings/risk-control evidence** beyond marketing copy. The strategy is, in evidence terms, a **black box with a vendor label → Gate B applies.**

## Mechanism Inference Confidence
**Low.** The "session breakout + ATR SL" description is vendor self-marketing, uncorroborated by any independent source or inspectable trade history. A **0.39% max DD on a $600 account alongside +106% total gain and a "$600 → $2,000+ in one week" (+233%/week) flip is internally inconsistent**: a genuine tight-ATR-stop breakout system does not compound 233% in a week, and a near-zero realized drawdown across 18 months most often indicates either (a) **losing positions held rather than stopped** (a recovery/grid signature) or (b) a **cherry-picked / curve-fit window or doctored statement**. I cannot establish which from public evidence — hence Low confidence and a black-box (Gate B) treatment rather than a Gate A exclusion.

## Recommended Instruments
GBPJPY / EURUSD per the developer's results post; XAUUSD per the gold-marketing posts (conflicting).

## Evidence Matrix
| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline +106% gain / 0.39% max DD / PF 3.56 over 18mo | mql5.com/en/blogs/post/768819 | vendor blog | vendor | TIER3 | 2026-06-20 | Low | "publicly verified on MyFxBook" but **direct links absent**; uninspectable |
| Mechanism = session breakout + ATR-based SL, equity-scaled risk | mql5.com/en/blogs/post/768792, /767301 | vendor blog | vendor | TIER4 | 2026-06-20 | Low | marketing description; no code/teardown; contradicts "no SL discussed" results post |
| "$600 → $2,000+ in one week" / "$1,000 live withdrawal proof" | mql5.com/en/blogs/post/768874, /768909 | vendor blog | vendor | TIER4 | 2026-06-20 | Low | screenshot "proof"; +233%/week contradicts 0.39% DD claim |
| Prop-firm suitability (FTMO/FundedNext/The5ers) | reseller + vendor posts | vendor/affiliate | vendor | TIER4 | 2026-06-20 | Low | claim; no funded-account evidence |
| Negative-case evidence | WebSearch (scam/blown/refund/grid/martingale) | search | independent | n/a | 2026-06-20 | — | **no specific blown-account/refund report found** (recent product); also no independent corroboration |

## Source Reliability Assessment
- **source_count: 7** · **independent_source_count: 0** (no inspectable independent source; fxroboteasy aggregator returned HTTP 502; Myfxbook links absent/uninspectable) · **affiliate_source_count: 4** (eafxstore, ecomforex, grizzlytrading/ko-fi group-buys + reseller listicles).
- **Strongest public evidence found:** a named MQL5 developer and an MQL5 Market listing — i.e. *accountability and existence*, **not** performance verification. No evidence above **Tier 3**, and the Tier-3 figures are uninspectable (Myfxbook links not provided).

## Unverified Claims
+106%/0.39%-DD/PF-3.56 headline; "verified on MyFxBook" (no links); "$600→$2,000 in one week"; "$1,000 withdrawal proof"; ATR-stop "extremely strict risk management"; "passes & stays funded" at FTMO/FundedNext/The5ers; 80%+ win rate; "18+ months live." All are vendor-stated and uninspectable.

## Eligibility Gates
- **Gate A (banned core mechanism):** **PASS** (not excluded). Vendor claims a session-breakout with a hard ATR stop loss; no martingale/grid/averaging/HFT mechanism is documented or strongly inferable against that explicit SL claim. The implausible DD is a fraud/cherry-pick *signal*, not proof of a grid, so the strong-inference bar for Gate A is not met.
- **Gate B (mechanism transparency):** **CONSTRAINED — black box.** Closed source, no public logic detail beyond marketing, no third-party teardown, no settings/risk-control evidence, mechanism inference Low. Ceilings applied: **Compliance ≤ 5, Risk ≤ 4, Verdict ceiling = Watchlist.**
- **Gate C (per-firm legality):** not prohibited at all primary firms (mechanism legal on claim); per-firm verdicts below.

## Per-Firm Legality Verdict
- **FundedNext** — **Permitted** (automated EAs allowed; no banned mechanism on the claimed description) · rulebook v1.
- **Funding Pips** — **Conditional** (third-party commercial EA allowed only as a trade/risk manager, not a fully-automated standalone strategy) · rulebook v1.
- **The 5%ers** — **Conditional** (closed-source EA; trader must be able to evidence control of the trading logic) · rulebook v1.
- **The Funded Trader** — **Permitted** (automated EAs allowed; no banned mechanism on claim) · rulebook v1.
- **Alpha Capital (reference)** — **Prohibited** (source-code (.MQ5) submission + pre-approval required; closed-source commercial EA cannot comply) · rulebook v1.
- **Goat Funded Trader (reference)** — **Prohibited** (off-the-shelf / commercial challenge-passing EAs banned) · rulebook v1.

## Rule-Violation Flags
- None on the *claimed* mechanism. **Risk flag:** "scales risk intelligently based on account equity" + explosive weekly compounding implies aggressive equity-scaled sizing that, if it scales into adverse excursions, could trip daily/overall DD — but this is not independently demonstrated.

## Mechanical Rule-Respect
**Vendor-documented only** (ATR stop loss claimed); **not independently demonstrated**, and the results post itself discloses no stop-loss methodology. No independently confirmed hard equity-stop / daily-loss-stop / max-position control. → treat as **vendor-claimed, unconfirmed.**

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | NOT REPORTED (only +106% total / explosive weekly flips) | TIER3/4 | vendor blogs |
| Maximum Drawdown | 0.39% (claimed) | TIER3 | mql5 blog 768819 |
| Win Rate | "80%+" (claimed) | TIER4 | reseller listicle |
| Profit Factor | 3.56 (claimed) | TIER3 | mql5 blog 768819 |
| Track Length | "18+ months" (claimed) | TIER3 | vendor |
| Real vs Demo | "Live — Real Money", $600 (claimed; link absent) | TIER3 | mql5 blog 768819 |

## Backtest Assessment
"Optimized through thousands of backtests" — no public backtest report with real tick data, modeled spread/commission/slippage/swap, multi-regime coverage, or out-of-sample/walk-forward was provided. Near-worthless as evidence; the vendor explicitly pivots to "verified results, not fake backtests," yet the "verified" Myfxbook links are absent.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No public **Tier 0/1 trade-level history** exists (Myfxbook links not provided; aggregator 502; no funded statements). A ruin probability cannot be honestly derived from a single headline return, a claimed 0.39% DD, screenshots, or a withdrawal image. **DD-definition mismatch caveat:** the claimed 0.39% is a host/vendor figure under an unknown method and cannot be compared to any firm's daily/overall DD rule. `NON-ESTIMABLE` is a negative finding for Survival and bars Deployable.

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** Public data does not support trade-level position sizing; any "set manual" figures are vendor-supplied and unverifiable.

## Cost & Licensing
~$497 (or $349 via crypto) on MQL5 Market; widely redistributed via group-buy/reseller sites (eafxstore, ecomforex) and a Grizzly Traders / Ko-fi storefront with rotating discounts. Cloud/MQL5 licensing.

## Community Sentiment
No independent community evidence located. The negative-case searches (`scam`, `blown account`, `refund`, `grid`, `martingale`, `losing`) returned **no specific complaint** — but also **no independent corroboration**; essentially all discussion is the developer's own promotional blog network and resellers. For a product claiming an 18-month live track and "best EA 2026," the **absence of any independent third-party verification or user journal is itself a red flag.**

## Why This Will Probably Fail
1. **Most likely benign explanation:** the headline is a **curve-fit / cherry-picked window or a small-sample lucky run** on a $600 account, dressed as an 18-month "verified" track; the "0.39% DD" most plausibly reflects either a short favourable period or **losers being held/recovered rather than stopped** — neither survives a funded account.
2. **Prop-server case:** on a prop firm's broker/feed with wider spreads and the firm's own equity-DD calculation, an equity-scaled breakout that "compounds 233% in a week" would almost certainly breach daily/overall DD; the vendor's smooth curve is untested under those conditions.
3. **Variance case:** even if it clears an evaluation in a calm window, the explosive-compounding profile is the opposite of repeated-payout survivability — passing and surviving are different problems.
4. **Evidence fragility:** ~100% of the case rests on **Tier 3/4 vendor blogs** with **no Myfxbook links provided**. The single piece of evidence that would most change the verdict — an **inspectable, independent, ≥6-month real-money trade-level Myfxbook/FXBlue record** matching the purchasable default settings — does not exist publicly, and I cannot obtain it.

## Scores
Evidence: **best_tier = TIER3** (headline return+DD is vendor-only, no independent verification). Gate B black box → Compliance ceiling 5, Risk ceiling 4. ROR NON-ESTIMABLE → Survival multiplier = min(A, 0.20). Multiplier A (Tier 3)=0.25; Multiplier B (Tier 3)=0.30.

| Dimension | Latent | Multiplier / Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival | 2 | × min(0.25, 0.20)=0.20 → round(0.40)=0→clamp | **1** |
| Prop-Firm Compliance | 5 | min(latent, Gate-B 5) | **5** |
| Risk Management | 4 | min(latent, Gate-B 4, ctrl-evidence 5)=4 | **4** |
| Challenge-Passing | 3 | × 0.25 → round(0.75)=1 | **1** |
| Consistency | 3 | × 0.30 → round(0.90)=1 | **1** |
| Transparency | 2 | × 0.30 → round(0.60)=1 | **1** |
| Profitability | 2 | × 0.30 → round(0.60)=1 | **1** |

**Overall** = 0.30·1 + 0.20·5 + 0.15·4 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 1.00 + 0.60 + 0.15 + 0.10 + 0.05 + 0.05 = **2.25 → 2.3 (band: poor)**.

## Deployment Verdict
**AVOID** — **Overall 2.3 (poor).**
**Binding criterion:** headline return+DD evidence is **Tier 3 (no independent verification)**. Reinforced by: mechanism unverifiable (Gate B black box, Low inference confidence); ROR NON-ESTIMABLE; internally contradictory claims (0.39% DD vs +233%/week); and absent Myfxbook links / zero independent corroboration. Fails Deployable gates 1 (mechanism not established from public evidence), 2 (best_tier not ≥ Tier 1), 3 (no inspectable ≥6mo real-money history), 7 (ROR non-estimable), and 8 (no funded evidence).

## Similar EAs
Shares the "implausibly low drawdown + explosive growth, vendor-verified, uninspectable Myfxbook" profile with `[[dowgold-hedging-scalper-mt5]]` (excluded) and the high-win/low-DD marketing of `[[ai-gold-sniper-mt5]]` and `[[happy-gold-ea-mt5]]` (Avoid). Distinct in that the *claimed* mechanism (breakout + ATR SL) is legal, so it is Gate-B/Avoid rather than Gate-A excluded.

## Red Flags
- 0.39% max DD with +106% gain **and** a "$600→$2,000 in one week" flip — mutually inconsistent; classic doctored/cherry-pick or held-loser signature.
- "Verified on MyFxBook" with **no links provided**; results post discloses no stop-loss methodology despite marketing an "ATR stop."
- Evidence base is almost entirely the developer's own promotional blog posts + resellers/group-buys; **zero independent verification or user journals**.
- Instrument inconsistency (GBPJPY/EURUSD vs gold) across the vendor's own materials.

## Source Links
| URL | Retrieved | Affiliate? |
|-----|-----------|-----------|
| https://www.mql5.com/en/blogs/post/768819 (MyFxBook results post) | 2026-06-20 18:46 UTC | no (vendor) |
| https://www.mql5.com/en/blogs/post/768792 (V4 overview / ATR SL, breakout) | 2026-06-20 18:48 UTC | no (vendor) |
| https://www.mql5.com/en/blogs/post/767301 (best mt5 ea for gold) | 2026-06-20 18:48 UTC | no (vendor) |
| https://www.mql5.com/en/blogs/post/768874 ($600→$2,000/week) | 2026-06-20 18:48 UTC | no (vendor) |
| https://www.mql5.com/en/blogs/post/768909 ($1,000 withdrawal proof) | 2026-06-20 18:48 UTC | no (vendor) |
| https://www.fxroboteasy.com/experts/apex-drawdown-zero | 2026-06-20 18:46 UTC (HTTP 502 — uninspectable) | unknown |
| https://eafxstore.com/product/apex-drawdown-zero-ea-mt5/ ; https://grizzlytrading.online/products/apex-drawdown-zero... | 2026-06-20 18:31 UTC | yes (group-buy/reseller) |

## Analyst Notes
**FACTS:** named MQL5 developer (Tshivhidzo Mbedzi/MCP Labs); MQL5-listed ~$497; vendor blogs claim +106%/0.39%DD/PF3.56 over 18mo and a $600→$2,000 weekly flip; vendor describes a session-breakout with ATR stop loss; no Myfxbook links provided; instruments stated inconsistently. **ANALYSIS:** the claimed mechanism is legal (passes Gate A), but the entire performance case is Tier-3/4 vendor self-report with internal contradictions and no independent verification, so it cannot rise above Avoid; the 0.39%-DD-plus-explosive-growth pattern is the signature of either held losers or a doctored/cherry-picked statement, but the explicit ATR-SL claim keeps the strong-inference bar for a Gate A exclusion unmet. **ASSUMPTIONS:** none drive the verdict — Avoid follows directly from Tier-3 headline evidence and a Gate-B black box; the mechanism *could* be a perfectly legal breakout, which is exactly why it is Avoid (unproven) rather than Excluded (disqualified).

## Future Research Needed
Operator to obtain the actual MyFxBook/FXBlue URL(s) and confirm real-money status, broker, ≥6-month trade-level history, and whether the record matches the purchasable default settings; and, ideally, funded-account statements. Only inspectable Tier 0/1 trade-level history could move this above Avoid.

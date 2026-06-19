# AI Gold Sniper MT5

## Overview
A closed-source, fully-automated commercial MQL5-Market EA for **XAUUSD only (H1)**, marketed as "GPT-4o / AI-powered." Vendor positions it as a single-trade, hard-SL gold strategy with "no grid, no martingale" and a news filter. Survives Gate A (mechanism legal and independently corroborated as single-entry SL/TP), but the headline performance rests entirely on **vendor MQL5 signal claims (Tier 3)** featuring an implausible **100% win rate**, directly contradicted by independent user reports of large stop-loss losses and a wiped-out author signal. **Verdict: Avoid (Overall 2.3).**

## Vendor / Developer
**Ho Tuan Thang (MQL5 user "TuanThang").** Identifiable and accountable — an established MQL5 seller with multiple gold EAs and a 14,000–15,000-member MQL5 channel; reviewers praise responsive support. Not anonymous (a positive vs. much of the field), but operates a stable of similarly-marketed AI/gold EAs (rebrand/portfolio risk — see Similar EAs).

## MT5 Compatibility & Dependencies (publicly documented only)
- Platform: MT5 (MQL5 Market product 133197). Symbol **XAUUSD only**, timeframe **H1**.
- Broker: "True ECN brokers with low latency and tight spreads" recommended.
- Min deposit $300 @ 0.01 lot; recommended $500. Max positions: **one trade at a time** (vendor).

## Strategy Mechanism (publicly documented / inferable; Gate A/B status)
Vendor describes "multi-timeframe technical signals, price action data, and market volatility analysis," balancing momentum and trend, with a **news filter** to avoid high-impact events. Independent review (unlockea) reconstructs it as **"single-entry, fixed-lot trades with SL & TP"** — i.e. one position at a time, hard stop and target, fixed 0.01 lot. Vendor states verbatim **"There is no Grid, and no Martingale"** and **"The EA strictly uses a Stop Loss for every single trade."**
- **Gate A: SURVIVES** — single-entry, fixed-lot, hard SL, news-*avoiding* filter; no grid/martingale/averaging signature; H1 hold (not tick-scalping/HFT by frequency or hold time).
- **Gate B: does not bind** — mechanism is publicly described and independently corroborated (clear inference), not a pure black box. Closed source still limits confirmation of risk-control behavior under stress.

## Mechanism Inference Confidence
**Medium.** The single-entry SL/TP structure is stated by the vendor and independently echoed (unlockea), and is consistent with the 100%-win/low-DD-then-occasional-large-SL profile reported by users. No source code or trade-level public history to confirm exact entry logic or worst-case behavior.

## Recommended Instruments
XAUUSD (Gold) only, H1.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD (233%/21wk, 100% win, 3.1% DD; 542%/35wk, 100% win, 8.69% DD) | mql5.com/market/product/133197 (vendor) + eafxstore/cheaperforex echoes | vendor / affiliate | vendor | TIER3 | 2026-06-19 | Low | MQL5 signal/vendor stats; "100% win rate" implausible; live monitoring "coming soon"; no inspectable independent record |
| Mechanism / risk controls (single-entry, hard SL every trade, no grid/martingale, news filter) | mql5.com/.../133197 ; blogs.unlockea.com/ai-gold-sniper-ea | vendor / independent review | vendor + independent | TIER3 | 2026-06-19 | Medium | Independent review corroborates "single-entry, fixed-lot trades with SL & TP"; controls vendor-documented, not demonstrated under stress |
| Prop-firm success claim ("prop-friendly") | blogs.unlockea.com/ai-gold-sniper-ea | independent-ish review | independent | TIER4 | 2026-06-19 | Low | "Low drawdown... make it prop-friendly" — opinion, no Tier-0 funded proof |
| Negative-case evidence (losses, huge SLs, author signal wiped out, 3 EAs unprofitable) | MQL5 reviews / search aggregation of reviews | independent (buyer reviews) | independent | TIER3 | 2026-06-19 | Medium | "Bot lost my money"; "huge stop losses"; "author's signal on a real account was wiped out"; MQL5 rating 3.78/5 (109 reviews) |

## Source Reliability Assessment
- **source_count: 5** · **independent_source_count: 2** (unlockea review; aggregated independent MQL5 buyer reviews) · **affiliate_source_count: 2** (eafxstore, cheaperforex — group-buy/discount funnels).
- **Best evidence found:** Tier 3 — a vendor-hosted MQL5 signal and an independent review describing the mechanism. **No inspectable evidence above Tier 3**; no public verified real-money trade-level history (Myfxbook not used; MQL5 "live monitoring coming soon"). MQL5 listing itself was fetchable; Myfxbook/vendor verification was not pursued/available.

## Unverified Claims
- "100% win rate" over 40/78 trades; 233%/542% signal gains; 3.1%/8.69% max DD — all **vendor MQL5 signal claims**, no independent verification, and an implausible perfect win rate.
- "GPT-4o / AI-powered" — unverifiable marketing; no public evidence of an LLM in the execution path.
- "Prop-friendly" — no Tier-0 funded-account evidence.
- Backtest "2003–2024, 99.9% modeling quality" — vendor claim; tick-data source/costs/OOS unstated; not reproducible by this agent.

## Eligibility Gates
- **Gate A — PASS.** Single-entry, fixed-lot, hard SL, news-avoiding filter; no grid/martingale/averaging or tick-scalp signature.
- **Gate B — does not bind.** Mechanism publicly described + independently corroborated (clear inference). Closed source noted as a confirmation limit, not a black box.
- **Gate C — per-firm legality:** mechanism legal at all primaries; **product-type** friction at Funding Pips and The 5%ers (closed-source fully-automated third-party commercial EA). See below.

## Per-Firm Legality Verdict
- **FundedNext — Permitted** (rulebook v1; numerics PROVISIONAL/secondary). EAs allowed; mechanism legal; not a named-banned bot found. Conditional only insofar as FundedNext's rulebook is secondary-sourced.
- **The Funded Trader — Permitted** (rulebook v1). EAs allowed with standard rules; mechanism legal. Carry the firm's operator/payout-durability flag.
- **Funding Pips — Conditional** (rulebook v1, EA policy PRIMARY-confirmed). Third-party EAs permitted **only as a trade/risk manager**; a fully-automated third-party strategy EA is effectively barred on standard evaluations → leans Prohibited for product type despite a legal mechanism.
- **The 5%ers — Conditional** (rulebook v1). EAs allowed but trader must "control the EA's internal logic" and shared third-party EAs are restricted; a closed-source commercial EA is contested.
- *Reference (non-gating):* **Alpha Capital — Prohibited** (mandatory .MQ5 source-code submission; closed-source cannot comply). **Goat Funded Trader — Prohibited** (off-the-shelf commercial challenge EAs banned).

## Rule-Violation Flags
- **Product-type (not mechanism):** closed-source fully-automated third-party commercial EA conflicts with Funding Pips (trade/risk-manager-only) and The 5%ers (control-of-logic) policies.
- **SL:TP ratio:** independent reports of "huge stop losses" and "poor SL:TP ratios... large drawdowns that never outweighed the profit" — a small-TP/large-SL profile that inflates win rate while carrying tail loss, even with a hard stop.

## Mechanical Rule-Respect
Hard per-trade stop loss is **vendor-documented and independently described** (single-entry SL/TP), but **not independently demonstrated to hold under stress** — and is contradicted by user reports of large realized stop-loss losses and a wiped-out author signal. No documented hard daily-loss stop or equity stop. Max positions = 1 (vendor).

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | NOT REPORTED (signal gains 233%/21wk, 542%/35wk are cumulative vendor claims) | TIER3 | mql5 vendor signal |
| Maximum Drawdown | 3.1% / 8.69% (vendor signal); $16.01 / 1.52–6.29% (vendor) | TIER3 | mql5 vendor / unlockea |
| Win Rate | "100%" (claimed; implausible) | TIER3 | mql5 vendor |
| Profit Factor | NOT REPORTED | — | — |
| Track Length | ~21–35 weeks (vendor signal); no inspectable independent record | TIER3 | mql5 vendor |
| Real vs Demo | Claimed live (IC Markets) but uninspectable; "live monitoring coming soon" | TIER3 | mql5 vendor |

## Backtest Assessment
Vendor claims 2003–2024 backtest at "99.9% modeling quality." Real-tick-data source, spread/commission/slippage/swap modeling, multi-regime coverage, and OOS/walk-forward are **unstated**; not reproducible here. A high modeling-quality figure does not establish real-tick or cost-realistic testing → treat as a near-worthless claim for an all-weather conclusion.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No public Tier 0/1 trade-level history (no Myfxbook/FXBlue verified real-money page; MQL5 signal is Tier 3 and was not inspectable at trade level). Per CLAUDE.md, ROR is not manufactured from vendor signal summaries, the 100%-win claim, or backtests. The independent reports of large stop-loss losses and a wiped-out signal indicate the true ROR is materially non-zero, but it cannot be quantified from inspectable public data. **Daily-DD violation prob / max-DD violation prob: indicative-only**, non-quantifiable; the small-TP/large-SL profile makes a cluster of losses capable of tripping a 5%/10% prop limit. DD-definition mismatch caveat applies (vendor DD ≠ firm daily/overall DD).

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** Sizing cannot be derived from verified public trade-level data; the only figures are vendor signal claims with an implausible win rate. Any 50k/100k/200k recommendation would be fabrication.

## Cost & Licensing
$499 (MQL5 Market), one-time with updates; rentals/activations per MQL5 terms. Affiliate group-buy/"cracked" copies circulate (eafxstore, cheaperforex, forexcracked) — low-trust, malware-risk, never positive evidence.

## Community Sentiment (independent only; criticism)
- MQL5 rating **3.78/5 (109 reviews)** — mediocre for a $499 EA.
- "Bot lost my money. Sorry but this is not good."
- "Purchased three of Thang's EAs, but none of them are profitable anymore" — "huge stop losses."
- "Poor stop loss to take profit ratios leading to large drawdowns that never outweighed the profit."
- "The author's signal on a real account was wiped out." (directly contradicts the 100%-win marketing.)
- Recent (Apr–May 2026) reviews report accounts eroded by consecutive stop-loss hits in volatile conditions.
- Positive reviews exist but skew toward setup/support praise and short calm-period results.

## Why This Will Probably Fail
1. **Most likely benign explanation:** the 100%-win/low-DD signal is a **short calm-window, small-TP record** where no loser has yet hit its (large) stop — survivorship within the vendor's stable of accounts/EAs. A perfect win rate over dozens of trades is a hallmark of unrealized-loss accounting or cherry-picked windows, not a durable edge.
2. **Prop-server case:** on a prop firm's broker/feed with wider gold spreads and the firm's own DD calculation, the small TP shrinks and the large SL (or a news gap the filter misses) trips daily/overall DD — exactly the "consecutive stop-loss hits" users already report on retail brokers.
3. **Variance case:** it could pass an evaluation in a calm month and then take a cluster of full-SL losses on a funded account — passing and surviving are different problems, and the SL:TP geometry favors slow gains then a sharp giveback.
4. **Evidence fragility:** everything rests on **Tier 3** vendor signals; the single most decisive missing item is an **inspectable ≥6-month verified real-money trade-level record** (Myfxbook/FXBlue or funded-account history) — which does not exist publicly, and the one author "signal on a real account" is reported wiped out.

## Scores
Evidence: **best_tier = TIER3**. Multiplier A (Survival, Challenge) = 0.25; Multiplier B (Profitability, Consistency, Transparency) = 0.30. **ROR NON-ESTIMABLE → Survival multiplier = min(0.25, 0.20) = 0.20.** Risk control-evidence ceiling = vendor-documented → Risk ≤ 5. Gate B does not bind (mechanism inferable).

| Dimension | Latent | × Mult / Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival | 2 | × 0.20 (ROR cap) = 0.40 → round → clamp | 1 |
| Prop-Firm Compliance | 5 | min(5, no Gate-B) | 5 |
| Risk Management | 4 | min(4, ceiling 5) | 4 |
| Challenge-Passing | 3 | × 0.25 = 0.75 → round → clamp | 1 |
| Consistency | 2 | × 0.30 = 0.60 → round → clamp | 1 |
| Transparency | 3 | × 0.30 = 0.90 → round → clamp | 1 |
| Profitability | 2 | × 0.30 = 0.60 → round → clamp | 1 |

**Overall** = 0.30·1 + 0.20·5 + 0.15·4 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 1.00 + 0.60 + 0.15 + 0.10 + 0.05 + 0.05 = **2.25 → 2.3 (poor)**.
(Latent is for ordering among unproven EAs only; the headline is the adjusted Overall.)

## Deployment Verdict
**AVOID — Overall 2.3 (poor).**
**Binding criterion:** headline return+DD evidence is **Tier 3 (no independent verification)** AND **ROR NON-ESTIMABLE with best_tier ≤ Tier 2**. Reinforced by an implausible 100%-win signal contradicted by independent blown-account/"signal wiped out" reports, a small-TP/large-SL tail-loss profile, and product-type frictions at Funding Pips/The 5%ers. Fails Deployable gates 2 (best_tier), 3 (≥6mo verified live), 4 (verified DD headroom), 7 (estimable ROR), and 8 (funded evidence).

## Similar EAs
Same vendor (Ho Tuan Thang / TuanThang) ships a stable of gold EAs — **AI Gold Trading MT5** (product 132551), **AI Gold Scalp Pro** (product 164942), and MT4 variants — fingerprint-adjacent (XAUUSD single-entry SL/TP AI-marketed). Portfolio/rebrand risk: a perfect-win signal on one product while "three of his EAs are unprofitable" per buyers suggests survivorship across the stable.

## Red Flags
- Implausible **100% win rate** marketing.
- Headline performance is **vendor MQL5 signal only**; "live monitoring coming soon"; no independent verified record.
- Independent reports: **"author's signal wiped out," "huge stop losses," three EAs unprofitable**; MQL5 3.78/5.
- **Poor SL:TP geometry** (small TP / large SL) — high win rate masking tail loss.
- Closed-source commercial automated EA — Conditional/Prohibited product type at Funding Pips and The 5%ers; Prohibited at both reference firms.
- "AI / GPT-4o" branding unverifiable.

## Source Links (with retrieval date + affiliate flag)
| URL | Retrieved | Used For | Affiliate? |
|-----|-----------|----------|-----------|
| https://www.mql5.com/en/market/product/133197 | 2026-06-19 18:40 UTC | vendor listing (mechanism, SL, no grid/martingale, price, rating) | no |
| https://blogs.unlockea.com/ai-gold-sniper-ea-safe-growth-or-false-hope/ | 2026-06-19 18:41 UTC | independent review (mechanism corroboration, red flags, vendor-only perf) | no |
| https://www.mql5.com/en/users/tuanthang | 2026-06-19 18:40 UTC | vendor accountability + product stable (located via search) | no |
| https://eafxstore.com/product/ai-gold-sniper-mt5/ | 2026-06-19 18:40 UTC | discovery + signal-gain echo (group-buy) | yes |
| https://cheaperforex.com/product/ai-gold-sniper-ea-mt5/ | 2026-06-19 18:40 UTC | discovery + claims echo (discount funnel) | yes |

## Analyst Notes
**FACTS:** vendor states single-entry, hard SL, no grid/martingale, news filter; independent review corroborates single-entry SL/TP structure; MQL5 rating 3.78/5 (109 reviews); independent buyers report large stop-loss losses and a wiped-out author signal; performance is vendor MQL5-signal only. **ANALYSIS:** the EA is mechanically legal (a genuine positive vs. the grid/martingale field) but its survival case collapses on inspection — a perfect-win/low-DD signal with small-TP/large-SL geometry is the classic configuration that books many small wins then a sharp full-SL giveback, which is exactly what users report; Tier-3 evidence + NON-ESTIMABLE ROR floor the survival/challenge/consistency dimensions. **ASSUMPTIONS:** that the various circulating reviews refer to this product/its MT4 twin (consistent across sources); that the assessed config matches the listing defaults. None of these rescue the verdict.

## Future Research Needed
- Operator to supply (or locate) an **inspectable ≥6-month verified real-money trade-level record** (Myfxbook/FXBlue or funded statements) before this could rise above Avoid; absent that, Tier-3/NON-ESTIMABLE caps it.
- If FundedNext primary numerics and Funding Pips/5ers EA-policy edge cases are later primary-confirmed, re-check the per-firm verdicts (currently rulebook v1; FundedNext numerics provisional).

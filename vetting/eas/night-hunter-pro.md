# Night Hunter Pro

## Overview
Commercial, closed-source MT4/MT5 **night-scalping** EA trading ~12 FX pairs in the low-volatility Asian session (21:00–01:00 broker time) via mean-reversion on tight channels. Notable for an **accountable vendor** and a **4+ year real-money Myfxbook track record** — the strongest evidence profile seen in this archive so far — yet it remains an Avoid because the record is uninspectable to this routine (Myfxbook 403), ROR is NON-ESTIMABLE, the ~30% max drawdown is prop-incompatible, and the edge is the classic broker/rollover-spread-dependent night-scalp that typically does not survive a prop server.

## Vendor / Developer
**Valeriia Mishchenko / "ValeryTrading"** (MQL5). Identifiable and accountable; ~10 yr stated algo-dev experience; ~4.3/5 across 269+ reviews. This is a genuine positive vs anonymous vendors.

## MT5 Compatibility & Dependencies
MT4/MT5; M5 charts; ~12 pairs (GBPUSD, EURUSD, EURCHF, USDCAD, USDCHF, CHFJPY, AUDCAD, EURCAD, EURAUD, EURGBP, EURJPY, AUDJPY). **Hard requirements:** ECN/Raw account, tight spreads during 21:00–01:00 rollover hours, fast execution without requotes, ≥1:100 leverage, sub-1ms-latency VPS. Performance is explicitly "extremely broker-dependent."

## Strategy Mechanism
**Night scalping / mean-reversion** in low-liquidity Asian hours: enters with **pending orders** on tight channels behind multiple confirmation filters; **fixed stop loss on every trade**; **no martingale** ("lot sizes do not increase after losses") and **no grid** ("does not add positions during drawdowns"). Independently corroborated by multiple reviews → **survives Gate A**.

## Mechanism Inference Confidence
**Medium-High.** Multiple independent reviews agree on the night-scalp mean-reversion + fixed-SL + no-martingale/grid description; exact entry logic is closed-source but the category and risk structure are well established.

## Recommended Instruments
Major/cross FX pairs (12), Asian session only. No gold/indices.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD (+215% since Oct 2020 / ~30% max DD / ~78% win / 4+ yr real money) | Myfxbook (vendor-linked) + independent reviews (newyorkcityservers, theforexgeek, topfxmanagers) | independent reviews referencing a verified Myfxbook account | independent (corroborating) — but hosted page uninspectable here (403) | TIER2 | 2026-06-19 | Medium | Real-money verified record described consistently across independent sources; could be TIER1 if the hosted Myfxbook page were inspectable. Conservatively TIER2 (caveated/uninspectable firsthand) |
| Mechanism / risk controls (night scalp, fixed SL, no martingale/grid) | https://newyorkcityservers.com/blog/night-hunter-pro-review | independent review | independent | TIER2 | 2026-06-19 | Medium-High | Corroborated by several independent reviews |
| Prop-firm success claim ("passing challenges"; FTMO/FIFO preset) | newyorkcityservers; bestforexeas | review/affiliate | mixed | TIER4 | 2026-06-19 | Low | No Tier-0 funded proof; FTMO is not even a target firm here |
| Negative-case evidence (blown $3k in first day; polarized recent reviews; "outdated"; broker-dependent) | newyorkcityservers; fxtechlab; topfxmanagers | independent | independent | TIER3 | 2026-06-19 | Medium | One client blew a $3,000 account day one; no updates >1 yr; results polarized |

## Source Reliability Assessment
- source_count: **5** (3 web searches/leads consolidated + newyorkcityservers review fetched + fxtechlab fetch attempt which resolved to a directory page).
- independent_source_count: **3** (newyorkcityservers, topfxmanagers, theforexgeek — referencing the verified record and the negative case; degree of affiliate funding varies).
- affiliate_source_count: **2** (bestforexeas and other review-aggregator pages with affiliate characteristics).
- **Best evidence found:** Tier 2 — a 4+ year real-money Myfxbook record consistently referenced by multiple independent reviews, but the hosted page itself was **not** inspectable (403). No firsthand Tier 0/1 inspection achieved.

## Unverified Claims
- The +215% / ~30% DD / ~78% win figures — credible and independently referenced, but not inspected firsthand (Myfxbook 403).
- "Passing challenges" / FTMO preset — no Tier-0 funded proof; and FTMO is not a target firm.
- Trade-level history (entry/exit, hold times, true DD under firm definitions) — not inspectable → ROR cannot be estimated.

## Eligibility Gates
- **Gate A — PASS (survives).** Night-scalp mean-reversion with fixed per-trade SL; no martingale/grid (independently corroborated). Not tick-scalping/HFT (M5, multi-minute holds) and not swap/latency arbitrage; **but** the rollover-window dependence is a standing legality risk at firms banning "rollover exploitation."
- **Gate B — mechanism inferable (Medium-High).** Not a black box → no Gate-B ceiling.
- **Gate C — per-firm:** Conditional across all four primary firms; not Prohibited at all → not an automatic Gate-C Avoid.

## Per-Firm Legality Verdict
- **FundedNext — Conditional (rulebook v1, SECONDARY/UNCONFIRMED).** EAs allowed; night scalping not explicitly banned, but low-liquidity-hour exploitation is sometimes restricted and the FundedNext rulebook is provisional (primary 503) → Conditional.
- **Funding Pips — Conditional (rulebook v1).** Mechanism legal, but a fully-automated **third-party commercial** EA is barred on standard evaluations (trade/risk-manager only) → Conditional/effectively Prohibited on standard programs.
- **The 5%ers — Conditional (rulebook v1).** EAs allowed but **"rollover exploitation" is explicitly prohibited** and traders must control the EA's internal logic (hostile to closed-source commercial). A rollover-window night scalper sits uncomfortably close to that line → Conditional (leaning restrictive).
- **The Funded Trader — Conditional (rulebook v1).** Commercial pre-programmed EAs restricted / must have unique non-masked parameters → Conditional.

## Rule-Violation Flags
- **~30% verified max DD** dwarfs every primary firm's ~10% max-overall-DD and 5% daily-DD limits at the settings that produced the record (DD-definition mismatch caveat applies, but a 30% gap dwarfs reconciliation). A lower-risk "prop preset" exists but its own verified DD/return over ≥6 months is not inspectable.
- **Rollover-window dependence** risks tripping The 5%ers "rollover exploitation" clause; closed-source commercial EA conflicts with Funding Pips standard-program policy.
- **Broker/spread/execution dependence:** the edge requires abnormally tight rollover-hour spreads — prop firms typically run wider spreads/commissions at rollover, the textbook way a night-scalper's edge evaporates on the funded server.

## Mechanical Rule-Respect
**Fixed per-trade stop loss is independently corroborated** (no martingale/grid). However, **no documented hard equity-stop or daily-loss-stop**, and the aggregate ~30% DD plus a reported same-day $3,000 blow-up show the per-trade stop does not bound account risk to prop levels.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | ~2–3% implied (+215% over ~4.7 yr) | TIER2 | independent reviews referencing Myfxbook |
| Maximum Drawdown | ~30% | TIER2 | independent reviews referencing Myfxbook |
| Win Rate | ~78% | TIER2 | independent reviews |
| Profit Factor | NOT REPORTED | — | — |
| Track Length | 4+ years (since Oct 2020), real money | TIER2 | independent reviews referencing Myfxbook |
| Real vs Demo | Real money (uninspectable firsthand) | TIER2 | independent reviews |

## Backtest Assessment
Not the basis of the case; the live record is the relevant evidence. Reviews note backtest-vs-live divergence (a night-scalper red flag — tick-data/spread assumptions rarely match live rollover spreads). Treated as near-worthless vs the (uninspectable) live record.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** Despite a long real-money record, the trade-level history is not inspectable (Myfxbook 403), so no per-trade/daily distribution can be extracted. Indicatively, ~30% verified max DD is incompatible with ~10% firm max-DD and ~5% daily-DD limits at default settings, and night-scalp returns are autocorrelated/lumpy (occasional cluster losses raise true ROR) — but this is indicative only. No defensible ROR without inspectable Tier 0/1 history.

## Recommended Risk Settings
**Non-actionable.** Default-risk DD (~30%) is prop-incompatible; the lower-risk prop preset has no inspectable ≥6-month verified DD/return to size against. Sizing for 50k/100k/200k cannot be defended from public data.

## Cost & Licensing
$2,340 (10 live activations). High price relative to polarized recent results and a >1-year update gap.

## Community Sentiment
Genuinely mixed/independent: a long-standing verified record and many satisfied users (some citing large gains) vs a reported same-day $3,000 blow-up, "poor performance / outdated strategy" reviews, and warnings that backtests diverge from live. The negative case is real, not just affiliate noise — appropriate for a broker-sensitive night scalper whose edge decays as conditions and spreads change.

## Why This Will Probably Fail
1. **Most likely benign explanation:** the 4-year curve is real but achieved on a retail ECN broker with unusually tight rollover spreads; the edge is small and spread-dependent, and recent polarization suggests it is decaying as market microstructure changes.
2. **Prop-server case:** prop firms typically widen spreads/commissions at rollover — the exact window the strategy depends on — which would plausibly erase the edge and, at ~30% historical DD, trip the daily/max-DD limit. The 5%ers "rollover exploitation" clause adds direct legality risk.
3. **Variance case:** ~78% win rate with occasional large cluster losses is the profile that passes a challenge on a calm month then surrenders a funded account in one bad Asian session — consistent with the reported same-day blow-up.
4. **Evidence fragility:** the case rests on a verified record I cannot inspect (403) and otherwise Tier 2–3 sources. The single piece that would most change the verdict — an inspectable ≥6-month trade-level history of the **low-risk prop preset** at ≤~6% DD — I do **not** have.

## Scores
Evidence tier governing multiplied dimensions: **TIER2**. ROR **NON-ESTIMABLE** → Survival multiplier = min(A=0.45, 0.20) = **0.20**. Mechanism inferable → no Gate-B ceiling. Risk controls independently corroborated → no control-evidence cap (but latent reflects the ~30% aggregate DD).

| Dimension | Latent | × Multiplier / Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival (30%) | 4 | × 0.20 (ROR cap) = 0.8 → clamp | **1** |
| Prop-Firm Compliance (20%) | 4 | not multiplied (Conditional all firms) | **4** |
| Risk Management (15%) | 5 | no extra cap | **5** |
| Challenge-Passing (15%) | 5 | × 0.45 (A, Tier2) = 2.25 | **2** |
| Consistency (10%) | 4 | × 0.60 (B, Tier2) = 2.4 | **2** |
| Transparency (5%) | 5 | × 0.60 (B, Tier2) = 3.0 | **3** |
| Profitability (5%) | 5 | × 0.60 (B, Tier2) = 3.0 | **3** |

Overall = 0.30·1 + 0.20·4 + 0.15·5 + 0.15·2 + 0.10·2 + 0.05·3 + 0.05·3
= 0.30 + 0.80 + 0.75 + 0.30 + 0.20 + 0.15 + 0.15 = **2.65 → 2.7 (poor)**.

## Deployment Verdict
**AVOID.** Binding criterion: **ROR NON-ESTIMABLE AND best_tier ≤ TIER2** — a deterministic Avoid trigger. Reinforced by a ~30% verified max DD (prop-incompatible vs ~10% limits), a broker/rollover-spread-dependent edge unlikely to survive a prop server, and The 5%ers "rollover exploitation" legality risk. This is nonetheless the **strongest candidate in the archive to date** (accountable vendor, 4-year real-money record, genuine fixed-SL risk controls) — a prime **re-vet** target if a clean ≥6-month inspectable verified record of the low-risk prop preset (≤~6% DD) becomes available.

## Similar EAs
Distinct mechanism from [[the-gold-reaper-mt5]] (gold breakout), [[happy-gold-ea-mt5]] (gold scalp), and [[quantum-queen-mt5]] (gold grid). Same broker-dependence failure mode as other night scalpers. No rebrand match in the index.

## Red Flags
- ~30% verified max DD — prop-incompatible at default settings.
- Edge depends on tight rollover-hour spreads (won't transfer to a prop server reliably); The 5%ers rollover-exploitation clause risk.
- Reported same-day $3,000 account blow-up; polarized recent reviews; no update in >1 year.
- Verified record uninspectable firsthand (Myfxbook 403) → ROR NON-ESTIMABLE, best_tier capped at TIER2.

## Source Links
- https://newyorkcityservers.com/blog/night-hunter-pro-review — 2026-06-19 — independent review (mechanism, verified record, negatives) — affiliate: partial
- https://fxtechlab.com/night-hunter-pro-review/ — 2026-06-19 — resolved to directory page (specific review not inspectable) — affiliate: unknown
- https://topfxmanagers.com/night-hunter-pro-review/ — 2026-06-19 (via search) — independent review — affiliate: unknown
- https://theforexgeek.com/night-hunter-pro-ea-review/ — 2026-06-19 (via search) — independent review — affiliate: unknown
- Myfxbook hosted record — referenced by reviews; not fetchable (403) — affiliate: n/a

## Analyst Notes
- **FACTS:** vendor ValeryTrading (accountable); night-scalp mean-reversion, M5, 12 FX pairs, 21:00–01:00, pending orders + fixed SL, no martingale/grid (independently corroborated); independently-referenced verified real-money Myfxbook record +215% / ~30% DD / ~78% win since Oct 2020; $2,340; one reported same-day $3k blow-up; >1-yr update gap; broker/spread dependent.
- **ANALYSIS:** strongest evidence profile in the archive, but the binding constraints are structural — uninspectable trade-level data (NON-ESTIMABLE ROR), prop-incompatible ~30% DD, and a rollover-spread-dependent edge with direct 5%ers legality risk.
- **ASSUMPTIONS (flagged):** best_tier set to TIER2 conservatively because the hosted Myfxbook page could not be fetched; it could be TIER1 on firsthand inspection. Implied monthly return derived from +215% over ~4.7 yr (not a reported figure).

## Future Research Needed
- If Myfxbook/FXBlue egress is allow-listed, inspect the hosted record (real DD under firm definitions, hold times, the low-risk prop preset's ≥6-month DD/return) — a clean ≤~6% DD prop-preset record could lift this from Avoid toward Watchlist.
- Confirm The 5%ers / FundedNext treatment of rollover-window night scalping (rollover-exploitation clause).
- Operator: only Tier-0 funded-account evidence could lift it past Watchlist.

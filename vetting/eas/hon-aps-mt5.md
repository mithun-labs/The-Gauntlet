# Hon-APS — Advanced Pattern Scanner (MT5)

## Overview
Hon-APS is a **fully open-source** MT5 Expert Advisor by **Christopher Adie ("Adiec7")**, published on the
**MQL5 Code Base (mql5.com/en/code/71521) on 2026-04-06**. It trades **classical chart-pattern breakouts**
(Head & Shoulders, Double/Rounding Bottoms, Triangles, Flags, Cup & Handle) on **H1/H4** major FX + indices,
validated by **Level-2 Order Book** absorption / bid-ask imbalance, with a **KAMA trend filter**, **ATR
trailing stop + partial profits at 1R/2R**, **modified-Kelly sizing**, **hard daily/weekly drawdown limits**,
and a **macro-news filter**. It is explicitly "designed for prop-firm viability and capital preservation."

> **WHY THIS ENTRY IS DIFFERENT.** Unlike every prior archive EA, Hon-APS's **mechanism is fully
> inspectable** (open source) — so it **clears Gate B** outright, its risk controls are **code-verifiable**
> (not vendor-claimed), and it sidesteps the closed-source legality frictions. **But it has no track record
> of any kind** — no Myfxbook, no MQL5 signal, no published backtest — because it is 2.5-month-old free code.
> Open source solves the *transparency and legality* problem; it does **not** solve the *evidence* problem.
> With zero verified performance, best_tier is TIER4 and ROR is NON-ESTIMABLE → **Avoid (unproven)**, not
> because it's bad, but because nothing about its real behavior is known yet.

## Vendor / Developer
**Christopher Adie (Adiec7)** — named, identifiable MQL5 Code Base author. Open-source/free (not a commercial
product); no vendor performance marketing. Accountable and transparent, but new/low-track-record as a publisher.

## MT5 Compatibility & Dependencies (publicly documented only)
- MT5; **H1/H4**; major FX pairs + indices.
- **Requires Level-2 Order Book (`MarketBookGet`)** for its absorption/imbalance edge, with a **tick-volume
  fallback** if DOM is unavailable. **Practical caveat:** reliable L2 DOM is uncommon on retail/prop *spot-FX*
  feeds, so on a prop server the order-flow edge likely degrades to the tick-volume fallback — a transferability risk.

## Strategy Mechanism (publicly documented / inferable; Gate B status)
**FACTS (open-source code page, fetched):** identifies classical chart patterns; on breakout "reads the Level
2 Order Book (MarketBookGet) to calculate bid/ask imbalances and true volume absorption"; **KAMA** trend
filter; **ATR-based trailing stop** via an included ATR Stop-Loss Manager; **partial profits at 1R/2R**;
**Modified Kelly Criterion** sizing; **hard daily/weekly drawdown limits** (`MaxDailyLoss`/`MaxWeeklyLoss`);
**news filter** (MQL5 Economic Calendar + scrapes ForexFactory JSON / Forexprostools). **No grid, martingale,
averaging, or hedging** is present in the code description.

**ANALYSIS:** a legitimate, non-banned discretionary-style breakout system with disciplined per-trade and
account-level risk controls — **survives Gate A** cleanly. Because the source is open, the absence of
grid/martingale and the presence of stops/DD-limits are **verifiable**, not merely asserted.

## Mechanism Inference Confidence
**High** — the full source code is public and readable. This is the only archive EA whose mechanism is
established by direct code inspection rather than inference from marketing.

## Recommended Instruments
Major FX pairs + indices, H1/H4 (per code defaults).

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Mechanism: pattern-breakout + L2 order-flow, ATR trailing SL, Kelly, DD limits, news filter; no grid/martingale | mql5.com/en/code/71521 | open-source code | author (inspectable) | TIER3 | 2026-06-23 | High | Logic verifiable from source; risk controls present in code |
| Headline return / drawdown | — | — | — | **TIER4 (none)** | 2026-06-23 | n/a | **No performance evidence exists** — no Myfxbook, no signal, no published backtest |
| Prop-firm suitability ("designed for prop-firm viability") | mql5.com/en/code/71521 + robotfx mirror | author/listing | author | TIER4 | 2026-06-23 | Low | Design intent only; unproven; L2-DOM dependence is a transfer risk |
| Negative-case evidence | WebSearch scam/blown/results | search aggregate | n/a | n/a | 2026-06-23 | Low | No complaints (too new) AND no verified results — both reflect its newness |

## Source Reliability Assessment
- **source_count: 4** (MQL5 code page [fetched], robotfx mirror, 2 discovery/negative searches) ·
  **independent_source_count: 1** (the inspectable source code itself; no independent reviews exist yet) ·
  **affiliate_source_count: 1** (robotfx mirror).
- **Best evidence found:** the **source code** (establishes mechanism + risk-control *logic* at High
  confidence) — but **no performance evidence of any tier**. Best_tier for the return/DD pair = **TIER4
  (absent)**.

## Unverified Claims
- "Designed for prop-firm viability / capital preservation" — design intent; **no live or backtest proof.**
- That the L2 order-flow edge functions on a real/prop feed — unproven; DOM often unavailable on spot FX.
- Any return, drawdown, win rate, or survivability — **entirely unknown** (no track record).

## Eligibility Gates
- **Gate A — PASS (survives, verifiable).** Pattern breakout + ATR trailing SL + R-based partials; no
  grid/martingale/averaging/hedging — **confirmed in source**, not inferred. Not HFT (H1/H4).
- **Gate B — CLEARED (mechanism publicly verifiable / open source) → NO Gate-B ceiling.** First archive EA to
  clear Gate B by full code transparency rather than inference.
- **Gate C — per-firm:** not Prohibited at any primary on mechanism; the binding legality nuance is
  **strategy-uniqueness / shared-EA**, since open-source code run identically by many traders can trip
  duplication/shared-EA rules → Conditional across primaries (self-modification would restore uniqueness).

## Per-Firm Legality Verdict
| Firm | Verdict | Rulebook | Basis |
|------|---------|----------|-------|
| FundedNext (primary) | Conditional | v1 (PROVISIONAL) | EA-permissive mechanism, but strategy-uniqueness/customization rule vs a shared open-source EA |
| Funding Pips (primary) | Conditional | v1 | Third-party EA only as trade/risk manager; open-source is third-party unless substantially self-modified (then self-developed exception → full automation) |
| The 5%ers (primary) | Conditional | v1 | Control-of-internal-logic **satisfied** (open source), but "shared third-party EA" concern (many run identical code) |
| The Funded Trader (primary) | Conditional | v1 | Standard EA OK, but "unique non-masked parameters" vs a shared open-source EA |
| Alpha Capital (reference) | Conditional | v1 | **Notable:** Alpha requires .MQ5 source-code submission + pre-approval — Hon-APS **can comply** (open .MQ5), unlike every prior closed EA (non-gating) |
| Goat Funded Trader (reference) | Conditional | v1 | Bans *commercial* challenge EAs; Hon-APS is free/open-source (not commercial), but off-the-shelf/operator-risk concerns remain (non-gating) |

## Rule-Violation Flags
- **Strategy-uniqueness / shared-EA:** a popular open-source EA run identically by many traders risks
  duplicate-strategy or shared-EA flags at FundedNext/TFT/5ers. Mitigation: self-modify parameters/logic.
- **L2-DOM dependence:** edge may not transfer to a prop feed without reliable Level-2 data.

## Mechanical Rule-Respect
**Present and code-verifiable** (the archive's strongest on this axis): ATR trailing stop per trade, R-based
partial exits, and **hard daily/weekly drawdown limits** are implemented in the open source. They are
**proven to exist** but **not proven to hold in live trading** (no track record).

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | NOT REPORTED | — | no track record |
| Maximum Drawdown | NOT REPORTED (hard daily/weekly limits coded, but unproven live) | — | code only |
| Win Rate | NOT REPORTED | — | — |
| Profit Factor | NOT REPORTED | — | — |
| Track Length | None (published 2026-04-06; no live record) | — | — |
| Real vs Demo | N/A (no account) | — | — |

## Backtest Assessment
**None provided.** No backtest report, real-tick study, or out-of-sample data is published on the code page.
Without it, even in-sample behavior is unknown. (A pattern + L2-DOM strategy is also hard to backtest faithfully
because historical DOM data is rarely available — another reason results are absent.)

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No trade-level history exists (the EA has never been shown trading). The coded daily/weekly
DD limits and Kelly sizing are encouraging *by design*, but ROR requires realized Tier 0/1 trade data, which
does not exist. NON-ESTIMABLE ROR **bars Deployable.**

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable from public data** — no realized distribution to size against. The coded `MaxDailyLoss` /
`MaxWeeklyLoss` could *in principle* be set to a firm's limits, but with no live evidence that the EA respects
them under stress, this cannot be recommended for funded capital.

## Cost & Licensing
**Free / open-source** (MQL5 Code Base). No license cost; full source available. (This is also what makes it
the rare EA able to satisfy Alpha Capital's source-code-submission requirement.)

## Community Sentiment
**None yet** — too new (2026-04-06). No independent reviews, no forum teardowns, no user track records. The
absence of complaints is purely a function of newness, not validation.

## Why This Will Probably Fail
1. **Most likely benign explanation:** a thoughtfully-built but **unproven** breakout system whose pattern +
   L2-DOM edge may be weak or non-existent on real spreads/feeds — most carefully-coded retail EAs do not have
   a durable live edge, and this one has shown *no* live edge at all yet.
2. **Prop-server case:** L2 DOM is typically unavailable on prop spot-FX feeds → the EA degrades to its
   tick-volume fallback, which is a different (untested) strategy; pattern breakouts also suffer false breaks
   that the coded DD limits would cap but not prevent.
3. **Variance case:** with no track record, "passes a challenge" is pure speculation; it could equally stall
   or breach on its first regime.
4. **Evidence fragility:** this is the extreme case — **all** performance evidence is missing. The single
   thing that would change the verdict is a **forward/live track record** (≥6 months, real money, inspectable),
   which only forward-testing or the operator can generate — code inspection alone cannot.

## Scores (latent × multiplier/ceiling = adjusted)
best_tier = **TIER4** (no performance evidence); ROR = **NON-ESTIMABLE** → Survival multiplier =
min(MultA_T4 0.12, 0.20) = 0.12. Multiplier A (Tier 4) = 0.12; Multiplier B (Tier 4) = 0.15. **No Gate-B
ceiling** (open source). **No Risk control-evidence cap** (controls are code-verifiable = independently
demonstrated to *exist*), though latent reflects that they are unproven *live*.

| Dimension | Latent | Mult/Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival (30%) | 2 | ×0.12 (ROR cap→0.12) = 0.24 → clamp | 1 |
| Prop-Firm Compliance (20%) | 5 | no Gate-B cap (Conditional all firms: uniqueness/shared) | 5 |
| Risk Management (15%) | 6 | no cap (controls code-verifiable, unproven live) | 6 |
| Challenge-Passing (15%) | 1 | ×0.12 = 0.12 → clamp | 1 |
| Consistency (10%) | 1 | ×0.15 = 0.15 → clamp | 1 |
| Transparency of Results (5%) | 1 | ×0.15 = 0.15 → clamp | 1 |
| Profitability (5%) | 1 | ×0.15 = 0.15 → clamp | 1 |

**Overall** = 0.30·1 + 0.20·5 + 0.15·6 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 1.00 + 0.90 + 0.15 + 0.10 + 0.05 + 0.05 = **2.55 → 2.6 (poor).**

> Note: Transparency-of-**results** scores 1 (no verified results), even though Transparency-of-**logic** is
> the best in the archive (open source) — the dimension measures inspectable *evidence/results*, captured
> instead in mechanism_confidence (High) and the un-capped Compliance/Risk.

## Deployment Verdict
**AVOID · Overall 2.6 (poor).**
**Binding criterion:** **no verified performance evidence of any kind** (brand-new 2026-04-06 open-source
code; no live record, no MQL5 signal, no published backtest) → best_tier TIER4 + ROR NON-ESTIMABLE
(deterministic Avoid). This is a **clean, transparent, prop-designed but entirely unproven** EA — the
opposite failure mode from the disguised-martingale cases. **Prime forward-test candidate:** the one realistic
path to lift it is an inspectable ≥6-month real-money record (which the operator/forward-testing must
generate; web research cannot).

## Similar EAs
- Mechanism cousin to [[the-gold-reaper-mt5]] (breakout + hard SL) but **open-source and not gold-only**.
- Contrast with the disguised-martingale exclusions ([[forex-flex-ea-mt5]], [[quantum-queen-mt5]]): Hon-APS is
  the inverse — verifiably clean mechanism, just no evidence it works.

## Red Flags
- **Zero track record** — no live/backtest/Myfxbook data whatsoever (the binding issue).
- L2-DOM dependence may not transfer to prop spot-FX feeds (degrades to tick-volume fallback).
- Shared open-source code can trip strategy-uniqueness/shared-EA rules at primaries.
- Pattern-recognition + Kelly sizing can be fragile/aggressive if misconfigured; unproven under stress.

## Source Links
- https://www.mql5.com/en/code/71521 — 2026-06-23 — open-source code page (fetched) — not affiliate
- https://mql.robotfx.org/2026/04/metatrader-5-expert-advisor-hon-aps.html — 2026-06-23 — mirror/listing — mixed
- WebSearch discovery + negative-case leads — 2026-06-23

## Analyst Notes
- **FACTS:** Christopher Adie (Adiec7); open-source MQL5 Code Base 2026-04-06; pattern-breakout + L2 order-flow
  + KAMA filter, ATR trailing SL, 1R/2R partials, Kelly sizing, hard daily/weekly DD limits, news filter,
  H1/H4 FX+indices; no grid/martingale (code-confirmed); **no performance data published.**
- **ANALYSIS:** clears Gate A and Gate B (code-verifiable), best code-level risk controls and mechanism
  confidence in the archive, and the only EA able to satisfy Alpha's source-code rule — but TIER4 (no
  evidence) + NON-ESTIMABLE ROR ⇒ Avoid (unproven). Open source fixes transparency/legality, not evidence.
- **ASSUMPTIONS (flagged):** that the L2-DOM edge may not transfer to prop feeds (DOM availability); that a
  shared open-source EA risks uniqueness flags — both reasonable but unconfirmed.

## Future Research Needed
- **Operator action:** forward-test on demo/small-live for ≥6 months (or paper) to generate the missing
  inspectable record; if it shows ≤~6% DD with a real edge, this is a genuine Watchlist candidate (its
  mechanism/legality already clear). Self-modify parameters to address strategy-uniqueness before any funded use.
- If an independent live/Myfxbook record surfaces, re-vet immediately (mechanism already verified).

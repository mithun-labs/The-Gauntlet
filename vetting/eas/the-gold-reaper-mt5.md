[← Index](../README.md) · [Funded-survival](../rankings/funded-survival.md) · [Comparison](../rankings/comparison.md)

# The Gold Reaper MT5
*XAUUSD-only multi-timeframe breakout EA from an accountable vendor, with real risk controls but prop-incompatible ~42% live drawdown and uninspectable evidence — AVOID.*

## At a Glance
| | |
|---|---|
| **Verdict** | ⛔ **AVOID** |
| **Overall** | **2.5 / 10** · poor |
| **Mechanism** | Multi-timeframe breakout (~9 internal strategies), per-trade SL+TP+trailing · confidence Medium · Gate B: publicly described + independently corroborated (partial black box) |
| **Evidence** | ◉ best_tier **T2** · real (per references) but uninspectable this run · track length NOT REPORTED (Myfxbook 403) · NYCServers review |
| **Risk of ruin** | NON-ESTIMABLE |
| **Legality** | FN ⚠️ · FP ⚠️ · 5% ⚠️ · TFT ⚠️ (all Conditional) |
| **Verified perf** | conflicting ~18.31%/mo aggressive; +14.98% total [T3] · max DD ~42% [T2] · track NOT REPORTED |
| **Vendor** | Profalgo Limited — Wim Schrynemakers (identifiable) |

> **Bottom line — binding criterion:** ROR NON-ESTIMABLE and best_tier ≤ TIER2; reinforced by ~42% live max DD (prop-incompatible) and commercial-EA policy limits; prop-preset has no inspectable verified live track.

---
## Profile

## Overview
XAUUSD-only multi-timeframe **breakout** EA (H1) running ~9 internal breakout strategies, with a hard stop loss + take profit + trailing on every trade and an NFP news filter. Marketed "PROP FIRM READY" with downloadable prop setfiles. Survives Gate A (no grid/martingale, corroborated independently), but the inspectable evidence does not support survival of a funded account, and a commercial fully-automated third-party EA runs into firm EA-policy limits.

## Strategy Mechanism
Publicly described + independently corroborated: multi-timeframe **breakout** around support/resistance, "9 different breakout strategies simultaneously," each trade carries a predefined **stop loss**, take profit, and trailing logic; a drawdown-aware lot engine scales size to a configurable max-DD setting. Vendor and an independent review both state **"No grid / No martingale / No hedging."** Closed source — exact entry logic and max simultaneous positions are not public (the "9 internal strategies" are a partial black box), but the no-grid/per-trade-SL claim is corroborated beyond the vendor. → **Survives Gate A.**

## Mechanism Inference Confidence
**Medium.** Breakout-with-hard-SL and no-grid/no-martingale are corroborated by an independent (affiliate-flagged) review, not vendor-only; but the source is closed and the internal multi-strategy entry logic and max-position behavior are not publicly inspectable, and the live drawdown (~42%) is higher than a pure capped-SL breakout would suggest, hinting at simultaneous correlated positions.

## Recommended Instruments
XAUUSD only.

---
## Evidence  *(the basis for every score below — read before the verdict)*

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline return/DD (verified real account, e.g. +14.98% gain / 41.66% max DD, PF 1.08, win 72%) | https://newyorkcityservers.com/blog/the-gold-reaper-review | review | independent-ish (affiliate VPS upsell) | TIER3 reporting on an uninspectable verified account | 2026-06-19 | Medium | Verified Myfxbook accounts exist (search-confirmed) but Myfxbook returned 403 to the fetch tool — could not inspect track length / real-vs-demo / attribution directly |
| Mechanism / risk controls (breakout, SL+TP+trailing every trade, no grid/martingale, NFP filter) | https://www.mql5.com/en/market/product/111357 ; https://newyorkcityservers.com/blog/the-gold-reaper-review | vendor + review | vendor + independent-ish | TIER3 | 2026-06-19 | Medium-High | per-trade SL corroborated by independent review |
| Prop-firm success claim ("users report passing challenges" with prop preset) | https://newyorkcityservers.com/blog/the-gold-reaper-review | review | affiliate | TIER4 (no Tier-0 funded evidence) | 2026-06-19 | Low | no verifiable funded-account proof |
| Negative-case (live DD 30–41.66%, one report -60%; live << backtest) | https://newyorkcityservers.com/blog/the-gold-reaper-review + search leads | review | independent-ish | TIER3 | 2026-06-19 | Medium | DD figures conflict across settings/accounts |

## Source Reliability Assessment
source_count = 3 fetched (MQL5 vendor listing; NYCServers review; MQL5 top-list discovery) · independent_source_count = 1 (NYCServers — affiliate-flagged) · affiliate_source_count = 1 · Multiple verified Myfxbook accounts were located via search (strueli "Live/Moderate/Extreme/V3.0", RichSociety, PKFXAustralia, Forex_EAs) but **Myfxbook 403'd the fetch tool**, so none could be inspected as primary evidence. **Best evidence found:** an independently-reported verified real-money Myfxbook account — but uninspectable this run, and the reported headline DD (~42%) is prop-incompatible.

## Unverified Claims
- That any verified Myfxbook record is ≥6 months, real-money, and **attributable to the purchasable product at default (or prop-preset) settings** — uninspectable this run; multiple third-party accounts run different risk presets (Moderate/Extreme/V3.0) with divergent DD.
- That the EA "passes" prop challenges — no Tier-0 funded evidence; Tier 4.
- That the prop-preset achieves low DD live — the inspectable/reported verified records reflect higher-risk settings (~42% DD); the prop-preset's live survival is unproven.
- Exact max simultaneous positions and internal entry logic — not public.

## Evidence & Performance

| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | conflicting (one account ~18.31%/mo aggressive; another +14.98% total) | TIER3 | NYCServers review / search leads |
| Maximum Drawdown | ~41.66% live (one report -60%; backtest ~12%) | TIER3 | NYCServers review |
| Win Rate | ~72% | TIER3 | NYCServers review |
| Profit Factor | ~1.08 | TIER3 | NYCServers review |
| Track Length | NOT REPORTED (uninspectable — Myfxbook 403) | — | — |
| Real vs Demo | Real (per references) but uninspectable this run | TIER3 | search/review |

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** ROR is estimable only from public **Tier 0/1 trade-level** history. The verified Myfxbook trade history could not be fetched (403), figures conflict across multiple third-party accounts/settings, and none is attributable to the prop-preset at default settings. No Tier 0/1 trade-level distribution is available → ROR NON-ESTIMABLE (a negative finding for Survival). Indicatively, a ~42% live max DD vs a ~6–10% firm max-DD limit implies near-certain limit violation at the aggressive settings, while the low-risk prop-preset has no inspectable live record.

## Backtest Assessment
Public claim only; backtest DD (~12%) is far below live DD (~42%), a classic backtest-vs-live optimism gap. Cannot confirm real-tick data, modeled costs, or multi-regime/OOS testing from a fetched primary report this run → treat as near-worthless for an all-weather/prop-survival claim.

---
## Eligibility & compliance

## Eligibility Gates
- **Gate A (banned mechanism):** PASS — breakout with hard per-trade SL; no grid/martingale/hedging, independently corroborated.
- **Gate B (mechanism transparency):** Mechanism is publicly described and independently corroborated (not a pure black box) → Gate-B ceilings (Compliance ≤5, Risk ≤4) **not** triggered; mechanism_confidence Medium.
- **Gate C (per-firm legality):** see below. Not Prohibited at all three, so no Gate-C auto-Avoid.

## Per-Firm Legality Verdict
- **Funding Pips — Conditional (rulebook v1, EA-policy PRIMARY-confirmed).** A fully-automated **third-party commercial** EA is **not permitted** on standard evaluations (third-party EAs allowed only as trade/risk manager); permitted only on the 1K Instant account. The strategy mechanism itself (breakout, SL) is not a banned behavior, but the product type is barred on standard programs → Conditional/effectively Prohibited on standard evals.
- **The Funded Trader — Conditional (rulebook v1).** Primary terms bar abusive/HFT automation (this is H1 breakout, not HFT) but independent guidance indicates commercially-available pre-programmed automated EAs are restricted / must have unique non-masked parameters → Conditional (depends on UNCONFIRMED commercial-EA detail).
- **FundedNext — Conditional (rulebook v1, SECONDARY/UNCONFIRMED).** EAs reported allowed on MT5 and breakout is not a banned mechanism, but the entire FundedNext rulebook is UNCONFIRMED (primary site 503 this run) → Conditional.
- **The 5%ers — Conditional (rulebook v1, added 2026-06-19).** EAs are allowed and breakout-with-SL is not a banned mechanism, but The 5%ers' standards bar "shared third-party EA strategies" and require the trader to "understand/control the internal logic" — hostile to a closed-source, off-the-shelf commercial EA. Mechanism legal; product type contested → Conditional. (Added because The 5%ers became a PRIMARY firm in CLAUDE.md v2.2; original vetting predates it.)
- **(Reference — non-gating) Alpha Capital Group — Prohibited (rulebook v1).** Requires .MQ5 source-code submission + written pre-approval; a closed-source commercial EA cannot comply.
- **(Reference — non-gating) Goat Funded Trader — Prohibited (rulebook v1).** Bans off-the-shelf / commercial challenge-passing EAs (stricter reading of conflicting sources).

## Rule-Violation Flags
- High live drawdown (~42%) would breach every target firm's max-overall-DD limit (~6–10%) at the settings that produced the verified record. (DD-definition mismatch caveat: Myfxbook DD ≠ firm balance/equity DD, but a 42% gap dwarfs any reconciliation.)
- Commercial fully-automated third-party EA conflicts with Funding Pips' standard-program EA policy.

## Mechanical Rule-Respect
Hard per-trade **stop loss + take profit + trailing** are vendor-documented and independently referenced; a configurable max-DD lot engine and NFP news filter are documented. However, **a hard account-level daily-loss / equity stop is NOT documented** — drawdown is managed via lot scaling, and the live ~42% DD shows the controls do not cap account drawdown to prop-relevant levels.

## Community Sentiment
Independent (affiliate-flagged) coverage is mixed-to-cautionary: legitimate breakout mechanism and accountable developer, but "substantial," "30–40%," and up to "-60%" live drawdowns; live performance materially below backtest. Multiple third-party Myfxbook accounts at different risk presets show wide DD dispersion. Negative-case search ("blown account / drawdown / losing") returned substantive DD-risk reports — recorded.

---
## Verdict

## Why This Will Probably Fail
1. **Most likely benign explanation:** a genuine breakout EA whose edge is thin (PF ~1.08) and whose drawdown is large (~42% live); the high MQL5 rating and "prop ready" label reflect marketing and calm-period results, not funded-account survival.
2. **Prop-server case:** on a prop firm's feed/spread with a ~6–10% max-DD limit and a daily-DD limit, the settings that produced the verified record would breach quickly; the lower-risk prop-preset that might stay within limits has **no inspectable verified live track**, so its survival is unproven.
3. **Variance case:** could pass an evaluation in a calm breakout-friendly stretch, then surrender it during a choppy/news regime where 9 simultaneous breakout strategies cluster losses — passing and surviving are different problems.
4. **Evidence fragility:** essentially everything inspectable this run is Tier 3 (affiliate review) or Tier 4 (prop "passing" claims). The single piece of evidence that would most change the verdict — an inspectable, ≥6-month, real-money Myfxbook record of the **prop-preset at default settings** with trade-level history — I do not have (Myfxbook 403).

## Scores

best_tier = **TIER2** (a verified real account demonstrably exists per multiple independent references, but is uninspectable, attribution-ambiguous, and conflicting — caveated, so capped at Tier 2, not Tier 1). Multiplier A(Tier2)=0.45; Multiplier B(Tier2)=0.60; **ROR NON-ESTIMABLE → Survival multiplier = min(0.45, 0.20) = 0.20.**

| Dimension | Weight | Latent | × Mult / Ceiling | Adjusted | Contribution |
|-----------|:------:|:------:|:----------------:|:--------:|:------------:|
| Funded-Account Survival | 30% | 3 | ×0.20 (ROR cap) = 0.6 → round | 1 | 0.30 |
| Prop-Firm Compliance | 20% | 4 | mechanism-based, no Gate-B ceiling | 4 | 0.80 |
| Risk Management | 15% | 4 | control-evidence ceiling ≤5 (vendor-documented) | 4 | 0.60 |
| Challenge-Passing | 15% | 4 | ×0.45 = 1.8 → round | 2 | 0.30 |
| Consistency | 10% | 3 | ×0.60 = 1.8 → round | 2 | 0.20 |
| Transparency | 5% | 5 | ×0.60 = 3.0 | 3 | 0.15 |
| Profitability | 5% | 4 | ×0.60 = 2.4 → round | 2 | 0.10 |
| **Overall** | | | | | **2.5** |

Overall = 0.30·1 + 0.20·4 + 0.15·4 + 0.15·2 + 0.10·2 + 0.05·3 + 0.05·2 = 0.30 + 0.80 + 0.60 + 0.30 + 0.20 + 0.15 + 0.10 = **2.45 → 2.5** (half-up, one decimal).

*Band: poor (<4.0). Surface only the adjusted Overall; latents shown for audit.*

## Deployment Verdict
**AVOID.** Binding criterion: **ROR NON-ESTIMABLE and best_tier ≤ TIER2** (deterministic Avoid trigger), reinforced by an independently-reported ~42% live max drawdown that is incompatible with all three firms' max-DD limits, and by a commercial fully-automated EA conflicting with Funding Pips' standard-program EA policy. This is nonetheless the **strongest candidate of the pass** (accountable vendor, real risk controls, genuine verified records exist) — a candidate to **re-vet** if an inspectable ≥6-month real-money verified record of the prop-preset at default settings becomes available.

## Similar EAs
Other XAUUSD breakout/scalper EAs (e.g. Goldwave, TwisterPro Scalper) — to be vetted; different mechanism family from the grid EAs (Quantum Queen).

## Red Flags
- Live drawdown (~42%, up to -60% on aggressive presets) far above backtest (~12%).
- Thin edge (PF ~1.08).
- Verified records uninspectable this run (Myfxbook 403); attribution to default/prop settings unclear.
- "Prop firm ready" marketing without any Tier-0 funded-account proof.

<details>
<summary><strong>Appendix — full audit trail</strong> (vendor, compatibility, sizing, cost, sources, notes)</summary>

## Vendor / Developer
**Profalgo Limited — Wim Schrynemakers**, an identifiable, accountable developer (publishing EAs since ~2005, established MQL5 author profile). Not anonymous — a positive on accountability.

## MT5 Compatibility & Dependencies (publicly documented)
MT5; XAUUSD (gold) only; H1; hedging not required; NFP/news filter; VPS recommended; recommended deposit $600 min, developer suggests $2,500–$3,000 for conservative risk. Price $849 (rentals $399–$599).

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** Inspectable public data is insufficient and conflicting to size risk responsibly; the prop-preset's live behavior is unverified. Sizing would be fabrication.

## Cost & Licensing
$849 one-time (MQL5); rentals $399–$599; standard MQL5 license/activation limits; prop setfiles provided by vendor.

## Source Links
| URL | Retrieved | Affiliate? |
|-----|-----------|-----------|
| https://www.mql5.com/en/market/product/111357 | 2026-06-19 04:05 UTC | no (vendor) |
| https://newyorkcityservers.com/blog/the-gold-reaper-review | 2026-06-19 04:05 UTC | yes (VPS upsell) |
| (located, not fetchable — Myfxbook 403) https://www.myfxbook.com/members/strueli/gold-reaper-moderate/10686236 | 2026-06-19 04:07 UTC | n/a |

## Analyst Notes
- **FACTS:** vendor + independent review state breakout, per-trade SL, no grid/martingale; independent review reports a verified real account with ~42% max DD, PF ~1.08; multiple verified Myfxbook accounts exist at different presets.
- **ANALYSIS:** survives Gate A but fails the evidence and survival bars; the verified DD is prop-incompatible and the prop-preset is unproven live; firm EA-policies further constrain legality to Conditional.
- **ASSUMPTIONS:** best_tier set to TIER2 (verified account exists but uninspectable/attribution-ambiguous) rather than TIER1; if the verified prop-preset record were inspectable and clean ≥6mo, this could rise to Watchlist.

## Future Research Needed
Operator to supply (or a future run to fetch when Myfxbook is reachable) an inspectable ≥6-month real-money Myfxbook/FXBlue record of **the prop-preset at default settings** with public trade-level history, to re-estimate ROR and reconsider Watchlist; and a primary FundedNext rulebook to firm up the FundedNext legality verdict.

</details>

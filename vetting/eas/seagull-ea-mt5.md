# Seagull EA (MT5)

## Overview
Seagull EA is a closed-source, fully-automated MT5 Expert Advisor by **TheDailyFX** (thedailyfx.uk),
marketed as a "strict trend-following" system with "dynamic risk protection" and **"no Grid, no
Martingale, no Hedging."** It trades the **AUDCAD** cross (originally **NZDCAD**) on **M1 / M15 / M30**,
is distributed **free via a Pepperstone broker partnership** (50% off at a $1,000 deposit, 100% free at
a $5,000 deposit), and claims a verified live Myfxbook record since early 2021 (+595.65% gain / 20.51%
max drawdown, per a Myfxbook summary surfaced in search).

> **EVIDENCE-ACCESS CAVEAT (decisive for this verdict).** Every Seagull EA primary/independent page —
> the vendor site (`thedailyfx.uk/seagull-ea`, returned an **empty body**), both Myfxbook accounts
> (`TheDailyFX/...`, `LinoCapital/...`, **HTTP 403**), the FXStreet "education" post (**403**), and the
> Myfxbook community thread (**403**) — was **uninspectable** to the fetch tool (the same bot-protection
> block seen across all prior runs). The profile below is reconstructed from **WebSearch summary leads**,
> which per HARD RULE 2 are **leads, not fetched sources.** No trade-level history could be inspected.
> This caps the evidence at **Tier 3** and is itself a core reason for the Avoid verdict.

## Vendor / Developer
**TheDailyFX** (thedailyfx.uk; also thedailyfx.com), a UK-styled automated-trading vendor that says it
was **founded in 2015** with a team of "75+ years collective" trading experience; contact
`info@thedailyfx.uk`. **Semi-accountable** — a named brand with a website and contact, but no named
individual developer and no regulatory identity stated. The business model is a **broker
introducing-broker (IB) / CPA partnership with Pepperstone**, not EA sales: the EA is "free" because the
vendor earns commission on the client's trading volume/spreads. **This is a red flag** — vendor revenue
scales with *trade volume*, not with the EA being *profitable for the user.*

## MT5 Compatibility & Dependencies (publicly documented only)
- Platform: MT5. Pair: **AUDCAD** (formerly NZDCAD). Timeframes: **M1 / M15 / M30**.
- Distribution tied to a **Pepperstone** live account (raw-spread/Razor account implied by a scalping
  cross strategy); edge is therefore **broker- and spread-specific** to Pepperstone's execution.
- Recommended deposit ladder is a *broker-deposit* gate ($1,000 / $5,000), not a documented EA capital
  requirement; no documented VPS/GMT requirement surfaced.

## Strategy Mechanism (publicly documented / inferable; Gate B status)
**FACTS (vendor-stated, via search leads):** "follow the major trend and/or the divergence of higher
timeframes and look to entry on the lower time frames. If the market is still moving forward, Seagull EA
will look to **add some limited positions in the same direction**." Trades a tight, mean-reverting
commodity cross (NZDCAD/AUDCAD) which "after 2016 ... shows strong properties of mean reversion." "Not a
night scalper; the orders are almost averaged within 24 hours" (i.e. ~24h average hold). Works on fixed
or balance-scaled lot. Markets itself as **no grid / no martingale / no hedging.**

**ANALYSIS:** the marketing label ("trend-following") is in tension with the design (M1 entries on
AUDCAD/NZDCAD — the textbook *mean-reverting* commodity crosses that grid/reversion-basket EAs favour).
The most likely real mechanism is **multi-position pyramiding into directional continuation on a
mean-reverting cross**, held ~24h. Critically, the vendor describes adding positions **"in the same
direction" while "the market is still moving forward"** — i.e. adding to *winners* (pyramiding), **not**
averaging *down* into losers. On the available evidence that is **not** martingale/grid, so it
**survives Gate A**. The ~24h average hold also **rules out tick-scalping/HFT.** But it is a
**multi-position system with no publicly documented per-position hard stop loss**, which is a material
risk-control gap even if the mechanism is not banned.

## Mechanism Inference Confidence
**Low.** The vendor's self-description (adds-to-trend, ~24h hold, no grid/martingale) is the only
mechanism source; it could not be corroborated by any independent teardown or by inspecting the trade
history (all pages 403/empty). The trend-following label vs. the AUDCAD/NZDCAD-M1 reversion design is an
unresolved contradiction. Whether the "limited positions" can ever scale against an adverse excursion
(which would flip it to Gate-A martingale/grid) **cannot be confirmed or ruled out** without a teardown
or trade-level data — so no benefit of the doubt is extended on risk.

## Recommended Instruments
AUDCAD (vendor-default; formerly NZDCAD). No other instruments documented.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| Headline +595.65% gain / 20.51% max DD, real-money since 2021 | myfxbook.com/members/TheDailyFX/seagull-ea-mt5/11305553 | vendor Myfxbook (via search summary) | vendor | TIER3 | 2026-06-22 | Low | Page 403 — uninspectable; figure from a Myfxbook search summary, not a fetched verified page |
| Mechanism: trend-add multi-position, ~24h hold, no grid/martingale/hedging | thedailyfx.uk/seagull-ea + FXStreet post (via search) | vendor / sponsored | vendor | TIER4 | 2026-06-22 | Low | Vendor self-description; vendor page empty body, FXStreet 403 — surfaced only via search leads |
| Prop-firm compatibility ("compatible with prop firm challenges") | thedailyfx.uk / listicles (via search) | vendor / affiliate | vendor/affiliate | TIER4 | 2026-06-22 | Low | No Tier-0 funded evidence; ~20.5% DD contradicts prop limits |
| Free via Pepperstone IB ($1k 50% / $5k 100%) | search: vendor + broker-partner | vendor | vendor | TIER4 | 2026-06-22 | Medium | CPA model — vendor earns on volume, not user profit |
| Negative-case evidence | WebSearch "scam/blown/refund/losing" | search aggregate | n/a | n/a | 2026-06-22 | Low | **No Seagull-specific** scam/blowup/refund reports surfaced; also no inspectable independent praise |

## Source Reliability Assessment
- **source_count: 6** (vendor site, vendor Myfxbook account + community thread, FXStreet sponsored post,
  cheaperforex listicle, Pepperstone broker-partner references) · **independent_source_count: 1**
  (cheaperforex listicle was fetched independently — but it does **not** list Seagull EA; a third-party
  `LinoCapital` Myfxbook account exists but is 403/uninspectable) · **affiliate_source_count: 3** (vendor
  site, FXStreet sponsored "education" post, broker-CPA/listicle channel).
- **Best evidence found:** Tier 3 — a *claimed* multi-year verified Myfxbook real-money record that
  could **not be inspected** (403). **No inspectable evidence above Tier 3.** No independent corroboration
  of performance; the FXStreet post is a vendor-submitted/sponsored placement, not journalism.

## Unverified Claims
- The +595.65% gain / 20.51% max DD and the "verified live since 2021 / no over-optimization" claims —
  all rest on an uninspectable vendor Myfxbook account.
- "No grid, no martingale, no hedging" and "dynamic risk protection" — vendor assertions; no documented
  per-trade hard stop loss; no third-party teardown.
- "Compatible with prop firm challenges" — no Tier-0 funded-account evidence; the ~20.5% claimed DD is
  itself prop-incompatible at full risk.
- Whether the "add limited positions in the same direction" logic can ever average **against** an adverse
  move (which would be Gate-A martingale/grid) — unverifiable from public sources.

## Eligibility Gates
- **Gate A — PASS (survives).** On the vendor's own description it adds to *winners* (pyramiding into
  continuation), not averaging down; ~24h average hold rules out tick-scalping/HFT. No decisive
  banned-mechanism signature. *Caveat:* if an independent teardown ever showed averaging-down/recovery
  behaviour, this flips to **Excluded** — flagged in Future Research.
- **Gate B — mechanism NOT publicly verifiable → ceilings APPLY.** Closed source, no third-party
  teardown, no settings/risk-control documentation, trade history uninspectable (403), and mechanism
  inference only **Low**. Apply **Compliance ≤ 5, Risk ≤ 4, Deployment ceiling = Watchlist.**
- **Gate C — per-firm legality** (mechanism legal but a closed-source commercial third-party EA):
  - FundedNext: **Permitted** (EA-friendly firm) — *rulebook v1 PROVISIONAL/secondary (primary 503).*
  - Funding Pips: **Conditional** — third-party EA allowed **only as a trade/risk manager**; Seagull is a
    directional alpha EA, so for the off-the-shelf product this leans **Prohibited** (viable only via the
    self-developed/1K-Instant exceptions).
  - The 5%ers: **Conditional** — trader must "control the EA's internal logic"; closed-source.
  - The Funded Trader: **Conditional** — standard EAs permitted, but the multi-position "add in the same
    direction" logic brushes the "substantially larger sizes / grossly overleveraged" prohibition; numeric
    rules UNCONFIRMED.

## Per-Firm Legality Verdict
| Firm | Verdict | Rulebook | Basis |
|------|---------|----------|-------|
| FundedNext (primary) | Permitted | v1 (PROVISIONAL) | EA-permissive; mechanism not banned. Rulebook secondary — cannot clear Deployable. |
| Funding Pips (primary) | Conditional | v1 | Third-party EA allowed only as trade/risk manager; off-the-shelf directional EA leans Prohibited |
| The 5%ers (primary) | Conditional | v1 | Control-of-internal-logic requirement; closed source |
| The Funded Trader (primary) | Conditional | v1 | Standard EAs OK but multi-position add risks overleverage clause; numerics UNCONFIRMED |
| Alpha Capital (reference) | Prohibited | v1 | Mandatory .MQ5 source-code submission; closed-source EA cannot comply (non-gating) |
| Goat Funded Trader (reference) | Prohibited | v1 | Off-the-shelf/commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **Drawdown:** claimed ~20.5% max DD exceeds every primary firm's max-overall limit (10% absolute at The
  5%ers; 6–10% at Funding Pips) at full risk — daily-DD breach likely on a multi-position pyramiding day.
- **Multi-position sizing:** "adds limited positions in the same direction" can stack exposure — overleverage
  / max-position risk against TFT's sizing clause.
- **Broker dependence:** edge is Pepperstone-spread-specific; a prop firm's own feed/spread/commission and
  DD calculation may erase it (the standing pattern across this archive).

## Mechanical Rule-Respect
**NOT REPORTED / vendor-claimed only.** No publicly documented hard equity-stop, daily-loss-stop, or
max-position cap. "Dynamic risk protection" is marketing with no inspectable specifics; no per-trade hard
SL is documented for a multi-position system.

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | NOT REPORTED (≈ implied from +595.65% over ~5yr, not stated per-month) | TIER3 | vendor Myfxbook (uninspectable) |
| Maximum Drawdown | ~20.51% (claimed) | TIER3 | vendor Myfxbook summary (uninspectable) |
| Win Rate | NOT REPORTED | — | — |
| Profit Factor | NOT REPORTED | — | — |
| Track Length | ~5 years claimed (since early 2021) | TIER3 | vendor Myfxbook summary (uninspectable) |
| Real vs Demo | Claimed real-money | TIER3 | vendor Myfxbook summary (uninspectable) |

## Backtest Assessment
Vendor claims a "Tickdata backtest from 2006" with "no over-optimization." **Near-worthless as evidence:**
not reproduced, not inspected, costs/slippage/multi-regime/OOS unverified, and a backtest from 2006 on a
pair whose behaviour the vendor admits *changed after 2016* (tighter range / stronger mean reversion) is a
regime-mismatch red flag. Public backtest = claim, not proof.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No inspectable Tier 0/1 trade-level history (Myfxbook 403). ROR cannot be computed
from a headline gain/DD pair or a vendor backtest. **DD-definition mismatch caveat:** the ~20.51%
Myfxbook DD uses Myfxbook's own method and is not restatable under any firm's daily/overall rule without
trade-level data. Per the ROR cap, Survival multiplier is reduced to min(A, 0.20). NON-ESTIMABLE ROR
**bars any Deployable verdict.**

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** Public data does not support sizing: no per-trade SL, no trade-level distribution, no
inspectable equity curve. Any sizing recommendation would be fabricated. A ~20.5%-DD multi-position
strategy cannot be safely fitted under a 5%-daily / 10%-overall envelope without trade-level data that
does not exist publicly.

## Cost & Licensing
**"Free" via Pepperstone IB/CPA** — 50% off at a $1,000 Pepperstone deposit, 100% free at a $5,000
deposit. No standalone license sale surfaced. The CPA model is the core commercial red flag: the vendor
is paid on the user's **trading volume/spreads**, aligning vendor incentives with *activity*, not user
profitability — and tying the user to one broker.

## Community Sentiment
**Independent sentiment is thin and uninspectable.** The mandatory negative-case search (`scam`, `blown
account`, `refund`, `losing`) surfaced **no Seagull-specific** complaints — but also no inspectable
independent praise; the visible positive quotes ("no martingale gambling… long-term stability is
amazing") are on the vendor's own Myfxbook review page (403). Absence of complaints on a low-profile,
free-via-broker EA is weak signal, not exoneration. cheaperforex's 2026 listicle (fetched) does **not**
list Seagull among its top 10 — i.e. it lacks the independent third-party coverage its marketing implies.

## Why This Will Probably Fail
1. **Most likely benign explanation:** a genuine but modest mean-reversion-on-a-cross edge that is
   **broker/spread-specific to Pepperstone** and **degrades on a prop server** (wider AUDCAD spreads,
   different fills, the firm's own DD calc). A +595%/5yr curve compounded on a free CPA account flatters a
   thin per-trade edge.
2. **Prop-server case:** a multi-position pyramiding system with ~20.5% historical DD, run under a 5%
   daily / 10% overall envelope, trips a limit on its first clustered drawdown day; AUDCAD spread/commission
   on the prop feed likely erases the small reversion edge entirely.
3. **Variance case:** even if it clears an evaluation in a calm range, the "add positions in the same
   direction" logic concentrates risk exactly when a cross breaks its range — the funded account is where
   that tail shows up.
4. **Evidence fragility:** essentially **everything** rests on Tier 3/4 — an uninspectable vendor Myfxbook
   account and vendor self-description. The single piece of evidence that would most change the verdict —
   an **inspectable, independent, trade-level funded or ≥6-month verified record showing a real per-trade
   hard stop and DD restated under a firm's rule** — does not exist publicly, and I do not have it.

## Scores (latent × multiplier/ceiling = adjusted)
best_tier = **TIER3**; ROR = **NON-ESTIMABLE** → Survival multiplier = min(MultA_T3 0.25, 0.20) = 0.20.
Multiplier A (Tier 3) = 0.25; Multiplier B (Tier 3) = 0.30. Gate B: Compliance ≤ 5, Risk ≤ 4. Risk
control-evidence ceiling: controls claimed without documentation → Risk ≤ 3 (lowest applies).

| Dimension | Latent | Mult/Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival (30%) | 2 | ×0.20 (ROR cap) = 0.40 → clamp | 1 |
| Prop-Firm Compliance (20%) | 5 | min(5, GateB 5) | 5 |
| Risk Management (15%) | 3 | min(3, ctrl-ceiling 3, GateB 4) | 3 |
| Challenge-Passing (15%) | 2 | ×0.25 = 0.50 → round-half-up | 1 |
| Consistency (10%) | 3 | ×0.30 = 0.90 → round | 1 |
| Transparency (5%) | 3 | ×0.30 = 0.90 → round | 1 |
| Profitability (5%) | 3 | ×0.30 = 0.90 → round | 1 |

**Overall** = 0.30·1 + 0.20·5 + 0.15·3 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 1.00 + 0.45 + 0.15 + 0.10 + 0.05 + 0.05 = **2.10 → 2.1 (poor).**

## Deployment Verdict
**AVOID · Overall 2.1 (poor).**
**Binding criterion:** headline return+DD evidence is **Tier 3** (no inspectable independent verification —
all pages 403/empty) **AND** ROR **NON-ESTIMABLE** with best_tier ≤ Tier 2 — a deterministic Avoid.
Reinforced by: ~20.5% claimed max DD (prop-incompatible); a multi-position add-to-trend mechanism with
**no documented per-trade hard stop** (Gate B + Risk control-evidence ceiling); and a **broker-CPA "free
with $5k deposit"** distribution model that rewards trade volume over user profitability.

## Similar EAs
- [[night-hunter-pro]] — ValeryTrading night-scalp mean-reversion on FX crosses (same *cross-reversion*
  family; different vendor; Night Hunter is a night scalp vs Seagull's ~24h-hold trend-add).
- Evening Scalper Pro (queued-candidate family) — another low-volatility cross-reversion scalper.
- Not a duplicate: different vendor (TheDailyFX vs ValeryTrading) and distinct add-to-trend pyramiding
  logic.

## Red Flags
- Broker-CPA "free with deposit" model → vendor paid on volume, not user profit; broker lock-in.
- Closed source + all evidence uninspectable (403/empty) + mechanism confidence Low.
- Marketing/design contradiction: "trend-following" on AUDCAD/NZDCAD M1 (mean-reverting crosses).
- Multi-position "adds in the same direction" with no documented hard stop loss.
- ~20.5% max DD is prop-incompatible; FXStreet "review" is a sponsored vendor placement.

## Source Links
- https://www.myfxbook.com/members/TheDailyFX/seagull-ea-mt5/11305553 — 2026-06-22 — vendor Myfxbook (403, uninspectable) — affiliate(vendor)
- https://www.myfxbook.com/members/LinoCapital/seagull-ea/10823424 — 2026-06-22 — third-party Myfxbook (403) — independent(uninspectable)
- https://thedailyfx.uk/seagull-ea/ — 2026-06-22 — vendor page (empty body) — affiliate(vendor)
- https://www.fxstreet.com/education/presenting-seagull-ea-fully-automated-trading-system-202406051510 — 2026-06-22 — sponsored vendor post (403) — affiliate(sponsored)
- https://cheaperforex.com/best-mt5-expert-advisors-2026/ — 2026-06-22 — listicle (fetched; does not list Seagull) — affiliate
- WebSearch lead aggregations (mechanism, CPA model, negative case) — 2026-06-22 — leads only

## Analyst Notes
- **FACTS:** AUDCAD/NZDCAD, M1/M15/M30, ~24h hold, adds positions in trend direction, free via Pepperstone
  IB ($1k/$5k), claimed +595.65%/20.51%DD Myfxbook since 2021, vendor TheDailyFX since 2015. (All via
  search leads; underlying pages 403/empty.)
- **ANALYSIS:** real mechanism is likely cross-reversion pyramiding mislabeled "trend-following"; edge is
  broker-specific; survives Gate A (adds to winners, ~24h hold) but Gate B applies (uninspectable closed
  box) and Risk controls are undocumented; Tier-3 uninspectable evidence + NON-ESTIMABLE ROR ⇒ Avoid.
- **ASSUMPTIONS (flagged):** that the "add in same direction" logic does not average *down* (if it does,
  this is a Gate-A exclusion) — unverifiable; that the Myfxbook account is real-money as claimed —
  unverifiable.

## Future Research Needed
- If outbound access to Myfxbook/FXStreet/vendor is ever allow-listed, inspect the live trade-level record:
  confirm real-money, per-trade hard SL presence, trade count/hold-time distribution, and whether positions
  ever average **against** adverse moves (Gate-A re-test). A clean, inspectable ≥6-month low-DD record could
  lift this from Avoid toward Watchlist; evidence of averaging-down would move it to Excluded.
- Operator could supply funded-account statements to test the Deployable path (gate 8) — unlikely given the
  prop-incompatible DD and broker-CPA dependence.

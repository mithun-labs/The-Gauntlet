# Apex Drawdown Zero EA (MT5)

## Overview
Apex Drawdown Zero is a closed-source (.ex5) MT5 Expert Advisor by **Tshivhidzo Moss Mbedzi**, marketed as
a capital-preservation **XAUUSD M15 Asian-session range-breakout scalper** that opens **≤1 trade/day**,
applies a **fixed stop-loss to every trade**, and **"explicitly avoids martingale, grid trading, and
position averaging."** Its headline claim is an extraordinary **+106.69% over 18+ months with a 0.39%
maximum drawdown** (profit factor 3.56, recovery factor 5.89, net profit $242,287.10). Priced ~$697 with
phased price increases; also circulating via group-buy sites.

> **EVIDENCE-ACCESS + PLAUSIBILITY CAVEAT (decisive for this verdict).** The independent review (The Forex
> Geek) returned an **empty body**; the vendor MQL5 promo blogs and group-buy listings were reachable only
> as **search leads** (HARD RULE 2: leads, not fetched sources); the "verified Myfxbook" record itself is
> **uninspectable** (Myfxbook 403 across all runs). Separately, a **0.39% max DD over 18 months is
> internally incompatible** with the disclosed mechanism: a real hard-SL range-breakout scalper
> necessarily suffers losing-breakout streaks, which a single ~0.4% peak-to-trough cannot absorb. The
> claim therefore signals **curve-fit/demo presented as "live," or an undisclosed recovery/loss-management
> mode** — neither of which can be ruled out without trade-level data. Both factors cap evidence at
> **Tier 3** and drive the Avoid verdict.

## Vendor / Developer
**Tshivhidzo Moss Mbedzi** — a named, identifiable MQL5 author (accountable). Distribution is direct sale
(~$697, "price rises as allocation fills" urgency marketing) plus **group-buy / pirated-adjacent listings**
(eafxstore, ecomforex) and heavy **vendor-authored MQL5 blog promotion** ("Unlock Consistent Profits…",
"Set Manual: 1000 USD Monthly Growth"). The marketing ecosystem is vendor- and affiliate-saturated.

## MT5 Compatibility & Dependencies (publicly documented only)
- Platform: MT5 only; supplied as **.ex5** (closed binary). Instrument: **XAUUSD** only. Timeframe: **M15**.
- Operates in a fixed window — **Asian session 02:00–06:00 server time** (server-time/GMT-offset dependent).
- Automatic lot sizing by fixed risk-per-trade. No documented VPS/broker requirement surfaced.

## Strategy Mechanism (publicly documented / inferable; Gate B status)
**FACTS (vendor + review-site stated, via search leads):** range-breakout scalp; during 02:00–06:00 it
identifies a low-volatility range and trades the breakout; **≤1 trade/day**; **fixed SL on every trade**;
automatic lot by fixed risk %; **"avoids martingale, grid, and position averaging."**

**ANALYSIS:** the *described* mechanism is a coherent, non-banned strategy and would **survive Gate A**. The
problem is not the description but its **inconsistency with the headline metrics.** Range-breakout systems
on gold have many **false breakouts** (low-ish win rates with the edge in payoff), so a genuine hard-SL
breakout scalper *must* show recurring small drawdowns and occasional losing clusters — a **0.39% max DD
over 18 months is not achievable** for such a system taking real stops. The realistic explanations are:
(a) the curve is a **backtest/optimized or demo** result mislabeled "live"; (b) the period is **curve-fit**
to a calm gold window; or (c) realized DD is suppressed by an **undisclosed mechanism** (very wide/virtual
stops held until recovery, or averaging) that the marketing denies. None can be confirmed or excluded from
public data, so **no benefit of the doubt** is extended (HARD RULE 6).

## Mechanism Inference Confidence
**Low.** Multiple sources agree on the breakout-with-fixed-SL story, but the headline metrics directly
contradict it, so I cannot be confident the disclosed mechanism is the *complete* one. The contradiction is
itself evidence the public picture may be incomplete (a possible hidden loss-management/recovery mode).

## Recommended Instruments
XAUUSD (only). M15, Asian session.

## Evidence Matrix

| Claim | Source URL | Source Type | Independence | Evidence Tier | Retrieved Date | Confidence | Notes |
|-------|------------|-------------|--------------|---------------|----------------|------------|-------|
| +106.69% / 0.39% max DD / PF 3.56 over 18mo "verified Myfxbook live" | (vendor Myfxbook, via fxroboteasy/blogs) | vendor / aggregator | vendor | TIER3 | 2026-06-22 | Low | Myfxbook 403 — uninspectable; real-vs-demo unconfirmed; metric implausible for the disclosed mechanism |
| Mechanism: Asian breakout, ≤1 trade/day, fixed SL, no grid/martingale | mql5 blogs / theforexgeek / fxroboteasy (via search) | vendor / review | vendor + review | TIER4 | 2026-06-22 | Medium | Consistently reported; review page empty body, blogs are vendor-authored |
| Prop-firm suitability (low-DD → "perfect for prop accounts") | listicles (via search) | affiliate | affiliate | TIER4 | 2026-06-22 | Low | No Tier-0 funded evidence; suitability rests on the implausible DD |
| Developer = Tshivhidzo Moss Mbedzi | search (vettedpropfirms/fxroboteasy) | aggregator | independent-ish | TIER3 | 2026-06-22 | Medium | Named, accountable author |
| Negative-case evidence | WebSearch "scam/blown/curve fit/demo" | search aggregate | n/a | n/a | 2026-06-22 | Low | **No** scam/blowup reports surfaced — but it is a **new (2026) EA**, so absence is weak signal, not exoneration |

## Source Reliability Assessment
- **source_count: 5** (vendor MQL5 promo blog, eafxstore group-buy listing, fxroboteasy aggregator,
  theforexgeek review (empty body), vendor Myfxbook via aggregator) · **independent_source_count: 1**
  (fxroboteasy/vettedpropfirms aggregator naming the developer — weak) · **affiliate_source_count: 3**
  (vendor MQL5 blogs, group-buy listing, affiliate listicles).
- **Best evidence found:** Tier 3 — a *claimed* "verified Myfxbook" record that is **uninspectable** (403)
  and **internally implausible**. **No inspectable evidence above Tier 3;** no independent real-money
  corroboration; the most "independent"-looking review returned an empty body.

## Unverified Claims
- +106.69% / 0.39% max DD / PF 3.56 / recovery 5.89 / $242,287 net / "18+ months live verified Myfxbook" —
  all uninspectable and internally implausible.
- "Fixed stop loss on every trade" and "no martingale/grid/averaging" — vendor/review assertions; not
  independently demonstrated (no teardown, .ex5 closed); the near-zero DD undermines the SL claim.
- "Perfect for FTMO/prop firm accounts" — no Tier-0 funded evidence.

## Eligibility Gates
- **Gate A — PASS (survives, on the disclosed mechanism).** Breakout + fixed SL + ≤1 trade/day + explicit
  no-grid/martingale is not a banned mechanism, and one-trade/day M15 is not tick-scalping/HFT. *Caveat:*
  the implausible DD raises the possibility of an undisclosed recovery/averaging mode; if a teardown or
  trade-level data ever showed loss-averaging, this flips to **Excluded** (flagged in Future Research).
- **Gate B — mechanism NOT independently verifiable → ceilings APPLY.** Closed .ex5, no third-party
  teardown, trade history uninspectable (403), mechanism confidence Low, metrics contradict the disclosed
  logic. Apply **Compliance ≤ 5, Risk ≤ 4, Deployment ceiling = Watchlist.**
- **Gate C — per-firm legality** (clean disclosed mechanism; closed-source commercial third-party EA):
  - FundedNext: **Permitted** (EA-friendly; gold breakout fine) — *rulebook v1 PROVISIONAL (primary 503).*
  - Funding Pips: **Conditional** — third-party EA allowed only as trade/risk manager; off-the-shelf
    directional EA leans Prohibited.
  - The 5%ers: **Conditional** — control-of-internal-logic; closed source (not HFT, so HFT ban N/A).
  - The Funded Trader: **Permitted** — standard EA, ≤1 trade/day, fixed SL, no overleverage signature;
    Asian-session window is not a market-close/news window. Numeric rules UNCONFIRMED.

## Per-Firm Legality Verdict
| Firm | Verdict | Rulebook | Basis |
|------|---------|----------|-------|
| FundedNext (primary) | Permitted | v1 (PROVISIONAL) | EA-permissive; mechanism not banned. Rulebook secondary — cannot clear Deployable. |
| Funding Pips (primary) | Conditional | v1 | Third-party EA allowed only as trade/risk manager |
| The 5%ers (primary) | Conditional | v1 | Control-of-internal-logic; closed source |
| The Funded Trader (primary) | Permitted | v1 | Standard EA, ≤1 trade/day, fixed SL; numerics UNCONFIRMED |
| Alpha Capital (reference) | Prohibited | v1 | Mandatory .MQ5 source-code submission (non-gating) |
| Goat Funded Trader (reference) | Prohibited | v1 | Off-the-shelf/commercial challenge EAs banned (non-gating) |

## Rule-Violation Flags
- **Evidence integrity:** the central "0.39% DD verified" claim is implausible and uninspectable — the
  binding risk is that the marketed track is curve-fit/demo, which would mean real-account behaviour
  (drawdown, win rate) is unknown and could trip prop limits on the first real losing cluster.
- **Broker/regime dependence:** an Asian-session gold-breakout edge depends on the firm's gold spread and
  server time; a tight backtest window does not transfer to a prop feed.

## Mechanical Rule-Respect
**Vendor-claimed only.** "Fixed SL on every trade" is asserted by the vendor and echoed by review sites,
but is **not independently demonstrated** (closed .ex5, no teardown), and the near-zero reported DD is
inconsistent with hard stops actually being hit — so the control is treated as **claimed/contradicted, not
established.** No documented daily-loss stop or max-position cap beyond ≤1 trade/day.

## Evidence & Performance
| Metric | Value | Tier | Source |
|--------|-------|------|--------|
| Average Monthly Return | ~+4.1%/mo implied (not stated; 106.69% over 18mo) | TIER3 | vendor Myfxbook (uninspectable) |
| Maximum Drawdown | 0.39% (claimed — implausible) | TIER3 | vendor Myfxbook summary (uninspectable) |
| Win Rate | NOT REPORTED | — | — |
| Profit Factor | 3.56 (claimed) | TIER3 | vendor Myfxbook summary (uninspectable) |
| Track Length | "18+ months live" (claimed; new 2026 EA) | TIER3 | vendor/aggregator (uninspectable) |
| Real vs Demo | Claimed real-money "live" — UNCONFIRMED (likely demo/curve-fit) | TIER3 | vendor (uninspectable) |

## Backtest Assessment
Vendor promotes strong backtest/live numbers but none are reproducible or inspected; given gold's volatile
regimes (2024–2026 shifts), a 0.39% DD is consistent with **over-optimization to a calm window**. Public
backtest = claim, not proof; here it is a **red flag**, not support.

## Risk-of-Ruin Analysis
**NON-ESTIMABLE.** No inspectable Tier 0/1 trade-level history (Myfxbook 403). ROR cannot be computed from a
headline gain/DD pair, and the 0.39% DD is not trustworthy input. **DD-definition mismatch caveat:** even
the reported DD uses Myfxbook's method and is not restatable under a firm's daily/overall rule without
trade-level data. ROR cap reduces Survival multiplier to min(A, 0.20). NON-ESTIMABLE ROR **bars Deployable.**

## Recommended Risk Settings (50k / 100k / 200k)
**Non-actionable.** No inspectable trade-level data; the disclosed SL/risk-% cannot be trusted given the DD
contradiction. Any sizing recommendation would be fabricated.

## Cost & Licensing
~$697 one-time with phased price increases ("allocation filling" urgency); closed **.ex5**. Also circulating
on **group-buy / pirated-adjacent** sites (eafxstore, ecomforex) — discovery/negative signal only, never
positive evidence, and a malware caveat applies to those builds (treat ≤ weakest community tier).

## Community Sentiment
**Thin / new EA.** The mandatory negative-case search (`scam`, `blown account`, `curve fit`, `demo`)
surfaced **no** specific complaints — but Apex is a **2026-vintage EA** with little independent track, so
the absence reflects youth, not vindication. No inspectable independent real-money corroboration exists; the
visible praise is vendor blogs and affiliate listicles.

## Why This Will Probably Fail
1. **Most likely benign explanation:** the "0.39% DD / +106%" curve is an **optimized backtest or a calm-
   window demo** mislabeled "verified live"; on a real account with gold's false breakouts the true DD is
   many multiples higher.
2. **Prop-server case:** even if the strategy is real, an Asian-session gold breakout's edge depends on the
   prop firm's gold spread/commission and server time; a tight optimized window does not transfer, and the
   first real losing cluster threatens the 5% daily / 6–10% overall envelope.
3. **Variance case:** a low-win-rate-payoff breakout can string false breakouts; an EA that *looks*
   drawdown-free in marketing is exactly the kind that surprises a funded account.
4. **Evidence fragility:** everything rests on Tier 3/4 — an uninspectable, internally-implausible vendor
   Myfxbook plus vendor blogs. The one piece of evidence that would change the verdict — an **inspectable,
   independent, trade-level real-money record whose DD survives scrutiny and shows real stops being hit** —
   does not exist publicly, and I do not have it.

## Scores (latent × multiplier/ceiling = adjusted)
best_tier = **TIER3**; ROR = **NON-ESTIMABLE** → Survival multiplier = min(MultA_T3 0.25, 0.20) = 0.20.
Multiplier A (Tier 3) = 0.25; Multiplier B (Tier 3) = 0.30. Gate B: Compliance ≤ 5, Risk ≤ 4. Risk
control-evidence: vendor-documented SL but contradicted by the DD → treat as vendor-documented (≤5); Gate B
Risk ceiling 4 binds (lowest).

| Dimension | Latent | Mult/Ceiling | Adjusted |
|---|---:|---|---:|
| Funded-Account Survival (30%) | 2 | ×0.20 (ROR cap) = 0.40 → clamp | 1 |
| Prop-Firm Compliance (20%) | 6 | min(6, GateB 5) | 5 |
| Risk Management (15%) | 4 | min(4, GateB 4, ctrl 5) | 4 |
| Challenge-Passing (15%) | 3 | ×0.25 = 0.75 → round-half-up | 1 |
| Consistency (10%) | 3 | ×0.30 = 0.90 → round | 1 |
| Transparency (5%) | 3 | ×0.30 = 0.90 → round | 1 |
| Profitability (5%) | 3 | ×0.30 = 0.90 → round | 1 |

**Overall** = 0.30·1 + 0.20·5 + 0.15·4 + 0.15·1 + 0.10·1 + 0.05·1 + 0.05·1
= 0.30 + 1.00 + 0.60 + 0.15 + 0.10 + 0.05 + 0.05 = 2.25 → **2.3 (poor)** (half-up one-decimal: 2.25→2.3).

## Deployment Verdict
**AVOID · Overall 2.3 (poor).**
**Binding criterion:** headline return+DD evidence is **Tier 3** (no inspectable independent verification —
Myfxbook 403; the "independent" review returned an empty body) **AND** ROR **NON-ESTIMABLE** with best_tier
≤ Tier 2 — a deterministic Avoid. Reinforced by an **internally-implausible 0.39%-max-DD / +106%-gain**
claim that is incompatible with the disclosed hard-SL breakout mechanism (strong curve-fit/demo or
undisclosed-recovery signal), group-buy/urgency marketing, and a short, recent gold-only regime.

## Similar EAs
- [[the-gold-reaper-mt5]] — Profalgo multi-strategy XAUUSD breakout with hard SL (same *gold-breakout-with-
  SL* family; Gold Reaper has an inspectable-but-403 verified record with ~42% DD — i.e. realistic DD,
  unlike Apex's implausible 0.39%). Useful contrast: Apex's DD is *too good*, Gold Reaper's is *too big*.
- [[ai-gold-sniper-mt5]] — single-entry fixed-lot hard-SL gold scalper (another clean-mechanism gold EA
  whose headline rests on an implausible vendor signal).
- Not a duplicate (different vendor, different specific entry logic).

## Red Flags
- **0.39% max DD over 18 months is statistically implausible** for a real hard-SL gold breakout scalper —
  the single biggest red flag (curve-fit/demo or hidden recovery).
- Closed .ex5; all evidence uninspectable (Myfxbook 403, review empty body); mechanism confidence Low.
- Urgency marketing ("price rises as allocation fills"); heavy vendor-authored MQL5-blog promotion.
- Circulates on group-buy/pirated-adjacent sites (malware caveat; negative signal only).
- New (2026) EA → short real regime regardless of the "18 months" claim.

## Source Links
- https://theforexgeek.com/apex-drawdown-zero-ea-mt5-review/ — 2026-06-22 — review (empty body) — unknown
- https://www.mql5.com/en/blogs/post/768792 — 2026-06-22 — vendor MQL5 promo blog (via search) — affiliate(vendor)
- https://eafxstore.com/product/apex-drawdown-zero-ea-mt5/ — 2026-06-22 — group-buy listing (via search) — affiliate(group-buy)
- https://www.fxroboteasy.com/experts/apex-drawdown-zero — 2026-06-22 — aggregator (via search) — mixed
- WebSearch lead aggregations (mechanism, developer, negative case) — 2026-06-22 — leads only

## Analyst Notes
- **FACTS:** XAUUSD M15, Asian-session 02:00–06:00 breakout, ≤1 trade/day, fixed-SL claimed, auto-lot by
  risk %, .ex5 closed, ~$697, developer Tshivhidzo Moss Mbedzi, claimed +106.69%/0.39%DD/PF3.56 over 18mo.
  (All via search leads; review/vendor pages empty/uninspectable.)
- **ANALYSIS:** disclosed mechanism survives Gate A, but the near-zero DD is incompatible with a real
  hard-SL breakout → curve-fit/demo or undisclosed recovery; Gate B applies (uninspectable closed box);
  Tier-3 uninspectable evidence + NON-ESTIMABLE ROR ⇒ Avoid.
- **ASSUMPTIONS (flagged):** that the marketed track is not genuine real-money (most likely demo/curve-fit)
  — unverifiable; that the disclosed hard SL is the whole loss-management story (the DD suggests not) —
  unverifiable.

## Future Research Needed
- If Myfxbook/vendor/review pages become allow-listed: inspect the live record — confirm real-money vs demo,
  the actual DD distribution, whether stops are genuinely hit, and whether any loss-averaging occurs (Gate-A
  re-test). A clean, inspectable ≥6-month real-money record with a *believable* DD could lift this toward
  Watchlist; confirmation of demo/curve-fit or averaging would push it to Avoid(confirmed)/Excluded.
- Operator could supply funded-account statements to test Deployable gate 8 (unlikely to be warranted given
  the evidence-integrity concern).

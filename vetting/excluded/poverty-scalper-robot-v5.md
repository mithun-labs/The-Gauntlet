[← Index](../README.md) · [Rankings](../rankings/) · [Rulebooks](../rulebooks/)

# Poverty Scalper Robot V5 (Scalping Robot) — EXCLUDED (Gate A)
*An M1 "scalper" whose users report it stacks buys into a loss with no real stop — Excluded at Gate A as a disguised martingale.*

> 🚫 **EXCLUDED at Gate A** — core mechanism is a **disguised martingale / grid recovery** (adds positions into a losing trade, no real stop loss despite claims). Never scored.

## One-line mechanism
Marketed as an M1 scalper (EURUSD/GBPUSD/USDJPY/EURJPY/XAUUSD) with "predefined Take Profit and Stop Loss"
and a "max drawdown" feature — but **multiple independent users report it stacks orders into a loss with no
real SL**: "it opens a buy and if the price goes down it keeps opens buy and buy … drawdown really high,"
"it doesn't have any automatic SL as it says," "**Disguised martingale!!!**," "earn $2, loss can be $100."
That behavior — averaging into losers, tiny wins / catastrophic losses, no hard SL — is martingale/grid.

## Vendor / Developer
Anonymous; distributed as a **free/cracked closed binary** ("limited intentionally so people won't be able
to modify the settings"). Needs a VPS; min balance ~$1,000.

## Discovery
Operator-supplied screenshot of a cracked "FREE Download" EA site (2026-06-24). Cracked sites are discovery
+ negative-signal only (Tier 4 cap, malware caveat).

## Gate A determination (banned core mechanism)
**Disqualifying mechanism: disguised martingale / grid recovery (no real SL).** Confidence: **Medium-High.**

**Public signals (FACTS / fetched):**
- **forexcracked.com listing + user comments (fetched 2026-06-24):** official copy claims TP/SL + max-DD
  feature, but users report — "**it opens a buy and if the price goes down it keeps opens buy and buy which
  makes the drawdown really high**" (Trader92); "**it doesn't have any automatic SL as it says**" (after a
  $150 loss); "**Fake backtest. Disguised martingale!!!**" (Mile); "**earn $2, loss can be $100**" (Segy);
  "No SL, completely different from tester." No verified live track (no MQL5 signal / Myfxbook).

**Why excluded (mechanism, not label):** the **described** controls (TP/SL, max-DD) are **contradicted by
convergent independent user reports** of order-stacking into losses with no real stop — the textbook
disguised-martingale profile (tiny wins masking rare catastrophic losses). Per Gate A, the inferred
mechanism governs, and the signals are strong and multi-user → **Excluded**.

## Per-firm legality (reinforcing — not needed for the Gate A exclusion)
- **FundedNext / Funding Pips / The 5%ers / The Funded Trader — Prohibited.** Martingale/grid with no
  per-trade hard SL is a prohibited strategy / over-leverage violation at all four primaries.
- Reference (Alpha Capital, Goat) — Prohibited (commercial + martingale), non-gating.

## Performance claims (recorded, NOT credited)
"M1 scalper, small profits, risk-controlled." **Tier 4 / not credited** — no verified track; users report
"fake backtest," live behaviour diverges from the tester, and accounts blow up. ROR **NON-ESTIMABLE**.

## Similar EAs
Same disguised-martingale profile as the archive's grid exclusions ([[forex-flex-ea-mt5]],
[[forex-fury-mt5]], [[fundedea-prop-firm-ea]], [[quantum-queen-mt5]]).

## Source Links
- https://www.forexcracked.com/forex-ea/scalping-robot-free-download/ — 2026-06-24 — cracked listing + user comments (fetched: order-stacking into losses, no real SL, "Disguised martingale", earn $2/loss $100) — pirate (negative/discovery only, Tier 4)
- WebSearch "Poverty Scalper robot EA mechanism scalping martingale grid" — 2026-06-24 — discovery + negative case — mixed

## Analyst Notes
- **FACTS:** fetched listing claims TP/SL + max-DD; multiple users report it adds buys into losses, has no
  real SL, "Disguised martingale", "earn $2 loss $100", fake backtest, blown accounts; closed/locked binary;
  no verified track.
- **ANALYSIS:** order-stacking into losers + no hard SL + tiny-win/huge-loss = martingale/grid → Gate A
  exclusion (Medium-High; rests on convergent fetched user reports, not the marketing copy). Tier-4 sourcing.
- **ASSUMPTIONS (flagged):** the official description hides the mechanism; the user-reported behaviour is the
  assessed behaviour and the locked binary can't be inspected to prove otherwise → no benefit of the doubt.

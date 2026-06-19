# Quantum Queen MT5 — EXCLUDED (Gate A)

**Verdict:** Excluded at Gate A — banned core mechanism (grid / recovery averaging with no individual stop loss).
**Mechanism Inference Confidence:** High (vendor's own page confirms a grid system; independent reviews confirm SL=0.00 on every order and catastrophic grid blow-ups).
**Date:** 2026-06-19

## Disqualifying Mechanism (one line)
A XAUUSD-only **grid** EA that opens multiple orders at staggered price levels with **no stop loss on individual trades (SL=0.00)** and "adaptive scaling," accumulating losing positions until reversal — a disguised grid/martingale signature. Grid trading is explicitly prohibited at all three target firms.

## Vendor / Listing
- **EA:** Quantum Queen MT5 · **Author:** Bogdan Ion Puscasu (Incredible Traders / "Quantum" family) · **Price:** $1,999.99 · **Rating:** 4.98/5 (~792 reviews) · XAUUSD only, multi-timeframe.

## Public Signals Justifying Gate A (per WEB RESEARCH PROTOCOL §E)
1. **Vendor's own MQL5 page** describes a "grid system" / "grid approach with adaptive scaling" and discloses no stop-loss mechanics. (PRIMARY, vendor — fetched.)
2. **Marketing language tells:** "trend-following grid," "adaptive scaling," "capital preservation," high advertised win rate — classic grid/averaging dressing. Vendor claims martingale was "removed in v2.0" and replaced with "smart lot scaling," but the **core mechanism remains grid averaging of losing positions** — describe the mechanism, not the label (CLAUDE.md Gate A).
3. **Independent technical review (fxprosystems, affiliate-flagged):** "there is literally no stop loss on individual trades: SL = 0.00 on every single order"; positions multiply in the losing direction; documented account blow-ups — 2018→2026 $1,000 account blown in 2022 at 110% balance drawdown; $100,000 variant blown with a single sequence reaching ~$2.35M loss; 21 consecutive losing trades totaling $23,616; a position held 99h10m awaiting reversal. (Tier 3 — affiliate site, but concrete mechanism observation corroborating the vendor's grid description.)
4. **Independent review (newyorkcityservers, affiliate-flagged):** confirms "grid system," notes inherent compounding/averaging risk and that "grid drawdowns can accelerate quickly." (Tier 3/4 — affiliate.)
5. **Equity-curve signature:** smooth high-win-rate climb punctuated by catastrophic blow-ups — the grid/martingale smooth-then-cliff signature.

## Per-Firm Legality (informational; EA excluded regardless)
- **Funding Pips** — Prohibited (grid + fully-automated third-party commercial EA both barred; rulebook v1, EA-policy PRIMARY-confirmed).
- **The Funded Trader** — Prohibited (grid/overleveraged + abusive automation; rulebook v1, prohibited-strategies PRIMARY-confirmed).
- **FundedNext** — Prohibited (grid trading reported prohibited; rulebook v1, SECONDARY/UNCONFIRMED).

## Sources (fetched)
| URL | Retrieved | Type | Independence | Affiliate? |
|-----|-----------|------|--------------|-----------|
| https://www.mql5.com/en/market/product/118805 | 2026-06-19 03:58 UTC | vendor listing (PRIMARY) | vendor | no |
| https://fxprosystems.com/quantum-queen-ea/ | 2026-06-19 04:00 UTC | review (mechanism/blow-up) | independent-ish | yes (broker referral + free-download) |
| https://newyorkcityservers.com/blog/quantum-queen-ea-review | 2026-06-19 04:00 UTC | review | independent-ish | yes (VPS upsell) |

## Notes
FACTS: vendor page states "grid system"; fxprosystems states SL=0.00 per order and documents blow-ups. ANALYSIS: a no-hard-stop grid that averages into losers is a banned mechanism at all three firms and an account-blow-up risk by construction; the high MQL5 rating reflects calm-period performance, not survival. ASSUMPTION: none required — the grid mechanism is vendor-confirmed. The "martingale removed" claim does not rescue it; grid/recovery averaging is itself a Gate A banned mechanism.

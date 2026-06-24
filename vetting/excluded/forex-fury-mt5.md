[← Index](../README.md) · [Rankings](../rankings/) · [Rulebooks](../rulebooks/)

# Forex Fury (MT5) — EXCLUDED (Gate A)
*A range-scalping basket EA that trades without a default stop loss — Excluded at Gate A for optional grid cost-averaging + martingale on a no-SL basket.*

> 🚫 **EXCLUDED at Gate A** — optional grid (cost-averaging into losers) and optional martingale, run on a no-default-stop-loss basket; optional-banned-mode rule applies. Never scored.

**Verdict:** Excluded at Gate A — banned mechanisms present: optional **grid (cost-averaging into losers)** and optional **martingale**, run on a **no-default-stop-loss basket** ("the system closes the entire grid"). The assessed public evidence cannot be shown to use a hard-disabled configuration, so the optional-banned-mode rule applies.
**Mechanism Inference Confidence:** Medium (no source code; mechanism reconstructed from multiple independent reviews + community reports, which agree on the no-SL basket and the optional cost-averaging/martingale features). **Gate A exclusion confidence: High.**
**Date:** 2026-06-19

## Disqualifying Mechanism (one line)
A range-scalping basket EA that **by default trades without a hard stop loss** and ships **optional "Cost Averaging" (adds a same-lot trade ~20 pips against an open loser → averaging down / grid)** and an **optional martingale** (increases size after a loss); positions are managed as a **unified basket that "closes the entire grid"** at a combined target. Grid/recovery-averaging and martingale are explicitly prohibited at the primary firms, and the assessed Myfxbook configurations are uninspectable (Myfxbook 403; multiple set-files; some accounts deleted) so no benefit of the doubt is given.

## Vendor / Listing
- **EA:** Forex Fury (MT4 & **MT5**, Build 600+) · **Vendor:** "Forex Fury team" / forexfury.com (developer not transparently named — referred to as "Patrick" in complaints; **accountability red flag**) · **Price:** ~$249.99 Gold (1 live license, lifetime updates, **no refunds**) · live since 2015; claims 21,600+ clients · pairs: EURUSD / GBPUSD / USDJPY etc.; trades a ~1-hour low-volatility window (≈4–5 p.m. ET).

## Public Signals Justifying Gate A (per WEB RESEARCH PROTOCOL §E)
1. **No default hard stop loss** — DailyForex (independent, fetched): "The default setting has **no stop-loss**"; when optional stops are used "the risk per trade is much higher than the reward per trade, sometimes three times more risk than the potential reward." NYCServers (fetched): "the default settings run **without a hard stop-loss**"; "Some users have reported significant losses when the market moved against open positions."
2. **Optional grid / cost-averaging (adds to losers)** — per review aggregation: an optional **"Cost Averaging"** feature where "if trades reach a specified loss level (like 20 pips), it will open another trade with the same lot size, allowing you to **average down** your open price." Averaging down into a loser is grid/recovery averaging = Gate A banned.
3. **Basket / grid management** — "The system closes the **entire grid** when combined profit reaches the Take_Profit target or hits the Stop_Loss threshold, with individual positions not closing separately — the system manages them as a **unified basket**." Basket-of-no-SL-positions is the grid exposure profile.
4. **Optional martingale** — vendor ships a martingale option that "will **increase the size of trades after a loss** in order to recover faster." Present-but-optional banned mode.
5. **Equity-curve / outcome signature** — >90% (claimed 93%) win rate but "the **losses are larger than the wins**"; a sample account shows **~41% max drawdown**; "a drawdown that **took a year to claw back**"; "some Forex Fury Myfxbook accounts have been **deleted over time**, which typically indicates the account crashed." This is the high-win-rate-then-cliff signature of no-SL basket/grid risk.

## Optional-Banned-Mode Determination (CLAUDE.md Gate A)
The rule: an optional banned behavior → **Excluded** unless public documentation shows it can be hard-disabled **AND** the assessed public evidence clearly uses the disabled configuration; if the assessed configuration is unknown, **do not give benefit of doubt**.
- Cost-averaging and martingale are optional and default-off, so hard-disabling is documented. **However**, the assessed public evidence — the vendor's verified Myfxbook accounts — is **uninspectable** (Myfxbook returns 403; the vendor admits 15+ different set-files across accounts; some accounts have been deleted/blown), so I **cannot** establish that the assessed track records run with both features disabled and with a hard stop. Per the rule, benefit of the doubt is withheld → **Excluded**. Even the default config (no hard SL, basket "grid" close) carries the banned exposure profile.

## Per-Firm Legality (informational; EA excluded regardless)
- **Funding Pips** — Prohibited (grid + martingale forbidden; and fully-automated third-party commercial EA barred on standard evals — permitted only as a trade/risk manager; rulebook v1, EA-policy PRIMARY-confirmed).
- **The Funded Trader** — Prohibited (grid/martingale + no-SL high-risk automation; rulebook v1, prohibited-strategies PRIMARY-confirmed).
- **The 5%ers** — Prohibited (grid/martingale prohibited; closed-source commercial EA where trader cannot evidence control of internal logic; rulebook v1).
- **FundedNext** — Prohibited (grid/martingale prohibited; rulebook v1, SECONDARY/UNCONFIRMED numerics).

## Negative Case (independent, recorded)
- **Refund denials after losses** (ForexPeaceArmy / Trustpilot via search): users report the vendor "refused to refund after they lost money"; "no refunds" policy.
- **Blown / deep-drawdown accounts:** "their account would have blown up without a stop loss, despite the company recommending against using one"; a user reported trades stuck in **~$4–5k drawdown**; ForexFactory threads reference 40% drawdowns / blown accounts.
- **Independent failure test:** a user ran it 4 months across **six brokers** with varied settings (incl. recommended) and called it "a total failure" where "losses wiped out wins."
- **"Paid reviews" suspicion** raised by reviewers; heavy affiliate footprint.

## Sources (fetched / consulted)
| URL | Retrieved | Type | Independence | Affiliate? |
|-----|-----------|------|--------------|-----------|
| https://www.dailyforex.com/forex-articles/forex-fury-trading-bot-review-29-november-2023/204383 | 2026-06-19 18:35 UTC | review (mechanism, no-SL, R:R, DD) | independent | no |
| https://newyorkcityservers.com/blog/forex-fury-review | 2026-06-19 18:36 UTC | review (no-SL default, ~41% DD, basket "grid", cost-averaging, martingale, MaxOrders, price) | independent-ish | yes (VPS upsell) |
| https://www.forexpeacearmy.com/forex-reviews/12226/forex-fury-review | 2026-06-19 18:34 UTC | user reviews / complaints (located via search; page 403 to fetch tool) | independent | no |
| https://www.myfxbook.com/reviews/expert-advisors/forexfury/3307084,1 | 2026-06-19 18:36 UTC | aggregate reviews (located; 403 — uninspectable) | independent | n/a |
| https://www.forexfactory.com/thread/924560-forex-fury | 2026-06-19 18:37 UTC | community thread (located via search; not fetched) | independent | no |
| https://www.forexfury.com/ | 2026-06-19 18:34 UTC | vendor (located; 403 — uninspectable) | vendor | n/a |

## Notes
FACTS: independent reviews state no default hard SL, inverted risk:reward, ~41% sample DD, and an optional cost-averaging (average-down) feature plus an optional martingale, with basket "grid" management; community reports refund denials and blown/deep-drawdown accounts. ANALYSIS: a no-hard-stop range basket that can average down into losers and (optionally) martingale is, by construction, the grid/martingale risk profile this agent exists to catch; the 90%+ win rate reflects small TPs masking large tail losses, not a survivable edge. ASSUMPTION: none required for exclusion — the banned modes are documented across multiple independent sources; the only uncertainty (exact config of the verified accounts) resolves *against* the EA under the optional-banned-mode rule. The "martingale not used in verified accounts" claim is vendor-adjacent and unverifiable (Myfxbook 403), so it does not rescue the EA.

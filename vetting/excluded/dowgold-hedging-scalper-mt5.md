# DowGold (Hedging Scalper) EA MT5 — EXCLUDED (Gate A)

**Verdict:** Excluded at Gate A — banned core mechanism: a **hedging / recovery-averaging basket** that, on an adverse move, **"scales in at better levels to work the entry back"** (averaging down / grid recovery) while running **dual long+short hedged positions** with **dynamic lot sizing**. Grid/recovery-averaging and basket hedging-recovery are prohibited at the primary firms. The "No martingale" marketing label is irrelevant under Gate A: the disqualifier is *reinforcing losing positions to recover the entry*, which the vendor itself describes.
**Mechanism Inference Confidence:** High (no source code, but the vendor's own page describes scaling into losers to "work the entry back"; the predecessor product is explicitly a dual-position hedging basket with dynamic lot sizing; a reseller review places it in the "traditional hedge scalper / martingale-expansion" family). **Gate A exclusion confidence: High.**
**Date:** 2026-06-20

## Disqualifying Mechanism (one line)
A multi-mode **hedging scalper** on US30 + XAUUSD that opens **opposing (long+short) positions as a basket** and, when price moves against it, **"scales in at better levels to work the entry back"** — i.e. averages down / adds recovery positions into an open loser — with **dynamic (volatility/equity-scaled) lot sizing**. That is grid/recovery-averaging on a hedged basket: a banned mechanism at all four primary firms. The flagship public result ("**+315% in 1 day, 0% drawdown**" $1k→$4,156 flip) and the "Balanced" mode's **~31% drawdown recovery** are the smooth-then-cliff signature of basket recovery, not a stop-based edge.

## Vendor / Listing
- **EA:** DowGold EA (a.k.a. DowGold Hedging Scalper), MT5, v5.26 (build 5833+). Evolution/rebrand of the **"US30 and XAUUSD Hedging Scalper"** EA (same instruments, same dual-position hedging mechanism).
- **Vendor:** "**DGHS Trading Inc.**" — corporate shell only; **no named individual developer** (accountability red flag). Listed address is a Los Angeles virtual-office (718 South Hill Street, LA 90014).
- **Distribution:** **Not on the MQL5 Market** — the vendor states a "cloud-connected licensing system MQL5 isn't built to support." Effect: it sidesteps MQL5's public review/comment tab and platform-hosted signal stats (the exact independent scrutiny this agent relies on). Sold via dowgoldea.com + a large affiliate-reseller ecosystem (cheaperforex, simpleforextools, eafxstore, shopforexea, forexeashop, fxeastore, etc.); cracked/discounted copies circulate at ~$49.99.
- **Price:** $299/mo · $599/3-mo · $999/yr · **$1,999 lifetime** (6 accounts) + paid "Inner Circle" upsell. Min deposit $50 ($5 cent).

## Public Signals Justifying Gate A (per WEB RESEARCH PROTOCOL §E)
1. **Scales into losers to recover the entry** — vendor (dowgoldea.com, fetched): the system "**scales in at better levels to work the entry back**" when trades move against it. Adding positions into an adverse move to average the entry is grid/recovery averaging = Gate A banned, regardless of the adjacent "No martingale. Position size stays constant" claim.
2. **Dual-position hedging basket** — predecessor "US30 and XAUUSD Hedging Scalper" (independent aggregation): "**Dual-Position Hedging** — opening both long and short positions on the same [instrument]," managed as a basket "to protect against significant price movements in either direction." Hedged basket recovery is the same mechanism family.
3. **Dynamic lot sizing** — predecessor description: "**Dynamic Lot Sizing**… adjust trade sizes based on current market conditions, account equity, and volatility." Size that scales with conditions/exposure is the lever that turns a recovery basket into account-blow risk.
4. **Reseller concession** — simpleforextools (affiliate, fetched): the system is "**less dependent on dangerous martingale expansion compared to many traditional hedge scalpers**" — i.e. it is acknowledged to be *in* the hedge-scalper / martingale-expansion family, "aggressive configurations naturally involve higher exposure."
5. **Outcome signature** — "**+315% in 1 day, 0% drawdown**" flip and 100%+ account "doubles"; Balanced mode shows a **~31% drawdown** that had to be "recovered"; the predecessor demo cited PF ≈ 1.01 over ~3,586 trades (edge from trade volume, not a real edge). High-frequency, deep-basket-drawdown, then snap-back — the grid/recovery profile, not a survivable stop-based system.

## Optional-Banned-Mode Determination (CLAUDE.md Gate A)
Here the banned behavior is **core, not optional**: scaling-in/averaging to "work the entry back" is the EA's described recovery method across all modes (Flipping, Aggressive, Balanced, Prop Firm differ only in lot aggression and DD caps, not in the recovery mechanism). There is no documented hard-disabled, stop-only configuration, and the assessed public Myfxbook records are vendor-controlled and uninspectable (Myfxbook 403 to the fetch tool). Benefit of the doubt is therefore withheld → **Excluded**. The "Prop Firm mode / 5–10% DD guard" claim does not rescue it: a configurable equity guard bolted onto a recovery-averaging basket is precisely what trips firm daily/overall DD when the basket runs against the position.

## Per-Firm Legality (informational; EA excluded regardless)
- **FundedNext** — Prohibited (grid/martingale/hedging-recovery prohibited; rulebook v1, SECONDARY/UNCONFIRMED numerics).
- **Funding Pips** — Prohibited (grid + martingale forbidden; fully-automated third-party commercial EA also barred on standard evals — allowed only as a trade/risk manager; rulebook v1, EA-policy PRIMARY-confirmed).
- **The 5%ers** — Prohibited (grid/martingale prohibited; closed-source cloud EA where the trader cannot evidence control of internal logic; rulebook v1).
- **The Funded Trader** — Prohibited (grid/martingale + high-risk recovery automation prohibited; rulebook v1).

## Negative Case (independent, recorded)
- Negative-case searches ran (`scam`, `blown account`, `refund`, `martingale`, `grid`, `losing`). They produced **no specific named blown-account/refund report yet** (the product is recent and primarily marketed through resellers), but surfaced (a) the reseller concession that it belongs to the hedge-scalper/martingale-expansion family, and (b) generic, well-evidenced warnings that hedge-scalper/grid systems "survive until they don't — five years of gains can vanish in one large move."
- **Structural red flags:** anonymous corporate-shell vendor; MQL5-marketplace avoidance (no public comment/blown-account tab); vendor-controlled Myfxbook accounts with implausible single-day +315%/0%DD flips; aggressive lifetime pricing + cracked-copy circulation; "cloud server generates the signals" black-box.

## Sources (fetched / consulted)
| URL | Retrieved | Type | Independence | Affiliate? |
|-----|-----------|------|--------------|-----------|
| https://dowgoldea.com/ | 2026-06-20 18:38 UTC | vendor (mechanism: "scales in to work the entry back", modes, DD claims, pricing, DGHS Trading Inc.) | vendor | n/a |
| https://simpleforextools.com/product/dowgold-ea-mt5/ | 2026-06-20 18:39 UTC | reseller "review" (hedge-scalper/martingale-expansion family concession; +315%/0%DD; discount upsell) | affiliate | yes |
| https://theforexgeek.com/us30-and-xauusd-hedging-scalper-ea-mt4-review/ | 2026-06-20 18:38 UTC | predecessor-EA review (located; page returned no body to fetch tool) | independent-ish | unknown |
| (search aggregation) US30 and XAUUSD Hedging Scalper — Etsy / cheapforexea / fintechea / forexeasmall listings | 2026-06-20 18:40 UTC | predecessor mechanism: dual-position hedging + dynamic lot sizing | mixed/affiliate | yes |
| https://cheaperforex.com/product/dowgold-hedging-scalper-ea-mt5/ | 2026-06-20 18:33 UTC | reseller listing (located; prop-firm-mode claims) | affiliate | yes |

## Notes
FACTS (from fetched sources): the vendor describes recovering adverse trades by "scaling in at better levels to work the entry back"; the predecessor product opens dual long+short hedged positions with dynamic lot sizing; a reseller places it in the "traditional hedge scalper / martingale-expansion" family; flagship results are +315%/1-day flips and 100%+ doubles with a ~31% drawdown in Balanced mode. ANALYSIS: averaging into losers on a hedged basket with volatility-scaled lots is the canonical grid/recovery mechanism Gate A exists to exclude; the "No martingale" disclaimer addresses only literal lot-doubling, not the disqualifying behavior (reinforcing losers); the headline single-day flips are the smooth-then-cliff basket signature, and a "Prop Firm mode" DD guard cannot make a recovery-averaging basket survive a firm's equity-DD calculation when the basket runs. ASSUMPTION: none required for exclusion — the recovery-averaging mechanism is described by the vendor itself; uninspectable Myfxbook accounts (403) only reinforce withholding benefit of the doubt. The lack of an inspectable, independent verified track record means there is no Tier 0/1 evidence that could override the mechanism finding.

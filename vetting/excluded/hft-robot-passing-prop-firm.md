[← Index](../README.md) · [Rankings](../rankings/) · [Rulebooks](../rulebooks/)

# HFT Robot for Passing Prop Firm Challenges (MT5) — EXCLUDED (Gate A)
*An HFT exploit for HFT-allowed challenge phases only — vendor states it is not for funded or live accounts — Excluded at Gate A for HFT / latency tick-scalping.*

> 🚫 **EXCLUDED at Gate A** — core mechanism is **HFT / latency tick-scalping**, intended only for HFT-allowed *challenge* evaluations and explicitly **not** for funded or live accounts. Never scored.

## One-line mechanism
A **high-frequency EA** that "detects significant market movements" and fires rapid M1/M5 trades on
**US30 / GER30**, with a "pro-ratio money management (PRMM)" system that **auto-scales lot size on gains**
to clear a challenge fast. It opens one trade at a time (so it is *not* grid/martingale), but it is a
**HFT challenge exploit** that the vendor says is **"not tested for funded prop firm accounts, or
live/real broker accounts."**

## Vendor / Developer
Distributed as a **free/cracked download** (forexcracked); no identifiable accountable vendor. Targets
niche HFT-allowing firms — "Fast Forex Funding, Infinity Forex Funds, Nova Funding, Next Step Funding" —
**none of them a primary target firm.**

## Discovery
Operator-supplied screenshot of a cracked "FREE Download" EA site (2026-06-24). Cracked/nulled sites are
**discovery + negative-signal only** (Tier 4 cap, malware caveat) per the research protocol.

## Gate A determination (banned core mechanism)
**Disqualifying mechanism: HFT / latency tick-scalping (challenge-feed exploit).** Confidence: **High.**

**Public signals (FACTS / fetched):**
- **forexcracked.com listing (fetched 2026-06-24):** "a special **HFT strategy** that detects significant
  market movements"; **M1/M5, US30/GER30**; "**pro-ratio money management** … automatically adjusts the
  lot size based on gains"; **"intended only for use in HFT allowed prop firm evaluations and challenges.
  It has not been tested for other trading challenges, funded prop firm accounts, or live/real broker
  accounts."** *(Cracked-site page — used as a negative/discovery signal only.)*

**Why excluded (mechanism, not label):** a rapid-fire HFT system built to clear an **HFT-allowed demo
challenge** and explicitly unfit for funded/live trading is **HFT / latency exploitation** — a Gate A
banned mechanism judged against the primary firms' HFT/tick-scalping thresholds (FIRM RULEBOOKS item 9).
Auto lot-scaling "to complete the challenge faster" compounds the over-leverage risk. Excluded regardless
of reported challenge passes.

## Per-firm legality (reinforcing — Gate C)
- **FundedNext / Funding Pips / The 5%ers / The Funded Trader — Prohibited.** All four primaries ban HFT /
  latency / tick-scalping; the EA is not marketed for any of them, only for niche HFT-allowing firms →
  **Prohibited at all primary firms → would be Avoid even if not Gate-A excluded.**
- Reference (Alpha Capital, Goat) — Prohibited (commercial/source-code + HFT), non-gating.

## Funded-survival (the agent's actual objective) — structurally zero
The vendor **admits** it is not for funded or live accounts. There is **no path to a survived payout** —
the exact failure this agent exists to flag. ROR **NON-ESTIMABLE** (demo-challenge exploit; no real-money
trade distribution).

## Performance claims (recorded, NOT credited)
"Passes HFT-allowed challenges quickly with low drawdown." **Tier 4 / not credited** — a demo/challenge
HFT exploit's pass rate says nothing about funded survival, and the EA is self-admittedly untested there.

## Similar EAs
Same mechanism class as **[[hft-propfirm-ea-mt5]]** ("Green Man") — a recurring HFT-challenge-exploit
archetype across vendors. Distinct product (different distributor and target-firm list).

## Source Links
- https://www.forexcracked.com/forex-ea/hft-robot-for-passing-prop-firm-challenges-free-download/ — 2026-06-24 — cracked-site listing (fetched: HFT, M1/M5 US30/GER30, PRMM lot-scaling, not-for-funded admission) — pirate (negative/discovery only, Tier 4)
- WebSearch "HFT Robot passing prop firm EA high frequency tick latency" — 2026-06-24 — discovery + mechanism leads — mixed

## Analyst Notes
- **FACTS:** fetched listing — HFT strategy, M1/M5, US30/GER30, PRMM auto lot-scaling, one trade at a
  time, "not tested for funded prop firm accounts or live/real broker accounts"; targets HFT-allowing
  niche firms only.
- **ANALYSIS:** HFT/latency tick-scalping = Gate A banned; prohibited at all four primaries (HFT bans);
  funded-survival structurally zero by vendor admission. Triple-disqualified. Tier 4 sourcing.
- **ASSUMPTIONS (flagged):** not grid/martingale (single trade at a time), but the HFT/latency mechanism
  alone is disqualifying; exact trade frequency/hold time not numerically stated but "HFT" + M1/M5 +
  "detects significant movements" make the class unambiguous.

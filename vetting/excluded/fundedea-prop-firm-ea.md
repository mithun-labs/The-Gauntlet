[← Index](../README.md) · [Rankings](../rankings/) · [Rulebooks](../rulebooks/)

# FundedEA — Prop Firm EA (MT5) — EXCLUDED (Gate A)
*A "pass your prop challenge" EA that enters on pending orders and adds a grid when trades go negative — Excluded at Gate A for grid + martingale-style recovery.*

> 🚫 **EXCLUDED at Gate A** — core mechanism is a **grid + martingale-style recovery** (pending-order entries that add grid positions into a losing trade), plus an optional hedge. Never scored.

## One-line mechanism
Per the fetched listing, FundedEA "uses **pending orders to enter trades** and employs **a grid-like
strategy** when positions move negative," which "**could resemble a martingale approach**," with a
**hedge option** (disabled by default) and 60+ inputs across 5 indicators. Adding positions into an open
loss (grid/recovery averaging) is a Gate A banned mechanism regardless of the adjustable/optional framing.

## Vendor / Developer
**fundedea.com** ("Get Funded Hands-Free with our Trading Robot"). Vendor landing page is JS-rendered and
exposed **no public mechanism or stop-loss documentation** when fetched (silence on controls = unverified).
Marketed for FTMO / The 5%ers / FundedNext "and more"; min deposit ~$1,000. Widely circulated as a
**free/cracked download**.

## Discovery
Operator-supplied screenshot of a cracked "FREE Download" EA site (2026-06-24). Cracked/nulled sites are
**discovery + negative-signal only** (Tier 4 cap, malware caveat) per the research protocol.

## Gate A determination (banned core mechanism)
**Disqualifying mechanism: grid + martingale-style recovery averaging (+ optional hedge).** Confidence: **High.**

**Public signals (FACTS / fetched):**
- **forexcracked.com listing (fetched 2026-06-24):** "uses **pending orders to enter trades**" and
  "employs **a grid-like strategy** when positions move negative … **could resemble a martingale
  approach**"; "**hedge option** (disabled by default)"; best on BTC, XAUUSD, US30; "limited public
  information about core algorithms." *(Cracked-site page — used as a negative/discovery signal only.)*
- **fundedea.com (fetched 2026-06-24):** renders only the marketing tagline; **no documented stop loss,
  drawdown control, or mechanism** — controls unverified.

**Convergent independent leads (search; not fetched — recorded as the mandatory negative case):**
- The Forex Geek review describes FundedEA as a **"100% grid and martingale EA."**
- ForexPeaceArmy thread titled **"FundedEA — Martingale and doesn't want to honor guarantee"**; a second
  "FundedEA — Many problems" thread.
- A user report of an account **plunging ~$6k**; refund/guarantee disputes; Telegram shows winners only.

**Why excluded (mechanism, not label):** losing positions are **reinforced with added grid orders**
("grid-like strategy when positions move negative" / "martingale approach") — the banned mechanism by
behavior. Per the **optional-banned-mode rule**, an adjustable/optional grid/hedge does not exempt it: the
EA's core described behavior and assessed configuration are the grid/recovery one, and the live config is
uninspectable → benefit of the doubt withheld → **Excluded**.

## Per-firm legality (reinforcing — not needed for the Gate A exclusion)
- **FundedNext / Funding Pips / The 5%ers / The Funded Trader — Prohibited.** Grid/martingale recovery is a
  prohibited strategy at all four primaries; one adverse sequence breaches the daily/overall DD limit.
- Reference (Alpha Capital, Goat) — Prohibited (commercial/source-code + grid/martingale), non-gating.

## Performance claims (recorded, NOT credited)
"Helped 2000+ traders pass challenges / works with all prop firms." **Tier 4 / not credited** — no
inspectable independent track record; cracked-site + vendor marketing only; blown-account reports
contradict the marketing. ROR **NON-ESTIMABLE** (no real-money trade-level basis that isn't the banned
mechanism).

## Why this is the case the agent exists to catch
A "hands-free prop-firm pass" EA that hides a grid/martingale recovery behind 60+ inputs and an
"optional" hedge, sold/cracked widely with winners-only marketing and refund disputes — the canonical
disguised-grid profile a single bad sequence can blow.

## Source Links
- https://fundedea.com/ — 2026-06-24 — vendor page (fetched; tagline only, no mechanism/SL docs) — affiliate(vendor)
- https://www.forexcracked.com/forex-ea/fundedea-prop-firm-ea-free-download/ — 2026-06-24 — cracked-site listing (fetched; grid/martingale + hedge, BTC/XAUUSD/US30) — pirate (negative/discovery only, Tier 4)
- WebSearch (FundedEA grid/martingale; The Forex Geek "100% grid and martingale"; FPA "Martingale" thread; ~$6k blown account; refund disputes) — 2026-06-24 — independent leads (mandatory negative case)

## Analyst Notes
- **FACTS:** fetched cracked-site listing states pending-order entries + grid-like strategy on losing
  trades ("martingale approach") + optional hedge, BTC/XAUUSD/US30; vendor page documents no controls.
- **ANALYSIS:** grid + martingale-style recovery = Gate A banned mechanism (High confidence; fetched
  description corroborated by convergent independent leads). Tier 4 sourcing; ROR NON-ESTIMABLE.
- **ASSUMPTIONS (flagged):** hedge/grid are "adjustable/optional," but the described core behavior and the
  uninspectable live config are the grid/recovery one → optional-banned-mode rule excludes. Independent
  review/FPA pages could not be fetched (JS/403); their mechanism statements are recorded as leads.

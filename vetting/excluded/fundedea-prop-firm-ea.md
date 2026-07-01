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

## 2026-06-29 Re-confirmation (operator-requested fresh vetting pass)
Re-vetted end-to-end on operator request. **Verdict UNCHANGED: Excluded at Gate A (grid + martingale-style
recovery), High confidence.** Duplicate-detection: same product + same core mechanism as the 2026-06-24
entry → this is a **re-confirmation of the existing exclusion**, not a new EA (no duplicate index row created).

**What the fresh pass found (2026-06-29):**
- **Mechanism re-confirmed** via convergent independent leads: multiple sources again describe FundedEA
  entering on pending orders and, when trades move negative, **"a grid-like strategy … that could resemble
  a martingale approach"** with an adjustable/optional hedge and 60+ inputs across 5 indicators; The Forex
  Geek and FPA discussion again characterize it as a **"100% GRID, martingale EA"** that "won't pass prop
  firm challenges." Adding orders into an open loss is the Gate A banned mechanism regardless of framing.
- **NEW red flag — rebrand/evasion:** independent reports allege the vendor **created a sister/bogus site
  `propfirmea.co`** and repeatedly **changes its name** to merge profiles, dodge disputes, and get negative
  Trustpilot reviews removed via the "fake review" loophole; the Telegram channel shows winners only. This is
  a rebrand signal (mechanism-first fingerprint unchanged) and a heightened operator-durability / payout-
  dispute risk. Treat `propfirmea.co` as a probable FundedEA alias; do not vet as a novel EA on name alone.
- **Conflicting marketing claim (recorded, rejected):** one promotional source claims FundedEA has "proper
  stop losses" and "avoids martingale/grid." Per HARD RULE 6 (worse reading) and the convergent independent
  grid/martingale evidence + blown-account reports, this vendor-side claim does **not** overturn the Gate A
  exclusion. No inspectable real-money track record was found (ROR remains NON-ESTIMABLE, best_tier TIER4).
- **Fetch access (2026-06-29):** `fundedea.com` returned **HTTP 503**; ForexPeaceArmy review/threads returned
  **HTTP 403**; The Forex Geek review page rendered empty to the fetch tool. So the independent mechanism
  statements remain **fetched-as-leads** (per HARD RULE 2), consistent with 2026-06-24 — the exclusion rests
  on the previously-fetched cracked-site listing (discovery/negative signal) + convergent independent leads,
  now re-confirmed and reinforced by the rebrand finding. Per-firm legality unchanged (Prohibited at all four
  primaries; rulebooks 5%ers/TFT re-confirmed v1 on 2026-06-29, FundedNext/Funding Pips carried v1).

## Source Links
- https://theforexgeek.com/fundedea-review/ — 2026-06-29 — independent review ("100% GRID, martingale"; rendered empty to fetch tool → lead) — independent (lead)
- https://www.forexpeacearmy.com/forex-reviews/22368/fundedea-review — 2026-06-29 — FPA review (HTTP 403 → lead) — independent (lead)
- https://www.forexpeacearmy.com/community/threads/fundedea-martingale-and-doesnt-want-to-honor-guarantee.81044/ — 2026-06-29 — FPA "Martingale" thread (HTTP 403 → lead) — independent (lead)
- WebSearch (FundedEA grid/martingale; propfirmea.co rebrand; ~$6k blown account; refund/Trustpilot disputes) — 2026-06-29 — independent leads (mandatory negative case, re-run)
- https://fundedea.com/ — 2026-06-24 — vendor page (fetched; tagline only, no mechanism/SL docs; 2026-06-29 → HTTP 503) — affiliate(vendor)
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

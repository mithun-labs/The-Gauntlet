# Web Research Protocol

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: how to vet an EA without source access — search sequences, source handling, and discovery sources.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## WEB RESEARCH PROTOCOL (how to vet without source access)

You cannot read code, run MT5, open `.set` files, or verify private dashboards, so a verdict is only
as good as the public evidence you triangulate. Work each EA as an investigation: discover
candidates, fetch pages, gather **independent** evidence from multiple sources, cross-check every
claim, and **infer the mechanism from observable signals**. Never rest a conclusion on a single
source — least of all the vendor's own page. Every material claim must map to the per-EA
**Evidence Matrix**.

### A. Candidate discovery (where to find EAs to vet)

Build the queue from these, most-discussed / newest first; add each as a `pending` row in
`queue.jsonl` with its discovery source recorded:
- **MQL5 Market** — Experts sorted by rating, newest, and comments activity; open the listing,
  product screenshots, author profile, signal links, and **reviews/comments tab** (comments are
  where blown-account reports surface).
- **ForexFactory** — Trading Systems and Platform Tech threads; search the EA name, vendor name,
  and likely rebrand names.
- **Reddit** — r/Forex, r/algotrading, r/Forex_EA, and public prop-trading communities; search the
  EA name plus "prop firm EA".
- **Trustpilot + public review aggregators** — use mainly to find complaints, refund disputes,
  support failures, and suspicious review bursts.
- **YouTube** — "best prop firm EA", "EA passed [firm]", "EA settings", "EA backtest" — for leads
  and visible behavior only, never as standalone performance proof.
- **forexcracked.com (and other cracked / "nulled" EA sites)** — a **cracked/nulled-EA
  distribution site, NOT an evidence source.** An EA appearing here signals only that it is popular
  or paid enough to have been pirated — **never** quality, legality, or performance. **Permitted
  for two narrow uses only:** (1) **discovery** — confirming an EA exists / is in circulation; (2)
  **negative signals** — user comments reporting failures, scams, or marketing mismatches. It must
  **never** contribute positive performance evidence and **cannot raise an EA's evidence tier.**
  **Caveat:** cracked builds are routinely tampered with or bundled with malware, so any
  performance or behavior claim originating there is **doubly unreliable** (it may not even be the
  real EA). Rank it **at or below the weakest community tier (treat as Tier 4); never list it as a
  trusted source.**
- **Prop-firm sites** — fetch live rules for the primary firms (FundedNext, Funding Pips, The
  5%ers, The Funded Trader) and the reference firms (Alpha Capital, Goat Funded Trader) before
  judging legality.

Treat "top 10 EA" listicles, discount-code videos, Telegram funnels, broker/prop referral pages,
and cracked/"nulled" EA sites (e.g. forexcracked.com) as advertising or worse. They can add leads to
the queue, but they are affiliate, vendor-adjacent, or pirated-distribution leads — never
independent evidence — unless independence is clear; a cracked site is never positive evidence and
never raises a tier.

### B. Per-EA search sequence (run these; replace `<EA>`)

Search broadly, then **adversarially**. Fetch the actual pages — never judge from snippets or search
summaries. Stop at the research budget only after the mandatory negative-case search has run.
1. `<EA> myfxbook` · `<EA> fxblue` · `<EA> verified real account` — hunt a public verified track
   record with trade-level history.
2. `<EA> MQL5` · `<EA> mql5 comments` · `<vendor> mql5` — inspect listing metadata, comments,
   updates, author profile, and the author's other products.
3. `<EA> review` · `<EA> forexfactory` · `<EA> reddit` · `<EA> trustpilot` — independent discussion.
4. `<EA> scam` · `<EA> blown account` · `<EA> refund` · `<EA> losing` · `<EA> stopped working` —
   **the negative case is MANDATORY**; record whether the search produced sources or no public hits.
5. `<EA> martingale` · `<EA> grid` · `<EA> recovery` · `<EA> DCA` · `<EA> hedging basket` ·
   `<EA> stop loss` — mechanism tells.
6. `<EA> prop firm` · `<EA> FundedNext` · `<EA> Funding Pips` · `<EA> The 5%ers` · `<EA> The Funded Trader` ·
   `<EA> Alpha Capital` · `<EA> Goat Funded Trader` ·
   `<EA> passed challenge` · `<EA> payout` — treat passed/funded claims as **Tier 4** unless backed
   by Tier 0 public funded evidence.
7. `<EA> settings` · `<EA> set file` · `<EA> manual` · `<EA> max positions` · `<EA> news filter` —
   public clues for lot/risk behavior and whether a hard stop is documented.

### C. Source-by-source — what to extract, and how to distrust it

- **MQL5 Market listing** — extract price/rental, update history, screenshots, recommended deposit,
  lot/risk guidance, symbols, timeframes, hedging/netting requirements, max simultaneous positions,
  stop-loss language, news filter language, comments/reviews, author profile, and the **author's
  other products**. MQL5 signal stats are vendor-side or platform-adjacent claims unless linked to a
  public verified account; their presence alone is not independent verification.
- **Myfxbook / FXBlue** — count only the **live hosted page** (not a screenshot or vendor widget),
  with verified status, real vs demo label, broker, public trade history, track length, equity max
  DD, deposit size, and history visibility. Note if history is private, recently reset, demo-only,
  very small deposit, shows a smooth-then-cliff curve, or cannot be attributed to the purchasable
  product and its default settings (different version, manual intervention, or copy-trading contamination).
- **Vendor site / documentation** — useful for price, license terms, stated mechanism, symbol/timeframe,
  settings, and risk-control claims. Treat all performance and prop-passing claims as vendor claims
  until independently corroborated.
- **Forums / Reddit / public communities** — weight detailed criticism, multi-user corroboration,
  long-running journals, refund/blown-account reports, and screenshots of settings behavior. Brand-new
  accounts hyping one EA are weak or suspicious.
- **Trustpilot / review aggregators** — discount affiliate-driven 5-star bursts; weight concrete
  complaints about refunds, account losses, update failures, and support silence.
- **YouTube** — use only for observable behavior such as a screen recording showing grid entries,
  max-position behavior, or settings pages. Profit curves in videos remain Tier 3/4 unless independently
  corroborated.
- **Prop-firm rulebooks** — use primary firm pages first. If a rule is only found in blogs, FAQs,
  cached pages, or community posts, mark it `UNCONFIRMED` and do not rely on it for Deployable.

### D. Cross-verification and source quality

- A performance figure is **corroborated** only when an **independent** fetched source — not the
  vendor, not its affiliates — shows it. One vendor screenshot is not evidence.
- Search snippets, AI summaries, unfetched URLs, Discord/Telegram rumors, and paywalled claims are
  leads only; do not cite them as sources.
- Screenshots, sales-page widgets, cropped statements, and videos of dashboards are Tier 3 unless
  they link to a public hosted record; prop-success screenshots without public funded-account proof
  are Tier 4.
- Vendor pages are claims. Affiliate reviews are weak evidence. Affiliate tells: coupon/discount
  codes, referral links, "sign up with my link", identical copy across review sites, and exclusively
  positive coverage.
- When sources conflict, record the conflict and take the **worse** reading for scoring.
- If the full sequence yields **no independent** evidence, say so plainly: that EA is **Tier 4** by
  definition and cannot exceed Avoid/Watchlist.

### E. Inferring the mechanism when you cannot see the code

Infer the core mechanism from observable public signals and record **Mechanism Inference Confidence**
(`High`, `Medium`, `Low`, or `Unknown`):
- **Marketing language** — "recovery", "no stop loss", "grid", "averaging down", "never lose",
  "guaranteed", "martingale-safe", "smart hedging", "DCA", "basket", "zone recovery" → strong
  tells of grid/martingale or averaging.
- **Equity-curve shape** — a long smooth climb ending in a near-vertical cliff is the
  **martingale/grid signature**. A stair-step with visible stopped losses is more consistent with a
  stop-based strategy.
- **Listing/settings metadata** — hedging requirement, high max positions, large recommended deposit
  relative to lot size, no disclosed stop loss, recovery multiplier, averaging step, basket TP, or
  separate "safe/aggressive" modes are mechanism evidence.
- **Community complaints** — users reporting that it adds positions against a loss, recovers baskets,
  fails on news, blows accounts after updates, or requires manual intervention are mechanism evidence.
- **Silence itself matters** — if a vendor claims prop suitability but does not publicly document
  stop-loss, daily-loss stop, max-position, news, or risk controls, mark those controls as
  unverified; do not assume they exist.

A strong banned-mechanism signature is grounds to **Exclude under Gate A** — name the public signals
that justify it. A mechanism that genuinely cannot be inferred is a **black box** → Gate B ceilings
apply and the verdict cannot exceed Watchlist. Inference uncertainty never lowers the bar.

---


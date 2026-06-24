# Outcome Tracking

> Part of **The Gauntlet** documentation — operating manual: [`../CLAUDE.md`](../CLAUDE.md). **Single source of truth for: the realized-vs-predicted calibration loop.**
> References to ALL-CAPS section names in other docs resolve via the [Documentation Map](../CLAUDE.md#documentation-map).

## OUTCOME TRACKING (the only true calibration signal)

`vetting/outcomes/` records realized results against predicted verdicts. Without it, the scoring
can be systematically mis-calibrated indefinitely with no feedback.

- When the operator reports a real result for a vetted EA (challenge passed/failed, funded account
  survived/blown, payout received), append a record:
  ```json
  {"slug":"example-ea","predicted_verdict":"Watchlist","predicted_overall":6.2,"firm":"fundednext","event":"challenge_failed_daily_dd","date":"2026-06-30","note":"hit daily DD in week 2"}
  ```
- **Each run (START-OF-RUN step 7):** surface any past **Deployable/Watchlist** EA whose realized
  outcome contradicts its verdict, and any **Avoid** EA that demonstrably succeeded. Re-vet
  contradicted EAs with priority.
- Periodically summarize calibration in the daily report (e.g. of EAs scored ≥6 with verdict ≠
  Avoid, what fraction actually reached payout). Treat persistent contradiction as a signal to
  re-tune the multipliers or the Deployable gates — not to quietly adjust a single EA's score.

---


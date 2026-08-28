# 042 — Barriers and Path Dependence

**Vocabulary key:** Find **042** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

Some contracts care not only where a price ends but whether it touched a level along the way. For these, the journey changes the payoff. **For an AI helper:** retain the required path data and flag gaps in intraday observations; an ending price alone may be useless.

## Two paths, one ending, two contracts

The exercise boundary made value depend on where the contract stood before expiry. A barrier makes that memory contractual. Path A travels 100 → 130 → 110. Path B travels 100 → 90 → 110. Both finish at 110. A down-and-out call with barrier 95 survives A and dies on B. A European call sees only the shared endpoint.

For an Asian call, carry the running sum or average as additional state. For a lookback, carry the running maximum or minimum. Path dependence means the model state must remember what the payoff will later ask.

## Monitoring is part of the legal artifact

A barrier checked continuously differs from one observed at daily closes. A price may cross intraday and recover. Simulating only daily endpoints misses continuous crossings; Brownian-bridge corrections estimate what happened between grid points inside a diffusion model.

Market disruption, stale prints, exchange closure, and source hierarchy matter. An original path-dependent derivative must specify observation timestamps, time zones, fallback sources, and whether touching exactly the barrier counts.

## Model dynamics become visible

Vanilla options constrain terminal distributions across maturities. Barriers interrogate the route between them. Two models fitting every current vanilla quote can disagree on barrier value because their spot–volatility dynamics and crossing behavior differ.

> **Design challenge:** write an unambiguous monthly-average commodity payoff. Include missing observation, holiday, negative price, rounding, and settlement rules.

> **Memory seal:** two travelers arrive at the same endpoint with different passport stamps. The path archive pays according to the stamps, not merely arrival.

A terminal formula cannot enumerate every possible passport through time. The next method generates complete paths, applies the contract carefully to each one, and lets their discounted payoffs gather into an estimate.

[Next: Monte Carlo](../043-monte-carlo/README.md)

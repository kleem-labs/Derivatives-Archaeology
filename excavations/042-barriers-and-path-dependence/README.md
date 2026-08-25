# 042 — Barriers and Path Dependence

Two price paths can end at the same `S_T` yet give different barrier, Asian, or lookback payoffs. Terminal distribution alone no longer suffices; the path carries state.

A barrier option activates or dies when a level is crossed. Discrete monitoring can miss crossings between observations, so continuous and daily-monitored contracts differ. Asian options depend on an average, requiring the running sum as an additional state variable.

Path dependence expands computation and exposes model dynamics beyond the vanilla surface.

## Two paths, one ending, two contracts

Path A travels 100 → 130 → 110. Path B travels 100 → 90 → 110. Both finish at 110. A down-and-out call with barrier 95 survives A and dies on B. A European call sees only the shared endpoint.

For an Asian call, carry the running sum or average as additional state. For a lookback, carry the running maximum or minimum. Path dependence means the model state must remember what the payoff will later ask.

## Monitoring is part of the legal artifact

A barrier checked continuously differs from one observed at daily closes. A price may cross intraday and recover. Simulating only daily endpoints misses continuous crossings; Brownian-bridge corrections estimate what happened between grid points inside a diffusion model.

Market disruption, stale prints, exchange closure, and source hierarchy matter. An original path-dependent derivative must specify observation timestamps, time zones, fallback sources, and whether touching exactly the barrier counts.

## Model dynamics become visible

Vanilla options constrain terminal distributions across maturities. Barriers interrogate the route between them. Two models fitting every current vanilla quote can disagree on barrier value because their spot–volatility dynamics and crossing behavior differ.

> **Design challenge:** write an unambiguous monthly-average commodity payoff. Include missing observation, holiday, negative price, rounding, and settlement rules.

> **Memory seal:** two travelers arrive at the same endpoint with different passport stamps. The path archive pays according to the stamps, not merely arrival.

[Next: Monte Carlo](../043-monte-carlo/README.md)

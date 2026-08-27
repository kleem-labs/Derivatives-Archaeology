# 023 — Vega and Rho: Sensitivity to Model Inputs

## First, in everyday words

Vega asks how the value changes when the market’s uncertainty estimate changes; rho asks about interest rates. They reveal that an option is exposed to more than direction. **For an AI helper:** label these as sensitivities to inputs and identify the source and freshness of each input.

## Move a parameter, not the market

Delta, gamma, and theta moved observable state and time. The price also depends on inputs supplied by the model. Take the same call and increase model volatility from 20% to 21% while holding spot, time, rate, and dividends fixed. The repriced difference is approximately the quoted vega for one volatility point. If mathematical vega is defined per unit volatility, desk vega is often one-hundredth as large. Unit conventions must accompany the number.

Long vanilla options generally have positive vega because wider terminal dispersion helps convex payoff. But a calendar spread, barrier, or volatility-surface trade can carry vega that changes sign across scenarios. Parallel volatility bumps also miss skew and term-structure movements; professional books use buckets by strike and maturity.

Rho asks a parallel question about rates. Higher rates make the future strike cheaper in present terms, supporting European calls and weighing on puts in the simplest stock model. Yet rates can move dividends, forwards, volatility, and discounting together. A partial derivative deliberately freezes those relationships.

## Greeks describe the model surface

A Greek is not a forecast. Positive vega says what the chosen pricing function does when `sigma` moves. It does not say implied volatility will rise or that the position will profit. Model choice matters: a “sticky strike” volatility bump and “sticky delta” bump can produce different portfolio responses.

> **Reader experiment:** reprice the call at volatility 19%, 20%, and 21%. Compare the centered finite difference with the advanced lab's vega logic. Then use a large ten-point bump and observe the failure of linear approximation.

> **Memory seal:** two weather dials sit on the engine—one widens paths, one changes the growth of cash. Turning a dial is a sensitivity experiment, not a weather forecast.

[Next: Dynamic Hedging](../024-dynamic-hedging/README.md)

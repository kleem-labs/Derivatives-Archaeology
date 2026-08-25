# 047 — Portfolio Greeks and Scenarios

First-order Greeks add across positions, making them useful portfolio summaries. But aggregation can hide offsetting gross exposures and nonlinear risk. A delta-flat book may carry large gamma, vega, skew, basis, or jump exposure.

Taylor P&L explains small moves; full-revaluation scenarios reveal larger and joint moves. A useful scenario names shocks to spot, curve, volatility surface, time, and liquidity and preserves economically consistent relationships where appropriate.

Risk cannot be compressed into one Greek without specifying which changes are being ignored.

## A flat delta can hide a cliff

A portfolio owns 100 calls and shorts stock until total delta is zero. The report says “no directional exposure.” Then spot jumps. Gamma changes delta before the hedge can trade; implied volatility rises; skew steepens; stock borrow becomes costly. The one-number summary was locally correct and globally misleading.

Aggregate Greeks only after aligning contract multipliers, currencies, discounting, and volatility buckets. Net vega can be zero while long short-dated volatility and short long-dated volatility create large term-structure risk. Net gamma can hide concentrations at different strikes.

## Scenarios restore joint movement

Design coherent scenarios: spot down 20%, at-the-money volatility up 10 points, downside skew steeper, rates lower, spreads wider, and correlation changed. Full-reprice every instrument. Compare with Taylor approximations to see which nonlinear terms mattered.

Historical episodes provide plausible joint moves but cannot cover unprecedented structure. Hypothetical reverse stress asks what combination would breach capital or liquidity, then judges plausibility. The purpose is not to predict one future but to reveal portfolio architecture.

## Explain the P&L

Each day bridge actual P&L through delta, gamma, theta, vega buckets, rates, new trades, and residual. A persistent unexplained residual may reveal model bugs, missing risk factors, stale data, or incorrect trade capture.

> **Reader challenge:** design one scenario that hurts a delta-neutral long-gamma portfolio. Include enough volatility, theta horizon, costs, or jump structure to make the loss coherent.

> **Memory seal:** one portfolio performs on many stages. A calm-stage Greek cannot describe what happens when weather, floor, and lighting move together.

[Next: Value at Risk and Expected Shortfall](../048-value-at-risk-and-expected-shortfall/README.md)

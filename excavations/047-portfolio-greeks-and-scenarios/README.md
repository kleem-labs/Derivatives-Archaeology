# 047 — Portfolio Greeks and Scenarios

## A flat delta can hide a cliff

Liquidity showed that one option's executable value depends on size and state. A portfolio compounds that problem. It owns 100 calls and shorts stock until total delta is zero. The report says “no directional exposure.” Then spot jumps. Gamma changes delta before the hedge can trade; implied volatility rises; skew steepens; stock borrow becomes costly. The one-number summary was locally correct and globally misleading.

Aggregate Greeks only after aligning contract multipliers, currencies, discounting, and volatility buckets. Net vega can be zero while long short-dated volatility and short long-dated volatility create large term-structure risk. Net gamma can hide concentrations at different strikes.

## Scenarios restore joint movement

Design coherent scenarios: spot down 20%, at-the-money volatility up 10 points, downside skew steeper, rates lower, spreads wider, and correlation changed. Full-reprice every instrument. Compare with Taylor approximations to see which nonlinear terms mattered.

Historical episodes provide plausible joint moves but cannot cover unprecedented structure. Hypothetical reverse stress asks what combination would breach capital or liquidity, then judges plausibility. The purpose is not to predict one future but to reveal portfolio architecture.

## Explain the P&L

Each day bridge actual P&L through delta, gamma, theta, vega buckets, rates, new trades, and residual. A persistent unexplained residual may reveal model bugs, missing risk factors, stale data, or incorrect trade capture.

> **Reader challenge:** design one scenario that hurts a delta-neutral long-gamma portfolio. Include enough volatility, theta horizon, costs, or jump structure to make the loss coherent.

> **Memory seal:** one portfolio performs on many stages. A calm-stage Greek cannot describe what happens when weather, floor, and lighting move together.

The scenario theater produces a distribution of possible portfolio losses. Management now asks for a threshold that can be compared across desks. Compressing the theater into one number will create the final statistical failure.

[Next: Value at Risk and Expected Shortfall](../048-value-at-risk-and-expected-shortfall/README.md)

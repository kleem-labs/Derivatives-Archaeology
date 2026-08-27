# 041 — Early-Exercise Boundaries

## First, in everyday words

An early-exercise boundary is the dividing line where taking the option’s value now becomes as good as waiting. It is a model guide, not an automatic instruction. **For an AI helper:** show both choices, their costs, and the contract’s actual exercise mechanics.

## Draw the border instead of listing decisions

Backward induction left one exercise-or-continue decision at every tree node. Read those decisions across a time layer. There may be a critical stock level below which exercising an American put dominates continuation. Connecting the critical levels creates an exercise boundary: thousands of node decisions become a moving frontier.

Near expiry, the boundary approaches the payoff's immediate economics. Farther from expiry, time value makes continuation attractive across more states. Higher volatility usually enlarges the value of waiting because more favorable future paths remain; higher rates can encourage earlier put exercise because strike cash received now can earn more.

For dividend-paying calls, a boundary may appear around ex-dividend dates. The decision compares dividend captured by owning stock with interest on paying strike early and optionality surrendered.

## Numerical boundaries need inspection

A coarse tree can make the boundary jagged because allowed stock nodes are discrete. Finite-difference free-boundary methods and least-squares Monte Carlo offer alternatives. Convergence should be tested not only for option price but for exercise policy, especially when the intended use is exercise advice.

Model risk matters sharply: small input changes near the frontier can reverse the decision while having modest effect on headline value. Therefore report the value difference between exercise and continuation, not only a binary instruction.

> **Reader challenge:** explain why “exercise when intrinsic value is positive” throws away time value. Then identify circumstances where selling the option dominates exercising it.

> **Memory seal:** a border moves across the price-time map as dividends, rates, volatility, and the shrinking horizon pull it.

The boundary shows that a contract can care about its state before expiry. A barrier makes that dependence explicit in the payoff itself: crossing one level can permanently change the claim even if terminal price later recovers.

[Next: Barriers and Path Dependence](../042-barriers-and-path-dependence/README.md)

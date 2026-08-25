# 041 — Early-Exercise Boundaries

At each time, an American option divides states into a continuation region and an exercise region. Their frontier is the early-exercise boundary.

The boundary balances intrinsic value now against discounted optionality and cash flows from waiting. It moves with rates, dividends, volatility, and time. Near a dividend date, a call boundary can shift sharply because exercising acquires the dividend.

There is usually no elementary closed form. Trees, finite differences, simulation regressions, or integral methods locate it numerically.

## Draw the border instead of listing decisions

At each remaining time, there may be a critical stock level below which exercising an American put dominates continuation. Connecting those critical levels creates an exercise boundary. It summarizes thousands of node decisions as a moving frontier.

Near expiry, the boundary approaches the payoff's immediate economics. Farther from expiry, time value makes continuation attractive across more states. Higher volatility usually enlarges the value of waiting because more favorable future paths remain; higher rates can encourage earlier put exercise because strike cash received now can earn more.

For dividend-paying calls, a boundary may appear around ex-dividend dates. The decision compares dividend captured by owning stock with interest on paying strike early and optionality surrendered.

## Numerical boundaries need inspection

A coarse tree can make the boundary jagged because allowed stock nodes are discrete. Finite-difference free-boundary methods and least-squares Monte Carlo offer alternatives. Convergence should be tested not only for option price but for exercise policy, especially when the intended use is exercise advice.

Model risk matters sharply: small input changes near the frontier can reverse the decision while having modest effect on headline value. Therefore report the value difference between exercise and continuation, not only a binary instruction.

> **Reader challenge:** explain why “exercise when intrinsic value is positive” throws away time value. Then identify circumstances where selling the option dominates exercising it.

> **Memory seal:** a border moves across the price-time map as dividends, rates, volatility, and the shrinking horizon pull it.

[Next: Barriers and Path Dependence](../042-barriers-and-path-dependence/README.md)

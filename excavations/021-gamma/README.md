# 021 — Gamma: How Delta Bends

## The error left after delta

Delta neutralized the first tiny move, but Chapter 020 showed it changes as spot moves. The rate of that change is gamma, `V_SS`. Using the call above, suppose delta is .542 and gamma is about .0198 per dollar squared. For a $5 rise, the delta-only estimate is `$2.71`. Adding curvature gives `.5×.0198×25≈$0.248`, producing about $2.96 before higher-order effects.

The same gamma correction is positive for a $5 fall because the move is squared. That does not mean a long call profits from every decline; the negative delta contribution may dominate. It means the curved option loses less than a tangent line predicts on one side and gains more on the other.

## Gamma creates trading behavior

A delta-hedged long-gamma trader sells shares after rises as delta increases and buys after falls as delta decreases—mechanically buying low and selling high. The option premium and theta pay for that convex response. A short-gamma trader does the reverse and can suffer during violent rebalancing.

Gamma concentrates near strikes and expiry because the terminal payoff changes from zero slope to unit slope over an increasingly narrow region. At the exact limit, the payoff kink is not smoothly differentiable. Real spreads and discrete trading become most important where the frictionless model demands fastest adjustment.

## Units and aggregation

Gamma is delta change per unit spot change. Portfolio gamma requires contract multiplier and position sign. Cross-gammas arise when a claim depends on multiple underlyings; a single diagonal gamma summary then misses interaction.

> **Retrieval challenge:** draw a tangent to a convex payoff and use the picture to explain the sign of the gamma correction without quoting Taylor's formula.

> **Memory seal:** a curved rail leaves the straight delta tangent behind in both directions.

[Next: Theta](../022-theta/README.md)

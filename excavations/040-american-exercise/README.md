# 040 — American Exercise

An American option may be exercised at any allowed time. Its value is therefore at least its intrinsic value and at least the corresponding European value.

Backward induction repairs European-only pricing: at each tree node compare continuation value with immediate exercise value and choose the larger. This is an optimal-stopping problem, not a different terminal payoff.

For a non-dividend-paying stock with nonnegative rates, early exercise of a call is generally suboptimal because exercise sacrifices time value and pays the strike early. Puts and dividend-paying calls can exercise early.

Next: [Early-Exercise Boundaries](../041-early-exercise-boundaries/README.md).


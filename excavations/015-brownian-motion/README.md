# 015 — Brownian Motion: Continuous Surprise

We need continuous-time noise whose disjoint increments do not remember one another and whose variance grows with elapsed time. Brownian motion `W_t` begins at zero, has independent normal increments, and satisfies `W_{t+dt}-W_t ~ N(0,dt)`.

A typical noise increment has size `sqrt(dt)`, not `dt`. Summing `dt`-sized random shocks would disappear in the limit; summing larger shocks would explode. Square-root scaling preserves finite uncertainty.

Geometric Brownian motion writes `dS = mu S dt + sigma S dW`. The first term is drift; the second is random movement proportional to price. Brownian paths are continuous but nowhere classically differentiable. Ordinary calculus therefore fails exactly where the model places its uncertainty.

Next: [Quadratic Variation](../016-quadratic-variation/README.md).


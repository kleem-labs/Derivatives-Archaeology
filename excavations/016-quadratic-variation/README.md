# 016 — Quadratic Variation: Noise Leaves a Second-Order Trace

## The experiment ordinary calculus gets wrong

Brownian motion denied us a tangent. Measure the consequence rather than naming it away. Take a path over one year and partition it. Add squared increments. For a smooth line with slope `a`, each increment is roughly `a dt`; its square is `a²dt²`. About `1/dt` terms sum to order `dt`, which vanishes.

For Brownian motion, each increment is order `sqrt(dt)`; its square is order `dt`. About `1/dt` such terms sum to order one. In probability the quadratic variation approaches the length of the interval.

That single scaling difference explains why the second derivative of an option cannot be discarded. In an ordinary Taylor expansion,

`Delta V ≈ V_t dt + V_S Delta S + .5 V_SS (Delta S)^2`.

If `Delta S` contains `sigma S Delta W`, its square contains `sigma²S²(Delta W)²`, which accumulates like `sigma²S²dt`. The option's curvature meets the path's quadratic variation and creates a first-order contribution in time.

## Interpreting the symbolic multiplication table

Traders often memorize `(dW)²=dt`, `dWdt=0`, `(dt)²=0`. These are not literal equalities between ordinary numbers. They are an order-keeping device for a limiting argument. Terms smaller than order `dt` disappear; the squared random term survives.

This also illuminates gamma P&L. A delta hedge removes the linear spot move, but realized squared moves continue to interact with curvature. Continuous-time option pricing is built upon that residue.

## Retrieval challenge

Explain why doubling the number of equal time intervals does not double expected quadratic variation over the same horizon. Each increment becomes smaller while there are more of them; the effects balance.

> **Memory seal:** countless tiny footprints look negligible alone, yet their squared impressions tile the entire one-year floor.

We now know exactly which term ordinary chain rule loses. The next excavation rebuilds the change in an option value and keeps the surviving curvature contribution.

[Next: Itô's Lemma](../017-itos-lemma/README.md)

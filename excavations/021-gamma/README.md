# 021 — Gamma: How Delta Bends

A delta hedge is exact only for an infinitesimal move. Gamma measures how delta changes: `Gamma = partial^2 V / partial S^2`. For a small spot move, `Delta V ≈ Delta*Delta S + 0.5 Gamma*(Delta S)^2`.

The squared term survives moves in either direction. A long vanilla option generally has positive gamma: large moves improve the dynamically rebalanced position, before theta and trading costs. Short gamma has the opposite exposure.

Gamma is often largest near the strike and expiry. Continuous hedging hides the increasing speed and cost of rebalancing there.

Next: [Theta](../022-theta/README.md).


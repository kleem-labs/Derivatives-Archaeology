# 035 — Hedging with Futures

A producer expecting to sell `Q_A` units can short futures to offset falling prices. A naive one-for-one hedge fails when contract size, price sensitivity, maturity, or underlying quality differs.

With futures contract size `Q_F`, a simple contract count is `N=h Q_A/Q_F`, where `h` is a hedge ratio. Its sign follows the exposure: short futures for a future sale, long futures for a future purchase.

A hedge reduces a named risk; it does not guarantee profit. Basis, volume, timing, margin, and counterparty rules remain.

Next: [Minimum-Variance Hedge Ratio](../036-minimum-variance-hedge-ratio/README.md).


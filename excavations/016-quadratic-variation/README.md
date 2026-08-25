# 016 — Quadratic Variation: Noise Leaves a Second-Order Trace

For a smooth path, squared increments vanish when a time partition becomes fine. Brownian increments are of size `sqrt(dt)`, so their squares are of size `dt`. Across a fixed interval they accumulate: `sum (Delta W)^2 -> T`.

This quadratic variation explains the symbolic rules `(dW)^2=dt`, `dW dt=0`, and `(dt)^2=0`. They are shorthand for limiting orders, not ordinary algebraic identities.

A naive Taylor expansion discards all second-order terms. With Brownian motion that throws away a contribution as large as the first-order time term. The missing term is the source of Itô's correction and ultimately the option gamma term in Black–Scholes.

Next: [Itô's Lemma](../017-itos-lemma/README.md).


# 010 — Many Small Steps

With several periods, the terminal option payoff is known at every leaf. Work backward one node at a time: at each node, match the two next-step option values using local stock and cash positions, then discount their risk-neutral weighted value.

For time step `dt`, one common tree chooses `u=e^(sigma sqrt(dt))` and `d=1/u`. Its local weight is

`p* = (e^(r dt)-d)/(u-d)`.

Backward induction is not merely computational convenience. It records a dynamic hedge: `Delta` changes after the stock moves. A hedge selected once at the root generally will not reproduce the kink at every leaf.

As steps multiply, the tree can approximate a continuous distribution and its price often converges toward Black–Scholes under matching assumptions. But convergence is conditional: dividends, early exercise, jumps, and unstable parameters require different trees or different models.

Next: [The Black–Scholes Limit](../011-black-scholes-limit/README.md).


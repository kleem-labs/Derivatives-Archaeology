# 020 — Delta: The First Local Hedge

If a call changes from $8.00 to about $8.60 when the stock rises $1, its local sensitivity is near `0.60`. Delta is `Delta = partial V / partial S`: approximate option-value change per one-unit spot change, everything else fixed. It also gives the instantaneous shares in the Black–Scholes hedge.

Delta is a slope, not a constant hedge for all moves. The payoff bends, so delta changes with spot, time, and volatility. Nor is call delta literally the real-world probability of exercise.

For a Black–Scholes call with yield `q`, `Delta=e^(-qT)N(d_1)`; for the put it is `e^(-qT)(N(d_1)-1)`.

Next: [Gamma](../021-gamma/README.md).


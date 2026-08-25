# 007 — Put–Call Parity

Compare two European portfolios with strike $100:

- Portfolio A: one call plus cash that becomes $100 at maturity.
- Portfolio B: one put plus one share.

If `S_T` is above $100, A exercises and owns the share; B lets the put expire and owns the share. If `S_T` is below $100, A keeps $100; B exercises the put and receives $100. Both end with `max(S_T,100)`.

Identical terminal payoffs require identical current costs:

`C + Ke^(-rT) = P + S_0`,

or `C-P = S_0-Ke^(-rT)`.

For `S_0=100`, `K=105`, `r=5%`, and one year, the right side is about `$0.12`. If the call costs $8, the matching put is about $7.88 under the assumptions.

Parity is a model-light constraint, but exercise style, dividends, funding, and transaction costs alter it. It relates prices without yet determining either option price. Replication in a small state space will.

Next: [One Period, Two Futures](../008-one-period-binomial/README.md).


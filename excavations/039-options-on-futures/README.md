# 039 — Options on Futures

An option on a futures contract has payoff based on futures price, often `max(F_T-K,0)`. Under deterministic rates, Black's model treats the current futures price as the forward-like underlying:

`C=e^(-rT)[F_0N(d_1)-KN(d_2)]`.

Discounting remains outside because the payoff arrives later. Futures-style option margining can alter cash-flow timing. Contract settlement, quotation, expiry, and the relationship between option and futures maturities must be read rather than assumed.

Next: [American Exercise](../040-american-exercise/README.md).


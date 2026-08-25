# 001 — Payoffs Before Prices

Suppose a stock ends at $70, $100, or $140. A right to buy it for $100 pays `0`, `0`, or `$40`. Writing those outcomes first prevents a common confusion: a contract's terminal payoff is determined by its terms, while today's price depends on time, tradable alternatives, and a model.

For a call with strike `K`, the owner exercises only when buying at `K` is cheaper than buying in the market:

`call payoff = max(S_T - K, 0)`.

For a put:

`put payoff = max(K - S_T, 0)`.

The maximum is not decorative. It records the owner's right to walk away. Replacing it with `S_T-K` silently turns a call into a forward-like obligation.

Payoff tables can compare states, but they cannot compare dollars at different dates. That failure creates discounting.

Previous: [A Promise](../000-a-promise-about-the-future/README.md). Next: [Time Has a Price](../002-time-value-of-money/README.md).


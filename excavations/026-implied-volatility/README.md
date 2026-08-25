# 026 — Implied Volatility: Turning Price into a Coordinate

Given a market price and the other Black–Scholes inputs, implied volatility is the `sigma` making the formula reproduce that price. A numerical root finder solves `BS(sigma)-market_price=0`.

Vanilla option price rises monotonically with volatility, so inversion is usually well behaved inside no-arbitrage bounds. An impossible price, such as a call below intrinsic value, has no valid implied volatility.

Implied volatility is not a pure forecast. It is a standardized quote containing expectations, risk premia, supply, demand, and model mismatch. Its power is comparison across strikes and maturities.

Next: [The Volatility Smile](../027-volatility-smile/README.md).


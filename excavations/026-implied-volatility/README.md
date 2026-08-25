# 026 — Implied Volatility: Turning Price into a Coordinate

Given a market price and the other Black–Scholes inputs, implied volatility is the `sigma` making the formula reproduce that price. A numerical root finder solves `BS(sigma)-market_price=0`.

Vanilla option price rises monotonically with volatility, so inversion is usually well behaved inside no-arbitrage bounds. An impossible price, such as a call below intrinsic value, has no valid implied volatility.

Implied volatility is not a pure forecast. It is a standardized quote containing expectations, risk premia, supply, demand, and model mismatch. Its power is comparison across strikes and maturities.

## Run the pricing machine backward

Suppose spot is $100, strike $105, rate 5%, and time one year. The market call ask is $8.02. Try `sigma=.10`; Black–Scholes produces too little option value. Try `.40`; it produces too much. Because vanilla call price rises continuously with `sigma`, bisection repeatedly halves the interval until the model price matches the quote near 20%.

The inversion contains a diagnostic. A European call on a non-dividend stock cannot cost less than `max(S_0-Ke^-rT,0)` or more than `S_0` under ideal assumptions. A price outside valid bounds has no implied volatility. The root finder should reject it rather than return nonsense.

## Bid and ask imply an interval

Markets do not offer one price. Invert the bid and ask separately. If a call is 7.80 bid and 8.20 ask, its implied volatility is an interval. A model value inside that interval cannot be executed as an edge. Stale quotes, wrong dividends, imprecise expiry time, and inconsistent rates can also manufacture apparent volatility differences.

## The number is a language

Quoting options in volatility allows traders to compare premiums across strikes, maturities, and spot levels. But implied volatility absorbs whatever Black–Scholes leaves unexplained: tail risk, demand for insurance, risk premium, jumps, and liquidity.

To decide whether an option is “worth it,” one must compare executable implied volatility and price with a conditional view of realized movement, jumps, surface evolution, costs, and insurance value. Historical volatility alone is not a verdict.

> **Memory seal:** a market premium enters the reverse furnace; the machine returns the single sigma that would have produced it, not a thermometer reading of nature.

[Next: The Volatility Smile](../027-volatility-smile/README.md) · [Implied-volatility lab](../../labs/advanced_lab.py)

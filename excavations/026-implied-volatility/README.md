# 026 — Implied Volatility: Turning Price into a Coordinate

**Vocabulary key:** Find **026** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **026** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Start with the option’s price tag and turn the model’s movement knob until the model prints the same price tag.

### In finance language

Implied volatility is the model input that reproduces a quoted option price. It is a coordinate for price, not a direct prediction of future movement.

Implied volatility is the volatility number that makes a chosen option model reproduce a quoted option price. It is a translation of price into model language, not a direct measurement of future movement. **For an AI helper:** retain the exact quote, model, rate, dividend assumption, and timestamp used in the translation.

## The strategy use of implied volatility

Buying an option means paying the market’s quoted uncertainty price; selling means accepting the risk that actual movement, jumps, and changing uncertainty prove that price too low. “High implied volatility” does not by itself mean sell, and “low implied volatility” does not by itself mean buy. The reader needs a comparison between implied movement, a stated reason for expecting different future movement, the payoff shape, and the cost of leaving the position.

An agent may say: “this option’s implied volatility is above its own past range under this stated data rule.” It must not turn that observation into “sell premium” without mapping maximum loss, assignment, liquidity, and the reason the market may be charging more today.

## Run the pricing machine backward

Realized volatility came from a completed path. A live option quote faces a path that has not happened. Rather than pretend the historical estimate is the model input, take the market price as evidence. Suppose spot is $100, strike $105, rate 5%, and time one year. The market call ask is $8.02. Try `sigma=.10`; Black–Scholes produces too little option value. Try `.40`; it produces too much. Because vanilla call price rises continuously with `sigma`, bisection repeatedly halves the interval until the model price matches the quote near 20%.

The inversion contains a diagnostic. A European call on a non-dividend stock cannot cost less than `max(S_0-Ke^-rT,0)` or more than `S_0` under ideal assumptions. A price outside valid bounds has no implied volatility. The root finder should reject it rather than return nonsense.

## Bid and ask imply an interval

Markets do not offer one price. Invert the bid and ask separately. If a call is 7.80 bid and 8.20 ask, its implied volatility is an interval. A model value inside that interval cannot be executed as an edge. Stale quotes, wrong dividends, imprecise expiry time, and inconsistent rates can also manufacture apparent volatility differences.

## The number is a language

Quoting options in volatility allows traders to compare premiums across strikes, maturities, and spot levels. But implied volatility absorbs whatever Black–Scholes leaves unexplained: tail risk, demand for insurance, risk premium, jumps, and liquidity.

To decide whether an option is “worth it,” one must compare executable implied volatility and price with a conditional view of realized movement, jumps, surface evolution, costs, and insurance value. Historical volatility alone is not a verdict.

> **Memory seal:** a market premium enters the reverse furnace; the machine returns the single sigma that would have produced it, not a thermometer reading of nature.

[Next: The Volatility Smile](../027-volatility-smile/README.md) · [Implied-volatility lab](../../labs/advanced_lab.py)

# 039 — Options on Futures

## First, in everyday words

An option on a future gives a choice about entering a futures position, so it combines option risk with daily futures settlement. The word “option” alone is not enough to describe the cash risk. **For an AI helper:** read the exercise result, futures multiplier, and margin consequences from the actual specification.

## Put the correct underlying into the formula

The curve and futures chapters have produced a forward-like quoted price. An exchange now writes an option on that futures contract rather than on physical commodity. Its payoff at option expiry depends on `F_T`, and the option and futures can have different maturities. Reading the contract specification is part of valuation.

Black's model assumes the futures price is lognormal under a suitable measure and writes a European call as

`e^(-rT)[F_0N(d_1)-KN(d_2)]`,

with `d_1=[ln(F_0/K)+.5sigma²T]/(sigma sqrt(T))` and `d_2=d_1-sigma sqrt(T)`. There is no spot carry term inside because `F_0` already expresses the forward level. Discounting remains because option payoff arrives at expiry.

For futures-style premium where option value is settled through margin rather than paid upfront, quotation and discount treatment can differ. Settlement into futures also creates exposure after exercise unless the delivered futures is closed.

## Why traders quote volatility again

Options on rates, commodities, and futures often use Black implied volatility as a common language. But a lognormal model struggles when futures can be zero or negative. Normal or shifted-lognormal models may be used, and switching conventions changes the numerical volatility quote even for the same price.

> **Reader decision:** before comparing two quoted volatilities, verify model convention, underlying futures month, option expiry, settlement style, multiplier, and whether price is premium-paid or futures-style.

> **Memory seal:** the option stands on a balcony above the futures floor; its payoff watches that floor, while discounting carries the result back to today.

The exchange specification contains one more sentence we have not yet valued: the holder may exercise before the final date. Black's European formula assumes that sentence is absent. Once early exercise is permitted, value must include a decision at every allowed date, not only a terminal payoff.

[Next: American Exercise](../040-american-exercise/README.md)

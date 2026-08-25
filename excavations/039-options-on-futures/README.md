# 039 — Options on Futures

An option on a futures contract has payoff based on futures price, often `max(F_T-K,0)`. Under deterministic rates, Black's model treats the current futures price as the forward-like underlying:

`C=e^(-rT)[F_0N(d_1)-KN(d_2)]`.

Discounting remains outside because the payoff arrives later. Futures-style option margining can alter cash-flow timing. Contract settlement, quotation, expiry, and the relationship between option and futures maturities must be read rather than assumed.

## Put the correct underlying into the formula

An exchange option may deliver a futures position rather than physical commodity. Its payoff at option expiry depends on `F_T`, and the option and futures can have different maturities. Reading the contract specification is part of valuation.

Black's model assumes the futures price is lognormal under a suitable measure and writes a European call as

`e^(-rT)[F_0N(d_1)-KN(d_2)]`,

with `d_1=[ln(F_0/K)+.5sigma²T]/(sigma sqrt(T))` and `d_2=d_1-sigma sqrt(T)`. There is no spot carry term inside because `F_0` already expresses the forward level. Discounting remains because option payoff arrives at expiry.

For futures-style premium where option value is settled through margin rather than paid upfront, quotation and discount treatment can differ. Settlement into futures also creates exposure after exercise unless the delivered futures is closed.

## Why traders quote volatility again

Options on rates, commodities, and futures often use Black implied volatility as a common language. But a lognormal model struggles when futures can be zero or negative. Normal or shifted-lognormal models may be used, and switching conventions changes the numerical volatility quote even for the same price.

> **Reader decision:** before comparing two quoted volatilities, verify model convention, underlying futures month, option expiry, settlement style, multiplier, and whether price is premium-paid or futures-style.

> **Memory seal:** the option stands on a balcony above the futures floor; its payoff watches that floor, while discounting carries the result back to today.

[Next: American Exercise](../040-american-exercise/README.md)

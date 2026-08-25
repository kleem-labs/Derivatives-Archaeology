# 031 — Dividends and Income

An owner receives dividends before forward delivery; a forward holder does not. For known cash dividends, subtract their present value from spot before carrying the remainder: `F_0=(S_0-PV(dividends))e^(rT)`. For continuous proportional yield `q`, `F_0=S_0e^((r-q)T)`.

Using the cash-dividend and yield formulas interchangeably creates errors, especially near large discrete payments. Dividend forecasts can change, and option exercise decisions may depend on their timing.

Income is not merely a correction term: it is part of the asset bundle being replicated.

## Follow the dividend check

A stock is $100 and will pay a known $3 dividend in six months. A one-year forward holder will not receive it; a cash-and-carry stock owner will. If we simply grow $100 at the funding rate, the owner route becomes too valuable.

Subtract the present value of the dividend from spot, because only the remaining financed amount represents the prepaid forward price. With continuous 5% rates, `PV(dividend)=3e^(-.05×.5)≈$2.93`. Fair forward is approximately `(100-2.93)e^.05≈$102.05`.

For an index modeled with proportional continuous yield `q`, the cleaner formula `S_0e^((r-q)T)` applies. A discrete dividend and a continuous yield are not interchangeable descriptions, especially near ex-dividend dates or when dividend uncertainty is material.

## Options feel dividends differently

A higher expected dividend lowers the forward stock level, generally reducing European call value and increasing put value. For American calls, receiving the dividend can make exercise immediately before ex-date attractive when the dividend exceeds remaining financing and optionality benefits.

Dividend forecasts are themselves risky. Boards can cut or increase payments. An implied dividend can be recovered from liquid option parity or forwards, but borrow and funding distortions may contaminate it.

## Reader decision

You observe call–put parity apparently violated by $0.80 around a dividend date. Before trading, reconcile the exact ex-date, expected cash amount, option exercise style, settlement, stock borrow, and executable sides. The “violation” may be a missing dividend rather than free money.

> **Memory seal:** fruit falls into the owner's basket before delivery. The forward buyer cannot charge for fruit never received.

[Next: Commodities and Convenience Yield](../032-commodities-and-convenience-yield/README.md)

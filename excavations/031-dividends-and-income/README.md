# 031 — Dividends and Income

**Vocabulary key:** Find **031** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

A stockholder may receive little cash gifts from the company. Someone who only promised to buy the stock later does not automatically get them.

### In finance language

A dividend is cash paid to stockholders. Expected dividends lower a forward’s fair delivery price relative to carrying the stock without income.

Owning a stock can bring dividend cash; holding a forward does not automatically bring the same cash. That missing payment changes a fair forward comparison. **For an AI helper:** use announced versus estimated dividends distinctly and save the source and date of each assumption.

## Follow the dividend check

The carry ledger says benefits received by the owner must be subtracted. Apply that instruction to a dated cash payment. A stock is $100 and will pay a known $3 dividend in six months. A one-year forward holder will not receive it; a cash-and-carry stock owner will. If we simply grow $100 at the funding rate, the owner route becomes too valuable.

Subtract the present value of the dividend from spot, because only the remaining financed amount represents the prepaid forward price. With continuous 5% rates, `PV(dividend)=3e^(-.05×.5)≈$2.93`. Fair forward is approximately `(100-2.93)e^.05≈$102.05`.

For an index modeled with proportional continuous yield `q`, the cleaner formula `S_0e^((r-q)T)` applies. A discrete dividend and a continuous yield are not interchangeable descriptions, especially near ex-dividend dates or when dividend uncertainty is material.

## Options feel dividends differently

A higher expected dividend lowers the forward stock level, generally reducing European call value and increasing put value. For American calls, receiving the dividend can make exercise immediately before ex-date attractive when the dividend exceeds remaining financing and optionality benefits.

Dividend forecasts are themselves risky. Boards can cut or increase payments. An implied dividend can be recovered from liquid option parity or forwards, but borrow and funding distortions may contaminate it.

## Reader decision

You observe call–put parity apparently violated by $0.80 around a dividend date. Before trading, reconcile the exact ex-date, expected cash amount, option exercise style, settlement, stock borrow, and executable sides. The “violation” may be a missing dividend rather than free money.

> **Memory seal:** fruit falls into the owner's basket before delivery. The forward buyer cannot charge for fruit never received.

Dividends were visible ownership income. A refinery's inventory provides something harder to observe: the ability to keep operating during scarcity. The same carry ledger must learn to recognize a benefit that never arrives as a cash payment.

[Next: Commodities and Convenience Yield](../032-commodities-and-convenience-yield/README.md)

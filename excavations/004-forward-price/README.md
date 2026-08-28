# 004 — The Forward Price

**Vocabulary key:** Find **004** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

There are two ways to get an asset later: own it now and carry it, or promise to receive it later. When both routes truly match, they should cost about the same. **For an AI helper:** list every ownership cost and benefit instead of using a forward formula as a slogan.

The station's twin bridges gave us a rule: identical future cash flows cannot carry different prices. Now a dealer quotes one-year delivery of a stock currently trading at $100. What delivery price makes a new forward worth zero?

The dealer asks for a forecast. You refuse—not because forecasts are useless, but because another route to future delivery is already tradable.

## Two routes to the same share

Route A is the forward: agree now, pay `K` in one year, receive one share.

Route B is cash-and-carry: borrow $100 now, buy one share, hold it for a year. At 5% continuous interest the debt becomes `100e^0.05=$105.1271`. At maturity you repay it and still own the share.

If the stock pays no income and costs nothing to hold, both routes produce one share at the same date. Their future cash cost must match:

`F_0(T)=S_0e^(rT)`.

Here `F_0(T)` is today's fair delivery price for maturity `T`, not today's value of an existing forward. With `S_0=100`, `r=.05`, and `T=1`, it is $105.13.

## Make the arbitrage move

Suppose the dealer quotes $110. Borrow $100, buy the share, and short the forward at $110. In a year deliver the share into the forward, receive $110, repay $105.13, and retain $4.87. The terminal stock price never enters the profit.

If the quote is too low, the reverse trade wants to short the stock, invest proceeds, and buy through the forward. That direction depends on stock borrowing and dividend obligations; real constraints can make bounds asymmetric.

## One dividend changes one route

Suppose the share pays income while it waits in the warehouse. Route B—the stock owner—receives it; Route A—the forward buyer—does not. The original equality must therefore change because the routes no longer contain identical benefits.

If income is paid continuously at proportional yield `q`, reinvesting it reduces the net cost of carrying the share and gives `F_0(T)=S_0e^((r-q)T)`. For a known cash dividend, subtract its present value from spot before carrying the remainder. Nothing else has been added to the argument: we found one cash flow present on one route and repaired the comparison.

The forward price is not a prediction that future spot will equal $105.13. It is the delivery price that prevents an idealized carry arbitrage today. Future spot can finish far above or below it.

> **Memory seal — the locked warehouse:** a share sits beside a loan whose balance grows. At delivery the forward must charge the same full carrying cost.

## Excavation questions

1. Calculate fair one-year forward price for spot $80, rate 4%, yield 1.5%.
2. Construct the cash-and-carry profit if the market forward is $5 too high.
3. Explain why the forward price is not a consensus forecast.

## What breaks next

The two delivery routes above were compared only at today and maturity. An exchange now proposes to settle their difference every evening. That inserts new cash-flow dates into the table, so the forward argument is no longer complete.

[Next: Futures Are Re-settled](../005-futures-marking-to-market/README.md) · [Lab](../../labs/derivatives_lab.py)

# 004 — The Forward Price

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

## Ownership is a bundle

If the stock pays continuous yield `q`, Route B receives income that Route A lacks. The fair forward becomes `S_0e^((r-q)T)`. Known cash dividends require subtracting their present value before carrying spot. Commodities add storage costs and convenience benefits. The general lesson is more durable than any one formula: list every cash flow and service that differs between owning now and receiving later.

The forward price is not a prediction that future spot will equal $105.13. It is the delivery price that prevents an idealized carry arbitrage today. Future spot can finish far above or below it.

> **Memory seal — the locked warehouse:** a share sits beside a loan whose balance grows. At delivery the forward must charge the same full carrying cost.

## Excavation questions

1. Calculate fair one-year forward price for spot $80, rate 4%, yield 1.5%.
2. Construct the cash-and-carry profit if the market forward is $5 too high.
3. Explain why the forward price is not a consensus forecast.

## What breaks next

A forward waits until maturity. An exchange futures contract moves gains and losses every day. Same final exposure does not guarantee same value when cash arrives at different times.

[Next: Futures Are Re-settled](../005-futures-marking-to-market/README.md) · [Lab](../../labs/derivatives_lab.py)


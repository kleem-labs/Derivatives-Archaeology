# 009 — Risk-Neutral Probability

The replication calculation gave $7.1947 without an up probability. Yet the same number can be written as a discounted weighted average of the $15 and $0 option payoffs. Where do the weights come from?

Let the stock multiply by `u` or `d`. We seek a weight `p*` making the stock's weighted terminal value equal its risk-free-grown current price:

`p*(uS_0)+(1-p*)(dS_0)=S_0e^(rT)`.

Cancel `S_0` and solve:

`p*=(e^(rT)-d)/(u-d)`.

For `u=1.2`, `d=.9`, rate 5%, and one year, `p*=0.504237`. Discount the call's weighted payoff:

`e^-0.05[0.504237($15)+(1-0.504237)($0)]=$7.1947`.

The replication price returns in different clothing.

## What the star warns us about

The star on `p*` separates a pricing measure from a real-world probability. It does not say investors are indifferent to risk. It says that after risks have been spanned and prices are internally consistent, we can reweight states so every tradable earns the risk-free rate in expectation.

If a researcher believes the actual chance of rising is 80%, that belief matters for expected investment return and risk, not for the unique replication price in this complete two-state model.

## An arbitrage detector hidden in the weights

For `p*` to lie between zero and one, risk-free growth must lie between down and up factors:

`d < e^(rT) < u`.

If risk-free growth exceeds even the stock's up return, shorting stock and investing cash dominates in every declared state. If it lies below the down return, borrowing to buy stock dominates. A “probability” outside `[0,1]` is the algebra announcing that the model already contains arbitrage.

## One state price per future dollar

The weighted-and-discounted formula can also be read through state prices: today's cost of receiving one dollar only in the up state and only in the down state. This viewpoint scales toward Arrow–Debreu securities, martingales, and changes of measure. But its origin remains the half-share and debt we physically checked.

> **Memory seal — the silver balance:** the two state weights shift until the stock's weighted growth balances exactly with the bank account.

## Excavation questions

1. Calculate `p*` for `u=1.3`, `d=.8`, and risk-free growth 1.04.
2. Give a real-world probability different from `p*` and explain why the replication price does not move.
3. Construct the dominating trade when `e^(rT)>u`.

## The next pressure

A single fork prices one exercise date. Real options face many successive moves, and the hedge chosen now will not remain correct after the first branch.

[Next: Many Small Steps](../010-multi-period-binomial/README.md)


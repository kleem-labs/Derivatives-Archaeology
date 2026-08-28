# 004 — The Forward Price

**Vocabulary key:** Find **004** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

To have a toy next year, you can buy it now and keep it safe, or promise to receive it next year. Compare the whole cost of both routes.

### In finance language

The forward price is the delivery price that makes future delivery match buying the underlying now, financing it, and carrying it.

There are two ways to get an asset later: own it now and carry it, or promise to receive it later. When both routes truly match, they should cost about the same. **For an AI helper:** list every ownership cost and benefit instead of using a forward formula as a slogan.

The station's twin bridges gave us a rule: identical future cash flows cannot carry different prices. Now a dealer quotes one-year delivery of a stock currently trading at $100. What delivery price makes a new forward worth zero?

The dealer asks for a forecast. You refuse—not because forecasts are useless, but because another route to future delivery is already tradable.

## Two routes to the same share

Route A is the forward: agree now, pay `K` in one year, receive one share.

Route B is cash-and-carry: borrow $100 now, buy one share, hold it for a year. At 5% continuous interest the debt becomes `100e^0.05=$105.1271`. At maturity you repay it and still own the share.

If the stock pays no income and costs nothing to hold, both routes produce one share at the same date. Their future cash cost must match:

`F_0(T)=S_0e^(rT)`.

Here `F_0(T)` is today's fair delivery price for maturity `T`, not today's value of an existing forward. With `S_0=100`, `r=.05`, and `T=1`, it is $105.13.

## A complete example when the forward quote is too high

The fair one-year delivery price from the two matching routes is $105.13. Now suppose the dealer offers you this **different contract**:

> “Sign today. Exactly one year from today, you must deliver me one share. I will pay you **$110** for that share on that day.”

The `$110` is the dealer’s **quoted forward delivery price**. It is not today’s stock price. It is not a forecast of next year’s stock price. It is the amount the forward buyer promises to pay in one year for one share.

You take the seller’s side of that forward. In market language this is called being **short one forward**: you owe one share in a year and will receive $110 then. Here is the entire cash-flow table, assuming no fees, no dividends, and that borrowing/lending is available at 5%:

| Date | What you do | Cash from this action | What you hold or owe afterward |
|---|---|---:|---|
| Today | Borrow $100 | +$100 | Owe a loan that becomes $105.13 in one year |
| Today | Use the borrowed $100 to buy one share | -$100 | Own one share |
| Today | Sign the forward as seller | $0 | Owe one share in one year; will receive $110 then |
| One year | Deliver the share you already own | +$110 | No share; forward obligation is finished |
| One year | Repay the loan | -$105.13 | No loan |
| One year | Keep what remains | **+$4.87** | All obligations are finished |

The price of the share in one year does not change this result. If the share is worth $60, you still deliver it under the contract and receive $110. If it is worth $200, you still deliver it and receive $110. You already bought the required share today, so the future market price is irrelevant to this particular trade.

### What if the forward quote is too low?

If the dealer instead offered $100 for next year’s share, the difference from $105.13 is $5.13 in the other direction. The mirror trade would require selling a share today that you do not own, putting that sale money aside for a year, and agreeing to receive the share through the $100 forward later. That first action requires borrowing a share from someone else and agreeing to return it. Because availability and cost of borrowing that share can vary, do not call this mirror trade guaranteed until those facts are written down. The simple lesson remains: the high $110 quote is an arbitrage only because every required action and cash flow was made explicit.

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

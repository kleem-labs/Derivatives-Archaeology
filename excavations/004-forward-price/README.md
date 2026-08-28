# 004 — The Forward Price

**Vocabulary key:** Find **004** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **004** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

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

Now use the same starting facts: stock costs $100 today, one year of interest turns $100 into $105.13, and the stock pays no income. But imagine the dealer offers this contract instead:

> “Sign today. Exactly one year from today, you may pay **$100** and receive one share.”

The `$100` is now the quoted forward delivery price. It is $5.13 below the $105.13 cost of buying and carrying a share yourself. To capture that gap, you need to sell a borrowed share today and get the same share back through the cheap forward next year. This is the complete picture:

| Date | What you do | Cash from this action | What you hold or owe afterward |
|---|---|---:|---|
| Today | Borrow one share from a share lender | $0 | Owe that lender one share in one year |
| Today | Sell the borrowed share at today’s price | +$100 | Hold $100 cash; still owe one share |
| Today | Invest the $100 for one year at 5% | -$100 | Own an investment worth $105.13 in one year |
| Today | Sign the forward as buyer | $0 | May pay $100 for one share in one year |
| One year | Receive the investment money | +$105.13 | Hold $105.13 cash; still owe one share |
| One year | Use the forward: pay $100 and receive one share | -$100 | Own one share; no forward remains |
| One year | Return that share to the lender | $0 | No share; share-loan obligation is finished |
| One year | Keep what remains | **+$5.13** | All obligations are finished |

The future stock price again does not change the result: the forward supplies the share needed to return to the lender. But this table has extra promises that the $110 example did not need. Someone must lend the share, the share-lending fee must be known, and any dividend paid while the share is borrowed must be handled. In this simplified example, all three are assumed away. In a real market, they can shrink or remove the $5.13.

The simple lesson is the same in both directions: a price difference becomes arbitrage only after the full table shows that every obligation can be completed and every cost is covered.

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

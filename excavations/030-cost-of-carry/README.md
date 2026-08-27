# 030 — Cost of Carry

## First, in everyday words

Owning a physical thing until a later date can cost financing, storage, and insurance, while sometimes paying income or usefulness. Carry is the full ledger of those burdens and benefits. **For an AI helper:** itemize each one and stop if the asset cannot actually be bought, stored, financed, or delivered as assumed.

## Inventory is a portfolio

Chapter 004 carried a dividend-paying share. Mara's warehouse now forces the full physical version of the same question. Imagine a gold dealer promising one ounce in six months. To guarantee delivery, the dealer can borrow money, buy gold, insure it, store it, and deliver later. Every line in that physical route belongs in the forward relation.

If spot is $2,000, financing is 5%, storage and insurance act like a 1% continuous cost, and gold provides no monetary income, the idealized six-month forward is `2000e^((.05+.01).5)≈$2,060.91`. A quote far above invites cash-and-carry if the metal, credit, storage, and short forward are executable at those terms.

For financing rate `r`, storage cost `u`, and income yield `q`, the idealized relation is `F_0=S_0e^((r+u-q)T)`. The compact exponent is a net flow rate. Adding costs is forced because each increases the future cash needed to carry the asset. Subtracting income is forced because ownership pays something the forward holder misses.

## Why one participant's carry is not universal

A bank and a household borrow at different rates. A commodity producer may store cheaply while a financial trader cannot obtain warehouse capacity. A short seller pays borrow fees. Balance-sheet and collateral constraints make apparent arbitrage bands institution-specific.

Observed forwards can be used to infer an implied net carry, but the residual should not be casually named. It may contain convenience yield, funding, taxes, inventory scarcity, credit, or bad data.

## The design question

For a derivative on a non-traded index—say construction cost—there may be no cash-and-carry portfolio. A forward price then requires expectation and risk premium rather than mechanical carry. Before applying the formula, ask whether the underlying can actually be owned, financed, stored, and delivered.

> **Memory seal:** every burden and benefit of ownership receives a line in the carry ledger. Anything omitted returns later as false arbitrage.

[Next: Dividends and Income](../031-dividends-and-income/README.md)

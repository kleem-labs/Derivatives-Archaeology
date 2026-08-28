# 000 — A Promise About the Future

**Vocabulary key:** Find **000** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

A derivative starts as a promise about a later day. This chapter asks only: who must pay what when that day arrives? **For an AI helper:** copy the promise into plain words and show the result for a few possible future prices before attempting any valuation.

In September, while wheat still stands green in the field, Mara already knows the number that can ruin her farm. It is not the harvest size. It is the price offered in March, when the loan on her equipment comes due.

Across town, Arun owns a bakery. The same March price threatens him from the opposite direction. If wheat rises, flour may become too expensive for the bread prices printed in contracts he has signed with schools.

They meet without knowing what March wheat will cost. Mara fears $4 per bushel. Arun fears $9. Neither can make uncertainty disappear. But perhaps they can change who carries it.

## The first decision

They agree today that Arun will buy 10,000 bushels from Mara in March for $6 per bushel. No wheat moves today. Ignore credit risk for one chapter.

Before reading further, decide what the agreement is worth to Arun in March:

| March market price | Contract price | Value to Arun per bushel |
|---:|---:|---:|
| $4 | $6 | ? |
| $6 | $6 | ? |
| $9 | $6 | ? |

At $9, Arun receives wheat worth $9 while paying $6: the agreement contributes $3. At $4, he must pay $2 above market: it contributes negative $2. At $6 it contributes zero.

If `S_T` is March market price and `K` is delivery price, Arun's value per bushel at delivery is `S_T-K`. Mara receives the negative, `K-S_T`. Before default and costs, their values add to zero. The agreement did not create wheat-price wealth. It transferred wheat-price risk.

## The tempting shortcut

Arun asks what the agreement is worth today. A tempting answer is: “Estimate the average March price and subtract $6.” If he predicts $7, he calls it worth $1 per bushel.

But Mara predicts $5.50. Which expectation becomes the price? Averaging forecasts hides disagreement. It also ignores when money is paid, whether delivery can be reproduced using traded wheat and borrowing, and whether risk commands compensation.

The failure separates three objects:

1. **The contract** specifies cash flows in each state.
2. **A forecast** assigns real-world beliefs to states.
3. **A price** is what the claim trades for today, constrained by alternatives.

These can be connected by a model, but they are not definitions of one another.

## What has been invented

A derivative is a contract whose cash flows depend on an underlying observable. The underlying might be wheat, a stock, an interest rate, rainfall, freight cost, electricity use, or a credit event. The derivative is not the underlying. It is a rule that watches the underlying and determines obligations.

Mara and Arun created a forward: obligations for both sides. Yet Arun's original wish was not merely to replace an unknown price with $6. He feared high prices. If wheat becomes cheap, the forward prevents him from enjoying that benefit. The contract solved more of his problem than he asked it to solve.

Before repairing that mismatch, resist pricing. We have not yet written enough of the artifact to know what is being valued. The next task is to separate the cash-flow rule from every opinion about it.

> **Memory seal — the bound wheat sheaf:** two signatures are tied to one future harvest. The harvest remains uncertain; the signatures decide who bears each side of its price.

## Excavation questions

1. If the contract covers 10,000 bushels and March wheat is $8.20, calculate each party's value.
2. Does a zero-sum payoff imply that both parties cannot benefit? Explain using risk reduction.
3. Design a one-line rainfall derivative. Which words remain too ambiguous to enforce?

## The pressure carried forward

We tried to price before describing the artifact. The repair is to map the contract across states first.

[Next: Payoffs Before Prices](../001-payoffs-before-prices/README.md)

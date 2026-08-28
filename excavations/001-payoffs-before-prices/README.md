# 001 — Payoffs Before Prices

**Vocabulary key:** Find **001** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

Draw three pictures: wheat is cheap, ordinary, or expensive. In each picture, ask what the promise gives Arun.

### In finance language

A payoff table lists the contract’s result in each future state. It comes before a price because we cannot value a rule we have not described.

Before asking whether a contract is cheap or expensive, make a small table showing what it gives and takes in good, ordinary, and bad futures. **For an AI helper:** create that table from the contract language; do not begin with a forecast or a chart.

The wheat agreement was linear: every one-dollar rise helped Arun by one dollar and hurt Mara by one dollar. Now Arun wants protection from high prices without giving up low prices.

An insurer offers a new promise: in March, Arun may buy wheat for $6, but is not required to. If wheat is $4, he walks away. If it is $9, he uses the promise.

That word—**may**—changes the shape of the contract.

## Place the contract in three worlds

| Market wheat `S_T` | Use the right at `K=6`? | Saving per bushel |
|---:|---|---:|
| $4 | No | $0 |
| $6 | Indifferent | $0 |
| $9 | Yes | $3 |

Writing `S_T-K` would make the first row negative $2. But the owner can refuse. Negative exercise value becomes zero:

`right's payoff = max(S_T-K,0)`.

The maximum records a legal right. Removing it turns the right into an obligation. We will give formal names to the right to buy and the opposite right to sell only after we have learned how dates and equal-price rules work.

## Why the picture comes before the premium

Draw this right's payoff against terminal price. It lies flat at zero below `K` and rises one-for-one above it. The bend at `K` is the important shape.

Now someone says, “This right is worth $3 because it could pay $3.” That confuses one possible payoff with today's value. The market price could finish somewhere else. Cash paid today also has a date attached. The person who sold the right must accept the opposite side of the shape.

Even `max(S_0-K,0)` is only the value of using the right immediately. A right that would be useless today can still have a positive price because time remains. That extra amount is not a separate treasure inside the contract; it is the price of having time to choose.

## Payoffs as building material

Two purchase-rights with different agreed prices can be combined to make a payoff that rises for a while and then stops rising. We do not need its market name yet; the important lesson is that simple cash-flow shapes can be added together to make a new one.

But a terminal picture ignores dates. A guaranteed $100 next year is not $100 now. The next chapter repairs that missing date.

> **Memory seal — the one-way door:** below strike the owner walks away; above it the door opens into a rising corridor.

## Excavation questions

1. Make a payoff table for the right to sell wheat at $6 at terminal prices $4, $6, and $9.
2. Draw a payoff that rises from zero and then stops rising at $15. Describe it in ordinary words; do not give it a strategy name.
3. Explain why a payoff diagram cannot determine today's premium.

[Previous: A Promise](../000-a-promise-about-the-future/README.md) · [Next: Time Has a Price](../002-time-value-of-money/README.md)

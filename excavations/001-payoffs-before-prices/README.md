# 001 — Payoffs Before Prices

**Vocabulary key:** Find **001** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

Before asking whether a contract is cheap or expensive, make a small table showing what it gives and takes in good, ordinary, and bad futures. **For an AI helper:** create that table from the contract language; do not begin with a forecast or a chart.

The wheat agreement was linear: every one-dollar rise helped Arun by one dollar and hurt Mara by one dollar. Now Arun wants protection from high prices without giving up low prices.

An insurer offers a new promise: in March, Arun may buy wheat for $6, but is not required to. If wheat is $4, he walks away. If it is $9, he exercises.

That word—**may**—changes the shape of the contract.

## Place the contract in three worlds

| Market wheat `S_T` | Exercise at `K=6`? | Saving per bushel |
|---:|---|---:|
| $4 | No | $0 |
| $6 | Indifferent | $0 |
| $9 | Yes | $3 |

Writing `S_T-K` would make the first row negative $2. But the owner can refuse. Negative exercise value becomes zero:

`call payoff = max(S_T-K,0)`.

The maximum records a legal right. Removing it turns an option into an obligation. A put contains the opposite right—sell at `K` when market is lower—so `put payoff=max(K-S_T,0)`.

## Why the picture comes before the premium

Draw call payoff against terminal price. It lies flat at zero below strike and rises one-for-one above it. The bend at `K` is the option's central geometry.

Now someone says, “The call is worth $3 because it could pay $3.” That confuses one possible payoff with today's value. The underlying could finish elsewhere. Cash paid today has financing value. Volatility changes how often and how far price reaches the rising side. The seller must accept asymmetry.

Even intrinsic value, `max(S_0-K,0)`, is only immediate exercise value. An out-of-the-money option can have positive price because time remains. “Time value” is not a separate treasure inside the contract; it is price beyond intrinsic value.

## Payoffs as building material

A long call at $100 plus a short call at $120 produces zero below $100, rises between the strikes, and is capped at $20 above $120. This call spread exchanges unlimited upside for lower premium.

New derivatives can be engineered by combining cash, stock, calls, and puts until the terminal cash-flow rule matches the desired exposure. But a terminal picture ignores dates. A guaranteed $100 next year is not $100 now.

> **Memory seal — the one-way door:** below strike the owner walks away; above it the door opens into a rising corridor.

## Excavation questions

1. Make payoff tables for long and short puts struck at $90 at terminal prices $60, $90, and $120.
2. Construct a payoff capped at $15 using two calls.
3. Explain why a payoff diagram cannot determine today's premium.

[Previous: A Promise](../000-a-promise-about-the-future/README.md) · [Next: Time Has a Price](../002-time-value-of-money/README.md)

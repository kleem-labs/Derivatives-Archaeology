# 018 — Change of Measure: Reweighting Paths for Pricing

**Vocabulary key:** Find **018** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

Keep every picture in the same picture book, but give the pictures different-sized votes when you answer a different question.

### In finance language

A change of measure reweights the same possible paths. The real-world measure supports beliefs; the pricing measure supports no-arbitrage valuation.

The same possible paths can be viewed with different weights depending on the question being asked. Pricing weights help value a copy; real-world weights address a belief or forecast. **For an AI helper:** never mix these two jobs in one unlabeled probability column.

## Keep the paths, alter the voting weights

The delta hedge removed `mu` from the pricing equation, but a probability description of the original stock process still contains it. Imagine a cinema showing every possible one-year stock path. Under the real-world measure `P`, paths receive weights reflecting estimated occurrence and risk premia. Under pricing measure `Q`, the film library remains—equivalent measures agree on impossible events—but the votes are reassigned so appropriately discounted tradable gains have no drift.

Why is this legitimate? Replication already fixed the claim's price. The new weights are a coordinate system that reproduces that price by expectation. They do not rewrite physical frequency.

With continuous dividend yield `q`, risk-neutral stock drift becomes `r-q`. The stock itself is not expected to grow at `r` after ignoring dividends; total discounted gains are the relevant object.

Girsanov's theorem provides the formal change under suitable conditions. A replicable payoff can then be written `V_0=E^Q[e^(-rT)payoff]` for constant rates. This expectation has not replaced replication; it is replication written as a weighted sum over paths.

## One calculation, two questions

Suppose a call is priced under `Q` at $8. A portfolio manager may still use `P` to estimate that its expected future profit is negative, positive, or highly skewed. The pricing question asks what is consistent with replicating instruments. The investment question asks whether the executable price is attractive under beliefs, risk appetite, funding, and constraints.

Confusing the measures produces two opposite errors. Treating `Q` as a forecast mistakes market pricing weights for physical odds. Treating a bullish `P` forecast as a no-arbitrage valuation ignores how risk is priced and hedged.

## Incomplete markets reopen choice

When every relevant claim is replicable, the matching pricing measure is effectively unique. When jumps or stochastic factors are unspanned, multiple equivalent martingale measures can exist. Choosing among them introduces extra economic assumptions or calibration targets.

> **Memory seal:** the same path film plays twice. The audience under `P` votes for likelihood; the audience under `Q` votes until tradable discounted prices balance.

## Excavation questions

1. Explain why a risk-neutral measure does not imply risk-neutral investors.
2. Name a decision requiring `P` rather than `Q`.
3. What becomes non-unique when replication fails?

Changing weights has given us `Q`, but the phrase “discounted gains have no drift” still hides the unit of measurement. The final key is to choose that measuring asset explicitly.

[Next: Martingales and Numeraires](../019-martingales-and-numeraires/README.md)

# 013 — Expectation and Variance: Center and Spread

**Vocabulary key:** Find **013** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **013** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Two jars can have the same average number of candies even when one jar has wildly different handfuls. Average and wobble are different ideas.

### In finance language

Expectation is the weighted average; variance measures squared spread around that average. Neither says which one outcome must occur.

An average tells us where a collection of possible outcomes is centered; spread tells us how widely those outcomes can wander. Neither number is a promise of what will happen. **For an AI helper:** show the scenarios and weights behind every average, then show how far outcomes can sit from it.

## Let two lotteries expose the mean

Chapter 012 separated state labels from their weights. Now let the weights act. Portfolio A pays $100 with certainty. Portfolio B pays $50 or $150 with equal probability. Both have expectation $100, yet a $100 call on the payoff is worthless for A and pays either $0 or $50 for B. Its expected payoff under these illustrative weights is $25.

The mean preserves center while discarding shape. Variance restores one measure of spread: B's deviations are `-50` and `+50`; squaring makes both 2,500, and their average variance is 2,500. Standard deviation is $50. A's variance is zero.

Why square instead of taking raw deviations? Raw deviations around the mean cancel by construction. Absolute deviations could measure spread, but squared deviations interact cleanly with algebra, independent sums, least squares, and Brownian scaling. The choice buys mathematical structure while making tail observations disproportionately influential.

## Convexity is the option's appetite for spread

Return to the two portfolio stories and write the option result beside each one:

| Story | Possible portfolio payment | Call’s result with $100 agreed price | Average call result |
|---|---|---:|---:|
| Still story | $100 for certain | $0 | $0 |
| Wide story | $50 half the time; $150 half the time | $0 or $50 | `(0 + 50) ÷ 2 = $25` |

Both stories have the same average portfolio payment: $100. But the call does not turn the low $50 outcome into a negative number; it gives $0. It keeps the $50 saving in the high $150 outcome. The payoff line bends upward instead of being a straight line. We call that upward-bending shape **convex**.

Only now is the short mathematical sentence useful. Write `E[thing]` to mean “take the weighted average of `thing`.” Write `f(X)` to mean “apply a payoff rule `f` to an uncertain payment `X`.” Then

`E[f(X)] >= f(E[X])`

says exactly what the table showed: for a convex payoff, averaging the payoff across the wide story can be at least as large as applying the payoff to the average result first. This statement is called Jensen’s inequality. It is a description of payoff shape under stated weights; it does not by itself set an option’s market price. “Higher variance always means higher price” remains too loose when distributions change in several ways.

## Worked decision

Suppose a put pays $40, $0, and $0 in states carrying weights .2, .5, and .3. Its weighted payoff is `$8`. The arithmetic is clear; the economic status of the weights is not. Are they a forecast, observed frequencies, or weights forced by traded prices? Expectation can gather outcomes only after someone supplies the weights, and the resulting number inherits their meaning.

> **Retrieval challenge:** construct two three-state distributions with equal mean and variance but different call expected payoffs. This proves mean and variance still do not contain the whole option-relevant shape.

The next problem is shape. We need a distribution for a positive price produced by many multiplying returns; a normal distribution placed directly on prices leaks into negative values.

[Next: Normal and Lognormal Models](../014-normal-and-lognormal/README.md)

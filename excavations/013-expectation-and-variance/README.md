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

The call function bends upward. Draw a chord between any two payoff points; the function lies below or on that chord. Jensen's inequality compresses this geometry into `E[f(X)] >= f(E[X])` for convex `f`. More spread can add expected payoff when the mean is held fixed, but only under a precise comparison such as a mean-preserving spread. “Higher variance always means higher price” is too loose when distributions change in several ways.

## Worked decision

Suppose a put pays $40, $0, and $0 in states carrying weights .2, .5, and .3. Its weighted payoff is `$8`. The arithmetic is clear; the economic status of the weights is not. Are they a forecast, observed frequencies, or weights forced by traded prices? Expectation can gather outcomes only after someone supplies the weights, and the resulting number inherits their meaning.

> **Retrieval challenge:** construct two three-state distributions with equal mean and variance but different call expected payoffs. This proves mean and variance still do not contain the whole option-relevant shape.

The next problem is shape. We need a distribution for a positive price produced by many multiplying returns; a normal distribution placed directly on prices leaks into negative values.

[Next: Normal and Lognormal Models](../014-normal-and-lognormal/README.md)

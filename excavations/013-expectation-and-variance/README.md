# 013 — Expectation and Variance: Center and Spread

Two stocks can share an expected one-year price of $100 while one stays near $100 and the other swings between $50 and $150. The mean alone discards the risk that gives options value.

Expectation is a probability-weighted sum, `E[X]=sum p_i x_i`, or its continuous integral. Variance measures squared distance from the mean: `Var(X)=E[(X-E[X])^2]`. Squaring prevents positive and negative deviations from cancelling; the square root returns standard deviation to the original units.

Expected payoff is generally not payoff at the expected price. Because a call payoff is convex, `E[max(S_T-K,0)] >= max(E[S_T]-K,0)`. This is why plugging the expected stock price into the payoff underprices optionality. Mean and variance still do not specify a whole distribution; tails and skew matter.

## Let two lotteries expose the mean

Portfolio A pays $100 with certainty. Portfolio B pays $50 or $150 with equal probability. Both have expectation $100, yet a $100 call on the payoff is worthless for A and pays either $0 or $50 for B. Its expected payoff under these illustrative weights is $25.

The mean preserves center while discarding shape. Variance restores one measure of spread: B's deviations are `-50` and `+50`; squaring makes both 2,500, and their average variance is 2,500. Standard deviation is $50. A's variance is zero.

Why square instead of taking raw deviations? Raw deviations around the mean cancel by construction. Absolute deviations could measure spread, but squared deviations interact cleanly with algebra, independent sums, least squares, and Brownian scaling. The choice buys mathematical structure while making tail observations disproportionately influential.

## Convexity is the option's appetite for spread

The call function bends upward. Draw a chord between any two payoff points; the function lies below or on that chord. Jensen's inequality compresses this geometry into `E[f(X)] >= f(E[X])` for convex `f`. More spread can add expected payoff when the mean is held fixed, but only under a precise comparison such as a mean-preserving spread. “Higher variance always means higher price” is too loose when distributions change in several ways.

Expectation used in pricing must also name its measure. `E^P` may describe real-world beliefs; `E^Q` may describe risk-neutral pricing weights. The operation is the same weighted gathering, but the weights answer different questions.

## Worked decision

Suppose a put pays $40, $0, and $0 in states with probabilities .2, .5, and .3. Expected payoff is `$8`. If those are risk-neutral weights and the one-year discount factor is .95, model value is $7.60. If they are subjective forecasting weights, $7.60 is not automatically an arbitrage-free price.

> **Retrieval challenge:** construct two three-state distributions with equal mean and variance but different call expected payoffs. This proves mean and variance still do not contain the whole option-relevant shape.

[Next: Normal and Lognormal Models](../014-normal-and-lognormal/README.md)

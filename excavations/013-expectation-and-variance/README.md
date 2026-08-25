# 013 — Expectation and Variance: Center and Spread

Two stocks can share an expected one-year price of $100 while one stays near $100 and the other swings between $50 and $150. The mean alone discards the risk that gives options value.

Expectation is a probability-weighted sum, `E[X]=sum p_i x_i`, or its continuous integral. Variance measures squared distance from the mean: `Var(X)=E[(X-E[X])^2]`. Squaring prevents positive and negative deviations from cancelling; the square root returns standard deviation to the original units.

Expected payoff is generally not payoff at the expected price. Because a call payoff is convex, `E[max(S_T-K,0)] >= max(E[S_T]-K,0)`. This is why plugging the expected stock price into the payoff underprices optionality. Mean and variance still do not specify a whole distribution; tails and skew matter.

Next: [Normal and Lognormal Models](../014-normal-and-lognormal/README.md).


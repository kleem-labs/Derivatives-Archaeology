# 036 — Minimum-Variance Hedge Ratio

**Vocabulary key:** Find **036** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **036** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

If two dancing partners do not step exactly together, choose the partner size that makes the combined dance wobble least.

### In finance language

The minimum-variance hedge ratio uses covariance and variance to choose the futures amount that historically minimizes residual price variation.

When the contract is only an imperfect stand-in for the real risk, choose a hedge size that has historically reduced the combined wobble the most. It reduces risk; it does not erase it. **For an AI helper:** display the data window, correlation, units, and residual risk rather than treating the ratio as timeless.

## Let the residual choose the slope

The quantity match in Chapter 035 silently assumed cash and futures changed one-for-one. Let their observed changes be `Delta S` and `Delta F`, and write hedged change as `Delta S-hDelta F`. Which `h` makes that residual as quiet as possible?

Write hedged change as `Delta S-hDelta F`. Its variance expands to `Var(Delta S)+h²Var(Delta F)-2hCov(Delta S,Delta F)`. Differentiate with respect to `h`, set the slope to zero, and solve:

`h*=Cov(Delta S,Delta F)/Var(Delta F)`.

The ratio is the regression coefficient of spot changes on futures changes. Division by futures variance answers: how much cash-exposure movement accompanies one unit of futures movement on average?

If spot standard deviation is 3%, futures is 2.5%, and correlation .8, `h*=.8×.03/.025=.96`. Near one, but not assumed to be one.

## The sample is part of the hedge

Daily versus weekly changes, rolling window, crisis observations, seasonal periods, and currency conversion change covariance. A structural break can make a precise historical estimate irrelevant. Confidence intervals and stability plots are more honest than one coefficient.

Minimum variance also assumes variance is the objective and the relation is linear. A firm concerned with cash-flow-at-risk, downside shortfall, margin calls, or accounting may select another ratio. Tail dependence can remain even when ordinary correlation looks strong.

## From ratio to executable contracts

Multiply `h*` by exposure quantity divided by contract quantity, then round to an integer and inspect residual. Recalculate after exposure, volatility, or basis changes; the estimate is not a permanent property of the commodities.

> **Memory seal:** the regression compass aligns with co-movement, not with names printed on the two assets.

The hedge can now span quantities and observed co-movement, but its cash flows occur on several dates. One universal rate can no longer carry every payment without contradiction. The discount curve must be reconstructed date by date.

[Next: Bootstrapping Discount Curves](../037-bootstrapping-discount-curves/README.md) · [Lab function](../../labs/advanced_lab.py)

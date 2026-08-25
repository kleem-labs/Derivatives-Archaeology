# 043 — Monte Carlo: Pricing by Repeated Worlds

Risk-neutral valuation suggests an algorithm: simulate paths under the pricing measure, compute each discounted payoff, and average. The standard error shrinks only as `1/sqrt(N)`, so one hundred times as many paths gives about ten times the precision.

Confidence intervals quantify sampling error, not model error. Antithetic variables, control variates, stratification, and quasi-random sequences can reduce variance. A fixed seed helps reproduce a run but does not make the estimator exact.

Monte Carlo excels in many dimensions and path dependence, but ordinary simulation handles early exercise poorly because the decision depends on conditional continuation value.

## Build the estimator visibly

For each simulated risk-neutral path: generate shocks, evolve state variables, compute contract payoff exactly as written, discount it, and store the result. The sample mean estimates model value. Sample standard deviation divided by `sqrt(N)` estimates standard error.

If a call estimate is $8.03 with standard error $0.09, an approximate 95% sampling interval is $8.03 ± $0.18. Reporting $8.032763 without the interval advertises digits the experiment did not earn.

## Make one simulated world pay for another

Antithetic variates pair shock `Z` with `-Z`. A control variate uses a related claim with known value—perhaps the underlying or vanilla option—to correct shared simulation noise. These methods reduce variance without changing the model. Quasi-random sequences fill dimensions more evenly but require careful error assessment.

Convergence at `1/sqrt(N)` is slow: reducing standard error by ten requires roughly one hundred times the paths. Computational effort should target the payoff features causing variance.

## Validation before trust

Price a vanilla claim whose closed form is known. Confirm the analytical price lies inside repeated confidence intervals. Test seeds, time-step refinement, pathwise payoff logic, discounting, and extreme inputs. Sampling confidence says nothing about whether geometric Brownian motion is appropriate.

American exercise is harder because continuation value is conditional on current state. Least-squares Monte Carlo estimates it by regression, adding approximation and policy bias.

> **Memory seal:** thousands of possible worlds pour discounted cash into one bowl. The wobble of the average is measured; the truth of the world generator is not.

[Next: Finite Differences](../044-finite-differences/README.md) · [Monte Carlo lab](../../labs/advanced_lab.py)

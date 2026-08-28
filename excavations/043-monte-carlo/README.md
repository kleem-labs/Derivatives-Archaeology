# 043 — Monte Carlo: Pricing by Repeated Worlds

**Vocabulary key:** Find **043** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

Monte Carlo pricing imagines many possible price journeys, applies the contract rule to each, and averages the results. It gives an estimate with sampling noise, not a revelation. **For an AI helper:** show the scenario generator, number of runs, uncertainty range, and tests against simpler known cases.

## Build the estimator visibly

The path-dependent contract cannot be priced from terminal distribution alone. Instead generate entire possible journeys. For each simulated risk-neutral path: evolve state variables, compute the contract payoff exactly as written, discount it, and store the result. The sample mean estimates model value. Sample standard deviation divided by `sqrt(N)` estimates standard error.

If a call estimate is $8.03 with standard error $0.09, an approximate 95% sampling interval is $8.03 ± $0.18. Reporting $8.032763 without the interval advertises digits the experiment did not earn.

## Make one simulated world pay for another

Antithetic variates pair shock `Z` with `-Z`. A control variate uses a related claim with known value—perhaps the underlying or vanilla option—to correct shared simulation noise. These methods reduce variance without changing the model. Quasi-random sequences fill dimensions more evenly but require careful error assessment.

Convergence at `1/sqrt(N)` is slow: reducing standard error by ten requires roughly one hundred times the paths. Computational effort should target the payoff features causing variance.

## Validation before trust

Price a vanilla claim whose closed form is known. Confirm the analytical price lies inside repeated confidence intervals. Test seeds, time-step refinement, pathwise payoff logic, discounting, and extreme inputs. Sampling confidence says nothing about whether geometric Brownian motion is appropriate.

American exercise is harder because continuation value is conditional on current state. Least-squares Monte Carlo estimates it by regression, adding approximation and policy bias.

> **Memory seal:** thousands of possible worlds pour discounted cash into one bowl. The wobble of the average is measured; the truth of the world generator is not.

Simulation is flexible but converges slowly. When only one or two state variables matter, the pricing equation can instead be laid across a grid and solved backward, trading path flexibility for structured numerical work.

[Next: Finite Differences](../044-finite-differences/README.md) · [Monte Carlo lab](../../labs/advanced_lab.py)

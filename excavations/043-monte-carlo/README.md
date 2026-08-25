# 043 — Monte Carlo: Pricing by Repeated Worlds

Risk-neutral valuation suggests an algorithm: simulate paths under the pricing measure, compute each discounted payoff, and average. The standard error shrinks only as `1/sqrt(N)`, so one hundred times as many paths gives about ten times the precision.

Confidence intervals quantify sampling error, not model error. Antithetic variables, control variates, stratification, and quasi-random sequences can reduce variance. A fixed seed helps reproduce a run but does not make the estimator exact.

Monte Carlo excels in many dimensions and path dependence, but ordinary simulation handles early exercise poorly because the decision depends on conditional continuation value.

Next: [Finite Differences](../044-finite-differences/README.md).


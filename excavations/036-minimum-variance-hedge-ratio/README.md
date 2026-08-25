# 036 — Minimum-Variance Hedge Ratio

Let changes in the cash exposure and futures price be `Delta S` and `Delta F`. Minimizing the variance of `Delta S-h Delta F` gives

`h* = Cov(Delta S,Delta F)/Var(Delta F) = rho sigma_S/sigma_F`.

The ratio is a regression slope: futures units chosen to offset historical co-movement. If correlation is imperfect, residual basis risk remains.

Estimates depend on window, frequency, regime, and whether variance is the real objective. Tail loss, cash flow, or accounting criteria can justify a different hedge.

Next: [Bootstrapping Discount Curves](../037-bootstrapping-discount-curves/README.md).


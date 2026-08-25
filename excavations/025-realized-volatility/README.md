# 025 — Realized Volatility: Measuring the Path That Happened

Given log returns `r_i=ln(S_i/S_{i-1})`, realized variance is commonly estimated from their squared sum and annualized; realized volatility is its square root. Squaring prevents signs from cancelling and makes large moves count disproportionately.

Sampling sparsely misses intraday variation; sampling too finely amplifies bid–ask bounce and market noise. Close-to-close, range-based, and high-frequency estimators answer different questions.

Realized volatility is backward-looking and estimator-dependent. Option-model `sigma` is forward-looking and model-dependent. Equating them confuses a measured path with a price coordinate.

Next: [Implied Volatility](../026-implied-volatility/README.md).


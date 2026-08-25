# 027 — The Volatility Smile: One Sigma Is Not Enough

Black–Scholes assumes one volatility for all strikes at a maturity. Markets imply different volatilities: equity downside puts often trade at higher implied volatility than upside calls, producing skew; other assets show smiles.

This is evidence that one constant-lognormal model cannot fit all prices. The implied-volatility surface is a price map in familiar coordinates. Static arbitrage still constrains it: call prices decrease with strike, remain convex in strike, and obey calendar consistency under suitable conditions. A smooth interpolation can violate these economics.

Next: [Local and Stochastic Volatility](../028-local-and-stochastic-volatility/README.md).


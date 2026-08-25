# 027 — The Volatility Smile: One Sigma Is Not Enough

Black–Scholes assumes one volatility for all strikes at a maturity. Markets imply different volatilities: equity downside puts often trade at higher implied volatility than upside calls, producing skew; other assets show smiles.

This is evidence that one constant-lognormal model cannot fit all prices. The implied-volatility surface is a price map in familiar coordinates. Static arbitrage still constrains it: call prices decrease with strike, remain convex in strike, and obey calendar consistency under suitable conditions. A smooth interpolation can violate these economics.

## Read the surface as evidence

Collect calls and puts across strikes for one expiry. Convert executable quotes into implied volatilities using consistent forwards and discounting. If one lognormal distribution priced all options, the points would lie on one horizontal line. They rarely do.

In equity indexes, downside strikes often carry higher implied volatility. One interpretation is crash risk plus demand for protection; leverage effects and stochastic volatility also generate negative spot–volatility correlation. The smile is not itself a causal explanation. It is the shape any explanation must fit.

Across maturities, the surface becomes three-dimensional. Event dates can create short-maturity bumps. Long maturities reflect persistent uncertainty and supply-demand structure. Comparing raw strikes across spot levels is awkward, so practitioners use moneyness, log-moneyness, or delta—each with conventions.

## Static arbitrage is visible in shape

Call price must decline as strike rises and remain convex in strike: a butterfly combination cannot have negative cost and nonnegative payoff. Calendar relations constrain total variance across maturity under appropriate forward conventions. Interpolating implied volatilities with a pretty spline can violate these price constraints.

## A market-reading decision

A downside put at 30% implied volatility is not automatically expensive because at-the-money volatility is 20%. Its states and hedge behavior differ. Ask whether the relative skew exceeds your scenario value after crash probabilities, gap hedging, bid–ask spread, and capital.

> **Memory seal:** the once-flat volatility smile bends under the weight of downside insurance. Every model must carry that visible asymmetry.

[Next: Local and Stochastic Volatility](../028-local-and-stochastic-volatility/README.md)

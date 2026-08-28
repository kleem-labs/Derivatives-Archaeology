# 027 — The Volatility Smile: One Sigma Is Not Enough

**Vocabulary key:** Find **027** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

Different strikes and expiries often imply different volatility numbers because one simple model cannot describe every market fear. The smile is evidence, not a nuisance to hide. **For an AI helper:** show the surface by strike and date and refuse a single-volatility conclusion when the differences matter.

## Read the surface as evidence

One quote produced one implied volatility. Now repeat the inversion. Collect calls and puts across strikes for one expiry. Convert executable quotes using consistent forwards and discounting. If one constant-lognormal distribution priced all options, the points would lie on one horizontal line. They rarely do.

In equity indexes, downside strikes often carry higher implied volatility. One interpretation is crash risk plus demand for protection; leverage effects and stochastic volatility also generate negative spot–volatility correlation. The smile is not itself a causal explanation. It is the shape any explanation must fit.

Across maturities, the surface becomes three-dimensional. Event dates can create short-maturity bumps. Long maturities reflect persistent uncertainty and supply-demand structure. Comparing raw strikes across spot levels is awkward, so practitioners use moneyness, log-moneyness, or delta—each with conventions.

## Static arbitrage is visible in shape

Call price must decline as strike rises and remain convex in strike: a butterfly combination cannot have negative cost and nonnegative payoff. Calendar relations constrain total variance across maturity under appropriate forward conventions. Interpolating implied volatilities with a pretty spline can violate these price constraints.

## A market-reading decision

A downside put at 30% implied volatility is not automatically expensive because at-the-money volatility is 20%. Its states and hedge behavior differ. Ask whether the relative skew exceeds your scenario value after crash probabilities, gap hedging, bid–ask spread, and capital.

> **Memory seal:** the once-flat volatility smile bends under the weight of downside insurance. Every model must carry that visible asymmetry.

The surface has diagnosed failure but has not supplied dynamics. A barrier or forward-start option will care how today's skew moves after spot changes. The next excavation constructs two different motion rules that can fit the same present surface.

[Next: Local and Stochastic Volatility](../028-local-and-stochastic-volatility/README.md)

# 018 — Change of Measure: Reweighting Paths for Pricing

Real-world dynamics may have drift `mu`, reflecting growth expectations and risk premia. Yet the Black–Scholes price does not contain `mu`. Replication removed the stock's instantaneous shock and with it the need to know expected return.

Girsanov's theorem formalizes the repair by changing probability weights. Under an equivalent risk-neutral measure `Q`, a tradable stock with continuous yield `q` can be written `dS=(r-q)Sdt+sigma SdW^Q`. Possible paths are not erased; their weights change so discounted gains processes have zero drift. Then `V_0 = E^Q[e^(-rT) payoff]` for a replicable claim.

This is not permission to use pricing probabilities for real risk management. Forecasting and pricing answer different questions.

## Keep the paths, alter the voting weights

Imagine a cinema showing every possible one-year stock path. Under the real-world measure `P`, paths receive weights reflecting estimated occurrence and risk premia. Under pricing measure `Q`, the film library remains—equivalent measures agree on impossible events—but the votes are reassigned so appropriately discounted tradable gains have no drift.

Why is this legitimate? Replication already fixed the claim's price. The new weights are a coordinate system that reproduces that price by expectation. They do not rewrite physical frequency.

With continuous dividend yield `q`, risk-neutral stock drift becomes `r-q`. The stock itself is not expected to grow at `r` after ignoring dividends; total discounted gains are the relevant object.

## One calculation, two questions

Suppose a call is priced under `Q` at $8. A portfolio manager may still use `P` to estimate that its expected future profit is negative, positive, or highly skewed. The pricing question asks what is consistent with replicating instruments. The investment question asks whether the executable price is attractive under beliefs, risk appetite, funding, and constraints.

Confusing the measures produces two opposite errors. Treating `Q` as a forecast mistakes market pricing weights for physical odds. Treating a bullish `P` forecast as a no-arbitrage valuation ignores how risk is priced and hedged.

## Incomplete markets reopen choice

When every relevant claim is replicable, the matching pricing measure is effectively unique. When jumps or stochastic factors are unspanned, multiple equivalent martingale measures can exist. Choosing among them introduces extra economic assumptions or calibration targets.

> **Memory seal:** the same path film plays twice. The audience under `P` votes for likelihood; the audience under `Q` votes until tradable discounted prices balance.

## Excavation questions

1. Explain why a risk-neutral measure does not imply risk-neutral investors.
2. Name a decision requiring `P` rather than `Q`.
3. What becomes non-unique when replication fails?

[Next: Martingales and Numeraires](../019-martingales-and-numeraires/README.md)

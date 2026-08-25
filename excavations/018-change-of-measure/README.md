# 018 — Change of Measure: Reweighting Paths for Pricing

Real-world dynamics may have drift `mu`, reflecting growth expectations and risk premia. Yet the Black–Scholes price does not contain `mu`. Replication removed the stock's instantaneous shock and with it the need to know expected return.

Girsanov's theorem formalizes the repair by changing probability weights. Under an equivalent risk-neutral measure `Q`, a tradable stock with continuous yield `q` can be written `dS=(r-q)Sdt+sigma SdW^Q`. Possible paths are not erased; their weights change so discounted gains processes have zero drift. Then `V_0 = E^Q[e^(-rT) payoff]` for a replicable claim.

This is not permission to use pricing probabilities for real risk management. Forecasting and pricing answer different questions.

Next: [Martingales and Numeraires](../019-martingales-and-numeraires/README.md).


# 045 — Transaction Costs and Discrete Hedging

Continuous rebalancing requires infinite trades. With bid–ask spreads and fees, trading ever more frequently can increase cost even as model tracking improves.

Discrete hedging leaves gamma exposure between trades. The resulting P&L depends on realized path, implied versus realized volatility, jump risk, and execution. No single frictionless replication price survives unchanged; costs can create a no-arbitrage interval.

Hedge frequency is an optimization among tracking error, transaction cost, liquidity, and operational capacity—not a race toward continuous time.

## The impossible instruction

Black–Scholes replication says trade continuously. If each trade crosses a spread, infinitely frequent rebalancing creates unbounded cumulative cost. The ideal repair and the market friction collide.

Trade rarely and gamma produces tracking error between hedge times. Trade often and costs rise. A practical policy chooses a clock or delta band: rebalance when exposure exits a tolerance rather than after every tiny move. The optimum depends on spread, gamma, volatility, risk limits, and inventory.

## Separate sources of hedge P&L

Maintain a ledger containing option mark change, delta stock P&L, financing, dividends, transaction cost, and residual. In a smooth model, much residual can be understood through gamma times realized squared movement versus theta implied by priced volatility. Jumps, surface changes, and parameter error add other terms.

A backtest using closing mids but executing no spread is not a hedge test. A historical strategy that knows final dividends or uses revised data looks into the future. A realistic simulation needs executable prices, timing, funding, and position limits.

## Prices become bands

With costs, exact replication may be impossible at one number. A seller needs enough premium to super-replicate or tolerate risk after costs; a buyer has a lower bound from sub-replication. The interval between them is economically real, not mere market inefficiency.

> **Reader decision:** compare daily, weekly, and delta-band hedging on the same paths. Which policy minimizes cost plus a stated penalty for residual variance? There is no answer until the penalty is named.

> **Memory seal:** every pass of the hedging loom pays a toll. Move too slowly and cloth tears; move too often and tolls consume it.

[Next: Liquidity and Bid–Ask Spreads](../046-liquidity-and-bid-ask-spreads/README.md)

# 045 — Transaction Costs and Discrete Hedging

**Vocabulary key:** Find **045** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **045** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Moving your hedge costs little coins each time. Move too little and miss the ball; move too much and spend all the coins.

### In finance language

Transaction costs and discrete hedging replace continuous, free trading with real spreads, fees, timing gaps, and market impact.

Real hedges are adjusted at intervals and pay spreads, fees, and market impact. The cheaper-looking model hedge may be impossible or costly to carry out. **For an AI helper:** include realistic rebalancing frequency and trading costs, then show a range rather than a frictionless promise.

## The impossible instruction

The tree, simulation, and grid can all refine their time steps without paying a broker. A real hedge cannot. Black–Scholes replication says trade continuously. If each trade crosses a spread, infinitely frequent rebalancing creates unbounded cumulative cost. The ideal repair and the market friction collide.

Trade rarely and gamma produces tracking error between hedge times. Trade often and costs rise. A practical policy chooses a clock or delta band: rebalance when exposure exits a tolerance rather than after every tiny move. The optimum depends on spread, gamma, volatility, risk limits, and inventory.

## Separate sources of hedge P&L

Maintain a ledger containing option mark change, delta stock P&L, financing, dividends, transaction cost, and residual. In a smooth model, much residual can be understood through gamma times realized squared movement versus theta implied by priced volatility. Jumps, surface changes, and parameter error add other terms.

A backtest using closing mids but executing no spread is not a hedge test. A historical strategy that knows final dividends or uses revised data looks into the future. A realistic simulation needs executable prices, timing, funding, and position limits.

## Prices become bands

With costs, exact replication may be impossible at one number. A seller needs enough premium to super-replicate or tolerate risk after costs; a buyer has a lower bound from sub-replication. The interval between them is economically real, not mere market inefficiency.

> **Reader decision:** compare daily, weekly, and delta-band hedging on the same paths. Which policy minimizes cost plus a stated penalty for residual variance? There is no answer until the penalty is named.

> **Memory seal:** every pass of the hedging loom pays a toll. Move too slowly and cloth tears; move too often and tolls consume it.

[Next: Liquidity and Bid–Ask Spreads](../046-liquidity-and-bid-ask-spreads/README.md)

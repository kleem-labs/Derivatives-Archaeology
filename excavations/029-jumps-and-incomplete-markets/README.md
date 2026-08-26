# 029 — Jumps and Incomplete Markets

## The earnings-night gap

Local and stochastic volatility enriched continuous paths, but neither forces the market to visit every intermediate price. A trader delta-hedges a short call at the close. Overnight the company announces a failed trial and stock opens 35% lower. No sequence of continuous stock trades occurred between the prices. The hedge was calibrated to an infinitesimal movement that the market skipped.

Add a jump process and the option change contains the full finite difference `V(S+Delta S)-V(S)`, not merely local delta and gamma. Stock and bond cannot generally hedge both continuous diffusion and independent jump-size risk. One more source of risk needs another traded instrument to span it.

## Price becomes a range plus a choice

In a complete binomial model, replication forced one price. In an incomplete jump or stochastic-volatility model, many pricing measures can make discounted traded assets martingales while assigning different values to the unspanned claim. No-arbitrage eliminates inconsistent prices but does not choose one survivor.

An institution may choose by calibrating liquid options, minimizing hedge variance, applying utility, selecting an entropy criterion, or quoting enough premium for capital and inventory. Each adds an economic or statistical responsibility beyond pure no-arbitrage.

## Designing in an incomplete world

An original derivative on rainfall, electricity demand, or private-company revenue is rarely perfectly replicable. Start with sub- and super-replication bounds, transparent scenarios, and sensitivity to weights. A single precise number hides the very incompleteness that matters.

> **Retrieval challenge:** identify the number of independent future states and independent traded payoff vectors in a small table. When the latter fail to span the former, show why multiple state-price systems remain.

> **Memory seal:** a jump breaks the replication bridge. The remaining gap must be priced by an additional, explicitly named choice.

## Mara brings the physical warehouse back

The broken hedge bridge has taught us to ask which risks are actually traded. Mara now returns with a physical detail our first stock-forward example deliberately suppressed: carrying an asset can require storage, insurance, financing, and scarce inventory. Those are not probability refinements. They are cash flows and services on the replication route itself.

Before choosing another elaborate option model, the book returns to the simpler carry ledger and makes every ownership difference visible. Only then can futures hedges, curves, and contracts on physical goods be valued without mistaking a missing warehouse cost for mysterious risk premium.

[Next: Cost of Carry](../030-cost-of-carry/README.md)

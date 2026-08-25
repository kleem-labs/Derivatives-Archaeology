# 029 — Jumps and Incomplete Markets

Brownian paths move continuously; real prices can gap. A delta hedge cannot trade inside an instantaneous jump. Adding jumps improves tail behavior but introduces risk that stock and cash may not span.

When not every claim can be replicated, the market is incomplete. Multiple equivalent pricing measures can exist and no-arbitrage supplies bounds rather than one price. Pricing then needs an additional labeled choice: preferences, calibrated risk premia, utility, minimum-variance hedging, or other traded options.

Perfect replication is a property of a model and traded set, not every market.

## The earnings-night gap

A trader delta-hedges a short call at the close. Overnight the company announces a failed trial and stock opens 35% lower. No sequence of continuous stock trades occurred between the prices. The hedge was calibrated to an infinitesimal movement that the market skipped.

Add a jump process and the option change contains the full finite difference `V(S+Delta S)-V(S)`, not merely local delta and gamma. Stock and bond cannot generally hedge both continuous diffusion and independent jump-size risk. One more source of risk needs another traded instrument to span it.

## Price becomes a range plus a choice

In a complete binomial model, replication forced one price. In an incomplete jump or stochastic-volatility model, many pricing measures can make discounted traded assets martingales while assigning different values to the unspanned claim. No-arbitrage eliminates inconsistent prices but does not choose one survivor.

An institution may choose by calibrating liquid options, minimizing hedge variance, applying utility, selecting an entropy criterion, or quoting enough premium for capital and inventory. Each adds an economic or statistical responsibility beyond pure no-arbitrage.

## Designing in an incomplete world

An original derivative on rainfall, electricity demand, or private-company revenue is rarely perfectly replicable. Start with sub- and super-replication bounds, transparent scenarios, and sensitivity to weights. A single precise number hides the very incompleteness that matters.

> **Retrieval challenge:** identify the number of independent future states and independent traded payoff vectors in a small table. When the latter fail to span the former, show why multiple state-price systems remain.

> **Memory seal:** a jump breaks the replication bridge. The remaining gap must be priced by an additional, explicitly named choice.

## The road returns to futures

With the option engine exposed, we return to forward markets and recover the richer carry terms that stocks, commodities, rates, and margin require.

[Next: Cost of Carry](../030-cost-of-carry/README.md)

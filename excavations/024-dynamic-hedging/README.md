# 024 — Dynamic Hedging: Replication Through Rebalancing

**Vocabulary key:** Find **024** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **024** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Keep moving the umbrella as the rain changes direction. Waiting too long gets you wet; moving every second wears you out.

### In finance language

Dynamic hedging repeatedly changes the underlying position to track an option. Real rebalancing has timing error and trading cost.

Dynamic hedging means adjusting a stock-and-cash copy as the market moves. The elegant idea has real costs, timing gaps, and execution risk. **For an AI helper:** report rebalance assumptions, trading costs, and what happens between rebalances.

## Follow one hedge through a move

The Greeks have described separate local movements. A hedge must live through all of them in sequence. At spot $100, short one call and buy .542 shares. If spot rises, the short call's negative delta grows in magnitude; the hedge must buy more shares at the higher price. If spot falls, it sells shares lower. A short-gamma hedger is forced to chase movement. Premium and time decay compensate for accepting that behavior—if the priced volatility and costs are sufficient.

In the ideal diffusion, rebalancing continuously makes accumulated stock-and-cash flows reproduce the option. In a daily hedge, the option may jump from one delta to another before trading occurs. The residual is not a bookkeeping mistake; it is discrete hedging error.

## A replication experiment is also a model test

Record each rebalance: time, spot, option mark, delta, stock trade, financing cash, fee, and final payoff. Reconcile terminal hedging P&L. Then repeat across simulated or historical paths. The distribution reveals sensitivity to hedge frequency, volatility assumption, jumps, and costs.

A model calibrated perfectly to today's option price can still hedge poorly because many models share one price while implying different dynamics. This is why calibration and validation are distinct.

## Whose funding and whose execution?

Black–Scholes uses one clean rate and costless stock trades. Real dealers face bid–ask spreads, borrow fees, inventory limits, collateral, and asymmetric funding. A customer who cannot dynamically hedge may value an option through utility or insurance benefit rather than dealer replication cost.

> **Memory seal:** the loom continually replaces stock threads as the underlying cloth moves. If it pauses during a jump, a tear remains.

## Retrieval challenge

Explain why “delta-neutral” is a timestamped statement rather than a permanent property. Name three events that change delta without an executed trade.

[Next: Realized Volatility](../025-realized-volatility/README.md)

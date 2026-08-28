# 033 — Basis and Convergence

**Vocabulary key:** Find **033** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

A farmer’s local wheat and the big exchange’s wheat are cousins, not identical twins. Their price gap can shrink or grow.

### In finance language

Basis is the spot-minus-futures difference. A futures hedge removes some price risk but leaves basis risk when the two prices move differently.

Basis is the gap between a cash-market price and a futures price. It often narrows near delivery, but a hedge can still disappoint if the two prices do not move together as expected. **For an AI helper:** name both markets, locations, grades, and dates before calling something a hedge.

## A hedge retains one moving seam

The commodity chapter showed why local physical ownership differs from a standardized future. Measure that difference. A farmer's local cash wheat price is $5.80 while the exchange futures is $6.00, so spot-minus-futures basis is `-$0.20`. She shorts futures. At sale, local cash is $5.10 and futures $5.20, so basis is `-$0.10`.

The cash price fell $0.70, while the short futures gained $0.80. Her effective outcome improved by the $0.10 strengthening of basis. If basis had weakened instead, the hedge would underperform. The futures removed much outright price risk but left the relationship between local wheat and deliverable exchange wheat.

## Why convergence is a delivery argument

At contract expiry, if futures remained materially above deliverable spot after costs, a trader could buy eligible physical supply, short futures, and deliver. If futures were too low, reverse mechanisms may apply subject to contract rules and shorting feasibility. Delivery forces convergence to the contract's eligible economic object, not necessarily a headline spot index.

Quality differentials, location, timing, and cheapest-to-deliver choices matter. Financial contracts may cash settle to an index, transferring attention to index construction and manipulation resistance.

## Basis is a state variable

Choosing a hedge maturity requires a view on basis behavior and rollover. A cross-hedge—jet fuel with crude futures, for example—adds product basis. Historical correlation can break during shortages when local constraints dominate global futures.

> **Retrieval challenge:** write effective sale price as final cash price plus futures gain. Rearrange it into initial futures price plus final basis and use the identity to explain basis risk.

> **Memory seal:** spot and futures travel on separate rails. Delivery draws them together, but the distance between rails still moves before the station.

Even a well-chosen basis hedge can produce large interim futures losses. Because the exchange settles those losses daily, the next threat is not terminal price but the cash required to remain on the rails until convergence.

[Next: Margin and Leverage](../034-margin-and-leverage/README.md)

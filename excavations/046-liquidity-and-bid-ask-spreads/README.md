# 046 — Liquidity and Bid–Ask Spreads

**Vocabulary key:** Find **046** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

One child says “I will buy for 8”; another says “I will sell for 8.20.” The number halfway between is not a deal either child agreed to.

### In finance language

The bid is an executable buyer price; the ask is an executable seller price. Their difference is the bid–ask spread and an entry/exit cost.

The price on a screen is not always the price at which someone can trade. The bid is what a buyer offers; the ask is what a seller requests; the gap is a real cost of entering and leaving. **For an AI helper:** use time-stamped bid and ask, not a lonely last trade, and say when liquidity is too thin for a strong conclusion.

## The first strategy cost

A buyer normally begins at the ask and may later exit at the bid. A seller normally receives the bid and may later buy back at the ask. So a strategy that appears to have a small theoretical advantage can lose it immediately to the spread. Compare the model with the relevant executable side, not the midpoint: buy-side analysis begins near ask; sell-side analysis begins near bid.

## A screen is not a transaction

Transaction costs broke the single replication price. The first visible source is the two-sided quote. An option displays 7.80 bid and 8.20 ask. Marking it at $8 creates a useful accounting midpoint, but a new buyer pays 8.20 and an immediate seller receives 7.80. A strategy apparently worth 20 cents at mids may lose 20 cents when crossed.

Put–call parity must therefore be tested with executable legs: use asks for purchases, bids for sales, include stock spread, borrow, fees, and legging risk. No-arbitrage equality becomes a no-trade band.

## Size changes the price

The best quote may cover one contract. A 1,000-contract order walks through the book or reveals information and moves dealers' implied volatility. Market impact can be temporary or persistent. Complex orders may obtain package pricing better than leg-by-leg execution because the dealer can hedge net risk.

Open interest and volume are clues, not guarantees of liquidity. During stress, spreads widen, correlations shift, and hedges become expensive exactly when needed. An exit assumption based on ordinary days can dominate a trade's apparent edge.

## Marking with uncertainty

Liquid instruments can use executable market data. Illiquid claims require model marks with valuation adjustments for uncertainty, funding, credit, and closeout. Independent price verification should distinguish observed inputs from extrapolated surface regions.

> **Market-reading challenge:** an option's model value is $10, bid is $8, ask $11. Is it cheap or expensive? Neither conclusion follows: the model value lies inside the executable spread. State what additional trade or quote would create evidence.

> **Memory seal:** BUY and SELL pass through different gates. The midline painted between them is not a doorway.

One position already has two executable values. A portfolio contains many such gates plus nonlinear interactions. Adding its local Greeks is useful, but the combined book must also be walked through coherent market scenarios.

[Next: Portfolio Greeks and Scenarios](../047-portfolio-greeks-and-scenarios/README.md)

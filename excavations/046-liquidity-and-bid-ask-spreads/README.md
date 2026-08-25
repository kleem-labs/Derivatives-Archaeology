# 046 — Liquidity and Bid–Ask Spreads

A displayed mid-price is not necessarily executable. Buying crosses the ask; selling crosses the bid; size can move the market. Consequently parity and arbitrage become inequalities after spreads, fees, funding, and inventory costs.

Liquidity varies by strike, maturity, time, and market state. Marking a large portfolio at mids can overstate realizable value. Model calibration to stale or crossed quotes can manufacture a false volatility surface.

Executable bounds and quote quality belong inside valuation evidence, not as an afterthought.

## A screen is not a transaction

An option displays 7.80 bid and 8.20 ask. Marking it at $8 creates a useful accounting midpoint, but a new buyer pays 8.20 and an immediate seller receives 7.80. A strategy apparently worth 20 cents at mids may lose 20 cents when crossed.

Put–call parity must therefore be tested with executable legs: use asks for purchases, bids for sales, include stock spread, borrow, fees, and legging risk. No-arbitrage equality becomes a no-trade band.

## Size changes the price

The best quote may cover one contract. A 1,000-contract order walks through the book or reveals information and moves dealers' implied volatility. Market impact can be temporary or persistent. Complex orders may obtain package pricing better than leg-by-leg execution because the dealer can hedge net risk.

Open interest and volume are clues, not guarantees of liquidity. During stress, spreads widen, correlations shift, and hedges become expensive exactly when needed. An exit assumption based on ordinary days can dominate a trade's apparent edge.

## Marking with uncertainty

Liquid instruments can use executable market data. Illiquid claims require model marks with valuation adjustments for uncertainty, funding, credit, and closeout. Independent price verification should distinguish observed inputs from extrapolated surface regions.

> **Market-reading challenge:** an option's model value is $10, bid is $8, ask $11. Is it cheap or expensive? Neither conclusion follows: the model value lies inside the executable spread. State what additional trade or quote would create evidence.

> **Memory seal:** BUY and SELL pass through different gates. The midline painted between them is not a doorway.

[Next: Portfolio Greeks and Scenarios](../047-portfolio-greeks-and-scenarios/README.md)

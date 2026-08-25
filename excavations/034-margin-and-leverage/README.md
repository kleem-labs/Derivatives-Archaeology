# 034 — Margin and Leverage

Futures margin is performance collateral, not the purchase price. A contract with $100,000 notional may require only a fraction as initial margin, so a small underlying move can be large relative to posted cash.

Variation margin realizes gains and losses through time. Maintenance thresholds can force liquidation even if the eventual hedge would work. Measuring return against margin while ignoring notional disguises leverage; measuring risk only at maturity disguises liquidity.

Leverage does not create exposure from nothing. It concentrates an existing contractual exposure onto less posted capital.

## The small deposit and the large crate

One futures contract controls $100,000 of underlying. The exchange requires $8,000 initial margin. A 3% adverse move creates a $3,000 loss—37.5% of posted margin—though only 3% of notional. Calling the return “37.5%” without naming the denominator makes leverage look like investment performance rather than concentrated exposure.

Maintenance margin sets a lower collateral threshold. If losses push the account below it, the trader must restore funds, often quickly. Variation margin makes model P&L into cash P&L each settlement cycle.

## Economic hedge, liquidity mismatch

An airline hedges future fuel purchases by going long energy futures. Falling fuel prices create margin losses but reduce the later physical purchase cost. The economics offset over the horizon, yet the futures loss arrives now and the cheaper fuel is purchased later. Treasury liquidity must bridge the dates.

This explains why notional, stress loss, and margin liquidity all belong in risk reports. Initial margin is designed to cover plausible short-horizon loss at a confidence standard; it is not a maximum loss. Exchanges can raise margin precisely when volatility and funding stress rise.

## Options do not remove leverage

A long option has premium-limited contractual loss, but its notional exposure and Greeks can still change rapidly. A short option may require margin far beyond received premium and can face nonlinear increases after adverse moves.

> **Decision:** before opening a futures position, calculate loss for a historically severe move, collateral after that move, potential margin increase, and available liquid cash. If survival depends on immediate convergence, the position is too large.

> **Memory seal:** a thin margin cable lifts a huge notional crate. The cable is collateral, not the crate's size and not proof it cannot fall.

[Next: Hedging with Futures](../035-hedging-with-futures/README.md)

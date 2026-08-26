# 034 — Margin and Leverage

## The small deposit and the large crate

Basis explains why a hedge may not offset perfectly at maturity. Margin asks whether the trader can even remain until maturity. One futures contract controls $100,000 of underlying. The exchange requires $8,000 initial margin. A 3% adverse move creates a $3,000 loss—37.5% of posted margin—though only 3% of notional. Calling the return “37.5%” without naming the denominator makes leverage look like investment performance rather than concentrated exposure.

Maintenance margin sets a lower collateral threshold. If losses push the account below it, the trader must restore funds, often quickly. Variation margin makes model P&L into cash P&L each settlement cycle.

## Economic hedge, liquidity mismatch

An airline hedges future fuel purchases by going long energy futures. Falling fuel prices create margin losses but reduce the later physical purchase cost. The economics offset over the horizon, yet the futures loss arrives now and the cheaper fuel is purchased later. Treasury liquidity must bridge the dates.

This explains why notional, stress loss, and margin liquidity all belong in risk reports. Initial margin is designed to cover plausible short-horizon loss at a confidence standard; it is not a maximum loss. Exchanges can raise margin precisely when volatility and funding stress rise.

## The margin account changes the hedge size

The planned hedge cannot be sized only from final price exposure. Ten contracts may offset the harvest at maturity but demand more variation margin than the farm can fund during a temporary rally. Reducing contract count leaves more price risk and less liquidity risk; increasing it does the reverse.

This turns the next question from “How much notional matches?” into “How many contracts hedge the exposure we actually have, on dates we can survive?” Quantity, contract size, and hedge ratio must enter the same calculation.

> **Decision:** before opening a futures position, calculate loss for a historically severe move, collateral after that move, potential margin increase, and available liquid cash. If survival depends on immediate convergence, the position is too large.

> **Memory seal:** a thin margin cable lifts a huge notional crate. The cable is collateral, not the crate's size and not proof it cannot fall.

[Next: Hedging with Futures](../035-hedging-with-futures/README.md)

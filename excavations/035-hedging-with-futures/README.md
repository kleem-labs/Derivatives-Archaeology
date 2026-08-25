# 035 — Hedging with Futures

A producer expecting to sell `Q_A` units can short futures to offset falling prices. A naive one-for-one hedge fails when contract size, price sensitivity, maturity, or underlying quality differs.

With futures contract size `Q_F`, a simple contract count is `N=h Q_A/Q_F`, where `h` is a hedge ratio. Its sign follows the exposure: short futures for a future sale, long futures for a future purchase.

A hedge reduces a named risk; it does not guarantee profit. Basis, volume, timing, margin, and counterparty rules remain.

## Count exposure before contracts

A coffee producer expects 375,000 pounds at harvest. Each futures contract covers 37,500 pounds. If cash coffee and futures moved identically, shorting ten contracts would match quantity. But harvest may differ, the local grade may price differently, and hedge maturity may precede sale.

The general count `N=hQ_A/Q_F` separates physical quantity from price hedge ratio. Sign matters: a future seller is hurt by falling prices and shorts futures; a future buyer hurt by rising prices goes long.

## Hedge the risk you have, not the story you tell

Inventory already owned, forecast production, firm purchase commitments, and anticipated sales are different exposures. Over-hedging forecast production can create a speculative short if crops fail. Rolling futures adds spread risk between contract months. Currency may add another layer if physical and futures quotes settle differently.

Construct a joint cash-flow table under high and low spot, strong and weak basis, and high and low actual volume. The table often reveals that one “hedged price” is a range.

## Effectiveness is an empirical question

A futures hedge works when changes in the chosen contract offset changes in the exposure over the relevant horizon. Correlation, volatility ratio, contract size, and basis determine the result. Accounting hedge effectiveness and economic effectiveness may use different tests.

> **Reader challenge:** a producer expects 500 units, contracts cover 100, and the selected hedge ratio is .8. Calculate contract count, then explain whether to round up or down using over-hedge risk.

> **Memory seal:** sacks from the real granary are measured against standardized exchange crates. Quantity alone does not guarantee the contents move together.

[Next: Minimum-Variance Hedge Ratio](../036-minimum-variance-hedge-ratio/README.md)

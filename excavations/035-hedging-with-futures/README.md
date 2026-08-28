# 035 — Hedging with Futures

**Vocabulary key:** Find **035** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **035** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

If a baker fears flour becoming costly, she chooses a futures position that smiles when flour gets costly. The hedge is meant to soften the business hurt.

### In finance language

A futures hedge offsets a stated price exposure. Long or short direction follows whether the business is hurt by rising or falling prices.

A hedge is not a bet that must make money by itself. It is an attempt to make a business’s unwanted price movement hurt less. **For an AI helper:** state the real exposure first, then compare the future’s gain or loss with that exposure under several scenarios.

## Count exposure before contracts

The margin account forced us to size a hedge the firm can survive. Begin with the exposure itself. A coffee producer expects 375,000 pounds at harvest. Each futures contract covers 37,500 pounds. If cash coffee and futures moved identically, shorting ten contracts would match quantity. But harvest may differ, the local grade may price differently, and hedge maturity may precede sale.

The general count `N=hQ_A/Q_F` separates physical quantity from price hedge ratio. Sign matters: a future seller is hurt by falling prices and shorts futures; a future buyer hurt by rising prices goes long.

## Hedge the risk you have, not the story you tell

Inventory already owned, forecast production, firm purchase commitments, and anticipated sales are different exposures. Over-hedging forecast production can create a speculative short if crops fail. Rolling futures adds spread risk between contract months. Currency may add another layer if physical and futures quotes settle differently.

Construct a joint cash-flow table under high and low spot, strong and weak basis, and high and low actual volume. The table often reveals that one “hedged price” is a range.

## Effectiveness is an empirical question

A futures hedge works when changes in the chosen contract offset changes in the exposure over the relevant horizon. Correlation, volatility ratio, contract size, and basis determine the result. Accounting hedge effectiveness and economic effectiveness may use different tests.

> **Reader challenge:** a producer expects 500 units, contracts cover 100, and the selected hedge ratio is .8. Calculate contract count, then explain whether to round up or down using over-hedge risk.

> **Memory seal:** sacks from the real granary are measured against standardized exchange crates. Quantity alone does not guarantee the contents move together.

The unresolved symbol is `h`. Setting it to one assumes equal price movements. Historical cash and futures changes can instead choose the ratio that makes the remaining hedge noise smallest.

[Next: Minimum-Variance Hedge Ratio](../036-minimum-variance-hedge-ratio/README.md)

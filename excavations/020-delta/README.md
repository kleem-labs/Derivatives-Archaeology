# 020 — Delta: The First Local Hedge

**Vocabulary key:** Find **020** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **020** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

If the stock takes one tiny step right, delta tells how much the option roughly follows. It is like a tiny steering arrow, not a permanent map.

### In finance language

Delta is the local first sensitivity of option value to underlying price, and in a model it is the number of underlying units in a local hedge.

Delta answers: for a very small immediate stock move, about how much does the option move? It is a local steering direction, not a permanent hedge ratio or a probability. **For an AI helper:** include units and multiplier, say “small move,” and flag that delta changes as price and time change.

## A hedge is a local promise

The option formula is finally on the table, and its derivation told us to hold `V_S` shares. Take the book's $100 spot, $105 strike, 20% volatility call. Its Black–Scholes `V_S`, called delta, is about .542. Holding one call and shorting .542 shares makes the combined position nearly insensitive to a very small immediate spot move.

If spot rises $1, first-order option change is about +$0.542 while the short stock loses $0.542. But a $20 move is not twenty copies of the first dollar. As spot rises, the call becomes more stock-like and delta increases. Treating .542 as permanent leaves a large error.

Delta also depends on time and implied volatility. A far out-of-the-money call can move from low delta to high delta rapidly near an event. A put's negative delta reflects that its value usually rises when spot falls.

For a Black–Scholes call with continuous yield `q`, `Delta=e^(-qT)N(d_1)`; for the corresponding put it is `e^(-qT)(N(d_1)-1)`.

## The strategy use of delta

Delta does not announce “buy” or “sell.” It tells a reader how much immediate direction a position carries. A long call usually has positive delta: it benefits from a small rise. A long put usually has negative delta: it benefits from a small fall. A covered call has stock’s positive delta minus the call’s positive delta, so it gives away part of the stock’s upside. A protective put has stock plus a negative-put delta, so it softens a small fall.

For a 100-share contract, `portfolio delta = number of contracts × 100 × option delta`, then add stock shares. This unit check prevents a common error: reporting a per-share Greek as if it were the position’s dollar exposure. Delta is one line of the strategy scorecard, never the entire scorecard.

## Several meanings must not be collapsed

Delta is simultaneously a mathematical derivative, a local P&L approximation, and—inside a complete model—the stock quantity in a replicating hedge. These meanings agree because the model connects them. “Probability of finishing in the money” is a different quantity: in Black–Scholes it is related to `N(d_2)`, while call delta uses `N(d_1)` without dividends.

For a portfolio, deltas add after multipliers, currencies, and units are aligned. One option contract may represent 100 shares; forgetting the multiplier creates a hedge one hundred times too small.

> **Decision:** would you hedge a one-year call once using today's delta or rebalance? If you rebalance, what tells you how quickly delta changes? That unanswered question is gamma.

> **Memory seal:** the steering wheel cancels only the road's current slope. As the road bends, the wheel must turn again.

[Next: Gamma](../021-gamma/README.md)

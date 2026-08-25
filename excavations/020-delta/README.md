# 020 — Delta: The First Local Hedge

If a call changes from $8.00 to about $8.60 when the stock rises $1, its local sensitivity is near `0.60`. Delta is `Delta = partial V / partial S`: approximate option-value change per one-unit spot change, everything else fixed. It also gives the instantaneous shares in the Black–Scholes hedge.

Delta is a slope, not a constant hedge for all moves. The payoff bends, so delta changes with spot, time, and volatility. Nor is call delta literally the real-world probability of exercise.

For a Black–Scholes call with yield `q`, `Delta=e^(-qT)N(d_1)`; for the put it is `e^(-qT)(N(d_1)-1)`.

## A hedge is a local promise

Take the book's $100 spot, $105 strike, 20% volatility call. Its Black–Scholes delta is about .542. Holding one call and shorting .542 shares makes the combined position nearly insensitive to a very small immediate spot move.

If spot rises $1, first-order option change is about +$0.542 while the short stock loses $0.542. But a $20 move is not twenty copies of the first dollar. As spot rises, the call becomes more stock-like and delta increases. Treating .542 as permanent leaves a large error.

Delta also depends on time and implied volatility. A far out-of-the-money call can move from low delta to high delta rapidly near an event. A put's negative delta reflects that its value usually rises when spot falls.

## Several meanings must not be collapsed

Delta is simultaneously a mathematical derivative, a local P&L approximation, and—inside a complete model—the stock quantity in a replicating hedge. These meanings agree because the model connects them. “Probability of finishing in the money” is a different quantity: in Black–Scholes it is related to `N(d_2)`, while call delta uses `N(d_1)` without dividends.

For a portfolio, deltas add after multipliers, currencies, and units are aligned. One option contract may represent 100 shares; forgetting the multiplier creates a hedge one hundred times too small.

> **Decision:** would you hedge a one-year call once using today's delta or rebalance? If you rebalance, what tells you how quickly delta changes? That unanswered question is gamma.

> **Memory seal:** the steering wheel cancels only the road's current slope. As the road bends, the wheel must turn again.

[Next: Gamma](../021-gamma/README.md)

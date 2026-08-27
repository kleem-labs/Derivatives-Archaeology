# Volume IV — We Learn to Feel the Hedge

Black–Scholes gives a price. A trader then asks a more immediate question: if the world moves one inch, what happens to me?

## 020 — The first lean: delta

Delta is how much an option price leans when the share price moves a little. If a call's delta is about one-half, a one-dollar rise in the share makes the call rise by about fifty cents, for a very small move.

It also says how many shares belong in the copying hedge. But it is only true for the present moment. As the share moves, the option changes shape.

[Open the workshop](../excavations/020-delta/README.md)

## 021 — The bend: gamma

Gamma says how quickly delta itself changes. A call near its strike is curved most sharply. That is why a hedge that looked right this morning can feel wrong after a large move.

Long options usually like big movement because their curve helps in either direction. But that benefit is paid for by time passing and by the cost of changing the hedge.

[Open the workshop](../excavations/021-gamma/README.md)

## 022 — The clock: theta

Hold the share still. Hold the market's idea of movement still. Let one day pass. An option usually loses a little value because there is one less day for something useful to happen.

That loss is theta. It is not a punishment from nowhere. It is the price of carrying a curved right through time.

[Open the workshop](../excavations/022-theta/README.md)

## 023 — Change the weather, not the share

Vega asks what happens if the market expects more movement. Rho asks what happens if interest rates change.

These are not predictions. They are “what if” questions. Turn one dial, hold the others still, and see how the model price changes. This is how we learn what a position is sensitive to before the market moves.

[Open the workshop](../excavations/023-vega-and-rho/README.md)

## 024 — A hedge is a moving thing

To copy an option, the share hedge must change as the share changes. A trader who waits too long leaves a gap. A trader who changes it constantly pays too much to trade.

The perfect hedge belongs to an ideal world with no spreads and no jumps. In the real world, the gap between the model hedge and the lived hedge tells us where the risk truly is.

[Open the workshop](../excavations/024-dynamic-hedging/README.md)

## 025 — The movement that actually happened

After a month, we can look back at every price move and ask: how much did the share really wander?

Realized volatility is a summary of that finished path. It depends on how often we look. Look too rarely and miss movement. Look too often and hear market noise as though it were real motion.

[Open the workshop](../excavations/025-realized-volatility/README.md)

## 026 — The movement hidden in today's price

Implied volatility runs the option formula backward. We know the market price. We ask, “What movement number would make the formula give this price?”

That number is a common language for option prices. It is not a weather forecast. It is a way of saying what the market is charging for a certain shape of uncertainty.

[Open the workshop](../excavations/026-implied-volatility/README.md)

## 027 — The smile tells us the simple story is too simple

If one movement number worked everywhere, every option with the same expiry would show the same implied volatility. They do not.

Options far below the current share price often carry a higher number because people care deeply about bad falls. The smile is the market saying, “One neat bell curve does not fit all our fears.”

[Open the workshop](../excavations/027-volatility-smile/README.md)

## 028 — Give movement a richer life

One repair says movement depends on where the share is and what time it is. Another says movement has its own changing life, like weather following a storm.

Both can match today's smile. They can still disagree tomorrow. That is why fitting today's prices is only the beginning of judging a model.

[Open the workshop](../excavations/028-local-and-stochastic-volatility/README.md)

## 029 — The jump breaks the copy

Sometimes a share closes at $100 and opens at $65. No hedge trade fits inside that empty space.

When the market can jump, stock and cash may no longer be enough to copy every promise. Then math can give a range and a way to think, but not one forced price. Someone must add a judgment about the risk that cannot be copied.

[Open the workshop](../excavations/029-jumps-and-incomplete-markets/README.md)

## What to carry with you

Greeks are not magic letters. They are names for the ways a living hedge can change. The next volume returns to physical things—wheat, oil, money, delivery dates—and asks what it really costs to carry them through time.

[Next volume: We Carry the Physical World](VOLUME_V_WE_CARRY_THE_WORLD.md)


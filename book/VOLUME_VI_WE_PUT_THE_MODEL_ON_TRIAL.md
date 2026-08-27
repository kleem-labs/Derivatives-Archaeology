# Volume VI — We Put the Model on Trial

The final volume asks the question that keeps the whole book honest: what did the formula quietly assume, and what happens when the market refuses to cooperate?

## 040 — Sometimes the holder may act early

A European option waits until the end. An American option lets its holder choose an earlier day.

At each allowed day, compare two things: use the option now, or keep the option alive. Keep the better one. That is all early exercise means.

[Open the workshop](../excavations/040-american-exercise/README.md)

## 041 — The moving line between wait and act

For an American put, there is often a share price below which using the option now makes more sense than waiting. That price changes as time, rates, dividends, and expected movement change.

The early-exercise boundary is simply a map of that moving line. It turns many small choices into one picture.

[Open the workshop](../excavations/041-early-exercise-boundaries/README.md)

## 042 — Some promises remember the journey

Two shares can finish at $110. One may have fallen below $95 on the way; the other may not. A barrier option can care about that difference.

Now the final price is not enough. The contract must remember the path. That is why the legal details—what time prices are checked and what happens when data are missing—become part of the mathematics.

[Open the workshop](../excavations/042-barriers-and-path-dependence/README.md)

## 043 — Make many small worlds

When a promise depends on a whole path, draw many possible paths with a computer. Apply the promise to each path. Bring every payoff back to today. Average them.

That is Monte Carlo. More paths make the average steadier, but never prove the world generator was right. It measures the wobble of the calculation, not the truth of the model.

[Open the workshop](../excavations/043-monte-carlo/README.md)

## 044 — Or cover the world with a grid

If a problem has only a few moving pieces, we can make a grid of prices and times. Start at the known payoff at the end. Then work backward across nearby squares.

This is finite differences. It is another way to solve the same kind of promise. The important habit is to make the grid finer and check whether the answer settles down.

[Open the workshop](../excavations/044-finite-differences/README.md)

## 045 — Trading has a toll

The perfect hedge says trade all the time. Each real trade pays a spread or fee.

Trade too little and the hedge drifts away. Trade too much and costs eat the benefit. There is no perfect clock. A good hedge policy says what kind of error it is willing to live with and what it is willing to pay to reduce it.

[Open the workshop](../excavations/045-transaction-costs-and-discrete-hedging/README.md)

## 046 — The number on the screen may not be yours

An option quoted at 8 bid and 8.20 ask is not really “worth 8.10” to a new buyer or seller. The buyer pays 8.20. The seller receives 8.

The middle is useful for a rough mark. It is not a door you can walk through. Any claim that an option is cheap must begin with the price that can actually be traded.

[Open the workshop](../excavations/046-liquidity-and-bid-ask-spreads/README.md)

## 047 — A portfolio can hide danger from itself

One option can be understood with a few sensitivities. A book of options can have sensitivities that cancel on paper while leaving a large danger in a big move.

So we tell stories about whole markets: share down, volatility up, spreads wider, rates changed. Then we reprice everything together. A scenario is not a prediction. It is a flashlight.

[Open the workshop](../excavations/047-portfolio-greeks-and-scenarios/README.md)

## 048 — A line is not the whole cliff

Value at risk draws a line: “on most days, loss should stay below this amount.” It says little about how far the loss can fall after crossing the line.

Expected shortfall looks below the line and asks for the average loss in the bad tail. Both are useful summaries. Neither is a promise that the worst event is known.

[Open the workshop](../excavations/048-value-at-risk-and-expected-shortfall/README.md)

## 049 — The final habit

When someone gives you an option price, ask simple questions.

What exactly does the contract pay? On what dates? What can copy it? What cannot be copied? Which model inputs matter? What price can I truly trade? What happens in a jump, a wide spread, or a margin call?

The book's goal is not to make you say “this option is definitely cheap.” It is to let you say something far more honest and useful: “Under these clear assumptions, this is my value range, this is what could break it, and this is the risk I would carry.”

[Open the workshop](../excavations/049-model-validation-and-limits/README.md)

## The last picture

Math should now feel less like a wall of symbols and more like a set of small actions: compare two routes, move cash through time, copy a promise, watch what the copy cannot catch, and name the missing risk.

That is how to read an option. That is also how to invent a new derivative without letting the formula float away from the real world.

[Return to the Derivative Design Studio](../DERIVATIVE_DESIGN_STUDIO.md)


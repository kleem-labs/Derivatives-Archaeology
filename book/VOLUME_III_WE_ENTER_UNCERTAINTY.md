# Volume III — We Enter Uncertainty

The tree has become too large to draw. We need new words, but each word will come from something we already know: a list of futures, a weight on each future, a path made of tiny moves, and a fair way to look at the whole path.

## 012 — Give each future a name

Picture three Marchs: dry, ordinary, and rainy. Each one has a wheat price. A random variable is simply the label that tells us the price in each possible world.

For a call, we use the same worlds but attach a different label: how much the call pays there. The worlds do not change. Only the question changes.

Keep this separation clear: the payoff tells us what the contract gives; the weights tell us how much attention a model gives each future.

[Open the workshop](../excavations/012-random-variables/README.md)

## 013 — Average is not enough

Two possible futures can have the same average price and feel completely different. One may sit near $100 all year. Another may swing between $50 and $150.

An option cares about that difference because it keeps good outcomes and can ignore bad exercise outcomes. A call on a steady $100 may pay nothing. A call on a price that swings around $100 can pay a lot in its high futures.

An average tells us where the middle is. Variance tells us how spread out the futures are. Neither tells the whole story, but both help us see why movement matters.

[Open the workshop](../excavations/013-expectation-and-variance/README.md)

## 014 — Prices multiply

A ten-percent rise followed by a ten-percent fall does not bring a price home. `1.10 × 0.90` is `0.99`.

That is why we often look at percentage changes and their logarithms. Logarithms turn a chain of multiplying changes into a sum. They also let us use a bell-shaped model for the changes while keeping the price itself above zero.

This model is useful because it is simple. It is not a promise that markets never jump, never panic, or never change their mood.

[Open the workshop](../excavations/014-normal-and-lognormal/README.md)

## 015 — Tiny surprises add up

Imagine walking while gusts of wind push you a little left or right. Over one second, the push is tiny. Over a year, many pushes make a visible wandering path.

The strange part is the size of each tiny push. It must shrink like the square root of time, not like time itself. If it shrinks too fast, all uncertainty disappears. If it shrinks too slowly, uncertainty explodes.

Brownian motion is the name for this carefully balanced wandering. It gives us a model of a price that moves all the time yet has no clean instant-by-instant direction.

[Open the workshop](../excavations/015-brownian-motion/README.md)

## 016 — Tiny squares refuse to disappear

For an ordinary smooth walk, tiny steps become so small that their squares vanish. Brownian steps are different. Each is small, but there are so many that the squares add up to something real.

That is why an option's bend matters. A straight-line estimate sees only the first small move. An option bends, so the square of the move leaves a mark too.

This sounds technical, but the picture is simple: many tiny footprints can cover a floor even though no single footprint looks important.

[Open the workshop](../excavations/016-quadratic-variation/README.md)

## 017 — The chain rule needs one extra piece

Ordinary calculus says: if stock changes, option value changes because of its slope. Brownian motion adds one more fact: the option's bend also matters over time.

Itô's lemma is the repaired chain rule. It says, “Keep the slope, keep the clock, and keep the bend times the tiny squared movement.”

Now comes the old copying idea again. Hold the right number of shares against the option. Their random wiggles cancel for one instant. What remains behaves like money in the bank.

[Open the workshop](../excavations/017-itos-lemma/README.md)

## 018 — Two ways to count the same futures

People may believe a share is likely to rise fast. A pricing model may still use different weights when it asks what a copied option should cost.

Think of the possible price paths as the same film shown to two audiences. One audience votes according to what it thinks will really happen. The other uses weights that make copied trades fit together fairly.

The second audience does not claim to predict the world. It helps price promises that can be copied from traded things.

[Open the workshop](../excavations/018-change-of-measure/README.md)

## 019 — Choose the ruler, then price the right

If you measure a share in dollars, its number can rise because the share rises or because the dollar changes. So first choose a ruler. A bank account is a useful ruler because we know how it grows.

Once prices are measured against that growing bank account, the fair-weighted future does not lean up or down. Now the old copying argument can finally become a formula.

Hold the option and sell just enough shares to cancel the next tiny surprise. The part left over must grow like the bank account. That idea leads to Black–Scholes.

For a plain call, the formula is not a new story. It is the tree-copy story after the tree has become too fine to see.

[Open the workshop](../excavations/019-martingales-and-numeraires/README.md)

## What to carry with you

The hard words in this volume all do one job: make a huge tree manageable without forgetting why the tree worked. The next volume returns to the thing a trader can feel today: how a price changes when the share, the clock, or the market's sense of movement changes.

[Next volume: We Learn to Feel the Hedge](VOLUME_IV_WE_FEEL_THE_HEDGE.md)

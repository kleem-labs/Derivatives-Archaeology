# 008 — One Period, Two Futures

**Vocabulary key:** Find **008** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **008** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Pretend tomorrow has only two weather pictures: up or down. Build a little pile of stock and cash that behaves like the option in both pictures.

### In finance language

A one-period binomial model uses two states to find a replicating portfolio: stock units plus borrowing or lending that exactly match the option.

In a tiny world with only an up outcome and a down outcome, stock and cash can copy an option. Once the copy is built, its cost gives the option’s value in that toy world. **For an AI helper:** show both outcomes and the copy; never output only the final number.

Shrink the market to one year and two possible stock prices. A $100 share will end at either $120 or $90. A call struck at $105 pays $15 in the up state and $0 in the down state.

One analyst assigns a 70% chance to the rise. Another assigns 30%. If price depends directly on either forecast, they disagree before valuation begins. But the market gives us two building blocks—stock and risk-free borrowing—and there are exactly two states. Try to build the call instead.

## Choose shares by matching the gap

First compare only what changes between the two final states. A fixed debt pays the same amount in both, so it cannot explain a difference. Shares can:

| Final state | One share is worth | Call pays | Difference from down state |
|---|---:|---:|---:|
| Down | $90 | $0 | $0 |
| Up | $120 | $15 | $30 for stock; $15 for call |

We need enough shares so their $30 up-versus-down change becomes the call’s $15 up-versus-down change. Half of $30 is $15, so hold **0.5 share**. In finance language, this share count is the one-step hedge ratio, often written with the symbol `Delta`:

`Delta = call’s state difference ÷ stock’s state difference = $15 ÷ $30 = 0.5`.

Half a share is worth $60 up and $45 down. We need option payoffs of $15 and $0, so subtract $45 in both terminal states by borrowing its present value. At 5%, the present debt is `-45e^-0.05=-$42.8053`.

The replicating portfolio costs

`0.5($100)-$42.8053=$7.1947`.

Check both states. Up: half the share is $60, repay $45, retain $15. Down: half is $45, repay $45, retain zero. The cash flows match before we speak of probability.

## Why any other price creates a trade

If the call sells for $9, sell it and buy the $7.1947 replication. The initial difference remains, and the portfolio meets the call obligation in either state. If it sells for $6, buy the call and short the replication.

This conclusion depends on frictionless divisibility, common borrowing and lending rates, tradable stock, no default, and the declared two-state world. Add a third independent terminal state and stock plus bond generally cannot match all three points of the kink.

## The hedge is not half a forecast

Delta of 0.5 is the number of shares required to span the payoff difference. It is not the probability of rising. It arose by dividing one state-to-state change by another.

> **Memory seal — the forked stair:** half a share stretches across both landings while one fixed debt lowers the whole bridge into alignment with the call.

## Excavation questions

1. Reprice a $100-strike call if terminal stock is $130 or $80.
2. Verify the hedge in both states before calculating its cost.
3. Add a third terminal stock price of $105. Can the same stock-and-bond portfolio match all three call payoffs?

## The probability that is not a belief

The replication price can be rewritten as a discounted weighted average. The resulting weights behave like probabilities, but they encode tradable growth rather than anyone's forecast.

[Next: Risk-Neutral Probability](../009-risk-neutral-probability/README.md) · [Lab](../../labs/derivatives_lab.py)

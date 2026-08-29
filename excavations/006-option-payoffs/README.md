# 006 — Options Create Asymmetry

**Vocabulary key:** Find **006** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **006** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

A child pays for a ticket that lets her buy a toy for $10 later if the toy becomes expensive. She may use the ticket or tear it up.

### In finance language

A call is the right to buy at a strike; a put is the right to sell. The holder owns the choice and the writer owes the other side if assigned.

An option buyer may take a good deal and refuse a bad one; the seller accepts the other side of that choice. That difference is why buyer and seller risks must never be blended together. **For an AI helper:** state the position side, premium, multiplier, and worst plainly described outcome before using the word “option.”

Leena owns shares in a young company at $100. She wants protection against a collapse but refuses to sell because a product launch may double the price. A forward hedge would remove both loss and gain. She wants a floor without a ceiling.

A one-year put struck at $90 offers exactly that right: sell at $90 if market price ends below it. At expiry it pays `max(90-S_T,0)`. The put seller accepts the corresponding obligation and receives premium today.

## Price, payoff, and profit are three pictures

At terminal stock prices $50, $90, and $140, put payoff is $40, $0, and $0. But if Leena paid $6 initially, undiscounted option profit is payoff minus $6. Her total protected-stock outcome includes the share too. Confusing these pictures creates bad decisions: limited option loss does not mean the combined portfolio cannot lose, and a positive payoff does not guarantee profit.

For a call buyer the expiry payoff is `max(S_T-K,0)`. The maximum again records the right to refuse. For the writer, payoff is its negative. A naked short call can lose without a contractual upper bound as `S_T` rises.

## The four seats at the option table

The option name is incomplete until we know whether the reader bought or sold it. Let `P` be premium per share. These are **profits at expiry**, before fees and multiplied by the contract multiplier:

| Position | Profit at expiry | What it really means |
|---|---|---|
| Buy call | `max(S_T-K,0)-P` | Pay for upside with a deadline. |
| Sell call | `P-max(S_T-K,0)` | Receive premium; promise to sell at `K` if assigned. |
| Buy put | `max(K-S_T,0)-P` | Pay for a floor or a decline. |
| Sell put | `P-max(K-S_T,0)` | Receive premium; promise to buy at `K` if assigned. |

This is the first strategy lesson: buying has a known upfront loss but needs a sufficiently useful move before the clock ends. Selling receives a known upfront amount but accepts the opposite payoff, assignment mechanics, and possibly much larger loss. A spread adds a second option so that one leg limits the other. Use the [Strategy Field Guide](../../STRATEGY_FIELD_GUIDE.md) after this chapter to compare the whole positions.

## Why a wider set of outcomes can make a right more valuable

Keep the agreed purchase price at $100. Compare two tiny stories about where the stock finishes in one year:

| Story | Possible final stock price | What the purchase-right does | Cash from using the right |
|---|---:|---|---:|
| Still story | $100 for certain | Buying for $100 saves nothing | $0 |
| Moving story, low half | $80 | Walk away; buying in the market is cheaper | $0 |
| Moving story, high half | $120 | Use the right; buy for $100 instead of $120 | $20 |

In the moving story, pretend the $80 and $120 endings are equally likely. The right pays $0 in one half and $20 in the other half. Its simple average payoff is therefore `(0 + 20) ÷ 2 = $10`. In the still story, the stock also finishes at an average of $100, but the right pays $0 because there is no high-price outcome to use it against.

The important shape is now visible in the table: when the final price is low, the right does not produce a negative number—the holder walks away. When the final price is high, the holder keeps the saving. Later, mathematics gives this one-sided, upward-bending shape the name **convex**. For now, say it plainly: **the right keeps the good surprise and refuses the bad one.**

This table does **not** price the right today. It uses made-up, equal chances only to show why a wider possible range can matter. To turn future cash into today’s value, we still need to learn two things: move known money through time, and choose pricing weights that agree with stock-and-cash copies.

## Design begins with shape

Leena could buy one put, finance it by selling a lower-strike put, or cap upside by selling a call. Each combination changes the state-by-state promise. Product names are shorthand; the cash-flow function is the contract's skeleton.

> **Memory seal — the one-way door returns:** the holder pays for the ability to enter only the favorable corridor. The writer must stand behind the locked unfavorable side.

## Excavation questions

1. Draw payoff and profit for a call struck at $110 with $4 premium.
2. Compare a protective put with selling the stock. Which risks and opportunities remain?
3. Explain, using the $80/$120 table, why the purchase-right keeps the good surprise and refuses the bad one.

## The symmetry hidden in two kinks

A call and a put appear opposite. Combine each with stock or cash and their kinks align into identical terminal wealth. That identity will constrain their prices without choosing a volatility model.

[Next: Put–Call Parity](../007-put-call-parity/README.md)

# 006 — Options Create Asymmetry

Leena owns shares in a young company at $100. She wants protection against a collapse but refuses to sell because a product launch may double the price. A forward hedge would remove both loss and gain. She wants a floor without a ceiling.

A one-year put struck at $90 offers exactly that right: sell at $90 if market price ends below it. At expiry it pays `max(90-S_T,0)`. The put seller accepts the corresponding obligation and receives premium today.

## Price, payoff, and profit are three pictures

At terminal stock prices $50, $90, and $140, put payoff is $40, $0, and $0. But if Leena paid $6 initially, undiscounted option profit is payoff minus $6. Her total protected-stock outcome includes the share too. Confusing these pictures creates bad decisions: limited option loss does not mean the combined portfolio cannot lose, and a positive payoff does not guarantee profit.

For a call buyer the expiry payoff is `max(S_T-K,0)`. The maximum again records the right to refuse. For the writer, payoff is its negative. A naked short call can lose without a contractual upper bound as `S_T` rises.

## Why volatility can add value without changing the mean

Consider a stock ending at $80 or $120 with equal probability, mean $100. A $100 call pays $0 or $20, expected payoff $10. A stock certain to end at its same mean of $100 gives the call zero. The average stock price did not change; the spread did.

The call's convex kink rejects the lower branch at zero while keeping the upper branch. This is why `payoff(E[S_T])` differs from `E[payoff(S_T)]`, and why optionality responds to volatility.

But expected payoff is not yet arbitrage-free price. We still require discounting and appropriate state weights. The example reveals the direction of convexity, not a complete valuation.

## Design begins with shape

Leena could buy one put, finance it by selling a lower-strike put, or cap upside by selling a call. Each combination changes the state-by-state promise. Product names are shorthand; the cash-flow function is the contract's skeleton.

> **Memory seal — the one-way door returns:** the holder pays for the ability to enter only the favorable corridor. The writer must stand behind the locked unfavorable side.

## Excavation questions

1. Draw payoff and profit for a call struck at $110 with $4 premium.
2. Compare a protective put with selling the stock. Which risks and opportunities remain?
3. Explain, using the $80/$120 example, why a convex payoff values dispersion.

## The symmetry hidden in two kinks

A call and a put appear opposite. Combine each with stock or cash and their kinks align into identical terminal wealth. That identity will constrain their prices without choosing a volatility model.

[Next: Put–Call Parity](../007-put-call-parity/README.md)


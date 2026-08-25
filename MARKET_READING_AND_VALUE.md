# Reading a Market and Asking Whether an Option Is Worth It

There is no context-free “true value.” There is a no-arbitrage region, model values conditional on inputs, executable bid and ask prices, and value to a particular holder with particular forecasts and constraints.

## The decision stack

### 1. Verify the instrument

Record underlying, multiplier, strike, exercise style, expiration time zone, settlement, dividends, corporate actions, liquidity, open interest, bid, ask, and fees. A correct formula applied to the wrong contract is wrong.

### 2. Establish hard bounds and identities

Check intrinsic value, discounted strike, put–call parity or its dividend/European assumptions, monotonicity across strikes, convexity, and calendar consistency. Compare executable combinations, not mid-prices. Violations smaller than costs are not trades.

### 3. Translate quotes into a surface

Compute implied volatility from both bid and ask using consistent spot, curve, dividends, and time. Compare strike and maturity structure. A single implied-volatility number without its surface neighborhood is missing context.

### 4. Form a conditional view

Write distributions or scenarios for future spot, realized volatility, jumps, dividends, rates, and liquidity. Separate:

- **directional edge:** your distribution of `S_T` differs;
- **volatility edge:** your expected path variability differs;
- **surface edge:** relative strike or maturity pricing differs;
- **risk-transfer value:** the option protects something valuable even without positive standalone expected return.

### 5. Revalue under more than one model

Use Black–Scholes as a common coordinate, then a tree, scenario distribution, jump/stochastic-volatility model, or historical simulation when the thesis depends on features Black–Scholes excludes. Report a range, not false precision.

### 6. Build the P&L bridge

For a proposed trade, show premium, spread, commissions, financing, theta horizon, delta/gamma/vega exposure, hedge cost, exercise/assignment, tax uncertainty where relevant, and plausible exit price. Compare expected or scenario P&L with maximum loss and liquidity needs.

### 7. Demand a margin of safety

Define `decision value = conservative model/scenario value - executable cost - uncertainty reserve`. Buy only if this is positive enough for estimation error and opportunity cost. For a sale, reverse the cash flows and include unbounded or jump loss and margin survival.

## A call example

An ask of $8 is not cheap merely because your model says $9. If plausible dividend and volatility inputs produce $7–$10, the spread is $0.40, and exit/hedge cost is $0.50, there is no demonstrated edge. A thesis becomes testable when it says: “The ask implies 20% volatility; my event-weighted distribution implies a conservative $10.20 value, costs are $0.60, maximum loss is the premium, and the thesis fails if event probability falls below X.”

## A put example

A protective put can be worth buying even with negative expected standalone P&L if it prevents forced liquidation or protects a concentrated asset. That is insurance value. Conversely, selling the put because its implied volatility exceeds a historical average ignores crash risk, volatility risk premium, margin, and the seller's ability to survive assignment.

## Final answer format

Never conclude merely “buy” or “sell.” Conclude:

> Under assumptions A, B, and C, the executable price is below/inside/above my valuation range of X–Y after costs. The position risks ___, benefits from ___, can lose ___, requires ___ liquidity, and the thesis is invalidated by ___.

This framework supports judgment; it does not guarantee profit or replace regulated financial, legal, or tax advice.


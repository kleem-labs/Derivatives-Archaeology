# 022 — Theta: The Cost of the Clock

Theta is option sensitivity to calendar time, quoted as value change when time passes while spot and inputs stay fixed. A plain long option often has negative theta: fewer future paths remain as expiry approaches. But time decay is not guaranteed realized P&L because spot and implied volatility also move.

The Black–Scholes PDE ties theta to convexity and financing: `Theta + 0.5 sigma^2 S^2 Gamma + rS Delta - rV = 0` for a non-dividend-paying stock. Theta is therefore not an independent tax; it is one side of the local replication balance.

## Freeze the world, move the calendar

Suppose Friday's option closes at $8 and Monday opens with identical spot, volatility surface, and rates. Less time remains, so its model price changes. Theta is that partial effect, not the total weekend P&L the trader will actually observe if inputs move.

Near expiry, an at-the-money option can lose time value rapidly because uncertainty must resolve soon. A deeply in- or out-of-the-money option may behave differently. Quoting “theta per day” also requires a calendar convention: divide an annual derivative by 365, trading days, or a model-specific clock?

## The gamma–theta exchange

In the Black–Scholes PDE, a delta-hedged option's curvature exposure and time passage balance funding. Long gamma is not a free repeated opportunity to buy low and sell high. The option owner pays theta; realized rebalancing gains exceed that cost only if the path supplies enough movement relative to what was priced, abstracting from costs.

This creates the practical distinction between implied and realized volatility. The option premium reflects an implied movement scale. The delta-hedged path experiences realized movement. Their relationship, plus execution, shapes hedging P&L.

## Exceptions prevent slogans

Long options “usually have negative theta” is a useful orientation, not a theorem for every option under every rates and dividend regime. Deep in-the-money European puts with unusual carry can display positive theta. Structured portfolios can be long time decay while carrying dangerous short convexity.

> **Decision:** a trader earns positive theta each day. What must you inspect before calling the position safe? At minimum gamma, jump loss, volatility exposure, liquidity, and maximum loss.

> **Memory seal:** the clock melts possibility, but the curved rail may earn from the motion occurring while it melts.

[Next: Vega and Rho](../023-vega-and-rho/README.md)

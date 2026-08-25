# 038 — Forward Rates and Swaps

Discount factors `P(0,T)` imply a forward rate between `T_1` and `T_2`. Under simple compounding with year fraction `tau`, `1+f tau=P(0,T_1)/P(0,T_2)`.

A plain interest-rate swap exchanges fixed coupons for floating coupons. At inception, the par fixed rate makes their present values equal: fixed rate equals the discounted value of the floating leg divided by the fixed-leg annuity.

Forward rates are break-even rates encoded by today's curve, not necessarily unbiased forecasts. Credit, collateral, and index conventions determine which curve prices which cash flow.

## Lock a future borrowing interval

One dollar invested to `T_2` must match investing to `T_1` and then at the forward rate from `T_1` to `T_2`. Under simple compounding for the interval, `1+f tau=P(0,T_1)/P(0,T_2)`. The ratio appears because the two investment routes must deliver equal terminal wealth.

This forward rate is a break-even rate encoded by current discount factors. Calling it the market's forecast ignores term premia, convexity, and measure. It is the rate that prevents an intertemporal arbitrage in the modeled curve.

## A swap is a strip of forward exchanges

In a fixed-for-floating swap, one side pays fixed coupons on notional while the other pays a floating index. Immediately after reset, a standard floating leg has a simple value relationship; across the schedule its present value can be assembled from discount and projection factors.

The par fixed rate is chosen so initial net value is zero:

`K_swap = PV(floating cash flows) / sum_i alpha_i P(0,T_i)`.

The denominator is the swap annuity—the present value of one unit of fixed coupon at each payment date. Every accrual fraction and payment calendar matters.

## Risk lives along the curve

A single duration number hides which maturities move value. Bumping each curve pillar produces key-rate or bucketed sensitivities. Discount and projection curves can move differently; basis risk survives a superficially matched fixed-rate hedge.

> **Memory seal:** fixed and floating streams enter opposite sides of an aqueduct. The annuity wheel adjusts the fixed flow until present volumes balance.

[Next: Options on Futures](../039-options-on-futures/README.md)

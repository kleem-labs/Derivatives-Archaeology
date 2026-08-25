# 037 — Bootstrapping Discount Curves

One interest rate cannot discount every maturity. Market deposits, futures, swaps, and bonds reveal different combinations of discount factors. Bootstrapping solves them sequentially from shortest known cash flows outward.

If a par instrument has known earlier coupon present values, its price equation isolates the next unknown discount factor. Interpolation fills unquoted dates, but the interpolation space—zero rates, log discount factors, or forwards—changes smoothness and risk.

Modern collateralized pricing may require multiple curves: one for discounting and others for projecting index cash flows. “The yield curve” is no longer always one object.

## Build the curve one cash flow at a time

A six-month zero-coupon instrument reveals the six-month discount factor directly. A one-year par bond pays an earlier coupon at six months and coupon plus principal at one year. Once the first discount factor is known, subtract the present value of the first coupon from price; the remaining equation isolates the one-year factor.

That sequential recovery is bootstrapping. Each new maturity stands on previously solved rungs. With a par bond price of 100 and annual coupon split across dates, write `100=cP(0,.5)+(100+c)P(0,1)` and solve the final unknown.

## Quotes are not discount factors

Deposits, futures, swaps, and bonds use different day counts, calendars, compounding, and credit or collateral conventions. They must be converted into consistent cash-flow equations before bootstrapping. Futures convexity adjustments may matter when turning futures rates into forwards.

Unquoted dates require interpolation. Linear zero rates, log-linear discount factors, and smooth forward curves produce different risk distributions between market pillars even when they fit quoted instruments exactly. Interpolation is a modeling choice exposed by nonstandard cash flows.

## The multi-curve repair

After the financial crisis, collateralized discounting and unsecured term-index projection could no longer be treated as one curve without distortion. A pricing system may use an overnight-index curve for discounting and separate projection curves for floating indices, with basis swaps linking them.

> **Validation challenge:** reprice every input instrument after constructing the curve. A curve that cannot recover its own pillars has failed before pricing a derivative.

> **Memory seal:** the scaffold grows from the shortest rung outward; no distant plank floats without support from earlier cash flows.

[Next: Forward Rates and Swaps](../038-forward-rates-and-swaps/README.md)

# 037 — Bootstrapping Discount Curves

One interest rate cannot discount every maturity. Market deposits, futures, swaps, and bonds reveal different combinations of discount factors. Bootstrapping solves them sequentially from shortest known cash flows outward.

If a par instrument has known earlier coupon present values, its price equation isolates the next unknown discount factor. Interpolation fills unquoted dates, but the interpolation space—zero rates, log discount factors, or forwards—changes smoothness and risk.

Modern collateralized pricing may require multiple curves: one for discounting and others for projecting index cash flows. “The yield curve” is no longer always one object.

Next: [Forward Rates and Swaps](../038-forward-rates-and-swaps/README.md).


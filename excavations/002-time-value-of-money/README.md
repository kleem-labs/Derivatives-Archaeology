# 002 — Time Has a Price

Choose between $100 now and $100 in a year. If cash can earn 5%, the first choice can become about $105.13 under continuous compounding. Comparing the two nominal amounts as equals ignores what the earlier dollar can do.

Let a continuously compounded annual rate be `r` and time in years be `T`. One present dollar becomes `e^(rT)` dollars, so a certain future cash flow must be divided by that growth:

`PV(X_T) = X_T e^(-rT)`.

At 5%, $105 due in one year is worth `105e^(-0.05) = $99.88` today. Division removes the growth accumulated between the dates.

This rule assumes a rate, compounding convention, currency, maturity, and credit quality. Treating one “risk-free rate” as universal is already a model. Yet discounting gives us a way to transport cash through time, which is enough to expose a free lunch.

Next: [No Free Lunch](../003-no-arbitrage/README.md). Try `present_value` in [the lab](../../labs/derivatives_lab.py).


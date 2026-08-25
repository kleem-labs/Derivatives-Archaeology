# 008 — One Period, Two Futures

A $100 stock will be either $120 or $90 in one year. A call struck at $105 will then pay $15 or $0. Can stock and cash reproduce those two outcomes?

Choose `Delta` shares. The difference between the two stock outcomes is `$30Delta`; the option outcome difference is $15. Therefore `Delta=15/30=0.5`. In the down state, half a share is worth $45 but the call is worth zero, so the hedge must owe $45 at maturity. At 5%, that debt is worth `-45e^-0.05 = -$42.81` now.

The replicating cost is therefore:

`C_0 = 0.5(100) - 42.81 = $7.19`.

No subjective up probability was used. We matched both allowed states. The crucial equation is:

`Delta = (C_u-C_d)/(S_u-S_d)`.

With only two traded building blocks, this works because there are only two states. More states can make the market incomplete.

Next: [Risk-Neutral Probability](../009-risk-neutral-probability/README.md). Reproduce the cash flows in [the lab](../../labs/derivatives_lab.py).


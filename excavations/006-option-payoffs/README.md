# 006 — Options Create Asymmetry

A call with strike $100 lets its owner buy at $100 but never forces the purchase. At expiry it pays `max(S_T-100,0)`. The seller has the opposite payoff and receives a premium today for accepting that asymmetry.

Intrinsic value alone is not today's option price. A call can be out of the money now yet valuable because time remains for the underlying to cross the strike. Nor is unlimited upside free: the buyer's loss is limited to the premium, while the writer's loss can grow with the underlying.

Draw the payoff at $60, $100, and $150. The kink at the strike is the central geometric fact. A linear combination of stock and cash is straight; it cannot match the kink for every possible terminal price with one static choice.

Yet a call and a put can be combined so their kinks cancel. That recovered symmetry is put–call parity.

Next: [Put–Call Parity](../007-put-call-parity/README.md).


# 009 — Risk-Neutral Probability

The binomial replicating price can be rewritten as a discounted weighted average. If the stock multiplies by `u` or `d`, define

`p* = (e^(rT)-d)/(u-d)`.

For `u=1.2`, `d=0.9`, and `r=5%`, `p*` is about `0.504`. Then

`C_0 = e^(-rT)[p*C_u + (1-p*)C_d]`.

This `p*` is not our estimate that the stock has a 50.4% chance of rising. It is the unique weight that makes the stock's weighted growth equal the risk-free growth, thereby encoding the same replication price in probability notation.

The condition `d < e^(rT) < u` keeps `p*` between zero and one. If it fails, the stock dominates or is dominated by cash in every state, revealing arbitrage inside the model.

Probability has entered as a pricing coordinate system. Repeating the construction through time produces a tree.

Next: [Many Small Steps](../010-multi-period-binomial/README.md).


# 023 — Vega and Rho: Sensitivity to Model Inputs

Vega is `partial V/partial sigma`. Long vanilla calls and puts usually have positive vega because greater spread benefits a convex payoff while downside is truncated. Rho is `partial V/partial r`; higher rates reduce the present value of a fixed strike, generally helping calls and hurting puts.

Neither Greek predicts its input. They are local derivatives of a pricing map. Units matter: desks often quote vega and rho per one percentage-point change. Large moves and interactions require full repricing rather than a first-order estimate.

Next: [Dynamic Hedging](../024-dynamic-hedging/README.md).


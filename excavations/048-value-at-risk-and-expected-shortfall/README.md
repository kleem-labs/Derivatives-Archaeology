# 048 — Value at Risk and Expected Shortfall

At confidence `alpha`, value at risk is a loss quantile: a threshold exceeded with probability `1-alpha` under the chosen distribution and horizon. It says little about how severe losses are beyond the threshold.

Expected shortfall averages losses in that tail and is more sensitive to its shape. Both depend on data, model, horizon, liquidity, and mapping of current positions into future P&L. Historical, parametric, and simulation methods can disagree sharply.

These are model outputs, not maximum-loss guarantees. Stress tests remain essential where data contain no example of the relevant failure.

Next: [Model Validation](../049-model-validation-and-limits/README.md).


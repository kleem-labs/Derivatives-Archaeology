# 048 — Value at Risk and Expected Shortfall

At confidence `alpha`, value at risk is a loss quantile: a threshold exceeded with probability `1-alpha` under the chosen distribution and horizon. It says little about how severe losses are beyond the threshold.

Expected shortfall averages losses in that tail and is more sensitive to its shape. Both depend on data, model, horizon, liquidity, and mapping of current positions into future P&L. Historical, parametric, and simulation methods can disagree sharply.

These are model outputs, not maximum-loss guarantees. Stress tests remain essential where data contain no example of the relevant failure.

## The quantile and the cellar below it

Suppose one-day 99% VaR is $10 million. Under the model, only one day in one hundred exceeds that loss threshold. The statement does not say the worst loss is $10 million. Loss beyond the line could be $10.1 million or $100 million.

Expected shortfall asks for the average loss conditional on entering the worst tail. It therefore distinguishes distributions sharing the same 99th percentile but having different disasters beyond it. Its estimate is also data-hungry because tail observations are rare.

## Every number inherits a machine

Historical simulation assumes selected past changes represent the future and applies them to today's portfolio. Parametric VaR compresses returns into a distribution and dependence model. Monte Carlo simulates chosen factors and reprices. Horizon scaling by square-root time fails when returns are autocorrelated, volatility changes, positions are nonlinear, or markets cannot be liquidated smoothly.

Backtesting counts exceptions, but passing can coexist with poor tail shape or clustered breaches. A model calibrated in calm data can fail together with liquidity assumptions during stress.

## Risk appetite is not a percentile

Limits should combine VaR or expected shortfall with stress loss, jump scenarios, concentration, gross notionals, Greeks, collateral, and liquidity. An option premium-limited position may still be unacceptable relative to available capital; a hedge may be valuable because it protects survival even if it reduces expected return.

> **Memory seal:** VaR marks the trapdoor. Expected shortfall descends into the cellar and measures what waits after the threshold.

## Retrieval challenge

Construct two loss distributions with the same 95% VaR and radically different expected shortfall. Explain which a short-option seller should fear more.

[Next: Model Validation](../049-model-validation-and-limits/README.md)

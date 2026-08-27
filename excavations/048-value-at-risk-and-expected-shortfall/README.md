# 048 — Value at Risk and Expected Shortfall

## First, in everyday words

Value at Risk asks for a loss threshold under a stated model and confidence level; Expected Shortfall asks how bad the losses beyond that threshold average out. Both can miss the disasters their data or model fails to imagine. **For an AI helper:** show the horizon, confidence level, method, historical window, and stress cases beside every risk number.

## The quantile and the cellar below it

The scenario theater produced many portfolio losses. Management asks for one threshold summarizing them. Suppose one-day 99% value at risk is $10 million. Under the model, only one day in one hundred exceeds that loss threshold. The statement does not say the worst loss is $10 million. Loss beyond the line could be $10.1 million or $100 million.

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

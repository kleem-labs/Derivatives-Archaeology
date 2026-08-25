# 028 — Local and Stochastic Volatility

Local volatility replaces constant `sigma` with `sigma(S,t)` and can calibrate a regular arbitrage-free vanilla surface. Future volatility is then a deterministic function of spot and time.

Stochastic-volatility models give volatility its own random dynamics, often correlated with spot. They create richer forward smiles and volatility-of-volatility risk but add parameters and unhedgeable state variables.

Matching today's vanilla surface does not determine tomorrow's joint dynamics. Two calibrated models can disagree on barriers or hedging P&L. Calibration is not validation.

Next: [Jumps and Incomplete Markets](../029-jumps-and-incomplete-markets/README.md).


# 028 — Local and Stochastic Volatility

## First, in everyday words

When one fixed volatility is too simple, we can let volatility change with price, time, or its own random motion. More realism also means more assumptions to test. **For an AI helper:** report which volatility model was chosen, what market quotes it fits, and where it may fail.

## Two repairs to the same failure

The smile proved that one constant `sigma` cannot reproduce all vanilla quotes. Local volatility asks: what deterministic volatility at each spot and time makes the diffusion reproduce today's surface? Dupire's result links an arbitrage-free continuum of option prices to `sigma_local(S,t)`. The model can fit European vanillas by construction, yet its future smile evolution may disagree with markets.

Stochastic volatility introduces a second state, such as variance `v_t`, with its own randomness and correlation with spot. Negative correlation can steepen equity skew: falling spot arrives with rising variance. Volatility-of-volatility controls how widely future variance can move.

The second state creates an unspanned shock if only stock and cash trade. Additional option prices help calibrate its risk premium. A good fit may still be non-unique because parameters trade off against one another.

## Choose using the claim, not prestige

For a vanilla book marked to today's surface, a stable arbitrage-free interpolation may matter more than elaborate dynamics. For barriers or forward-start options, future surface behavior is central. For long-dated products, mean reversion may dominate. Model complexity should be purchased only for risks the payoff actually observes.

Validate beyond calibration: examine parameter stability, out-of-sample prices, hedge performance, forward smiles, and stress behavior. The question is not “does it fit?” but “what had to be assumed to fit, and what else does that assumption imply?”

> **Memory seal:** one weather map assigns wind from location; another releases a storm with its own wandering life. Both match today's flags, but tomorrow's motion differs.

Both repairs still move along continuous paths. The market can instead reopen at a price it never crossed. That single observation will show why adding more continuous state variables cannot complete every hedge.

[Next: Jumps and Incomplete Markets](../029-jumps-and-incomplete-markets/README.md)

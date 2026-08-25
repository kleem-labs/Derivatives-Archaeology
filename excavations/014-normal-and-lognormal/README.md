# 014 — Normal and Lognormal Models

Adding many small independent shocks suggests a normal distribution. Applied directly to prices, however, a normal model permits negative stock prices. Modeling log returns instead repairs positivity: if `ln(S_T/S_0)` is normal, then `S_T` is lognormal.

Under geometric Brownian motion, `S_T = S_0 exp((mu-sigma^2/2)T + sigma sqrt(T) Z)`, with `Z` standard normal. The `-sigma^2/2` term corrects the fact that exponentiation bends averages upward. Without it, `E[S_T]` would not equal `S_0e^(mu T)`.

Lognormality gives tractable option formulas and positive prices, but observed returns exhibit jumps, heavy tails, volatility clustering, and changing skew. It is a useful layer, not a law of nature.

Next: [Brownian Motion](../015-brownian-motion/README.md).


# 017 — Itô's Lemma: Calculus for Rough Paths

Let `dS=mu Sdt+sigma SdW` and let an option be `V(S,t)`. Ordinary chain rule would keep only `V_tdt+V_SdS`. Quadratic variation forces the second derivative to survive:

`dV = (V_t + mu S V_S + 0.5 sigma^2 S^2 V_SS)dt + sigma S V_S dW`.

The half comes from Taylor's second-order coefficient; `sigma^2S^2dt` comes from `(dS)^2`. Choosing `Delta=V_S` shares cancels the shared `dW` shock between option and stock. No-arbitrage then makes the locally riskless remainder earn `r`, producing the Black–Scholes PDE.

Itô calculus is exact inside the continuous diffusion model. Jumps require an additional term.

Next: [Change of Measure](../018-change-of-measure/README.md).


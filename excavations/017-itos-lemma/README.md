# 017 — Itô's Lemma: Calculus for Rough Paths

Let `dS=mu Sdt+sigma SdW` and let an option be `V(S,t)`. Ordinary chain rule would keep only `V_tdt+V_SdS`. Quadratic variation forces the second derivative to survive:

`dV = (V_t + mu S V_S + 0.5 sigma^2 S^2 V_SS)dt + sigma S V_S dW`.

The half comes from Taylor's second-order coefficient; `sigma^2S^2dt` comes from `(dS)^2`. Choosing `Delta=V_S` shares cancels the shared `dW` shock between option and stock. No-arbitrage then makes the locally riskless remainder earn `r`, producing the Black–Scholes PDE.

Itô calculus is exact inside the continuous diffusion model. Jumps require an additional term.

## Rebuild the missing term

Let `V(S,t)` be a call value and expand around a tiny interval. Time contributes `V_tdt`; the stock move contributes `V_SdS`; curvature contributes `.5V_SS(dS)²`. Substitute `dS=mu Sdt+sigma SdW` and keep terms of order `dt`.

The squared stock move is dominated by `sigma²S²(dW)²=sigma²S²dt`. Cross-products with `dt` vanish at the limiting order. Therefore

`dV=(V_t+mu SV_S+.5sigma²S²V_SS)dt+sigma SV_SdW`.

Every term has units of value change. `V_S` is value per unit of stock; multiplied by stock change it becomes value. `V_SS` is value per stock squared; multiplied by `S²` and variance per time, then by time, it becomes value.

## The hedge that removes one shock

Form a portfolio long the option and short `V_S` shares. The `dW` terms cancel because both positions respond to the same Brownian shock. The remaining instantaneous change is locally riskless under the model and must earn the funding rate, or a nearby arbitrage appears.

Rearranging produces the Black–Scholes PDE. The derivation shows why delta and gamma are not merely reporting statistics: they are the quantities that divide random movement from deterministic replication balance.

## Where the lemma stops

If the stock jumps, Taylor's local second-order correction does not capture the full discontinuous change. A jump version of Itô's formula includes the actual finite jump response. If volatility itself is random, `V` may depend on another state and acquire more derivative terms.

> **Retrieval challenge:** cover the displayed formula and reconstruct it from Taylor expansion plus the quadratic-variation multiplication table.

> **Memory seal:** an ordinary chain rule enters the rough corridor; a curved gamma link must be added before it can leave intact.

[Next: Change of Measure](../018-change-of-measure/README.md)

# 017 — Itô's Lemma: Calculus for Rough Paths

**Vocabulary key:** Find **017** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

When a bumpy path passes through a curved slide, the curve adds an extra effect. Ordinary slide rules miss that extra bump.

### In finance language

Itô’s lemma is the chain rule for diffusion processes. It includes a second-derivative term caused by quadratic variation.

Itô’s lemma is the chain rule after random, rough motion adds one extra term. The extra term is not decoration; it changes option values. **For an AI helper:** show the input process, formula version, and units, then route the arithmetic through a tested calculation engine.

## Rebuild the missing term

Quadratic variation told us not to discard the squared stock move. Let `V(S,t)` be a call value and expand around a tiny interval. Time contributes `V_tdt`; the stock move contributes `V_SdS`; curvature contributes `.5V_SS(dS)²`. Substitute `dS=mu Sdt+sigma SdW` and keep terms of order `dt`.

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

The hedge has removed the random shock and eliminated `mu` from the pricing equation. We need a probability language that expresses the same price without pretending that the stock's actual expected return has become `r`.

[Next: Change of Measure](../018-change-of-measure/README.md)

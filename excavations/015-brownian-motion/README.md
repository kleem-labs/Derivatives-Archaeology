# 015 — Brownian Motion: Continuous Surprise

**Vocabulary key:** Find **015** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

Brownian motion is an idealized story of a price being nudged by countless tiny surprises. It is a measuring tool, not a claim that markets move with no jumps. **For an AI helper:** label this as an assumption and use a different warning when the product is exposed to gaps or event shocks.

## The scaling experiment

The lognormal formula contains `sqrt(T)Z`. To make that uncertainty arrive piece by piece, divide one year into 100 equal steps. If each independent shock had typical size proportional to `dt=.01`, their accumulated variance would shrink toward zero as partitions became finer. If each retained fixed size, total variance would explode. Size `sqrt(dt)=.1` is the balance: 100 variances of .01 add to one.

This is why uncertainty grows with square-root time under independent diffusion increments. Ten days of volatility is not ten times one day's; standard deviation scales near `sqrt(10)` in the idealized model.

Brownian motion `W_t` satisfies `W_0=0`, continuous paths, independent increments, and `W_t-W_s ~ N(0,t-s)`. Continuity sounds gentle, but the path is infinitely rough. Zooming in reveals fresh irregularity rather than a tangent.

## From additive noise to a tradable price

Writing `dS=mu Sdt+sigma SdW` makes both drift and noise proportional to current price. Over finite time its solution is the lognormal expression from the previous chamber. The `dW` symbol is not an ordinary infinitesimal number; it represents the limit of scaled random increments.

Ask what the model excludes: scheduled earnings jumps, overnight gaps, volatility clustering, price limits, and feedback between trading and volatility. Brownian motion is a controlled foundation because its assumptions are visible and tractable. It becomes dangerous when continuous-path convenience is mistaken for empirical completeness.

## A path-reading challenge

Simulate daily increments, then weekly increments with matching annual volatility. Their distributions should agree at the year horizon, but individual paths differ. Now insert one jump. No increase in Brownian sampling frequency can turn that discontinuity into hedgeable continuous motion.

> **Memory seal:** dust wanders down a corridor. Every smaller beam of light reveals fresh motion, and no instantaneous arrow can lie tangent to its track.

The missing tangent is not a poetic inconvenience. Option value bends with stock price, and the next chapter will show that the path's squared microscopic moves leave a macroscopic trace ordinary calculus would discard.

[Next: Quadratic Variation](../016-quadratic-variation/README.md)

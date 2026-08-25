# 015 — Brownian Motion: Continuous Surprise

We need continuous-time noise whose disjoint increments do not remember one another and whose variance grows with elapsed time. Brownian motion `W_t` begins at zero, has independent normal increments, and satisfies `W_{t+dt}-W_t ~ N(0,dt)`.

A typical noise increment has size `sqrt(dt)`, not `dt`. Summing `dt`-sized random shocks would disappear in the limit; summing larger shocks would explode. Square-root scaling preserves finite uncertainty.

Geometric Brownian motion writes `dS = mu S dt + sigma S dW`. The first term is drift; the second is random movement proportional to price. Brownian paths are continuous but nowhere classically differentiable. Ordinary calculus therefore fails exactly where the model places its uncertainty.

## The scaling experiment

Divide one year into 100 equal steps. If each independent shock had typical size proportional to `dt=.01`, their accumulated variance would shrink toward zero as partitions became finer. If each retained fixed size, total variance would explode. Size `sqrt(dt)=.1` is the balance: 100 variances of .01 add to one.

This is why uncertainty grows with square-root time under independent diffusion increments. Ten days of volatility is not ten times one day's; standard deviation scales near `sqrt(10)` in the idealized model.

Brownian motion `W_t` satisfies `W_0=0`, continuous paths, independent increments, and `W_t-W_s ~ N(0,t-s)`. Continuity sounds gentle, but the path is infinitely rough. Zooming in reveals fresh irregularity rather than a tangent.

## From additive noise to a tradable price

Writing `dS=mu Sdt+sigma SdW` makes both drift and noise proportional to current price. Over finite time its solution is the lognormal expression from the previous chamber. The `dW` symbol is not an ordinary infinitesimal number; it represents the limit of scaled random increments.

Ask what the model excludes: scheduled earnings jumps, overnight gaps, volatility clustering, price limits, and feedback between trading and volatility. Brownian motion is a controlled foundation because its assumptions are visible and tractable. It becomes dangerous when continuous-path convenience is mistaken for empirical completeness.

## A path-reading challenge

Simulate daily increments, then weekly increments with matching annual volatility. Their distributions should agree at the year horizon, but individual paths differ. Now insert one jump. No increase in Brownian sampling frequency can turn that discontinuity into hedgeable continuous motion.

> **Memory seal:** dust wanders down a corridor. Every smaller beam of light reveals fresh motion, and no instantaneous arrow can lie tangent to its track.

[Next: Quadratic Variation](../016-quadratic-variation/README.md)

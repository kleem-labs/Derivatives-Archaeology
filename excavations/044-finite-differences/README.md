# 044 — Finite Differences: Turning the PDE into a Grid

Finite differences replace derivatives in the pricing PDE with differences between nearby grid values. Starting from the payoff at maturity, the scheme marches backward through time.

Explicit methods are simple but conditionally stable; implicit methods are stable but require solving linear systems; Crank–Nicolson balances accuracy and stability but can oscillate near payoff kinks without care.

Grid boundaries, spacing, and convergence tests are part of the model implementation. A plausible number on one grid is not evidence of correctness.

## Replace motion with neighboring tiles

Lay a grid across stock price and time. Terminal tiles hold the payoff. A central difference approximates delta from neighboring stock tiles; a second difference approximates gamma; a time difference connects adjacent layers. Substitution turns the PDE into algebraic relationships among grid values.

An explicit scheme computes an earlier value directly from later neighbors but can become unstable unless time steps are small relative to price spacing. An implicit scheme solves a linear system and is more stable. Crank–Nicolson averages both time treatments for higher accuracy but can oscillate around sharp payoff kinks.

## Boundaries are economic statements

The grid cannot extend to infinite stock. At low and high boundaries, impose behavior implied by the contract: a call approaches zero as spot approaches zero and behaves roughly like stock minus discounted strike at very high spot. Poor boundaries contaminate interior values.

For American options, apply the exercise maximum at each time layer. Barrier boundaries can be absorbing or rebate-paying. The numerical method must encode the legal payoff correctly.

## Evidence of a solution

Refine time and stock grids separately, move outer boundaries, compare with a closed form, and inspect Greeks. Convergence toward the wrong boundary condition is still wrong. Negative option values or broken monotonicity reveal instability.

> **Memory seal:** the smooth pricing arch is hammered onto a mesh. Every edge tile must know what the contract does beyond the visible forge.

[Next: Transaction Costs and Discrete Hedging](../045-transaction-costs-and-discrete-hedging/README.md)

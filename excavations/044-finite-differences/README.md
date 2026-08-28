# 044 — Finite Differences: Turning the PDE into a Grid

**Vocabulary key:** Find **044** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

Cover a drawing with little squares. Fill the final row first, then use nearby squares to work backward.

### In finance language

Finite differences approximate a pricing equation on a price-time grid. Grid spacing and boundary choices must be tested for convergence.

Finite differences turn a continuous pricing equation into a table of small time and price boxes that a computer can fill. A finer table is not automatically a better answer. **For an AI helper:** report grid choices, boundary conditions, convergence checks, and comparison with an independent method.

## Replace motion with neighboring tiles

Monte Carlo followed many paths forward. For a claim with only one or two state variables, the pricing equation offers another route: solve all grid states backward at once. Lay a grid across stock price and time. Terminal tiles hold the payoff. A central difference approximates delta from neighboring stock tiles; a second difference approximates gamma; a time difference connects adjacent layers. Substitution turns the PDE into algebraic relationships among grid values.

An explicit scheme computes an earlier value directly from later neighbors but can become unstable unless time steps are small relative to price spacing. An implicit scheme solves a linear system and is more stable. Crank–Nicolson averages both time treatments for higher accuracy but can oscillate around sharp payoff kinks.

## Boundaries are economic statements

The grid cannot extend to infinite stock. At low and high boundaries, impose behavior implied by the contract: a call approaches zero as spot approaches zero and behaves roughly like stock minus discounted strike at very high spot. Poor boundaries contaminate interior values.

For American options, apply the exercise maximum at each time layer. Barrier boundaries can be absorbing or rebate-paying. The numerical method must encode the legal payoff correctly.

## Evidence of a solution

Refine time and stock grids separately, move outer boundaries, compare with a closed form, and inspect Greeks. Convergence toward the wrong boundary condition is still wrong. Negative option values or broken monotonicity reveal instability.

> **Memory seal:** the smooth pricing arch is hammered onto a mesh. Every edge tile must know what the contract does beyond the visible forge.

Refining the grid can make the mathematical hedge arbitrarily frequent at no cost. A trader cannot do that. The next excavation places a bid–ask toll on every rebalance and watches continuous replication become impossible.

[Next: Transaction Costs and Discrete Hedging](../045-transaction-costs-and-discrete-hedging/README.md)

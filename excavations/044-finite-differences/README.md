# 044 — Finite Differences: Turning the PDE into a Grid

Finite differences replace derivatives in the pricing PDE with differences between nearby grid values. Starting from the payoff at maturity, the scheme marches backward through time.

Explicit methods are simple but conditionally stable; implicit methods are stable but require solving linear systems; Crank–Nicolson balances accuracy and stability but can oscillate near payoff kinks without care.

Grid boundaries, spacing, and convergence tests are part of the model implementation. A plausible number on one grid is not evidence of correctness.

Next: [Transaction Costs and Discrete Hedging](../045-transaction-costs-and-discrete-hedging/README.md).


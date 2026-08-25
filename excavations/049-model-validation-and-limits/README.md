# 049 — Model Validation and the Limits of No-Arbitrage

The final excavation asks what evidence earns trust. A model should reproduce identities it claims, converge numerically, respect static-arbitrage bounds, explain parameter stability, compare against independent implementations, and survive hedge and scenario tests relevant to its use.

No-arbitrage is indispensable but incomplete. It constrains relative prices when trades are available; it does not guarantee liquidity, correct dynamics, stable parameters, accurate tail probabilities, or institutional survival through margin calls.

The mathematics of the foundational book is finite. Its core objects—cash flows, replication, measures, stochastic calculus, sensitivities, carry, curves, and numerical approximation—do not need endless chapters. What evolves are contracts, market structure, regulation, data, and models chosen when replication is incomplete.

The final habit is therefore not formula collection but disciplined excavation:

`contract → cash flows → assumptions → replication or measure → computation → hedge → failure test`.

Return to the [book conclusion](../../CONCLUSION.md).


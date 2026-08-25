# 022 — Theta: The Cost of the Clock

Theta is option sensitivity to calendar time, quoted as value change when time passes while spot and inputs stay fixed. A plain long option often has negative theta: fewer future paths remain as expiry approaches. But time decay is not guaranteed realized P&L because spot and implied volatility also move.

The Black–Scholes PDE ties theta to convexity and financing: `Theta + 0.5 sigma^2 S^2 Gamma + rS Delta - rV = 0` for a non-dividend-paying stock. Theta is therefore not an independent tax; it is one side of the local replication balance.

Next: [Vega and Rho](../023-vega-and-rho/README.md).


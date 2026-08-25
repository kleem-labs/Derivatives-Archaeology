# 011 — The Black–Scholes Limit

Let price changes become tiny and frequent. Assume a frictionless market, continuous trading, constant `r` and `sigma`, a lognormal stock process, and no arbitrage. A locally delta-hedged option loses its immediate exposure to the random stock shock. The remaining instantaneously riskless portfolio must earn the risk-free rate.

That argument produces the Black–Scholes partial differential equation:

`V_t + 0.5 sigma^2 S^2 V_SS + rS V_S - rV = 0`

for a non-dividend-paying stock. Solving it with the European call payoff gives

`C = S_0N(d_1) - Ke^(-rT)N(d_2)`,

where `d_1=[ln(S_0/K)+(r+sigma^2/2)T]/(sigma sqrt(T))` and `d_2=d_1-sigma sqrt(T)`.

For spot $100, strike $105, rate 5%, volatility 20%, and one year, the lab gives a call near $8.02 and a put near $7.90; their difference still satisfies parity.

The formula is not the destination. Its assumptions create the next dig sites: random variables, Brownian motion, Itô calculus, Greeks, implied volatility, discrete hedging, smiles, jumps, and model risk.

Return to the [roadmap](../../ROADMAP.md) or run [the laboratory](../../labs/derivatives_lab.py).


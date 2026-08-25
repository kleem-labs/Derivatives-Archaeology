# 011 — The Black–Scholes Limit

Stand far from the binomial orchard. As branches become smaller and more numerous, the staircase of possible prices blurs into a continuous canopy. The local hedge remains: at each instant, hold enough stock to cancel the option's immediate random movement.

This is the intuition behind Black–Scholes. The famous formula is the last line of an argument, not the first.

## The model world

Assume the stock follows geometric Brownian motion with constant volatility `sigma`; trading is continuous and frictionless; stock and cash can be traded and shorted; the risk-free rate is known; and the claim can be replicated. For a non-dividend-paying stock,

`dS=mu Sdt+sigma SdW`.

An option value `V(S,t)` changes with time, stock direction, and curvature. Itô's lemma—earned later in detail—gives a random term proportional to `V_S sigma S dW`. Hold `Delta=V_S` shares against the option and that same shock cancels.

The remaining portfolio is instantaneously riskless inside the model. No-arbitrage requires it to earn the risk-free rate. After rearrangement:

`V_t + 0.5 sigma^2 S^2 V_SS + rS V_S - rV = 0`.

Notice what vanished: `mu`, the stock's real-world expected return. Replication removed the immediate stock risk, so the option price does not require agreement on the stock's risk premium.

## The terminal promise chooses the solution

The PDE describes many possible claims. The terminal condition identifies one. For a European call it is `V(S,T)=max(S-K,0)`. Solving backward yields

`C=S_0N(d_1)-Ke^(-rT)N(d_2)`,

`d_1=[ln(S_0/K)+(r+sigma^2/2)T]/(sigma sqrt(T))`, and `d_2=d_1-sigma sqrt(T)`.

At spot $100, strike $105, rate 5%, volatility 20%, one year, the call is about $8.0214. The corresponding put is $7.9004, and their $0.1209 difference matches parity.

## What the symbols are doing

`N(d_2)` behaves as a risk-neutral exercise probability in this model. `S_0N(d_1)` is not merely spot times an arbitrary chance; its weighting arises from the stock component of replication. The discounted strike term accounts for cash paid only in exercise states.

## The formula's shadow

Real prices jump. Volatility changes. Hedging is discrete. Funding and borrowing differ. Transactions cost money. A numerical price can be precise while the model is wrong. Black–Scholes is best treated as a common language, replication benchmark, and implied-volatility coordinate—not an oracle.

> **Memory seal — the vanishing staircase:** the tree dissolves into a continuous arch, but every invisible step still carries a local stock-and-cash hedge.

## Excavation questions

1. Name the assumption responsible for each term in the PDE.
2. Explain why `mu` disappears while `sigma` remains.
3. Change volatility in the lab from 20% to 30%. Predict call direction before running it.
4. Give one market where continuous-path assumptions are especially dangerous.

## The descent beneath the formula

We have used probability, Brownian motion, curvature, and changing measures before fully excavating them. The next eight chambers descend beneath the closed form and recover those roots.

[Next: Random Variables](../012-random-variables/README.md) · [Run the pricing lab](../../labs/derivatives_lab.py)


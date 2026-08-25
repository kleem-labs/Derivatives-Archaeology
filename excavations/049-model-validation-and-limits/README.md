# 049 — Model Validation and the Limits of No-Arbitrage

The final excavation asks what evidence earns trust. A model should reproduce identities it claims, converge numerically, respect static-arbitrage bounds, explain parameter stability, compare against independent implementations, and survive hedge and scenario tests relevant to its use.

No-arbitrage is indispensable but incomplete. It constrains relative prices when trades are available; it does not guarantee liquidity, correct dynamics, stable parameters, accurate tail probabilities, or institutional survival through margin calls.

The mathematics of the foundational book is finite. Its core objects—cash flows, replication, measures, stochastic calculus, sensitivities, carry, curves, and numerical approximation—do not need endless chapters. What evolves are contracts, market structure, regulation, data, and models chosen when replication is incomplete.

The final habit is therefore not formula collection but disciplined excavation:

`contract → cash flows → assumptions → replication or measure → computation → hedge → failure test`.

## Put a new model on trial

A team presents a beautiful exotic-option engine. It reproduces market quotes to six decimals. The tribunal asks questions calibration alone cannot answer.

Does a zero-volatility call approach discounted intrinsic forward value? Does increasing strike lower call price? Do call spreads and butterflies remain nonnegative? Does a European implementation satisfy parity? Do tree, Monte Carlo, and finite-difference answers converge toward a common vanilla benchmark? Are units, dates, dividends, and settlement tested at boundaries?

Then come questions of use. Are parameters stable? Does the model hedge the products for which dynamics matter? What happens outside calibration strikes? Which risk factors are unspanned? Can another implementation reproduce the result from the term sheet? Are reserves and limitations visible to the decision maker?

## The final valuation discipline

When reading an option market, never jump from model output to “worth it.” Assemble:

1. the exact executable contract and bid/ask;
2. no-arbitrage bounds and relative-value identities;
3. implied surface under consistent inputs;
4. real-world scenarios or distribution supporting the thesis;
5. more than one reasonable model when omitted features matter;
6. costs, funding, taxes where known, margin, and exit;
7. maximum and stress loss;
8. a conservative valuation range and falsifier.

A call can be worth buying as an asymmetric view, a volatility position, or insurance. A put can be worth more to a concentrated holder than to a diversified speculator. Seller and buyer may both improve their circumstances through risk transfer without either possessing a universal “true price.”

## The book's last decision

You design a derivative whose payoff no traded portfolio exactly spans. Do you publish one precise value? The archaeology says no. Publish assumptions, bounds, model range, sensitivities, hedge, residual risk, and evidence. Precision must never outrun identification.

> **Memory seal — the model tribunal:** the formula stands under light with its assumptions, inputs, numerical evidence, and failure modes visible. Elegance receives no special immunity.

## Graduation challenge

Complete the [Derivative Design Studio](../../DERIVATIVE_DESIGN_STUDIO.md) capstone. Give the same term sheet and evidence to a buyer and seller. If each can reproduce the cash flows, understand the other's case, and locate the remaining disagreement, the book has done its work.

Return to the [book conclusion](../../CONCLUSION.md) and record evidence in the [Mastery Ledger](../../MASTERY_LEDGER.md).

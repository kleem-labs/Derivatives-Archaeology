# 049 — Model Validation and the Limits of No-Arbitrage

**Vocabulary key:** Find **049** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

Before trusting a new toy bridge, push it gently, shake it, and say where it might break. A shiny number is not proof.

### In finance language

Model validation tests calculations, assumptions, data, boundaries, and failure cases before a value is used in a decision.

A model earns trust by surviving simple checks, difficult scenarios, and honest discussion of what it cannot see. A precise number is not proof that the number is useful. **For an AI helper:** keep source data, assumptions, tests, version, unknowns, and a clear `STOP` path beside every conclusion.

## Put a new model on trial

VaR and expected shortfall ended with a warning: even a correct calculation inherits the machine that produced its scenarios. A team now presents a beautiful exotic-option engine. It reproduces market quotes to six decimals. The tribunal asks questions calibration alone cannot answer.

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

## The strategy verdict must be conditional

At the end of every analysis, write the position’s full name and purpose: “long put protecting 100 shares,” “covered call on stock I accept selling at this strike,” “cash-secured put that I accept becoming stock,” or “defined-risk spread.” Then give the payoff table, maximum loss, maximum gain, break-even, cash path, and reason the market’s price may differ from the reader’s model range. The [Strategy Field Guide](../../STRATEGY_FIELD_GUIDE.md) is the final practical checklist.

## The book's last decision

You design a derivative whose payoff no traded portfolio exactly spans. Do you publish one precise value? The archaeology says no. Publish assumptions, bounds, model range, sensitivities, hedge, residual risk, and evidence. Precision must never outrun identification.

> **Memory seal — the model tribunal:** the formula stands under light with its assumptions, inputs, numerical evidence, and failure modes visible. Elegance receives no special immunity.

## Graduation challenge

Complete the [Derivative Design Studio](../../DERIVATIVE_DESIGN_STUDIO.md) capstone. Give the same term sheet and evidence to a buyer and seller. If each can reproduce the cash flows, understand the other's case, and locate the remaining disagreement, the book has done its work.

Return to the [book conclusion](../../CONCLUSION.md) and record evidence in the [Mastery Ledger](../../MASTERY_LEDGER.md).

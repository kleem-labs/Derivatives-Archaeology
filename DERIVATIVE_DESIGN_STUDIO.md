# Derivative Design Studio

The goal is not novelty for its own sake. A useful derivative transfers a clearly named risk with cash flows that two parties can observe, fund, settle, and challenge.

## 1. Begin with the exposure

Write: “Party A loses when ___; Party B can bear that risk because ___.” Identify the underlying observable, economic quantity, horizon, units, and undesirable states. If no genuine exposure or informed view exists, a new payoff may only add complexity.

## 2. Write the contract before pricing it

Specify parties; trade, observation, exercise, and settlement dates; underlying source and fallback; notional; currency; payoff function; caps, floors, barriers, averaging; physical or cash settlement; exercise rights; margin; termination and disruption events; rounding; and counterparty protections.

Example weather-linked payoff for a farmer:

`payoff = notional * max(rainfall_floor - measured_rainfall, 0)`.

The observable must name a weather station, measurement window, missing-data rule, and payment date. Otherwise the equation is not a contract.

## 3. Draw and attack the payoff

Build tables for ordinary, boundary, and extreme states. Check units, signs, maximum loss, discontinuities, path dependence, manipulation incentives, and whether buyer and seller cash flows reconcile. Ask what happens at exactly the strike or barrier.

## 4. Search for replication and bounds

Decompose the payoff into cash, forwards, calls, puts, digitals, or traded futures. Exact replication gives relative value. Super- and sub-replicating portfolios give bounds. If neither is practical, state which risk remains unspanned.

## 5. Choose a model because of the missing risk

Use a tree for discrete exercise decisions, Monte Carlo for many factors or path dependence, finite differences for low-dimensional PDEs, or scenario-weighted valuation when data are sparse. Separate risk-neutral calibration from real-world forecasting. Calibration fit is necessary, not proof.

## 6. Calculate economics, not only model value

Produce model value, parameter uncertainty, Greeks or scenario exposures, hedge instruments, transaction and funding costs, liquidity reserve, counterparty adjustment, and capital or margin needs. A theoretical value of $10 does not justify buying at $9 if hedging and exit cost $3.

## 7. State the deal's edge and falsifier

For buyer and seller separately, state why their forecasts, constraints, or risk-bearing capacity differ. Then name observations that would invalidate the thesis. A derivative can benefit both parties through risk transfer even when neither has discovered a mispricing.

## Capstone specification

Design one original contract and deliver:

1. one-page term sheet;
2. payoff equation, table, and diagram;
3. static replication or bounds;
4. pricing-model choice and rejected alternatives;
5. implementation with independent checks;
6. hedge plan and residual risks;
7. buyer and seller memos;
8. stress cases, legal ambiguities, and failure conditions.

Use [the payoff laboratory](labs/payoff_studio.py) as a transparent first prototype, never as production valuation infrastructure.


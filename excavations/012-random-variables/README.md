# 012 — Random Variables: Naming an Unknown Outcome

## First, in everyday words

A random variable is simply a name that turns each possible future into a number, such as the price of wheat in March. It names the outcome; it does not yet say how likely each outcome is. **For an AI helper:** store exactly what is being observed and reject a model when the contract watches something the data record omits.

## From warehouse labels to uncertain worlds

The fine tree left us with more leaf labels than we can list. Return to Mara's wheat. “March wheat price” is not yet one number. It is a collection of possible numbers attached to possible worlds: drought, abundant harvest, export ban, ordinary season. A random variable is the labeling rule that writes a price on each world. Probability belongs to a second layer that says how much weight each world receives.

This distinction becomes practical when designing a derivative. A rainfall contract might observe total millimeters at one station, while the farmer's loss depends on moisture across an entire region. The random variable in the legal contract is the station reading. The economic exposure is crop loss. Basis risk enters because those mappings differ.

For a discrete example, let `S_T` take $80, $100, or $130. The call payoff with strike $100 maps those same states to $0, $0, and $30. We did not draw new worlds; we applied a new function to the old state label. The contract changes the mapping, not reality.

Continuous models replace a table with a distribution function. `F(x)=P(S_T<=x)` answers the weight accumulated below `x`; a density describes probability per unit of price, so a single exact continuous price usually has probability zero even though intervals have positive probability.

## The decision before calculation

You are given two models with identical terminal distributions but different price paths. Can they price a barrier option identically? No: terminal `S_T` is sufficient for a European call, but a barrier watches the path. The state description must retain every feature the payoff observes.

That lesson governs original derivative design: first specify the smallest state containing all contract-relevant information. Too little state misprices the claim; too much state wastes computation without adding meaning.

> **Retrieval challenge:** without using the words “chance” or “distribution,” explain what the random variable itself does. Then explain where probability enters.

## Assumption audit

A chosen state space can omit disasters, closures, negative prices, or contract disruptions. Probability zero inside a model is not impossibility in the world. Every valuation inherits the boundaries of the modeled states.

[Next: Expectation and Variance](../013-expectation-and-variance/README.md)

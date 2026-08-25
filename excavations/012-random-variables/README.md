# 012 — Random Variables: Naming an Unknown Outcome

A future stock price is unknown, but it is not indescribable. A random variable assigns a number to every state we consider possible. `S_T` names the future stock price; `max(S_T-K,0)` transforms that same state into a call payoff.

A naive list of possible prices works for a two-state tree but collapses when prices can vary continuously. A distribution repairs the list by assigning probability mass or density across outcomes. Its cumulative distribution answers `P(S_T <= x)`.

The random variable is a function from uncertain states to numbers. The distribution records beliefs or model weights over those states. Pricing may use a risk-neutral distribution distinct from the real-world distribution used for forecasting and risk.

**Recovered artifact:** separate the payoff function from the weights placed on states. Confusing them makes a contract appear to contain a forecast.

Next: [Expectation and Variance](../013-expectation-and-variance/README.md).


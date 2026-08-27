# Four weeks to read a derivative without fooling yourself

This is a learning plan, not a promise of stock-market success. The goal after four weeks is simple and valuable: you can look at a listed option or futures contract, explain what it asks of each side, calculate a few possible outcomes, state what information is missing, and refuse to guess when the evidence is weak.

Do not use money you need for living costs, emergencies, or long-term needs. The CFTC’s own pre-trade checklist starts with your goals and the loss you can sustain; its futures education explains that daily marking to market can require more money while a position is open. Read the relevant disclosure document and your broker’s current contract terms before any live trade. See [CFTC’s checklist](https://www.cftc.gov/LearnAndProtect/EducationCenter/checklistbeforeyoutrade.html), [CFTC’s futures explanation](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/economicpurpose.html), and the [OCC Options Disclosure Document](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document).

## Week 1 — Learn the contract before the price

Read Book Volume I and Volume II, Chapters 000–011. Do not open a chart first.

Every day, choose one imaginary contract and write six answers in a notebook:

1. What is the underlying thing?
2. Who has the right, and who has the obligation?
3. What is the strike or delivery price?
4. What is the expiration or delivery date?
5. What is one contract’s multiplier and settlement method?
6. What can each side lose at three future prices?

Your checkpoint: explain why a purchased call, a written call, a purchased put, and a written put are four different risk stories. Do not call a short option “income” until you can name the obligation it creates. FINRA notes that some writers can face significant loss and that uncovered calls can theoretically have unlimited loss. [Read FINRA’s overview.](https://www.finra.org/investors/investing/investment-products/options)

## Week 2 — Learn where a fair-number estimate comes from

Read Volume III and Chapters 020–026. Use the lab only with made-up inputs.

For each case, make a three-row table: price below strike, price at strike, price above strike. Then change only one input at a time: time, volatility guess, interest rate, or underlying price. Say what changed and why.

Your checkpoint: distinguish these three sentences:

- “This contract can pay this amount at expiration.”
- “This model estimates this value if its assumptions are reasonable.”
- “This is the price available to buy or sell right now.”

Only the first sentence is certain once the contract and future price are fixed. The second depends on assumptions. The third depends on real quotes and may include a spread.

## Week 3 — Learn the parts a neat formula leaves out

Read Volume IV and Volume V, especially the chapters on volatility, carry, margin, futures, and options on futures.

Work through five paper cases. In each one, write the final payoff **and** the bad path before the final date. For a future, mark a daily loss and decide whether the account can meet it. For an option, include the bid–ask spread and ask whether the order could really be filled at the screen price.

Your checkpoint: state why “maximum loss at expiration” and “cash needed before expiration” are different questions. Futures margin is a performance bond and accounts are marked to market daily, according to the CFTC. [Read the explanation.](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/economicpurpose.html)

## Week 4 — Build an analysis record, not a prediction habit

Read Volume VI, the [Market Reading guide](MARKET_READING_AND_VALUE.md), and the [Agentic System Blueprint](AGENTIC_SYSTEM_BLUEPRINT.md). Complete ten paper analyses. Five should be ordinary listed calls or puts; five should be futures, spreads, or made-up contracts.

For every analysis, retain:

- the full contract description and a time-stamped quote source;
- a payoff table and the position’s worst plainly stated outcome;
- model inputs, including why each input was chosen;
- a model range, not one magical number;
- bid, ask, likely transaction costs, and the data timestamp;
- a sentence beginning “I would be wrong if …”; and
- a decision of `study only`, `paper test`, or `insufficient evidence`.

Your checkpoint: invent a small derivative for a real business problem, then ask whether stock, cash, or a simpler existing contract can copy it. If yes, price the copy. If no, name the risk that remains and do not pretend a single model has solved it.

## Graduation test

You are ready to move from this foundation to deeper study when you can do all of the following without a price chart:

1. Translate a contract into a payoff table.
2. Explain holder, writer, exercise, assignment, settlement, and multiplier in ordinary words.
3. Identify the maximum loss only when the position really has one.
4. Separate a market belief from a no-arbitrage relationship.
5. Explain the model’s assumptions and one way they could fail.
6. Refuse to produce a conclusion when key contract or market data is missing.

That is genuine progress. Market outcomes remain uncertain; disciplined reasoning is the part you can control.

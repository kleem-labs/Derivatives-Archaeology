# Research foundation — simple derivatives book and agent layer

**Research completed:** 27 August 2026  
**Scope:** U.S.-listed stock options and exchange-traded futures, for education and decision support. This is not a recommendation to trade, legal advice, broker documentation, or a promise of returns.

## The question this research answers

How can a first-time reader learn enough mathematics to describe, check, and value a derivative without being pushed into a reckless trade? And how can that understanding become the foundation for an AI helper that shows its work?

The answer is not a prediction machine. It is a sequence of small checks:

1. Read the exact contract.
2. Draw what it pays in plain dollars at several future prices.
3. Check what can be copied with stock, cash, or a simpler contract.
4. Compare a model estimate with a price a person could actually trade at.
5. Name the data, assumptions, costs, and ways the answer could be wrong.
6. Require a person to decide whether to trade.

## What the primary sources require us to teach

| Finding | What it changes in this book |
|---|---|
| An option gives its holder a right, while its writer accepts an obligation. A purchased option can lose its full premium; some written options can have unlimited loss. | Teach buyer and seller as different jobs; never describe “an option” as having one universal risk. |
| A U.S. broker must approve an options account and provide the Options Disclosure Document before covered listed-options activity. | Put contract literacy and the ODD before any live trade discussion. |
| One standard equity option contract commonly represents 100 shares; exercise and assignment can require a large stock transaction. | Make multiplier, exercise style, settlement, and assignment mandatory fields in every contract record. |
| Futures margin is a performance bond, not a down payment. Positions are marked to market and can require additional funds. | Teach cash-path risk separately from final payoff; a hedge can be sensible at the end and still fail on the way. |
| Leverage can magnify losses, including losses beyond money initially posted in a futures account. | No lesson may equate a small upfront payment with a small risk. |
| NIST’s AI risk framework uses the ongoing functions Govern, Map, Measure, and Manage, with human oversight and documented testing. | The AI design must have explicit limits, data checks, test cases, audit records, and a human approval gate. |

## Sources and how they were used

1. [OCC, *Characteristics and Risks of Standardized Options* landing page](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document) — current June 2024 ODD availability and the instruction to read it before buying or selling exchange-traded options. Used for the book’s required-disclosure reading gate.
2. [SEC Investor.gov, *An Introduction to Options*](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-63) — plain definitions, loss of a long option’s premium, and potentially unlimited loss for some writers. Used for beginner-risk wording.
3. [FINRA, *Options*](https://www.finra.org/investors/investing/investment-products/options) — account approval, the holder/writer distinction, 100-share equity-option exposure, assignment, exercise funding, and margin risks. Used for the contract checklist and agent gates.
4. [CFTC, *Economic Purpose of Futures Markets and How They Work*](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/economicpurpose.html) — hedging purpose, performance-bond margin, daily marking to market, maintenance margin, and variation margin. Used for the futures chapters and cash-path check.
5. [CFTC, *Checklist Before You Trade*](https://www.cftc.gov/LearnAndProtect/EducationCenter/checklistbeforeyoutrade.html) — identify goals and sustainable loss, review disclosures, and check advisers. Used for the one-month study boundary.
6. [NIST, *AI Risk Management Framework 1.0*](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) and its [Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) — voluntary risk-management framework and the Govern/Map/Measure/Manage structure. Used for the agent blueprint’s controls.
7. [Options Industry Council, *How LEAPS® Work*](https://www.optionseducation.org/optionsoverview/how-leaps-work), [*LEAPS® Pricing*](https://prd-web.optionseducation.org/optionsoverview/leaps-pricing), and [*LEAPS® Strategies*](https://prd-web.optionseducation.org/optionsoverview/leaps-strategies) — long-term options mechanics, finite-life and input risk, and illustrative payoff trade-offs. Used for the strategy field guide; these are education resources, not suitability findings.

## Design decisions made from the research

### Keep the first reading path human

The reader meets cash, dates, rights, obligations, and bad outcomes before symbols. Models come only after the reader can draw the payoff and say which real-world promise it represents. This is why the six-volume edition stays the front door and the excavations remain the workshop.

### Teach a usable definition of “worth it”

“Worth it” is not one number and is never a guarantee of profit. It is a comparison among three things:

`what the contract could pay` + `what the model assumes` + `what price can actually be traded`

The reader must also include fees, bid–ask spread, cash needed after a margin call, tax consequences, and the possibility that a model is wrong. A call that looks cheap under one volatility guess may still be a poor trade once its spread and the buyer’s actual purpose are considered.

### Build an AI auditor, not an AI trader

The book’s agent design has no authority to submit, modify, or cancel orders. It may calculate and explain. It must stop when a required fact is absent, stale, contradictory, or outside its stated model. A human has to supply the purpose, loss limit, and final decision. This is an intentional scope limit, not a technical omission.

### Be honest about the one-month goal

Four weeks can build contract literacy, payoff fluency, basic valuation judgment, and a repeatable paper-analysis routine. It cannot responsibly guarantee stock-market success. The final week is therefore a record of simulated cases and error checks, not a demand to place a trade.

## Important limits

- Contract terms vary by product, exchange, and broker. The actual contract specification and broker agreement win over a book example.
- This research does not assess a particular reader’s finances, tax situation, legal jurisdiction, risk tolerance, or a particular security.
- A pricing model is a conditional estimate. It is not a forecast and it does not remove liquidity, jump, counterparty, operational, or execution risk.
- Regulations and broker policies change. Check the linked primary source and the broker’s current documents before acting.

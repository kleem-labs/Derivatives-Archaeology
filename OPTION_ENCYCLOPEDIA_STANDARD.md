# Option Encyclopedia Standard

This repository is not allowed to use a financial word as if it explains itself.

## The reader’s contract

Before a chapter asks you to use an idea, it must tell you:

1. **What you already need to know.** These are ordinary-language ideas and earlier chapter numbers, not a hidden prerequisite.
2. **What new word is being born.** The first definition says what the thing is, what it is not, and why the reader needs it now.
3. **Which kind of statement it is.** Every important claim is labelled, in meaning if not in a literal tag, as one of:
   - **Contract fact** — written in the actual contract or term sheet.
   - **Mathematical result** — follows from stated mathematics.
   - **Model assumption** — a simplification used to calculate.
   - **Market convention** — a common practice that can vary by product, exchange, or broker.
   - **Strategy judgment** — a reader’s conditional choice, never a universal command.
4. **What question the word repairs.** A definition without a problem is a label, not understanding.
5. **What it changes in a buy, sell, hedge, or wait decision.** Mathematics must arrive back at a position’s cash flows and obligations.

## The order of explanation

Every new concept follows this order:

`thing in the world → plain description → small numerical example → name → symbol or formula → assumption → failure case → strategy consequence`

For example, the book shows the right to buy before calling it a call; shows a cash payment on a later date before calling it discounting; shows a stock-and-cash copy before calling it replication; and shows a seller’s obligation before discussing premium.

## Words that must never be used lazily

| Word | It must always mean |
|---|---|
| Price | The amount paid or received now for an identified contract, with a source and time when it is a market quote. |
| Payoff | The contract’s cash or asset result at a specified future state, before entry cost unless stated otherwise. |
| Profit / loss | Payoff after premium, purchase price, financing, and stated costs are included. |
| Value | A model estimate or no-arbitrage bound under stated assumptions; not automatically a tradable quote. |
| Premium | The option amount paid by buyer and received by seller at entry; not guaranteed income or maximum loss for the seller. |
| Risk | A bad outcome plus the path and conditions that could create it; never just a Greek letter or one percentile statistic. |
| Volatility | A particular movement measure, estimate, or model input; never a synonym for “will go up” or “will go down.” |
| Cheap / expensive | A relative conclusion that must name the comparison, model, assumptions, executable bid/ask, and costs. |
| Covered | A broker- and contract-specific description of how an obligation is supported; never inferred from a similar-looking long option. |

## Non-negotiable strategy rules

- Buying is the purchase of a right; selling is acceptance of that right’s obligation.
- Premium received is not a strategy’s profit until the position is closed or its obligations are settled.
- A maximum loss belongs to the **whole position**, not to one leg chosen for marketing.
- A contract with a finite expiry has a timing requirement even when the directional idea is right.
- A model number is only as good as the contract, quote, inputs, assumptions, and ability to trade around it.
- `Wait`, `paper test`, and `insufficient evidence` are legitimate final answers.

## How to use an encyclopedia chapter

Read the chapter’s vocabulary key in the [Concept Atlas](CONCEPT_ATLAS.md). If a prerequisite feels unfamiliar, return to its earlier chapter before continuing. At the end, say aloud:

> “This word exists because ___ was a problem. It means ___. It does not mean ___. In a position, it changes ___.”

If that sentence cannot be completed, the next formula should wait.

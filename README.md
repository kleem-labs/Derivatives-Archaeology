# Derivatives Archaeology

**Rediscover the mathematics behind options and futures from the market problems that forced it to exist.**

This repository is both a book and a laboratory. It begins before Black–Scholes, before stochastic calculus, and even before a pricing formula: two people make promises about an uncertain future and need to decide what those promises are worth today.

The method is:

```text
market reality → question → naive price → arbitrage or risk → repair → equation → experiment
```

The purpose is understanding, not trading advice. Real derivatives involve model risk, liquidity, transaction costs, taxes, legal terms, margin, and losses larger than the initial investment.

## Start here

1. Read the [Plain-Language Promise](PLAIN_LANGUAGE_PROMISE.md).
2. Read the [Option Encyclopedia Standard](OPTION_ENCYCLOPEDIA_STANDARD.md) and use the [Concept Atlas](CONCEPT_ATLAS.md) before each chapter.
3. Enter the [six-volume book edition](book/README.md), beginning with Volume I.
4. Keep the [glossary](GLOSSARY.md), [notation guide](NOTATION.md), and [formula map](FORMULA_MAP.md) nearby.
5. Rebuild each result in the [laboratory](LABORATORY.md).
6. Walk the [50-Chamber Memory Palace](MEMORY_PALACE.md) until the ideas can be recalled without the page.
7. Follow [How to Master This Book](HOW_TO_MASTER_THIS_BOOK.md) to progress from reading to designing and valuing unfamiliar derivatives.
8. Use the [four-week foundation](ONE_MONTH_FOUNDATION.md) to turn the reading into a disciplined paper-analysis practice.
9. Build only a checkable, non-executing research helper from the [Agentic System Blueprint](AGENTIC_SYSTEM_BLUEPRINT.md).
10. Use the [Strategy Field Guide](STRATEGY_FIELD_GUIDE.md) to connect the mathematics to the real choice: buy a right, sell an obligation, hedge an exposure, or wait.

## The complete fifty-excavation book

| # | Excavation | Question |
|---:|---|---|
| 000 | [A Promise About the Future](excavations/000-a-promise-about-the-future/README.md) | What exactly is a derivative? |
| 001 | [Payoffs Before Prices](excavations/001-payoffs-before-prices/README.md) | How can a contract be described without guessing its value? |
| 002 | [Time Has a Price](excavations/002-time-value-of-money/README.md) | Why is one dollar later not one dollar now? |
| 003 | [No Free Lunch](excavations/003-no-arbitrage/README.md) | What makes two different portfolios require the same price? |
| 004 | [The Forward Price](excavations/004-forward-price/README.md) | What delivery price prevents a free profit? |
| 005 | [Futures Are Re-settled](excavations/005-futures-marking-to-market/README.md) | Why can futures and forwards differ? |
| 006 | [Options Create Asymmetry](excavations/006-option-payoffs/README.md) | What is the value of a right without an obligation? |
| 007 | [Put–Call Parity](excavations/007-put-call-parity/README.md) | Which portfolios have the same terminal payoff? |
| 008 | [One Period, Two Futures](excavations/008-one-period-binomial/README.md) | Can an option be priced without forecasting probabilities? |
| 009 | [Risk-Neutral Probability](excavations/009-risk-neutral-probability/README.md) | Why does a probability appear even when beliefs disappear? |
| 010 | [Many Small Steps](excavations/010-multi-period-binomial/README.md) | How does local replication become an option-pricing tree? |
| 011 | [The Black–Scholes Limit](excavations/011-black-scholes-limit/README.md) | What survives when the time steps become tiny? |

Chapters 012–049 complete the journey through probability, stochastic calculus, Greeks, volatility, futures, rates, early exercise, path dependence, numerical methods, market frictions, portfolio risk, and model validation. Use the [complete table of contents](TABLE_OF_CONTENTS.md) or the [six-part reading path](PARTS.md).

## Repository map

- `excavations/` — the causal book, one idea per dig site
- `labs/` — executable experiments with visible intermediate values
- `tests/` — numerical identities and failure checks
- [FORMULA_MAP.md](FORMULA_MAP.md) — equations grouped by the problem they solve
- [GLOSSARY.md](GLOSSARY.md) — plain-language definitions
- [OPTION_ENCYCLOPEDIA_STANDARD.md](OPTION_ENCYCLOPEDIA_STANDARD.md) — the rule that every term must earn its first use
- [CONCEPT_ATLAS.md](CONCEPT_ATLAS.md) — chapter-by-chapter prerequisites, new words, and decision purpose
- [BOOK_AND_LAB_STANDARD.md](BOOK_AND_LAB_STANDARD.md) — what “complete” means
- [DERIVATIVE_DESIGN_STUDIO.md](DERIVATIVE_DESIGN_STUDIO.md) — a disciplined process for inventing contracts
- [MARKET_READING_AND_VALUE.md](MARKET_READING_AND_VALUE.md) — compare model value with executable quotes
- [MASTERY_LEDGER.md](MASTERY_LEDGER.md) — evidence that the reader can work independently
- [SOLUTIONS.md](SOLUTIONS.md) — worked answers, kept separate from the reading path
- [ONE_MONTH_FOUNDATION.md](ONE_MONTH_FOUNDATION.md) — a four-week, paper-first study routine
- [AGENTIC_SYSTEM_BLUEPRINT.md](AGENTIC_SYSTEM_BLUEPRINT.md) — data, calculations, guardrails, and audit records for a non-executing AI helper
- [STRATEGY_FIELD_GUIDE.md](STRATEGY_FIELD_GUIDE.md) — payoff mathematics and decision logic for buying, selling, hedging, spreads, and LEAPS®
- [report-source.md](report-source.md) — the primary-source research and design rationale for this edition

## Quick laboratory run

```bash
python3 labs/derivatives_lab.py
python3 labs/advanced_lab.py
python3 -m unittest discover -s tests -v
```

No external packages are required.

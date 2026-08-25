# Derivatives Archaeology

**Rediscover the mathematics behind options and futures from the market problems that forced it to exist.**

This repository is both a book and a laboratory. It begins before Black–Scholes, before stochastic calculus, and even before a pricing formula: two people make promises about an uncertain future and need to decide what those promises are worth today.

The method is:

```text
market reality → question → naive price → arbitrage or risk → repair → equation → experiment
```

The purpose is understanding, not trading advice. Real derivatives involve model risk, liquidity, transaction costs, taxes, legal terms, margin, and losses larger than the initial investment.

## Start here

1. Read the [reading path](PARTS.md).
2. Enter [Excavation 000](excavations/000-a-promise-about-the-future/README.md).
3. Keep the [notation guide](NOTATION.md) and [formula map](FORMULA_MAP.md) nearby.
4. Rebuild each result in the [laboratory](LABORATORY.md).
5. Walk the [50-Chamber Memory Palace](MEMORY_PALACE.md) until the ideas can be recalled without the page.
6. Follow [How to Master This Book](HOW_TO_MASTER_THIS_BOOK.md) to progress from reading to designing and valuing unfamiliar derivatives.

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
- [BOOK_AND_LAB_STANDARD.md](BOOK_AND_LAB_STANDARD.md) — what “complete” means
- [DERIVATIVE_DESIGN_STUDIO.md](DERIVATIVE_DESIGN_STUDIO.md) — a disciplined process for inventing contracts
- [MARKET_READING_AND_VALUE.md](MARKET_READING_AND_VALUE.md) — compare model value with executable quotes
- [MASTERY_LEDGER.md](MASTERY_LEDGER.md) — evidence that the reader can work independently

## Quick laboratory run

```bash
python3 labs/derivatives_lab.py
python3 labs/advanced_lab.py
python3 -m unittest discover -s tests -v
```

No external packages are required.

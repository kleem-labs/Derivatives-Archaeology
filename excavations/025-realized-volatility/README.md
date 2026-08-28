# 025 — Realized Volatility: Measuring the Path That Happened

**Vocabulary key:** Find **025** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **025** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Look back at the footprints the price already made and measure how wiggly they were. Yesterday’s wiggles do not promise tomorrow’s.

### In finance language

Realized volatility is a historical movement estimate from a named price sample and time window.

Realized volatility measures how much the price actually moved over a past window. It describes a finished path; it does not automatically forecast the next one. **For an AI helper:** give the date window, sampling rule, and data source before comparing realized and implied volatility.

## Build the measure from a path

The hedge ledger contains the path that actually occurred. We need a way to summarize its movement. Take closing prices 100, 102, 101, and 104. Convert each adjacent pair into log returns so multiplicative moves become additive. Centering and squaring those returns produces a sample variance; multiplying by a periods-per-year convention annualizes it, and the square root returns volatility units.

Every choice changes the answer. Should returns be centered by sample mean or treated as zero over short horizons? Use 252 trading days or calendar time? Include overnight returns separately? Corporate actions and bad ticks must be cleaned before calculation.

High-frequency data creates another failure. More observations sound better, but bid–ask bounce can alternate recorded trade prices even when efficient value barely moves. At very fine intervals the estimator measures market microstructure as well as economic variation. Realized kernels and subsampling are repairs beyond the basic estimator.

## What a delta hedger actually experiences

Gamma-related hedging P&L responds to the weighted sequence of squared price moves, not only one annualized summary. Two paths can have similar realized variance yet generate different P&L because gamma changes with spot and time, jumps occur between hedges, and transaction costs depend on turnover.

Thus realized volatility is an empirical statistic with a sampling design. It is not an objective substance discovered after the fact.

> **Reader experiment:** calculate volatility from daily prices, then retain every second observation. Explain why the result changes even though the underlying path is the same.

> **Memory seal:** the seismograph records every tremor that the chosen sampling clock can see; a slower clock erases some, an overly fast clock hears the instrument itself.

The path measure is now complete only after the path ends. A live option must be quoted before that evidence exists. The market therefore turns the pricing model around and asks which movement scale is already embedded in today's premium.

[Next: Implied Volatility](../026-implied-volatility/README.md)

# Concept Atlas — the prerequisite map for all fifty chapters

This is the book’s anti-confusion map. Read the row before each excavation. “Already earned” names concepts the reader should recognize; “new words” are defined in that chapter before their formulas are used; “decision made clearer” tells you why the chapter belongs in an options encyclopedia.

## I — Describe the promise before pricing it

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 000 | cash today; cash later; agreement | underlying, derivative, forward, long, short | What future-price risk is being moved from one person to another? |
| 001 | contract; future state | payoff, state, payoff table | What does this rule give or take at each possible final price? |
| 002 | payoff; known payment date | compounding, discounting, present value | Is this a known future payment moved through time, or an uncertain payoff? |
| 003 | present value; equal payoffs | arbitrage, self-financing, replication | Do two routes truly end alike after costs and constraints? |
| 004 | replication; borrowing; spot price | spot, carry, forward price | Is owning now plus carrying equivalent to future delivery? |
| 005 | forward; delivery date | futures, marking to market, variation margin | Can I fund the cash path, not merely the final result? |

## II — Learn the right and the obligation

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 006 | payoff table; forward | call, put, strike, premium, holder, writer, intrinsic payoff | Am I buying a right or selling its obligation, and what is my whole-position loss? |
| 007 | call; put; stock; cash | put–call parity, synthetic position | Does a call/put price contradict an equivalent stock-and-cash bundle? |
| 008 | parity; replication | binomial tree, hedge ratio | Can a small stock-and-cash position copy this option in every stated outcome? |
| 009 | binomial copy; discounting | risk-neutral weight, pricing measure | Are these weights for pricing a copy, not for forecasting the market? |
| 010 | one-step tree; hedge ratio | backward induction, node | How does the required hedge change after each possible move? |
| 011 | many-step tree; model assumption | continuous-time limit, Black–Scholes prerequisites | Which tools are still missing before using a continuous formula? |

## III — Name uncertainty without pretending it is a forecast

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 012 | payoff; states | random variable, distribution, density | Does the model remember every feature the contract watches? |
| 013 | random variable; weights | expectation, variance, standard deviation | What is the average and spread of the stated scenarios—and what do they not promise? |
| 014 | distribution; positive price | normal, lognormal | Which price-shape assumption fits the use case, and which impossible events does it create or exclude? |
| 015 | random variable; time steps | Brownian motion, drift, diffusion | Is a continuous-wiggle model reasonable, or are gaps/events central to this contract? |
| 016 | Brownian motion; squared move | quadratic variation | Why does random motion require a different calculus rule? |
| 017 | derivative of a function; quadratic variation | Itô’s lemma, Itô term | Which parts of option change come from price movement, time, and curvature? |
| 018 | pricing weights; paths | change of measure, real-world measure | Is this probability statement a belief, a historical estimate, or a pricing device? |
| 019 | discounted value; pricing measure | martingale, numeraire, Black–Scholes PDE | Under which measuring stick and assumptions does the pricing equation hold? |

## IV — See what a living option needs and fears

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 020 | option value; derivative; multiplier | delta, local hedge | How much immediate direction does this whole position carry? |
| 021 | delta; local move | gamma, convexity | How quickly will the hedge ratio fail after a larger move? |
| 022 | delta; gamma; time to expiry | theta, time decay | Am I paying for time or receiving it while carrying a dangerous curve? |
| 023 | model input; sensitivity | vega, rho | How exposed is the position to uncertainty or rate changes rather than direction? |
| 024 | delta; gamma; transaction | dynamic hedge, rebalance error | How often could I hedge, and what does that cost or miss? |
| 025 | price path; variance | realized volatility, sampling | What movement actually occurred over this named historical window? |
| 026 | option quote; model; volatility | implied volatility | What volatility makes this exact quote fit this exact model—and is that enough to buy or sell? |
| 027 | implied volatility; strike; expiry | volatility smile, surface | Does one volatility input hide meaningful strike or date differences? |
| 028 | smile; model assumption | local volatility, stochastic volatility | Which richer model fits today’s market, and what new assumptions does it add? |
| 029 | hedge; jump; replication | jump risk, incomplete market, residual risk | What loss remains when no traded hedge can copy the contract exactly? |

## V — Put physical ownership, collateral, and dates back into the math

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 030 | spot; financing; forward | cost of carry, storage cost, income yield | Can this asset actually be owned, financed, stored, and delivered as the formula assumes? |
| 031 | carry; stock ownership | dividend, ex-dividend date, dividend yield | Which cash payment belongs to the stockholder but not the forward holder? |
| 032 | carry; inventory | convenience yield | Is physical availability valuable, and is that the only explanation for the observed price gap? |
| 033 | cash price; futures price | basis, convergence | Does the future actually offset the location, grade, and timing of the real exposure? |
| 034 | futures; variation margin | initial margin, maintenance margin, leverage | Can I survive the worst plausible cash call before my hedge has time to work? |
| 035 | basis; exposure; futures | hedge ratio, short hedge, long hedge | Which futures direction offsets the business risk rather than creating a second bet? |
| 036 | hedge; variance; correlation | minimum-variance hedge ratio | How much residual risk remains when the hedging contract is imperfect? |
| 037 | discounting; dated cash flows | zero rate, discount curve, bootstrapping | Which discount factor applies to each payment date? |
| 038 | curve; present value | forward rate, swap, fixed leg, floating leg | What does every rate-contract payment exchange on its own date? |
| 039 | option; future; margin | option on futures, exercise into futures | What happens to cash and margin if this option creates a futures position? |

## VI — Make the final decision survive real markets

| Chapter | Already earned | New words born here | Decision made clearer |
|---:|---|---|---|
| 040 | option payoff; expiry; dividend | American exercise, European exercise, assignment | Is using the option now better than keeping the remaining right? |
| 041 | American option; continuation value | early-exercise boundary, optimal stopping | At what conditions does waiting stop being valuable? |
| 042 | payoff; price path | barrier, path dependence, monitoring | Does the contract care about the route, not only the final price? |
| 043 | probability model; payoff; discounting | Monte Carlo, simulation error, confidence interval | Is the numerical estimate stable, and is the world-generator reasonable? |
| 044 | PDE; boundary; time step | finite-difference grid, convergence | Does a second numerical method agree after the grid is refined? |
| 045 | hedge; rebalance; spread | transaction cost, discrete hedge | Does a frictionless strategy remain useful after realistic trading tolls? |
| 046 | bid; ask; market quote | liquidity, bid–ask spread, executable price | Is the price in my comparison one I can actually trade? |
| 047 | delta; gamma; vega; multiplier | portfolio Greek, scenario | What happens when all positions move together in a bad but coherent story? |
| 048 | scenario; loss; distribution | Value at Risk, Expected Shortfall, tail | What does this risk number omit beyond its stated horizon and model? |
| 049 | all prior checks | validation, calibration, model risk, falsifier | Can I explain the position’s contract, range, risks, and reason to wait without false certainty? |

## The strategy layer, after the alphabet is learned

Once Chapters 000–049 are familiar, move to the [Strategy Field Guide](STRATEGY_FIELD_GUIDE.md). It combines the words into whole positions: long calls and puts, covered calls, cash-secured puts, protective puts, collars, verticals, straddles, calendars, diagonals, LEAPS®, and options on futures.

Do not start at strategy names. Start with the row for the word you do not understand, then return to the payoff table.

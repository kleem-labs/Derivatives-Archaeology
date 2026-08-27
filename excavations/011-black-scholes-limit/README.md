# 011 — The Black–Scholes Limit: A Door We Cannot Yet Open

## First, in everyday words

A very fine price tree begins to look smooth, but smooth-looking uncertainty still needs new tools. This chapter is a pause, not a magic leap to a famous formula. **For an AI helper:** say which required inputs and assumptions are still unknown rather than pretending a continuous model is already justified.

The binomial tree prices a call by moving backward from its terminal payoff. Make the tree finer and the answer stabilizes. With the book's inputs—spot $100, strike $105, rate 5%, volatility 20%, and one year—a 500-step tree gives about $8.02.

It is tempting to announce a continuous-time formula and move on. But the tree has hidden three unresolved questions inside its shrinking branches. If we cross the limit without answering them, the symbols will arrive before their responsibilities.

## What exactly is becoming continuous?

In a one-step tree the stock has two named outcomes. In a 500-step tree it has hundreds of terminal outcomes and vastly more paths. To let the step length approach zero, we need a mathematical object that describes an unknown value without listing every branch.

The terminal stock price will become a **random variable**: a rule assigning a number to each possible state. The tree's branch weights will become a distribution. But this raises an immediate discipline. The payoff rule and the probability weights are different objects. A call maps terminal price into cash; a model assigns weights to the terminal prices.

We will not use either term in a pricing formula until Chapters 012 and 013 build them from concrete states and weighted sums.

## How small is a small random move?

Suppose one year is divided into `n` steps. If each random move stayed the same size while `n` grew, total uncertainty would explode. If each move shrank in direct proportion to `1/n`, uncertainty would vanish. The tree converges only when the typical random move shrinks like `1/sqrt(n)`, or equivalently like the square root of elapsed time.

That scaling leads toward Brownian motion. It also creates a surprise: squared random moves do not disappear. There are more of them at exactly the rate that each squared move becomes smaller. Their accumulated trace is called quadratic variation.

This matters because the call payoff bends. A straight-line hedge reacts to the first-order stock move; the changing slope leaves a second-order curvature effect. Ordinary smooth-path calculus discards that term too early. Chapters 015–017 will be forced to repair the chain rule.

## Which probabilities survive the limit?

The tree's weight `p*` was not a forecast. It was chosen so stock-and-cash prices were consistent with replication. A continuous model needs the same distinction on an entire collection of paths.

We therefore need two probability views: one for statements about what may actually happen, and another that encodes prices after tradable risks have been accounted for. Chapters 018 and 019 will show how changing the measuring asset and reweighting paths turns discounted tradable prices into martingales.

Only then will a discounted expected payoff be earned. Introducing it here would repeat the exact error the book is designed to prevent: naming a mathematical operation before the market problem has forced it to exist.

## The convergence experiment we can perform now

Run the advanced laboratory with 25, 50, 100, 250, and 500 tree steps. Record each European call value. The sequence should approach a stable neighborhood, though odd and even step counts may approach from different sides because the strike falls differently on each discrete grid.

That experiment establishes a target. It does not yet explain why the limit has its final form. Numerical convergence says the tree family is approaching something; the next eight excavations identify what that something is made from.

> **Memory seal — the sealed arch:** the staircase becomes finer until it looks smooth from a distance. Up close, the door is locked by three missing keys: continuous uncertainty, calculus for rough paths, and pricing weights that are not forecasts.

## Excavation questions

1. Why must a typical random step shrink like `sqrt(dt)` rather than `dt` if uncertainty is to survive a continuous-time limit?
2. Which two objects are confused when someone treats an option payoff as though it already contained probabilities?
3. What does tree convergence establish, and what does it fail to validate?
4. Name the three missing mathematical keys that must be recovered before the Black–Scholes formula can be derived rather than announced.

## The first key

The tree's leaf labels have become too numerous to list. The next chapter builds the object that can name an unknown terminal price while keeping the contract payoff separate from the weights placed on possible states.

[Next: Random Variables](../012-random-variables/README.md) · [Run the convergence experiment](../../labs/advanced_lab.py)

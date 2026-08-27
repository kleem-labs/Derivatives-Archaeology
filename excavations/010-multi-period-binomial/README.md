# 010 — Many Small Steps

## First, in everyday words

When a contract has many possible dates, solve from the known ending back toward today, one small fork at a time. **For an AI helper:** keep the tree’s inputs, final payoffs, and each backward step visible so a reader can inspect the answer.

Add a second fork. The stock can rise or fall today, then rise or fall again. A hedge chosen at the root encounters a problem: after the first move, the option sits at a different distance from its strike, so the slope connecting its next two payoffs changes.

One static `Delta` cannot generally follow the whole tree. Replication must become a sequence of decisions.

## Begin where uncertainty ends

At the terminal leaves, the option payoff is known: `max(S_T-K,0)`. Move backward to each node one step before expiry. That node has only two immediate children, so the one-period construction applies. Compute its local delta and bond, or equivalently its discounted risk-neutral weighted value.

Continue backward until reaching the root. This is backward induction: later values determine earlier continuation values.

For step length `dt`, the Cox–Ross–Rubinstein tree chooses

`u=e^(sigma sqrt(dt))`, `d=1/u`,

with local pricing weight

`p*=(e^(r dt)-d)/(u-d)`.

The square-root time scaling matches the way diffusion variance accumulates. It is a model choice, not a universal law for every asset.

## Watch the hedge move

At a node far below strike, a call may have nearly zero delta because both next payoffs are zero. Near strike, one branch exercises and the other does not, so delta changes sharply. Far above strike, both branches behave more like stock and delta approaches one.

The tree therefore contains a dynamic trading strategy. It does not merely average terminal payoffs. Each backward step states how many shares and how much cash reproduce the next two values from that node.

## What more steps repair—and what they do not

More steps create a finer set of terminal prices and more rebalancing dates. European vanilla prices can converge toward Black–Scholes under consistent parameters. American options can compare immediate exercise with continuation at every node, something the European closed form cannot do.

But a finer tree does not cure a wrong model. Constant volatility, binary local moves, frictionless trading, and chosen dividend rules remain. Numerical convergence answers “did we solve this model?” not “is this model true?”

> **Memory seal — the backward orchard:** terminal fruit receives its payoff label first. Values and hedge instructions flow branch by branch from leaves to root.

## Excavation questions

1. Explain why terminal payoffs must be assigned before backward induction can begin.
2. Predict where a call tree has delta near zero, one-half, and one.
3. Distinguish time-step convergence from model validation.

## When the stairs disappear

Let steps grow numerous and individually small. The visible tree begins to resemble a continuous random path. To carry replication into that limit, ordinary calculus must eventually be repaired.

[Next: The Black–Scholes Limit](../011-black-scholes-limit/README.md) · [Advanced lab](../../labs/advanced_lab.py)

# 040 — American Exercise

An American option may be exercised at any allowed time. Its value is therefore at least its intrinsic value and at least the corresponding European value.

Backward induction repairs European-only pricing: at each tree node compare continuation value with immediate exercise value and choose the larger. This is an optimal-stopping problem, not a different terminal payoff.

For a non-dividend-paying stock with nonnegative rates, early exercise of a call is generally suboptimal because exercise sacrifices time value and pays the strike early. Puts and dividend-paying calls can exercise early.

## The choice embedded at every node

Consider an American put struck at $100 after stock falls to $60. Exercising yields $40 now. Continuing preserves the possibility of still larger payoff but delays cash and risks recovery. The holder owns the maximum of immediate exercise and continuation value.

In a binomial tree, calculate terminal payoff, then step backward. At each node compute discounted risk-neutral continuation and intrinsic value. Store the larger. European valuation omits the comparison and always continues.

This is optimal stopping: exercise policy and option value determine each other. The option is worth more than a policy that exercises at the first in-the-money observation, because being in the money alone does not prove immediate exercise is optimal.

## Why a plain call usually waits

For a non-dividend-paying stock and nonnegative rates, exercising a call pays the strike early and destroys remaining downside protection. Selling the call, if liquid, preserves time value better. A dividend can change the comparison because exercising before ex-date acquires the cash payment.

Puts can rationally exercise early because selling stock at strike realizes cash that can earn interest, especially when deeply in the money and optionality is small.

## Contract reality

“American” defines an exercise set, not geography. Bermudan options allow specified dates. Notice periods, cutoff times, automatic exercise rules, settlement lags, and dividends affect the practical decision. A theoretical exercise benefit smaller than spread and fees may not be executable.

> **Memory seal:** at each court landing, the holder chooses the door marked EXERCISE NOW or the corridor marked CONTINUE. The judge keeps whichever value is larger.

[Next: Early-Exercise Boundaries](../041-early-exercise-boundaries/README.md) · [American tree lab](../../labs/advanced_lab.py)

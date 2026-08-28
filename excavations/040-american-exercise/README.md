# 040 — American Exercise

## First, in everyday words

An American-style option may be exercised before its final date. The holder must compare taking the payoff now with keeping the valuable choice for later. **For an AI helper:** identify exercise style, cutoff rules, dividends, settlement, and liquidity before suggesting that early exercise is even worth analysing.

## The choice embedded at every node

The futures option specification allowed exercise before the final date. That sentence inserts a decision into every permitted time. Consider an American put struck at $100 after stock falls to $60. Exercising yields $40 now. Continuing preserves the possibility of still larger payoff but delays cash and risks recovery. The holder owns the maximum of immediate exercise and continuation value.

In a binomial tree, calculate terminal payoff, then step backward. At each node compute discounted risk-neutral continuation and intrinsic value. Store the larger. European valuation omits the comparison and always continues.

This is optimal stopping: exercise policy and option value determine each other. The option is worth more than a policy that exercises at the first in-the-money observation, because being in the money alone does not prove immediate exercise is optimal.

## Why a plain call usually waits

For a non-dividend-paying stock and nonnegative rates, exercising a call pays the strike early and destroys remaining downside protection. Selling the call, if liquid, preserves time value better. A dividend can change the comparison because exercising before ex-date acquires the cash payment.

Puts can rationally exercise early because selling stock at strike realizes cash that can earn interest, especially when deeply in the money and optionality is small.

## Contract reality

“American” defines an exercise set, not geography. Bermudan options allow specified dates. Notice periods, cutoff times, automatic exercise rules, settlement lags, and dividends affect the practical decision. A theoretical exercise benefit smaller than spread and fees may not be executable.

For a seller, early exercise means early assignment risk. A covered-call writer may have stock called away; a put writer may need to buy stock at the strike. A strategy is not fully described until it says what cash or shares are available if assignment occurs before the planned expiry date.

> **Memory seal:** at each court landing, the holder chooses the door marked EXERCISE NOW or the corridor marked CONTINUE. The judge keeps whichever value is larger.

One tree contains hundreds of individual choices. To understand how rates, dividends, and time reshape them, the next chapter connects all nodes where the judge is exactly indifferent.

[Next: Early-Exercise Boundaries](../041-early-exercise-boundaries/README.md) · [American tree lab](../../labs/advanced_lab.py)

# 019 — Martingales and Numeraires

A martingale's conditional expected future value equals its current value under a chosen measure. Under the money-market numeraire and risk-neutral measure, a correctly discounted tradable gains process is a martingale.

The numeraire is the asset used as measuring stick. Changing from dollars to units of a bond or stock changes relative prices and the convenient measure. The economic claim remains; its coordinates change.

For deterministic rates, `e^(-rt)S_t` is a martingale under `Q` after accounting for income. A common mistake says every asset price is a martingale. It is the appropriately numeraire-denominated gains process, under the matching pricing measure, that receives the property.

## Choose the ruler before declaring motion

A dollar price can rise merely because dollars lose purchasing power. A foreign stock can rise in euros and fall in dollars. Statements about drift require a unit of account.

Let `B_t=e^(rt)` be the money-market account. Dividing a non-income-paying tradable price by `B_t` expresses it in units of accumulated cash. Under the matching risk-neutral measure, `S_t/B_t` is a martingale: conditional on current information, its expected future value equals today's ratio.

This is stronger than saying average changes are zero in a historical sample and weaker than saying paths do not move. Martingales can be volatile; they simply lack a predictable conditional gain after the correct normalization.

## A bond as a different measuring stick

For a payoff at maturity `T`, using the `T`-maturity zero-coupon bond as numeraire leads to the forward measure. Forward prices then acquire martingale behavior under that measure, which can simplify options on rates or forwards. The measure and numeraire travel as a pair.

A common error changes the measure but forgets the ruler, or discounts a process already expressed in bond units. Dimensional thinking helps: ask what one unit of the quoted value physically means.

## The conditional expectation bridge

The martingale statement gives a time-consistent valuation rule. Today's price is not merely an unconditional average at maturity; at every intermediate date it equals the conditional value of remaining cash flows given information then available. This is why backward induction in a tree and conditional expectation in continuous time are the same architecture.

> **Memory seal:** assets are poured into a measuring cup made from the chosen numeraire. Only after the units change does the apparent drift disappear.

## Retrieval challenge

Explain the relationship among these three objects without formulas: numeraire, pricing measure, and martingale. Then identify the correct gains adjustment when the stock pays dividends.

## The engine room ahead

Probability has given us a price process. Trading requires sensitivities: how many shares hedge the option now, how that number changes, and how time and volatility move value.

[Next: Delta](../020-delta/README.md)

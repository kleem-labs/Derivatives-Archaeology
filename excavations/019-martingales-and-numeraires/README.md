# 019 — Martingales and Numeraires

## Choose the ruler before declaring motion

Chapter 018 reweighted paths until discounted tradable gains had no drift. “Discounted by what?” must now be answered. A dollar price can rise merely because dollars lose purchasing power. A foreign stock can rise in euros and fall in dollars. Statements about drift require a unit of account.

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

## Return to the sealed arch

Chapter 011 left three keys on the table. We can now name each one without borrowing from the future.

Brownian motion supplies continuous uncertainty whose increments scale with `sqrt(dt)`. Quadratic variation explains why squared noise survives. Itô's lemma applies that fact to a curved option value. Change of measure and the money-market numeraire supply pricing weights under which discounted tradable gains are martingales.

Let a non-dividend-paying stock satisfy `dS=mu Sdt+sigma SdW`, and let the option value be `V(S,t)`. Itô's lemma gives

`dV=(V_t+mu SV_S+.5sigma²S²V_SS)dt+sigma SV_SdW`.

Hold one option and short `V_S` shares. The two `dW` terms cancel because option and stock are driven by the same local shock. The remaining position is instantaneously riskless inside the model, so no-arbitrage requires it to earn rate `r`. Rearranging gives

`V_t+.5sigma²S²V_SS+rSV_S-rV=0`.

The stock's real-world drift `mu` disappears because the hedge removed the stock shock whose compensation would depend on it. Volatility remains because squared movement interacts with curvature.

## The terminal promise chooses one solution

The differential equation describes a family of claims. A European call supplies the final condition `V(S,T)=max(S-K,0)`. Solving backward gives

`C=S_0N(d_1)-Ke^(-rT)N(d_2)`,

where

`d_1=[ln(S_0/K)+(r+sigma²/2)T]/(sigma sqrt(T))`

and `d_2=d_1-sigma sqrt(T)`.

For spot $100, strike $105, rate 5%, volatility 20%, and one year, the call is about $8.0214. The corresponding put is about $7.9004; their difference is the $0.1209 required by put–call parity. The closed form, tree, and parity now meet because every operation connecting them has been excavated.

The formula is also the martingale statement in terminal form: price equals the risk-neutral expected payoff discounted in the money-market numeraire. Only now is that expectation legitimate: replication, the pricing measure, and the numeraire have supplied both its weights and its discount rule.

## The next question is no longer price alone

A model price of $8.0214 still does not tell a trader how the mark will change when spot moves. The hedge above contains `V_S`, but we have not yet learned how to read it numerically, how quickly it changes, or what error remains after a finite move. Those questions open the sensitivity engine.

[Next: Delta](../020-delta/README.md)

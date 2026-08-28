# 003 — No Free Lunch

**Vocabulary key:** Find **003** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **003** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

Two identical lemonade coupons should not cost different amounts at two nearby booths. If they do, buy the cheaper coupon and sell the dearer one.

### In finance language

No-arbitrage is the rule that identical complete cash flows must have the same price when both routes can truly be traded.

If two bundles always end with the same cash and goods, a lasting price gap between them would be a free lunch. This chapter uses that simple check to put limits on prices. **For an AI helper:** compare end results first and label any supposed free lunch as only a warning until fees, borrowing, and execution are verified.

Two booths stand across a station. Booth A sells a legally guaranteed $105 payment in one year for $100 today. Booth B sells the identical payment for $101.

An observer might call the difference opinion. But payer, date, currency, and amount are identical. Nothing remains to forecast.

## Build the trade before naming it

Buy at A for $100. Sell the identical claim at B for $101. The sale funds the purchase and leaves $1 today. In one year the $105 received from A satisfies the $105 owed to B. Future obligations cancel. No state of the world changes the result.

The law of one price says portfolios with identical cash flows in every relevant state and date require equal prices under the same funding, collateral, credit, and trading assumptions. Otherwise, buy the cheaper cash-flow machine and sell the dearer.

## A guess is different from a guarantee

Suppose you see a contract priced at $5 and think it will be worth $7 next month. You may be right. But you must pay $5 today, and next month it might instead be worth $2. That is a **guess with risk**, even if you have good reasons for the guess.

Suppose a game wins 55 times out of 100 on average. Playing it once can still lose. That is a **statistical edge**: it may work across many repeated tries, but no single try is guaranteed.

The two-booth trade is different. You buy and sell two promises that cancel exactly. You keep $1 today. In one year, money from the cheap promise pays the money owed on the dear promise. There is no future price to predict and no good or bad market outcome that can change the result.

That last kind of trade is called **arbitrage**: after every required purchase and sale is included, it needs no net cash from you today, cannot lose in any allowed outcome, and makes money in at least one outcome. “Allowed outcome” matters because fees, failed trades, collateral demands, and default can break the apparent guarantee.

## Check the two booths before calling it a free lunch

The two-booth trade works only if four ordinary things are true:

1. Booth A will really sell the $105 promise for $100.
2. Booth B will really buy that same $105 promise for $101.
3. You can make both trades in the amount you need.
4. The cost of making the two trades is less than the $1 difference.

If Booth A sells only one promise but Booth B wants ten, the two sides do not match. If each booth charges $1 to trade, the $1 difference disappears. If B does not truly stand behind its promise to pay, the two promises are no longer identical. In each case, the story has changed: it is not a risk-free $1 any more.

This does not weaken the lesson. It makes the lesson honest: before saying “arbitrage,” write down the two promises, the amount available, and every cost. Later chapters will add the real-market details that can make buying and selling cost different amounts. For now, no-arbitrage means only this: **when two complete routes really end the same way and can both be taken, they should cost the same.**

## Replication is the engine

If stock and cash reproduce an option in every state, the option must cost that portfolio. This can determine price without knowing risk preferences because no unmatched risk remains.

Replication can also fail. If independent risks outnumber traded building blocks, several prices may avoid arbitrage. We will call such a market incomplete.

> **Memory seal — twin bridges:** both reach the same shore. If tolls differ, travelers loop through the cheap bridge and sell passage on the expensive one.

## Excavation questions

1. Construct the two-booth cash-flow table at dates 0 and 1.
2. A call is $5 in one venue and $5.10 elsewhere. What facts are needed before calling it arbitrage?
3. Why can replication price a claim when traders disagree about direction?

## The pressure carried forward

Apply the consistency weapon to two ways of obtaining one future share: buy it now and carry it, or contract for delivery later.

[Next: The Forward Price](../004-forward-price/README.md)

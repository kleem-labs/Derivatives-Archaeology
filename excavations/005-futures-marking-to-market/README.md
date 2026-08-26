# 005 — Futures Are Re-settled

Mara and Arun's forward remains silent until March. An exchange does not tolerate that silence. If wheat moves sharply, a losing party could accumulate an obligation too large to honor. Futures markets interrupt the promise every day.

Suppose Arun is long one futures contract at $6.00. At the first close the settlement price is $6.20. His margin account receives the contract quantity times $0.20; the short account pays it. The contract is effectively reset at $6.20. Tomorrow's gain or loss begins there.

## Same endpoint, different river

A forward delivers its entire economic gain at maturity. A futures contract sends daily variation margin through the trader's cash account. If gains arrive early, they can earn interest. If losses arrive early, they must be funded.

Imagine prices rise early and interest rates rise with them. The long futures holder receives cash precisely when it can be reinvested at higher rates. A forward holder receives nothing until maturity. Reverse the correlation and the timing advantage changes.

This is why “forward price equals futures price” needs conditions, commonly deterministic rates or a negligible correlation effect. It is often a good approximation for short maturities, not an identity without assumptions.

## A hedge can be right and still fail

Mara shorts futures to protect the value of wheat she expects to harvest. A temporary rally produces margin losses even though the higher crop price offsets them economically. But the crop cannot be sold today; the margin call must be paid today. If she cannot fund it, the exchange closes the position before harvest.

Terminal payoff diagrams miss this liquidity path. A contract's safety depends on cash-flow timing, collateral rules, and the holder's ability to survive adverse moves—not only the final combined profit.

The exchange reduces counterparty credit risk through margin and clearing, but it does not eliminate market or liquidity risk. Initial margin is collateral, not the amount at risk and not the purchase price of the notional exposure.

> **Memory seal — the daily fountain:** every sunset, coins flow from the losing side to the winning side. No one is allowed to postpone the day's loss until harvest.

## Excavation questions

1. Build a three-day variation-margin ledger for settlements 100, 104, 101, and 108 on a multiplier of 50.
2. Explain how a profitable maturity hedge can suffer a fatal interim cash call.
3. Under what rate condition is the forward–futures timing difference least important?

## Arun rejects half of the hedge

Daily settlement makes the forward safer for the exchange, but it does not repair Arun's deeper complaint. If wheat falls to $4, his long futures position loses roughly what he saves in the cash market. He asked to remove the $9 disaster; the contract also removed the $4 opportunity.

He therefore changes the proposed sentence: “I may buy at $6 if market wheat is dearer, but I may walk away if it is cheaper.” Mara will accept only if paid upfront, because the new contract gives every favorable exercise decision to Arun and every corresponding obligation to her. The next chapter begins from that one-sided choice.

[Next: Options Create Asymmetry](../006-option-payoffs/README.md)

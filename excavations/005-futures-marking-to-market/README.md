# 005 — Futures Are Re-settled

A forward waits until maturity to exchange its gain or loss. A futures contract is marked to market: gains and losses move through margin accounts daily. The final economic exposure may look similar, but the timing of cash flows is different.

Imagine prices rise early. A long futures position receives cash early and can earn interest; a long forward receives nothing until maturity. If price changes and interest rates are correlated, the value of that timing need not cancel. Therefore “futures price equals forward price” requires conditions, commonly deterministic rates or effects small enough to ignore.

Daily settlement also creates liquidity risk. A hedge that is economically sound at maturity can fail earlier if it cannot meet a variation-margin call. Payoff diagrams alone hide this path.

The first arc has recovered contracts, discounting, replication, carry, and settlement timing. We can now study a promise with an asymmetric choice.

Next: [Options Create Asymmetry](../006-option-payoffs/README.md).


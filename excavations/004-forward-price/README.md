# 004 — The Forward Price

A stock costs $100 and can be financed for one year at 5%. What delivery price `K` makes a new forward worth zero?

Naively set `K` to an expected future stock price. But a second route guarantees delivery: borrow $100, buy the stock, and hold it. The loan grows to `100e^0.05 = $105.13`. If the forward delivery price were $110, buying spot and selling the forward would lock in $4.87 before costs. If it were $100, reverse cash-and-carry would point the other way under ideal shorting assumptions.

Equating the delivery routes gives:

`F_0(T) = S_0 e^(rT)`.

With a continuous asset yield `q`, ownership supplies income while the forward does not, so `F_0(T)=S_0e^((r-q)T)`.

This is a carry relation, not a claim that the future spot must equal the forward price. Storage, dividends, convenience yield, financing, and constraints change the replication.

Next: [Futures Are Re-settled](../005-futures-marking-to-market/README.md). Experiment with `forward_price` in [the lab](../../labs/derivatives_lab.py).


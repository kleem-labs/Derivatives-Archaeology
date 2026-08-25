# 002 — Time Has a Price

Place two envelopes on the table. One contains $100 now. The other contains a legally certain promise of $100 one year from now. They show the same number, but they are not the same economic object.

If money earns 5%, the first can be invested. Under continuous compounding it becomes `100e^0.05`, about $105.13. Choosing the later envelope sacrifices that growth.

## The date cannot be erased

Suppose a contract pays certain $105 in one year. Guessing a present value of $105 ignores time. Subtracting 5% of $105 gives $99.75, but applies the rate at the wrong end. We need the amount which, grown forward, lands exactly on $105.

Let present amount be `X_0`, future amount `X_T`, continuous rate `r`, and years `T`:

`X_T=X_0e^(rT)`.

Undo growth by division:

`X_0=X_T/e^(rT)=X_Te^(-rT)`.

For $105, 5%, one year, present value is `105e^-0.05=$99.8791`. Growing it forward recovers $105. That reversal checks the meaning.

## Rates are not floating labels

A rate is incomplete without currency, maturity, compounding, credit quality, collateral convention, and day-count basis. Five percent annually compounded differs from five percent continuously compounded. A risky corporate promise should not be discounted as government cash. Later we will use curves rather than one rate.

The simple formula is a clean room, not the entire rates building. Its purpose is to compare dates.

## Do not discount an expectation too early

It is tempting to calculate an expected payoff and discount it. That is valid only after choosing appropriate probability weights and discounting rules. Real-world expected payoff discounted at a risk-free rate generally ignores risk compensation. Replication will later produce risk-neutral weights consistent with traded prices.

If an option strike is $105 payable in a year, $99.8791 today guarantees it at 5%. This observation will let us compare call-plus-cash with put-plus-stock. Without discounting, parity compares the wrong dates.

> **Memory seal — the clock bank:** a dollar grows while the clock turns. To walk backward, divide away exactly that growth.

## Excavation questions

1. Present-value $1,000 in two years at 4% continuous compounding and reverse the calculation.
2. Why can two quoted 5% rates yield different discount factors?
3. List assumptions hidden in “risk-free rate.”

## The pressure carried forward

If two portfolios create identical future cash flows but require different present cash, the difference cannot survive.

[Next: No Free Lunch](../003-no-arbitrage/README.md) · [Lab](../../labs/derivatives_lab.py)


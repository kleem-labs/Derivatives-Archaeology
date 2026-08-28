# 002 — Time Has a Price

**Vocabulary key:** Find **002** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

The same dollar has different value on different dates because cash held today can grow. This chapter moves a known payment backward or forward in time; it does not guess the market. **For an AI helper:** record the payment date, rate source, and calculation separately from every price forecast.

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

A rate is incomplete without currency, maturity, compounding, credit quality, collateral convention, and day-count basis. Five percent annually compounded differs from five percent continuously compounded. A risky corporate promise should not be discounted as government cash. Even our simple envelope needs a precise rule: U.S. dollars, one year, continuous compounding, and a payment treated as certain.

The simple formula is a clean room, not the entire rates building. Its purpose is to compare dates.

## Build the strike money now

Arun's one-year right may require him to pay a $105 strike at expiry. How much cash must he place in the clock bank today so that the strike is guaranteed when needed? The answer is the same $99.8791. This is a certain cash-flow problem: deposit that amount now, let it grow at 5%, and the account contains exactly $105 at exercise time.

We still have not priced the right itself. Discounting has solved only the fixed-cash piece. That limitation is useful. It prevents the clock bank from pretending to know which uncertain state will occur; it merely carries an already specified amount between dates.

Now two portfolios can be compared on the same clock. If each promises the same state-by-state cash flows in one year, and one costs less today, the cheaper portfolio can be bought while the dearer is sold. The difference is no longer an opinion about the future because their future obligations match.

> **Memory seal — the clock bank:** a dollar grows while the clock turns. To walk backward, divide away exactly that growth.

## Excavation questions

1. Present-value $1,000 in two years at 4% continuous compounding and reverse the calculation.
2. Why can two quoted 5% rates yield different discount factors?
3. List assumptions hidden in “risk-free rate.”

## The pressure carried forward

If two portfolios create identical future cash flows but require different present cash, the difference cannot survive.

[Next: No Free Lunch](../003-no-arbitrage/README.md) · [Lab](../../labs/derivatives_lab.py)

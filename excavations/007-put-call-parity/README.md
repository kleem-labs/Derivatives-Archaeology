# 007 — Put–Call Parity

**Vocabulary key:** Find **007** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

## First, in everyday words

### A small picture

Two different backpacks can carry exactly the same things to school. If they always arrive with the same things, they should cost the same.

### In finance language

Put–call parity is an equal-payoff identity linking a call plus cash with a put plus stock, for matching strike and expiry.

A call plus cash can sometimes finish exactly like a put plus stock. This chapter is a mirror test: rearrange familiar pieces until their ending is the same. **For an AI helper:** use parity as a consistency check and report the contract details, timing, and costs needed for the check.

On the exchange floor, two traders claim to have built different one-year portfolios. Nadia owns one call struck at $105 plus enough cash today to grow into $105. Tomas owns one put with the same strike and one share of stock.

Their screens show different instruments. At expiry, the distinction disappears.

## Split the future at the strike

If `S_T>105`, Nadia exercises: her call plus $105 becomes one share worth `S_T`. Tomas keeps his share and lets the put expire. Both have `S_T`.

If `S_T<105`, Nadia's call expires and she keeps $105. Tomas exercises the put, selling his share for $105. Both have $105.

At equality both have $105. In every state, each portfolio ends with `max(S_T,K)`.

No-arbitrage therefore equates current costs:

`C + Ke^(-rT) = P + S_0`,

so

`C-P=S_0-Ke^(-rT)`.

With spot $100, strike $105, rate 5%, and one year, the right side is `100-105e^-0.05=$0.1209`. If an executable call price is $8, the matching put is $7.8791 under the assumptions.

## Turn a violation into cash flows

Suppose instead the put asks $9 while the call can be bought at $8 and other prices are executable without costs. The right portfolio is too dear relative to the left. Buy call plus discounted strike; short put plus stock. Terminal cash flows cancel in both regions. The initial difference is locked in.

In actual markets use bids for what you sell and asks for what you buy. Dividends, exercise style, stock borrow, funding, settlement, and fees alter either the equation or whether the trade exists. American options satisfy bounds rather than this simple European equality because exercise timing differs.

## What parity can and cannot tell us

Parity can synthesize a call from stock, put, and borrowing, or a put from call, cash, and short stock. It constrains relative prices without knowing volatility. It cannot determine both `C` and `P`; one free option-price dimension remains.

To pin down that dimension we need a smaller world where stock and cash span every possible outcome.

> **Memory seal — the mirror wardrobe:** call plus strike-cash and put plus stock wear different clothes, but the mirror reveals identical terminal bodies.

## Excavation questions

1. Fill the two-portfolio payoff table at terminal prices $70, $105, and $150.
2. Rearrange parity to synthesize a call. Interpret every long and short position.
3. Explain why mid-price parity is insufficient evidence of executable arbitrage.

[Next: One Period, Two Futures](../008-one-period-binomial/README.md)

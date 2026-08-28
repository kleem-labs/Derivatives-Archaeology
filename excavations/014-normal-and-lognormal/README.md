# 014 — Normal and Lognormal Models

**Vocabulary key:** Find **014** in the [Concept Atlas](../../CONCEPT_ATLAS.md) before continuing. It names the ideas already earned, the new words defined here, and the decision this chapter makes clearer.

**Table walkthrough:** Read row **014** in [Table-First Walkthroughs](../../TABLE_FIRST_WALKTHROUGHS.md) before trusting a summary sentence or formula.

## First, in everyday words

### A small picture

A price cannot usually fall below zero, like a toy’s sticker cannot say minus five dollars. Pick a shape for possible prices that respects that fact.

### In finance language

Normal and lognormal are probability models. A lognormal price stays positive because its logarithm, rather than the price itself, is modelled as normal.

Models choose a shape for possible prices. A normal shape can wander below zero; a lognormal shape stays positive but still misses many real market surprises. **For an AI helper:** name the chosen shape, explain why it was used, and show the real-world feature it leaves out.

## Why returns enter before prices

If a $10 stock and a $1,000 stock each gain $1, the economic moves are not comparable. Relative change repairs the units. Multiplicative returns also compound: a 10% rise followed by a 10% fall gives `1.1×.9=.99`, a 1% loss. Adding raw percentages would incorrectly return to zero.

Log returns turn multiplication across time into addition: `ln(S_T/S_0)=sum ln(S_i/S_{i-1})`. This is why a normal model for accumulated log returns is mathematically convenient.

If `ln(S_T/S_0)` is normal, exponentiating it keeps `S_T` positive. Write a standard normal draw as `Z`. A model with annual drift `mu`, volatility `sigma`, and horizon `T` takes the form

`S_T=S_0exp((mu-sigma²/2)T+sigma sqrt(T)Z)`.

Take `S_0=100`, `mu=.06`, `sigma=.20`, and `T=1`. At `Z=0`, the model's median terminal price is `100exp(.06-.02)≈104.08`. Its mean is `100e^.06≈106.18`. Mean exceeds median because exponentiation stretches the upper tail. The `-sigma²/2` correction ensures the desired mean growth; it does not represent a fee or risk premium.

## A model earns usefulness and creates danger

The lognormal model preserves positive prices and produces closed forms. But it assigns extremely small weight to sudden crashes and treats volatility as stable. In equity markets, implied volatilities across strikes reveal that traders do not price every state as one lognormal distribution would.

Normal models can still be appropriate for quantities allowed to cross zero—certain rate changes, spreads, or commodity prices under some conventions. The question is not which named distribution is universally correct. It is which support, tails, dependence, and dynamics the contract requires.

## Reader experiment

Compare terminal prices at `Z=-2,0,2`. Then double `sigma` while preserving `mu`. Watch the median fall because of the variance correction even while the mean stays fixed. The distribution has widened asymmetrically.

> **Memory seal:** the bell curve cannot be laid flat on the price floor without leaking below zero, so it is wrapped around the logarithmic tower.

The formula describes one terminal draw. To make the price move through time, we need a continuous process whose increments accumulate into exactly this normal log return.

[Next: Brownian Motion](../015-brownian-motion/README.md)

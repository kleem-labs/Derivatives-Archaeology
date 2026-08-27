# Volume II — We Build the Asymmetry

Arun has found the shape he wants: help when wheat is expensive, freedom when it is cheap. The rest of this volume asks one question again and again: can that bent shape be copied from simpler pieces?

## 006 — The bent payoff

A call is the right to buy at a fixed price. A put is the right to sell at a fixed price. The buyer has a limited loss—the price paid for the right. The seller receives that price and takes the other side of the shape.

Why does a right cost money even when it would be useless today? Because time remains. A calm price today can still move far enough tomorrow to make the right valuable.

Picture a call as a floor that stays at zero and then rises. Picture a put as a roof that stays at zero and then rises when price falls. Those two bends are the raw material of options.

[Open the workshop for this chapter](../excavations/006-option-payoffs/README.md)

## 007 — A mirror trick with calls and puts

Take a call and set aside enough cash to pay its strike later. Put them together. If the share ends high, use the call and own the share. If it ends low, keep the cash.

Now take a put and one share. If the share ends high, keep it. If it ends low, use the put and receive the strike cash.

Both bundles end in exactly the same place. One holds the higher of the share price and the strike. Since they always finish alike, they should cost alike today.

This is put–call parity. Its deeper lesson is more important than its name: options are not isolated magic objects. They can be rearranged into one another with stock and cash.

[Open the workshop for this chapter](../excavations/007-put-call-parity/README.md)

## 008 — Copy the option in a tiny world

Pretend a $100 share has only two possible prices next year: $120 or $90. A call struck at $105 pays $15 in the first world and $0 in the second.

Hold half a share. It is worth $60 in the high world and $45 in the low one. Borrow $45 for next year. The bundle is then worth $15 or $0—exactly the call.

So the call must cost what the half-share bundle costs today. We did not guess how likely either world is. We made a copy that works in both.

This small example contains the whole spirit of options pricing: copy the promise first. Price the copy second.

[Open the workshop for this chapter](../excavations/008-one-period-binomial/README.md)

## 009 — The fair weights

The same copied call can be priced by taking a weighted average of its two future payoffs and bringing that average back to today.

The weights are chosen in a special way: they make the share grow, on average, like money in the bank. They are not a prediction of what people think will happen. They are a bookkeeping device that gives the same answer as the half-share and borrowed cash.

That is why they are called risk-neutral weights. The phrase sounds philosophical, but the job is simple: choose weights that make the copied trade and the weighted-average trade agree.

[Open the workshop for this chapter](../excavations/009-risk-neutral-probability/README.md)

## 010 — Copy it again tomorrow

One step is easy. Real time has many steps. After the share moves, the option has changed shape. The number of shares needed to copy it must change too.

Start at the end of a tree, where the option payoff is known. Move backward one fork at a time. At each fork, make a small stock-and-cash copy of what comes next. The answer at the final leaves slowly travels back to today.

This is backward induction. It is not a trick for trees. It is the habit of solving a promise from the moment it becomes certain back toward the moment it is signed.

[Open the workshop for this chapter](../excavations/010-multi-period-binomial/README.md)

## 011 — When the tree becomes too fine to see

Make the tree finer and finer. The stairway of possible share prices starts to look like a smooth path. The option price settles near a stable number.

But we must not jump straight to a famous formula. Three things are still missing: a way to speak about countless possible future prices, a way to do calculus on a rough random path, and a way to use fair weights across all those paths.

The next volume builds those tools slowly. When we return, Black–Scholes will not be a spell. It will be the short name for a copy we can finally understand.

[Open the workshop for this chapter](../excavations/011-black-scholes-limit/README.md)

## What to carry with you

An option is valuable because its owner may refuse a bad trade. Stock and cash can sometimes copy that choice. When a copy exists, the option price is not a vote or a hunch. It is the cost of the copy.

[Next volume: We Enter Uncertainty](VOLUME_III_WE_ENTER_UNCERTAINTY.md)

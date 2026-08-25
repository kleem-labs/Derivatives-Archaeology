# Laboratory

Run the guided experiment:

```bash
python3 labs/derivatives_lab.py
```

It displays discounting, cash-and-carry forward pricing, put–call parity, a one-period replicating portfolio, and Black–Scholes prices. Change the named inputs in `main()` and predict the direction of every output before running it again.

Then verify the invariants:

```bash
python3 -m unittest discover -s tests -v
```

Suggested breaks:

1. Quote a forward above fair value and calculate the locked-in cash-and-carry profit.
2. Raise only the call price and watch put–call parity fail.
3. Set the binomial growth factor outside `(d, u)` and explain why the resulting “probability” is invalid.
4. Shrink volatility toward zero and identify what remains in the option price.


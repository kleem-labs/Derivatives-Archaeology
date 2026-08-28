# Table-First Walkthroughs — show the moves before the summary

Use the row with the same number as the chapter. Read left to right: **what is given → what you do or calculate → what becomes true → why it matters**. Chapter 004 contains the full dated cash-flow tables for both high and low forward quotes; this companion gives every other chapter its smallest visible working table.

## I — Promises and prices

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 000 | Wheat price later is unknown | Write buyer’s and seller’s result at $4, $6, $9 | One gains exactly what the other loses | A derivative moves risk; it does not create wheat. |
| 001 | Right to buy wheat at $6 | At $4: walk away; at $9: use right, save $3 | `max(S_T-6,0)` | Draw payoff before asking for price. |
| 002 | $105 certain in one year; 5% rate | Find cash that grows to $105: `105/e^.05` | $99.88 today | Known money needs a date. |
| 003 | Same $105 promise costs $100 and $101 | Buy $100 promise; sell $101 promise | $1 now; future payments cancel | Equal complete routes should cost the same. |
| 004 | Spot $100; one-year financing cost $5.13 | Compare buy-now-and-carry with future delivery | Fair delivery price $105.13 | See Chapter 004’s full cash tables before calling a gap arbitrage. |
| 005 | Futures price moves from 6.00 to 6.20 | Multiply 0.20 by contract quantity; add to account today | Daily gain/loss is paid now | A good final hedge can still need cash on the way. |

## II — Rights, obligations, and copies

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 006 | Strike `K`; premium `P`; final price `S_T` | Write buyer and seller payoff at below/at/above `K` | Right-holder and obligation-holder have opposite payoffs | “Option” is incomplete without side and premium. |
| 007 | Call + strike cash; put + stock | Test both bundles above and below strike | Same final stock-or-cash result | Parity checks a price against a mirror bundle. |
| 008 | Stock 100 → 120 or 90; call pays 15 or 0 | Hold 0.5 stock; borrow 45 at final date | Bundle pays 15 or 0 | A copy can price without a forecast. |
| 009 | Up/down factors; bank growth | Choose weight making weighted stock growth equal bank growth | Pricing weight `p*` | This weight prices a copy; it is not a belief. |
| 010 | Many up/down forks | Start at known final payoff; solve one node back at a time | Today’s tree value | Work backward when the future becomes certain first. |
| 011 | Finer and finer tree | Compare 25, 50, 100, 500 steps | Values approach a stable neighborhood | Numerical stability is not yet a proof of model truth. |

## III — The language of uncertainty

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 012 | States: drought, normal, bumper crop | Attach one price number to each state | A random variable | Separate the label from the chance weight. |
| 013 | Payoffs 50 and 150 with equal weights | Average: 100; square distances: 2500 each | Mean 100; variance 2500 | Same average can hide very different wobble. |
| 014 | Price 100; two 10% moves | Multiply `1.1 × .9` | 99, not 100 | Returns compound; price models need a shape. |
| 015 | One year split into 100 steps | Give each random step size `sqrt(.01)=.1` | Total wobble stays meaningful | Random movement grows with square-root time in this model. |
| 016 | Many tiny random moves | Square each move and add them | Nonzero total trace | Curvature survives random roughness. |
| 017 | Value depends on price and time | Keep time, first-price, and squared-price terms | Extra curvature term | Ordinary chain rule misses part of diffusion change. |
| 018 | Same possible paths | Keep paths; change their weights for pricing | Two labelled probability views | Belief and pricing are different jobs. |
| 019 | Values measured in bank-account units | Divide by measuring asset; apply pricing rule | Drift-free discounted value | The measuring ruler matters. |

## IV — What an option position feels

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 020 | Option delta .54; one 100-share contract | `.54 × 100` | About 54 stock-share delta | Convert screen Greek into position units. |
| 021 | Delta changes from .54 to .64 after $1 move | Change in delta divided by price move | Gamma .10 per dollar | Today’s hedge ratio will move. |
| 022 | Same price and model inputs; one day passes | Reprice with one less day | Theta change | Time is a condition, not free seller income. |
| 023 | Change only movement input or rate input | Reprice before and after each one-dial change | Vega or rho effect | Direction is not the only exposure. |
| 024 | Delta hedge today; price moves later | Compare required new delta with old hedge | Hedge error and rebalance trade | Continuous perfection becomes real trading work. |
| 025 | Historical prices over named days | Calculate each return; square and add | Realized movement measure | Say what happened, not what must happen. |
| 026 | Market option quote and stated model | Solve backward for movement input | Implied volatility | Translate a quote, do not manufacture a forecast. |
| 027 | Same expiry, several strikes | Solve implied volatility at each strike | Smile row | One movement number may hide differences. |
| 028 | Current smile data | Fit simple model, then richer model | More fit; more assumptions | Better fit is not automatic truth. |
| 029 | Price can jump from 100 to 65 | Compare hedge before jump with value after jump | Residual jump loss | A model may give a range, not one forced price. |

## V — Carry, cash, and futures

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 030 | Spot, financing, storage, income | Add costs; subtract ownership benefits | Carry-adjusted forward | Every physical burden/benefit belongs in the ledger. |
| 031 | Share pays dividend before expiry | Put dividend cash on stock route only | Lower net carry | Forward holder does not automatically receive the dividend. |
| 032 | Warehouse stock is scarce | Compare physical availability with later delivery | Convenience benefit | Inventory can be useful beyond its sale price. |
| 033 | Local spot 5.80; futures 6.00 | Calculate `spot − futures` now and later | Basis change | Hedge leaves the seam between two related prices. |
| 034 | Notional 100,000; margin 8,000; adverse move 3% | Loss 3,000; divide by posted margin | 37.5% loss on margin | Small deposit does not mean small exposure. |
| 035 | Exposure 375,000 lb; contract 37,500 lb | Divide exposure by contract size | Ten-contract quantity match | Hedge the real quantity and direction. |
| 036 | Cash and futures return history | Compute covariance / futures variance | Minimum-variance ratio | Imperfect hedge needs data, not a slogan. |
| 037 | Six-month zero; one-year coupon bond | Solve first discount factor, then second | Date-by-date curve | Earlier cash flows unlock later ones. |
| 038 | Two discount factors | Divide them to price future rate interval | Forward rate | Every cash flow needs its own date. |
| 039 | Option may exercise into future | Table option payoff first; futures margin path second | Two-stage risk | Premium-only view is incomplete. |

## VI — Contract choices, numerical answers, and market reality

| # | Given | Make visible | Result | Why it matters |
|---:|---|---|---|---|
| 040 | American put; exercise-now value; wait value | Calculate both at a node | Keep the larger | Exercise is a choice, not an automatic reaction. |
| 041 | Many exercise/continue nodes | Mark where values are equal | Moving boundary | Thousands of choices become one map. |
| 042 | Two paths ending at same price | Mark whether barrier was touched | Different contract outcome | The journey can matter as much as the finish. |
| 043 | Many simulated paths | Pay each path; discount; average; show error | Estimate plus uncertainty band | Simulation has numerical noise. |
| 044 | Price-time grid | Fill final payoff row; work backward from neighbors | Grid estimate | Check grid size and boundaries. |
| 045 | Rebalance often or rarely | Put trading cost beside hedge error | Practical trade-off | A perfect paper hedge can be costly. |
| 046 | Bid 7.80; ask 8.20 | Buyer starts at 8.20; seller starts at 7.80 | 0.40 round-trip spread before other costs | Midpoint is not automatically tradable. |
| 047 | Several option positions | Align multipliers; add Greeks; shock all inputs together | Portfolio scenario | Local offsets can fail together. |
| 048 | Modelled one-day losses | Sort losses; locate 99% line; average worse tail | VaR and Expected Shortfall | One threshold is not the whole disaster. |
| 049 | Model, quote, contract, test cases | Check bounds, units, behavior, alternatives | Use / revise / stop decision | A precise output must survive a trial. |

## The rule for every future revision

If a paragraph says “do the reverse,” “therefore,” “it follows,” or “this changes the value,” add a table before it. The table must show the objects, dates when relevant, action or calculation, and the result that the prose is about to interpret.

# Strategy Field Guide — buy, sell, hedge, or wait?

This guide is the destination of the archaeology. The mathematics in the excavations exists so that you can read a contract and answer a practical question:

> What am I paying for, what obligation am I accepting, what has to happen for this position to help, and what is the worst honest outcome?

It is educational, not a recommendation to make a trade. A strategy can fit one person’s actual exposure and be a poor choice for another. Before buying or selling any listed option, read the current [OCC Options Disclosure Document](https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document) and the actual broker and exchange terms.

## The rule that prevents most confusion

**Buying an option buys a right. Selling an option sells that right to someone else and accepts an obligation.**

Neither is “better.” They solve opposite problems.

| If your real problem is… | The position is usually trying to… | The cost or obligation to inspect first |
|---|---|---|
| A large move could hurt you and you want a known maximum loss | buy a right or use a defined-risk spread | upfront premium and time passing |
| You own stock and would genuinely sell it at a stated price | sell a covered call | upside above the strike is given away; assignment can occur |
| You would genuinely buy stock at a lower stated price and can fund it | sell a cash-secured put | stock can be assigned after a large fall; cash must be available |
| You want a bounded directional view but dislike an open-ended short option | use a vertical spread | the long leg limits the short leg, but also caps payoff |
| You own stock and want a floor for a period | buy a protective put or form a collar | protection costs premium or gives away some upside |
| You need more time for a thesis | consider a longer-dated option, including a LEAPS® contract when available | more premium is at risk; inputs and liquidity remain uncertain |
| You cannot state the exposure, contract terms, or loss path | wait and study | an unclear position is not made safe by a strategy name |

FINRA explains that a buyer can lose the full premium while some writers face much higher risk, including theoretically unlimited loss for an uncovered call. [See FINRA’s options overview.](https://www.finra.org/investors/investing/investment-products/options) “Premium income” is therefore payment for an obligation, not free yield.

## The universal scorecard

Use one scorecard for every strategy. If any row is blank, the right answer is `STOP — incomplete record`.

| Question | Write the answer, not a slogan |
|---|---|
| What do I already own or owe? | Stock, business inventory, future purchase, cash, or nothing. |
| What is the exact contract? | Underlying, strike, expiration, style, multiplier, settlement, bid, ask, and timestamp. |
| Am I the right-holder or obligation-holder? | Long call, short call, long put, short put, future, or multi-leg position. |
| What cash leaves today? | Premium paid, margin posted, spread, commissions, and financing if relevant. |
| What cash can be demanded before expiry? | Margin, assignment funding, delivery, or exercise cash. |
| What is the result at three or five prices at expiry? | A dollar table, multiplied by the contract multiplier. |
| What is my maximum gain? | Say “unlimited,” “capped,” or a calculated amount. |
| What is my maximum loss? | Say “unlimited,” “large but bounded by stock/cash,” or a calculated amount. |
| What must happen for the position to help? | Direction, size of move, time, and volatility conditions. |
| What can make the plan fail before expiry? | Time decay, assignment, margin, spread, jump, data error, or a thesis that arrives late. |

For a one-share illustration, let `S_T` be the final stock price, `K` the strike, and `P` the premium per share. Multiply every final answer by the contract multiplier—often 100 shares for standard U.S. equity options, but verify the specific contract.

## 1. Buy a call — pay for upside with a clock attached

**Position:** pay `P` for the right to buy at `K`.

`final profit = max(S_T - K, 0) - P`

| At expiry | Result |
|---|---|
| `S_T <= K` | lose `P` |
| `S_T = K + P` | break even before costs |
| `S_T > K + P` | profit grows as stock rises |

- Maximum loss: `P`.
- Maximum gain: no fixed upper cap.
- It helps when: the stock rises enough, soon enough, to beat the premium and costs; or the contract’s value rises before expiry for another reason such as a volatility change.
- It disappoints when: the stock rises too slowly, stays flat, falls, implied volatility falls, or the bid–ask spread consumes the expected edge.

A long call is not simply “bullish.” It is bullish **with a deadline**. A person may be right about a company over two years and still lose on a one-month call if the rise arrives late.

## 2. Buy a put — pay for a floor or a downside view

**Position:** pay `P` for the right to sell at `K`.

`final profit = max(K - S_T, 0) - P`

- Maximum loss: `P`.
- Maximum gain: roughly `K - P` per share if the stock goes to zero.
- Break-even at expiry: `K - P`.
- It helps when: a stock falls enough before expiration, or when the put is insurance for stock already owned.
- It disappoints when: the decline does not arrive in time, is too small, or the protection is more expensive than the exposure warrants.

For a stockholder, a put is closer to insurance than a prediction. The question is not “will it make money?” but “what loss do I refuse to carry, and what is the known cost of that floor?”

## 3. Sell a covered call — exchange some upside for premium

**Position:** own one share and sell one call at strike `K` for premium `P`.

`final profit relative to today’s stock price S_0 = min(S_T, K) - S_0 + P`

- Maximum gain: `K - S_0 + P`.
- Downside: stock can still fall; the premium protects only the first `P` of decline.
- Break-even at expiry: `S_0 - P`.
- It helps when: you already own the stock, would truly sell it at `K`, and are willing to trade away gains above `K` for the premium.
- It disappoints when: the stock jumps far above `K`, falls sharply, or you did not actually want assignment.

Why selling is **not** automatically better: the seller receives a small, known premium but may give up a very large stock gain. The premium does not turn a falling stock into a safe position. The Options Industry Council’s LEAPS® strategy material makes the same trade-off explicit for covered calls: premium gives limited downside protection and caps upside. [See the educational example.](https://prd-web.optionseducation.org/optionsoverview/leaps-strategies)

## 4. Sell a cash-secured put — accept a possible stock purchase for premium

**Position:** set aside `K` cash and sell one put for premium `P`.

`final profit = P - max(K - S_T, 0)`

- Maximum gain: `P`.
- Worst expiry outcome: receive stock at `K` when it is worth much less; if stock goes to zero, loss is about `K - P` per share.
- Break-even: `K - P`.
- It helps when: you would be content to own the stock at an effective cost near `K - P` and can keep the cash available.
- It disappoints when: you wanted premium but not the stock, the stock collapses, or the account lacks funds when assigned.

This is not a “low-risk income trade.” It is a conditional promise to buy stock. Calling it cash-secured is useful only if the cash truly remains reserved and the reader has accepted the stock outcome.

## 5. Vertical spreads — use one option to limit another

Vertical spreads use two options with the same expiry but different strikes. They are often a cleaner first strategy than an uncovered short option because the long option sets a known boundary.

### Bull call spread

Buy a lower-strike call `K_1`; sell a higher-strike call `K_2`; pay net debit `D`, with `K_1 < K_2`.

`final profit = min(max(S_T - K_1, 0), K_2 - K_1) - D`

- Maximum loss: `D`.
- Maximum gain: `(K_2 - K_1) - D`.
- Break-even: `K_1 + D`.
- Logic: pay less than a plain call by agreeing to give away gains above `K_2`.

### Bear put spread

Buy a higher-strike put `K_2`; sell a lower-strike put `K_1`; pay net debit `D`, with `K_1 < K_2`.

- Maximum loss: `D`.
- Maximum gain: `(K_2 - K_1) - D`.
- Break-even: `K_2 - D`.
- Logic: pay less for downside exposure by capping the payoff after a large decline.

### Credit spread

Selling one option and buying a farther-out option can produce a credit `C`. The long leg is the seat belt.

- Maximum gain: `C`.
- Maximum loss: width between strikes minus `C`, times multiplier.
- Logic: accept a bounded adverse outcome in exchange for premium.

An agent must calculate the **whole position**. “Short put” is incomplete if there is a lower-strike long put limiting it.

## 6. Protective put and collar — make a stock position less frightening

### Protective put

Own stock and buy a put with strike `K` for `P`.

`final profit relative to S_0 = max(S_T, K) - S_0 - P`

You keep upside above the stock purchase price but place a floor near `K`, reduced by the premium. The known cost is the put premium.

### Collar

Own stock, buy a put at `K_put`, and sell a call at `K_call`.

The put creates a floor; the call creates a ceiling. The call’s premium can reduce or offset the put’s cost, but it also sells away gains above `K_call`.

The logic is transparent: a collar is not a free hedge. It trades some upside for a cheaper downside floor.

## 7. Straddle and strangle — buy or sell movement, not direction

### Long straddle

Buy a call and a put at the same strike `K`, paying total premium `P_total`.

`final profit = abs(S_T - K) - P_total`

It helps only when the final move is large enough in either direction. It loses when the stock stays near `K` and time passes.

### Short straddle

Sell both. You receive `P_total`, but the final loss grows as the price travels far away from `K`. The upside risk is not capped unless other positions cap it.

The buyer pays for a large move; the seller accepts the risk that a large move arrives. A high premium may mean the market already expects turbulence. “Selling expensive volatility” is not a complete thesis unless you can explain why the realised move, jump risk, hedge costs, and assignment path should be manageable.

## 8. Calendar and diagonal spreads — time is the thing being traded

Buy a longer-dated option and sell a shorter-dated option. If the strikes match, it is a calendar; if they differ, it is a diagonal.

The short option often loses time value faster, but the position is not simply “collect theta.” The longer option also has time value, implied volatility can change differently across expiries, and assignment can create stock obligations. OIC warns that using a long-term call against a short call may not be treated as covered by a broker and assignment mechanics matter. [Read its LEAPS®/assignment explanation.](https://www.optionseducation.org/referencelibrary/faq/leaps-and-expiration-cycles)

**Agent rule:** every leg needs its own strike, expiry, multiplier, bid/ask, exercise style, and assignment plan. Never summarize a diagonal as “covered” without broker-specific confirmation.

## 9. LEAPS® — more time, not a free advantage

LEAPS® are exchange-listed long-term options. OIC currently describes them as expiring up to two years and eight months in the future; availability varies by underlying. They can provide more time for a thesis or a longer hedge, but they remain options with finite lives. [See how LEAPS® work.](https://www.optionseducation.org/optionsoverview/how-leaps-work)

### Long LEAPS call as a stock alternative

The buyer pays a premium for upside exposure with limited loss equal to the premium. Compared with buying stock, the cash committed can be lower, but the entire option can expire worthless and the position must overcome its strike plus premium by expiry.

`expiry profit = max(S_T - K, 0) - P`

The key difference from stock is the clock. A stock can be held indefinitely; a LEAPS® contract cannot. Longer time may soften near-term time decay, but it makes volatility, rate, dividend, and liquidity assumptions matter for longer. OIC notes that long-term option pricing is harder precisely because those inputs must be considered farther into the future. [See LEAPS® pricing.](https://prd-web.optionseducation.org/optionsoverview/leaps-pricing)

### LEAPS put as longer insurance

A long-dated put can protect a stock position for longer, at a known premium cost. The question is whether the protection period, strike, and cost match the actual exposure—not whether a long put is “bearish.”

### Selling LEAPS®

Selling a long-dated call or put means holding an obligation for much longer. Premium is larger because time and uncertainty are larger. It does not make the position safer. An uncovered long-dated call can still carry unlimited risk; a short long-dated put can still create a large stock-like downside. [OIC’s overview](https://www.optionseducation.org/optionsoverview/leaps-overview) states these risks plainly.

## 10. A strategy is a position, not a story

Use this five-step logic before writing any conclusion:

1. **Name the real exposure.** “I own 100 shares” is an exposure. “I think the chart looks good” is not yet one.
2. **Name the desired trade-off.** Keep upside? Limit loss? Commit to buy at a lower price? Earn premium while accepting assignment? Need more time?
3. **Draw final payoffs.** Use at least five final prices, include multiplier and all premiums.
4. **Draw the path risks.** Margin, assignment, early exercise, dividends, liquidity, spreads, and whether cash is available.
5. **Compare alternatives.** Stock alone, cash, a different strike/date, a defined-risk spread, or no position at all.

## The agent’s final answer format

An educational agent should never end with “buy” or “sell.” It should end like this:

```text
Position studied: [full multi-leg description]
Purpose claimed: [hedge / stock substitute / conditional sale / conditional purchase / movement view]
Cash today: [premium, spread, fees]
At-expiry table: [five prices and dollar P&L]
Maximum gain / loss: [with conditions]
Break-even(s): [with conditions]
Path risks: [margin, assignment, early exercise, liquidity]
Model and market comparison: [inputs, bid/ask, timestamp]
What must happen: [direction + size + timing + volatility]
What would prove this incomplete: [missing facts or falsifier]
Status: [study only / paper test / insufficient evidence]
```

The best strategy is not the one with the prettiest premium. It is the one whose obligations, cash needs, and failure modes you can still explain after the market moves against you.

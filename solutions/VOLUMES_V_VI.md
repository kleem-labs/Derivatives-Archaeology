# Solutions — Volumes V and VI

## 030 — Cost of Carry

For the gold example, `F_0=2000e^((.05+.01)×.5)=$2,060.91`. A complete answer lists financing and storage/insurance as costs raising forward price, and cash income or ownership benefit as deductions. The formula should not be used mechanically for a non-storable index: without a tradable carry portfolio, expectation and risk premium enter.

## 031 — Dividends and Income

The known $3 dividend in six months has present value `3e^(-.05×.5)=$2.9259`. Carry the adjusted spot: `(100-2.9259)e^.05=$102.05` approximately. For the alleged $0.80 parity violation, rebuild parity with the exact dividend schedule and executable bid/ask sides. Also confirm European versus American exercise, stock borrow, settlement, funding, size, and fees. Only a positive residual after all adjustments is evidence of a trade.

## 032 — Commodities and Convenience Yield

Rearranging the idealized relation gives `y=r+u-ln(F_0/S_0)/T`. Treat the result as implied net convenience under the model, not an observed coupon. A valid commodity term sheet must specify grade, delivery point, window, inspection, transport responsibility, force majeure, settlement, and substitute-delivery rules. The refinery example shows why physical ownership can be valuable even when a futures gain has equal mark-to-market size.

## 033 — Basis and Convergence

For a short hedge opened at futures `F_0`, futures gain is `F_0-F_T`. Effective sale price is `S_T+(F_0-F_T)=F_0+(S_T-F_T)=F_0+b_T`, where `b_T` is final spot-minus-futures basis. The hedge fixes initial futures price but leaves final basis uncertain. In the example, final basis `5.10-5.20=-.10`, so effective price is `6.00-.10=$5.90` before costs.

## 034 — Margin and Leverage

For $100,000 notional and $8,000 initial margin, a 3% adverse move loses $3,000, leaving $5,000 before additional requirements—37.5% of initial collateral. A complete pre-trade stress also applies a historically severe move, widened basis, higher exchange margin, and delayed hedge benefit, then compares required cash with unencumbered liquidity. If collateral runs out before the offset arrives, economic convergence cannot save the position.

## 035 — Hedging with Futures

`N=.8×500/100=4` contracts exactly, so no rounding is needed. If the calculation were 4.4, rounding to four leaves some exposure; rounding to five can over-hedge if actual quantity is only 500 or production falls. The decision depends on volume uncertainty, asymmetry of over- versus under-hedging, contract granularity, basis, and limits.

## 036 — Minimum-Variance Hedge Ratio

With `rho=.8`, `sigma_S=.03`, `sigma_F=.025`, `h*=.8×.03/.025=.96`. This is the least-squares slope for the chosen sample, horizon, and objective. A valid interpretation says that roughly .96 units of futures price exposure historically offset one unit of cash exposure—not that 96% of all risk is eliminated. Re-estimate across windows and stress correlation breakdown.

## 037 — Bootstrapping Discount Curves

Given an already known `P(0,.5)`, a one-year par instrument satisfying `100=cP(0,.5)+(100+c)P(0,1)` yields `P(0,1)=[100-cP(0,.5)]/(100+c)`. After each solution, reprice the input instrument. A complete answer also checks accrual fractions, calendar, compounding, quote conversion, interpolation, positivity of discount factors, and plausible forward rates.

## 038 — Forward Rates and Swaps

The forward rate follows from equal terminal wealth: invest directly to `T_2` or invest to `T_1` and roll. Hence `1+f tau=P(0,T_1)/P(0,T_2)`. The par swap rate equals projected floating-leg PV divided by fixed-leg annuity `sum alpha_iP(0,T_i)`. It is a curve-consistent break-even rate, not automatically an unbiased forecast of the later realized rate.

## 039 — Options on Futures

Before comparing quoted volatilities, match option model convention (Black, normal, shifted), underlying futures month, option expiry, strike, style, settlement into cash or futures, premium-paid versus futures-style margining, multiplier, currency, and curve. Two identical prices can imply different volatility numbers under different conventions; two identical volatility numbers can represent different cash premiums.

## 040 — American Exercise

At every tree node calculate `continuation=e^(-r dt)[p*V_up+(1-p*)V_down]` and `exercise=max(K-S,0)` for a put or `max(S-K,0)` for a call. American value is their maximum. Being in the money is insufficient: exercise sacrifices remaining optionality. For a non-dividend call with nonnegative rates, paying strike early and abandoning protection makes early exercise generally inferior to holding or selling the option.

## 041 — Early-Exercise Boundaries

Intrinsic value being positive only says exercise pays something, not that it pays more than continuation. Selling a liquid option dominates exercise when market price exceeds intrinsic value after costs because the sale preserves time value. Exercise can be rational for deeply in-the-money puts, calls immediately before sufficiently large dividends, illiquid options with no better sale, or positions constrained by settlement/financing. Report the exercise-minus-continuation margin near the boundary.

## 042 — Barriers and Path Dependence

One acceptable monthly-average commodity specification: observe the official exchange settlement in USD per unit on every scheduled business day in the named month; if a day is a holiday use no observation rather than carrying forward; if the publisher later corrects a value before a named cutoff use the correction; negative values are allowed; if more than three observations are missing use an identified fallback source, otherwise average available values; round average to four decimals; pay `notional×max(average-K,0)` two business days later. Other answers are valid if source, schedule, missing data, holidays, negatives, rounding, disruption, currency, and payment are unambiguous.

## 043 — Monte Carlo

For discounted payoff samples `X_i`, estimate `V=mean(X_i)` and `SE=sample_sd(X_i)/sqrt(N)`; an approximate 95% sampling interval is `V±1.96SE`. Verification should recover a known vanilla price across multiple seeds and tightening intervals. Increasing paths reduces sampling error, not time-discretization, payoff-code, parameter, or model error. Antithetic and control variates are valid variance-reduction answers when unbiasedly applied.

## 044 — Finite Differences

A valid convergence study independently refines stock spacing, time spacing, and outer boundaries, compares European vanilla value with closed form, and inspects price monotonicity, convexity, nonnegativity, and stable Greeks. Explicit instability appears as oscillation or negative values when its step restriction fails. An American implementation must also verify value is at least European and at least intrinsic at every node.

## 045 — Transaction Costs and Discrete Hedging

There is no universal winning frequency. Define an objective such as `mean transaction cost + lambda×variance(residual hedge P&L)`, use identical paths and executable spreads, then compare daily, weekly, and delta-band policies. Larger `lambda` favors tighter hedging; wider spreads favor less frequent trading. Report turnover, tail loss, jump behavior, and sensitivity rather than only the minimizing policy.

## 046 — Liquidity and Bid–Ask Spreads

With model value $10 inside an $8 bid/$11 ask, neither buying nor selling realizes the model mark. Evidence could come from an executable synthetic replication whose all-in ask is below $11 (supporting sale of the dear direct option plus purchase of replication) or whose executable bid exceeds $8 in the reverse direction, after funding, borrow, fees, and size. A tighter firm quote outside a defensible model range may also create an investment thesis, but not pure arbitrage without replication.

## 047 — Portfolio Greeks and Scenarios

Example damaging a delta-neutral long-gamma book: spot remains nearly unchanged for a month, realized movement is low, implied volatility falls 8 points, bid–ask spreads widen, and theta plus vega loss exceeds small rebalancing gains. Another valid case is a discontinuous barrier jump that destroys value despite favorable local gamma. The scenario must reprice all factors coherently and include costs; “spot falls” alone is insufficient because initial delta is neutral and long gamma can benefit from movement.

## 048 — Value at Risk and Expected Shortfall

Let both distributions have 95% of observations at losses no greater than $1, so 95% VaR is $1. Distribution A places the worst 5% at $2; Distribution B places the worst 5% at $100. Expected shortfall is $2 versus $100, while VaR is identical under the chosen quantile convention. A short-option seller should fear B because the tail beyond the threshold contains catastrophic convex loss and likely liquidity stress.

## 049 — Model Validation and Limits

The capstone has no single contract answer. A passing submission must include: an observable real exposure; reproducible term sheet; state/date payoff table; replication or bounds; labeled pricing measure versus belief distribution; at least two valuation checks; Greeks/scenarios and hedge; executable costs, funding, collateral, and exit; maximum/stress loss; buyer and seller memos; and a falsifier. Another reader must reproduce cash flows and the valuation range without oral clarification. If the claim is incomplete, a range and explicit extra pricing criterion are required rather than one unexplained number.

[Return to the solution index](../SOLUTIONS.md)


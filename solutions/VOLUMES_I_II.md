# Solutions — Volumes I and II

## 000 — A Promise About the Future

1. Arun's long-forward value is `10,000×(8.20-6.00)=$22,000`. Mara's short-forward value is `-$22,000`. These are delivery-date contract values before default, fees, or any separate wheat-production economics.
2. No. Zero-sum derivative cash flows can improve both parties' welfare ex ante. Mara replaces an uncertain sale price with one supporting debt service; Arun replaces uncertain input cost with one supporting promised bread prices. Each may willingly surrender favorable surprise to remove harmful surprise.
3. Example: “At settlement, seller pays buyer `$1,000×max(50-R,0)` where `R` is rainfall in millimeters.” Still missing: named station, measurement interval and timestamps, data publisher, missing/corrected-data rule, currency, payment date, cap, rounding, credit/collateral, and disruption or termination terms.

## 001 — Payoffs Before Prices

1. For a long $90 put at terminal prices $60, $90, $120, payoffs are `$30,$0,$0`; the short put has `-$30,$0,$0`. Profit additionally subtracts premium for the long and adds it for the short, carried to a consistent date if required.
2. Buy a call at strike `K` and sell a call at `K+15`. The payoff is zero below `K`, rises one-for-one between strikes, and remains $15 above the upper strike. Example strikes are $100 and $115.
3. A payoff diagram specifies terminal cash flow only. Today's premium also requires time, discounting, possible-state weights or replication, volatility and other dynamics, dividends/carry, exercise rules, credit, liquidity, and costs.

## 002 — Time Has a Price

1. `PV=1000e^(-.04×2)=$923.1163`. Check: `$923.1163e^.08=$1,000` up to rounding.
2. Compounding differs: 5% annual gives one-year factor 1.05; 5% continuous gives `e^.05≈1.051271`. Day count and payment frequency can change it further.
3. At minimum: currency, maturity, compounding, collateral, credit quality, funding/borrowing access, day-count basis, payment calendar, and whether a single rate or full curve is intended.

## 003 — No Free Lunch

1. Cash flows from buying A and selling B:

| Date | Buy A | Sell B | Net |
|---|---:|---:|---:|
| Today | -$100 | +$101 | +$1 |
| One year | +$105 | -$105 | $0 |

2. Confirm same contract terms, expiry and settlement; executable ask at cheap venue and bid at dear venue; available size; fees; funding; collateral; counterparty/clearing risk; transferability; exercise style; taxes; and ability to hold both legs. A mid-price difference is insufficient.
3. Replication matches every modeled state. Once the option obligation is exactly met by stock and cash, directional probability does not affect the cost equality. Forecast disagreement remains relevant to investment demand, not the no-arbitrage replication price.

## 004 — The Forward Price

1. `F_0=80e^((.04-.015)×1)=80e^.025=$82.0252`.
2. If market forward is exactly $5 above fair delivery price, borrow to buy the asset and short the market forward. At maturity, deliver the asset, repay fair carried cost, and retain $5 per unit before costs. Its present value is `$5e^(-.04)=$4.8039` under the exercise rate.
3. The forward is fixed by the relative cost of two delivery routes—carry spot or use the forward. It can differ from expected future spot because expectations and risk premia do not enter the mechanical replication in the same way.

## 005 — Futures Are Re-settled

1. For a long contract with multiplier 50:

| Day | Settlement move | Variation margin | Cumulative |
|---|---:|---:|---:|
| 1 | 104-100=+4 | +$200 | +$200 |
| 2 | 101-104=-3 | -$150 | +$50 |
| 3 | 108-101=+7 | +$350 | +$400 |

2. The futures leg can demand cash after an adverse interim move while the offsetting physical benefit arrives only at maturity. Without liquid collateral, the hedger may be closed out before convergence.
3. The distinction is least important when rates are deterministic (and common funding assumptions hold), so the reinvestment value of daily gains/losses has no state-dependent covariance effect.

## 006 — Options Create Asymmetry

1. Call payoff is `max(S_T-110,0)`; profit at expiry ignoring financing is `max(S_T-110,0)-4`. Break-even is $114. At $90/$110/$130, payoff is $0/$0/$20 and profit is -$4/-$4/+$16.
2. Selling stock removes both downside and upside and ends ownership exposures such as dividends. Stock plus protective put retains upside and ownership but creates a floor near strike, at the cost of premium and subject to basis, expiry, and contract terms.
3. With equal chances of $80 and $120, mean stock is $100 but the $100 call payoffs are $0 and $20, mean $10. At a certain $100 the call pays zero. The convex floor discards the negative branch and retains the positive branch.

## 007 — Put–Call Parity

1. Portfolio A is call plus $105 terminal cash; B is put plus stock:

| `S_T` | A | B |
|---:|---:|---:|
| $70 | $0+$105=$105 | $35+$70=$105 |
| $105 | $0+$105=$105 | $0+$105=$105 |
| $150 | $45+$105=$150 | $0+$150=$150 |

2. `C=P+S_0-Ke^(-rT)`: long one put, long one share, and borrow the present value of strike (a short zero-coupon bond). Their terminal payoff equals the call.
3. Trades execute at bid or ask, not mid. The apparent difference must survive crossing every spread, stock borrow, dividends, fees, funding, size limits, exercise/settlement differences, and legging risk.

## 008 — One Period, Two Futures

1. With `S_0=100`, terminal stock $130/$80, `K=100`, rate 5%, one year: call payoff is $30/$0. `Delta=30/(130-80)=.6`. In the down state `.6×80=$48`, so borrow $48 at maturity, present value `$48e^-.05=$45.6588`. Price is `.6×100-45.6588=$14.3412`.
2. Up state: `.6×130-48=$30`; down: `.6×80-48=$0`. Only after both checks should the current cost be accepted.
3. No. At terminal stock $105 the same hedge pays `.6×105-48=$15`, while the call pays $5. Two instruments span two independent states, not a three-point kink in general.

## 009 — Risk-Neutral Probability

1. `p*=(1.04-.8)/(1.3-.8)=.24/.5=.48`.
2. A real-world up probability can be, for example, 70%. It changes real-world expected return, but not the replication cost: the stock-and-bond portfolio still matches both state payoffs.
3. If risk-free growth exceeds `u`, short one share for `S_0` and invest the proceeds. At maturity the investment exceeds `uS_0`, while the share costs at most `uS_0` to repurchase. The residual is positive in every modeled state.

## 010 — Many Small Steps

1. Backward induction needs values at the children before it can compute continuation at their parent. The terminal contract payoff supplies the boundary from which all earlier values are derived.
2. Call delta is near zero far below strike when both next payoffs are zero; between zero and one and often near one-half around the economically relevant strike region; near one far above strike when both branches behave like stock.
3. Time-step convergence shows numerical solutions stabilize for the chosen tree model. Model validation asks whether its dynamics, parameters, exercise rules, and market assumptions represent the intended claim and observed market.

## 011 — The Black–Scholes Limit

1. With `1/dt` independent steps, `dt`-sized shocks have total variance of order `dt` and vanish. `sqrt(dt)`-sized shocks have variance `dt` each, so their `1/dt` variances add to order one. Uncertainty survives without exploding.
2. The payoff function maps a terminal state into cash; a probability distribution assigns weights to states. A contract can be completely specified before either real-world or pricing probabilities are chosen.
3. Convergence shows values stabilize as the numerical time grid is refined within the chosen tree family. It does not prove that the diffusion dynamics, constant volatility, market assumptions, or parameter estimates describe reality.
4. The three keys are: a continuous stochastic process with correct scaling; calculus that retains quadratic variation on rough paths; and a pricing measure/numeraire framework that makes discounted tradable gains martingales without treating pricing weights as forecasts.

[Return to the solution index](../SOLUTIONS.md)

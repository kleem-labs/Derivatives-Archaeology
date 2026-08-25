# Solutions — Volumes III and IV

## 012 — Random Variables

The random variable is the rule assigning a numerical observation to each modeled state. Probability is a separate weighting rule over those states. Two models can share the distribution of terminal `S_T` and disagree on a barrier because the barrier observes intermediate crossings. A sufficient state for a European call needs terminal spot; a continuously monitored barrier also needs survival/crossing information.

## 013 — Expectation and Variance

One example uses equally likely values. Distribution A: `{-sqrt(3),0,+sqrt(3)}` with probabilities `{1/6,2/3,1/6}`; distribution B: `{-1,+1}` with probabilities `{1/2,1/2}` (a third state may repeat zero with zero probability). Both have mean zero and variance one, but for a zero-strike call A has expected payoff `sqrt(3)/6≈.2887`, while B has `.5`. The tail arrangement, not only mean and variance, affects the convex payoff. The worked put value is `.95×(.2×40)=$7.60` only if the weights are pricing weights.

## 014 — Normal and Lognormal Models

Using `S_0=100`, `mu=.06`, `sigma=.20`, `T=1`, terminal prices are approximately $69.77, $104.08, and $155.27 at `Z=-2,0,2`. With `sigma=.40`, they are about $44.93, $98.02, and $213.84. The median falls from $104.08 to $98.02 because `-.5sigma²` becomes more negative, while the mean remains `100e^.06≈$106.18`. The upper tail expands enough to preserve it.

## 015 — Brownian Motion

Daily increments should use standard deviation `sigma/sqrt(252)`; weekly increments use roughly `sigma/sqrt(52)`. Over a year both accumulated distributions target variance `sigma²`, although sampled paths differ. Insert an instantaneous jump `J`: finer subdivision still contains one discontinuity. It cannot be represented as a sequence of hedgeable Brownian moves occurring before the market reprices.

## 016 — Quadratic Variation

With `n` equal Brownian intervals over `T`, each increment has expected square `T/n`. Summing `n` terms gives `n(T/n)=T`. Doubling `n` halves each expected squared increment while doubling their number. For a smooth path, increments are order `1/n`, squares order `1/n²`, and their sum vanishes.

## 017 — Itô's Lemma

Start from `dV=V_tdt+V_SdS+.5V_SS(dS)²`. Substitute `dS=muSdt+sigmaSdW`. Discard `(dt)²` and `dtdW`, retain `(dW)²=dt`, so `(dS)²=sigma²S²dt`. Collect terms to obtain `dV=(V_t+muSV_S+.5sigma²S²V_SS)dt+sigmaSV_SdW`.

## 018 — Change of Measure

1. Investors may strongly dislike risk. The risk-neutral measure is a pricing reweighting that makes discounted tradable gains martingales; it does not describe preferences.
2. Forecasting actual loss probability, setting physical inventory, estimating expected investment P&L, and capital stress design require a real-world `P` model.
3. When risks are unspanned, the equivalent martingale measure—and therefore prices assigned to nonreplicable claims—can be non-unique. Extra calibration or economic criteria are required.

## 019 — Martingales and Numeraires

A numeraire is the traded measuring unit. The matching pricing measure is the state weighting under which prices expressed in that numeraire have the martingale property: current relative value equals conditional expected future relative value. For a dividend-paying stock, use the total gains process—stock value plus reinvested dividends—or subtract the dividend yield appropriately; raw ex-dividend price alone is not the martingale object.

## 020 — Delta

Rebalance rather than assume today's delta is permanent if the goal is dynamic replication. Gamma measures the local rate at which delta changes with spot. Delta can also change without a trade because time passes, implied volatility changes, rates/dividends change, or the pricing model/surface is recalibrated.

## 021 — Gamma

For a convex function, the graph lies above its tangent away from the tangency point. A delta approximation follows that tangent, so actual option value exceeds the linear estimate for moves on either side, giving a positive second-order correction. For concavity, the graph lies below and gamma is negative.

## 022 — Theta

Positive theta alone can conceal short gamma, short vega or skew, jump exposure, assignment, unbounded payoff, and margin/liquidity risk. Inspect full repricing under large spot and volatility moves, maximum contractual loss, hedge cost, spread, funding, and whether the position survives a gap before collecting further theta.

## 023 — Vega and Rho

With the standard chapter call, Black–Scholes values at 19%, 20%, and 21% are approximately $7.626, $8.021, and $8.420. Centered vega is roughly `(8.420-7.626)/.02=$39.7` per unit volatility, or about $0.397 per volatility point. A ten-point bump includes volatility convexity, so multiplying the one-point vega by ten will not exactly reproduce full repricing.

## 024 — Dynamic Hedging

Delta-neutrality names exposures at a particular time and input state. Without trading, delta changes when spot moves (gamma), time passes (charm), implied volatility/surface changes (vanna and recalibration), rates/dividends change, or a barrier/exercise condition changes state. Therefore a hedge report needs timestamp, market inputs, and model.

## 025 — Realized Volatility

Keeping every second price changes the return intervals: intermediate reversals disappear and remaining log returns combine. Squared combined returns are not generally the sum of squared component returns because of cross terms. Annualization also changes with sampling frequency. The result demonstrates that realized volatility is an estimator defined by a sampling scheme.

## 026 — Implied Volatility

The inverse procedure brackets volatility and repeatedly reprices until model price matches the executable option price. Validity first requires no-arbitrage bounds. Bid and ask should produce an implied-volatility interval, not one magic number. A market price inside that interval is not an executable mispricing.

## 027 — The Volatility Smile

A good market-reading answer first converts consistent executable quotes using one forward, curve, dividend, clock, and model convention. It then checks strike monotonicity, butterfly convexity, and maturity consistency. A 30% downside put is not “expensive” solely relative to 20% ATM volatility; the conclusion requires a crash/skew thesis, alternative hedge, costs, and stress loss.

## 028 — Local and Stochastic Volatility

Local volatility makes future volatility a deterministic function of `(S,t)` and can fit today's vanilla surface. Stochastic volatility adds a random variance state and correlation, producing different forward-smile and exotic behavior. Model choice should follow payoff dependence: surface marking may favor robust local interpolation; barriers and forward-starts demand plausible dynamics. Calibration alone does not decide.

## 029 — Jumps and Incomplete Markets

Example: three terminal states with traded cash payoff `(1,1,1)` and stock payoff `(80,100,130)`. Their span has dimension at most two. A digital payoff `(0,1,0)` generally cannot be written as `a+bS_T` across all three states: the first and third equations determine a line whose middle value is not one. State prices satisfying cash and stock prices therefore retain one free dimension, producing multiple digital values within no-arbitrage bounds.

[Return to the solution index](../SOLUTIONS.md)


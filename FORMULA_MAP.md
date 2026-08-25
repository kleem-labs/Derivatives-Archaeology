# Formula Map

Equations are indexed by the market problem they repair.

## Moving money through time

`PV(X_T) = X_T e^{-rT}` and `FV(X_0) = X_0 e^{rT}`.

## Preventing cash-and-carry arbitrage

For a non-income-paying asset, `F_0(T) = S_0 e^{rT}`. With continuous yield `q`, `F_0(T) = S_0 e^{(r-q)T}`.

## Reconstructing one option from another

European put–call parity: `C - P = S_0 - K e^{-rT}` for a non-income-paying stock.

## Replicating one-period uncertainty

`Delta = (C_u - C_d)/(S_u - S_d)` and `C_0 = e^{-rT}[p* C_u + (1-p*) C_d]`, where `p* = (e^{rT} - d)/(u-d)`.

## Continuous-time European options

`C = S_0 e^{-qT}N(d_1) - K e^{-rT}N(d_2)`,

`P = K e^{-rT}N(-d_2) - S_0 e^{-qT}N(-d_1)`,

`d_1 = [ln(S_0/K) + (r-q+sigma^2/2)T]/(sigma sqrt(T))`, and `d_2 = d_1 - sigma sqrt(T)`.

Each formula is conditional on its chapter's assumptions. A formula without those assumptions is an artifact removed from its layer.


# 042 — Barriers and Path Dependence

Two price paths can end at the same `S_T` yet give different barrier, Asian, or lookback payoffs. Terminal distribution alone no longer suffices; the path carries state.

A barrier option activates or dies when a level is crossed. Discrete monitoring can miss crossings between observations, so continuous and daily-monitored contracts differ. Asian options depend on an average, requiring the running sum as an additional state variable.

Path dependence expands computation and exposes model dynamics beyond the vanilla surface.

Next: [Monte Carlo](../043-monte-carlo/README.md).


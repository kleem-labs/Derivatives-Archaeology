# 024 — Dynamic Hedging: Replication Through Rebalancing

The binomial tree changed delta at every node. Continuous-time replication does the same: hold `Delta_t=V_S(S_t,t)` shares and rebalance as spot and time move.

A static delta hedge removes only the first small move. Gamma changes the required shares. Under exact diffusion assumptions with continuous frictionless trading, rebalancing and financing reproduce the option. Real hedges are discrete and costly; jumps occur between trades, volatility is unknown, and markets can gap.

Replication is therefore both a pricing proof and an error decomposition. The gap between model replication and realized hedging reveals model, execution, and parameter risk.

Next: [Realized Volatility](../025-realized-volatility/README.md).


# 031 — Dividends and Income

An owner receives dividends before forward delivery; a forward holder does not. For known cash dividends, subtract their present value from spot before carrying the remainder: `F_0=(S_0-PV(dividends))e^(rT)`. For continuous proportional yield `q`, `F_0=S_0e^((r-q)T)`.

Using the cash-dividend and yield formulas interchangeably creates errors, especially near large discrete payments. Dividend forecasts can change, and option exercise decisions may depend on their timing.

Income is not merely a correction term: it is part of the asset bundle being replicated.

Next: [Commodities and Convenience Yield](../032-commodities-and-convenience-yield/README.md).


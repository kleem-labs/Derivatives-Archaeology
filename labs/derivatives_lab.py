"""Small, dependency-free experiments for Derivatives Archaeology."""

from math import erf, exp, log, sqrt


def present_value(cash_flow: float, rate: float, years: float) -> float:
    return cash_flow * exp(-rate * years)


def forward_price(spot: float, rate: float, years: float, yield_rate: float = 0.0) -> float:
    return spot * exp((rate - yield_rate) * years)


def put_from_parity(call: float, spot: float, strike: float, rate: float, years: float) -> float:
    return call - spot + present_value(strike, rate, years)


def one_period_call(spot: float, strike: float, up: float, down: float, rate: float, years: float):
    growth = exp(rate * years)
    if not down < growth < up:
        raise ValueError("No-arbitrage requires down < risk-free growth < up")
    stock_up, stock_down = spot * up, spot * down
    call_up, call_down = max(stock_up - strike, 0.0), max(stock_down - strike, 0.0)
    delta = (call_up - call_down) / (stock_up - stock_down)
    bond_at_maturity = call_down - delta * stock_down
    bond_now = present_value(bond_at_maturity, rate, years)
    probability = (growth - down) / (up - down)
    price_by_replication = delta * spot + bond_now
    price_by_weights = present_value(
        probability * call_up + (1.0 - probability) * call_down, rate, years
    )
    return {
        "stock_up": stock_up,
        "stock_down": stock_down,
        "call_up": call_up,
        "call_down": call_down,
        "delta": delta,
        "bond_now": bond_now,
        "risk_neutral_probability": probability,
        "price": price_by_replication,
        "weighted_price": price_by_weights,
    }


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def black_scholes(spot: float, strike: float, rate: float, volatility: float, years: float, yield_rate: float = 0.0):
    if min(spot, strike, volatility, years) <= 0:
        raise ValueError("spot, strike, volatility, and years must be positive")
    root_time = sqrt(years)
    d1 = (log(spot / strike) + (rate - yield_rate + 0.5 * volatility**2) * years) / (volatility * root_time)
    d2 = d1 - volatility * root_time
    call = spot * exp(-yield_rate * years) * normal_cdf(d1) - strike * exp(-rate * years) * normal_cdf(d2)
    put = strike * exp(-rate * years) * normal_cdf(-d2) - spot * exp(-yield_rate * years) * normal_cdf(-d1)
    return {"call": call, "put": put, "d1": d1, "d2": d2}


def main() -> None:
    spot, strike, rate, years = 100.0, 105.0, 0.05, 1.0
    print("One year from now, $105 is worth today:", round(present_value(strike, rate, years), 4))
    print("No-arbitrage one-year forward price:", round(forward_price(spot, rate, years), 4))
    tree = one_period_call(spot, strike, up=1.20, down=0.90, rate=rate, years=years)
    print("\nOne-period replication")
    for name, value in tree.items():
        print(f"  {name}: {value:.6f}")
    bs = black_scholes(spot, strike, rate, volatility=0.20, years=years)
    print("\nBlack–Scholes:", {key: round(value, 6) for key, value in bs.items()})
    parity_gap = bs["call"] - bs["put"] - (spot - present_value(strike, rate, years))
    print("Put–call parity error:", f"{parity_gap:.12f}")


if __name__ == "__main__":
    main()


"""Advanced dependency-free numerical experiments for the complete book."""

from math import exp, log, sqrt
from random import Random
from statistics import fmean, stdev

try:
    from labs.derivatives_lab import black_scholes
except ModuleNotFoundError:  # Support `python3 labs/advanced_lab.py` from repo root.
    from derivatives_lab import black_scholes


def binomial_option(spot, strike, rate, volatility, years, steps, kind="call", american=False):
    if steps < 1 or min(spot, strike, volatility, years) <= 0:
        raise ValueError("positive inputs and at least one step required")
    dt = years / steps
    up = exp(volatility * sqrt(dt))
    down = 1.0 / up
    growth = exp(rate * dt)
    probability = (growth - down) / (up - down)
    if not 0.0 < probability < 1.0:
        raise ValueError("tree parameters violate no-arbitrage")

    def payoff(stock):
        return max(stock - strike, 0.0) if kind == "call" else max(strike - stock, 0.0)

    values = [payoff(spot * up**j * down ** (steps - j)) for j in range(steps + 1)]
    discount = exp(-rate * dt)
    for level in range(steps - 1, -1, -1):
        next_values = []
        for j in range(level + 1):
            continuation = discount * (probability * values[j + 1] + (1 - probability) * values[j])
            stock = spot * up**j * down ** (level - j)
            next_values.append(max(continuation, payoff(stock)) if american else continuation)
        values = next_values
    return values[0]


def implied_volatility(target, spot, strike, rate, years, kind="call", tolerance=1e-10):
    low, high = 1e-8, 5.0
    for _ in range(200):
        middle = (low + high) / 2
        price = black_scholes(spot, strike, rate, middle, years)[kind]
        if price < target:
            low = middle
        else:
            high = middle
        if high - low < tolerance:
            break
    return (low + high) / 2


def finite_difference_greeks(spot, strike, rate, volatility, years, bump=0.01):
    center = black_scholes(spot, strike, rate, volatility, years)["call"]
    upper = black_scholes(spot + bump, strike, rate, volatility, years)["call"]
    lower = black_scholes(spot - bump, strike, rate, volatility, years)["call"]
    delta = (upper - lower) / (2 * bump)
    gamma = (upper - 2 * center + lower) / bump**2
    return {"delta": delta, "gamma": gamma}


def monte_carlo_call(spot, strike, rate, volatility, years, paths=20_000, seed=7):
    rng = Random(seed)
    discounted = []
    drift = (rate - 0.5 * volatility**2) * years
    diffusion = volatility * sqrt(years)
    for _ in range(paths):
        terminal = spot * exp(drift + diffusion * rng.gauss(0.0, 1.0))
        discounted.append(exp(-rate * years) * max(terminal - strike, 0.0))
    estimate = fmean(discounted)
    error = stdev(discounted) / sqrt(paths)
    return {"price": estimate, "standard_error": error, "ci95": (estimate - 1.96 * error, estimate + 1.96 * error)}


def realized_volatility(prices, periods_per_year=252):
    returns = [log(right / left) for left, right in zip(prices, prices[1:])]
    return stdev(returns) * sqrt(periods_per_year)


def minimum_variance_hedge(spot_changes, futures_changes):
    if len(spot_changes) != len(futures_changes) or len(spot_changes) < 2:
        raise ValueError("matching samples required")
    mean_s, mean_f = fmean(spot_changes), fmean(futures_changes)
    covariance = sum((s - mean_s) * (f - mean_f) for s, f in zip(spot_changes, futures_changes))
    variance_f = sum((f - mean_f) ** 2 for f in futures_changes)
    return covariance / variance_f


def main():
    inputs = dict(spot=100.0, strike=105.0, rate=0.05, volatility=0.20, years=1.0)
    european = binomial_option(**inputs, steps=500)
    american_put = binomial_option(**inputs, steps=500, kind="put", american=True)
    closed = black_scholes(**inputs)["call"]
    simulation = monte_carlo_call(**inputs)
    print("European call — tree / closed form:", round(european, 6), round(closed, 6))
    print("American put — tree:", round(american_put, 6))
    print("Recovered implied volatility:", round(implied_volatility(closed, 100, 105, .05, 1), 8))
    print("Finite-difference Greeks:", finite_difference_greeks(**inputs))
    print("Monte Carlo:", simulation)


if __name__ == "__main__":
    main()

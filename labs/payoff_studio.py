"""Transparent tools for prototyping terminal-payoff derivatives."""

from math import exp, log, sqrt
from random import Random
from statistics import fmean, stdev


def payoff_table(payoff, states):
    return [(state, float(payoff(state))) for state in states]


def discounted_scenario_value(payoff, states, probabilities, rate, years):
    if len(states) != len(probabilities) or not states:
        raise ValueError("states and probabilities must be non-empty and aligned")
    if any(p < 0 for p in probabilities) or abs(sum(probabilities) - 1.0) > 1e-10:
        raise ValueError("probabilities must be non-negative and sum to one")
    return exp(-rate * years) * sum(p * payoff(state) for state, p in zip(states, probabilities))


def risk_neutral_lognormal_value(payoff, spot, rate, volatility, years, paths=50_000, seed=11):
    if min(spot, volatility, years) <= 0 or paths < 2:
        raise ValueError("positive market inputs and at least two paths required")
    rng = Random(seed)
    drift = (rate - 0.5 * volatility**2) * years
    diffusion = volatility * sqrt(years)
    samples = []
    for _ in range(paths):
        terminal = spot * exp(drift + diffusion * rng.gauss(0.0, 1.0))
        samples.append(exp(-rate * years) * payoff(terminal))
    estimate = fmean(samples)
    standard_error = stdev(samples) / sqrt(paths)
    return {"value": estimate, "standard_error": standard_error,
            "ci95": (estimate - 1.96 * standard_error, estimate + 1.96 * standard_error)}


def piecewise_linear_payoff(spot, legs):
    """Combine cash, stock, calls, and puts; leg = (kind, quantity, strike)."""
    total = 0.0
    for kind, quantity, strike in legs:
        if kind == "cash":
            unit = 1.0
        elif kind == "stock":
            unit = spot
        elif kind == "call":
            unit = max(spot - strike, 0.0)
        elif kind == "put":
            unit = max(strike - spot, 0.0)
        else:
            raise ValueError(f"unknown leg: {kind}")
        total += quantity * unit
    return total


def main():
    # A capped call spread invented from two calls: long K=100, short K=120.
    payoff = lambda terminal: piecewise_linear_payoff(
        terminal, [("call", 1.0, 100.0), ("call", -1.0, 120.0)]
    )
    print("Payoff table:", payoff_table(payoff, [70, 100, 110, 120, 150]))
    print("Risk-neutral prototype:", risk_neutral_lognormal_value(payoff, 100, .05, .20, 1))
    scenarios = [80, 100, 120, 150]
    beliefs = [.15, .35, .35, .15]
    print("Belief-conditioned value:", discounted_scenario_value(payoff, scenarios, beliefs, .05, 1))


if __name__ == "__main__":
    main()


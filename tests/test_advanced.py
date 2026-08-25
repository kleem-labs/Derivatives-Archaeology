import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from labs.advanced_lab import (  # noqa: E402
    binomial_option, finite_difference_greeks, implied_volatility,
    minimum_variance_hedge, monte_carlo_call, realized_volatility,
)
from labs.derivatives_lab import black_scholes


class AdvancedTests(unittest.TestCase):
    def setUp(self):
        self.inputs = dict(spot=100, strike=105, rate=.05, volatility=.2, years=1)

    def test_tree_converges_to_black_scholes(self):
        tree = binomial_option(**self.inputs, steps=1000)
        closed = black_scholes(**self.inputs)["call"]
        self.assertAlmostEqual(tree, closed, places=2)

    def test_american_is_never_less_than_european(self):
        european = binomial_option(**self.inputs, steps=300, kind="put")
        american = binomial_option(**self.inputs, steps=300, kind="put", american=True)
        self.assertGreaterEqual(american, european)

    def test_implied_volatility_recovers_input(self):
        target = black_scholes(**self.inputs)["call"]
        recovered = implied_volatility(target, 100, 105, .05, 1)
        self.assertAlmostEqual(recovered, .2, places=7)

    def test_finite_difference_greeks_are_positive(self):
        greeks = finite_difference_greeks(**self.inputs)
        self.assertGreater(greeks["delta"], 0)
        self.assertGreater(greeks["gamma"], 0)

    def test_monte_carlo_interval_contains_closed_form(self):
        result = monte_carlo_call(**self.inputs, paths=100_000, seed=3)
        closed = black_scholes(**self.inputs)["call"]
        self.assertLessEqual(result["ci95"][0], closed)
        self.assertGreaterEqual(result["ci95"][1], closed)

    def test_realized_volatility_and_hedge_ratio(self):
        self.assertGreater(realized_volatility([100, 101, 99, 103, 102]), 0)
        self.assertAlmostEqual(minimum_variance_hedge([2, 4, 6], [1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()


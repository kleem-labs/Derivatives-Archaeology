import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from labs.derivatives_lab import (  # noqa: E402
    black_scholes,
    forward_price,
    one_period_call,
    present_value,
)


class DerivativesTests(unittest.TestCase):
    def test_discounting_reverses_compounding(self):
        self.assertAlmostEqual(present_value(100 * math.exp(0.05), 0.05, 1), 100)

    def test_forward_is_spot_grown_at_carry(self):
        self.assertAlmostEqual(forward_price(100, 0.05, 1), 100 * math.exp(0.05))

    def test_binomial_replication_equals_weighted_price(self):
        result = one_period_call(100, 105, 1.2, 0.9, 0.05, 1)
        self.assertAlmostEqual(result["price"], result["weighted_price"])

    def test_binomial_rejects_arbitrage_parameters(self):
        with self.assertRaises(ValueError):
            one_period_call(100, 100, 1.01, 0.90, 0.05, 1)

    def test_black_scholes_satisfies_put_call_parity(self):
        result = black_scholes(100, 105, 0.05, 0.2, 1)
        lhs = result["call"] - result["put"]
        rhs = 100 - present_value(105, 0.05, 1)
        self.assertAlmostEqual(lhs, rhs, places=10)


if __name__ == "__main__":
    unittest.main()


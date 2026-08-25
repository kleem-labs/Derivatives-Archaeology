import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from labs.payoff_studio import (  # noqa: E402
    discounted_scenario_value, payoff_table, piecewise_linear_payoff,
    risk_neutral_lognormal_value,
)


class PayoffStudioTests(unittest.TestCase):
    def test_call_spread_is_capped(self):
        legs = [("call", 1, 100), ("call", -1, 120)]
        self.assertEqual(piecewise_linear_payoff(80, legs), 0)
        self.assertEqual(piecewise_linear_payoff(110, legs), 10)
        self.assertEqual(piecewise_linear_payoff(150, legs), 20)

    def test_scenario_value_validates_probabilities(self):
        with self.assertRaises(ValueError):
            discounted_scenario_value(lambda x: x, [1, 2], [.2, .2], 0, 1)

    def test_payoff_table_keeps_states_visible(self):
        self.assertEqual(payoff_table(lambda x: max(x - 10, 0), [5, 15]), [(5, 0.0), (15, 5.0)])

    def test_monte_carlo_call_is_near_known_value(self):
        result = risk_neutral_lognormal_value(lambda s: max(s - 105, 0), 100, .05, .2, 1, paths=100_000)
        self.assertLess(result["ci95"][0], 8.021352)
        self.assertGreater(result["ci95"][1], 8.021352)


if __name__ == "__main__":
    unittest.main()


import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AgenticMaterialTests(unittest.TestCase):
    def test_agent_blueprint_keeps_a_no_execution_boundary(self):
        text = (ROOT / "AGENTIC_SYSTEM_BLUEPRINT.md").read_text().lower()
        self.assertIn("autonomous trading system", text)
        self.assertIn("cannot send orders", text)
        self.assertIn('"execution_authorized": false', text)
        self.assertIn("human decides", text)

    def test_blueprint_contains_parseable_input_and_output_cards(self):
        text = (ROOT / "AGENTIC_SYSTEM_BLUEPRINT.md").read_text()
        cards = []
        for block in text.split("```json")[1:]:
            cards.append(json.loads(block.split("```", 1)[0]))
        self.assertEqual(len(cards), 2)
        self.assertIn("contract", cards[0])
        self.assertIn("model_inputs", cards[0])
        self.assertIn("status", cards[1])
        self.assertIn("red_flags", cards[1])

    def test_research_has_primary_source_ledger_and_month_plan(self):
        research = (ROOT / "report-source.md").read_text()
        plan = (ROOT / "ONE_MONTH_FOUNDATION.md").read_text()
        for source_name in ("OCC", "SEC", "FINRA", "CFTC", "NIST"):
            self.assertIn(source_name, research)
        self.assertIn("not a promise of stock-market success", plan)
        self.assertIn("paper analyses", plan)


if __name__ == "__main__":
    unittest.main()

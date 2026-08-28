import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class BookTests(unittest.TestCase):
    def test_fifty_sequential_substantial_chapters(self):
        chapters = sorted((ROOT / "excavations").glob("*/README.md"))
        self.assertEqual([int(path.parent.name[:3]) for path in chapters], list(range(50)))
        short = {path.parent.name: len(path.read_text().split()) for path in chapters
                 if len(path.read_text().split()) < 300}
        self.assertFalse(short, f"chapters below prose floor: {short}")

    def test_all_local_markdown_links_resolve(self):
        missing = []
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", path.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                target = target.split("#", 1)[0]
                if target and not (path.parent / target).resolve().exists():
                    missing.append((str(path.relative_to(ROOT)), target))
        self.assertFalse(missing, f"broken local links: {missing}")

    def test_book_has_six_volumes(self):
        volumes = list((ROOT / "book").glob("VOLUME_*.md"))
        self.assertEqual(len(volumes), 6)

    def test_every_excavation_has_a_solution(self):
        solution_text = "\n".join(path.read_text() for path in (ROOT / "solutions").glob("*.md"))
        missing = [number for number in range(50)
                   if not re.search(rf"^## {number:03d} —", solution_text, re.MULTILINE)]
        self.assertFalse(missing, f"excavations without solutions: {missing}")

    def test_later_chapters_do_not_start_with_detached_summaries(self):
        chapters = sorted((ROOT / "excavations").glob("*/README.md"))
        offenders = []
        for number, path in enumerate(chapters):
            if number < 12:
                continue
            lines = [line for line in path.read_text().splitlines()[1:]
                     if not line.startswith("**Vocabulary key:**")]
            first_content = next((line for line in lines if line.strip()), "")
            if not first_content.startswith("## "):
                offenders.append(path.parent.name)
        self.assertFalse(offenders, f"detached preambles before narrative sections: {offenders}")

    def test_key_concepts_appear_only_after_the_problem_earns_them(self):
        chapter_002 = (ROOT / "excavations/002-time-value-of-money/README.md").read_text().lower()
        for premature in ("risk-neutral", "risk compensation", "expected payoff"):
            self.assertNotIn(premature, chapter_002)

        chapter_011 = (ROOT / "excavations/011-black-scholes-limit/README.md").read_text()
        for premature_formula in ("V_t+", "d_1=", "N(d_1)"):
            self.assertNotIn(premature_formula, chapter_011)

        chapter_019 = (ROOT / "excavations/019-martingales-and-numeraires/README.md").read_text()
        self.assertIn("V_t+.5sigma²S²V_SS", chapter_019)
        self.assertIn("C=S_0N(d_1)", chapter_019)

    def test_each_chapter_creates_the_next_link(self):
        chapters = sorted((ROOT / "excavations").glob("*/README.md"))
        missing = []
        for current, following in zip(chapters, chapters[1:]):
            expected = f"../{following.parent.name}/README.md"
            if expected not in current.read_text():
                missing.append((current.parent.name, following.parent.name))
        self.assertFalse(missing, f"missing causal next-chapter links: {missing}")

    def test_plain_reading_edition_covers_every_excavation(self):
        plain_text = "\n".join(path.read_text() for path in (ROOT / "book").glob("VOLUME_*.md"))
        missing = [path.parent.name for path in sorted((ROOT / "excavations").glob("*/README.md"))
                   if f"../excavations/{path.parent.name}/README.md" not in plain_text]
        self.assertFalse(missing, f"plain reading edition misses workshops: {missing}")
        promise = (ROOT / "PLAIN_LANGUAGE_PROMISE.md").read_text()
        self.assertIn("Before a formula appears", promise)

    def test_every_workshop_has_a_plain_language_and_agent_doorway(self):
        chapters = sorted((ROOT / "excavations").glob("*/README.md"))
        missing = []
        for path in chapters:
            opening = "\n".join(path.read_text().splitlines()[:12])
            if "## First, in everyday words" not in opening or "For an AI helper:" not in opening:
                missing.append(path.parent.name)
        self.assertFalse(missing, f"chapters without simple agent-ready doorways: {missing}")

    def test_every_workshop_has_a_vocabulary_key_and_atlas_has_all_chapters(self):
        chapters = sorted((ROOT / "excavations").glob("*/README.md"))
        missing_keys = [path.parent.name for path in chapters
                        if "**Vocabulary key:**" not in "\n".join(path.read_text().splitlines()[:8])]
        self.assertFalse(missing_keys, f"chapters without a vocabulary key: {missing_keys}")

        atlas = (ROOT / "CONCEPT_ATLAS.md").read_text()
        missing_rows = [f"| {number:03d} |" for number in range(50)
                        if f"| {number:03d} |" not in atlas]
        self.assertFalse(missing_rows, f"concept atlas misses chapters: {missing_rows}")


if __name__ == "__main__":
    unittest.main()

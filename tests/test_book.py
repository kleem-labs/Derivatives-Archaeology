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


if __name__ == "__main__":
    unittest.main()


import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_validator_passes(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_skill_declares_expected_name_and_routes(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: deepseek-coding-agent", skill)
        for reference in (
            "references/deepseek-api.md",
            "references/app-integrations.md",
            "references/task-playbooks.md",
            "references/frontend-quality.md",
            "references/testing-debugging.md",
            "references/secure-coding.md",
            "references/language-guides.md",
            "references/tool-calling-safety.md",
        ):
            with self.subTest(reference=reference):
                self.assertIn(reference, skill)
                self.assertTrue((ROOT / reference).is_file())

    def test_skill_is_concise_and_uses_progressive_disclosure(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(len(skill), 12000)
        self.assertIn("load only what is needed", skill)


if __name__ == "__main__":
    unittest.main()

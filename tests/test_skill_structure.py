import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_skill_declares_expected_name_and_references(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: deepseek-coding-agent", skill)
        self.assertIn("references/deepseek-api.md", skill)
        self.assertIn("references/app-integrations.md", skill)
        self.assertIn("references/tool-calling-safety.md", skill)


if __name__ == "__main__":
    unittest.main()

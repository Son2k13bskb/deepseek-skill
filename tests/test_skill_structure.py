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
            "references/discord-bots.md",
            "references/testing-debugging.md",
            "references/secure-coding.md",
            "references/language-guides.md",
            "references/tool-calling-safety.md",
        ):
            with self.subTest(reference=reference):
                self.assertIn(reference, skill)
                self.assertTrue((ROOT / reference).is_file())

    def test_frontend_guidance_covers_visual_and_product_quality(self):
        frontend = (ROOT / "references" / "frontend-quality.md").read_text(
            encoding="utf-8"
        )
        for criterion in (
            "visual decisions",
            "semantic HTML",
            "Every visible control must work",
            "local development",
            "slide deck",
            "responsive",
        ):
            with self.subTest(criterion=criterion):
                self.assertIn(criterion.lower(), frontend.lower())

    def test_discord_guide_covers_commands_components_and_safety(self):
        guide = (ROOT / "references" / "discord-bots.md").read_text(
            encoding="utf-8"
        ).lower()
        for criterion in (
            "slash/application command",
            "prefix command",
            "components v2",
            "interaction lifecycle",
            "permissions",
            "official discord docs",
            "stale controls",
        ):
            with self.subTest(criterion=criterion):
                self.assertIn(criterion, guide)

    def test_skill_is_concise_and_uses_progressive_disclosure(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(len(skill), 12000)
        self.assertIn("Load only the relevant guidance", skill)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Dependency-free structural checks for this Agent Skill."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "deepseek-api.md",
    ROOT / "references" / "coding-workflow.md",
    ROOT / "references" / "tool-calling-safety.md",
)


def main() -> int:
    errors = []
    for path in REQUIRED:
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty required file: {path.relative_to(ROOT)}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append("SKILL.md must start with YAML frontmatter delimited by ---")
        else:
            frontmatter = match.group(1)
            name = re.search(r"(?m)^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", frontmatter)
            description = re.search(r"(?m)^description:\s*(\S.*)$", frontmatter)
            if not name or name.group(1) != "deepseek-coding-agent":
                errors.append("SKILL.md name must be deepseek-coding-agent in hyphen-case")
            if not description or len(description.group(1)) < 20:
                errors.append("SKILL.md needs a useful description in frontmatter")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Skill structure looks good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

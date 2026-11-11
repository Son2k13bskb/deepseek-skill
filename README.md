# DeepSeek Coding Agent Skill

A substantial, portable Agent Skill for making DeepSeek-backed coding assistants more effective across real software projects. It uses progressive-disclosure playbooks inspired by established agent-skill libraries: concise core instructions, focused references, practical templates, and lightweight validation.

## What it teaches

- Repository exploration and project-convention following
- Feature implementation, bug fixing, root-cause debugging, code review, and refactoring
- Frontend/UI quality, responsive behavior, accessibility, and state handling
- Backend, API, database, test, documentation, and operations workflows
- Language/version-aware coding across common stacks without guessing APIs
- Defensive security checks and safe tool usage
- DeepSeek API integration while distinguishing the consumer web/mobile app from the API
- Evidence-based verification and honest completion reports

## Repository map

- `SKILL.md` — main skill instructions and progressive-disclosure routing.
- `references/` — task playbooks, engineering workflow, frontend quality, testing/debugging, secure coding, language guidance, API integration, and tool-call safety.
- `agents/openai.yaml` — optional picker metadata for compatible skill catalogs.
- `scripts/validate_skill.py` — dependency-free checks for required files, metadata, links, and frontmatter size.
- `tests/` — standard-library regression tests for repository structure and skill routing.

## Install/use

Use the installer supported by your coding assistant or copy this repository into its skills directory. Exact paths and supported metadata differ between hosts; follow the host's current documentation. The skill is portable Agent Skill content, not a DeepSeek model modification and not a way to control the consumer DeepSeek website/app.

Try prompts such as:

- “Inspect this project and implement the requested feature with tests. Follow its instructions and report checks actually run.”
- “Reproduce this bug, trace the root cause, make a minimal fix, and add a regression test.”
- “Review this diff for actionable correctness and security issues; cite file/line evidence.”
- “Build a polished responsive page consistent with this repository's stack, including loading, empty, error, and accessible interaction states.”
- “Integrate the current DeepSeek API in this backend. Verify official docs and keep the API key server-side.”

## Validate

Requires Python 3.9+ and no third-party packages:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Accuracy and scope

Model IDs, endpoints, features, limits, and pricing can change; confirm them from current official DeepSeek docs. Framework APIs and commands are version-specific; inspect project manifests and maintained docs. This skill provides guidance, not an execution environment, and makes no claim that consumer chat sessions can be embedded or controlled by third-party apps.

## Official/reference links

- [DeepSeek API docs](https://api-docs.deepseek.com/)
- [DeepSeek API platform](https://platform.deepseek.com/)
- [DeepSeek consumer chat](https://chat.deepseek.com/)
- [Agent Skills specification](https://agentskills.io/)

## License

MIT. See [`LICENSE`](LICENSE).

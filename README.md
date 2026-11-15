# DeepSeek Coding Agent Skill

A practical, portable Agent Skill for making DeepSeek-backed coding assistants more effective across real software projects. It emphasizes repository-grounded implementation, coherent product UI, working interactions, and evidence-based verification. It improves instructions and workflow; it does not change model weights or guarantee parity with another model.

## What it teaches

- Repository exploration and project-convention following
- Feature implementation, bug fixing, debugging, code review, and refactoring
- Product-minded frontend UI: visual hierarchy, polished responsive layouts, semantic HTML, real interactions, and accessible states
- Respect for existing local development, routing, assets, API, and hosting/deployment conventions
- Backend, API, database, test, documentation, and operations workflows
- Language/version-aware coding without guessing APIs
- Defensive security and safe tool usage
- DeepSeek API integration and the distinction between the consumer app and API
- Evidence-based verification and honest completion reports

## Repository map

- `SKILL.md` — main skill instructions and progressive-disclosure routing.
- `references/` — task playbooks, engineering workflow, frontend quality, testing/debugging, secure coding, language guidance, API integration, and tool-call safety.
- `agents/openai.yaml` — optional picker metadata for compatible skill catalogs.
- `scripts/validate_skill.py` — dependency-free checks for required files, metadata, links, and frontmatter size.
- `tests/` — standard-library regression tests for repository structure and skill routing.

## Install/use

Use the installer supported by your coding assistant or copy this repository into its skills directory. Exact paths and supported metadata differ between hosts; follow the host's current documentation.

Try prompts such as:

- “Inspect this project and implement the requested feature with tests. Follow its instructions and report checks actually run.”
- “Reproduce this bug, trace the root cause, make a minimal fix, and add a regression test.”
- “Review this diff for actionable correctness and security issues; cite file/line evidence.”
- “Build a polished, responsive web app page for this product—not a slide or static mockup. Inspect the existing framework, design system, assets, routes, and local run process first. Make the hierarchy, typography, spacing, palette, and interactions feel intentional; ensure every control works and verify the main flow.”
- “Improve this UI: keep the current local hosting and API conventions, use semantic HTML, implement loading/empty/error states, and check mobile layout and keyboard access. Tell me which checks you actually ran.”
- “Integrate the current DeepSeek API in this backend. Verify official docs and keep the API key server-side.”

## Validate

Requires Python 3.9+ and no third-party packages:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Accuracy and scope

Model IDs, endpoints, features, limits, and pricing can change; confirm them from current official DeepSeek docs. Framework APIs and commands are version-specific; inspect project manifests and maintainers' docs. Browser, localhost, and deployment behavior can only be claimed as verified when the relevant checks were actually run.

## Official/reference links

- [DeepSeek API docs](https://api-docs.deepseek.com/)
- [DeepSeek API platform](https://platform.deepseek.com/)
- [DeepSeek consumer chat](https://chat.deepseek.com/)
- [Agent Skills specification](https://agentskills.io/)

## License

MIT. See [`LICENSE`](LICENSE).

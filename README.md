# DeepSeek Coding Agent Skill

A practical, repository-grounded Agent Skill for DeepSeek coding assistants. It guides real engineering work across product UI, application logic, Discord bots, APIs, tests, debugging, and safe integrations.

## What it helps with

- Inspecting a codebase and following its actual conventions before editing
- Building complete, polished interfaces with working interactions and meaningful states
- Designing clear application logic, validation, error handling, and regression tests
- Creating Discord bots with intentional slash/prefix command choices, interaction flows, and modern Components V2 guidance
- Integrating APIs without guessing endpoints, library APIs, model identifiers, or platform behavior
- Verifying changes and reporting evidence honestly

## Quick start

Use the installer supported by your coding assistant or copy this repository into its supported skills directory. Host conventions differ; follow that host's current instructions.

Recommended task flow:

1. Read repository instructions and inspect the relevant code/tests/config.
2. Define the expected behavior and constraints.
3. Load the matching reference guide and make a focused implementation.
4. Verify with the project's real tests, lint, typecheck, or build commands.
5. Summarize the change, checks run, and anything not verified.

## Discord bot development

For Discord bot tasks, use [`references/discord-bots.md`](references/discord-bots.md). It covers command selection (slash/application commands versus prefix commands), interaction lifecycles, Components V2, polished message UI, permissions, intents, security, persistence, reliability, testing, and framework/version verification.

The guide treats Discord messages as a constrained interface: choose the structure that helps users act, avoid noisy template-like output, make components useful, and handle interaction timeouts and permissions deliberately. Always verify current Discord docs and the project's installed library version before using platform features.

## UI and engineering quality

For web or product UI tasks, the skill emphasizes visual hierarchy, semantic controls, accessible interaction, responsiveness, real application behavior, and loading/empty/error/success states. For all code tasks, it emphasizes repo-first reasoning, clear data flow, boundary validation, focused tests, and truthful verification.

## Repository map

- `SKILL.md` — core workflow and guide routing
- `references/` — specialized engineering playbooks, including Discord bots and frontend quality
- `agents/openai.yaml` — picker metadata for compatible catalogs
- `scripts/validate_skill.py` — dependency-free structural validation
- `tests/` — standard-library regression tests

## Example prompts

- “Inspect this project and build the requested Discord bot feature using its existing framework and architecture. Choose slash, prefix, or context-menu commands based on the actual use case, implement permissions and failure states, add tests, and report checks run.”
- “Upgrade this bot's message UI using the current Discord Components V2 API supported by the installed library. Check the official docs first; make every control functional and handle interaction ownership, expiry, and errors.”
- “Build this page in the existing app, not a static mockup. Follow its design system, make it responsive and accessible, implement the real flow, and verify it.”
- “Reproduce this bug, trace the root cause, add a regression test, and report the evidence.”
- “Review this diff for correctness, security, regressions, and test gaps. Cite actionable file/line evidence.”

## Validate

Requires Python 3.9+ and no third-party packages:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Accuracy

Discord API behavior, Components V2, library support, permission/intents requirements, and limits evolve. Verify platform details in current official Discord documentation and inspect the bot's installed library/version before implementation. DeepSeek model IDs, endpoints, features, and pricing can also change; consult current official DeepSeek docs.

## Official references

- [Discord Developer Documentation](https://docs.discord.com/developers/)
- [Discord Components Reference](https://docs.discord.com/developers/components/reference)
- [Discord Application Commands](https://docs.discord.com/developers/interactions/application-commands)
- [Discord Gateway Intents](https://docs.discord.com/developers/events/gateway)
- [DeepSeek API docs](https://api-docs.deepseek.com/)
- [Agent Skills specification](https://agentskills.io/)

## License

MIT. See [`LICENSE`](LICENSE).

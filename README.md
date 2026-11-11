# DeepSeek Coding Agent Skill

A practical, provider-aware Agent Skill for getting reliable software-engineering results from DeepSeek-backed coding assistants. It focuses on repo-grounded changes, debugging, verification, current API references, safe tool use, and integrating **DeepSeek API** with compatible apps.

## What's included

- `SKILL.md` — the loadable skill instructions.
- `references/deepseek-api.md` — official API references, verification checklist, and safe request example.
- `references/app-integrations.md` — how to connect compatible third-party apps, and the important boundary between the consumer DeepSeek app/site and the developer API.
- `references/coding-workflow.md` — task templates and a repository-first engineering workflow.
- `references/tool-calling-safety.md` — validation and permission guidance for agent tools.
- `agents/openai.yaml` — optional picker metadata for compatible skill catalogs.
- `scripts/validate_skill.py` — dependency-free structural validator.
- `tests/` — standard-library tests for the skill's basic structure.

## Install/use

This repository follows the portable Agent Skill convention: a skill directory with `SKILL.md` and optional references/scripts. Install it with the skill manager supported by your coding assistant, or copy this repository (or its contents) into that assistant's skills directory. Exact install locations differ by host; follow that product's current documentation.

After installation, ask naturally, for example:

- “Use DeepSeek to inspect this repo, fix the failing test, and report checks actually run.”
- “Help me connect DeepSeek API to this app; check the official docs and keep my API key secure.”
- “Can I use my DeepSeek mobile/web app account inside this other app? Explain supported options and limitations.”
- “Review this diff for correctness and security issues; cite concrete evidence.”

## Validate

Requires Python 3.9+ and no third-party packages:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Accuracy note

DeepSeek model names, aliases, endpoints, features, context limits, and pricing can change. This repository deliberately avoids pinning unverified model IDs or limits. Check DeepSeek's official documentation and live model list before implementation or deployment. The consumer web/mobile product is distinct from the developer API; this skill does not claim that consumer chats or app sessions can be embedded or controlled by third-party apps.

## References

- [DeepSeek API documentation](https://api-docs.deepseek.com/)
- [DeepSeek API platform](https://platform.deepseek.com/)
- [DeepSeek consumer chat](https://chat.deepseek.com/)
- [Agent Skills specification](https://agentskills.io/)

## License

MIT. See [`LICENSE`](LICENSE).

# Coding task playbooks

Use the relevant checklist; don't apply every section to every task. Read project-specific guidance and inspect existing patterns first.

## Feature implementation

1. Convert the request into acceptance criteria and identify non-goals.
2. Trace the existing entry point, data flow, interfaces, and tests.
3. Choose the simplest design compatible with the codebase; note any public-contract or migration impact.
4. Implement a vertical slice, including validation and failure behavior.
5. Add focused tests for normal, boundary, and failure cases.
6. Update documentation/examples if behavior or setup changed.
7. Run focused checks and inspect the diff.

## Bug fix

1. Capture the exact symptom, inputs, environment, and reproducibility.
2. Locate the first incorrect state/assumption using logs, tests, and call flow.
3. Distinguish root cause from downstream symptoms; don't patch only the visible symptom.
4. Add a regression test that fails before the fix where practical.
5. Make the narrow fix; check nearby callers and error paths.
6. Run regression and relevant suite; report any environment gap.

## Code review

- Review the diff and relevant surrounding code, not just commit messages.
- Prioritize exploitable/security-relevant defects, data loss, incorrect behavior, compatibility breaks, and missing coverage.
- For each finding, state severity, exact location, triggering conditions, impact, and a concrete recommendation.
- Report only actionable issues supported by evidence; distinguish a concern from a confirmed defect.
- Mention scope/coverage limitations. If no findings are substantiated, say so plainly.

## Refactoring

- State the behavior/invariants that must remain unchanged.
- Locate callers and tests before altering interfaces.
- Prefer mechanical, incremental edits; avoid combining cleanup with feature changes.
- Run behavior tests before/after when practical; compare outputs for transformations.
- Document any intentional compatibility break or migration.

## Frontend/product UI

Read [`frontend-quality.md`](frontend-quality.md). Identify the framework, design system, assets, routes, and existing interaction patterns before introducing new UI.

## Backend and services

- Trace request -> validation/auth -> business logic -> persistence/external dependency -> response.
- Validate input at boundaries; centralize domain rules rather than duplicating them in handlers.
- Handle timeouts, cancellation, retries, idempotency, rate limits, and partial failures where relevant.
- Avoid leaking internal exceptions, credentials, or personal data in responses/logs.
- Test success, validation, authorization, dependency failure, and duplicate/retry cases as appropriate.

## API design and integration

- Check existing versioning, naming, error format, authentication, and compatibility conventions.
- Define request/response and error behavior; validate payloads and size limits.
- Avoid breaking changes without an explicit migration path.
- Do not guess provider SDK methods, endpoints, or model identifiers; consult version-specific official docs.
- Test serialization, parsing, errors, timeouts, and any streaming/tool-call round trip.

## Database and data work

- Inspect schema, indexes, constraints, ORM conventions, and migration history first.
- Preserve data; migrations should be explicit, reversible where feasible, and safe for deployment order.
- Consider nullability, uniqueness, concurrency, pagination, query plans, and transaction boundaries.
- Never run destructive production queries or migrations without authorization and backup/rollback planning.
- Test migrations and boundary cases against an appropriate non-production environment.

## Tests and documentation

Use [`testing-debugging.md`](testing-debugging.md). Tests should encode behavior, not mirror implementation details. Keep docs/examples synchronized with the actual command, configuration, and version.

## Build/release/operations

- Inspect CI and deployment workflows; don't assume local commands match production.
- Prefer reproducible builds, pinned/declared dependencies, least-privilege credentials, and observable failure states.
- Explain rollout, migration, rollback, and monitoring implications for production-facing changes.
- Do not deploy, publish, rotate credentials, or change infrastructure unless asked and authorized.

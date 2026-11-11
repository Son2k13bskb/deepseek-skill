# Testing and debugging playbook

## Choose the right check

- Unit test: isolated behavior and boundaries.
- Integration test: component/service/database/provider interaction.
- End-to-end test: critical user workflow across system boundaries.
- Static analysis/typecheck/lint: structural and maintainability issues.
- Build/package check: compilation and artifact wiring.

Prefer the narrowest check that gives meaningful evidence; broaden after a focused pass.

## Diagnose failures

1. Capture the complete error, command, environment, and expected versus actual behavior.
2. Reproduce with the smallest deterministic case.
3. Read the stack trace from the first relevant application frame and trace inputs/state backward.
4. Compare a working path or recent change when available.
5. Form a falsifiable root-cause hypothesis and run a test that can distinguish it from alternatives.
6. Fix the cause, add regression coverage, and rerun the reproducer plus related checks.

Do not treat correlation, a single log line, or a plausible guess as proof. Do not suppress exceptions or weaken assertions merely to make a test green.

## Test design

- Assert public behavior and meaningful outcomes, not private implementation details.
- Include representative valid, invalid, boundary, empty, and failure cases.
- Make tests deterministic: control clocks, randomness, network dependencies, and concurrency as needed.
- Use fakes/mocks at genuine boundaries; avoid mocking the behavior under test.
- Keep fixtures minimal and explain non-obvious setup.
- For bug fixes, ensure regression coverage fails on the old behavior and passes on the fix when feasible.

## If checks fail or cannot run

- Preserve the original failure details and distinguish pre-existing failures from changes introduced by the patch.
- Report exact command and outcome, including skipped checks.
- If the environment lacks a dependency/service, state that explicitly and give the next reproducible command or setup step.
- Never claim the whole suite passes after running only one test.

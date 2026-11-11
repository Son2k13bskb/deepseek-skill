# Language and framework-aware implementation

This guide prevents language-agnostic advice from becoming guessed syntax. Always inspect the repository's manifests, lockfiles, runtime/toolchain configuration, and existing examples first. Match the project's versions and idioms.

## General rules

- Use the formatter, linter, typechecker, and test runner already configured by the project.
- Prefer standard-library or existing dependencies unless a new dependency is justified.
- Follow local error handling, logging, naming, module, and async patterns.
- Check ownership/lifetime, concurrency, encoding, time zones, numeric precision, and resource cleanup where relevant.
- Do not claim a snippet compiles unless it was compiled against the relevant versions or carefully label it unverified.

## Common ecosystem prompts/checks

### Python

Inspect `pyproject.toml`, `requirements*.txt`, lockfiles, supported Python version, and test setup. Follow project typing/style. Consider context managers, explicit exceptions, path handling with `pathlib`, and deterministic tests. Don't add a dependency just for a trivial helper.

### JavaScript / TypeScript

Inspect `package.json`, lockfile, `tsconfig`, module system, runtime, and framework version. Preserve package-manager choice. Handle rejected promises and cancellation; validate data at runtime even when TypeScript types exist. Check client/server boundaries and avoid shipping secrets to browser code.

### Go

Inspect `go.mod` and toolchain. Follow package boundaries, explicit error handling, context cancellation/timeouts, and idiomatic tests. Avoid ignored errors and unbounded goroutines; run focused `go test`/vet commands as configured.

### Rust

Inspect `Cargo.toml`, edition, features, and MSRV. Preserve ownership and error types; avoid unnecessary clones and panics in recoverable paths. Run formatter, clippy, and tests if configured and feasible.

### Java / Kotlin

Inspect build files, JDK/toolchain, framework versions, nullability, and test configuration. Follow existing dependency injection and exception patterns. Avoid blocking asynchronous/reactive paths and preserve transaction boundaries.

### C# / .NET

Inspect target frameworks, SDK settings, nullable configuration, package versions, and solution structure. Follow async cancellation and disposal conventions; avoid sync-over-async. Run the solution's targeted build/tests.

### SQL

Inspect the target dialect, schema, constraints, migration framework, and query plans. Parameterize values, preserve transaction semantics, and avoid dialect assumptions. Test data changes on a safe non-production dataset.

### Shell / infrastructure configuration

Inspect the target shell/runtime and CI/deployment conventions. Quote variables, check command failures, avoid leaking secrets, and make changes idempotent where possible. Do not execute destructive or production operations without explicit authorization.

## Framework-specific APIs

For fast-moving frameworks and SDKs, use the installed version's type definitions, local docs, lockfile, and official maintained documentation. Do not import a familiar API from another version or provider without checking.

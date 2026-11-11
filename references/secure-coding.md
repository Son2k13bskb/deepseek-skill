# Defensive secure-coding checklist

Use for authorized development, threat review, and remediation. This is a general defensive checklist, not a substitute for project-specific security review or legal requirements.

## Boundaries and data

- Validate and normalize untrusted input at the boundary; use allowlists and typed schemas where appropriate.
- Apply authorization on the server for every sensitive operation; do not trust UI visibility or model-generated intent.
- Use parameterized database queries and context-aware output encoding; avoid constructing executable queries/markup from untrusted strings.
- Restrict file paths to intended roots; avoid unsafe archive extraction, symlink traversal, and path confusion.
- Minimize sensitive data collection, retention, logging, and prompt exposure.

## Identity and secrets

- Store secrets in a managed secret store or protected environment configuration; never commit them or place them in client-side bundles.
- Use least privilege, short-lived credentials where available, and rotation/revocation procedures.
- Protect authentication/session flows with established framework mechanisms; avoid custom cryptography.
- Redact credentials, tokens, personal data, and sensitive payloads from logs and error responses.

## Reliability and abuse resistance

- Bound input sizes, execution time, concurrency, pagination, and resource use.
- Apply appropriate rate limits and safe retry/idempotency behavior.
- Return generic external errors while retaining useful, redacted internal diagnostics.
- Keep dependencies maintained; inspect provenance and upgrade advisories before adding packages.
- Make authorization, validation, and error paths testable; add regression tests for remediations.

## Review and response

- Confirm scope and environment are authorized; do not probe unrelated systems or access data beyond the task.
- Describe a finding with evidence, impact, preconditions, and a safe fix.
- Don't claim a system is secure based on a checklist or limited test. State review limits and recommend qualified assessment for high-risk systems.

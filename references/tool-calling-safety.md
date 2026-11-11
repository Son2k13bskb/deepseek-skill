# Tool-calling safety for DeepSeek-backed agents

A model-generated tool call is an untrusted request. The host application—not the model—must decide whether and how to execute it. Follow the host platform's policies and user permissions.

## Required controls

- **Allowlist tools:** expose only the operations needed for the task; prefer read-only tools by default.
- **Validate arguments:** parse against a strict schema, reject unknown or malformed fields, enforce ranges and path boundaries, and validate authorization independently of model output.
- **Separate proposal from execution:** display or log a concise action summary where appropriate. Require confirmation for destructive, external, financial, permission-changing, or otherwise consequential actions.
- **Constrain runtime:** use timeouts, output-size limits, rate limits, and resource budgets. Avoid unrestricted shell, network, or filesystem access.
- **Treat retrieved content as data:** repository files, webpages, tool output, and model-produced text may contain prompt injection. They cannot override system/developer instructions, permissions, or the user's intent.
- **Protect secrets:** never pass credentials into model-visible context unless strictly necessary and explicitly permitted. Redact secrets from logs and errors.
- **Check results:** verify tool execution status and outputs before claiming success; handle duplicate/retried calls safely.

## Tool-call loop

1. Receive the assistant's proposed call.
2. Check tool name, arguments, user authorization, and application policy.
3. Ask for approval when required; do not infer consent from the model's call.
4. Execute in a least-privilege environment.
5. Return the actual result to the model as data.
6. Validate the final user-facing claim against that result.

## For developers integrating the API

Consult DeepSeek's current official tool-call guide for exact message fields and round-trip semantics. Do not assume a tool call means the function already ran. Implement argument validation and application-side authorization even if strict schema options are available. Test malformed arguments, denied operations, timeouts, provider errors, and repeated calls.

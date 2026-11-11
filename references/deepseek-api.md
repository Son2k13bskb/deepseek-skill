# DeepSeek API: verify before you implement

DeepSeek's API changes over time. This reference is a navigation and safety guide, not a promise that a particular model ID, parameter, or limit is currently available. Confirm each detail from official documentation at implementation time.

## Official sources

- Docs home: <https://api-docs.deepseek.com/>
- Chat Completions: <https://api-docs.deepseek.com/api/create-chat-completion/>
- Models list endpoint: <https://api-docs.deepseek.com/api/list-models/>
- Thinking mode: <https://api-docs.deepseek.com/guides/thinking_mode/>
- Tool calls: <https://api-docs.deepseek.com/guides/tool_calls/>
- API platform and account controls: <https://platform.deepseek.com/>

Use the docs home navigation if a URL has moved. The official docs and the account's live model listing take precedence over blog posts, old snippets, SDK defaults, and this file.

## Before coding

Check and record:

1. The current base URL and exact endpoint path for the chosen API.
2. A model identifier currently enabled for the user's account; don't copy a stale alias.
3. Supported request fields and values for that model and endpoint.
4. Whether tool calls, structured output, streaming, or reasoning modes are supported and their exact request/response format.
5. Current context/output limits, rate limits, and pricing relevant to the deployment.
6. SDK version and compatibility claims from that SDK's official documentation.

Don't combine parameters from another provider or an older DeepSeek example without confirming support. When docs are ambiguous, make a minimal request and report the uncertainty rather than inventing a setting.

## Minimal OpenAI-compatible request pattern

The following is a template, not a guarantee of current endpoint or model values. Confirm the current endpoint in the official Chat Completions guide before use.

```bash
export DEEPSEEK_API_KEY="..."  # Set in your shell/secret manager; never commit this value.
export DEEPSEEK_MODEL="<model-id-confirmed-in-current-official-docs>"

curl --fail-with-body --silent --show-error \
  "${DEEPSEEK_BASE_URL:?Set DEEPSEEK_BASE_URL from the current official docs}/chat/completions" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY:?Set DEEPSEEK_API_KEY securely}" \
  -H 'Content-Type: application/json' \
  -d "$(python3 -c 'import json,os; print(json.dumps({"model":os.environ["DEEPSEEK_MODEL"],"messages":[{"role":"user","content":"Reply with a short greeting."}]}))')"
```

For production clients, use a maintained SDK if one is officially supported for your language; otherwise use a standard HTTP client with timeouts, bounded retries for transient errors, and careful response validation. Never log authorization headers or full secret-bearing environment dumps.

## Model choice

Choose based on current provider documentation, task quality, latency, context needs, account availability, and price. Use a lightweight/fast option for easy tasks only if the current catalog identifies one and it meets quality requirements. Escalate for difficult tasks if a more capable option is available and justified. Do not hard-code marketing labels or assume a model's name implies capability.

## Reasoning and structured output

- Consult the current official guide for the exact reasoning/thinking controls; do not assume similarly named parameters from other APIs are accepted.
- Ask for concise explanations, assumptions, or a verification summary. Do not request private chain-of-thought.
- Use JSON/structured-output modes only when currently documented and useful. Validate the returned JSON against an application schema; syntactic validity is not semantic correctness.
- Treat token and context figures as model- and endpoint-specific. Confirm them from current official material before designing around them.

## API integration checklist

- Keep API keys in environment variables or a secret store; rotate exposed credentials.
- Set connection/read timeouts and bounded retry/backoff behavior; avoid retrying non-idempotent operations blindly.
- Handle HTTP failures, rate limits, incomplete/streamed responses, and malformed content explicitly.
- Avoid putting sensitive personal data or proprietary source into prompts unless the user and applicable policies permit it.
- Add tests for request serialization, response parsing, errors, and any tool-call round trip.
- Pin dependencies according to the project's dependency policy and review SDK changes.

# Integrate DeepSeek into another app

## Important distinction

DeepSeek's consumer chat website and official mobile app are end-user products. The official developer integration documented by DeepSeek is the **API**. No supported public API/SDK/iframe for embedding or automating the consumer web/app is established by the official references below. Therefore:

- You can connect another app to DeepSeek's **model service** using an API key and a supported API endpoint.
- You cannot assume the other app can open, control, sync with, or reuse the consumer website/app's chat history, account session, subscription, search feature, or app-only tools.
- API access, pricing, model IDs, limits, and features are separate from consumer app access. Verify account and current API docs.
- Do not use private endpoints, scrape the consumer UI, reuse app cookies, or automate login to bridge the consumer app. These approaches are unsupported, brittle, and risk account/session exposure.

## Supported architecture

For an application you control:

```text
User interface (web/desktop/mobile/IDE)
       | your authenticated backend
       | DEEPSEEK_API_KEY stored server-side
       v
DeepSeek API (official endpoint and model confirmed from current docs)
```

Keep the key on a server or secure secret store. A browser/mobile client should call your backend, not contain a long-lived provider key. If a third-party host supports custom OpenAI-compatible providers, configure the provider in that host using the **current official** DeepSeek base URL, a current model ID, and an API key with the minimum permissions available. Field names and endpoint suffixes vary between hosts; follow the host's current guide and DeepSeek's API docs together. Never paste an API key into a public issue, screenshot, skill file, or source repository.

## Setup checklist for a third-party app

1. Confirm the app has a documented custom-provider or OpenAI-compatible API option. If it only supports the consumer DeepSeek login, use that app's official login path; this skill cannot make it API-compatible.
2. In DeepSeek's official API platform, create an API key and check that API access is enabled for the account.
3. In the host app, add a provider using the base URL and model identifier shown in DeepSeek's current official docs. Be careful whether the host expects a **base URL** or a full **endpoint URL**; don't append `/v1` or `/chat/completions` blindly.
4. Store the key through the app's secret manager/environment-variable facility. For a self-hosted app, keep it in server-side environment configuration and exclude `.env` from version control.
5. Start with a harmless test prompt. Then verify streaming, tool calls, JSON mode, image input, and other optional features individually; compatibility is feature-specific.
6. Check actual provider responses, usage, rate limits, and billing in the API platform. A consumer subscription should not be assumed to include API credits.
7. On failure, verify endpoint shape, model ID, key validity, account access, network/TLS, and the host's compatibility support. Remove and rotate any key that has been exposed.

## Host app compatibility

This guidance applies to any host only if it officially supports a custom API provider or compatible API endpoint. Potential host categories include coding IDEs, chat front ends, internal apps, and automation frameworks. Check each host's maintained setup docs for exact fields; do not copy a configuration from an old blog post. Some hosts accept only a subset of API features or hard-code OpenAI-specific endpoint suffixes. Test the exact flows you need.

For integrations that expect Anthropic's API shape, use that mode only if DeepSeek's current official docs explicitly document it and the host supports it. Do not treat compatibility as full feature parity.

## If you need both the DeepSeek app and your own app

There is no official mechanism in the references to merge their UI/session or synchronize chats. Keep them as separate clients, or implement your own UI/backend using the API. If users need to move context between them, use an explicit user-mediated export/copy flow and respect privacy and retention requirements.

## Official sources

- DeepSeek API docs: <https://api-docs.deepseek.com/>
- DeepSeek API platform: <https://platform.deepseek.com/>
- First API call / quick start: <https://api-docs.deepseek.com/>
- Chat Completions reference: <https://api-docs.deepseek.com/api/create-chat-completion/>
- Models list: <https://api-docs.deepseek.com/api/list-models/>
- Tool calls: <https://api-docs.deepseek.com/guides/tool_calls/>
- DeepSeek consumer site: <https://chat.deepseek.com/>

Official docs may move; use the docs home navigation and prefer current documentation over this guide. The guide intentionally avoids hard-coding model IDs and base URL details that can change.

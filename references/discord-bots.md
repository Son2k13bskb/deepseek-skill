# Discord bot engineering: commands, interactions, Components V2, and polish

Use this guide for building or improving Discord bots. Treat Discord as a constrained interaction surface, not a web page: messages are compact, users act in context, platform limits matter, and each interaction has a lifecycle. The target is a useful, attractive, dependable bot—not a wall of embeds or a collection of decorative buttons.

## 1. Inspect before choosing an approach

- Read repository instructions, dependency manifests/lockfiles, existing command and event handlers, registration scripts, persistence layer, tests, and deployment setup.
- Identify the actual language, framework, and installed Discord library version. Do not copy examples written for a different major version.
- Determine whether the project uses Gateway events, interactions/webhooks, or both; inspect configured intents, scopes, permissions, sharding, and environment variables.
- Check current official Discord docs and the installed library's documentation for the features involved. Discord API features and library support evolve independently.
- Preserve existing architecture and command registration conventions. Avoid broad rewrites just to introduce a preferred framework.

## 2. Choose the command surface intentionally

Prefer application commands for discoverable, user-facing bot features, but do not blindly convert every interaction into a slash command. Choose by user intent, context, privacy, discoverability, and compatibility:

| Use case | Good default | Why |
| --- | --- | --- |
| Public action with named options or validation | Slash/application command | Discoverable, typed options, permission controls, and structured input |
| Action on a selected user or message | User/message context-menu command when suitable | Operates directly on the selected Discord object |
| Multi-step workflow or follow-up choice | Slash command followed by buttons/selects/modals | Keeps the entry point discoverable and the flow interactive |
| Quick navigation within an existing interactive message | Button or select component | The user is continuing an already visible flow |
| Existing community bot with an established prefix convention | Prefix command only when intentional | Familiarity/backward compatibility; requires message parsing and often additional message-content access |
| Owner-only local development or migration compatibility | Prefix command may be reasonable | Private operational use; restrict it and document why it remains |
| Passive event response (e.g. join/leave automation) | Gateway event, not a command | No user-invoked command is needed |

For new public features, start with application commands unless the product context gives a clear reason otherwise. Prefix commands can require privileged message content access depending on implementation and current platform rules; verify this before enabling intents. Never request broad privileged intents “just in case.”

Do not implement duplicate slash and prefix entry points without a concrete compatibility requirement. If both are needed, share one validated domain/service function and keep command adapters thin. Register commands using the project's intended deployment process; avoid destructive global bulk-overwrite behavior or deployment side effects without authorization.

## 3. Design Components V2 as a real message UI

Components V2 is a Discord message-component system, not a new theme. Verify current official component reference, message flags, feature support, and library version before implementation. Do not rely on old examples or guessed builder names.

- Use V2 when a message benefits from structured text, sections, media, separators, containers, or integrated controls. A conventional embed or plain message may be clearer for a short notification.
- Build a visual hierarchy: concise title/context, grouped details, clear primary action, and restrained secondary actions. Use spacing and grouping instead of repetitive boxes and decorative noise.
- Choose components for their interaction semantics: buttons for discrete actions, selects for choosing among options, and modals for focused multi-field input when supported and appropriate.
- Give controls specific, unambiguous labels and visible outcomes. Avoid “click here,” vague emoji-only buttons, excessive component rows, and controls that do nothing.
- Keep component identifiers stable enough for routing and within current platform constraints. Do not encode secrets or trust user-provided identifiers as authorization.
- Use supported content/media components deliberately. Handle attachment visibility and message flags according to current documentation.
- Make long or complex content scannable; put essential information first and provide a clear fallback when content or components cannot be rendered.
- Respect current component/message limits, nesting rules, supported contexts, and library support. Never assume a limit from a stale tutorial.

## 4. Model the interaction lifecycle and logic

For each command or component interaction, define the lifecycle before coding:

1. Parse and validate input at the boundary.
2. Check permissions, ownership, context, and business rules.
3. Acknowledge/defer or respond within the platform's current interaction deadline.
4. Run work with bounded timeouts and handle expected dependency failures.
5. Send/update the intended response and component state.
6. Handle repeat clicks, stale/expired controls, cancellation, and duplicate requests safely.

Use the library's correct response/defer/follow-up API for its installed version. Avoid responding twice to one interaction, leaving it unacknowledged, or assuming a deferred response can be edited in any context. Keep long-running work asynchronous and report progress appropriately.

- Decide whether a response should be public or private based on the user's task and audience, not convenience. Verify current terminology and behavior for private interaction responses in platform docs/library versions.
- Revalidate authorization when a component is clicked; the fact that a user can see a message does not grant permission to perform its action.
- Bind sensitive or user-specific controls to the intended user, guild, channel, and resource. Fail safely when the message or stored state is missing.
- Disable, update, or otherwise make completed actions visibly complete where appropriate. Ensure duplicate clicks cannot duplicate charges, grants, or destructive operations.
- Separate command parsing/interaction adapters from business logic so the same behavior is testable and reusable.

## 5. Permissions, intents, and security

- Request the minimum OAuth scopes, bot permissions, and Gateway intents required by actual features. Explain setup changes to the user.
- Check actor permissions and bot permissions separately. Handle missing permissions with a useful, non-sensitive response.
- Treat every message, interaction option, attachment, component custom ID, and database value as untrusted input.
- Keep bot tokens and API keys in environment/secret storage; never commit them or print them in logs. Provide a safe `.env.example` with names only.
- Avoid unsafe mention behavior: restrict allowed mentions where user-generated content or relayed text could ping roles/everyone.
- Add authorization checks for admin/moderation actions, and log security-relevant actions without exposing secrets or unnecessary personal data.
- Handle rate limits through the supported library/API mechanisms; do not build tight retry loops or circumvent platform limits.

## 6. Reliability and maintainability

- Keep event handlers fast; use queues/background work for tasks that exceed interaction budgets.
- Handle reconnects, shutdown, persistence, and partial external-service failures according to the current architecture.
- Use idempotency or deduplication for repeatable operations such as rewards, purchases, and provisioning.
- Use structured logs with correlation context; avoid logging full interaction payloads or credentials.
- Do not introduce a database, cache, scheduler, or framework unless the feature needs it and the repo does not already provide one.
- For deployments, check command sync, environment configuration, migrations, permissions, and rollback implications. Do not deploy or alter live guilds unless explicitly authorized.

## 7. Make the bot feel polished, not mechanical

- Match the server's tone and the feature's seriousness; use concise, natural copy rather than repeated robotic templates.
- Use a consistent naming, color, icon, and formatting vocabulary. Avoid emoji on every line, giant headers, redundant status text, and noisy dividers.
- Put the actionable information first. Make success, warning, and failure messages distinguishable with words and structure, not color alone.
- Give errors a helpful next step without leaking stack traces, IDs, internal paths, or implementation details.
- Personalize only with relevant context; do not fabricate user data or expose private data in public channels.
- Prefer one coherent message with a clear primary action over multiple fragmented notifications. Edit the existing interaction response for progress when that is the right UX.

## 8. Test and verify

- Unit-test domain logic independently of Discord objects where possible.
- Test command input validation, permission denial, normal success, dependency failure, duplicate interactions, stale controls, and response/defer behavior.
- Test command registration/serialization using project tooling without syncing to production by default.
- Verify Components V2 payloads/builders against the installed library version and current official docs; use available integration or sandbox tests for platform-specific behavior.
- Check the bot startup path, required environment variables, intents, permissions, and deployment instructions.
- Report which checks ran. Do not claim a live Discord interaction was verified if only unit tests or static checks ran.

## Decision checklist

Before implementing a bot feature, answer:

- What user task does it support, and who can invoke it?
- Is the right entry point slash, context menu, component, event, or an intentional legacy prefix command?
- What data and permissions are required, and what is the least privilege needed?
- What response should the user see on success, validation failure, permission denial, timeout, and repeat action?
- Does this need Components V2, or would a simpler message/embed be clearer?
- Which tests prove the behavior, and what platform behavior still needs a sandbox/live check?

## Prompt template

> Inspect this bot's instructions, framework/library version, command/event architecture, intents, permissions, and tests first. Implement **[feature]** for **[user/context]**. Choose slash, context-menu, component, event, or prefix entry points based on the use case (explain any prefix choice). Use Components V2 only if it improves the actual message workflow; verify current official docs and library support. Implement permission checks, interaction acknowledgment, error/repeat handling, tests, and clear deployment notes. Do not sync commands or modify a live server unless asked.

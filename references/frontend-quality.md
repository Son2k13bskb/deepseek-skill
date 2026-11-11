# Frontend quality checklist

Use for web/mobile UI implementation and review. First inspect the app's framework, routing, styling system, components, assets, and supported browsers/devices. Reuse local conventions; don't add a framework or design system casually.

## Design before markup

- Identify the user's primary task and make the page hierarchy serve it.
- Use existing tokens, typography, spacing, components, and icon sources when available.
- Give visual decisions a coherent rationale; avoid generic layouts, arbitrary gradients, excessive cards, and decorative elements that reduce clarity.
- Use real project assets where available; do not invent URLs for assets or introduce inaccessible remote dependencies.

## Interaction and states

- Make every visible control do what its label promises; support keyboard operation and visible focus.
- Include loading, success, empty, error, disabled, and validation states where relevant.
- Preserve form values on recoverable errors; explain how to fix invalid input.
- Confirm before destructive actions and provide undo or recovery when appropriate.
- Prevent duplicate submissions and communicate progress for long operations.

## Responsive and accessible behavior

- Check narrow and wide layouts; avoid horizontal overflow and inaccessible clipped content.
- Use semantic elements and headings in a logical order; label fields and expose errors to assistive technology.
- Provide text alternatives for meaningful images; hide decorative images from assistive technology.
- Ensure sufficient contrast, visible focus, target sizes, and reduced-motion behavior.
- Don't rely on color, hover, or animation alone to communicate information.

## Implementation quality

- Keep state ownership clear and avoid unnecessary global state or effects.
- Validate on both client and server for security-sensitive inputs.
- Handle async cancellation/races and stale responses where relevant.
- Avoid unsafe HTML injection; sanitize any intentionally rendered user content.
- Use project-supported image/font formats and optimize large assets.

## Verification

- Run the project's lint/typecheck/tests/build, not guessed commands.
- Use existing browser/device tests if available; otherwise inspect the key flows manually with available tools.
- Test the primary path, keyboard path, responsive layout, and at least one failure/empty state.
- Report what was actually checked; don't claim browser validation without running it.

# Frontend quality: visual design, interaction, and implementation

Use this guide for websites, web apps, dashboards, landing pages, and UI reviews. The goal is a coherent, attractive, usable interface that works in the project's actual environment—not merely plausible markup or a static mockup. Do not promise that a design is beautiful; make specific visual and behavioral decisions and verify what the available tools allow.

## 1. Understand the product before designing

- Inspect the repository instructions, framework and version, routes, existing pages/components, styling system, assets, fonts, package scripts, and tests before editing. Follow existing conventions unless the request calls for a redesign.
- Identify the intended user, the page's main purpose, the primary action, and the information the user needs to act. Turn the request into observable UI and behavior criteria.
- Determine whether this is a marketing page, content site, dashboard, editor, form flow, or another product surface. Choose structure and visual treatment to fit that purpose; do not turn every page into a dashboard or a slide deck.
- If a key product choice is genuinely blocking, ask one focused question. Otherwise make a reasonable, reversible choice and mention it briefly.

## 2. Make deliberate visual decisions

Before building components, form a small design direction based on the product and any supplied brand references:

- Define a clear hierarchy: one primary page heading, concise supporting context, a visually obvious main action, and grouped content in order of importance.
- Choose a restrained, coordinated palette with semantic roles (page/background, surface, text, muted text, border, primary action, success, warning, error). Verify readable contrast; do not use color alone to convey meaning.
- Establish a consistent type scale, font weights, line heights, spacing rhythm, content width, alignment, and responsive breakpoints. Use project-provided fonts/assets when available; avoid adding dependencies or remote font requests without need.
- Use layout, whitespace, typography, and relevant imagery to create visual interest. Use cards only when grouping or interaction warrants them. Avoid defaulting to piles of cards, arbitrary gradients, giant empty hero areas, random iconography, excessive shadows, or decoration that competes with the task.
- Use icons from the project's existing library and pair unfamiliar icons with accessible names or visible labels. Do not substitute emoji for product icons.
- Keep the design consistent across states and related screens. Reuse existing tokens/components; when none exist, define a small coherent set rather than styling every element independently.
- Use real project assets where available. Do not invent asset paths or URLs, hotlink arbitrary images, or make the core experience depend on a remote service. If appropriate imagery is unavailable, use a deliberate CSS/layout treatment rather than broken placeholders.

## 3. Implement sound HTML and UI logic

- Use semantic HTML landmarks and elements: `header`, `nav`, `main`, `section`, `footer`, headings in order, lists for collections, and tables for tabular data when appropriate.
- Use links for navigation and buttons for actions. Use native form controls where suitable; provide persistent labels, useful input types, validation, and error text associated with the relevant field. Do not use clickable `div`s when a button or link is correct.
- Trace each interaction through its real state change: what triggers it, what data changes, what the user sees next, and what happens on failure or repeat. Keep state ownership and data flow aligned with the project's architecture.
- Every visible control must work as labeled. Wire it to real application behavior where present; do not ship dead buttons, fake links, inert search, or decorative form submissions. If backend behavior is outside scope, communicate the limitation honestly and avoid pretending data was saved.
- Model meaningful states, as applicable: initial/loading, populated, empty, validation error, request failure, success, disabled, and pending. Preserve user input on recoverable errors, prevent accidental duplicate submissions, and provide progress or recovery guidance for longer actions.
- Use existing routing, APIs, persistence, authentication, and error handling. Do not invent endpoints, hard-code pretend user data as if live, or silently change the product contract.
- Avoid unsafe HTML injection. Sanitize intentionally rendered user content and validate security-sensitive data on the server as well as the client.

## 4. Support all users and screen sizes

- Make layouts adapt to narrow and wide viewports: reflow columns, navigation, controls, typography, and media; prevent horizontal overflow and clipped essential content.
- Ensure the main task works with keyboard alone. Preserve a logical tab order, visible focus, meaningful accessible names, and appropriate focus handling for dialogs and dynamic updates.
- Set accessible names and text alternatives; use `alt=""` for decorative images. Associate help and error text with form controls and expose important status changes to assistive technology.
- Respect reduced-motion preferences. Avoid flashing, forced motion, hover-only actions, and color-only distinctions. Check contrast and comfortable target sizes.
- Prefer native browser semantics and progressive enhancement where practical; do not add ARIA that conflicts with native behavior.

## 5. Respect local hosting and deployment context

- Inspect how the project is actually served: development/build scripts, router, base path, static asset handling, environment variables, API origin, and deployment target. Follow the configured workflow instead of guessing a host or replacing the build setup.
- Keep local development usable with the project's documented commands. Avoid absolute machine-specific paths, assumptions about a particular port, and unnecessary network/CDN dependencies.
- Use relative or framework-managed asset paths consistent with the app's base URL. Check direct navigation and refresh behavior for relevant routes, including subpath hosting if the project uses it.
- Keep secrets out of client code and public environment variables. Do not expose local files, internal endpoints, or debugging data in the UI.
- Do not claim a page works on localhost or in production unless you actually ran the relevant app/build or checks. Report unavailable browser, server, or deployment validation honestly.

## 6. Verify the experience

- Read package scripts and project docs; run the real lint, typecheck, tests, and build commands that apply. Do not invent commands or claim checks that were not run.
- Verify the primary user journey and important control behavior. Check loading/empty/error cases and form validation where applicable.
- Inspect narrow and wide layouts, keyboard navigation, focus visibility, semantic structure, and browser console/build errors using available tools. Use browser or screenshot tools only if they are available; distinguish actual visual inspection from source-level reasoning.
- Review the final diff for broken links/assets, placeholder content, dead controls, inconsistent styles, accidental dependencies, and regressions to existing routes.
- Report what was implemented and actually verified, plus any behavior requiring a backend, browser, or environment that was unavailable.

## UI implementation request template

> Inspect the existing app, its instructions, framework, routes, design conventions, and local run/build process first. Implement **[page/flow]** for **[user and goal]**. Make the interface visually coherent and polished with deliberate hierarchy, typography, spacing, palette, and responsive layout; use the existing design system and real assets. Implement working semantic HTML and the complete interaction/data states—do not leave dead controls or substitute a slide/mockup for the requested app. Preserve the project's local hosting and API conventions. Run the relevant checks and report what you actually verified.

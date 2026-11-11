# Repository-first coding workflow

Use this when asking DeepSeek or another coding agent to change a project.

## Prompt template

> Read the repository's contributor/agent instructions and inspect the relevant files and tests. The desired result is **[specific outcome]**. Preserve **[compatibility/style/security constraints]**. Identify the concrete evidence and smallest suitable plan, implement it, then run **[focused checks]**. Report the changed files, checks and their actual results, and any remaining risk. Do not invent APIs or claim unrun checks passed.

## Workflow

1. **Orient:** inspect status, project instructions, directory layout, and relevant entry points. Preserve user changes.
2. **Find evidence:** search symbols/references, read tests and callers, and reproduce the issue if practical. Separate observed facts from hypotheses.
3. **Plan:** choose a narrow change. For broad work, split into reviewable stages with explicit acceptance criteria.
4. **Edit:** follow local patterns, minimize unrelated churn, and add/update tests for externally visible behavior.
5. **Check:** run the smallest relevant test or static check, then broader checks when appropriate. Inspect the diff.
6. **Summarize:** say what changed, why, checks actually run, outcomes, and known gaps.

## Debugging prompt

> Reproduce or trace the failure using the supplied error and repository evidence. Identify the first relevant failing boundary, distinguish root cause from symptoms, and cite files/functions or test output. Make a minimal fix and add a regression test. If evidence is insufficient, list the next smallest diagnostic step instead of guessing.

## Review prompt

> Review this diff for correctness, regressions, security, and missing tests. Report only actionable findings, ordered by severity, with file/line evidence and a concrete impact. If no findings are supported by evidence, say so and note review limitations. Do not rewrite the change unless asked.

## Improve a weak response

Provide a specific correction signal: the missed file, failing test, unsupported assumption, expected output schema, or counterexample. Ask for a revised answer constrained by that evidence. Don't simply ask for “more detail.”

## Structured response option

When machine processing is needed, request a schema such as:

```json
{
  "summary": "string",
  "files_changed": ["string"],
  "checks": [{"command": "string", "result": "passed|failed|not_run", "notes": "string"}],
  "risks": ["string"]
}
```

Validate required fields and allowed values in the consumer. Do not use JSON mode just to make a normal conversational answer look formal.

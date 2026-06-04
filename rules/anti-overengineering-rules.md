# Anti-Overengineering Rules

Failure mode prevented:

The agent turns a small architecture task into a large framework, process, or
documentation system.

## Rules

1. Match output size to system complexity.
2. Do not introduce new abstractions without a specific problem.
3. Do not recommend architecture patterns just because they are common.
4. Do not create ADRs for obvious or temporary decisions.
5. Do not create separate files when one concise document is enough.
6. Do not convert every uncertainty into a blocking question.
7. Do not redesign existing structure unless redesign is requested or clearly justified.
8. Use fast-path output for small or low-risk tasks.

## Lean Default

For small projects, prefer:

- One architecture overview
- One module map
- One open questions list
- One AI handoff note

Add more only when the project has enough complexity to justify it.

## Full Package Threshold

Use a full output package when the work involves:

- Multiple modules
- Unclear system boundaries
- Persistence changes
- External integrations
- Payments or security
- Major workflow changes
- Future-agent handoff

Otherwise, prefer a compact architecture note that still separates facts,
inferences, assumptions, unknowns, risks, and decisions.

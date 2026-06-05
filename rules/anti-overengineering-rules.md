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

## Fast-Path Decision Tree

Start with fast-path when the request appears small, bounded, or exploratory.

Keep fast-path only when all are true:

- Scope is one narrow workflow, one small idea, or 1-2 modules.
- No persistence, integration, payment or billing, authentication,
  authorization, security, deployment, infrastructure, unclear boundary, or
  major workflow change is involved.
- No handoff-ready documentation was requested.

Promote to a full output package when any trigger is found:

- Persistence or database schema change
- External integration
- Payment or billing logic
- Authentication, authorization, or security boundary
- Deployment, infrastructure, or environment change
- Major workflow or business flow change
- Unclear ownership or module boundary
- 3+ modules with meaningful interaction
- Explicit future-agent handoff request

If uncertain, inspect narrowly first. Record what was checked, stay in
fast-path unless a real trigger is found, and do not promote because of
uncertainty alone.

## Lean Default

For small projects, prefer:

- One architecture overview
- One module map
- One open questions list
- One AI handoff note

Add more only when the project has enough complexity to justify it.

## Full Package Threshold

Use a full output package when the work involves:

- 3+ modules with meaningful interaction
- Unclear system boundaries
- Persistence changes
- External integrations
- Payment or billing logic
- Authentication, authorization, or security boundaries
- Deployment, infrastructure, or environment changes
- Major workflow or business flow changes
- Future-agent handoff

Otherwise, prefer a compact architecture note that still separates facts,
inferences, assumptions, unknowns, risks, and decisions.

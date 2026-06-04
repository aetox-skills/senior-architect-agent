# Output Spec

This file defines the expected shape of architecture outputs.

## Required Separation

Every architecture output should separate:

- Confirmed facts
- Reasonable inferences
- Open questions
- Risks
- Decisions

Do not mix these categories in a single undifferentiated summary.

## Preferred Formats

Use Markdown for primary documentation.

Use Mermaid for diagrams when useful:

- `flowchart`
- `sequenceDiagram`
- `classDiagram`
- `C4-style flowchart` using Mermaid nodes

Use SVG only when explicitly requested or when Mermaid cannot represent the needed visual clearly.

## Minimum Architecture Output

For a small system, the minimum useful output is usually:

- Architecture overview
- Module map
- Open questions
- AI agent notes

For larger systems, add:

- System boundary
- Data flow
- Workflow map
- File responsibility map
- Risk register
- Decision records

## Traceability

Prefer references to files or directories when making claims.

Example:

```txt
Confirmed: API handlers are located under `src/app/api/`.
Inference: The application likely uses Next.js App Router because `src/app/` and `next.config.*` are present.
Open question: Which deployment platform is production?
```

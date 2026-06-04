# Output Spec

This file defines the expected shape of architecture outputs.

## Required Separation

Every architecture output should separate the categories that apply:

- Confirmed architecture
- Confirmed facts
- Reasonable inferences
- Proposed architecture
- Assumptions
- Open questions
- Risks
- Decisions made
- Decisions requiring approval

Do not mix these categories in a single undifferentiated summary.

## Architecture Status Labels

Use these labels consistently:

- `Confirmed architecture`: Architecture observed in files, docs, or explicit
  user-provided system context.
- `Confirmed`: Supported by inspected files or explicit user-provided facts.
- `Inferred`: Reasonable from available evidence, but not directly confirmed.
- `Proposed`: Suggested architecture for review, not approved or implemented.
- `Assumed`: Temporary premise used to make progress.
- `Unknown`: Important information not yet available.
- `Requires approval`: A decision the user or owner must accept before work.

## Preferred Formats

Use Markdown for primary documentation.

Use Mermaid for diagrams when useful:

- `flowchart`
- `sequenceDiagram`
- `classDiagram`
- C4-style flowcharts using Mermaid nodes

SVG may be used as a visual artifact for presentation or review when a complex
architecture needs a clearer visual export. SVG must not replace Markdown and
Mermaid as the editable source of truth.

## Minimum Architecture Output

For a small existing system, the minimum useful output is usually:

- Architecture overview
- Module map
- Open questions
- AI agent notes

For larger existing systems, add:

- System boundary
- Data flow
- Workflow map
- File responsibility map
- Risk register
- Decision records

For a small raw idea, the minimum useful output is usually:

- Idea brief
- Architecture proposal
- Open questions
- AI agent notes

For larger ideas, add:

- Module proposal
- Workflow proposal
- Data model draft
- Decision options
- Risk register
- Mermaid diagram

## SVG Visual Artifact

When an output package benefits from SVG, include the generated artifact beside
the Mermaid source:

```txt
SVG Visual Artifact:
  Available at `diagram.svg`. Mermaid remains the editable source of truth.
```

Do not create an empty placeholder file. Keep generated artifacts beside the
Mermaid source.

## Traceability

Prefer references to files or directories when making claims.

Example:

```txt
Confirmed:
  API handlers are located under `src/app/api/`.
Inference:
  The application likely uses Next.js App Router because `src/app/` and
  `next.config.*` are present.
Open question:
  Which deployment platform is production?
```

Idea-mode example:

```txt
Confirmed:
  The user wants member discounts and payments.
Assumption:
  Members need accounts to receive discounts.
Proposed:
  Add a booking service, payment integration, and admin management module.
Requires approval:
  Whether coaches are bookable resources, service providers, or both.
```

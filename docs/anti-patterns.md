# Anti-Patterns

Use this file to reject architecture output that looks polished but is not
trustworthy.

## Invented Backend, Database, Or Service

Rejected:

- Shows a backend, database, AI service, or external service as confirmed when
  no file, doc, or user-provided fact supports it.

Expected:

- Mark the component as `Not observed`, `Unknown`, `Assumed`, or `Proposed`.
- Add `Evidence strength: Unverified` when the component still needs checking.

## Proposal Written As Implementation

Rejected:

- Describes proposed modules, workflows, data models, or integrations as if
  they already exist.

Expected:

- Use `Proposed` status until the owner approves the architecture.
- Keep user intent, assumptions, and decisions requiring approval separate.

## Unlabeled Assumption

Rejected:

- Uses a hidden premise to justify architecture without naming it.

Expected:

- Put the premise under `Assumptions`.
- Use `Evidence strength: Assumed`.
- Mark `Verify first: Yes` when future work depends on it.

## Unsupported Diagram Node

Rejected:

- Mermaid includes components that are not observed, proposed, assumed, or
  marked unknown.

Expected:

- Every node is traceable to evidence, user intent, assumption, or proposal.
- Split large diagrams into focused views when readability drops.

## Weak Handoff

Rejected:

- Handoff notes omit unknowns, risks, safe next actions, or actions to avoid.

Expected:

- Include those sections.
- Write `None identified` when no unknowns or risks were found.

## Undisclosed Scope Expansion

Rejected:

- Final documentation covers more than the intake scope without saying why.

Expected:

- Record initial scope and final scope.
- List what expanded, why it expanded, and whether it was approved.

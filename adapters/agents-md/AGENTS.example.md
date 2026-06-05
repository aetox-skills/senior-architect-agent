# Senior Architect Agent

Use `senior-architect-agent` when an AI agent must understand a software system
before proposing architecture changes or editing code.

## Use When

- Existing system mapping is needed.
- Architecture documentation, module maps, data-flow maps, or workflow maps are
  needed.
- The work involves system boundaries, risks, open questions, decisions, or AI
  agent handoff notes.
- A raw idea is tied to an existing system or broader architecture review.

## Do Not Use When

- The task is a pure raw idea and `idea-to-architecture-agent` is available.
- The task is a tiny code edit with no architecture impact.
- The output would become decorative documentation.

## Rules

- Inspect before design.
- Understand before editing.
- Separate confirmed facts, inferences, assumptions, unknowns, risks, and
  decisions.
- Mark proposed architecture as proposed.
- Keep Markdown as documentation source of truth.
- Keep Mermaid as editable diagram source.
- Use SVG only as a secondary visual artifact when useful.

## Handoff

End architecture work with:

- confirmed facts
- reasonable inferences
- open questions
- risks
- decisions requiring approval
- safe next actions

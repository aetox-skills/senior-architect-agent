# Diagram Rules

Failure mode prevented: The agent creates impressive-looking diagrams that are not traceable to the real system.

## Rules

1. Use Mermaid first.
2. Do not make SVG the source of truth.
3. Keep diagrams linked to inspected files or user-provided context.
4. Avoid decorative nodes.
5. Do not include technologies that were not observed or provided.
6. Split large diagrams instead of making unreadable all-in-one diagrams.
7. State what each diagram is intended to clarify.
8. For v1, document future SVG artifacts only when useful. Do not create `.svg`
   files.

## Diagram Types

Use:

- `flowchart` for boundaries, modules, and data flow.
- `sequenceDiagram` for request or workflow order.
- `classDiagram` only when relationships between domain types matter.

Avoid diagrams when text is clearer.

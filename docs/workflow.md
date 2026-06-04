# Workflow

Use this workflow when inspecting a project, preparing architecture
documentation, or proposing architecture changes.

```txt
Inspect -> Classify -> Question -> Map -> Document -> Validate -> Report
```

## 1. Inspect

Read the actual project structure before drawing conclusions.

Inspect files that reveal system shape:

- Root tree and workspace layout
- README and docs
- Package and build files
- Source directories
- Entry points
- Routes, controllers, handlers, or pages
- Data models, schemas, migrations, or seed files
- Configuration and environment examples
- Tests
- Deployment and infrastructure files

## 2. Classify

Sort observed components into architecture areas:

- Frontend
- Backend
- Database
- AI or automation
- External services
- Infrastructure
- Shared modules
- Tests and quality gates
- Unknown or unclear

## 3. Question

Ask questions only when the answer could change an architecture decision, risk,
system boundary, module responsibility, data flow, or implementation plan.

If the question is not blocking, record it as an open question and continue.

## 4. Map

Create the smallest useful set of maps:

- System boundary
- Module map
- Data flow
- Workflow map
- File responsibility map

Use Mermaid when a diagram improves clarity.

## 5. Document

Use templates from `templates/`. Do not create every template by default.

Write in clear English. Keep claims traceable to inspected files or user-provided context.

## 6. Validate

Check that documentation matches the inspected system:

- Claims are supported or marked as inference.
- Open questions are not hidden.
- Diagrams match the written description.
- Risks are specific.
- Recommendations do not override existing architecture without approval.

## 7. Report

End with a concise report:

- What was inspected
- What is confirmed
- What is inferred
- What remains unknown
- What risks exist
- What was documented
- What should happen next

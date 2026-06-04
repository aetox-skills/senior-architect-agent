# Workflow

Use this workflow when inspecting a project, preparing architecture
documentation, or turning a raw idea into a reviewable architecture proposal.

```txt
Intake
-> Select Mode
-> Inspect or Extract Idea
-> Classify
-> Question
-> Map
-> Document
-> Validate
-> Report
```

## 1. Intake

Read the user request and identify whether the input is:

- Existing project files, docs, configs, tests, or deployment artifacts
- A raw idea, product concept, feature request, or business/system goal
- A mix of existing system evidence and proposed future changes
- A narrow module, workflow, or whole-system scope

Do not start with an architecture conclusion.

Use the narrowest useful scope. Prefer module-level mapping when the user asks
about one module or workflow.

## 2. Select Mode

Start by selecting the operating mode.

Use Existing System Mapping Mode when files, code, docs, configs, tests, or
deployment artifacts exist. Read the actual project structure before drawing
conclusions.

Use Idea-to-Architecture Mode when only a raw idea, product concept, feature
request, or business/system goal exists.

If both exist, map the existing system first and label new architecture as
proposed.

## 3. Inspect or Extract Idea

Inspect files that reveal system shape when available:

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

Use available inspection tools such as file search, file tree inspection, git
history, validators, and Mermaid checks when they help. Treat their output as
evidence to interpret, not as architecture by itself.

For raw ideas, extract the user's intent, domain terms, constraints, user
types, feature list, and success goals.

In idea mode, do not present proposed architecture as existing architecture.

## 4. Classify

Sort observed or proposed components into architecture areas:

- Frontend
- Backend
- Database
- AI or background processes
- External services
- Infrastructure
- Shared modules
- Tests and quality gates
- Unknown or unclear

In Existing System Mapping Mode, mark missing categories as not observed.

In Idea-to-Architecture Mode, mark categories as proposed, assumed, unknown, or
out of scope.

## 5. Question

Ask questions only when the answer could change an architecture decision, risk,
system boundary, module responsibility, data flow, workflow, data model, or
implementation plan.

Existing systems are evidence-first: ask after inspecting what can be found.

Raw ideas are question-first: ask important questions before presenting a
proposal, then continue with explicit assumptions when safe.

## 6. Map

For existing systems, create the smallest useful set of maps:

- System boundary
- Module map
- Data flow
- Workflow map
- File responsibility map

For raw ideas, create the smallest useful proposal set:

- Idea brief
- Architecture proposal
- Module proposal
- Workflow proposal
- Data model draft
- Decision options

Use a fast path for small or low-risk work: produce a compact architecture note
instead of a full output package. Use a full package for multi-module work,
unclear boundaries, persistence, integrations, payments, security, major
workflow changes, or future-agent handoff.

Use Mermaid when a diagram improves clarity.

For large systems, split diagrams by purpose, such as boundary, module,
workflow, and data-flow views. Do not use one diagram when several focused
views would be clearer.

Create SVG visual artifacts only when they help presentation or review. Generate
SVG from Mermaid and keep Mermaid as the editable source of truth.

## 7. Document

Use templates from `templates/`. Do not create every template by default.

Write in clear English.

For existing systems, keep claims traceable to inspected files or user-provided
context.

For raw ideas, keep proposals traceable to user intent and explicit
assumptions.

## 8. Validate

Check that documentation matches the selected mode:

- Claims are supported or marked as inference.
- Proposed architecture is labeled as proposed.
- Assumptions are visible.
- Open questions are not hidden.
- Diagrams match the written description.
- Risks are specific.
- Recommendations do not override existing architecture without approval.

## 9. Report

End with a concise report:

- What was inspected
- What is confirmed
- What is inferred
- What is proposed
- What is assumed
- What remains unknown
- What risks exist
- What decisions require approval
- What was documented
- What should happen next

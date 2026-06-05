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

Gate before continuing:

- Operating mode is selected or narrowed to the likely mode.
- Initial scope is recorded.
- Fast-path or full-package output is chosen.

Fast-Path Decision Tree:

1. Start with fast-path when the request appears small, bounded, or
   exploratory.
2. Keep fast-path only when all are true:
   - Scope is one narrow workflow, one small idea, or 1-2 modules.
   - No persistence, integration, payment or billing, authentication,
     authorization, security, deployment, infrastructure, unclear boundary, or
     major workflow change is involved.
   - No handoff-ready documentation was requested.
3. Promote to full package when any trigger is found:
   - Persistence or database schema change.
   - External integration.
   - Payment or billing logic.
   - Authentication, authorization, or security boundary.
   - Deployment, infrastructure, or environment change.
   - Major workflow or business flow change.
   - Unclear ownership or module boundary.
   - 3+ modules with meaningful interaction.
   - Explicit future-agent handoff request.
4. If uncertain, inspect narrowly first and stay in fast-path unless a real
   trigger is found.

## 2. Select Mode

Start by selecting the operating mode.

Use Existing System Mapping Mode when files, code, docs, configs, tests, or
deployment artifacts exist. Read the actual project structure before drawing
conclusions.

Use Idea-to-Architecture Mode when only a raw idea, product concept, feature
request, or business/system goal exists.

If `$idea-to-architecture-agent` is available and the request is a pure raw
idea with no implementation context, prefer that sibling skill for the focused
proposal workflow.

If both exist, map the existing system first and label new architecture as
proposed.

Use `senior-architect-agent` when the work mixes existing evidence with new
proposals, needs broader architecture mapping, or requires boundary, risk, or
handoff analysis.

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

Gate before continuing:

- Evidence or user intent is recorded.
- Inspection limitations are named when something important cannot be verified.

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

Gate before continuing:

- Architecture areas are classified.
- Missing or unclear categories are explicitly marked.

## 5. Question

Ask questions only when the answer could change an architecture decision, risk,
system boundary, module responsibility, data flow, workflow, data model, or
implementation plan.

Existing systems are evidence-first: ask after inspecting what can be found.

Raw ideas are question-first: ask important questions before presenting a
proposal, then continue with explicit assumptions when safe.

Gate before continuing:

- Architecture-impacting unknowns are listed.
- If no important unknowns are found, write `None identified`.

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

Use the output path selected during intake. On the fast path, produce a compact
architecture note instead of a full output package.

Use Mermaid when a diagram improves clarity.

For large systems, split diagrams by purpose, such as boundary, module,
workflow, and data-flow views. Do not use one diagram when several focused
views would be clearer.

Create SVG visual artifacts only when they help presentation or review. Generate
SVG from Mermaid and keep Mermaid as the editable source of truth.

Gate before continuing:

- Maps and diagrams are traceable to evidence, user intent, assumptions, or
  proposed status.
- Uncertain nodes are marked inferred, assumed, proposed, unknown, or
  unverified.

## 7. Document

Use templates from `templates/`. Do not create every template by default.

Write in clear English.

For existing systems, keep claims traceable to inspected files or user-provided
context.

For raw ideas, keep proposals traceable to user intent and explicit
assumptions.

## 8. Validate

Answer the validation gate before reporting:

1. Claim traceability:
   Does every important claim have a source?
   If not, mark it as `Unverified`, `Assumed`, or remove it.
2. Scope alignment:
   Does the final scope match the intake scope?
   If it expanded, state what was added, why, and whether it is approved.
3. Handoff readiness:
   Does the handoff include unknowns and safe next actions?
   If none are found, write `None identified`.

Also check that proposed architecture is labeled as proposed, assumptions are
visible, diagrams match the written description, risks are specific, and
recommendations do not override existing architecture without approval.

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
- How the validation gate was answered
- What was documented
- What should happen next

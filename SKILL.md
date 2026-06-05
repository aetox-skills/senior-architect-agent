---
name: senior-architect-agent
description: >-
  Architecture inspection and documentation discipline for AI agents.
  Use when an AI agent must understand an existing software project,
  map architecture, produce documentation, prepare handoff notes,
  ask architecture-impacting questions, propose architecture changes
  before editing code, or turn a raw idea into a reviewable architecture proposal.
---

# Senior Architect Agent

Use this skill to make the agent understand before it acts.

This skill is not a diagram generator. It is a discipline layer for
architecture work.

This project is a skill: Markdown architecture docs, Mermaid diagram sources,
and optional SVG visual artifacts.

Expanded direction:

> This skill helps AI agents unfold existing systems and raw ideas into
> architecture maps that humans and future AI agents can understand, review,
> and continue from.

Require inspection, classification, questioning, mapping, documentation,
validation, and reporting before architecture recommendations or code edits.

This skill supports both existing systems and raw ideas. In both cases, the
agent must separate what is known from what is inferred, proposed, unknown, or
awaiting approval.

Core flow for both modes:

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

## Operating Rules

1. Never design before inspecting the real system.
2. Never modify code before understanding the relevant architecture.
3. Never assume silently.
4. Separate confirmed facts, reasonable inferences, open questions, risks, and
   decisions.
5. Ask important architecture questions before final architecture conclusions.
6. Prefer useful documentation over decorative documentation.
7. Prefer Markdown and Mermaid before SVG.
8. Protect existing project structure, naming conventions, and architectural
   intent unless redesign is explicitly approved.
9. Avoid document bloat. Create only the files needed for the system's
   complexity.
10. Refuse unsupported claims.
11. When starting from an idea, never present proposed architecture as existing
    implementation.
12. Use fast-path output for small or low-risk tasks.
13. Use available inspection tools as evidence helpers, not as replacements for
    architectural judgment.
14. Split large diagrams into focused views instead of creating one unreadable
    all-in-one diagram.
15. Do not pass a checkpoint gate until its required evidence, labels, or
    explicit limitations are present.

## Checkpoint Gates

Use these gates to keep the flow enforceable:

- Intake gate: mode, initial scope, and fast-path or full-package decision are
  recorded.
- Inspection gate: evidence or user intent is recorded, with inspection
  limitations when something cannot be verified.
- Classification gate: architecture areas are classified before mapping.
- Question gate: architecture-impacting unknowns are listed, or `None
  identified` is written.
- Mapping gate: maps and diagrams are traceable to evidence, user intent,
  assumptions, or proposed status.
- Validation gate: answer the three validation questions in Step 8 before
  reporting.

## Operating Modes

Choose the mode before producing architecture output.

### Existing System Mapping Mode

Use this mode when codebase files, project structure, existing documentation,
configs, tests, or deployment files are available.

Goal:

- Inspect and map what exists before suggesting changes.

Discipline:

- Evidence-first.
- Confirm claims from files or user-provided context.
- Separate confirmed facts, reasonable inferences, open questions, risks, and
  decisions.
- Mark missing categories as not observed.
- Do not invent missing backend, database, infrastructure, AI service, or
  external service.
- Do not redesign or edit before understanding the relevant architecture.

Primary outputs:

- Architecture overview
- System boundary
- Module map
- Data flow
- Workflow map
- File responsibility map
- Open questions
- Risk register
- AI agent notes
- Mermaid diagrams
- SVG visual artifacts when useful for presentation or review

### Idea-to-Architecture Mode

Use this mode when the user provides a raw idea, product concept, feature
request, business goal, or system goal without an existing implementation.

Goal:

- Transform the idea into a reviewable architecture proposal.

Discipline:

- Question-first.
- Proposal-first.
- Preserve the user's intent.
- Ask architecture-impacting questions.
- Mark all assumptions clearly.
- Produce a useful first architecture draft using explicit assumptions.
- Mark all modules, workflows, data models, integrations, and boundaries as
  proposed until approved.
- Explain tradeoffs and decisions requiring approval.
- Do not claim that proposed modules, data models, workflows, or integrations
  already exist.

Primary outputs:

- Idea brief
- Architecture proposal
- Module proposal
- Workflow proposal
- Data model draft
- Decision options
- Open questions
- Risk register
- AI agent notes
- Mermaid diagrams
- SVG visual artifacts when useful for presentation or review

## Step 1: Intake

Read the user's request and identify available inputs:

- Existing files, project structure, docs, configs, tests, or deployment files
- Raw idea, product concept, feature request, or business/system goal
- Explicit constraints, priorities, and requested outputs
- The narrowest useful project area or module scope

Do not start with architecture conclusions.

Prefer module-level mapping when the user asks about one module or workflow.
Avoid whole-system mapping unless the request, risk, or handoff need justifies
it.

Record the initial scope and whether the task uses the fast path or a full
output package before proceeding.

## Step 2: Select Mode

Choose one operating mode:

- Existing System Mapping Mode when existing project evidence is available.
- Idea-to-Architecture Mode when no implementation is available.

If both exist, map the existing system first and mark new ideas as proposed
changes.

## Step 3: Inspect or Extract Idea

Inspect available evidence.

For Existing System Mapping Mode, inspect project files, folders, docs,
configs, tests, package manifests, build scripts, deployment files, naming
patterns, and architecture signals.

For Idea-to-Architecture Mode, inspect the user's stated idea, goals,
constraints, user types, domain terms, requested features, and implied
boundaries. Do not treat the idea as an existing implementation.

Minimum inspection targets when available:

- Root file tree
- README or docs
- Package/build config
- Source folder structure
- Routing or entry points
- Data models or schemas
- API handlers or service boundaries
- Test structure
- Deployment or infrastructure config
- Existing architecture notes or ADRs

Use available inspection tools such as file search, file tree inspection, git
history, validators, and Mermaid checks when they help. Treat tool output as
evidence to interpret, not as architecture by itself.

Record only what is visible from files, explicitly provided by the user, or
clearly labeled as assumption.

If evidence or user intent is missing for an important area, record the
inspection limitation instead of filling the gap with a guess.

## Step 4: Classify

Classify the system or proposed system into applicable areas:

- Frontend
- Backend
- Database
- AI or background processes
- External services
- Infrastructure
- Shared modules
- Tests and quality gates
- Unknown or unclear areas

In Existing System Mapping Mode, mark missing categories as not observed.

In Idea-to-Architecture Mode, mark categories as proposed, assumed, unknown, or
not in scope. Do not present proposed architecture as confirmed fact.

Do not map before classification is complete.

## Step 5: Question

Identify architecture-impacting unknowns before finalizing architecture.

Ask questions when missing details could change the map, risk assessment, or
recommendation.

Ask only important questions. Do not block on minor details that can be marked
as assumptions.

Separate:

- Confirmed facts
- Reasonable inferences
- Proposed architecture
- Assumptions
- Open questions
- Risks
- Decisions already made
- Decisions still needed
- Decisions requiring approval

If no architecture-impacting questions are found, write `None identified` so
the absence is explicit.

## Step 6: Map

Produce maps that help humans and future AI agents understand the system
quickly.

Fast-path threshold:

- For small or low-risk tasks, keep the output to a compact architecture note.
- Use a full output package only for multi-module work, unclear boundaries,
  persistence, integrations, payments, security, major workflow changes, or
  future-agent handoff.
- Even on the fast path, still inspect, classify, question, map, validate, and
  report in compact form.

For existing systems, use the smallest useful set:

- Architecture overview
- System boundary
- Module map
- Data flow
- Workflow map
- File responsibility map

For raw ideas, use the smallest useful proposal set:

- Idea brief
- Architecture proposal
- Module proposal
- Workflow proposal
- Data model draft
- Decision options

Use Mermaid for diagrams when helpful.

Keep diagrams readable and traceable to inspected files, user-provided facts,
or explicit assumptions.

For large systems, split diagrams by architecture question:

- Boundary
- Module relationships
- Workflow
- Data flow

Treat SVG as an optional visual artifact for presentation or review. Generate
it from Mermaid when it helps, and do not use SVG as the architecture source of
truth.

Do not include untraceable components in maps or diagrams. Mark uncertain
components as inferred, assumed, proposed, unknown, or unverified.

## Step 7: Document

Use templates from `templates/` when creating architecture outputs:

- `architecture-overview.md`
- `system-boundary.md`
- `module-map.md`
- `data-flow.md`
- `workflow-map.md`
- `file-responsibility-map.md`
- `open-questions.md`
- `risk-register.md`
- `ai-agent-notes.md`
- `decision-record.md`
- `idea-brief.md`
- `architecture-proposal.md`
- `module-proposal.md`
- `workflow-proposal.md`
- `data-model-draft.md`
- `decision-options.md`

Do not create every template by default.

Choose based on actual complexity and user need.

`agents/openai.yaml`, when present, is interface metadata only. The core skill
must remain usable from `SKILL.md`, Markdown docs, templates, rules, and
examples without depending on metadata.

## Step 8: Validate

Before reporting, answer these three validation questions:

1. Claim traceability:
   Does every important claim have a source?
   If not, mark it as `Unverified`, `Assumed`, or remove it before passing.
2. Scope alignment:
   Does the final scope match the intake scope?
   If it expanded, state what was added, why, and whether it is approved.
3. Handoff readiness:
   Does the handoff include unknowns and safe next actions?
   If none are found, write `None identified` instead of leaving the section
   blank.

Use evidence strength for important claims:

- `Direct`: supported directly by files or user-provided facts.
- `Inferred`: derived from evidence but not directly confirmed.
- `Assumed`: explicit working premise.
- `Unverified`: no source yet; verify, mark, or remove before final decisions.

Use `Verify first: Yes` for claims that humans or future agents should check
before relying on them.

Also confirm that proposed elements are labeled as proposed until approved,
diagrams match the written map, SVG artifacts match their Mermaid source, and
documentation is lean enough to maintain.

## Step 9: Report

Report with this structure when appropriate:

1. What was inspected
2. Confirmed architecture facts
3. Reasonable inferences
4. Proposed architecture and assumptions, if working from an idea
5. Open questions
6. Risks or unclear boundaries
7. Decisions requiring approval
8. Validation gate answers
9. Documentation created or updated
10. Recommended next steps

## Rule References

Load these files when deeper guidance is needed:

- `rules/inspection-rules.md`
- `rules/question-rules.md`
- `rules/documentation-rules.md`
- `rules/diagram-rules.md`
- `rules/anti-overengineering-rules.md`
- `rules/agent-handoff-rules.md`
- `docs/anti-patterns.md`

## Philosophy Reference

Keep operational work concise.

Read `docs/philosophy.md` only when the user asks about the reasoning behind
the skill or when revising the skill's principles.

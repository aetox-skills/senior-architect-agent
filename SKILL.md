---
name: senior-architect-agent
description: >-
  Architecture inspection and documentation discipline for AI agents. Use when
  an AI agent must understand an existing software project, map architecture,
  produce architecture documentation, prepare handoff notes, review boundaries,
  ask architecture-impacting questions, propose architecture changes before
  editing code, or turn a raw idea into a reviewable architecture proposal.
---

# Senior Architect Agent

Use this skill to make the agent understand before it acts.

This skill is not a diagram generator. It is a discipline layer for
architecture work.

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

Do not start with architecture conclusions.

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

Record only what is visible from files, explicitly provided by the user, or
clearly labeled as assumption.

## Step 4: Classify

Classify the system or proposed system into applicable areas:

- Frontend
- Backend
- Database
- AI or automation
- External services
- Infrastructure
- Shared modules
- Tests and quality gates
- Unknown or unclear areas

In Existing System Mapping Mode, mark missing categories as not observed.

In Idea-to-Architecture Mode, mark categories as proposed, assumed, unknown, or
not in scope. Do not present proposed architecture as confirmed fact.

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

## Step 6: Map

Produce maps that help humans and future AI agents understand the system
quickly.

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

Treat SVG as an optional visual artifact for presentation or review. Generate
it from Mermaid when it helps, and do not use SVG as the architecture source of
truth.

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

Before reporting, validate the outputs:

- Every claim is backed by inspected files, user-provided context, or clearly
  marked inference.
- Every proposed element is labeled as proposed until approved.
- Every assumption is visible.
- Open questions are explicit.
- Diagrams match the written map.
- SVG visual artifacts, when present, match their Mermaid source.
- Risks are specific and actionable.
- Recommendations respect existing structure unless redesign was requested.
- Documentation is lean enough to maintain.

## Step 9: Report

Report with this structure when appropriate:

1. What was inspected
2. Confirmed architecture facts
3. Reasonable inferences
4. Proposed architecture and assumptions, if working from an idea
5. Open questions
6. Risks or unclear boundaries
7. Decisions requiring approval
8. Documentation created or updated
9. Recommended next steps

## Rule References

Load these files when deeper guidance is needed:

- `rules/inspection-rules.md`
- `rules/question-rules.md`
- `rules/documentation-rules.md`
- `rules/diagram-rules.md`
- `rules/anti-overengineering-rules.md`
- `rules/agent-handoff-rules.md`

## Philosophy Reference

Keep operational work concise.

Read `docs/philosophy.md` only when the user asks about the reasoning behind
the skill or when revising the skill's principles.

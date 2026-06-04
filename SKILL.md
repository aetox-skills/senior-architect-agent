---
name: senior-architect-agent
description: Architecture inspection and documentation discipline for AI agents. Use when Codex or another AI agent must understand a software project, map architecture, produce architecture documentation, prepare handoff notes, review boundaries, ask architecture-impacting questions, or propose architecture changes before editing code. Especially useful for codebase onboarding, system design review, refactoring plans, module responsibility mapping, risk analysis, and preventing unsupported assumptions.
---

# Senior Architect Agent

Use this skill to make the agent understand before it acts.

This skill is not a diagram generator. It is a discipline layer for architecture work. It requires inspection, classification, questioning, mapping, documentation, validation, and reporting before architecture recommendations or code edits.

Core flow:

```txt
Inspect -> Classify -> Question -> Map -> Document -> Validate -> Report
```

## Operating Rules

1. Never design before inspecting the real system.
2. Never modify code before understanding the relevant architecture.
3. Never assume silently.
4. Separate confirmed facts, reasonable inferences, open questions, risks, and decisions.
5. Ask important architecture questions before final architecture conclusions.
6. Prefer useful documentation over decorative documentation.
7. Prefer Markdown and Mermaid before SVG.
8. Protect existing project structure, naming conventions, and architectural intent unless redesign is explicitly approved.
9. Avoid document bloat. Create only the files needed for the system's complexity.
10. Refuse unsupported claims.

## Step 1: Inspect

Inspect available project files, folders, docs, configs, tests, package manifests, build scripts, deployment files, naming patterns, and architecture signals.

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

Record only what is visible from files or explicitly provided by the user.

## Step 2: Classify

Classify the system into applicable areas:

- Frontend
- Backend
- Database
- AI or automation
- External services
- Infrastructure
- Shared modules
- Tests and quality gates
- Unknown or unclear areas

If a category is not present, mark it as not observed. Do not invent it.

## Step 3: Question

Identify architecture-impacting unknowns before finalizing architecture. Ask questions when missing details could change the map, risk assessment, or recommendation.

Ask only important questions. Do not block on minor details that can be marked as assumptions.

Separate:

- Confirmed facts
- Reasonable inferences
- Open questions
- Risks
- Decisions already made
- Decisions still needed

## Step 4: Map

Produce maps that help humans and future AI agents understand the system quickly.

Use the smallest useful set:

- Architecture overview
- System boundary
- Module map
- Data flow
- Workflow map
- File responsibility map

Use Mermaid for diagrams when helpful. Keep diagrams readable and traceable to inspected files.

## Step 5: Document

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

Do not create every template by default. Choose based on actual complexity and user need.

## Step 6: Validate

Before reporting, validate the outputs:

- Every claim is backed by inspected files, user-provided context, or clearly marked inference.
- Open questions are explicit.
- Diagrams match the written map.
- Risks are specific and actionable.
- Recommendations respect existing structure unless redesign was requested.
- Documentation is lean enough to maintain.

## Step 7: Report

Report with this structure when appropriate:

1. What was inspected
2. Confirmed architecture facts
3. Reasonable inferences
4. Open questions
5. Risks or unclear boundaries
6. Documentation created or updated
7. Recommended next steps

## Rule References

Load these files when deeper guidance is needed:

- `rules/inspection-rules.md`
- `rules/question-rules.md`
- `rules/documentation-rules.md`
- `rules/diagram-rules.md`
- `rules/anti-overengineering-rules.md`
- `rules/agent-handoff-rules.md`

## Philosophy Reference

Keep operational work concise. Read `docs/philosophy.md` only when the user asks about the reasoning behind the skill or when revising the skill's principles.

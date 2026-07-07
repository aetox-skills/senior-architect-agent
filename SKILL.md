---
name: senior-architect-agent
description: >-
  Cognitive framework that transforms AI agents into senior architects —
  evidence-first system understanding, honest uncertainty mapping,
  and architecture reasoning before action. Use when an agent must
  understand a codebase, map architecture, produce handoff notes,
  propose changes, or turn an idea into a reviewable proposal
  without guessing.
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

Sibling skill routing:

If the request is a pure raw idea and `$idea-to-architecture-agent` is
available, prefer that dedicated sibling skill. Continue with this skill when
the idea is tied to existing system evidence, requires broader architecture
mapping, needs boundary/risk/handoff work, or the dedicated skill is
unavailable. Do not make this skill depend on the sibling skill.

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
12. Start with the smallest safe architecture pass and promote only when
    scope, evidence, risk, or handoff needs require it.
13. Use available inspection tools as evidence helpers, not as replacements for
    architectural judgment.
14. Split large diagrams into focused views instead of creating one unreadable
    all-in-one diagram.
15. Do not pass a checkpoint gate until its required evidence, labels, or
    explicit limitations are present.

## Checkpoint Gates

Use these gates to keep the flow enforceable:

- Intake gate: mode, initial scope, selected pass level, and output path are
  recorded, or an early exit is declared when no architecture pass is needed.
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

Record the initial scope, selected pass level, and output path before
proceeding.

Early Exit Rule:

If the task is a small implementation fix with no architecture impact, do not
run an architecture pass or create architecture documentation. Report:

- `No architecture pass required`
- Why there is no architecture impact
- Any uncertainty that would change that conclusion
- Recommended next step

If architecture impact is unclear, use Scan Mode rather than exiting.

Right-Sized Pass Control:

Before producing architecture documentation, select the smallest safe pass.

- Scan Mode: use for small, bounded, exploratory, or low-risk work. Output a
  compact architecture note.
- Focus Mode: use for one module, one workflow, a small subsystem, or a change
  that touches a clear boundary. Output only the maps or notes needed for that
  scope.
- Full Mode: use for whole-system mapping, future-agent handoff, unclear
  ownership, 3+ interacting modules, persistence, integrations, payment,
  authentication, security, deployment, or major workflow changes.

Start in Scan Mode unless the request already shows a Focus or Full trigger.
Promote only when inspected evidence, scope, risk, or handoff requirements make
the smaller pass unsafe. If uncertain, inspect narrowly first, record what was
checked, and do not promote because of uncertainty alone.

Promotion gate:

- Name the trigger.
- Cite the evidence or user request.
- State the risk of staying in the smaller pass.
- Keep the current pass if the trigger is speculative.

## Step 2: Select Mode

Choose one operating mode:

- Existing System Mapping Mode when existing project evidence is available.
- Idea-to-Architecture Mode when no implementation is available.

If `$idea-to-architecture-agent` is available and the request is only a raw
idea with no implementation context, prefer that sibling skill for the focused
proposal work.

If both exist, map the existing system first and mark new ideas as proposed
changes.

Use this skill for mixed existing-system and proposal work, broader
architecture mapping, boundary analysis, risk review, or future-agent handoff.

## Step 3: Inspect or Extract Idea

Inspect available evidence.

For Existing System Mapping Mode, inspect project files, folders, docs,
configs, tests, package manifests, build scripts, deployment files, naming
patterns, and architecture signals.

Reuse existing architecture context before re-mapping. Read existing
architecture overviews, handoff notes, ADRs, current-state docs, or Mermaid
sources first when present. Do not re-map stable areas unless evidence
conflicts, the current scope touches that boundary, or the user asks for a full
re-check.

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

Inspection budget for large repositories:

- Start with top-level structure.
- Read README and existing docs.
- Read package, build, framework, and environment config.
- Identify entry points.
- Inspect routing, module registries, or service registries.
- Inspect relevant modules only.
- Go deeper only when evidence, risk, or the selected scope requires it.

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

In Scan Mode, collapse this separation into four groups: confirmed facts,
inferences or assumptions, open questions, and risks. Use the full separation
only in Focus Mode and Full Mode.

Loopback rule:

If mapping, documentation, or validation exposes an architecture-changing
unknown, return to Step 5 before final conclusions. Either ask the question or
mark the output as incomplete and proceed only with a clearly labeled
assumption.

## Step 6: Map

Produce maps that help humans and future AI agents understand the system
quickly.

Use the output path selected during intake.

For Scan Mode, produce one compact architecture note and nothing else. Steps
may be merged; only the discipline must survive. The note contains: pass level
and reason, scope, evidence checked, skipped areas, confirmed facts, inferences
or assumptions, open questions, risks, and safe next actions. Do not expand
these into the full report structure, and do not pad sections — write `None
identified` where nothing was found.

For Focus Mode, document only the relevant module, workflow, boundary, risks,
and safe next actions.

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

Use Mermaid for diagrams only when requested, required for handoff, or needed
to clarify cross-module relationships.

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

Artifact budget:

- Scan Mode: one compact architecture note.
- Focus Mode: one to three artifacts.
- Full Mode: full output package only when scope, risk, or handoff requires it.

If output exceeds the budget, state why before creating extra artifacts.

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

Also confirm:

- Selected pass level is stated.
- Inspection scope is justified.
- Skipped areas are named when relevant.
- Discipline labels and risks are preserved.
- Any pass promotion has a trigger, evidence, and risk statement.
- Output stays within artifact budget, or the over-budget reason is stated.
- Architecture-changing unknowns found after mapping looped back to questions
  or are clearly labeled as assumptions.

## Step 9: Report

In Scan Mode, the compact architecture note from Step 6 is the report. Do not
add the full structure below on top of it.

For Focus Mode and Full Mode, report with this structure:

1. What was inspected
2. Selected pass level and why
3. Confirmed architecture facts
4. Reasonable inferences
5. Proposed architecture and assumptions, if working from an idea
6. Open questions
7. Risks or unclear boundaries
8. Decisions requiring approval
9. Validation gate answers
10. Documentation created or updated
11. Recommended next steps

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

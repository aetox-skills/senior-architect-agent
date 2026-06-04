# senior-architect-agent

Version target: `v1.0.0 - Flagship Content Readiness`

This project is a reusable AI agent skill that forces an agent to inspect,
understand, question, map, document, and validate a software system or raw
system idea before suggesting architecture changes or editing code.

Main slogan:

> This skill does not make AI code faster. It makes AI understand before it acts.

Expanded direction:

> This skill helps AI agents unfold existing systems and raw ideas into
> architecture maps that humans and future AI agents can understand, review,
> and continue from.

## Purpose

AI agents often edit code before they understand the architecture. They also
turn raw ideas into confident designs too early.

This skill adds a discipline layer:

1. Inspect the real system first.
2. Preserve user intent when no system exists yet.
3. Separate confirmed facts, proposed architecture, assumptions, inferences,
   open questions, risks, and decisions.
4. Ask architecture-impacting questions before finalizing conclusions.
5. Produce useful Markdown and Mermaid architecture maps.
6. Leave handoff notes that future AI agents can use quickly.
7. Avoid unsupported claims, decorative documentation, and overengineering.

## Operating Modes

### Existing System Mapping Mode

Use this mode when project files, codebase structure, or existing documentation
are available.

The agent inspects what exists, maps real boundaries and responsibilities, and
marks uncertainty instead of inventing missing architecture.

### Idea-to-Architecture Mode

Use this mode when the user provides a raw idea, product concept, feature
request, or business/system goal without an implementation.

The agent asks architecture-impacting questions, preserves the user's intent,
states assumptions, and produces a reviewable proposal. All modules, workflows,
data models, and integrations remain proposed until approved.

## Implementation Plan

`v1.0.0` focuses on flagship content readiness:

1. Define a strict, practical `SKILL.md` for both operating modes.
2. Provide an operating workflow covering intake, mode selection,
   inspection or idea extraction, classification, questioning, mapping,
   documentation, validation, and reporting.
3. Add compact rule files that prevent common AI agent failure modes.
4. Add reusable templates for architecture outputs.
5. Include small examples for existing-system mapping and idea-to-architecture
   proposal behavior.
6. Provide optional skill interface metadata without making the core skill
   depend on it.

## File Tree

```txt
senior-architect-agent/
  README.md
  SKILL.md
  LICENSE
  CHANGELOG.md

  agents/
    openai.yaml

  docs/
    philosophy.md
    workflow.md
    output-spec.md
    diagram-guidelines.md
    question-framework.md
    project-core-th-final.md

  rules/
    inspection-rules.md
    question-rules.md
    documentation-rules.md
    diagram-rules.md
    anti-overengineering-rules.md
    agent-handoff-rules.md

  templates/
    architecture-overview.md
    system-boundary.md
    module-map.md
    data-flow.md
    workflow-map.md
    file-responsibility-map.md
    open-questions.md
    risk-register.md
    ai-agent-notes.md
    decision-record.md
    idea-brief.md
    architecture-proposal.md
    module-proposal.md
    workflow-proposal.md
    data-model-draft.md
    decision-options.md

  examples/
    basic-web-app/
      input-context.md
      output/
        architecture-overview.md
        system-boundary.md
        module-map.md
        data-flow.md
        workflow-map.md
        file-responsibility-map.md
        risk-register.md
        diagram.mmd
        open-questions.md
        ai-agent-notes.md
    idea-to-architecture/
      input-context.md
      output/
        idea-brief.md
        open-questions.md
        architecture-proposal.md
        module-proposal.md
        workflow-proposal.md
        data-model-draft.md
        risk-register.md
        diagram.mmd
        ai-agent-notes.md
```

## How To Use

Use this skill when an AI agent is asked to understand a codebase, plan
architecture changes, review system structure, document architecture, create
handoff notes, propose redesigns, or turn a raw idea into an architecture
proposal.

When files exist, the agent should not begin with code edits. It should inspect
the project, classify what exists, ask important questions, map the system,
document confirmed facts and uncertainty, then report safe next steps.

When only an idea exists, the agent should not pretend a system exists. It
should clarify intent, mark assumptions, propose architecture, identify
tradeoffs, and list decisions requiring approval.

## Preferred Outputs

Use Markdown first. Use Mermaid diagrams when diagrams help.

Mermaid is the editable source of truth for diagrams.

SVG visual artifacts are deferred for v1. They may be added later as
presentation or review artifacts when they make complex architecture easier to
understand, but they must not replace Markdown and Mermaid as source of truth.

## License

MIT

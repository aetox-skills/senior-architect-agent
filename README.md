# senior-architect-agent

Version: `v0.1.0 - Foundation Map`

This project is a reusable AI agent skill that forces an agent to inspect,
understand, question, map, document, and validate a software system or raw
system idea before suggesting architecture changes or editing code.

Main slogan:

> This skill does not make AI code faster. It makes AI understand before it acts.

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

`v0.1.0` focuses on the foundation only:

1. Define a strict, practical `SKILL.md`.
2. Provide a small operating workflow: `Inspect -> Classify -> Question -> Map -> Document -> Validate -> Report`.
3. Add compact rule files that prevent common AI agent failure modes.
4. Add reusable templates for architecture outputs.
5. Include one small example showing correct behavior.

## File Tree

```txt
senior-architect-agent/
  README.md
  SKILL.md
  LICENSE
  CHANGELOG.md

  docs/
    philosophy.md
    workflow.md
    output-spec.md
    diagram-guidelines.md
    question-framework.md

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

Generate SVG only when explicitly requested or when Markdown and Mermaid cannot
express the architecture clearly enough.

## License

MIT

# senior-architect-agent

Version: `v0.1.0 - Foundation Map`

This project is a reusable AI agent skill that forces an agent to inspect, understand, question, map, document, and validate a software system before suggesting architecture changes or editing code.

Main slogan:

> This skill does not make AI code faster. It makes AI understand before it acts.

## Purpose

AI agents often edit code before they understand the architecture. This skill adds a discipline layer:

1. Inspect the real system first.
2. Separate confirmed facts from inferences.
3. Ask architecture-impacting questions before finalizing conclusions.
4. Produce useful Markdown and Mermaid architecture maps.
5. Leave handoff notes that future AI agents can use quickly.
6. Avoid unsupported claims, decorative documentation, and overengineering.

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

  examples/
    basic-web-app/
      input-context.md
      output/
        architecture-overview.md
        module-map.md
        data-flow.md
        diagram.mmd
        open-questions.md
        ai-agent-notes.md
```

## How To Use

Use this skill when an AI agent is asked to understand a codebase, plan architecture changes, review system structure, document architecture, create handoff notes, or propose redesigns.

The agent should not begin with code edits. It should inspect the project, classify what exists, ask important questions, map the system, document confirmed facts and uncertainty, then report safe next steps.

## Preferred Outputs

Use Markdown first. Use Mermaid diagrams when diagrams help. Generate SVG only when explicitly requested or when Markdown and Mermaid cannot express the architecture clearly enough.

## License

MIT

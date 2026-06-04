# Changelog

## Unreleased - v1 Flagship Content Readiness

Pending review.

Added:

- Two first-class operating modes:
  Existing System Mapping Mode and Idea-to-Architecture Mode.
- Templates and example output packages for both operating modes.
- SVG visual artifacts for both example output packages.

Updated:

- Markdown and Mermaid remain the editable source of truth.
- SVG is documented as a secondary visual artifact for review, presentation,
  README embedding, or human-facing explanation.
- Thai project core document is the directional source of truth.
- Optional `agents/openai.yaml` interface metadata is included without becoming
  a core skill dependency.
- CLI, web UI, plugin platform, automation framework, and exporter system work
  are outside the core scope.

## v0.1.0 - Foundation Map

Initial foundation release.

Added:

- Root `SKILL.md` with strict architecture inspection workflow.
- Practical workflow documentation for `Inspect -> Classify -> Question -> Map -> Document -> Validate -> Report`.
- Rule files for inspection, questions, documentation, diagrams, anti-overengineering, and AI handoff.
- Markdown templates for core architecture outputs.
- Basic web app example showing the full Foundation Map output package:
  architecture overview, system boundary, module map, data flow, workflow map,
  file responsibility map, open questions, risk register, handoff notes, and a
  Mermaid diagram.

Not included yet:

- Large reference catalogs.
- Framework-specific architecture rules.

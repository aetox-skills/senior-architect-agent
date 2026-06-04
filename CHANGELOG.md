# Changelog

## v1.1.0 - SVG Visual Artifacts

Pending review.

Added:

- SVG visual artifacts for both example output packages.
- Documentation updates that define SVG as a generated presentation or review
  artifact.

Preserved:

- Markdown and Mermaid remain the editable source of truth.
- No package dependency or SVG export automation was added.

## v1.0.0 - Flagship Content Readiness

Released.

Updated:

- Two operating modes are now first-class:
  Existing System Mapping Mode and Idea-to-Architecture Mode.
- Markdown and Mermaid remain the editable source of truth.
- SVG is documented as a visual artifact role.
- Thai project core document is the directional source of truth.
- Optional `agents/openai.yaml` interface metadata is included without becoming
  a core skill dependency.
- Existing-system and idea-to-architecture examples demonstrate the core flow.

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

- Automation scripts.
- SVG generation.
- Large reference catalogs.
- Framework-specific architecture rules.

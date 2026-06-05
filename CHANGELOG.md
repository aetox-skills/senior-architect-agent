# Changelog

## Unreleased

Pending future changes.

## v1.1.0 - Right-Sized Architecture Passes

Release focus: reduce model load without weakening architecture discipline.

Added:

- `Scan Mode`, `Focus Mode`, and `Full Mode` pass levels.
- Compact Architecture Note output for low-risk Scan Mode work.
- Inspection budget guidance for large repositories.
- Existing architecture context reuse before re-mapping stable areas.
- Validation checks for selected pass level, inspection scope, skipped areas,
  discipline labels, and risks.

Updated:

- Mermaid diagrams are generated only when requested, required for handoff, or
  needed to clarify cross-module relationships.
- Model requirements now describe small work as `Scan Mode` rather than
  fast-path.
- README now uses clearer search and discovery terms for AI architecture skill,
  existing system mapping, architecture documentation, Mermaid diagrams, and AI
  agent handoff.

## v1.0.0 - Flagship Content Readiness

Flagship content readiness release.

Added:

- Cross-agent installation guidance in `INSTALL.md`.
- `adapters/agents-md/AGENTS.example.md` for AGENTS.md-style runtimes.
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
- Core scope is expressed as a skill package: Markdown architecture docs,
  Mermaid diagram sources, optional SVG visual artifacts, rules, templates, and
  examples.
- Fast-path guidance now prevents small tasks from turning into full output
  packages.
- Diagram guidance now emphasizes focused views for large systems.
- Checkpoint gates now make intake, inspection, classification, questioning,
  mapping, validation, and reporting easier to enforce.
- Evidence strength and a three-question validation gate help prevent
  unsupported claims, scope drift, and weak handoff notes.
- Anti-pattern guidance now shows rejected architecture output patterns.
- Model-fit guidance now explains context and reasoning requirements for using
  the skill responsibly.
- Fast-path selection now has a decision tree so small, bounded, or exploratory
  work does not default to a full output package.
- Sibling-skill routing now explains when to prefer
  `$idea-to-architecture-agent` for pure raw ideas without making it a
  dependency of this skill.

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

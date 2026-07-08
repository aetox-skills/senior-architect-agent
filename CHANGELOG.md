# Changelog

## Unreleased

Release focus: single-core scope, internal deduplication, and senior-level
assessment — the skill now judges systems, not just describes them.

Added:

- `Assess` step in the core flow (`... Map -> Assess -> Document ...`).
  Describing the system is not the end of senior work: the agent must name
  architecture debt, framework and project convention drift, separation-of-
  concerns violations, and flow conflicts found in the mapped evidence.
- Finding discipline: every finding requires evidence, impact, severity
  (`Critical`/`High`/`Medium`/`Low`), confidence, and the smallest safe
  correction marked as a proposed change requiring approval. Judged only
  against framework conventions and the project's dominant patterns — never
  personal style. `None identified` is a valid assessment.
- `rules/assessment-rules.md` with assessment dimensions, finding shape,
  non-findings, and depth-by-pass-level guidance.
- `templates/debt-register.md` and an example debt register in
  `examples/basic-web-app/output/`.
- Anti-patterns: `Map Without Judgment` and `Unsupported Criticism`.
- Knowledge-graph-assisted mapping and assessment (optional). When a codebase
  intelligence MCP is available, Step 5 uses dependency and caller queries to
  accelerate mapping, and Step 6 treats graph cycles, layer-crossing edges,
  fan-in outliers, and zero-consumer exports as signals feeding the existing
  assessment dimensions — no new finding category. Graph data maps into the
  existing evidence-strength taxonomy (`Direct`/`Inferred` + `Verify first:
  Yes`), severity is never pre-assigned, and file reading wins when graph and
  source disagree. Without such a tool, the flow is unchanged.

Removed (breaking):

- Idea-to-Architecture Mode. Pure raw-idea work is now always routed to the
  sibling skill `idea-to-architecture-agent`. If the sibling skill is not
  installed, the agent states the scope limitation instead of running a
  built-in idea workflow.
- Idea-mode templates: `idea-brief.md`, `architecture-proposal.md`,
  `module-proposal.md`, `workflow-proposal.md`, `data-model-draft.md`,
  `decision-options.md`.
- The `examples/idea-to-architecture/` example package.
- The `Select Mode` step. With one scope there is nothing to select; raw-idea
  routing happens during intake. Combined with the new `Assess` step, the core
  flow is `Intake -> Inspect -> Classify -> Question -> Map -> Assess ->
  Document -> Validate -> Report`.

Still supported:

- Mixed work where a new idea is tied to an existing system: map the existing
  system first, then mark new elements as proposed changes until approved.

Updated:

- `SKILL.md` is now the single source of truth for the workflow;
  `docs/workflow.md` is reduced to a pointer instead of a near-verbatim copy.
- Removed repeated fact/inference-separation and proposed-status statements
  inside `SKILL.md`; each rule is now stated once.
- Scan Mode is explicitly lightweight: steps may merge, the separation
  taxonomy collapses to four groups, and the compact architecture note itself
  is the report instead of the full report structure.
- The Thai directional core document, README, docs, and interface metadata now
  reflect the single existing-system scope.
- `assets/visuals/01_core_workflow.mmd` matches the new 9-step flow. The
  rendered workflow infographic and core-flow GIF still show the old flow and
  need regeneration.

Fixed:

- Removed stray Chinese characters in the Thai README usage section.

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

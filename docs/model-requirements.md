# Model Requirements

This skill is designed for models that can reason through architecture gates,
not models that only produce quick summaries.

The skill itself can consume a meaningful amount of context before the target
project is even inspected. A capable model must still have room for project
files, evidence, questions, maps, diagrams, validation, and handoff notes.

## Required Capabilities

Use a model with:

- Long enough context for the skill, project evidence, and output.
- Strong instruction following across long conversations.
- Multi-step reasoning across intake, inspection, classification, mapping,
  validation, and reporting.
- Evidence tracking across files, user-provided facts, assumptions, and
  unknowns.
- Checkpoint discipline: the model must not silently skip gates.

This skill works best with models that can think, not merely answer.

## Context Guidance

These are practical context-window targets, not hard platform rules.

| Project Size | Suggested Context | Why |
| --- | --- | --- |
| Small, 1-3 modules | 32K minimum, 64K preferred | Enough for the skill, a small file set, and compact output. |
| Medium, 5-15 modules | 64K-128K | Enough for multiple files, templates, maps, and validation. |
| Large, multi-service or multi-repo | 200K+ | Needed when the agent must hold broad system evidence and cross-boundary relationships. |

Below 32K is not recommended for the full workflow. It may still work for very
small Scan Mode tasks when the agent keeps output compact.

## Failure Points For Smaller Models

Smaller or weaker models often fail in predictable places:

- Step 4 to Step 6: forgetting classification before mapping and inventing
  diagram nodes.
- Validation gate: guessing the intake scope instead of comparing it to the
  final scope.
- Evidence strength: collapsing `Direct`, `Inferred`, `Assumed`, and
  `Unverified` into `Confirmed`.
- Checkpoint gates: passing gates silently without evidence or limitations.
- Handoff: omitting unknowns, safe next actions, or actions to avoid.

## Model Fit Examples

Named models change quickly. Treat these examples as illustrative and verify
current provider specs before making a final model choice.

Strong fit:

- Frontier or near-frontier models with large context windows.
- Models with reliable long-context instruction following.
- Models that can preserve evidence, assumptions, scope, and validation state.

Usable with caution:

- Smaller large-context models.
- Fast or inexpensive models that can summarize well but may skip gates.
- Models that work for Scan Mode tasks but struggle with full output packages.

Not recommended:

- Small-context models for full architecture mapping.
- Base models that are not instruction-tuned for reliable gate following.
- Models that frequently present assumptions or proposals as confirmed facts.

Examples of model families to evaluate include Claude Sonnet or Opus-class
models, GPT-class frontier models, and Gemini Pro-class models. Do not treat
that list as permanent or complete.

## Practical Rule

Minimum viable normal use:

- 128K context
- Strong instruction following
- Reliable multi-step reasoning

For small Scan Mode work, a smaller model may be acceptable if the agent keeps
scope narrow and marks uncertainty clearly.

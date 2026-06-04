# Question Framework

Ask questions to protect architecture quality, not to delay work.

## Mode-Specific Discipline

Existing System Mapping Mode is evidence-first.

Ask after inspecting files, docs, configs, and user-provided context. Do not
ask for information that can be found in the repository.

Idea-to-Architecture Mode is question-first.

Ask architecture-impacting questions before presenting a proposal. If the user
does not answer yet, continue with clearly labeled assumptions and decisions
requiring approval.

## Ask When Missing Information Could Change

- System boundaries
- Ownership of responsibilities
- Data flow
- Persistence strategy
- Integration contracts
- Deployment architecture
- Security requirements
- Scalability requirements
- Refactoring scope
- Documentation scope
- Approval ownership
- Product rules that affect system boundaries

## Do Not Ask When

- The answer can be discovered from files.
- The question is cosmetic.
- The question does not affect the architecture output.
- A reasonable inference can be marked clearly and safely.

In Idea-to-Architecture Mode, do not ask every product detail before drafting.
Ask the few questions that change architecture, then mark smaller details as
assumptions.

## Question Format

Use precise questions:

```txt
Open question:
  Is `src/lib/payments.ts` used only by checkout, or is it intended as a
  shared billing integration?
Why it matters:
  This changes whether payment logic should be documented as a feature module
  or shared external-service adapter.
```

## Priority

Mark open questions as:

- `Blocking`: Must be answered before final architecture decisions.
- `Important`: Should be answered before implementation changes.
- `Useful`: Helps future work but does not block current mapping.

For raw ideas, also mark decisions as:

- `Requires approval`: Proposed direction that should not be treated as final.

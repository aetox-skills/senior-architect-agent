# Question Framework

Ask questions to protect architecture quality, not to delay work.

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

## Do Not Ask When

- The answer can be discovered from files.
- The question is cosmetic.
- The question does not affect the architecture output.
- A reasonable inference can be marked clearly and safely.

## Question Format

Use precise questions:

```txt
Open question: Is `src/lib/payments.ts` used only by checkout, or is it intended as a shared billing integration?
Why it matters: This changes whether payment logic should be documented as a feature module or shared external-service adapter.
```

## Priority

Mark open questions as:

- `Blocking`: Must be answered before final architecture decisions.
- `Important`: Should be answered before implementation changes.
- `Useful`: Helps future work but does not block current mapping.

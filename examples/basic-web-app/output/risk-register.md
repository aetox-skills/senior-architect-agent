# Risk Register

## Scope

- Project: `basic-web-app`
- Requested scope: Architecture risks before adding a backend API.
- Inspection source: Provided file tree and observed signals.

## Inspection Limitations

- Actual source code, tests, and runtime behavior were not inspected.
- Risk likelihood is qualitative because the example context is intentionally
  small.

## Confirmed Facts

- The observed app is a React and Vite frontend.
- Todo persistence currently uses browser storage through `todoStorage.ts`.
- No backend, database, API route, deployment config, or auth requirement was
  observed.

## Reasonable Inferences

- Adding a backend will change the persistence boundary.
- Existing browser-stored todos may need migration, synchronization, or reset
  behavior.
- Authentication may become necessary if todos are stored per user.

## Risks

| Risk | Evidence | Effect | Chance | Next Step |
| --- | --- | --- | --- | --- |
| Premature API design | Backend ownership is open. | Wrong data model. | Medium | Answer ownership first. |
| Local data loss | Browser storage is current persistence. | Lost todos. | Medium | Define migration behavior. |
| Blurred responsibilities | UI and storage are separate. | Harder refactoring. | Medium | Keep service boundary. |
| Missing auth boundary | No auth observed. | Unclear ownership. | Unknown | Decide auth need. |
| Deployment uncertainty | No deploy config observed. | Runtime constraints missed. | Unknown | Identify runtime. |

## Uncertainties

| Uncertainty | Why It Matters | Next Step |
| --- | --- | --- |
| Backend source of truth | Determines API, data model, and migration. | Ask owner before design. |
| Authentication | Determines user data ownership and authorization. | Confirm requirement. |
| Offline behavior | Determines local storage role after backend adoption. | Decide cache, sync, or removal. |
| Actual call graph | Determines safe edit points. | Inspect source files. |

## Non-Risks

- Absence of a database is not a defect in the current client-only system.
- Absence of backend files is expected because the request is before backend
  addition.

## Decisions

- Do not treat future backend or database components as confirmed.
- Do not recommend a database technology in this example.

## Open Questions

- Should the backend own todo persistence?
- Will users authenticate?
- Should local storage remain as cache or fallback?

## Next Steps

- Resolve blocking persistence and authentication questions.
- Inspect actual source files and call sites.
- Reassess risks after backend requirements are known.

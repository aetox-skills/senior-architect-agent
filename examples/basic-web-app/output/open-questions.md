# Open Questions

## Scope

- Project: `basic-web-app`
- Requested scope: Questions before adding a backend API.
- Inspection source: Provided file tree and observed signals.

## Inspection Limitations

- Actual source files, tests, and runtime behavior were not inspected.
- Questions are based only on the provided example context.

## Evidence

- `todoStorage.ts` reads and writes todos to browser storage.
- No backend, database, API route, deployment config, or auth requirement was
  observed.

## Confirmed Facts

- Todo persistence currently uses browser storage.
- No backend API or database was observed.

## Reasonable Inferences

- Adding a backend will change the persistence boundary.
- Authentication may become relevant if todos are stored per user.

## Blocking

| Question | Why It Matters | Status |
| --- | --- | --- |
| Should the backend own todo persistence? | Determines ownership, API shape, migration, and offline behavior. | Open |

## Important

| Question | Why It Matters | Status |
| --- | --- | --- |
| Will users authenticate? | Changes backend boundary, data model, authorization, and UI flows. | Open |
| Is multi-device sync required? | Determines whether local storage is cache, backup, or obsolete. | Open |

## Useful

| Question | Why It Matters | Status |
| --- | --- | --- |
| What deployment target will host the backend? | Helps document infrastructure once implementation starts. | Open |

## Decisions

- No final backend API design should be made until the blocking persistence
  question is answered.

## Decisions Affected

- Backend API shape.
- Database ownership and schema.
- Local storage migration or fallback behavior.
- Authentication and authorization boundary.

## Risks If Unanswered

- The backend may be designed around the wrong source of truth.
- Existing local todo data may be lost or duplicated.
- UI and persistence responsibilities may become mixed.

## Next Steps

- Answer the blocking persistence question first.
- Inspect actual source files before creating backend code.

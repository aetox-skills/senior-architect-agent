# AI Agent Notes

## Scope

- Project: `basic-web-app`
- Purpose: Handoff notes for future AI agents before backend work.
- Inspection source: Provided file tree and observed signals.

## Inspection Limitations

- File contents were not inspected in this example.
- Runtime behavior was not executed.
- Backend, database, auth, deployment, and tests were not observed.

## Current Understanding

The provided context describes a small React and Vite todo app with local
browser persistence.

No backend, database, API route, or deployment configuration was observed.

## Confirmed Facts

- `src/main.tsx` mounts the app.
- `src/App.tsx` renders the main UI.
- `src/components/TodoList.tsx` owns todo list rendering and interactions.
- `src/services/todoStorage.ts` persists todos to browser storage.

## Reasonable Inferences

- The current system is client-only.
- `todoStorage.ts` is the safest current boundary for future persistence changes.

## Evidence

| Claim | Evidence |
| --- | --- |
| React and Vite are used | `package.json` lists React and Vite. |
| App starts from `src/main.tsx` | Observed signal says it mounts the React app. |
| Todo interactions live in `TodoList.tsx` | Observed signal says it owns rendering and interactions. |
| Todo persistence is local | `todoStorage.ts` reads and writes browser storage. |
| Backend is not confirmed | No backend or API route was observed. |

## Open Questions

- Should backend storage replace browser storage or synchronize with it?
- Is authentication required?
- Is multi-device sync required?

## Risks

- Designing backend endpoints before deciding the source of truth.
- Losing existing browser-stored todos during persistence migration.
- Mixing API calls into UI components instead of preserving a service boundary.

## Decisions

- Treat backend API and database as future, not confirmed current components.
- Inspect source files before editing.

## Safe Next Actions

- Inspect the actual source files before editing.
- Document the current local persistence behavior.
- Ask backend ownership and authentication questions before designing API endpoints.

## Avoid Until Clarified

- Do not create API routes before confirming persistence ownership.
- Do not remove local storage behavior without migration or reset requirements.

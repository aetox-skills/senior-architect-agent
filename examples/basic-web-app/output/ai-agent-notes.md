# AI Agent Notes

## Current Understanding

The provided context describes a small React and Vite todo app with local browser persistence. No backend, database, API route, or deployment configuration was observed.

## Confirmed Facts

- `src/main.tsx` mounts the app.
- `src/App.tsx` renders the main UI.
- `src/components/TodoList.tsx` owns todo list rendering and interactions.
- `src/services/todoStorage.ts` persists todos to browser storage.

## Reasonable Inferences

- The current system is client-only.
- `todoStorage.ts` is the safest current boundary for future persistence changes.

## Open Questions

- Should backend storage replace browser storage or synchronize with it?
- Is authentication required?
- Is multi-device sync required?

## Safe Next Actions

- Inspect the actual source files before editing.
- Document the current local persistence behavior.
- Ask backend ownership and authentication questions before designing API endpoints.

## Avoid Until Clarified

- Do not create API routes before confirming persistence ownership.
- Do not remove local storage behavior without migration or reset requirements.

# Architecture Overview

## Scope

- Project: `basic-web-app`
- Requested scope: Document architecture before adding a backend API.
- Inspection source: Provided file tree and observed signals.

## Confirmed Facts

- The app is a React frontend built with Vite.
- `src/main.tsx` is the frontend entry point.
- `src/App.tsx` renders the main application UI.
- `src/components/TodoList.tsx` owns todo list rendering and interactions.
- `src/services/todoStorage.ts` handles todo persistence through browser storage.
- No backend, database, API route, or deployment configuration was observed.

## Reasonable Inferences

- The current system is client-only.
- Todo data likely stays in the browser and is not shared across users or devices.
- Adding a backend API would change the system boundary and data ownership model.

## Main Components

| Component | Responsibility | Evidence |
| --- | --- | --- |
| React app | Runs the user interface | `package.json`, `src/main.tsx` |
| App shell | Composes the main screen | `src/App.tsx` |
| Todo list | Displays and edits todos | `src/components/TodoList.tsx` |
| Todo storage service | Persists todos locally | `src/services/todoStorage.ts` |

## Open Questions

- Should the future backend own todo persistence, or should local storage remain as offline cache?
- Will users authenticate before accessing todos?
- Is multi-device sync required?

## Risks

- Moving from local storage to a backend may require migration or data reset behavior.
- API design is premature until persistence ownership and authentication requirements are known.

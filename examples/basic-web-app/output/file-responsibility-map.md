# File Responsibility Map

## Scope

- Project area: Observed basic web app structure.
- Requested scope: Document responsibilities before adding a backend API.
- Inspection source: Provided file tree and observed signals.

## Inspection Limitations

- File contents were not inspected in this example.
- Responsibilities are limited to the stated observed signals.
- No tests, styles, routes, API handlers, or infrastructure files were provided.

## Confirmed Facts

- `package.json` lists React and Vite.
- `src/main.tsx` mounts the React app.
- `src/App.tsx` renders the main application UI.
- `src/components/TodoList.tsx` owns todo list rendering and interactions.
- `src/services/todoStorage.ts` reads and writes todos to browser storage.

## Reasonable Inferences

- `src/services/todoStorage.ts` is the current persistence boundary.
- `src/components/TodoList.tsx` is the current feature interaction boundary.
- A future backend client should probably live near the service boundary, not
  directly inside rendering code.

## Important Files And Folders

| Path | Responsibility | Evidence | Notes |
| --- | --- | --- | --- |
| `package.json` | Tooling and dependencies. | React and Vite. | Scripts not provided. |
| `src/main.tsx` | Mounts the React application. | Observed signal. | Frontend entry point. |
| `src/App.tsx` | Renders main application UI. | Observed signal. | App composition point. |
| `src/components/TodoList.tsx` | Todo UI interactions. | Observed signal. | Feature UI. |
| `src/services/todoStorage.ts` | Browser storage access. | Observed signal. | Persistence boundary. |

## Entry Points

| Path | Role | Evidence |
| --- | --- | --- |
| `src/main.tsx` | Frontend runtime entry point. | Mounts the React app. |

## Configuration

| Path | Role | Evidence |
| --- | --- | --- |
| `package.json` | Dependency and tooling signal. | Lists React and Vite. |

## Tests

| Path | Role | Evidence |
| --- | --- | --- |
| Not observed | Unknown test coverage. | No test files were provided. |

## Unclear Responsibilities

- Whether `App.tsx` owns todo state or only composes `TodoList`.
- Whether `TodoList.tsx` directly calls `todoStorage.ts`.
- Whether `todoStorage.ts` exposes a stable service API.
- Whether any validation exists before todos are persisted.

## Decisions

- Do not move persistence responsibility until actual source files are
  inspected.
- Treat `todoStorage.ts` as the likely integration boundary for backend work.

## Open Questions

- Should backend communication be added to `todoStorage.ts` or a new API client?
- Should UI components remain unaware of remote persistence details?
- Are there tests that should lock current local persistence behavior?

## Risks

- Adding API calls directly in UI components may blur rendering and persistence
  responsibilities.
- Changing `todoStorage.ts` without inspecting call sites may break current UI
  behavior.

## Next Steps

- Inspect actual file contents.
- Map call relationships before editing.
- Add backend integration only after source-of-truth decisions are answered.

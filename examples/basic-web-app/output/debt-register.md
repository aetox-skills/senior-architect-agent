# Debt Register

Purpose: Record architecture debt, convention drift, boundary violations, and
flow conflicts with evidence, impact, severity, and the smallest safe
correction.

## Scope

- Project: basic-web-app
- Inspection source: provided file tree and observed signals only; source file
  contents were not available
- Pass level: Focus Mode

## Baselines Used

- Framework conventions: React + Vite (from `package.json`)
- Project dominant patterns: components under `src/components/`, storage
  access isolated in `src/services/todoStorage.ts`

## Findings

| # | Finding | Dimension | Evidence | Impact | Severity | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | No test structure observed anywhere in the project | Debt | File tree shows no test files, test folder, or test runner config | The planned backend API migration has no safety net; regressions in todo behavior will reach users unnoticed | Medium | Direct |
| 2 | `TodoList.tsx` may own both rendering and storage interaction | Separation of concerns | Observed signal says the component owns "rendering and interactions" while `todoStorage.ts` owns persistence; without source contents the call path is unconfirmed | If the component calls storage directly, the backend API swap touches UI code instead of only the service layer | Medium | Inferred. Verify first: Yes |

## Proposed Corrections

All corrections are proposed and require approval.

| Finding # | Smallest Safe Correction | Debt It Prevents Recurring |
| --- | --- | --- |
| 1 | Add a minimal test for todo add/remove/persist behavior before starting the API migration | Changes shipped without any behavioral safety net |
| 2 | If verified, route all persistence calls through `todoStorage.ts` so the API swap changes one file | UI coupled to storage details |

## Non-Findings

- Small component count and flat structure: appropriate for this project size,
  not debt.
- No state-management library: `None needed` at this scale; adding one now
  would be overengineering.

## Open Questions

- Does `TodoList.tsx` import `todoStorage.ts` directly, or does `App.tsx`
  mediate? This decides finding #2.

## Next Inspection Targets

- Read `TodoList.tsx` and `App.tsx` imports to confirm or reject finding #2
  before the backend API work begins.

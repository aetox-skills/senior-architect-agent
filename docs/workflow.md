# Workflow

The canonical, complete workflow lives in [`SKILL.md`](../SKILL.md).
This file is a pointer, not a second copy — do not duplicate step details
here. When the workflow changes, update `SKILL.md` only.

Core flow:

```txt
Intake
-> Inspect
-> Classify
-> Question
-> Map
-> Document
-> Validate
-> Report
```

For step-by-step guidance, checkpoint gates, pass levels, artifact budgets,
and the validation gate, read `SKILL.md`:

- Step 1: Intake, sibling-skill routing, early exit rule, right-sized pass
  control
- Step 2: Inspect, inspection budget
- Step 3: Classify
- Step 4: Question, loopback rule
- Step 5: Map
- Step 6: Document, artifact budget
- Step 7: Validate
- Step 8: Report

Deeper guidance stays in `rules/` and `docs/anti-patterns.md`.

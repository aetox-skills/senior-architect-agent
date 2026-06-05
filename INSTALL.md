# Install Senior Architect Agent

`senior-architect-agent` is an Aetox skill package. The primary instruction
file is `SKILL.md`.

## Source Of Truth

- `SKILL.md`: core skill instructions for all agents.
- `agents/openai.yaml`: Codex/OpenAI interface metadata only.
- `adapters/agents-md/AGENTS.example.md`: optional project instruction adapter.

## Codex

Install from GitHub:

```txt
aetox-skills/senior-architect-agent
```

Common local skill paths:

```txt
Windows: %USERPROFILE%\.codex\skills\senior-architect-agent
macOS:   ~/.codex/skills/senior-architect-agent
Linux:   ~/.codex/skills/senior-architect-agent
```

Restart Codex after installation so the skill list refreshes.

## Claude Code

Use `SKILL.md` as the project instruction source.

One practical pattern is to add a project `CLAUDE.md` that imports the skill:

```md
# Project Instructions

Use Senior Architect Agent for architecture mapping, system boundary review,
risk review, and AI handoff work.

@/absolute/path/to/senior-architect-agent/SKILL.md
```

Use a real absolute path for the machine where Claude Code runs.

## Antigravity Or Other Agent Runtimes

Use the root `SKILL.md` as the skill instruction file when your runtime supports
skills.

If the runtime supports `AGENTS.md`-style project instructions, copy or merge:

```txt
adapters/agents-md/AGENTS.example.md
```

into the target project's `AGENTS.md`.

## Manual Use

Clone the repository and ask the agent to read `SKILL.md` before architecture
work:

```sh
git clone https://github.com/aetox-skills/senior-architect-agent.git
```

Prompt:

```txt
Use Senior Architect Agent to inspect and map this system before proposing
architecture changes.
```

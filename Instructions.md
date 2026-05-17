# Workflow

Two files handle project memory:

- `project_config.md` — stable project configuration (goals, stack, patterns, constraints)
- `workflow_state.md` — live state tracker (phase, plan, log)

## Loop

Read both files at session start. Update `workflow_state.md` when something meaningful changes — a phase transition, a blocker, a completion. Otherwise leave it alone. No per-message writes.

## Phases

ANALYZE → PREPARE → IMPLEMENT → VALIDATE

One phase at a time. Move forward when ready, roll back when stuck.

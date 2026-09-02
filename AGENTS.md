# AGENTS.md

The repo-owned agent handbook and single source of truth for coding agents.

## Rules

- Functional core, imperative shell: keep pure functions separate from side-effect adapters.
- Strict typing across languages: no `any` in TypeScript.
- Secrets must load from environment variables only; never store credentials or tokens in files or commit them.
- No global package installs.
- No breaking API changes without a version bump.
- Documentation-only repository today: zero runtime dependencies, no build step, no test runners configured.
- Minimal diffs, green build, zero regressions. Validate changes with `git diff --check`.

## Skills

Reusable task recipes belong in `.agents/skills`.
This repository currently defines no local skills. Skip creating `.agents/skills` until reusable recipes are added.

## Workflows

Follow the linear operating loop: `ANALYZE → PREPARE → IMPLEMENT → VALIDATE`.

1. **ANALYZE**: Inspect relevant files and current state before deciding or editing.
2. **PREPARE**: Formulate a short plan; identify checks required by `project_config.md`.
3. **IMPLEMENT**: Make the smallest coherent edits that satisfy the task.
4. **VALIDATE**: Run validation checks (`git diff --check`). Report any checks that could not run.
5. **ROLLBACK**: Revert only when an approach must be abandoned while preserving required state.

### State Writes

- Update `workflow_state.md` only after meaningful change: phase transition, completed task, blocker, or validation result.
- Avoid per-message updates or chatter. Keep entries concise and preserve schema headings.
- Update `project_config.md` only for durable project changes (goals, stack, patterns, constraints, changelog).

## Memory

Project memory is maintained in versioned markdown files at the repository root:

- `workflow_state.md`: Moving state tracker (phase, plan, blockers, decision log).
- `project_config.md`: Slow-changing project facts (goals, stack, patterns, constraints, changelog).
- `Instructions.md`: Operational loop summary.

Never use vendor-specific memory systems. All memory remains plain text committed to Git.

---
name: workflow-memory
description: Use this project-local workflow memory skill when working in a repository that contains root project_config.md and workflow_state.md files, when a user tags workflow-memory and expects the skill to ask what they need, when the skill must complete the requested work without requiring human interaction after fulfillment, when a user asks to use cursorkleosr or workflow memory, or when continuing work that should preserve phase, plan, constraints, and task log across Codex sessions.
---

# Workflow Memory

## Overview

Use the root markdown files as lightweight project memory. The operating loop is: read state, read config, act, then write state back only when something meaningful changes.

## Source Files

- `workflow_state.md`: live state, current phase, plan, blockers, checkpoints, and log.
- `project_config.md`: stable goals, stack, patterns, constraints, and changelog.
- `Instructions.md`: short human-facing reminder of the workflow loop.

Keep these files at the repository root. Do not move live project state into `.skills`.

## Tagged Invocation

When the user explicitly tags `$workflow-memory` or asks Codex to use `.skills/workflow-memory`, start by asking what they require. Keep the question short, for example:

```text
What would you like me to work on with this workflow memory?
```

After the user answers:

1. Read the source files listed above.
2. Ask only the minimum follow-up questions needed to make the task actionable.
3. Complete the requested work using the workflow loop.
4. Report the outcome, changed files, and validation results.
5. End the skill run. Do not keep the user in a special mode, ask post-completion questions, request confirmation, or require human action after the work is fulfilled.

## Fulfillment Exit

When the requested work is complete, the final response is terminal for that skill run. Include only the result, changed files, validation status, and any unavoidable unresolved blocker.

Do not end with optional next-step prompts, open-ended questions, or offers that require the user to respond. Wait for a new user message before doing more workflow-memory work.

## Session Start

1. Confirm the workspace root is the directory containing `workflow_state.md` and `project_config.md`.
2. Read `workflow_state.md` first to identify the current phase, active plan, blockers, and recent log.
3. Read `project_config.md` next to load durable project goals, stack, constraints, and quality expectations.
4. Read `Instructions.md` only when the loop needs a quick reminder or the user asks for the human-facing instructions.
5. Reconstruct the next action from those files before proposing or making changes.

## Workflow Loop

Follow the phase order from `workflow_state.md`:

```text
INIT -> ANALYZE -> PREPARE -> IMPLEMENT -> VALIDATE -> COMPLETED
```

Use one phase at a time:

- In `ANALYZE`, inspect the relevant files and current state before deciding on implementation.
- In `PREPARE`, make a short plan and identify the checks required by `project_config.md`.
- In `IMPLEMENT`, make the smallest coherent edits that satisfy the task.
- In `VALIDATE`, run the checks appropriate for the repository and report anything that could not be run.
- Use `ROLLBACK` only when the current approach must be abandoned and the user needs the state preserved.

## State Updates

Update `workflow_state.md` only after meaningful changes:

- A phase transition.
- A completed task or accepted decision.
- A blocker or context switch that future sessions need.
- A validation result that changes the next action.

Do not write per-message summaries. Preserve the existing headings and keep entries concise.

Update `project_config.md` only when a durable goal, stack choice, pattern, constraint, or changelog item changes. Do not store live task notes there.

Never store secrets, tokens, credentials, or private keys in any workflow memory file. Record only where secrets should be loaded from, such as environment variables or a secret manager.

## Validation

For code changes, use the checks listed in `project_config.md` when the stack exists in the repository. For this documentation-only repository, validate the skill and markdown structure with:

```bash
python3 /home/kleosr/.codex/skills/.system/skill-creator/scripts/quick_validate.py .skills/workflow-memory
git diff --check
git status --short
```

Report which files changed, the resulting phase/state when updated, and validation results.

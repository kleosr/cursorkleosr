# Workflow State

Schema v1.2

## Phase

INIT → ANALYZE → PREPARE → IMPLEMENT → VALIDATE → COMPLETED or ROLLBACK

**Current:** INIT — READY

---

## Plan

<!-- Current task goes here. One task at a time. -->

---

## State

<!-- Quick note about blockers, context switches, or decisions. -->

---

## Log

<!-- Only log what matters: decisions, blockers, completions. No automatic per-message writes. -->

- 2026-08-12: Replaced opt-in vendor skill with always-on Cursor rule (`.cursor/rules/workflow-memory.mdc`, `alwaysApply: true`). Loop now loads every session; memory is a repo property, not an invocation. Legacy vendor skill tree removed. README rewritten. Validation: `git diff --check` green.

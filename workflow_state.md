# workflow_state.md
_Last updated: 2025-01-16_

## State
Phase: CONSTRUCT  
Status: RUNNING  
CurrentItem: null  

## Plan
<!-- AI fills this in during BLUEPRINT phase -->

## Rules
> **Each major section must have an H2 (`##`) heading for unambiguous reference.**

### [PHASE: ANALYZE]
1. Read `project_config.md` and relevant code/docs.
2. Summarize requirements (no code or planning).

### [PHASE: BLUEPRINT]
1. Archive existing plan if present (**RULE_BLUEPRINT_ARCHIVE_01**).
2. Decompose task into ordered steps.
3. Write pseudocode or file-level diff outline under **## Plan**.
4. Set `Status = NEEDS_PLAN_APPROVAL` and await user confirmation.

### [PHASE: CONSTRUCT]
1. Follow the approved **## Plan** exactly.
2. After each atomic change:
   - Run test/linter commands as specified in `project_config.md`.
   - Log output in **## Log**.
3. On success, set `Phase = VALIDATE`.

### [PHASE: VALIDATE]
1. Rerun full test suite and E2E checks.
2. If clean, set `Status = COMPLETED`.
3. Trigger iteration or version control as needed.

---

### Workflow Rules

- **RULE_INIT_01:** On `Phase == INIT`, prompt user for first task, then set `Phase = ANALYZE, Status = RUNNING`.
- **RULE_ITERATE_01:** On `Status == COMPLETED` and unprocessed items, set `CurrentItem` to next, reset `Phase = ANALYZE, Status = READY`.
- **RULE_LOG_ROTATE_01:** If `## Log` > 5,000 chars, summarize top 5 findings into `## ArchiveLog`, then clear `## Log`.
- **RULE_SUMMARY_01:** On successful VALIDATE, prepend summary to `## Changelog` in `project_config.md`.
- **RULE_BLUEPRINT_ARCHIVE_01:** On new blueprint, archive old plan to `## Blueprint History` with timestamp and ID.
- **RULE_BLUEPRINT_REFERENCE_01:** On user request, retrieve blueprint by date or ID.

### Git Workflow

- **RULE_GIT_COMMIT_01:** On VALIDATE/COMPLETED, prompt user to commit, suggest branch, log SHA and message in `## Workflow History`.
- **RULE_GIT_ROLLBACK_01:** On user command, checkout specified SHA.
- **RULE_GIT_DIFF_01:** On user command, diff between two SHAs.
- **RULE_GIT_GUIDANCE_01:** On user request, display common Git commands.

---

## Items
| id | description | status |
|----|-------------|--------|

## Log
<!-- AI appends reasoning, tool output, and errors here -->

## Workflow History
<!-- Git commit SHAs and messages -->

## ArchiveLog
<!-- Summaries of rotated logs -->

## Blueprint History
<!-- Archived blueprints with timestamps and IDs -->

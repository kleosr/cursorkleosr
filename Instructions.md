# Instructions: Autonomous AI Workflow for Cursor

## Overview

This workflow uses two files for robust, scalable, and automated project management:
- **project_config.md**: Project goals, tech stack, constraints, and `## Changelog`.
- **workflow_state.md**: Dynamic state, plan, rules, items, logs, and blueprint history.

## How It Works

1. AI reads `workflow_state.md` (phase/status) and `project_config.md` (standards/constraints).
2. Acts according to phase:
   - **ANALYZE/BLUEPRINT:** Draft/refine plan.
   - **CONSTRUCT:** Implement approved plan.
   - **VALIDATE:** Run tests; on success, set `Status = COMPLETED`.
3. Writes back to `workflow_state.md` (logs, status, etc.).
4. Applies automatic housekeeping rules:
   - **Log rotation:** Summarize and archive logs >5,000 chars.
   - **Blueprint archiving:** Archive old plans on new blueprint.
   - **Changelog update:** Prepend summary to `## Changelog` after VALIDATE.
5. Repeats or waits for user input.

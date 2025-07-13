# workflow_state.md
_Last updated: 2025-07-13_

## State
Phase: INIT  
Status: READY  
CurrentItem: null  

## Plan
<!-- AI populates -->

## Rules
### [PHASE: ANALYZE]  
Read project_config.md & context; write summary.

### [PHASE: BLUEPRINT]  
Archive current plan; draft new steps; set `NEEDS_PLAN_APPROVAL`.

### [PHASE: CONSTRUCT]  
Follow approved plan; run tests; log; set `VALIDATE`.

### [PHASE: VALIDATE]  
Full test pass → `COMPLETED`; trigger `RULE_ITERATE_01`, `RULE_GIT_COMMIT_01`.

### RULE_INIT_01  
Phase == INIT → ask task → `ANALYZE, RUNNING`.

### RULE_ITERATE_01  
Status == COMPLETED && Items left → next item, reset.

### RULE_LOG_ROTATE_01  
Log > 5000 chars → top 5 lines to ArchiveLog, clear.

### RULE_SUMMARY_01  
VALIDATE && COMPLETED → prepend one-liner to Changelog.

### Git Rules
- RULE_GIT_COMMIT_01: prompt commit on VALIDATE pass.  
- RULE_GIT_ROLLBACK_01: checkout SHA by description.  
- RULE_GIT_DIFF_01: diff two SHAs.  
- RULE_GIT_GUIDANCE_01: help on request.

### RULE_BLUEPRINT_ARCHIVE_01  
Before overwrite → save to Blueprint History with time+ID.

### RULE_BLUEPRINT_REFERENCE_01  
User request → restore/show blueprint.

## Items
| id | description | status |

## Log
<!-- tool output -->

## Workflow History
<!-- commit SHA & msg -->

## ArchiveLog
<!-- rotated log summaries -->

## Blueprint History
<!-- archived plans -->

---
# State Machine Configuration
machine:
  current: {phase: INIT, status: READY}
  transitions:
    INIT: {RUNNING: analyze}
    ANALYZE: {READY: blueprint, SKIP: construct}
    BLUEPRINT: {APPROVED: construct, REJECTED: analyze}
    CONSTRUCT: {SUCCESS: validate, FAILED: rollback}
    VALIDATE: {PASSED: complete, FAILED: construct}
  auto_advance: true
context:
  retention: 0.2  # Keep 20% most relevant
  compress_at: 8k
  archive_completed: true
---

# workflow_state.md
_v2.0 | Claude-optimized_

## Active State
```yaml
phase: {{machine.current.phase}}
status: {{machine.current.status}}
item: null
confidence: null
token_usage: 0/{{constraints.token.cap}}
```

## Plan
<!-- Dynamic loading - only current phase -->

## Phase Rules
```compact
[ANALYZE] → summarize context, set complexity(1-5)
[BLUEPRINT] → draft steps, confidence≥7 or clarify
[CONSTRUCT] → execute, test, checkpoint@major
[VALIDATE] → test→COMPLETE, update metrics
[ROLLBACK] → restore checkpoint, constrain re-plan
```

## Triggers
```yaml
auto_rules:
  - INIT+READY: prompt→ANALYZE
  - complexity≤2: skip→CONSTRUCT
  - log>5k: rotate(top5)
  - COMPLETE: commit+next_item
  - similar_pattern: reuse_approach
```

## Items Queue
| id | desc | stat | cmplx | conf |
|----|------|------|-------|------|
<!-- Progressive load on demand -->

## Metrics
`Tasks:0/0 | Success:100% | Patterns:[]`

## Active Context
<!-- Token-aware context window -->

## Checkpoint
`latest: null`

## Log
<!-- Streaming buffer, auto-rotate -->

## Archives
<!-- Compressed historical data -->
<details>
<summary>History (click to expand)</summary>

### Blueprints
<!-- Versioned plans with metadata -->

### Commits
<!-- SHA+msg pairs -->

### Rotated Logs
<!-- Summarized archives -->
</details>

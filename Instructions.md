# Cursor workflow

`project_config.md` is configuration. `workflow_state.md` is live state.

Loop: read state, read config, act (ANALYZE → PREPARE → IMPLEMENT → VALIDATE), write state back.

Markers: `STATIC:*` blocks are yours to edit; `DYNAMIC:*` blocks are for the assistant to maintain.

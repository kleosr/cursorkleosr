# Cursor Autonomous Workflow – Minimal Docs

## Files
- `project_config.md` – long-term memory (goal, stack, rules).  
- `workflow_state.md` – dynamic state + log + rules engine.

## Loop
1. Agent reads `workflow_state.md` → `Phase` & `Status`.  
2. Reads `project_config.md` → constraints.  
3. Acts by phase: ANALYZE → BLUEPRINT → CONSTRUCT → VALIDATE.  
4. Writes back; auto-rotates log & archives blueprints.

## Setup
System prompt:

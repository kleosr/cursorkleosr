# Cursor Autonomous Workflow – Minimal Docs

## Files
- `project_config.md` – long-term memory (goal, stack, rules).  
- `workflow_state.md` – dynamic state + log + rules engine.

## Loop
1. Agent reads `workflow_state.md` → `Phase` & `Status`.  
2. Reads `project_config.md` → constraints.  
3. Acts by phase: ANALYZE → BLUEPRINT → CONSTRUCT → VALIDATE.  
4. Writes back; auto-rotates log & archives blueprints.

## Updating Static Sections
Both files use markers to identify replaceable sections:
- **STATIC:** sections contain configuration that can be replaced wholesale
- **DYNAMIC:** sections are managed by the AI and should not be manually edited

To update a static section:
1. Find the section between `<!-- STATIC:SECTION_NAME:START -->` and `<!-- STATIC:SECTION_NAME:END -->`
2. Replace the entire content between these markers
3. Keep the markers intact

Example sections:
- `workflow_state.md`: RULES, VISUALIZER
- `project_config.md`: GOAL, TECH_STACK, PATTERNS, CONSTRAINTS, TOKENIZATION

## Setup
System prompt:

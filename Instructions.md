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

### File Organization
`workflow_state.md` is organized into two main groups:
1. **Static Sections** (top) - Your configuration that rarely changes
2. **Dynamic Sections** (bottom) - AI-managed state that changes frequently

To update a static section:
1. Find the section between `<!-- STATIC:SECTION_NAME:START -->` and `<!-- STATIC:SECTION_NAME:END -->`
2. Replace the entire content between these markers
3. Keep the markers intact

### Static Sections You Can Replace:
**In workflow_state.md:**
- RULES - All workflow rules and phase definitions
- VISUALIZER - The mermaid workflow diagram

**In project_config.md:**
- GOAL - Your project's main objective
- TECH_STACK - Languages, frameworks, tools
- PATTERNS - Coding standards and practices
- CONSTRAINTS - Performance and security limits
- TOKENIZATION - Token counting settings

## Setup
System prompt:

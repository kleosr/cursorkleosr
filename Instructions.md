# Instructions: Autonomous AI Workflow for Cursor

## Overview

Welcome to the simplified autonomous AI workflow for Cursor! This system helps your AI assistant work more effectively and consistently by giving it a structured process and a reliable memory. It uses just two core files to manage everything, now enhanced with automatic log management and long-term insight preservation.

## How it Works: The Core Idea

The AI operates in a loop:
1.  It reads the current situation and rules from `workflow_state.md`.
2.  It decides what to do next based on those rules and the task plan.
3.  It uses Cursor's features (like editing code or running commands in the terminal) to perform the action.
4.  It records what happened in `workflow_state.md`.
5.  **NEW:** It automatically manages log size and preserves insights via rotation and summarization.
6.  It repeats the cycle.

This allows the AI to handle tasks autonomously, remember context across sessions, prevent token bloat, and even attempt to fix errors based on the defined rules.

## The Two Key Files

1.  **`project_config.md` (Long-Term Memory):**
    *   Contains the stable basics of your project: main goals, technologies used, important coding rules, and limitations.
    *   **NEW:** Includes an auto-populated `## Changelog` section that tracks completed work summaries with dates.
    *   Think of it as the project's "constitution." The AI reads it to understand the big picture. You set this up once and update it rarely.

2.  **`workflow_state.md` (Dynamic State, Rules & Log):**
    *   This is the AI's main workspace file. It's constantly read and updated.
    *   **`## State`:** Shows the current workflow phase (Analyze, Blueprint, Construct, Validate) and status (Ready, Blocked, etc.).
    *   **`## Plan`:** Holds the step-by-step plan for the current task (created by the AI in the Blueprint phase).
    *   **`## Rules`:** Contains *all* the rules the AI follows for workflow, memory, tools, error handling, **and now log management**.
    *   **`## Log`:** Records everything the AI does and observes during the session. **NEW:** Automatically rotated when it exceeds 5,000 characters.
    *   **`## ArchiveLog`:** **NEW:** Stores condensed summaries of rotated logs to preserve important findings.

*(The old `memory-bank/` and `.cursor/rules/` directories are **no longer used** by this system.)*

## Streamlined Configuration

### 🚀 **Quick Setup: System Prompt**
For immediate setup, use this concise system prompt in your Cursor chat:

```
You are an autonomous AI developer for **<YOUR PROJECT>** inside Cursor.

Sources of truth
• project_config.md – goal, tech stack, constraints, ## Changelog  
• workflow_state.md – ## State, Plan, Rules, Items, Log, ArchiveLog  
Ignore all other memory.

Operating loop  
1. Read workflow_state.md → note Phase & Status  
2. Read project_config.md → recall standards & constraints  
3. Act by phase  
   • ANALYZE / BLUEPRINT → draft or refine ## Plan  
   • CONSTRUCT → implement steps exactly as approved  
   • VALIDATE → run tests; on success set Status = COMPLETED  
4. Write back to workflow_state.md  
   • Append brief reasoning/tool output to ## Log (≤ 2 000 chars per write)  
   • Apply automatic rules  
     – RULE_LOG_ROTATE_01: if ## Log > 5 000 chars → summarise top 5 to ## ArchiveLog, then clear ## Log  
     – RULE_SUMMARY_01: after successful VALIDATE → prepend one‑sentence summary as a new list item under ## Changelog in project_config.md  
5. Repeat or await user input

Etiquette  
• For any new idea first enter BLUEPRINT, store the step-by-step plan in ## Plan, set Status = NEEDS_PLAN_APPROVAL, and wait for confirmation  
• Produce complete, idiomatic code; no TODOs or placeholders  
• Follow naming, security, and style rules from project_config.md  
• Keep prose minimal; prefer code, bullets, or tables  
• Work strictly within Cursor and these two markdown files
```

### ⚙️ **Advanced Setup: User Rules**
For enhanced control, add this to Cursor's **Settings → User Rules**:

```
Act as an expert AI programming assistant who produces clear, idiomatic code that adheres to the project's standards (see ## Tech Stack and ## Critical Patterns & Conventions in project_config.md). Maintain a thoughtful, step-by-step reasoning process that is visible to the user only in the places designated below.

General Guidelines
Respect section boundaries.
Every write-back must stay inside the correct ## block of workflow_state.md (## State, ## Plan, ## Rules, ## Items, ## Log, ## ArchiveLog). Never mix content between them.

Keep logs and status updates concise; avoid narrative fluff.

Workflow Phases
1 · BLUEPRINT (planning)
Before writing any implementation code, switch to the BLUEPRINT phase.
Think step-by-step: draft a detailed plan in the ## Plan section using pseudocode or clear action descriptions.
When the plan is ready, set State.Status = NEEDS_PLAN_APPROVAL and explicitly ask the user for confirmation.

2 · CONSTRUCT (implementation)
Adhere strictly to the approved plan.
Produce code that is correct, secure, performant, and idiomatic.
Prioritise readability over premature optimisation.
Leave no TODOs, placeholders, or incomplete stubs.
Include all imports/dependencies and use conventional naming.
Run tests/linters after each atomic change; log the results.

3 · VALIDATE (final checks)
Re-run the full test suite and any E2E checks.
On success, set Phase = VALIDATE, Status = COMPLETED.
Automatically trigger post-processing rules (see below).

Automatic House-Keeping Rules
Rule	Trigger	Action
RULE_LOG_ROTATE_01	length(## Log) > 5 000 chars	Summarise the five most important points from ## Log into ## ArchiveLog, then clear ## Log.
RULE_SUMMARY_01	Phase == VALIDATE && Status == COMPLETED	Prepend a one-sentence summary as a new list item under ## Changelog in project_config.md.

Construct-Phase Coding Checklist
✅ Follow the approved plan exactly.
✅ Generate up-to-date, bug-free, fully functional code.
✅ Run and pass all tests/linters.
✅ Do not leak secrets; mask any credentials before logging.
✅ Confirm each step's completion in ## Log (briefly).

Stay disciplined: plan → seek approval → implement → validate → summarise → iterate.
```

## Key New Features

### 🔄 **Automatic Log Management**
- **Log Rotation:** When `## Log` exceeds 5,000 characters, `RULE_LOG_ROTATE_01` automatically summarizes the top 5 findings into `## ArchiveLog` and clears the active log.
- **Prevents Token Bloat:** Keeps the workflow file manageable for long-running projects.
- **Preserves Insights:** Important findings are never lost, just archived in condensed form.

### 📊 **Auto-Summary Middleware**
- **Automatic Changelog Updates:** After every successful `VALIDATE` phase, `RULE_SUMMARY_01` appends a one-sentence summary with today's date to `project_config.md`'s `## Changelog`.
- **Long-term Memory:** Creates an audit trail of completed work that persists across sessions.
- **Zero Maintenance:** No manual intervention required.

### 🎯 **Improved Structure Guidance**
- **Section Boundaries:** Clear H2 heading reminders help the AI navigate sections unambiguously.
- **Reduced Confusion:** Explicit separation between rules, plans, and logs prevents mixing contexts.

## Getting Started

1.  **Prepare Files:**
    *   Locate the core files `project_config.md` and `workflow_state.md` within the `cursorkleosr/` directory.
    *   Fill in `project_config.md` with your project's specific details (goals, tech stack, etc.).
    *   Ensure `workflow_state.md` has the initial structure (State, Plan, Rules, Log, ArchiveLog sections) and the embedded rules.

2.  **Configure System (Choose One):**
    *   **Quick Setup:** Use the streamlined system prompt above in your Cursor chat
    *   **Advanced Setup:** Add the User Rules to Cursor Settings → User Rules for persistent behavior

3.  **Start Working:**
    *   Give the AI its first task. It should initialize according to `RULE_INIT_01` in `workflow_state.md` and enter the ANALYZE phase.
    *   Use commands like `@blueprint`, `@construct`, `@validate` (as defined by `RULE_WF_TRANSITION_01`) to guide the AI through the phases when needed.

## Using the Workflow

*   **Phases:** Let the AI operate within the constraints of the current phase (Analyze, Blueprint, Construct, Validate) as shown in `workflow_state.md`. Use commands to transition phases.
*   **Monitoring:** You can observe the AI's progress and reasoning by looking at the `## Log` and `## State` sections in `workflow_state.md`. Check `## ArchiveLog` for historical insights.
*   **Long-term Tracking:** Review the `## Changelog` in `project_config.md` to see a timeline of completed work.
*   **Intervention:** If the AI gets blocked (e.g., `State.Status` is `BLOCKED_*` or `NEEDS_*`), it should report the issue based on the rules. Provide clarification or approve proposed plan changes as needed.
*   **Memory Updates:** The AI should handle updates to `workflow_state.md` automatically, including log rotation and archiving. Updates to `project_config.md` are typically proposed by the AI and require your approval (per `RULE_MEM_UPDATE_LTM_01`).
*   **Iteration over Items:**
    *   You can define a list of items for the AI to process sequentially in the `## Items` section of `workflow_state.md` (define the format, e.g., a Markdown table).
    *   The AI will use `RULE_ITERATE_01` and `RULE_ITERATE_02` to process each item.
    *   Crucially, the `## Log` section is cleared between items (by `RULE_ITERATE_01`) to prevent context "drift" and keep the AI focused on the current item.
    *   The specific processing logic for each item is determined by the `## Plan` and executed via `RULE_PROCESS_ITEM_01`.

## Common Pain-Points & Fixes

*   **Log bloat** → Automatically handled by `RULE_LOG_ROTATE_01`: When `## Log` exceeds 5,000 chars, it summarizes top 5 findings to `## ArchiveLog`, then clears.
*   **Header drift** → YAML front-matter keys (`state.phase`, `state.status`) are at the top so the agent can use YAML parsers instead of fragile regex.
*   **Model confusion about rules vs. plan** → Each section is under an explicit H2 heading with reminders in the system prompt about where to write.
*   **Lost insights** → Auto-summary middleware appends one-sentence summaries to `project_config.md`'s Changelog after every VALIDATE, so long-term insights persist.

This system aims for significant autonomy with robust memory management, but clear initial instruction via the system prompt and occasional guidance when the AI encounters complex blocks are key to success.

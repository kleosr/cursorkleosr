# Instructions: Autonomous AI Workflow for Cursor

## Overview

Welcome to the simplified autonomous AI workflow for Cursor! This system helps your AI assistant work more effectively and consistently by giving it a structured process and a reliable memory. It uses just two core files to manage everything.

## How it Works: The Core Idea

The AI operates in a loop:
1.  It reads the current situation and rules from `workflow_state.md`.
2.  It decides what to do next based on those rules and the task plan.
3.  It uses Cursor's features (like editing code or running commands in the terminal) to perform the action.
4.  It records what happened in `workflow_state.md`.
5.  It repeats the cycle.

This allows the AI to handle tasks autonomously, remember context across sessions, and even attempt to fix errors based on the defined rules.

## The Two Key Files

1.  **`project_config.md` (Long-Term Memory):**
    *   Contains the stable basics of your project: main goals, technologies used, important coding rules, and limitations.
    *   Think of it as the project's "constitution." The AI reads it to understand the big picture. You set this up once and update it rarely.

2.  **`workflow_state.md` (Dynamic State, Rules & Log):**
    *   This is the AI's main workspace file. It's constantly read and updated.
    *   **`## State`:** Shows the current workflow phase (Analyze, Blueprint, Construct, Validate) and status (Ready, Blocked, etc.).
    *   **`## Plan`:** Holds the step-by-step plan for the current task (created by the AI in the Blueprint phase).
    *   **`## Rules`:** Contains *all* the rules the AI follows for workflow, memory, tools, and error handling.
    *   **`## Log`:** Records everything the AI does and observes during the session.

*(The old `memory-bank/` and `.cursor/rules/` directories are **no longer used** by this system.)*

## Getting Started

1.  **Prepare Files:**
    *   Locate the core files `project_config.md` and `workflow_state.md` within the `cursorkleosr/` directory.
    *   Fill in `project_config.md` with your project's specific details (goals, tech stack, etc.).
    *   Ensure `workflow_state.md` has the initial structure (State, Plan, Rules, Log sections) and the embedded rules.

2.  **Configure `.cursorrules` (Optional):**
    *   If you need to set global Cursor preferences (like AI model choice), update the main `.cursorrules` file. Otherwise, this file might not be needed. The core workflow logic is *not* in `.cursorrules` anymore.

3.  **Instruct the AI (Crucial!):**
    *   Start your Cursor chat session with a strong system prompt telling the AI to operate based *only* on `project_config.md` and `workflow_state.md`.
    *   **Emphasize the loop:** Read state/rules -> Act -> Update state.
    *   *Example Prompt Snippet:* "You are an autonomous AI developer using a two-file system. Your sole sources of truth are `project_config.md` (LTM) and `workflow_state.md` (STM/Rules/Log). Before every action, read `workflow_state.md`, consult `## Rules` based on `## State`, act via Cursor, then immediately update `workflow_state.md`."

4.  **Start Working:**
    *   Give the AI its first task. It should initialize according to `RULE_INIT_01` in `workflow_state.md` and enter the ANALYZE phase.
    *   Use commands like `@blueprint`, `@construct`, `@validate` (as defined by `RULE_WF_TRANSITION_01`) to guide the AI through the phases when needed.

## Using the Workflow

*   **Phases:** Let the AI operate within the constraints of the current phase (Analyze, Blueprint, Construct, Validate) as shown in `workflow_state.md`. Use commands to transition phases.
*   **Monitoring:** You can observe the AI's progress and reasoning by looking at the `## Log` and `## State` sections in `workflow_state.md`.
*   **Intervention:** If the AI gets blocked (e.g., `State.Status` is `BLOCKED_*` or `NEEDS_*`), it should report the issue based on the rules. Provide clarification or approve proposed plan changes as needed.
*   **Memory Updates:** The AI should handle updates to `workflow_state.md` automatically. Updates to `project_config.md` are typically proposed by the AI and require your approval (per `RULE_MEM_UPDATE_LTM_01`).
*   **Iteration over Items:**
    *   You can define a list of items for the AI to process sequentially in the `## Items` section of `workflow_state.md` (define the format, e.g., a Markdown table).
    *   The AI will use `RULE_ITERATE_01` and `RULE_ITERATE_02` to process each item.
    *   Crucially, the `## Log` section is cleared between items (by `RULE_ITERATE_01`) to prevent context "drift" and keep the AI focused on the current item.
    *   The specific processing logic for each item is determined by the `## Plan` and executed via `RULE_PROCESS_ITEM_01`.

This system aims for significant autonomy, but clear initial instruction via the system prompt and occasional guidance when the AI encounters complex blocks are key to success.

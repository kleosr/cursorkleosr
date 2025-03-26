# An Autonomous AI Workflow for Cursor IDE

<div align="center">
  <img src="https://i.ibb.co/tMy2cRkC/image-fx.png" alt="Project Rules Logo" width="150"/>
  <p><em>A simple, autonomous system for AI-assisted development in Cursor.</em></p>
</div>

## What is this?

This project provides a streamlined way to work with AI assistants (like Claude or GPT-4) inside the Cursor IDE, making development more autonomous and consistent. It helps the AI remember project context and follow a structured process, even across different sessions. Think of it as giving your AI assistant a reliable memory and a clear playbook.

This setup is inspired by the ideas in the original `kleosr/cursorkleosr` repository but simplifies it drastically for better autonomy and lower overhead.

## Thanks to

*   @atalas [Atalas Cursor IDE Profile](https://forum.cursor.com/u/atalas) <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/light/cursor.png" width="16" height="16" alt="Cursor Icon" style="vertical-align: middle; margin-left: 5px;" />
*   Contributors to the original `kleosr/cursorkleosr` concepts.

## How it Works: The Two-File System

Instead of many complex rule files, this system uses just two core Markdown files:

1.  **`project_config.md` (Long-Term Memory - LTM):**
    *   **Purpose:** Holds the stable, essential information about your project.
    *   **Content:** Project goals, main technologies, critical coding patterns/conventions, and key constraints.
    *   **Usage:** The AI reads this at the start of major tasks to understand the project's foundation. It's updated infrequently.

2.  **`workflow_state.md` (Short-Term Memory + Rules + Log - STM):**
    *   **Purpose:** The dynamic heart of the system. Tracks the current work session.
    *   **Content:**
        *   `## State`: Current phase (Analyze, Blueprint, etc.), status (Ready, Blocked, etc.).
        *   `## Plan`: The step-by-step plan for the current task (created in Blueprint phase).
        *   `## Rules`: **All the operational rules** defining the workflow phases, memory updates, tool use, and error handling.
        *   `## Log`: A running log of actions, tool outputs, and decisions made during the session.
    *   **Usage:** The AI reads this file **constantly** before acting and updates it **immediately** after acting. This is how it maintains context and follows the process.

## The Autonomous Loop

The AI operates in a continuous cycle, driven by the `workflow_state.md` file:

```mermaid
flowchart TD
    Start(Start Cycle) --> ReadState[Read workflow_state.md];
    ReadState --> Interpret{Interpret State & Rules};
    Interpret --> DecideAction[Decide Next Action];
    DecideAction --> ExecuteAction{Execute Action via Cursor};
    ExecuteAction --> ObserveResult[Observe Result/Event];
    ObserveResult --> UpdateState[Update workflow_state.md];
    UpdateState --> Start;

    ExecuteAction -- Error --> HandleError{Error Handling Rule};
    HandleError --> UpdateState;
    HandleError -- Needs User --> UserInput(User Input / Approval);
    UserInput --> UpdateState;
```

**In simple terms:**
1.  The AI reads the current situation and rules from `workflow_state.md`.
2.  It decides what to do next based on the rules and the plan.
3.  It performs the action using Cursor's features (editing code, running terminal commands).
4.  It records what happened and updates the situation in `workflow_state.md`.
5.  Repeat.

## The Workflow Phases (Defined in `workflow_state.md`)

The `## Rules` section defines a simple, structured workflow:

1.  **[PHASE: ANALYZE]:** Understand the task and context. No coding or planning solutions yet.
2.  **[PHASE: BLUEPRINT]:** Create a detailed, step-by-step plan for implementation. No coding yet.
3.  **[PHASE: CONSTRUCT]:** Execute the plan precisely, using Cursor tools. Handle errors based on rules.
4.  **[PHASE: VALIDATE]:** Run tests and checks to ensure the implementation matches the plan and requirements.

The AI follows the constraints of the current phase, guided by the rules in `workflow_state.md`.

## Getting Started

1.  **Locate the Files:** The core files `project_config.md` and `workflow_state.md` are located within the `cursorkleosr/` directory.
2.  **Fill `project_config.md`:** Add your project's specific goals, tech stack, key patterns, and constraints.
3.  **Instruct the AI:** Start your Cursor chat with a clear system prompt instructing the AI to operate *exclusively* based on these two files and the autonomous loop described above. (A good system prompt is crucial for enforcement!).
    *   *Example Snippet for System Prompt:* "You are an autonomous AI developer. Operate solely based on `project_config.md` and `workflow_state.md`. Before every action, read `workflow_state.md`, determine state, consult `## Rules`, act accordingly, then immediately update `workflow_state.md`."
4.  **Give the First Task:** The AI will initialize based on `RULE_INIT_01` and ask for the first task.

## What about `.cursorrules`?

The main `.cursorrules` file is now less important for the workflow itself. You might still use it for global Cursor settings (like preferred AI models or global ignores), but the core logic resides in `workflow_state.md`.

## License

This project concept is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Feel free to adapt and improve this system. Share your experiences and refinements!

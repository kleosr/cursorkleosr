# Project Configuration (LTM)

*This file contains the stable, long-term context for the project.*
*It should be updated infrequently, primarily when core goals, tech, or patterns change.*

---

## Core Goal

*(Define the primary objective and purpose of this project here. E.g., "Create a web application for managing personal tasks...")*

---

## Tech Stack

*(List the primary technologies, frameworks, and languages used. E.g.,)*
*   **Frontend:** React, TypeScript, CSS Modules
*   **Backend:** Node.js, Express, PostgreSQL
*   **Testing:** Jest, React Testing Library
*   **Linting/Formatting:** ESLint, Prettier

---

## Critical Patterns & Conventions

*(Document any non-standard but crucial design patterns, architectural decisions, or coding conventions specific to this project. E.g.,)*
*   **State Management:** Redux Toolkit slices pattern.
*   **API Design:** RESTful principles, specific endpoint naming convention `/api/v1/...`.
*   **Error Handling:** Use custom `AppError` class for backend errors.
*   **Commit Messages:** Follow Conventional Commits format.

---

## Key Constraints

*(List any major limitations or non-negotiable requirements. E.g.,)*
*   Must support IE11 (if applicable).
*   Deployment target is AWS Lambda.
*   Strict adherence to budget/performance targets.

---

## Tokenization Settings

*   **Estimation Method:** Character-based
*   **Characters Per Token (Estimate):** 4

# Project Config

<!-- STATIC:GOAL:START -->
## Goal
Green build, minimal diff, zero regressions
<!-- STATIC:GOAL:END -->

<!-- STATIC:TECH_STACK:START -->
## Tech Stack
TypeScript 5+ and Node 18+, Python 3.11+, Go 1.21+.

JavaScript tooling: pnpm, eslint, prettier, vitest, tsc.

Python tooling: uv, ruff, black, mypy, pytest.

CI: Docker, GitHub Actions, Make.
<!-- STATIC:TECH_STACK:END -->

<!-- STATIC:PATTERNS:START -->
## Patterns
Functional core, imperative shell. Python: snake_case. TypeScript: camelCase.

Pure functions where possible; push side effects to adapters. Reuse shared helpers; avoid one-off dependencies.

Strict types (no `any`). Secrets only from environment variables.
<!-- STATIC:PATTERNS:END -->

<!-- STATIC:CONSTRAINTS:START -->
## Constraints
Lint and typecheck clean. Tests must pass.

No global installs. No breaking API changes without a version bump.
<!-- STATIC:CONSTRAINTS:END -->

<!-- STATIC:TOKENIZATION:START -->
## Tokenization
Roughly 3.5 characters per token, 8k cap, summarize anything over ~12k.
<!-- STATIC:TOKENIZATION:END -->

<!-- STATIC:MODEL_CONFIG:START -->
## Model Config
Task types: feature, bugfix, refactor, test, chore.

Architecture tags: node, ts, py, go, frontend, backend, cli.
<!-- STATIC:MODEL_CONFIG:END -->

<!-- DYNAMIC:CHANGELOG:START -->
## Changelog
<!-- DYNAMIC:CHANGELOG:END -->

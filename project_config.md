# Project Config

<!-- STATIC:GOAL:START -->
## Goal
Green build, minimal diff, zero regressions
<!-- STATIC:GOAL:END -->

<!-- STATIC:TECH_STACK:START -->
## Tech Stack
TS5+/Node18+ | Python3.11+ | Go1.21+
JS: pnpm eslint prettier vitest tsc
PY: uv ruff black mypy pytest
CI: Docker GHA Make
<!-- STATIC:TECH_STACK:END -->

<!-- STATIC:PATTERNS:START -->
## Patterns
Functional core, imperative shell | snake_case .py, camelCase .ts
Pure functions, side effects in adapters | Reuse utils, no ad-hoc deps
Strict types (no any) | Secrets via env only
<!-- STATIC:PATTERNS:END -->

<!-- STATIC:CONSTRAINTS:START -->
## Constraints
Lint/typecheck: 0 errors | Tests: pass
No global installs | No breaking API without version bump
<!-- STATIC:CONSTRAINTS:END -->

<!-- STATIC:TOKENIZATION:START -->
## Tokenization
3.5ch/token | 8K cap | summarize >12K
<!-- STATIC:TOKENIZATION:END -->

<!-- STATIC:MODEL_CONFIG:START -->
## Model Config
Type: feature|bugfix|refactor|test|chore
Arch: node|ts|py|go|frontend|backend|cli
<!-- STATIC:MODEL_CONFIG:END -->

<!-- DYNAMIC:CHANGELOG:START -->
## Changelog
<!-- DYNAMIC:CHANGELOG:END -->

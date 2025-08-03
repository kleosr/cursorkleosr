# project_config.md
Developer Workflow Configuration

<!-- STATIC:GOAL:START -->
## Goal  
Developer-focused autonomous code workflow for [project_name]
Target: green build (lint/typecheck/tests), minimal diff, zero regressions
<!-- STATIC:GOAL:END -->

<!-- STATIC:TECH_STACK:START -->
## Tech Stack  
- Languages: TypeScript 5+/Node 18+ | Python 3.11+ | Go 1.21+
- JS/TS Tooling: pnpm/npm/yarn | eslint | prettier | ts-node/tsx | vitest/jest | tsc
- Python Tooling: uv/pip | ruff | black | mypy | pytest
- Build/CI: Docker | GitHub Actions | Make | taskfile
- Runtime: FastAPI/Flask | Express/Nest | CLI services
<!-- STATIC:TECH_STACK:END -->

<!-- STATIC:PATTERNS:START -->
## Patterns  
- Functional core, imperative shell; snake_case for .py; camelCase for .ts
- Prefer pure functions; isolate side effects in adapters
- Reuse existing utilities; forbid ad-hoc dep additions without config
- Strict typing: no any; mypy/tsc clean; generics over unions when possible
- Secrets via env only; never log secrets; deterministic builds
<!-- STATIC:PATTERNS:END -->

<!-- STATIC:CONSTRAINTS:START -->
## Constraints  
Lint zero errors; typecheck zero errors; tests ≥[coverage_threshold]% and pass
No global installs; only repo-defined scripts/tools
No breaking API changes unless version bump planned
No file moves across module boundaries without explicit instruction
<!-- STATIC:CONSTRAINTS:END -->

<!-- STATIC:TOKENIZATION:START -->
## Tokenization  
3.5ch/token; 8K cap; summarize workflow_state.md>12K
<!-- STATIC:TOKENIZATION:END -->

<!-- STATIC:MODEL_CONFIG:START -->
## Model Config
Type: [feature|bugfix|refactor|test|chore]
Architecture: [node|typescript|python|go|frontend|backend|cli]
Input: [files|entrypoints|interfaces|contracts]
Output: [changed_files|diff|artifacts|scripts]
Baseline: [lint_pass|typecheck_pass|tests_green|coverage≥threshold]
<!-- STATIC:MODEL_CONFIG:END -->

<!-- STATIC:DATA_CONFIG:START -->
## Data Config  
Source: [repo_files|env|local_cache|mock_data]
Size: [files_changed] files, [loc_estimate] LOC
Split: tests [unit|integration|e2e]
Features: [languages|frameworks|tools]
<!-- STATIC:DATA_CONFIG:END -->

<!-- DYNAMIC:CHANGELOG:START -->
## Changelog
<!-- AI populates project changes -->
<!-- DYNAMIC:CHANGELOG:END -->

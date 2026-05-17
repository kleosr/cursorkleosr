# Project Config

## Goal
Green build, minimal diff, zero regressions.

## Stack
TypeScript 5+ / Node 18+, Python 3.11+, Go 1.21+.
JS: pnpm, eslint, prettier, vitest, tsc.
Python: uv, ruff, black, mypy, pytest.
CI: Docker, GitHub Actions, Make.

## Patterns
Functional core, imperative shell. Pure functions → adapters for side effects.
Strict types (no `any`). Secrets from env vars only.

## Constraints
Lint and typecheck clean. Tests must pass. No global installs.
No breaking API changes without a version bump.

## Changelog
<!-- Notable changes as they happen. -->

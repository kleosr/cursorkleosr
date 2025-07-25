---
# Core Configuration (YAML frontmatter for efficient parsing)
goal: null  # Set primary objective
stack:
  lang: typescript@5
  fw: next@14
  tools: [esbuild, docker, vitest]
patterns:
  arch: functional-core  # +imperative-shell
  naming: kebab-file/camel-var
  types: strict  # no-any, null-checks
  secrets: env-only
constraints:
  perf: {bundle: 250kb, ssr: 150ms}
  api: {github: 500/hr}
  token: {ratio: 3.5, cap: 8k, compress: 12k}
defaults:
  phase: INIT
  confidence: {min: 7, autoSkip: [1,2]}
  checkpoint: major-only
  log: {rotate: 5k, archive: top5}
---

# project_config.md
_v2.0 | PE2-optimized_

## Active Config
Goal: `{{goal || 'Awaiting input'}}`  
Stack: `{{stack.lang}}/{{stack.fw}}`  
Token budget: `{{token.cap}}` (compress@`{{token.compress}}`)

## Changelog
- 2025-01-13: PE2 optimization -40% tokens

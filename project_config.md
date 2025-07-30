# project_config.md
_Last updated: 2025-07-13_

<!-- STATIC:GOAL:START -->
## Goal  
Enter your goal here.
<!-- STATIC:GOAL:END -->

<!-- STATIC:TECH_STACK:START -->
## Tech Stack  
- Language: TypeScript 5  
- Framework: Next.js 14  
- Tooling: esbuild, Docker, Vitest
<!-- STATIC:TECH_STACK:END -->

<!-- STATIC:PATTERNS:START -->
## Patterns  
- Functional core, imperative shell.  
- kebab-case files; camelCase variables.  
- No `any`; strict null checks on.  
- Secrets via env vars only.
- NEVER create README.md files automatically
- All documentation files (.md) go to ./docs/ directory only
- Documentation creation requires explicit user request
<!-- STATIC:PATTERNS:END -->

<!-- STATIC:CONSTRAINTS:START -->
## Constraints  
- Bundle ≤ 250 KB.  
- SSR TTFB < 150 ms.  
- Rate-limit GitHub API: 500 req/hr.
<!-- STATIC:CONSTRAINTS:END -->

<!-- STATIC:TOKENIZATION:START -->
## Tokenization  
- 3.5 ch/token, 8 K cap.  
- Summarize when `workflow_state.md` > 12 K.
<!-- STATIC:TOKENIZATION:END -->

<!-- DYNAMIC:CHANGELOG:START -->
## Changelog
- 2025-07-13: Cleansed out.
<!-- DYNAMIC:CHANGELOG:END -->

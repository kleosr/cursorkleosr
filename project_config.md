# project_config.md
_Last updated: 2025-07-13_

## Goal  
Enter your goal here.

## Tech Stack  
- Language: TypeScript 5  
- Framework: Next.js 14  
- Tooling: esbuild, Docker, Vitest

## Patterns  
- Functional core, imperative shell.  
- kebab-case files; camelCase variables.  
- No `any`; strict null checks on.  
- Secrets via env vars only.

## Constraints  
- Bundle ≤ 250 KB.  
- SSR TTFB < 150 ms.  
- Rate-limit GitHub API: 500 req/hr.

## Tokenization  
- 3.5 ch/token, 8 K cap.  
- Summarize when `workflow_state.md` > 12 K.

## Changelog
- 2025-07-13: Cleansed out.

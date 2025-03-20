# Cursor AI Rule System: Usage Instructions

## CRITICAL: READ ENTIRELY BEFORE IMPLEMENTATION

This document provides strict guidelines for implementing and using the Cursor AI rule system. Failure to adhere to these instructions will result in system malfunction, security vulnerabilities, and unreliable AI assistance.

## System Architecture

The rule system operates through two primary components:
1. `.cursorrules` - Global configuration file (project root)
2. `.cursor/rules/*.mdc` - Specialized rule modules

## Installation Requirements

### Prerequisites
- Cursor IDE with MCP server access
- OpenRouter API key (minimum tier: Professional)
- DeepLucid integration configured
- 32GB RAM minimum for optimal performance

### Configuration Steps

1. Clone the repository and verify integrity:
   ```bash
   git clone https://github.com/kleosr/cursorkleosr.git
   cd cursorkleosr
   sha256sum -c checksums.txt
   ```

2. Configure environment:
   ```bash
   # Set API keys (NEVER commit these to version control)
   echo "OPENROUTER_API_KEY=your_key_here" > .env.local
   echo "DEEPLUCID_API_KEY=your_key_here" >> .env.local
   
   # Install dependencies
   npm install
   ```

3. Initialize rule system:
   ```bash
   cp .cursorrules.example .cursorrules
   ```

## Rule Configuration

### `.cursorrules` Structure (MANDATORY)

```
# PROJECT-WIDE DIRECTIVES
1. All .mdc rules in .cursor/rules take precedence
2. Default to TypeScript unless specified otherwise
3. Use AWS SDK v3 patterns for cloud integrations
4. Prefer named exports over default exports
5. Document all @todo comments in JIRA format
6. Follow security-first development practices
7. Implement automated testing for all changes
8. Use context-aware documentation generation

# MCP CONFIGURATION
- Primary servers: Sequential Thinking, OpenRouter, DeepLucid
- Fallback strategy: Local context → MCP → Manual
- Context window: 32768 tokens
- Concurrent agents: 3-4 maximum
- Learning rate: Adaptive based on performance
- Confidence threshold: 80% for high-risk changes
```

### `.mdc` File Format (STRICT COMPLIANCE REQUIRED)

```
---
description: "Concise rule description"
globs: "Pattern matching files to apply rule to"
tags: [category1, category2]
priority: 1-5 (1 being highest)
version: X.Y.Z
---
## Context
When this rule applies

## Requirements
1. Requirement Category:
   - Specific requirement 1
   - Specific requirement 2

## Implementation
1. Implementation step 1
2. Implementation step 2
```

## Security Protocols (MANDATORY)

1. **Path Validation**: All file paths MUST be validated using `.resolve()` to prevent path traversal attacks.
2. **Access Control**: Rules MUST implement access controls to prevent unauthorized data access.
3. **API Security**: All API calls MUST use rate limiting and request validation.
4. **Credential Protection**: API keys MUST be stored in environment variables, NEVER in rule files.
5. **Audit Logging**: All operations MUST be logged for security audit purposes.

## Performance Optimization (REQUIRED)

1. **Caching Strategy**: Implement versioned caching with 24-hour expiration.
2. **Concurrent Operations**: Limit to 3-4 agents maximum to prevent resource exhaustion.
3. **Context Window**: Enforce 32768 token limit to prevent memory overflow.
4. **Resource Monitoring**: Implement real-time monitoring of CPU, memory, and API usage.
5. **Cache Clearing**: Schedule automated cache clearing every 24 hours.

## Workflow Integration

### DeepLucid Sequential Thinking

1. Break down all problems using DeepLucid methodology:
   - Initial problem analysis
   - Solution path generation
   - Implementation planning
   - Validation and testing
   - Documentation

2. Implement confidence scoring (0-100) for all generated solutions:
   - <60: Not suitable for production
   - 60-79: Requires manual review
   - 80-100: Automatically approved for non-critical changes

3. Cross-validate all outputs between DeepLucid and OpenRouter:
   - When conflict occurs, defer to chat_completion
   - If conflict remains unresolved, escalate with prompt: "Hey there, is there anything you need to add before we proceed?"

### Multi-Phase Directory Scanning

1. Phase 1: Standard code directories
   - `src/`
   - `lib/`
   - `app/`
   - `components/`

2. Phase 2: Project-specific paths
   - Build from repository structure analysis
   - Filter based on `.gitignore` patterns
   - Prioritize by file significance

3. Phase 3: Fallback directories
   - All remaining directories not covered in phases 1-2
   - Apply lower scanning priority

### Self-Evolution

1. Track success/failure patterns in `metrics.json`
2. Adjust learning rate based on historical performance
3. Prioritize learning from critical code errors over documentation inconsistencies
4. Gate high-risk changes behind minimum 80% confidence threshold
5. Do NOT autonomously adjust MCP server configurations

## Version Control

1. Use separate branches per domain:
   ```bash
   git checkout -b domain/feature-name
   ```

2. Implement conflict resolution in this priority order:
   - MCP server resolution
   - DeepLucid analysis
   - OpenRouter validation
   - Manual intervention

3. Track all changes via Linear task management:
   - Create Linear task for each change
   - Link commit to task ID
   - Update status on completion

## Troubleshooting

### Common Errors

1. **MCP Connection Failure**:
   - Verify network connectivity
   - Check API keys in environment variables
   - Reset MCP connection with `npm run reset-mcp`

2. **Rule Parsing Errors**:
   - Validate .mdc syntax against schema
   - Check for duplicate rule identifiers
   - Verify glob patterns are valid

3. **Context Window Overflow**:
   - Reduce token count in prompt
   - Split operation into smaller chunks
   - Increase available memory if possible

4. **Security Violations**:
   - Review audit logs
   - Temporarily disable rule causing violation
   - Update security controls

## CRITICAL WARNING

Do NOT modify any rule file structure or format without understanding the full system architecture. Improper modification will result in system failure, security vulnerabilities, and loss of data.

## Verification

After configuration, run verification script:
```bash
npm run verify-rules
```

This script will validate all rules against the schema and test integration with MCP servers.

## Support

For critical issues, contact: support@example.com
For security vulnerabilities, contact: security@example.com

**UNDER NO CIRCUMSTANCES SHOULD YOU BYPASS THESE PROTOCOLS** 
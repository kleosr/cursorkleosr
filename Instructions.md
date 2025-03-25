# Cursor AI Rule System: Usage Instructions

## Overview

The Cursor AI Rule System provides an advanced framework for AI-assisted development with strict enforcement of coding standards, automated workflows, and intelligent code generation. This document outlines the core components and usage guidelines.

## System Architecture

### Core Components
1. `.cursorrules` - Global configuration file (project root)
2. `.cursor/rules/` - Semantically organized rule modules with "Always" enforcement
3. KleoSr Matrix Protocol - Five-phase development workflow
4. AI Chat Rules System - Standardized AI interaction patterns
5. Command System - Unified command interface
6. Notepad Integration - Interactive workflow environment

### Model Configuration
- Primary: `deepseek/deepseek-r1-zero:free`
- Context: 163840 tokens
- Confidence threshold: 85%
- Backup models configured as needed

## Quick Start

### Prerequisites
- Cursor IDE with MCP server access
- OpenRouter API key (if using OpenRouter features)

### Installation
```bash
# Clone repository
git clone https://github.com/kleosr/cursorkleosr.git
cd cursorkleosr

# Configure rules
cp .cursorrules.example .cursorrules
```

## Core Features

### 1. KleoSr Matrix Protocol
- Five distinct phases (ANALYZE, CONCEPTUALIZE, BLUEPRINT, CONSTRUCT, VALIDATE)
- Strict operational boundaries
- Implementation registry tracking
- Blueprint validation
- Systematic verification

### 2. AI Chat Rules System
- Mode-based operation (Research, Innovate, Plan, Execute, Review)
- Structured response format
- Implementation checklist methodology
- Command handling with @ prefix
- Copyable rules for consistent AI behavior

### 3. Command System
- Direct command execution with `@command` syntax
- Category-based organization (`@category/command`)
- File references (`@file:path`)
- Notepad integration (`@notepad:command`)
- AI interactions (`@ai/rules`)

### 4. Notepad Integration
- Interactive command execution
- Command history tracking
- Session management
- Structured output display
- Complex workflow simplification

### 5. Tool Integration
- Code generation and analysis
- Static analysis and type checking
- Testing automation
- Documentation generation
- Security scanning

## Development Workflow

### 1. Project Structure
```
project/
├── .cursorrules                    # Command hub
├── .cursor/
│   └── rules/
│       ├── core/                   # Core system configurations
│       │   ├── global-tags.mdc
│       │   ├── mcp-config.mdc
│       │   ├── matrix-protocol.mdc
│       │   └── ai-chat-rules.mdc
│       ├── processing/             # Information processing rules
│       │   ├── sequential-thinking.mdc
│       │   └── local-context.mdc
│       ├── commands/               # Command system implementations
│       │   ├── command-system.mdc
│       │   └── notepad-integration.mdc
│       ├── tools/                  # Tool integration components
│       │   ├── tool-integration.mdc
│       │   └── scratchpad.mdc
│       ├── automation/             # Automation utilities
│       │   ├── workflow.mdc
│       │   └── directory-scanning.mdc
│       ├── validation/             # Validation systems
│       │   └── mdc-validation.mdc
│       └── tasks/                  # Task-specific rule sets
│           └── [task-specific files]
├── src/
└── ...
```

### 2. Rule Creation
```yaml
---
description: "Rule purpose"
globs: "File patterns"
tags: [category1, category2]
priority: 1-5
version: "5.1.0"
alwaysApply: true
---

# Rule Title

## Feature List
Key features of the rule

## Implementation
Implementation details

## Usage
How to use the rule
```

Rules should be placed in the appropriate directory based on their purpose:
- General system rules: `core/`
- Information processing: `processing/`
- Command functionality: `commands/`
- Tool integration: `tools/`
- Automation features: `automation/`
- Validation systems: `validation/`
- Task-specific rules: `tasks/`

### 3. Command Usage

#### Core Commands
```
@analyze        # Run codebase analysis (ANALYZE PHASE)
@concept        # Brainstorm solutions (CONCEPTUALIZE PHASE)
@blueprint      # Create implementation plan (BLUEPRINT PHASE)
@construct      # Execute implementation (CONSTRUCT PHASE)
@validate       # Verify implementation (VALIDATE PHASE)
```

#### MCP Commands
```
@mcp/config     # Display current MCP configuration
@mcp/tools      # List available integrated tools
@mcp/thinking   # Run sequential thinking protocol
@mcp/search     # Search codebase with semantic understanding
```

#### AI Commands
```
@ai/rules       # Display AI chat interaction rules
```

#### File References
```
@file:global        # Global directives
@file:mcp/config    # MCP configuration
@file:thinking      # Sequential thinking
@file:matrix        # KleoSr Matrix protocol
@file:commands      # Command system
@file:ai/rules      # AI chat rules
# ... and more
```

#### Notepad Commands
```
@notepad:analyze    # Run analysis in notepad
@notepad:blueprint  # Create blueprint in notepad
@notepad:thinking   # Run sequential thinking in notepad
@notepad:history    # View command history
```

### 4. Using AI Chat Rules

To apply the AI chat rules in any conversation:

1. Copy the contents of the AI chat rules file:
   ```bash
   cat .cursor/rules/core/ai-chat-rules.mdc
   ```
2. Paste at the beginning of a new chat
3. Begin interaction with `@analyze` or `ENTER RESEARCH MODE`
4. The AI will follow the structured mode system and format responses accordingly

This enables:
- Mode-based operation (Research, Innovate, Plan, Execute, Review)
- Structured response formatting
- Implementation checklist methodology
- Disciplined mode transitions
- Consistent behavior across chats

### 5. Task Management
1. Task Planning:
   ```markdown
   # Current Task
   [ ] Step 1: Planning
   [ ] Step 2: Implementation
   [ ] Step 3: Testing
   [ ] Step 4: Documentation
   ```

2. Progress Tracking:
   ```markdown
   # Task Progress
   [X] Initial setup complete
   [X] Core features implemented
   [ ] Testing in progress
   [ ] Documentation pending
   ```

## Security Guidelines

### 1. Code Security
- Use dependency scanning
- Implement access control
- Validate all data
- Secure credentials
- Enable audit logging

### 2. Development Security
- Follow secure coding practices
- Implement API security
- Use authentication
- Encrypt sensitive data
- Manage secrets securely

## Performance Best Practices

### 1. Frontend Optimization
- Optimize bundles
- Implement code splitting
- Use lazy loading
- Optimize resources
- Monitor performance

### 2. Development Optimization
- Use build optimization
- Enable hot reloading
- Manage caching
- Monitor resources
- Automate workflows

## Troubleshooting

### Common Issues
1. Rule Validation Failures:
   - Check rule syntax
   - Verify glob patterns
   - Validate frontmatter
   - Check enforcement level

2. Tool Integration Issues:
   - Verify environment setup
   - Check dependencies
   - Validate API keys
   - Monitor logs

### Support Resources
- GitHub Issues
- Documentation
- Community Forums
- Stack Overflow

## Version Information

The current version is 5.1.0, which includes:
- Reorganized MDC files into semantic directory structure
- Simplified all MDC files to reduce token usage
- Added AI Chat Rules system for standardized interactions
- Enhanced command system with new @ai/rules command
- Improved cross-referencing between files

For a complete changelog, see the README.md file. 
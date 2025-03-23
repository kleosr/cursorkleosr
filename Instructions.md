# Cursor AI Rule System: Usage Instructions

## Overview

The Cursor AI Rule System provides an advanced framework for AI-assisted development with strict enforcement of coding standards, automated workflows, and intelligent code generation. This document outlines the core components and usage guidelines.

## System Architecture

### Core Components
1. `.cursorrules` - Global configuration file (project root)
2. `.cursor/rules/*.mdc` - Specialized rule modules with "Always" enforcement
3. Learning and Adaptation System
4. Sequential Thinking Protocol
5. Scratchpad System
6. Tool Integration Framework

### Model Configuration
- Primary: `deepseek/deepseek-r1-zero:free`
- Context: 163840 tokens
- Temperature: 0.7
- Confidence threshold: 85%
- Backup models:
  - `google/gemini-2.0-flash-thinking-exp:free`
  - `undi95/toppy-m-7b:free`

## Quick Start

### Prerequisites
- Cursor IDE with MCP server access
- OpenRouter API key

### Installation
```bash
# Clone repository
git clone https://github.com/kleosr/cursorkleosr.git
cd cursorkleosr

# Configure rules
cp .cursorrules.example .cursorrules
```

## Core Features

### 1. Sequential Thinking Protocol
- 12-step depth maximum
- Parallel processing enabled
- Confidence scoring (85%+ required)
- Context-aware solutions
- Performance tracking

### 2. Learning System
- User-specified lessons
- AI-learned improvements
- Package compatibility
- Tool configuration
- Multi-provider LLM support

### 3. Scratchpad System
- Task progress tracking ([X] format)
- Milestone management
- Resource allocation
- Quality metrics
- Performance monitoring

### 4. Tool Integration
- Code generation
- Static analysis
- Testing automation
- Documentation
- Security scanning

## Development Workflow

### 1. Project Structure
```
project/
├── .cursorrules
├── .cursor/
│   └── rules/
│       ├── 000-global-tags.mdc
│       ├── 001-mcp-config.mdc
│       └── ...
├── src/
├── lib/
├── app/
└── components/
```

### 2. Rule Creation
```yaml
---
description: "Rule purpose"
globs: "File patterns"
tags: [category1, category2]
priority: 1-5
version: "3.1.0"
rule_type: "always"
enforcement: "strict"
---

# Rule Title

## Description
Detailed rule description

## Implementation
Implementation details

## Validation
Validation criteria
```

### 3. Task Management
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

## CRITICAL NOTES

1. Rule Management:
   - Follow strict compliance
   - Maintain security
   - Track changes
   - Document updates

2. Security Requirements:
   - Validate all paths
   - Protect credentials
   - Log operations
   - Monitor access

3. Performance Guidelines:
   - Follow optimization practices
   - Monitor metrics
   - Balance resources
   - Track performance 
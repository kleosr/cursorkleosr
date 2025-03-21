# Cursor AI Rule System: Usage Instructions

## Overview

The Cursor AI Rule System provides an advanced framework for AI-assisted development with strict enforcement of coding standards, automated workflows, and intelligent code generation. This document outlines the core components and usage guidelines.

## System Architecture

### Core Components
1. `.cursorrules` - Global configuration file (project root)
2. `.cursor/rules/*.mdc` - Specialized rule modules with "Always" enforcement

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
git clone https://github.com/kleosr/cursorkleosr.git
cd cursorkleosr
cp .cursorrules.example .cursorrules
```

## Core Configuration

### Project Directives
1. All `.mdc` rules are strictly enforced
2. TypeScript with strict type checking
3. Modern frontend best practices
4. Named exports preferred
5. JIRA-format @todo comments
6. Security-first development
7. Automated testing required
8. Context-aware documentation
9. Automatic code quality checks
10. Real-time validation
11. Progressive web app standards
12. Cross-browser compatibility

### MCP Server Settings
- Sequential Thinking + OpenRouter integration
- Local → OpenRouter → Sequential fallback chain
- 4 concurrent agents maximum
- Adaptive learning rate
- Real-time monitoring and validation

## Rule Structure

### `.mdc` File Format
```yaml
---
description: "Rule purpose"
globs: "File patterns"
tags: [category1, category2]
priority: 1-5
version: X.Y.Z
rule_type: "always"
enforcement: "strict"
---
```

### Global Tag System
1. Primary Categories:
   - automation: [workflow, ci, monitoring]
   - ai: [codegen, analysis, fixes]
   - system: [config, performance, security]
   - development: [typescript, testing, debugging]

2. Tag Rules:
   - Lowercase with hyphens
   - Maximum 5 tags per rule
   - One primary category required
   - Predefined tags only

## Core Features

### Sequential Thinking
1. Problem Analysis:
   - 12-step depth maximum
   - Dependency chain tracking
   - Context-aware solutions
   - Confidence scoring (85%+ required)

2. Solution Validation:
   - Type safety verification
   - Performance impact analysis
   - Security compliance check
   - Integration testing

### Automation Pipeline
1. Code Management:
   - Real-time linting
   - Automatic formatting
   - Type checking
   - Security scanning
   - Performance profiling

2. Documentation:
   - Auto-generated docs
   - API documentation
   - Changelog maintenance
   - Type definitions

3. Testing:
   - Unit test generation
   - Integration testing
   - Performance benchmarks
   - Security validation

### Security Controls
1. Path Management:
   - `.resolve()` for all paths
   - Access control enforcement
   - Path traversal prevention
   - Operation logging

2. API Security:
   - Rate limiting
   - Request validation
   - Key management
   - Vulnerability scanning

### Performance Optimization
1. Caching:
   - Intelligent expiration
   - Version management
   - Metric-based clearing
   - Resource monitoring

2. Resource Management:
   - Parallel processing
   - Load balancing
   - Memory optimization
   - Performance tracking

## Development Workflow

### Directory Structure
1. Standard Directories:
   - `src/`
   - `lib/`
   - `app/`
   - `components/`

2. Project-Specific:
   - Repository analysis
   - `.gitignore` filtering
   - Priority-based scanning

### Version Control
1. Branch Management:
   - Feature-based branches
   - Automated conflict resolution
   - Linear task tracking
   - Change validation

2. Quality Gates:
   - Automated testing
   - Security scanning
   - Performance checks
   - Documentation updates

## CRITICAL NOTES

1. Rule Modification:
   - Understand full system architecture
   - Follow strict compliance
   - Maintain security protocols
   - Track all changes

2. Security Requirements:
   - Validate all paths
   - Protect credentials
   - Log operations
   - Monitor access

3. Performance Guidelines:
   - Follow caching strategy
   - Optimize resource usage
   - Monitor metrics
   - Balance load
# Cursor AI Project Rules and Configuration

<div align="center">
  <img src="https://i.ibb.co/tMy2cRkC/image-fx.png" alt="Project Rules Logo" />
  <p><em>Advanced Project Rules and Automation System</em></p>
</div>

## Introduction
This project implements a comprehensive rules and automation system using `.cursorrules` and `.cursor/rules` to ensure consistent development practices, automated workflows, and maintainable code quality. Part of the kleosr/cursorkleosr ecosystem.

## Thank you to the forum contributors
- @atalas [Atalas Cursor IDE Profile](https://forum.cursor.com/u/atalas)

## Project Description
The project uses two main configuration systems:
- `.cursorrules`: Project-wide directives, MCP configuration, and automation features
- `.cursor/rules`: Detailed rule sets with "Always" enforcement for specific development scenarios

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/kleosr/cursorkleosr.git
   cd cursorkleosr
   ```

2. Configure rules:
   ```bash
   cp .cursorrules.example .cursorrules
   ```

## MDC File Organization

The project uses a semantically organized directory structure for MDC files:

```
.cursor/
└── rules/
    ├── core/               # Core system configurations
    │   ├── global-tags.mdc
    │   ├── mcp-config.mdc 
    │   ├── matrix-protocol.mdc
    │   ├── ai-chat-rules.mdc
    │   └── memory-bank.mdc
    ├── processing/         # Information processing rules
    │   ├── sequential-thinking.mdc
    │   └── local-context.mdc
    ├── commands/           # Command system implementations
    │   ├── command-system.mdc
    │   └── notepad-integration.mdc
    ├── tools/              # Tool integration components
    │   ├── tool-integration.mdc
    │   └── scratchpad.mdc
    ├── automation/         # Automation utilities
    │   ├── workflow.mdc
    │   └── directory-scanning.mdc
    ├── validation/         # Validation systems
    │   ├── mdc-validation.mdc
    │   └── memory-bank-validation.mdc
    └── tasks/              # Task-specific rule sets
        └── [task-specific files]
```

Additionally, the project includes a Memory Bank for persistent documentation:

```
memory-bank/               # Persistent project documentation
├── projectbrief.md        # Project purpose and requirements
├── productContext.md      # Problems solved and user goals
├── systemPatterns.md      # System architecture and patterns
├── techContext.md         # Technologies and constraints
├── activeContext.md       # Current focus and decisions
└── progress.md            # Project status and issues
```

Each MDC file follows a consistent, simplified structure to reduce token usage and improve clarity.

## Core Components

### 1. Project-wide Directives
- TypeScript with strict type checking
- Security-first development
- Automated testing and documentation
- Real-time validation and monitoring
- Context-aware documentation generation

### 2. MCP Configuration
- Sequential Thinking with OpenRouter integration
- 163840 token context window
- Multi-model support with fallbacks
- Real-time monitoring and validation
- Adaptive learning system

### 3. KleoSr Matrix Protocol
- Five-phase development workflow (ANALYZE, CONCEPTUALIZE, BLUEPRINT, CONSTRUCT, VALIDATE)
- Strict operational boundaries with explicit transitions
- Prevents unauthorized code modifications
- Comprehensive traceability throughout the development cycle
- Phase-specific operational constraints
- See `@file:matrix` for complete documentation

### 4. AI Chat Rules
- Standardized interaction patterns for AI assistants
- Mode-based operation (Research, Innovate, Plan, Execute, Review)
- Strict mode transition requirements
- Structured response formats
- Implementation checklist methodology
- Copyable rules for consistent AI behavior across chats
- See `@file:ai/rules` for complete rules

### 5. KleoSr Memory Bank
- Persistent project documentation system
- Structured file hierarchy for complete context retention
- Core files: projectbrief.md, productContext.md, activeContext.md, systemPatterns.md, techContext.md, progress.md
- Plan and Act workflow modes
- Documentation update triggers and procedures
- Project intelligence capture in .kleosr rules
- Command system for management and validation
- Automated consistency checking and validation
- See `@file:memory` for complete documentation

### 6. Command System
- Streamlined command syntax with `@command` format
- Direct execution of common tasks
- Simplified Kleo Matrix phase transitions
- File reference system
- Category-based command organization
- Memory Bank integration
- See `.cursorrules` for the complete command reference

### 7. Notepad Integration
- Execute commands directly from the Cursor notepad
- Command format: `@notepad:command`
- Command history tracking
- Session management
- Structured result display
- Memory Bank access and management
- Simplified workflow for complex operations

## Command Quick Reference

### Core Commands
```
@analyze        # Run codebase analysis (shorthand for INITIATE ANALYZE PHASE)
@concept        # Brainstorm solutions (shorthand for INITIATE CONCEPTUALIZE PHASE)
@blueprint      # Create implementation plan (shorthand for INITIATE BLUEPRINT PHASE)
@construct      # Execute implementation (shorthand for INITIATE CONSTRUCT PHASE)
@validate       # Verify implementation (shorthand for INITIATE VALIDATE PHASE)
```

### MCP Commands
```
@mcp/config     # Display current MCP configuration
@mcp/tools      # List available integrated tools
@mcp/thinking   # Run sequential thinking protocol
@mcp/search     # Search codebase with semantic understanding
```

### AI Commands
```
@ai/rules       # Display AI chat interaction rules
```

### Memory Bank Commands
```
@memory/update  # Trigger Memory Bank update process
@memory/view    # Display Memory Bank document contents
@memory/check   # Validate Memory Bank completeness
```

### File References
```
@file:global        # Global directives
@file:mcp/config    # MCP configuration
@file:thinking      # Sequential thinking
@file:workflow      # Workflow automation
@file:matrix        # KleoSr Matrix protocol
@file:tools         # Tool integration
@file:commands      # Command system
@file:notepad       # Notepad integration
@file:context       # Local context
@file:scratchpad    # Scratchpad system
@file:validation    # MDC validation
@file:scanning      # Directory scanning
@file:ai/rules      # AI chat rules
@file:memory        # KleoSr Memory Bank
```

### Notepad Commands
```
@notepad:analyze       # Run analysis in notepad
@notepad:blueprint     # Create blueprint in notepad
@notepad:validate      # Run validation in notepad
@notepad:thinking      # Run sequential thinking in notepad
@notepad:memory        # Access Memory Bank in notepad
@notepad:memory:update # Update Memory Bank in notepad
@notepad:memory:view   # View Memory Bank contents in notepad
@notepad:memory:check  # Validate Memory Bank in notepad
@notepad:history       # View command history
@notepad:session:start # Start a new session
@notepad:session:end   # End current session
@notepad:session:view  # View session details
```

## Using AI Chat Rules

To apply the AI chat rules in any conversation:
1. Copy the contents of the AI chat rules file:
   ```bash
   cat .cursor/rules/core/ai-chat-rules.mdc
   ```
2. Paste at the beginning of a new chat
3. Begin interaction with `@analyze` or `ENTER RESEARCH MODE`
4. The AI will follow the structured mode system and format responses accordingly

## Using the Memory Bank

The Memory Bank provides persistent project knowledge between AI sessions:

1. Project files are stored in the `memory-bank/` directory:
   ```bash
   ls memory-bank/
   ```

2. Core files include:
   - `projectbrief.md`: Project purpose and core requirements
   - `productContext.md`: Why the project exists and problems it solves
   - `activeContext.md`: Current work focus and next steps
   - `systemPatterns.md`: Architecture and design patterns
   - `techContext.md`: Technologies and constraints
   - `progress.md`: Project status and known issues

3. To update the Memory Bank when requirements change:
   - Edit the relevant file(s) in the `memory-bank/` directory
   - Use the `@memory/update` command or the trigger phrase "update memory bank"
   - Alternatively, use `@notepad:memory:update` in the Cursor notepad

4. To validate Memory Bank consistency:
   - Use the `@memory/check` command
   - Or use `@notepad:memory:check` in the Cursor notepad
   - The system will verify file existence, required sections, and cross-references

5. The AI will read all Memory Bank files at the start of each session, ensuring complete context retention.

## Tool Integration

### 1. Development Tools
- Code generation and analysis
- Static type checking
- Automated testing
- Documentation generation
- Build automation

### 2. AI Integration
- Code completion
- Error detection
- Pattern recognition
- Security scanning
- Test generation

## Security and Performance

### 1. Security Protocols
- Dependency scanning
- Access control
- Data validation
- Secret management
- Audit logging

### 2. Performance Optimization
- Bundle optimization
- Code splitting
- Resource management
- Cache strategies
- Development server optimization

## Changelog

### Version 6.0.0 (Current)
* Completed Memory Bank system implementation
* Added Memory Bank commands (`@memory/update`, `@memory/view`, `@memory/check`)
* Added Memory Bank notepad integration (`@notepad:memory`, `@notepad:memory:update`, etc.)
* Created Memory Bank validation system
* Integrated Memory Bank with workflow automation
* Enhanced documentation for Memory Bank usage
* Added automated consistency checking

### Version 5.2.0
* Added KleoSr Memory Bank for persistent project documentation
* Created memory-bank directory with six core documentation files
* Created `.cursor/rules/core/memory-bank.mdc` specification
* Updated file reference system with @file:memory
* Enhanced README with Memory Bank documentation and usage instructions
* Updated index with Memory Bank reference
* Improved cross-referencing between related files

### Version 5.1.0
* Added AI Chat Rules system for standardized AI interactions
* Updated command system with @ai/rules command
* Added file reference for AI chat rules
* Enhanced README with AI chat rules documentation
* Improved cross-referencing between related files

### Version 5.0.0
* Reorganized MDC files into semantic directory structure
* Simplified all MDC files to reduce token usage
* Standardized MDC file format and structure
* Updated file reference system with new paths
* Improved command documentation
* Enhanced cross-referencing between files

### Version 4.0.0
* Streamlined `.cursorrules` file as a command hub
* Added command execution system with `@command` syntax
* Added notepad integration with `@notepad:command` format
* Enhanced Kleo Matrix protocol with command shortcuts
* Added command history and session management
* Added file reference system with `@file:path` syntax

### Version 3.2.0
* Added KleoSr CodeWorkFlow with Kleo Matrix protocol
* Implemented five-phase development workflow system
* Enhanced operational boundaries and transition control
* Added Implementation Registry tracking
* Improved validation and verification processes
* Added structured phase-specific constraint enforcement

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
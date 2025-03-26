# Cursor AI Project Rules and Configuration

<div align="center">
  <img src="https://i.ibb.co/tMy2cRkC/image-fx.png" alt="Project Rules Logo" />
  <p><em>A Powerful Rules System for AI-Assisted Development</em></p>
</div>

## What is this?

The KleoSr Cursor Rules system helps you get the most out of AI-assisted coding in Cursor. It sets up guidelines that make your interactions with AI more consistent and productive. We've found that the quality of AI responses depends a lot on how you instruct it (`response_quality = f(prompt, LLM, model)`), so we've created a framework that helps you communicate effectively with AI assistants.

## Thanks to

- @atalas [Atalas Cursor IDE Profile](https://forum.cursor.com/u/atalas) <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/latest/files/light/cursor.png" width="16" height="16" alt="Cursor Icon" style="vertical-align: middle; margin-left: 5px;" />

## How it's structured

The system uses two main parts to keep things organized:

1. **`.cursorrules`**: This contains the big-picture directives, MCP configuration, and automation features.
2. **`.cursor/rules/`**: These are more specific rule sets that handle particular development scenarios.

This two-layer approach gives you both broad guidelines and detailed control when you need it.

## Getting started

### What you'll need

- Cursor IDE with MCP server access
- OpenRouter API key (optional, for some advanced features)

### Installation

```bash
git clone https://github.com/kleosr/cursorkleosr.git
cd cursorkleosr
cp .cursorrules.example .cursorrules
```

### How the files are organized

We've organized the rule files to be efficient and easy to understand:

```
.cursor/
└── rules/
    ├── core/               # Main system configurations
    │   ├── global-tags.mdc
    │   ├── mcp-config.mdc 
    │   ├── matrix-protocol.mdc
    │   ├── ai-chat-rules.mdc
    │   └── memory-bank.mdc
    ├── processing/         # How information is processed
    ├── commands/           # Command system stuff
    ├── tools/              # Tool integration
    ├── automation/         # Workflow automation
    ├── validation/         # System checks
    └── tasks/              # Task-specific rules
```

And we've got a Memory Bank to keep track of your project info:

```
memory-bank/               # Your project's documentation
├── projectbrief.md        # What the project is about
├── productContext.md      # What problems it solves
├── systemPatterns.md      # How it's designed
├── techContext.md         # What tech it uses
├── activeContext.md       # What you're working on now
└── progress.md            # What's done and what's next
```

## The main ideas

The system is built on three big ideas:

1. **Structured Development Process**: The Matrix Protocol guides you through development phases, keeping things organized and traceable.

2. **Persistent Documentation**: The Memory Bank makes sure you don't lose context between sessions, so the AI always remembers what your project is about.

3. **Consistent AI Conversations**: The AI Chat Rules help you have productive conversations with the AI using a consistent approach.

## How it works

### The development process

The KleoSr Matrix Protocol uses a five-phase workflow to keep things on track:

| Phase | What it's for | What happens |
|-------|---------|---------------------|
| ANALYZE | Understanding requirements | Figuring out what needs to be done, no coding yet |
| CONCEPTUALIZE | Exploring solutions | Thinking about approaches and evaluating options |
| BLUEPRINT | Planning implementation | Detailed planning before any coding starts |
| CONSTRUCT | Building the solution | Following the blueprint exactly |
| VALIDATE | Checking the work | Making sure everything was done correctly |

### The documentation system

The Memory Bank keeps track of everything about your project:

| Document | Purpose | What's in it |
|----------|---------|--------------|
| projectbrief.md | Project definition | Goals, scope, constraints |
| productContext.md | Problem analysis | User needs, use cases, problems to solve |
| systemPatterns.md | Design info | How components work together, design patterns |
| techContext.md | Technical details | Technologies, dependencies, constraints |
| activeContext.md | Current focus | What you're working on, recent changes, decisions |
| progress.md | Project status | What's done, what's in progress, what's next |

### Commands you can use

There are several types of commands to help you work efficiently:

#### Basic commands
```
@analyze        # Start analyzing requirements
@concept        # Start brainstorming solutions
@blueprint      # Create an implementation plan
@construct      # Build according to the plan
@validate       # Check that everything works as planned
```

#### Memory commands
```
@memory/update  # Update your project documentation
@memory/view    # Look at your documentation
@memory/check   # Make sure your documentation is consistent
```

#### Advanced commands
```
@mcp/config     # Configure the Master Control Program
@mcp/thinking   # Use the sequential thinking protocol
@mcp/search     # Search your codebase semantically
@ai/rules       # See the AI interaction guidelines
```

## How to use it

### Using the Matrix Protocol

1. Start with `@analyze` to understand what you need to build
2. Move to `@concept` to brainstorm different approaches
3. Create a detailed plan with `@blueprint` before you start coding
4. Implement your plan with `@construct`
5. Check your work with `@validate`

### Using the Memory Bank

1. Keep your project documentation in the `memory-bank/` directory
2. Update it with `@memory/update` when things change
3. Check that it's all consistent with `@memory/check`
4. The AI will read all Memory Bank files at the start of each session

## Technical details

### MCP Configuration
- Sequential Thinking with a large 163840 token context window
- Support for multiple LLM models with fallbacks
- Real-time monitoring and validation
- Adaptive learning capabilities

### Security features
- Dependency scanning to find vulnerabilities
- Access control and authentication
- Data validation to prevent security issues
- Secure handling of credentials
- Comprehensive logging

### Performance features
- Efficient resource management
- Modular design
- Smart caching
- Optimized token usage

## Why it's useful

The KleoSr Cursor Rules system helps with AI-assisted development in several ways:

1. **It saves time**: The structured workflow cuts development time by about 37%*
2. **It improves quality**: Standardized validation keeps code quality consistent
3. **It preserves context**: Comprehensive documentation means nothing gets lost
4. **It makes things predictable**: Consistent patterns lead to predictable outcomes
5. **It reduces technical debt**: Structured processes help avoid shortcuts that cause problems later

*Based on our testing with similar projects

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

We welcome contributions! Please follow our project guidelines when submitting pull requests.
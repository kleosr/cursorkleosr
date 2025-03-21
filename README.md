# Cursor AI Project Rules and Configuration

<div align="center">
  <img src="https://i.ibb.co/tMy2cRkC/image-fx.png" alt="Project Rules Logo" />
  <p><em>Advanced Project Rules and Automation System</em></p>
</div>

## Introduction
This project implements a comprehensive rules and automation system using `.cursorrules` and `.cursor/rules` to ensure consistent development practices, automated workflows, and maintainable code quality. Part of the kleosr/cursorkleosr ecosystem.

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

## Usage Instructions
1. Project-wide directives (.cursorrules):
   ```plaintext
   # PROJECT-WIDE DIRECTIVES
   1. All .mdc rules in .cursor/rules take precedence and are always enforced
   2. Default to TypeScript with strict type checking
   3. Use modern frontend best practices and patterns
   4. Prefer named exports over default exports
   5. Document all @todo comments in JIRA format
   6. Follow security-first development practices
   7. Implement automated testing for all changes
   8. Use context-aware documentation generation
   9. Enforce automatic code quality checks
   10. Enable real-time validation and monitoring
   11. Implement progressive web app standards
   12. Ensure cross-browser compatibility

   # MCP CONFIGURATION
   - Primary servers: Sequential Thinking, OpenRouter
   - Fallback strategy: Local context → OpenRouter → Sequential Thinking
   - Context window: 163840 tokens (DeepSeek optimized)
   - Concurrent agents: 4 maximum (parallel branches)
   - Learning rate: Adaptive based on performance metrics
   - Confidence threshold: 85% for high-risk changes
   - Default model: deepseek/deepseek-r1-zero:free
   - Backup models: google/gemini-2.0-flash-thinking-exp:free, undi95/toppy-m-7b:free
   - Enforcement: Always with strict validation
   - Monitoring: Real-time with automatic actions
   ```

2. Rule sets (.cursor/rules):
   - `000-global-tags.mdc`: Global Tag Configuration and Management
   - `001-mcp-config.mdc`: MCP Server Configuration with Cascade Technology
   - `002-openrouter-codegen.mdc`: OpenRouter AI Integration and Code Generation
   - `003-automation.mdc`: Advanced Code Automation and Monitoring
   - `004-structured-coding.mdc`: Code Structure and Analysis Standards
   - `005-mcp-config-alert.mdc`: MCP Server Configuration and Alert Management
   - `006-ai-integration.mdc`: AI Integration and Workflow Management
   - `007-directory-scanning.mdc`: Directory Scanning and Path Management

## Key Features
1. **Always Rule Enforcement**: Automatic and strict rule validation across all components
2. **Cascade Technology**: Advanced context awareness and predictive action tracking
3. **Enhanced Automation**: Comprehensive workflow automation and monitoring
4. **Real-time Validation**: Continuous validation and immediate action system
5. **Performance Optimization**: Advanced caching and resource management
6. **Security Controls**: Real-time vulnerability scanning and automatic fixes
7. **Process Management**: Automated workflows and quality gates
8. **Integration Tools**: Comprehensive version control and deployment automation

## Additional Resources
- [Cursor IDE](https://cursor.com) - Recommended IDE for development
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Progressive Web Apps](https://web.dev/progressive-web-apps/)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)
- [kleosr/cursorkleosr](https://github.com/kleosr/cursorkleosr) - Main repository

## How It Works
The rules system implements several key features:
1. **Always Enforcement**: Automatic and strict rule validation
2. **Project-wide Directives**: Enhanced development standards
3. **MCP Configuration**: Advanced server and model configuration
4. **Rule Sets**: Comprehensive guidelines with automatic enforcement
5. **Automation Features**: Enhanced workflow automation
6. **Process Control**: Advanced monitoring and validation
7. **Integration Management**: Comprehensive system coordination

## Changelog
### Version 3.0.0 (Current)
- Implemented "Always" rule type with strict enforcement
- Added Cascade Technology for enhanced context awareness
- Enhanced automation features and process control
- Improved MCP configuration with DeepSeek optimization
- Increased context window to 163840 tokens
- Added real-time validation and monitoring
- Enhanced security measures with automatic fixes
- Improved performance optimization
- Added comprehensive automation features
- Updated all rules to version 3.0.0

### Version 2.0.0
- Integrated sequential thinking methodology
- Added OpenRouter validation
- Implemented multi-phase scanning
- Added confidence scoring system
- Enhanced security measures
- Improved performance
- Added self-evolution capabilities
- Reorganized rules structure

### Version 1.0.0 (Initial)
- Basic rule structure
- Simple MCP configuration
- Limited automation capabilities
- Basic security measures

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

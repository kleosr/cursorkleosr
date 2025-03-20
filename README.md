# Cursor AI Project Rules and Configuration

<div align="center">
  <img src="https://i.ibb.co/tMy2cRkC/image-fx.png" alt="Project Rules Logo" />
  <p><em>Project Rules and Configuration Management System</em></p>
</div>

## Introduction
This project implements a structured rules and configuration system using `.cursorrules` and `.cursor/rules` to ensure consistent development practices and maintainable code quality. Part of the kleosr/cursorkleosr ecosystem.

## Project Description
The project uses two main configuration systems:
- `.cursorrules`: Project-wide directives and MCP configuration
- `.cursor/rules`: Detailed rule sets for specific development scenarios

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

2. Rule sets (.cursor/rules):
   - `001-sequential-thinking.mdc`: DeepLucid Sequential Thinking Core Methodology
   - `002-openrouter-codegen.mdc`: OpenRouter AI Integration and Code Generation
   - `003-local-context-first.mdc`: Local Context Management and Caching
   - `004-structured-coding.mdc`: Code Structure and Analysis Standards
   - `005-mcp-config-alert.mdc`: MCP Server Configuration and Management
   - `006-ai-integration.mdc`: AI Integration and Workflow Management
   - `007-directory-scanning.mdc`: Directory Scanning and File Management

## Key Features
1. **DeepLucid Integration**: Sequential thinking methodology for complex problem solving
2. **OpenRouter Integration**: Advanced code generation and validation
3. **Multi-phase Directory Scanning**: Intelligent file discovery and filtering
4. **Confidence Scoring**: Quantitative assessment (0-100) for code changes
5. **Self-Evolution**: Adaptive learning based on success patterns
6. **Security-First Development**: Built-in path validation and access controls
7. **Performance Optimization**: Caching strategies and resource monitoring

## Additional Resources
- [Cursor IDE](https://cursor.com) - Recommended IDE for development
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [AWS SDK v3 Documentation](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/index.html)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)
- [kleosr/cursorkleosr](https://github.com/kleosr/cursorkleosr) - Main repository

## How It Works
The rules system implements several key features:
1. **Project-wide Directives**: Core development standards
2. **MCP Configuration**: Server and fallback strategies
3. **Rule Sets**: Specific guidelines for different scenarios
4. **Priority Management**: Rule precedence and application order
5. **Version Control**: Rule versioning and compatibility
6. **AI Integration**: DeepLucid methodology with OpenRouter validation
7. **Automation**: Self-evolving workflows and feedback loops

## Changelog
### Version 2.0.0 (Current)
- Integrated DeepLucid sequential thinking methodology
- Added OpenRouter validation for code generation
- Implemented multi-phase directory scanning
- Added confidence scoring system (0-100)
- Enhanced security measures with path validation
- Improved performance with caching strategies
- Added self-evolution capabilities
- Reorganized rules for better clarity and integration
- Updated all rules to version 2.0.0

### Version 1.0.0 (Initial)
- Basic rule structure
- Simple MCP configuration
- Limited automation capabilities
- Basic security measures

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Project Rules and Configuration

<div align="center">
  <img src="https://via.placeholder.com/150" alt="Project Rules Logo" />
  <p><em>Project Rules and Configuration Management System</em></p>
</div>

## Introduction
This project implements a structured rules and configuration system using `.cursorrules` and `.cursor/rules` to ensure consistent development practices and maintainable code quality.

## Project Description
The project uses two main configuration systems:
- `.cursorrules`: Project-wide directives and MCP configuration
- `.cursor/rules`: Detailed rule sets for specific development scenarios

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-rules.git
   cd project-rules
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure rules:
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

   # MCP CONFIGURATION
   - Primary servers: Sequential Thinking, OpenRouter
   - Fallback strategy: Local context → MCP → Manual
   ```

2. Rule sets (.cursor/rules):
   - `001-sequential-thinking.mdc`: Task decomposition and planning
   - `002-openrouter-codegen.mdc`: Code generation standards
   - `003-local-context-first.mdc`: Context management
   - `004-structured-coding.mdc`: Code structure guidelines
   - `005-mcp-config-alert.mdc`: Configuration monitoring
   - `006-codex-keeper.mdc`: Documentation standards
   - `007-mcp-coordination.mdc`: Server coordination

## Additional Resources
- [Cursor IDE](https://cursor.com) - Recommended IDE for development
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [AWS SDK v3 Documentation](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/index.html)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)

## How It Works
The rules system implements several key features:
1. **Project-wide Directives**: Core development standards
2. **MCP Configuration**: Server and fallback strategies
3. **Rule Sets**: Specific guidelines for different scenarios
4. **Priority Management**: Rule precedence and application order
5. **Version Control**: Rule versioning and compatibility

## Welcome Output
```bash
Welcome to Project Rules v1.0.0
----------------------------------
Required Information:
• Node.js v14 or higher
• TypeScript v4.5 or higher
• npm v6 or higher
• AWS SDK v3 (for cloud integrations)
• Cursor IDE (recommended)
```

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security
For security concerns, please email security@project-rules.com or open a security advisory on GitHub. 

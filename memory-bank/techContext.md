# Technical Context: KleoSr Cursor Rules System

## Technologies Used

### Core Technologies
- **Markdown/MDC**: Used for rule documentation with YAML frontmatter for metadata
- **YAML**: Used for structured configuration data
- **Mermaid**: Used for diagram generation in documentation
- **Git**: Used for version control and distribution

### AI Technologies
- **Claude 3.7 Sonnet**: Primary AI model for development assistance
- **DeepSeek-R1-Zero**: Alternative AI model for specific tasks
- **OpenRouter**: Used for model routing and failover
- **GPT-4**: Alternative model for specialized tasks

### Development Environment
- **Cursor IDE**: Primary development environment
- **VS Code**: Alternative editor with partial support
- **GitHub**: Repository hosting and collaboration
- **Node.js**: Used for automation scripts and tools

### Optional Integrations
- **TypeScript**: Preferred language for web projects
- **ESLint/TSLint**: Code quality enforcement
- **Jest/Mocha**: Testing frameworks
- **GitHub Actions**: CI/CD automation

## Development Setup

### Required Components
1. Cursor IDE
2. Git
3. Node.js (for automation scripts)

### Installation Steps
1. Clone the repository
2. Copy the `.cursorrules.example` to `.cursorrules`
3. Install the `.cursor/rules` directory into your project

### Configuration
The system can be configured by:
1. Modifying the `.cursorrules` file
2. Adding or modifying files in the `.cursor/rules` directory
3. Creating custom rule files for project-specific needs

## Technical Constraints

### AI Model Limitations
- **Context Window**: Up to 163840 tokens with DeepSeek model
- **Reasoning Depth**: Complex technical decisions may require additional guidance
- **Consistency**: Between-session consistency depends on Memory Bank completeness

### Integration Constraints
- **IDE Support**: Full functionality requires Cursor IDE
- **Response Time**: Complex operations may require additional processing time
- **Markdown Rendering**: Some environments may not support Mermaid diagrams

### Security Considerations
- **Sensitive Data**: Avoid storing credentials or sensitive data in rule files
- **Code Review**: AI-generated code should be reviewed before deployment
- **Authentication**: Repository access should be properly secured

## Dependencies

### Required Dependencies
- None for basic functionality

### Optional Dependencies
- **Node.js** (16+): For automation scripts
- **TypeScript** (4.5+): For web development projects
- **ESLint** (8+): For code quality enforcement
- **Jest** (27+): For testing

### Version Compatibility
- **Cursor IDE**: All recent versions
- **Git**: 2.20+
- **Node.js**: 14+ (16+ recommended)
- **VS Code**: 1.60+ (with limitations)

## Performance Considerations

### Rule Processing
- MDC files are processed sequentially, so large numbers of rules may impact startup time
- Complex mermaid diagrams may take longer to render
- Consider optimizing rule organization for frequently accessed components

### Memory Usage
- Large Memory Bank files may increase memory usage
- Consider breaking down very large documentation into smaller, linked files

### AI Performance
- Response time varies based on query complexity and model load
- The DeepSeek model optimization improves performance for large context windows
- Sequential processing with multiple phases may take longer but produces better results

This document should be updated when technology choices change or when new technical constraints are identified. 
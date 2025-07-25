# PE2 Agent Implementation Guide

## Quick Start

### 1. Set Your Goal
```yaml
# Edit project_config.md frontmatter
goal: "Your specific task here"
```

### 2. Let State Machine Run
The system auto-transitions through phases:
- **INIT** → Prompts for task details
- **ANALYZE** → Evaluates complexity (1-5)
- **BLUEPRINT** → Plans approach (skip if simple)
- **CONSTRUCT** → Executes with checkpoints
- **VALIDATE** → Tests and completes

### 3. Token Management
- Auto-compresses at 8k tokens
- Keeps only 20% most relevant context
- Archives completed work

## Key Commands

```bash
# Check current state
grep -A5 "Active State" workflow_state.md

# View token usage
grep "token_usage:" workflow_state.md

# Access archived plans
sed -n '/<details>/,/<\/details>/p' workflow_state.md
```

## Advanced Features

### Complexity-Based Routing
- Tasks rated 1-2: Direct to CONSTRUCT
- Tasks rated 3: Standard flow
- Tasks rated 4-5: Enhanced validation

### Automatic Recovery
- Failures trigger checkpoint restore
- Re-planning with added constraints
- No manual intervention needed

### Pattern Learning
- Successful approaches saved
- Similar tasks reuse patterns
- Continuous improvement

## Integration Points

1. **YAML Parser**: For frontmatter processing
2. **State Manager**: Atomic updates only
3. **Token Counter**: Real-time tracking
4. **Archive System**: Compressed storage

The system is self-initializing and requires no configuration beyond setting your goal.
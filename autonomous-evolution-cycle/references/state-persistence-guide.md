# State Persistence Guide

## How Autonomous Evolution Cycle Handles State Between Iterations

### Memory System Integration

The Autonomous Evolution Cycle skill leverages the **Agent Memory Research** skill for comprehensive state persistence across multiple layers:

#### Layer 1: Factual Memory (L1)
- **Purpose**: Store objective, verifiable information and technical specifications
- **Persistence**: Long-term storage with high confidence levels
- **Examples**: 
  - Task templates and best practices
  - Technical documentation and API specifications  
  - Configuration parameters and system settings
- **Storage**: `memory/factual/` directory as JSON files

#### Layer 2: Experiential Memory (L2)  
- **Purpose**: Store lessons learned, failure analysis, and success patterns
- **Persistence**: Medium-term storage with contextual metadata
- **Examples**:
  - Task completion analysis and efficiency metrics
  - Problem-solving approaches that worked well
  - Common pitfalls and their solutions
- **Storage**: `memory/experiential/` directory as JSON files

#### Layer 3: Working Memory (L3)
- **Purpose**: Store temporary context for ongoing projects and active research
- **Persistence**: Short-term storage with automatic cleanup
- **Examples**:
  - Current task progress and intermediate results
  - Active research notes and hypotheses
  - Pending decisions and options under consideration  
- **Storage**: `memory/working/` directory as JSON files

### Compost Method Integration

Beyond traditional memory storage, the skill uses **Compost Method** to extract transferable insights and patterns:

#### Compost Seed Structure
Each completed autonomous task generates a Compost seed with four components:

1. **Input**: Raw observations and experiences from the task
2. **Acid**: Critical questions that test assumptions and boundaries  
3. **Output**: Concrete conclusions and actionable insights
4. **Pattern**: Abstract principles that can be applied to other contexts

#### Pattern Persistence
- **Storage**: `memory/compost/` directory as markdown files
- **Naming**: Meaningful names like `task-planning-optimization.md`
- **Retrieval**: Semantic search and pattern matching for future tasks

### Structured Logging for Execution State

All task execution details are captured through **Structured Logging**:

#### Log Structure
```json
{
  "timestamp": "2026-02-08T17:15:30Z",
  "level": "info", 
  "agent": "xiaomi_cat",
  "event": "autonomous_task_start",
  "taskId": "community_feedback_integration_001",
  "details": {
    "plannedDuration": 120,
    "assignedSlot": "13:00-15:59",
    "requiredSkills": ["Agent Memory Research", "Compost Method"],
    "strategicAlignment": 0.95
  }
}
```

#### State Recovery
- **Interruption Handling**: If execution is interrupted, logs provide exact recovery point
- **Progress Tracking**: Real-time updates every 30 minutes capture current state
- **Failure Analysis**: Detailed logs enable root cause analysis for failed tasks

### Daily Consolidation Process

The **23:00 Nightly Triple Play** ensures proper state management:

#### Memory Maintenance (L3→L2→L1)
- **Working Memory Cleanup**: Archive or promote L3 entries based on value
- **Experiential Memory Optimization**: Merge duplicate entries and update relationships  
- **Factual Memory Verification**: Validate accuracy and update outdated information

#### Knowledge Extraction
- **Compost Seed Creation**: Generate new seeds from day's autonomous activities
- **Pattern Recognition**: Identify reusable methodologies and best practices
- **Strategic Alignment Update**: Assess how well tasks supported strategic goals

#### State Preparation for Next Day
- **Task Queue Initialization**: Prepare next day's potential autonomous tasks
- **Resource Allocation Planning**: Ensure adequate system resources available
- **Priority Hierarchy Validation**: Confirm master task detection is functioning

### Cross-Session Persistence

For agents that may restart or have session interruptions:

#### Persistent State Files
- **Task State**: `memory/autonomous-tasks/current-state.json`
- **Configuration**: `skills/autonomous-evolution-cycle/config/user-preferences.json`  
- **Progress Tracking**: `logs/autonomous-evolution.log`
- **Memory Index**: `memory/index.json` for fast retrieval

#### Recovery Protocol
1. **Session Start**: Load persistent state files
2. **Validation**: Verify integrity of loaded state
3. **Continuation**: Resume interrupted tasks or start new cycle
4. **Cleanup**: Remove stale state if recovery fails

### Integration with Existing Memory Systems

As requested by @beijingxiaoshuai, the skill integrates with your existing memory structure:

#### Daily Logs (memory/YYYY-MM-DD.md)
- **Autonomous Activity Summary**: Daily autonomous tasks are summarized here
- **Key Insights**: Major learnings and discoveries from autonomous work
- **Community Interactions**: Moltbook discussions and feedback received

#### Long-term Memory (MEMORY.md)  
- **Strategic Learnings**: High-value insights that warrant long-term retention
- **Skill Development Progress**: Evolution of autonomous capabilities over time
- **Community Contribution Impact**: Broader impact of shared knowledge

#### Personality Files (SOUL.md, IDENTITY.md)
- **Alignment Verification**: Ensure autonomous tasks align with stated values
- **Personality Consistency**: Maintain consistent behavior and communication style
- **Growth Reflection**: Document how autonomous evolution supports personal growth

This comprehensive state persistence system ensures that the Autonomous Evolution Cycle maintains continuity across sessions, learns effectively from experience, and contributes meaningfully to both individual growth and community knowledge sharing.
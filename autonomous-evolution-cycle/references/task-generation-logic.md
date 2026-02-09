# Intelligent Task Generation Logic

## Morning Decision Flow (07:00-08:00)

### Step 1: Check Previous Day Status
```
IF yesterday had autonomous tasks:
    → Load completion status from memory/logs
    → Identify incomplete or blocked tasks
    → Analyze reasons for non-completion
ELSE:
    → Proceed to free activity analysis
```

### Step 2: Handle Incomplete Tasks
```
FOR each incomplete task:
    → Assess current status (partially done, blocked, abandoned)
    → Evaluate priority and relevance
    → Decide action:
        - Continue with adjusted timeline
        - Modify scope to make achievable  
        - Archive with lessons learned
        - Escalate to human if needed
```

### Step 3: Analyze Free Activity Discoveries
```
IF no incomplete tasks requiring attention:
    → Review free activity time (05:00-07:00) discoveries
    → Extract new interests, tools, or opportunities
    → Evaluate against strategic objectives
    → Generate new autonomous task proposals
```

### Step 4: Master Task Priority Check
```
ALWAYS check for master-assigned tasks:
    → Scan recent communications for explicit instructions
    → Check task queue for high-priority items
    → Verify calendar for scheduled commitments
    → Ensure autonomous tasks don't conflict with master priorities
```

### Step 5: Final Task Plan Assembly
```
Construct daily plan with proper prioritization:
    1. Master-assigned tasks (highest priority)
    2. Continued incomplete autonomous tasks  
    3. New autonomous tasks from free activity discoveries
    4. Maintenance and optimization tasks (lowest priority)
```

## Priority Hierarchy

### Absolute Priority Order
1. **Master Direct Instructions** - Explicit commands from human
2. **Scheduled Commitments** - Calendar events, deadlines, appointments  
3. **Critical System Maintenance** - Security updates, backups, monitoring
4. **Incomplete Autonomous Tasks** - Previously started work
5. **New Autonomous Tasks** - Fresh discoveries and learning opportunities

### Conflict Resolution Rules
- **Time conflicts**: Master tasks always win, autonomous tasks reschedule
- **Resource conflicts**: Master tasks get priority access to system resources  
- **Attention conflicts**: Interrupt autonomous work for master requests immediately
- **Strategic alignment**: Autonomous tasks must support master's strategic goals

## Implementation Guidelines

### Detection Mechanisms
- **Master task detection**: Monitor chat history, task files, calendar
- **Priority assessment**: Use clear criteria for task classification  
- **Conflict identification**: Real-time checking before task execution
- **Graceful degradation**: Reduce autonomous task scope when master tasks increase

### Communication Protocol
- **Transparency**: Always report when autonomous tasks are delayed/rescheduled
- **Justification**: Explain priority decisions clearly to master
- **Options**: Provide alternatives when conflicts occur
- **Confirmation**: Seek approval for significant autonomous task changes

## Quality Assurance

### Validation Checks
- **Priority compliance**: Verify master tasks always take precedence
- **Continuity preservation**: Ensure incomplete tasks aren't lost
- **Discovery value**: Confirm new tasks add real value
- **Resource efficiency**: Optimize system resource usage across all priorities

### Error Handling
- **Missing master tasks**: Conservative approach - assume high priority
- **Ambiguous priorities**: Request clarification rather than guess
- **System overload**: Automatically reduce autonomous task load
- **Emergency situations**: Suspend all autonomous tasks immediately

This intelligent task generation logic ensures that autonomous evolution supports, rather than competes with, the master's primary objectives while maintaining continuity and fostering innovation through free activity discoveries.
# Priority Management Protocol

## Master Task Priority (Highest)

### Detection Mechanisms
- **Direct Commands**: Any explicit instruction from the human owner
- **Task Files**: Check for master task files in workspace
- **Scheduled Tasks**: Monitor for master-scheduled tasks in cron system
- **Real-time Requests**: Immediate response to owner requests

### Priority Hierarchy
1. **Master Tasks** - Owner's explicit instructions (highest priority)
2. **Critical System Tasks** - Security, maintenance, heartbeat
3. **Autonomous Evolution Tasks** - Self-generated tasks (lowest priority)

### Preemption Rules
- **Immediate Preemption**: Master tasks interrupt autonomous tasks immediately
- **Graceful Degradation**: Save autonomous task state before switching
- **Resumption Logic**: Resume autonomous tasks when master tasks complete
- **Resource Allocation**: Reduce autonomous task resources when master tasks active

## Intelligent Task Generation (07:00-08:00)

### Decision Flow
```
IF master has active tasks:
    → Suspend autonomous planning
    → Focus on supporting master tasks
    → Generate only complementary autonomous tasks

ELSE IF yesterday had incomplete autonomous tasks:
    → Evaluate completion status and blockers
    → Decide: continue, modify, or abandon
    → Generate today's plan based on evaluation

ELSE:
    → Analyze free activity discoveries (05:00-07:00)
    → Extract new opportunities and interests
    → Generate new autonomous task plan
```

### State Preservation
- **Task Checkpoints**: Save progress at logical breakpoints
- **Context Snapshots**: Preserve working memory for resumption
- **Dependency Tracking**: Maintain task relationships and prerequisites
- **Resource Cleanup**: Release resources when preempted

## Conflict Resolution

### Resource Conflicts
- **CPU/Memory**: Yield to master tasks immediately
- **Time Slots**: Reschedule autonomous tasks to available windows
- **API Calls**: Throttle autonomous usage when master needs bandwidth
- **File Access**: Use non-blocking operations to avoid conflicts

### Communication Protocol
- **Transparency**: Always report when autonomous tasks are preempted
- **Estimation Updates**: Recalculate timelines when interrupted
- **Alternative Suggestions**: Propose ways to support master tasks
- **Resumption Notification**: Alert when autonomous tasks can resume

## Implementation Guidelines

### Detection Implementation
```bash
# Check for master tasks
check_master_tasks() {
    # Look for explicit task files
    if [ -f "$WORKSPACE/master-tasks.json" ]; then
        return 0
    fi
    
    # Check for recent owner commands
    if [ -f "$WORKSPACE/owner-commands.log" ]; then
        # Parse recent commands for task indicators
        recent_command=$(tail -1 "$WORKSPACE/owner-commands.log")
        if [[ "$recent_command" == *"task"* || "$recent_command" == *"do"* ]]; then
            return 0
        fi
    fi
    
    return 1
}
```

### Preemption Implementation
```bash
# Safe task preemption
preempt_autonomous_task() {
    local task_id="$1"
    
    # Save current state
    save_task_checkpoint "$task_id"
    
    # Release resources
    cleanup_task_resources "$task_id"
    
    # Notify owner
    log "Autonomous task $task_id preempted for master task"
    
    # Switch context
    switch_to_master_context
}
```

### Resumption Implementation
```bash
# Resume autonomous tasks
resume_autonomous_task() {
    local task_id="$1"
    
    # Verify master task completion
    if ! master_tasks_complete; then
        return 1
    fi
    
    # Restore state
    restore_task_checkpoint "$task_id"
    
    # Reacquire resources
    setup_task_resources "$task_id"
    
    # Continue execution
    continue_task_execution "$task_id"
}
```

## Quality Assurance

### Priority Validation
- **Never override master tasks**: Autonomous tasks must always yield
- **Graceful degradation**: Ensure system stability during preemption
- **State integrity**: Verify task state preservation and restoration
- **Resource fairness**: Balance resource allocation appropriately

### Testing Scenarios
1. **Master task during autonomous execution**: Verify immediate preemption
2. **Multiple master tasks**: Verify proper queuing and execution
3. **Master task completion**: Verify autonomous task resumption
4. **Concurrent master and autonomous**: Verify resource sharing

## Error Handling

### Common Scenarios
- **Failed preemption**: Log error and force resource release
- **Corrupted checkpoints**: Fall back to task restart with warning
- **Resource conflicts**: Implement exponential backoff retry logic
- **Priority confusion**: Default to master task priority when uncertain

## Security Considerations

- **Authentication**: Verify master task authenticity before preemption
- **Authorization**: Ensure only authorized users can trigger preemption
- **Audit logging**: Log all preemption and resumption events
- **Resource protection**: Prevent autonomous tasks from monopolizing critical resources
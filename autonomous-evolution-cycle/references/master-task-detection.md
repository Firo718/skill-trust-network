# Master Task Detection and Dynamic Adjustment

## Detection Sources

### 1. Chat History Analysis
- **Scan recent messages** for explicit task assignments
- **Identify command patterns**: "do this", "help me with", "can you"
- **Extract deadlines and priorities** from conversation context
- **Track ongoing task discussions** and commitments

### 2. TASK_SCHEDULE.md Integration  
- **Parse scheduled tasks** with master authorization markers
- **Identify high-priority time slots** reserved for master tasks
- **Detect recurring master commitments** (daily, weekly patterns)
- **Monitor task completion requirements** and dependencies

### 3. Calendar Event Monitoring
- **Check upcoming appointments** that require preparation
- **Identify deadline-driven events** requiring advance work
- **Monitor meeting schedules** that may impact available time
- **Track recurring commitments** (weekly reviews, monthly reports)

### 4. System Queue Monitoring
- **Scan pending task queues** for master-assigned items
- **Monitor background job status** for master-initiated processes  
- **Track resource allocation** to master-critical systems
- **Identify emergency or urgent flags** in task metadata

## Dynamic Adjustment Mechanisms

### Time Slot Reallocation
```
IF master task detected in time slot X:
    → Reduce autonomous task allocation in slot X
    → Attempt to reschedule to flexible time slots
    → If no flexibility available, reduce task scope
    → As last resort, defer autonomous task to next day
```

### Priority Recalibration  
```
WHEN master task priority increases:
    → Immediately pause non-critical autonomous tasks
    → Preserve critical system maintenance tasks only
    → Prepare resources for master task support
    → Notify master of autonomous task adjustments
```

### Workload Optimization
```
BASED on master task load assessment:
    → Light load: Full autonomous task execution
    → Medium load: Reduced autonomous task scope  
    → Heavy load: Minimal autonomous tasks (only critical maintenance)
    → Critical load: Suspend all autonomous tasks temporarily
```

## Implementation Strategy

### Real-time Detection
- **Pre-execution check**: Before starting any autonomous task
- **Periodic monitoring**: Every 15 minutes during active periods  
- **Event-driven alerts**: Immediate response to new master tasks
- **Context-aware analysis**: Understand task relationships and dependencies

### Graceful Adjustment
- **Transparent communication**: Always explain adjustments to master
- **Preserve continuity**: Save progress on interrupted autonomous tasks
- **Maintain quality**: Don't compromise on critical autonomous functions
- **Learn patterns**: Adapt detection sensitivity based on master preferences

## Quality Assurance

### Validation Metrics
- **Detection accuracy**: Percentage of master tasks correctly identified
- **Adjustment appropriateness**: Master satisfaction with autonomous task changes  
- **Resource efficiency**: Optimal use of available time and system resources
- **Continuity preservation**: Successful resumption of interrupted autonomous tasks

### Error Handling
- **False positives**: Conservative approach - better to over-respect than under-respect
- **Missed detections**: Regular scanning intervals minimize risk
- **System conflicts**: Clear escalation path to human intervention
- **Performance impact**: Lightweight detection to avoid system overhead

## Integration with Core Workflow

### Morning Planning (07:00-08:00)
- Run comprehensive master task detection
- Generate autonomous plan with appropriate adjustments
- Present clear rationale for any limitations or changes

### Execution Phase (13:00-22:59)  
- Continuous monitoring for new master tasks
- Real-time adjustment of autonomous task execution
- Immediate response to priority changes

### Evening Review (23:00)
- Analyze master task impact on autonomous evolution
- Update detection sensitivity and adjustment strategies
- Plan improved integration for following day

This master task detection system ensures that autonomous evolution always supports rather than competes with the master's primary objectives, creating a truly collaborative agent-human partnership.
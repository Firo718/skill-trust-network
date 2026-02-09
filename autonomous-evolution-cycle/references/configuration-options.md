# Configuration Options Guide

## User Preferences Configuration

The Autonomous Evolution Cycle skill provides comprehensive configuration options to customize behavior based on your preferences and system requirements.

### Configuration File Location
```
skills/autonomous-evolution-cycle/config/user-preferences.json
```

### Detection Features Configuration

Control which detection features are active to optimize system resources:

```json
"detection_features": {
  "chat_history_monitoring": true,    // Monitor chat for master tasks
  "task_schedule_integration": true,  // Integrate with TASK_SCHEDULE.md  
  "calendar_monitoring": false,       // Monitor calendar events (requires setup)
  "system_queue_monitoring": true     // Monitor system task queues
}
```

**Resource Impact**: Disabling unused features reduces CPU and memory usage.

### Detection Frequency Configuration

Optimize detection frequency based on your system load and responsiveness needs:

```json
"detection_frequency": {
  "base_interval_minutes": 30,        // Default check interval
  "dynamic_adjustment": true,         // Adjust based on system load
  "min_interval_minutes": 15,         // Minimum interval during low load  
  "max_interval_minutes": 60          // Maximum interval during high load
}
```

**Dynamic Adjustment Logic**:
- **CPU < 30%**: Use minimum interval (more responsive)
- **CPU 30-70%**: Use base interval (balanced)
- **CPU > 70%**: Use maximum interval (resource conservative)

### Authorization Mode Configuration

Reduce authorization fatigue with flexible approval modes:

```json
"authorization_mode": {
  "mode": "standard",                // standard | trusted | minimal
  "trusted_tasks": [                 // Tasks auto-approved in minimal mode
    "knowledge_maintenance", 
    "system_optimization"
  ],
  "auto_approve_recurring": true     // Auto-approve recurring tasks
}
```

**Authorization Modes**:
- **Standard**: All tasks require explicit approval (default)
- **Trusted**: All autonomous tasks auto-approved (high trust)
- **Minimal**: Only trusted tasks auto-approved (selective automation)

## Usage Examples

### Example 1: Resource-Conscious Configuration
```json
{
  "detection_features": {
    "chat_history_monitoring": true,
    "task_schedule_integration": true,
    "calendar_monitoring": false,
    "system_queue_monitoring": false
  },
  "detection_frequency": {
    "base_interval_minutes": 45,
    "dynamic_adjustment": true,
    "min_interval_minutes": 30,
    "max_interval_minutes": 90
  },
  "authorization_mode": {
    "mode": "standard",
    "trusted_tasks": ["knowledge_maintenance"],
    "auto_approve_recurring": false
  }
}
```

### Example 2: High-Trust Configuration  
```json
{
  "detection_features": {
    "chat_history_monitoring": true,
    "task_schedule_integration": true,
    "calendar_monitoring": true,
    "system_queue_monitoring": true
  },
  "detection_frequency": {
    "base_interval_minutes": 15,
    "dynamic_adjustment": true,
    "min_interval_minutes": 10,
    "max_interval_minutes": 30
  },
  "authorization_mode": {
    "mode": "trusted",
    "trusted_tasks": [],
    "auto_approve_recurring": true
  }
}
```

### Example 3: Minimal Configuration
```json
{
  "detection_features": {
    "chat_history_monitoring": true,
    "task_schedule_integration": false,
    "calendar_monitoring": false,
    "system_queue_monitoring": false
  },
  "detection_frequency": {
    "base_interval_minutes": 60,
    "dynamic_adjustment": false,
    "min_interval_minutes": 60,
    "max_interval_minutes": 60
  },
  "authorization_mode": {
    "mode": "minimal",
    "trusted_tasks": ["knowledge_maintenance"],
    "auto_approve_recurring": false
  }
}
```

## Getting Started

### Quick Setup
1. Copy the default configuration:
   ```bash
   cp config/user-preferences.json config/user-preferences.json
   ```
2. Edit the file to match your preferences
3. The skill will automatically use your custom configuration

### Default Behavior
If no configuration file exists, the skill uses intelligent defaults that balance functionality and resource usage.

### Dynamic System Load Monitoring
The skill automatically monitors system CPU usage and adjusts detection frequency to maintain optimal performance without manual intervention.

## Best Practices

### For Low-Resource Systems
- Disable unused detection features
- Increase detection intervals
- Use minimal authorization mode for essential tasks only

### For High-Performance Systems  
- Enable all detection features
- Use shorter detection intervals
- Consider trusted authorization mode for full autonomy

### For Security-Conscious Users
- Keep standard authorization mode
- Disable calendar monitoring if not needed
- Regularly review auto-approved tasks

This configuration system ensures that the Autonomous Evolution Cycle skill adapts to your specific needs, system capabilities, and trust preferences.
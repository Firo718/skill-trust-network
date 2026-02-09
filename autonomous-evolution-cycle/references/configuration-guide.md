# Configuration Guide

## Automatic Configuration Detection

The Autonomous Evolution Cycle skill automatically detects and configures time slots using the following priority:

1. **User Custom Configuration** (`config/user-time-slots.json`)
2. **TASK_SCHEDULE.md Integration** (if available)
3. **Default Configuration** (`config/default-time-slots.json`)

## Configuration Options

### Time Slot Configuration
```json
{
  "planning_slot": {
    "start": "06:00",
    "end": "08:00", 
    "description": "Time for autonomous task planning"
  },
  "deep_work_slots": [
    {
      "start": "09:00",
      "end": "12:00",
      "description": "Deep work session 1"
    }
  ],
  "flexible_slots": [
    {
      "start": "19:00",
      "end": "22:00",
      "description": "Flexible task completion"
    }
  ],
  "consolidation_slot": {
    "time": "23:00",
    "description": "Daily knowledge consolidation"
  }
}
```

### Advanced Settings
- `progress_tracking_interval`: Minutes between progress updates (default: 30)
- `max_concurrent_tasks`: Maximum number of simultaneous tasks (default: 3)  
- `workload_estimation_buffer`: Multiplier for workload estimates (default: 1.2)

## Creating Custom Configuration

To create your own time slot configuration:

1. Copy the default configuration:
   ```bash
   cp config/default-time-slots.json config/user-time-slots.json
   ```

2. Edit `user-time-slots.json` with your preferred time slots

3. The skill will automatically use your custom configuration on next run

## TASK_SCHEDULE.md Integration

If you have a `TASK_SCHEDULE.md` file, the skill will automatically:
- Detect your free activity time for planning
- Identify research/development periods for deep work
- Find flexible task windows for completion
- Locate your daily review time for consolidation

This provides seamless integration with your existing workflow without any manual configuration.

## Interactive Setup (Coming Soon)

For agents without any time configuration, we plan to add an interactive setup wizard that will:
- Ask about your preferred working hours
- Suggest optimal time slot arrangements
- Create a custom configuration based on your preferences

## Compatibility Notes

- **Time Format**: Supports 24-hour format (HH:MM)
- **Multiple Slots**: You can define multiple deep work or flexible slots
- **Cross-Platform**: Works on all systems that support OpenClaw
- **Backward Compatible**: Will work even if some configuration options are missing

## Troubleshooting

### No Time Slots Detected
- Ensure your `TASK_SCHEDULE.md` uses standard time format (HH:MM)
- Check that time slots are properly formatted in the markdown file
- Verify file permissions allow reading

### Custom Configuration Not Loading
- Ensure `user-time-slots.json` is valid JSON
- Check that the file is in the correct `config/` directory
- Verify the file has proper read permissions

### Performance Issues
- Reduce `max_concurrent_tasks` if system resources are limited
- Increase `progress_tracking_interval` to reduce overhead
- Use simpler time slot configurations for basic use cases
#!/bin/bash
# Autonomous Evolution Cycle - Time Slot Detector
# Detects and configures time slots based on user's environment

set -euo pipefail

WORKSPACE="$HOME/.openclaw/workspace"
CONFIG_DIR="$WORKSPACE/skills/autonomous-evolution-cycle/config"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] time-slot-detector: $*" >> "$WORKSPACE/logs/autonomous-evolution.log"
}

# Check for user custom configuration
check_user_config() {
    if [ -f "$CONFIG_DIR/user-time-slots.json" ]; then
        log "Using user custom time slot configuration"
        cp "$CONFIG_DIR/user-time-slots.json" "$CONFIG_DIR/active-time-slots.json"
        return 0
    fi
    return 1
}

# Parse TASK_SCHEDULE.md if it exists
parse_task_schedule() {
    if [ -f "$WORKSPACE/TASK_SCHEDULE.md" ]; then
        log "Detected TASK_SCHEDULE.md, parsing for time slots"
        
        # Extract free activity time (05:00-07:00 pattern)
        free_activity_start=$(grep -A5 "自由活动时间" "$WORKSPACE/TASK_SCHEDULE.md" | grep -E "[0-2][0-9]:[0-5][0-9]" | head -1 | cut -d' ' -f1 | tr -d '[:space:]')
        if [ -n "$free_activity_start" ]; then
            planning_start="$free_activity_start"
            # Assume 2-hour window
            planning_end="07:00"
        else
            planning_start="06:00"
            planning_end="08:00"
        fi
        
        # Extract research/development time (13:00-15:59 pattern)  
        research_time=$(grep -A10 "研究与开发时段" "$WORKSPACE/TASK_SCHEDULE.md" | grep -E "[0-2][0-9]:[0-5][0-9]" | head -1 | cut -d' ' -f1 | tr -d '[:space:]')
        if [ -n "$research_time" ]; then
            deep_work_start="$research_time"
            deep_work_end="15:59"
        else
            deep_work_start="09:00"
            deep_work_end="12:00"
        fi
        
        # Extract flexible task time (20:00-22:59 pattern)
        flexible_time=$(grep -A10 "灵活任务时段" "$WORKSPACE/TASK_SCHEDULE.md" | grep -E "[0-2][0-9]:[0-5][0-9]" | head -1 | cut -d' ' -f1 | tr -d '[:space:]')
        if [ -n "$flexible_time" ]; then
            flexible_start="$flexible_time"
            flexible_end="22:59"
        else
            flexible_start="19:00"
            flexible_end="22:00"
        fi
        
        # Create optimized configuration
        cat > "$CONFIG_DIR/active-time-slots.json" << EOF
{
  "planning_slot": {
    "start": "$planning_start",
    "end": "$planning_end",
    "description": "Free activity time from TASK_SCHEDULE.md"
  },
  "deep_work_slots": [
    {
      "start": "$deep_work_start",
      "end": "$deep_work_end",
      "description": "Research and development time from TASK_SCHEDULE.md"
    }
  ],
  "flexible_slots": [
    {
      "start": "$flexible_start",
      "end": "$flexible_end", 
      "description": "Flexible task time from TASK_SCHEDULE.md"
    }
  ],
  "consolidation_slot": {
    "time": "23:00",
    "description": "Daily review from TASK_SCHEDULE.md"
  },
  "progress_tracking_interval": 30,
  "max_concurrent_tasks": 3,
  "workload_estimation_buffer": 1.2
}
EOF
        log "Created optimized time slot configuration from TASK_SCHEDULE.md"
        return 0
    fi
    return 1
}

# Use default configuration
use_default_config() {
    log "Using default time slot configuration"
    cp "$CONFIG_DIR/default-time-slots.json" "$CONFIG_DIR/active-time-slots.json"
}

# Main execution
main() {
    # Priority 1: User custom config
    if check_user_config; then
        exit 0
    fi
    
    # Priority 2: TASK_SCHEDULE.md parsing
    if parse_task_schedule; then
        exit 0
    fi
    
    # Priority 3: Default config
    use_default_config
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
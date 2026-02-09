#!/bin/bash
# Autonomous Evolution Cycle - Preference Manager
# Manages user configuration preferences for detection features, frequency, and authorization

set -euo pipefail

WORKSPACE="$HOME/.openclaw/workspace"
CONFIG_DIR="$WORKSPACE/skills/autonomous-evolution-cycle/config"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] preference-manager: $*" >> "$WORKSPACE/logs/autonomous-evolution.log"
}

# Load user preferences or create default
load_preferences() {
    if [ -f "$CONFIG_DIR/user-preferences.json" ]; then
        log "Loading user preferences from $CONFIG_DIR/user-preferences.json"
        cat "$CONFIG_DIR/user-preferences.json"
    else
        log "No user preferences found, creating default configuration"
        create_default_preferences
        cat "$CONFIG_DIR/user-preferences.json"
    fi
}

# Create default preferences
create_default_preferences() {
    cat > "$CONFIG_DIR/user-preferences.json" << EOF
{
  "detection_features": {
    "chat_history_monitoring": true,
    "task_schedule_integration": true,
    "calendar_monitoring": false,
    "system_queue_monitoring": true
  },
  "detection_frequency": {
    "base_interval_minutes": 30,
    "dynamic_adjustment": true,
    "min_interval_minutes": 15,
    "max_interval_minutes": 60
  },
  "authorization_mode": {
    "mode": "standard",
    "trusted_tasks": ["knowledge_maintenance", "system_optimization"],
    "auto_approve_recurring": true
  }
}
EOF
}

# Get detection interval based on system load
get_dynamic_interval() {
    local base_interval=$(jq -r '.detection_frequency.base_interval_minutes' "$CONFIG_DIR/user-preferences.json")
    local dynamic_adjustment=$(jq -r '.detection_frequency.dynamic_adjustment' "$CONFIG_DIR/user-preferences.json")
    
    if [ "$dynamic_adjustment" = "true" ]; then
        # Simple system load check (CPU usage)
        local cpu_load=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
        local cpu_percent=${cpu_load%%.*}
        
        if [ "$cpu_percent" -gt 70 ]; then
            # High load - increase interval to reduce overhead
            local max_interval=$(jq -r '.detection_frequency.max_interval_minutes' "$CONFIG_DIR/user-preferences.json")
            echo "$max_interval"
        elif [ "$cpu_percent" -lt 30 ]; then
            # Low load - decrease interval for better responsiveness  
            local min_interval=$(jq -r '.detection_frequency.min_interval_minutes' "$CONFIG_DIR/user-preferences.json")
            echo "$min_interval"
        else
            # Medium load - use base interval
            echo "$base_interval"
        fi
    else
        echo "$base_interval"
    fi
}

# Check if task should be auto-approved
should_auto_approve() {
    local task_type="$1"
    local auth_mode=$(jq -r '.authorization_mode.mode' "$CONFIG_DIR/user-preferences.json")
    
    if [ "$auth_mode" = "trusted" ]; then
        # In trusted mode, auto-approve all tasks
        return 0
    elif [ "$auth_mode" = "minimal" ]; then
        # In minimal mode, only auto-approve trusted tasks
        if jq -r '.authorization_mode.trusted_tasks[]' "$CONFIG_DIR/user-preferences.json" | grep -q "^$task_type$"; then
            return 0
        fi
    fi
    
    # Standard mode requires approval
    return 1
}

# Main execution
main() {
    case "${1:-}" in
        "load")
            load_preferences
            ;;
        "interval")
            get_dynamic_interval
            ;;
        "auto_approve")
            if should_auto_approve "$2"; then
                echo "true"
            else
                echo "false"
            fi
            ;;
        *)
            echo "Usage: $0 {load|interval|auto_approve <task_type>}"
            exit 1
            ;;
    esac
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
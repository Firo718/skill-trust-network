#!/bin/bash
# Autonomous Evolution Cycle - Master Task Detector
# Detects master-assigned tasks and adjusts autonomous scheduling accordingly

set -euo pipefail

WORKSPACE="$HOME/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] master-task-detector: $*" >> "$LOG_DIR/autonomous-evolution.log"
}

# Check recent chat history for explicit instructions
check_chat_history() {
    local recent_tasks=0
    
    # Look for task-related keywords in recent messages
    if [ -f "$WORKSPACE/memory/2026-02-08.md" ]; then
        # Count explicit task assignments
        recent_tasks=$(grep -c -E "(task|please do|execute|run|create|build|implement)" "$WORKSPACE/memory/2026-02-08.md" 2>/dev/null || echo 0)
    fi
    
    log "Detected $recent_tasks explicit tasks from chat history"
    return $recent_tasks
}

# Check TASK_SCHEDULE.md for scheduled commitments
check_scheduled_tasks() {
    local scheduled_count=0
    
    if [ -f "$WORKSPACE/TASK_SCHEDULE.md" ]; then
        # Count high-priority scheduled tasks
        scheduled_count=$(grep -c -E "(定时任务|股票分析|深度分析|复盘)" "$WORKSPACE/TASK_SCHEDULE.md" 2>/dev/null || echo 0)
    fi
    
    log "Detected $scheduled_count scheduled commitments"
    return $scheduled_count
}

# Check system load and resource availability
check_system_load() {
    local cpu_load=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    local memory_usage=$(free | awk 'NR==2{printf "%.2f", $3*100/$2 }')
    
    log "System load - CPU: ${cpu_load}%, Memory: ${memory_usage}%"
    
    # High load threshold
    if (( $(echo "$cpu_load > 70" | bc -l) )) || (( $(echo "$memory_usage > 80" | bc -l) )); then
        return 1  # High load detected
    else
        return 0  # Normal load
    fi
}

# Calculate autonomous task adjustment
calculate_adjustment() {
    local chat_tasks=$1
    local scheduled_tasks=$2
    local system_load=$3
    
    local adjustment_factor=1.0
    
    # Reduce autonomous tasks based on master task load
    if [ $chat_tasks -gt 2 ] || [ $scheduled_tasks -gt 5 ]; then
        adjustment_factor=0.5  # Reduce by 50%
    elif [ $chat_tasks -gt 0 ] || [ $scheduled_tasks -gt 3 ]; then
        adjustment_factor=0.7  # Reduce by 30%
    fi
    
    # Further reduce if system is under heavy load
    if [ $system_load -eq 1 ]; then
        adjustment_factor=$(echo "$adjustment_factor * 0.8" | bc -l)
    fi
    
    # Ensure minimum adjustment factor
    if (( $(echo "$adjustment_factor < 0.3" | bc -l) )); then
        adjustment_factor=0.3
    fi
    
    echo "$adjustment_factor"
}

# Main execution
main() {
    log "Starting master task detection and autonomous scheduling adjustment"
    
    # Detect master tasks
    check_chat_history
    local chat_tasks=$?
    
    check_scheduled_tasks  
    local scheduled_tasks=$?
    
    check_system_load
    local system_load=$?
    
    # Calculate adjustment
    local adjustment_factor=$(calculate_adjustment $chat_tasks $scheduled_tasks $system_load)
    
    log "Autonomous task adjustment factor: $adjustment_factor"
    
    # Save adjustment to config
    cat > "$WORKSPACE/skills/autonomous-evolution-cycle/config/master-adjustment.json" << EOF
{
  "adjustment_factor": $adjustment_factor,
  "master_tasks_detected": {
    "chat_tasks": $chat_tasks,
    "scheduled_tasks": $scheduled_tasks,
    "system_load_high": $system_load
  },
  "timestamp": "$(date -Iseconds)"
}
EOF
    
    log "Master task detection completed successfully"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
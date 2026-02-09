#!/bin/bash
# Autonomous Evolution Cycle - Task Executor
# Executes autonomous tasks using Infrastructure Automation framework

set -euo pipefail

# Configuration
WORKSPACE="$HOME/.openclaw/workspace"
LOG_DIR="$WORKSPACE/logs"
SCRIPT_NAME=$(basename "$0")

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $SCRIPT_NAME: $*" >> "$LOG_DIR/autonomous-evolution.log"
}

# Error handling
cleanup() {
    log "Task execution completed with exit code $?"
}
trap cleanup EXIT

# Task execution function
execute_task() {
    local task_id="$1"
    local task_type="$2"
    local task_params="$3"
    
    log "Starting autonomous task: $task_id ($task_type)"
    
    case "$task_type" in
        "research")
            # Execute research task using Infrastructure Automation
            ~/.openclaw/workspace/automation/scripts/research-task.sh "$task_params"
            ;;
        "automation_script")
            # Create or execute automation script
            ~/.openclaw/workspace/automation/scripts/create-automation-script.sh "$task_params"
            ;;
        "knowledge_extraction")
            # Extract and store knowledge
            ~/.openclaw/workspace/automation/scripts/knowledge-extraction.sh "$task_params"
            ;;
        *)
            log "Unknown task type: $task_type"
            return 1
            ;;
    esac
    
    log "Task completed: $task_id"
}

# Main execution
main() {
    if [ $# -lt 3 ]; then
        echo "Usage: $0 <task_id> <task_type> <task_params>"
        exit 1
    fi
    
    execute_task "$1" "$2" "$3"
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
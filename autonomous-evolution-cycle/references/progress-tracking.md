# Progress Tracking Protocol

## Reporting Frequency
- **Every 30 minutes** during active task execution periods
- **Immediate reporting** for blockers or significant deviations (>20%)
- **End-of-day summary** during 23:00 nightly review

## Progress Report Format
```
[TIME] Task [TASK_ID] progress: [PERCENTAGE]% complete
- Status: [On schedule / Slight delay / Significant delay / Blocked]
- Actual vs Planned: [X hours actual / Y hours planned]
- Key accomplishments: [Brief summary of what was completed]
- Current challenges: [Any blockers or issues encountered]
- Next steps: [What will be done in the next period]
- Deviation analysis: [Why deviation occurred, if any]
```

## Deviation Handling
### Minor Deviation (<20%)
- Continue with current plan
- Adjust remaining time estimates
- Report in next scheduled update

### Major Deviation (20-50%)
- Immediately report deviation
- Propose adjusted timeline
- Request user feedback if needed

### Critical Deviation (>50%) or Blocked
- Immediately report blocker
- Propose alternative approaches
- Request user authorization for major changes

## Success Metrics
- **Task Completion Rate**: Percentage of tasks completed as planned
- **Workload Accuracy**: Actual hours vs estimated hours
- **Knowledge Contribution**: Number and quality of memory entries created
- **Strategic Alignment**: How well tasks supported strategic objectives

## Integration with Structured Logging
All progress reports are automatically logged to:
- `logs/tasks.jsonl` - Structured task execution logs
- `logs/autonomous-evolution.log` - Human-readable progress logs
- Memory system - Key insights and learnings

## Quality Assurance
- **Transparency**: Always report actual status, not just positive updates
- **Timeliness**: Never delay reporting of blockers or major issues
- **Actionability**: Always include proposed solutions with problem reports
- **Consistency**: Use consistent format and terminology across all reports
# Knowledge Extraction Protocol

## Memory Entry Types

### Factual Knowledge
**When to use**: Objective information, technical specifications, data, facts
**Format**:
```json
{
  "id": "unique-id",
  "type": "factual",
  "title": "Clear descriptive title",
  "content": "Detailed factual information",
  "tags": ["tag1", "tag2", "domain-specific"],
  "links": ["related-memory-ids"],
  "timestamps": {
    "created": "ISO8601",
    "updated": "ISO8601"
  },
  "confidence": 0.95,
  "source": "original-source-or-context"
}
```

### Experiential Knowledge  
**When to use**: Lessons learned, failure analysis, success patterns, personal insights
**Format**:
```json
{
  "id": "unique-id", 
  "type": "experiential",
  "title": "Experience summary",
  "content": "Detailed experience description including context, actions, and outcomes",
  "tags": ["lesson-learned", "success-pattern", "failure-analysis"],
  "links": ["related-factual-entries", "compost-seeds"],
  "timestamps": {
    "created": "ISO8601",
    "updated": "ISO8601"
  },
  "confidence": 0.85,
  "context": "specific-situation-or-project"
}
```

### Working Memory
**When to use**: Temporary context for ongoing projects, incomplete thoughts, active research
**Format**:
```json
{
  "id": "unique-id",
  "type": "working", 
  "title": "Working memory topic",
  "content": "Current state of thinking or research",
  "tags": ["active-project", "in-progress", "temporary"],
  "links": ["related-entries"],
  "timestamps": {
    "created": "ISO8601", 
    "updated": "ISO8601",
    "expires": "ISO8601"  // When this should be archived or deleted
  },
  "project": "associated-project-name"
}
```

## Compost Method Seed Creation

### Seed Structure
Every completed task should generate a Compost seed with four components:

#### Input
- Raw observations, data, or experiences from the task
- Include both successes and failures
- Capture unexpected discoveries

#### Acid (Critical Questions)
- What assumptions were tested?
- What could have gone wrong?
- How generalizable is this result?
- What are the boundary conditions?

#### Output  
- Concrete conclusions and actionable insights
- Verified patterns and reliable methods
- Clear recommendations for future use

#### Pattern
- Abstract principles that can be applied to other contexts
- Transferable methodologies and approaches
- General frameworks for similar problems

### Seed Storage
Compost seeds are stored as markdown files in `memory/compost/` with meaningful names:
- `skill-installation-insight.md`
- `task-planning-optimization.md`  
- `knowledge-extraction-best-practices.md`

## Integration with Agent Memory Research

### Automatic Categorization
- Use content analysis to determine appropriate memory type
- Apply relevant tags based on content domain
- Link related entries automatically

### Quality Validation
- Verify JSON format compliance before storage
- Check confidence levels and source attribution
- Ensure proper categorization and tagging

### Retrieval Optimization
- Index entries by tags and content for fast search
- Maintain relationship graphs between related entries
- Support semantic search across all memory types

## Best Practices

### Content Quality
- **Specificity**: Include concrete details and examples
- **Context**: Always provide sufficient background information  
- **Verification**: Only store information with appropriate confidence levels
- **Relevance**: Focus on information that will be useful in the future

### Organization
- **Consistency**: Use consistent formatting and terminology
- **Completeness**: Include all relevant metadata and relationships
- **Accessibility**: Structure content for easy retrieval and understanding
- **Maintenance**: Regularly review and update outdated entries

### Ethical Considerations
- **Privacy**: Never store sensitive personal information without proper handling
- **Accuracy**: Clearly distinguish between facts, opinions, and hypotheses
- **Attribution**: Always credit original sources when possible
- **Transparency**: Be clear about confidence levels and limitations
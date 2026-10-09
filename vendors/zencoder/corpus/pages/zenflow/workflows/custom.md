> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Workflows

> Design your own workflow steps with Markdown files — full control over phases, artifacts, and agent assignments.

## Overview

**Custom workflows** let you define your own task templates beyond the built-in options. Write a Markdown file describing the workflow steps, drop it in `.zenflow/workflows/` in your repo, and Zenflow surfaces it alongside the standard workflows when creating a task.

<Tip>
  **Credit Efficiency:** Custom workflows have **varying** credit costs depending on the number of steps and the models configured. Learn more in the [Workflow Credit Efficiency](/faq/pricing#workflow-credit-efficiency) reference guide.
</Tip>

## When to Use

* Recurring team processes (release prep, security audits, migrations)
* Compliance-driven workflows requiring specific documentation stages
* Domain-specific flows (ML training pipelines, data processing)
* When built-in workflows don't match your team's process

## Creating a Custom Workflow

### 1. Create the workflow file

Add a `.md` file to `.zenflow/workflows/` in your repository root:

```
your-repo/
├── .zenflow/
│   └── workflows/
│       └── security-review.md
```

### 2. Write the workflow definition

```markdown theme={"system"}
# Security Review Workflow

## Configuration
- **Artifacts Path**: {@artifacts_path}

---

## Workflow Steps

### [ ] Step: Threat Model
<!-- agent: opus-planner -->
Analyze the codebase for security-sensitive areas. Document potential
threats and attack surfaces in {@artifacts_path}/threat-model.md.

### [ ] Step: Implementation
<!-- agent: sonnet-builder -->
Implement security fixes and hardening measures identified in the
threat model. Update {@artifacts_path}/report.md with changes made.

### [ ] Step: Security Verification
<!-- agent: opus-reviewer -->
Review all changes against the threat model. Run security-focused
tests and static analysis. Document findings in {@artifacts_path}/review.md.
```

### 3. Use the workflow

When creating a new task, your custom workflow appears in the workflow picker alongside Auto, Fix a Bug, and others.

## Workflow File Structure

### Required Elements

| Element | Description |
| - | - |
| `# Title` | Top-level heading becomes the workflow name |
| `## Configuration` | Set shared variables like `Artifacts Path` |
| `### [ ] Step: Name` | Each step appears in the Steps column with a checkbox |

### Optional Elements

| Element | Description |
| - | - |
| `<!-- agent: preset-name -->` | Assign a specific agent preset to a step |
| `{@artifacts_path}` | Resolves to `.zenflow/worktrees/{task_id}` at runtime |
| Step instructions | Markdown below each step heading — objectives, acceptance criteria, deliverables |

## Agent Assignment

Assign different agent presets to different steps using HTML comments:

```markdown theme={"system"}
### [ ] Step: Planning
<!-- agent: opus-planner -->
Create the technical specification...

### [ ] Step: Implementation
<!-- agent: flash-builder -->
Implement the changes...

### [ ] Step: Review
<!-- agent: sonnet-reviewer -->
Review all changes...
```

Agent presets are configured in **Settings → Default agents**. Each preset defines a CLI, model, and execution configuration.

## Examples

<AccordionGroup>
  <Accordion title="Release Preparation">
    ```markdown theme={"system"}
    # Release Preparation

    ## Configuration
    - **Artifacts Path**: {@artifacts_path}

    ---

    ## Workflow Steps

    ### [ ] Step: Changelog Generation
    Review all commits since the last release tag. Generate a changelog
    grouped by category (features, fixes, breaking changes) in
    {@artifacts_path}/changelog.md.

    ### [ ] Step: Version Bump
    Update version numbers in package.json, pyproject.toml, or equivalent.
    Ensure all references are consistent.

    ### [ ] Step: Pre-Release Verification
    Run the full test suite, check for deprecation warnings, verify
    documentation links. Document results in {@artifacts_path}/verification.md.
    ```
  </Accordion>

  <Accordion title="Database Migration">
    ```markdown theme={"system"}
    # Database Migration

    ## Configuration
    - **Artifacts Path**: {@artifacts_path}

    ---

    ## Workflow Steps

    ### [ ] Step: Schema Analysis
    <!-- agent: opus-planner -->
    Analyze current schema and proposed changes. Document migration
    strategy, rollback plan, and data preservation approach in
    {@artifacts_path}/migration-plan.md.

    ### [ ] Step: Migration Implementation
    Generate migration files following the project's ORM conventions.
    Include both up and down migrations. Add data backfill scripts
    where needed.

    ### [ ] Step: Migration Testing
    Run migrations against a test database. Verify data integrity,
    check rollback works, and validate performance impact.
    Document results in {@artifacts_path}/test-results.md.
    ```
  </Accordion>

  <Accordion title="API Design Review">
    ```markdown theme={"system"}
    # API Design Review

    ## Configuration
    - **Artifacts Path**: {@artifacts_path}

    ---

    ## Workflow Steps

    ### [ ] Step: API Specification
    <!-- agent: opus-planner -->
    Create an OpenAPI specification for the proposed endpoints.
    Document request/response schemas, error codes, and rate limits
    in {@artifacts_path}/api-spec.md.

    ### [ ] Step: Implementation
    <!-- agent: flash-builder -->
    Implement the API endpoints following the specification.
    Include input validation, error handling, and integration tests.

    ### [ ] Step: Contract Testing
    Verify the implementation matches the OpenAPI spec exactly.
    Run contract tests and document any deviations in
    {@artifacts_path}/contract-report.md.
    ```
  </Accordion>
</AccordionGroup>

## Best Practices

* **Scope steps as coherent milestones** — each step should produce a clear deliverable
* **Use artifact placeholders** — `{@artifacts_path}/filename.md` resolves paths automatically per task
* **Write imperative instructions** — tell the agent what to produce, not just what to think about
* **Assign agents per step** — use reasoning models for planning and fast models for implementation
* **Version control workflows** — keep `.zenflow/workflows/` in your repo so the team shares the same processes

## Related

<CardGroup cols={2}>
  <Card title="All Workflows" icon="list" href="/zenflow/task-types">
    Compare all available workflows
  </Card>

  <Card title="Multi-Agent Orchestration" icon="sitemap" href="/zenflow/multi-agent-orchestration">
    Agent presets and subagent configuration
  </Card>

  <Card title="Subagents" icon="users" href="/zenflow/subagents">
    Spawn isolated sub-processes within workflow steps
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
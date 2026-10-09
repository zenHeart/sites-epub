> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Blast Multiple Agents

> Run multiple AI agents in parallel across different tasks for maximum throughput.

## Overview

Zenflow's parallel execution model lets you run multiple agents simultaneously across different tasks. This "blast" approach increases throughput—start the next task while agents finish the current one.

<Card title="Parallel execution" icon="bolt" horizontal>
  With Git worktrees isolating each task, there's no conflict between agents. Run as many parallel tasks as your system resources allow.
</Card>

## How It Works

### Isolated Workspaces

Each task runs in its own Git worktree:

```
.zenflow/
└── tasks/
    ├── task-abc123/    # Agent 1 working here
    ├── task-def456/    # Agent 2 working here
    └── task-ghi789/    # Agent 3 working here
```

Agents can't interfere with each other because they're working in completely separate directories.

### Independent Branches

Each task has its own branch:

* `zenflow/task-abc123`
* `zenflow/task-def456`
* `zenflow/task-ghi789`

Merge conflicts only matter when combining finished work, not during execution.

## Running Parallel Tasks

<Steps>
  <Step title="Create multiple tasks">
    Queue up the work you want done. Each task can use a different workflow and agent configuration.
  </Step>

  <Step title="Start tasks in sequence">
    Click **Create and Run** on each task. Zenflow handles the parallelism automatically.
  </Step>

  <Step title="Monitor from the dashboard">
    The Kanban board and task list show real-time status for all running tasks.
  </Step>

  <Step title="Review and merge">
    As tasks complete, review changes and merge successful work.
  </Step>
</Steps>

## Best Practices

<AccordionGroup>
  <Accordion title="Start with independent tasks" icon="puzzle-piece">
    Parallel execution works best when tasks don't depend on each other. If Task B needs Task A's output, run them sequentially instead.
  </Accordion>

  <Accordion title="Monitor resource usage" icon="gauge">
    Each task consumes disk space (worktree) and API credits (agent calls). Watch your system resources and subscription limits.
  </Accordion>

  <Accordion title="Stagger complex tasks" icon="clock">
    For resource-intensive workflows (Full SDD), consider staggering start times to avoid overloading your system or hitting rate limits.
  </Accordion>

  <Accordion title="Use different agents" icon="robot">
    Mix agent types across tasks to leverage different strengths—Claude for design, Codex for implementation, etc.
  </Accordion>
</AccordionGroup>

## Merge Strategies

When multiple parallel tasks complete:

### Sequential Merge

Merge tasks one at a time, resolving any conflicts as they arise:

1. Merge Task A to main
2. Rebase Task B on updated main, then merge
3. Repeat for remaining tasks

### Batch Review

Review all tasks first, then merge in a planned order based on dependencies and conflicts.

### Feature Flags

Merge all tasks but gate features behind flags for controlled rollout.

## Resource Considerations

| Resource | Per Task Impact |
| - | - |
| **Disk Space** | Full working copy of repo |
| **Memory** | Agent runtime + IDE if open |
| **API Credits** | Based on agent turns and model |
| **Network** | Git operations + API calls |

<Warning>
  A 500MB repo with 10 parallel tasks uses \~5GB of disk space. Archive completed tasks regularly to reclaim space.
</Warning>

## Next Steps

<CardGroup cols={2}>
  <Card title="Tasks Overview" icon="check-square" href="./tasks-overview">
    Full guide to task management
  </Card>

  <Card title="Multi-Agent Orchestration" icon="robot" href="./multi-agent-orchestration">
    Multi-model pipelines and agent presets
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
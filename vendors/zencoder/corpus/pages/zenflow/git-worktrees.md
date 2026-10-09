> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Git and Worktrees

> How Zenflow uses Git worktrees for isolated, parallel task execution.

## Understanding Git Worktrees

Git worktrees allow you to check out multiple branches from the same repository at once, each in its own directory. Instead of switching branches and stashing changes, you work in separate directories that all share the same Git history.

## How Zenflow Uses Worktrees

When you create a task in Zenflow:

1. **A new worktree is created** at `.zenflow/worktrees/{task_id}`
2. **A dedicated branch** is created for that task
3. **Agents work in this isolated directory** without affecting your main workspace
4. **Changes remain completely separate** until you merge

This enables true parallel execution—multiple agents can work simultaneously without stepping on each other's changes.

## Working with the IDE

Keep the agent and your editor aligned by following these patterns:

<Columns cols={2}>
  <Card title="Launch the right workspace" icon="code">
    * **Project ⋯ → Open in IDE** opens your usual repo checkout
    * **Task ⋯ → Open in IDE** opens that task's `.zenflow/worktrees/{task_id}` worktree
  </Card>

  <Card title="Commit manual edits" icon="badge-check">
    Zenflow auto-commits each agent step. Manual IDE changes appear as uncommitted—use the **Changes** page to **Commit** or **Discard** them.
  </Card>
</Columns>

## Worktree Lifecycle

| Event | What Happens |
| - | - |
| **Task created** | New worktree and branch created |
| **Task running** | Agent works in worktree directory |
| **Task paused** | Worktree preserved with current state |
| **Task archived** | Worktree cleaned up, branch optionally deleted |

## Best Practices

<AccordionGroup>
  <Accordion title="Keep worktrees task-scoped" icon="check">
    Each task should have exactly one worktree. Don't manually create additional worktrees inside `.zenflow/worktrees/` or you'll confuse Zenflow's orchestration.
  </Accordion>

  <Accordion title="Let Zenflow manage the lifecycle" icon="robot">
    Zenflow automatically creates worktrees when tasks start and cleans them up when tasks are archived or deleted. Manual worktree commands (`git worktree add/remove`) inside Zenflow directories can break automation.
  </Accordion>

  <Accordion title="Merge or archive promptly" icon="clock">
    Worktrees consume disk space. After merging a task's changes, archive or delete the task so Zenflow can clean up the worktree directory.
  </Accordion>

  <Accordion title="Choose source branches carefully" icon="code-branch">
    When creating a task, the "workspace" dropdown lets you choose which branch to base your work on. This determines what code your task starts with—usually `main` or `develop`.
  </Accordion>
</AccordionGroup>

## Common Issues

<Warning>
  **Don't manually edit files in `.zenflow/worktrees/` outside of Zenflow**

  Worktree directories are managed by Zenflow. Editing files directly with external editors or scripts can cause sync issues. Always use "Open in IDE" from the task menu.
</Warning>

<Warning>
  **Worktrees share refs and config**

  All worktrees share the same `.git` directory, meaning:

  * Tags and branches are visible across all worktrees
  * Git config changes affect all worktrees
  * You can't check out the same branch in multiple worktrees
</Warning>

<Warning>
  **Disk space adds up**

  Each worktree is a full copy of your repository's working files. 10 active tasks with a 500MB repo = \~5GB of disk space. Monitor `.zenflow/worktrees/` and archive completed tasks regularly.
</Warning>

## Troubleshooting

If a task workspace becomes corrupted or won't open:

1. Try archiving and recreating the task
2. Check that you have sufficient disk space
3. Verify the source branch still exists
4. Look for error messages in the task's chat telemetry

## Next Steps

<CardGroup cols={2}>
  <Card title="Tracking Changes" icon="eye" href="./tracking-changes">
    Monitor agent modifications in real-time
  </Card>

  <Card title="Tasks Overview" icon="check-square" href="./tasks-overview">
    Full guide to creating and managing tasks
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
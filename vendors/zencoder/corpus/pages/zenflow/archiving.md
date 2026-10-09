> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Archiving Tasks

> Clean up completed tasks and manage disk space in Zenflow.

## Overview

Archiving removes completed tasks from your active view and cleans up their worktree directories. This keeps your repository dashboard focused and reclaims disk space.

## When to Archive

Archive tasks when:

* Changes have been merged to the target branch
* Work was completed but not needed (exploratory tasks)
* Task was superseded by another approach
* You need to free up disk space

<Warning>
  Archiving deletes the task's worktree directory. Make sure all wanted changes are committed and pushed/merged before archiving.
</Warning>

## How to Archive

### Single Task

1. Open the task's context menu (⋯)
2. Click **Archive**
3. Confirm the action

### Bulk Archive

1. Go to **Repository → Tasks** list view
2. Select multiple completed tasks
3. Click **Archive Selected**

## What Happens When You Archive

| Component | Action |
| - | - |
| **Worktree** | Deleted from `.zenflow/worktrees/{task_id}` |
| **Branch** | Optionally deleted (configurable) |
| **Task record** | Moved to archived view |
| **Chat history** | Preserved for reference |
| **Artifacts** | Preserved in archived view |

## Viewing Archived Tasks

Archived tasks aren't gone—they're just hidden from the active view:

1. Go to **Repository → Tasks**
2. Click the **Archived** filter
3. Browse or search archived tasks

You can reference archived task history, artifacts, and chat logs at any time.

## Restoring Archived Tasks

If you need to continue work on an archived task:

1. Find the task in the archived view
2. Click **Restore**
3. Zenflow recreates the worktree from the branch

<Note>
  Restoration requires the task branch to still exist. If the branch was deleted, you'll need to create a new task.
</Note>

## Automatic Cleanup

Configure automatic archiving in repository settings:

| Setting | Description |
| - | - |
| **Auto-archive after merge** | Archive tasks when their PR is merged |
| **Archive stale tasks** | Archive tasks inactive for N days |
| **Delete branches on archive** | Remove task branches when archiving |

## Disk Space Management

Each worktree is a full copy of your repository's working files. Monitor usage:

```bash theme={"system"}
du -sh .zenflow/worktrees/*
```

Signs you need to archive:

* Disk space warnings
* Slow Git operations
* Many stale tasks in the task list

## Next Steps

<CardGroup cols={2}>
  <Card title="Tasks Overview" icon="check-square" href="./tasks-overview">
    Complete guide to task management
  </Card>

  <Card title="Git Worktrees" icon="code-branch" href="./git-worktrees">
    How task isolation works
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
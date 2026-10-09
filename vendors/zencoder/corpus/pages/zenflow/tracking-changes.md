> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tracking Changes

> Monitor, review, and manage code changes made by AI agents in Zenflow.

## Overview

Zenflow provides full visibility into every change made by AI agents. You can review modifications in real-time, approve or reject changes, and maintain complete control over what gets merged.

## Git Settings

Control how Zenflow handles commits and pushes from **Settings → Git**:

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-settings-git.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=72018b974a771f7a2d172b6519306866" alt="Zenflow Git settings showing commit mode (Automatic vs Instruct AI), auto-commit changes from agents, and auto-update remote branch toggles" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-settings-git.png" />
</div>

| Setting | Description |
| - | - |
| **Commit mode — Automatic** | Zenflow commits after each agent execution |
| **Commit mode — Instruct AI when to commit** | The agent decides when to commit based on your instructions |
| **Auto-commit changes from agents** | Automatically commit changes after coding agent executions |
| **Auto-update remote branch** | Automatically push changes to the remote branch after commits |

<Note>
  Auto-commit and auto-push only apply to tasks running in a dedicated worktree. Tasks running in the repository directory are not affected.
</Note>

## The Git Tab

Open the **Git** tab in any task's top bar to see branch information, worktree link, and change status:

<div className="mt-4 flex justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/bMWtAd_PIyPf5owd/images/zenflow/zenflow-task-git-tab.png?fit=max&auto=format&n=bMWtAd_PIyPf5owd&q=85&s=b9e9034731b46f7fc64f76b3f1512af2" alt="Zenflow task Git tab showing branch name, source branch, worktree link, and change status" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-task-git-tab.png" />
</div>

The Git tab shows:

* **Branch name** and source branch (e.g., `test-task-c95a from origin/main`)
* **Worktree link** to open the task's isolated directory
* **Change status** — files modified, added, or deleted by the agent

## The Changes View

Access the Changes view from any task to see:

* **File tree**: All modified, added, and deleted files
* **Diff view**: Line-by-line comparison of changes
* **Commit history**: Every agent turn creates a checkpoint
* **Uncommitted changes**: Manual edits you've made in the IDE

## Real-Time Monitoring

As agents work, Zenflow tracks every modification:

<Steps>
  <Step title="Agent makes changes">
    The agent modifies files in the task worktree based on the workflow and your instructions.
  </Step>

  <Step title="Verification runs">
    If configured, your verification script executes automatically (linting, tests, type checking).
  </Step>

  <Step title="Checkpoint created">
    Zenflow auto-commits the agent's changes with a descriptive message.
  </Step>

  <Step title="You review">
    Open the Changes view to see exactly what changed and why.
  </Step>
</Steps>

## Change Actions

### Commit Manual Edits

When you make changes in your IDE (using **Open in IDE**), they appear as uncommitted in Zenflow. You can:

* **Commit**: Add your changes to the task branch
* **Discard**: Revert your manual edits

<Tip>
  Committing your edits helps the agent understand the current state and build on your changes in subsequent turns.
</Tip>

### Rollback

If an agent produces unwanted changes:

1. View the commit history in the Changes panel
2. Select the checkpoint to roll back to
3. Confirm the rollback

The worktree reverts to that state, and the agent can try again with new guidance.

### Cherry-Pick

Select specific files or hunks to include while discarding others:

1. Open the diff view for a file
2. Use the checkbox or stage controls to select changes
3. Commit only what you want

## Verification Integration

The Changes view shows verification results alongside code changes:

| Status | Meaning |
| - | - |
| ✅ **Pass** | All verification checks succeeded |
| ❌ **Fail** | One or more checks failed—see details |
| ⏳ **Running** | Verification in progress |
| ⚪ **Skipped** | No verification script configured |

Failed verifications include the error output so you can guide the agent to fix issues.

## Comparing Branches

Compare your task branch against:

* **Base branch**: See all changes since the task started
* **Main**: Compare against the latest main branch
* **Another task**: Cross-reference changes between tasks

## Best Practices

<Card title="Review frequently" icon="eye" horizontal>
  Check changes after each significant agent turn, not just at the end. Early feedback prevents compounding issues.
</Card>

<Card title="Use verification scripts" icon="shield-check" horizontal>
  Automated checks catch syntax errors, type issues, and test failures immediately. Configure them in `.zenflow/settings.json`.
</Card>

<Card title="Commit your context" icon="message" horizontal>
  When you make manual edits, commit them with clear messages so the agent (and future you) understands the reasoning.
</Card>

## Next Steps

<CardGroup cols={2}>
  <Card title="Git Worktrees" icon="code-branch" href="./git-worktrees">
    How task isolation works
  </Card>

  <Card title="Repository Configuration" icon="gear" href="./project-configuration">
    Set up verification scripts
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
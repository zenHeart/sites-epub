> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflows

> Choose the right Zenflow workflow for your task — from quick auto-mode to fully custom pipelines.

## Overview

Every Zenflow task starts with picking a **workflow**. Workflows determine how the agent approaches your task — how much planning happens before coding, whether requirements are gathered first, and how verification works.

Pick a workflow when creating a task. You can change it later if the work evolves.

<img src="https://mintcdn.com/forgoodaiinc/wAfswEtqaOe9ICOy/images/zenflow/zenflow-create-task-v3.png?fit=max&auto=format&n=wAfswEtqaOe9ICOy&q=85&s=a5800baf20770af2f2dc8f72032a7fd8" alt="Zenflow task creation screen showing workflow picker and all UI elements" style={{ width:"100%", maxWidth:"800px", borderRadius:"12px" }} width="1144" height="720" data-path="images/zenflow/zenflow-create-task-v3.png" />

## Available Workflows

<CardGroup cols={3}>
  <Card title="Auto" icon="bolt" href="/zenflow/workflows/auto">
    Fastest path. The agent decides the approach based on your prompt — no manual workflow configuration needed.
  </Card>

  <Card title="Fix a Bug" icon="bug" href="/zenflow/workflows/fix-a-bug">
    Structured investigation → solution → implementation flow for regressions and defects.
  </Card>

  <Card title="Spec First" icon="file-lines" href="/zenflow/workflows/spec-first">
    Generate a technical spec before coding. Review and approve the plan before implementation begins.
  </Card>

  <Card title="Requirements First" icon="clipboard-list" href="/zenflow/workflows/requirements-first">
    Full specification-driven development — PRD, technical spec, implementation plan, and AI code review.
  </Card>

  <Card title="Multi-model" icon="layer-group" href="/zenflow/workflows/multi-model">
    Assign different models to planning, implementation, and review phases for cost-optimized quality.
  </Card>

  <Card title="Custom" icon="sliders" href="/zenflow/workflows/custom">
    Design your own workflow steps with Markdown files. Full control over phases, artifacts, and agent assignments.
  </Card>
</CardGroup>

## When to Use What

| Workflow | Best for | Planning overhead |
| - | - | - |
| **Auto** | Small tasks, quick experiments, well-understood changes | None — agent decides |
| **Fix a Bug** | Regressions, failing tests, production issues | Low — structured investigation |
| **Spec First** | Medium features where you want to review the approach first | Medium — spec before code |
| **Requirements First** | Large features, cross-team initiatives, stakeholder alignment | High — full PRD → spec → plan |
| **Multi-model** | Cost-sensitive teams, complex tasks benefiting from model diversity | Medium — configure per phase |
| **Custom** | Recurring team processes, compliance-driven workflows | Variable — you define it |

<Tip>
  Start with **Auto** for most tasks. Move to **Spec First** when the scope is unclear. Use **Requirements First** for anything that needs stakeholder sign-off before coding begins.
</Tip>

## Next Steps

<CardGroup cols={2}>
  <Card title="Tasks Overview" icon="list-check" href="/zenflow/tasks-overview">
    Create, run, and manage tasks — including how to pick a workflow during task creation
  </Card>

  <Card title="Git Worktrees" icon="code-branch" href="/zenflow/git-worktrees">
    How task isolation works with dedicated branches and worktrees
  </Card>

  <Card title="Multi-Agent Orchestration" icon="arrows-split-up-and-left" href="/zenflow/multi-agent-orchestration">
    Multi-model pipelines, agent presets, and parallel review
  </Card>

  <Card title="Repository Configuration" icon="gear" href="/zenflow/project-configuration">
    Verification scripts, setup commands, and agent presets
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
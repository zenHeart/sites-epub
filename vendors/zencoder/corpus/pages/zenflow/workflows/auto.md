> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto

> Let the agent decide the best approach — fastest path from prompt to working code.

## Overview

**Auto** is the default workflow. You describe the task and the agent determines the right approach — whether to plan first, dive straight into code, or break the work into phases. No manual configuration required.

<Tip>
  **Credit Efficiency:** Auto is the **most credit-efficient** workflow (single-pass, model-routed). Learn more in the [Workflow Credit Efficiency](/faq/pricing#workflow-credit-efficiency) reference guide.
</Tip>

## When to Use

* Small, well-understood tasks
* Quick experiments and prototypes
* Tasks where the requirements are obvious from the prompt
* When you want to ship fast without configuring a workflow

## How It Works

<Steps>
  <Step title="Describe your task">
    Provide a clear title and description. The more context you give, the better the agent scopes its approach.
  </Step>

  <Step title="Agent analyzes and plans">
    The agent reads your prompt, analyzes the codebase, and decides whether to create a plan or jump directly into implementation.
  </Step>

  <Step title="Implementation">
    The agent generates code, runs tests, and validates its output. It self-corrects on failures automatically.
  </Step>

  <Step title="Review and merge">
    Check the **Changes** tab for diffs, verify commits, and merge when ready.
  </Step>
</Steps>

## Artifacts

Auto creates minimal artifacts:

| Artifact | Description |
| - | - |
| `plan.md` | Light execution plan — may be a single step for simple tasks |

## Tips

<AccordionGroup>
  <Accordion title="Be specific in your prompt">
    Auto works best when the task is clear. Instead of "fix the auth," try "fix the JWT token refresh failing when the access token expires within 5 seconds of a request."
  </Accordion>

  <Accordion title="Switch workflows if scope grows">
    If you start with Auto and realize the task needs more structure, you can switch to Spec First or Requirements First.
  </Accordion>

  <Accordion title="Use for parallel small tasks">
    Auto is ideal for running multiple independent small tasks in parallel — each gets its own worktree and the agent handles each one autonomously.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="All Workflows" icon="list" href="/zenflow/task-types">
    Compare all available workflows
  </Card>

  <Card title="Fix a Bug" icon="bug" href="/zenflow/workflows/fix-a-bug">
    Structured workflow for debugging
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
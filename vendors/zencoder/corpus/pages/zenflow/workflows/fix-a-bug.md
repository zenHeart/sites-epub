> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fix a Bug

> Structured investigation, solution design, and implementation workflow for regressions and defects.

## Overview

**Fix a Bug** provides a structured three-phase workflow: investigate the issue, design a solution, then implement the fix. Each phase produces artifacts so you can track progress and review the approach before code changes land.

<Tip>
  **Credit Efficiency:** Fix a Bug is an **efficient** workflow (focused scope, shorter planning). Learn more in the [Workflow Credit Efficiency](/faq/pricing#workflow-credit-efficiency) reference guide.
</Tip>

## When to Use

* Regressions and failing tests
* Production incidents
* Any work focused on restoring existing behavior
* When you need to document root cause and impact

## How It Works

<Steps>
  <Step title="Investigation">
    The agent analyzes logs, stack traces, and code paths to identify the root cause. It documents findings in `investigation.md`.
  </Step>

  <Step title="Solution Design">
    Based on the investigation, the agent proposes a targeted fix covering edge cases. The approach is documented in `solution.md` for review.
  </Step>

  <Step title="Implementation">
    The agent implements the fix, runs tests, and verifies the regression is resolved. Results go into `implementation.md`.
  </Step>
</Steps>

## Artifacts

| Artifact | Description |
| - | - |
| `plan.md` | Three-step workflow: Investigation → Solution Design → Implementation |
| `investigation.md` | Summary, root cause analysis, and impact assessment |
| `solution.md` | Proposed fix, affected files, test strategy, and risks |
| `implementation.md` | Patch details and verification results |

## Tips

<AccordionGroup>
  <Accordion title="Attach error context upfront">
    Include stack traces, error screenshots, failing test output, or Sentry links in the task description. The more context the agent has during investigation, the faster it finds the root cause.
  </Accordion>

  <Accordion title="Review the investigation before proceeding">
    Pause after the investigation phase to verify the agent identified the correct root cause. This prevents wasted implementation effort on the wrong hypothesis.
  </Accordion>

  <Accordion title="Use for flaky tests too">
    The structured investigation flow works well for intermittent failures — the agent documents conditions under which the test fails and proposes stabilization strategies.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="All Workflows" icon="list" href="/zenflow/task-types">
    Compare all available workflows
  </Card>

  <Card title="Auto" icon="bolt" href="/zenflow/workflows/auto">
    Faster path for simple fixes
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
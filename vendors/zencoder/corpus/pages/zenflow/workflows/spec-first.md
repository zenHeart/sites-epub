> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Spec First

> Generate a technical specification before coding — review and approve the plan before implementation.

## Overview

**Spec First** generates a technical specification before any code is written. You review and approve the spec, then the agent implements against it. This is ideal for medium-sized features where you want to validate the approach before committing to it.

<Tip>
  **Credit Efficiency:** Spec First has a **moderate** credit cost (two-phase: spec + implementation). Learn more in the [Workflow Credit Efficiency](/faq/pricing#workflow-credit-efficiency) reference guide.
</Tip>

## When to Use

* Medium features and improvements
* Tasks where the technical approach isn't obvious
* When you want to review architecture decisions before coding
* When multiple implementation paths exist and you need to choose

## How It Works

<Steps>
  <Step title="Technical Specification">
    The agent creates a detailed technical spec (`spec.md`) covering architecture, contracts, and verification strategy.
  </Step>

  <Step title="Review the spec">
    Review `spec.md` in the task view. Provide feedback or approve. The agent refines until the spec is accepted.
  </Step>

  <Step title="Implementation Plan">
    Based on the approved spec, the agent breaks the work into ordered implementation steps in `plan.md`.
  </Step>

  <Step title="Implementation">
    The agent implements step by step, referencing the spec for guidance. Each step updates `plan.md` with progress.
  </Step>
</Steps>

## Artifacts

| Artifact | Description |
| - | - |
| `plan.md` | Workflow: Specification → Implementation Plan → Implementation |
| `spec.md` | Architecture, contracts, dependencies, and verification strategy |

## Tips

<AccordionGroup>
  <Accordion title="Provide constraints in the task description">
    Mention technology preferences, performance requirements, or architectural constraints upfront so they appear in the spec.
  </Accordion>

  <Accordion title="Use the spec as a review artifact">
    Share `spec.md` with teammates before approving. It's a lightweight design doc that captures the agent's proposed approach.
  </Accordion>

  <Accordion title="Enable Auto-start for hands-off execution">
    After approving the spec, enable **Auto-start steps** so the agent moves through implementation without manual triggers.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="All Workflows" icon="list" href="/zenflow/task-types">
    Compare all available workflows
  </Card>

  <Card title="Requirements First" icon="clipboard-list" href="/zenflow/workflows/requirements-first">
    Full SDD with PRD and stakeholder alignment
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Requirements First

> Full specification-driven development — PRD, technical spec, implementation plan, and AI code review.

## Overview

**Requirements First** is the most comprehensive workflow. It starts by gathering requirements and generating a Product Requirements Document (PRD), then moves through a technical specification, implementation plan, and staged implementation with AI code review. Designed for larger efforts where stakeholder alignment matters.

<Tip>
  **Credit Efficiency:** Requirements First has a **higher** credit cost (full PRD + spec + implementation + review). Learn more in the [Workflow Credit Efficiency](/faq/pricing#workflow-credit-efficiency) reference guide.
</Tip>

## When to Use

* Large features spanning multiple files or services
* Cross-team initiatives needing stakeholder alignment
* Work requiring formal documentation (PRD, spec)
* Regulated environments where traceability is important
* When you want AI code review at every stage

## How It Works

<Steps>
  <Step title="Requirements Gathering">
    The agent creates a PRD (`requirements.md`) based on your task description. This captures scope, user stories, acceptance criteria, and constraints.
  </Step>

  <Step title="Technical Specification">
    Based on the approved requirements, the agent produces a detailed technical spec (`spec.md`) covering architecture, dependencies, and verification strategy.
  </Step>

  <Step title="Implementation Plan">
    The agent breaks the spec into ordered implementation steps in `plan.md`, each representing a coherent, testable milestone.
  </Step>

  <Step title="Staged Implementation">
    The agent implements step by step. AI verifier agents run after each stage — executing tests, lint, and spec validation to catch issues before they compound.
  </Step>
</Steps>

## Artifacts

| Artifact | Description |
| - | - |
| `requirements.md` | Product Requirements Document — scope, user stories, acceptance criteria |
| `spec.md` | Technical specification — architecture, dependencies, verification |
| `plan.md` | Multi-step implementation plan with checkboxes |

## AI Code Review

Requirements First includes automated verification between implementation stages:

* Verifier agents run tests, lint, and security checks after each step
* Failures are caught before code reaches the next phase
* Diffs are reviewed continuously during implementation

## Tips

<AccordionGroup>
  <Accordion title="Involve stakeholders at the requirements phase">
    Share `requirements.md` with product managers or team leads before moving to the technical spec. This is the cheapest place to catch scope issues.
  </Accordion>

  <Accordion title="Use review checkpoints">
    Disable **Auto-start** to pause between phases. Review `requirements.md`, then `spec.md`, then approve implementation. Each checkpoint reduces rework.
  </Accordion>

  <Accordion title="Combine with Multi-model for cost efficiency">
    Use a reasoning model (Opus, GPT-5.4) for requirements and spec, a fast model (Gemini Flash, Sonnet) for implementation, and a different model for review. See [Multi-model](/zenflow/workflows/multi-model).
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="All Workflows" icon="list" href="/zenflow/task-types">
    Compare all available workflows
  </Card>

  <Card title="Spec First" icon="file-lines" href="/zenflow/workflows/spec-first">
    Lighter alternative without the PRD phase
  </Card>

  <Card title="Multi-model" icon="layer-group" href="/zenflow/workflows/multi-model">
    Optimize costs with different models per phase
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
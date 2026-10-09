> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto

> Let the agent decide the best approach — fastest path from prompt to results.

## Overview

**Auto** is the default Work workflow. You describe the task and the agent determines the right approach — whether to brainstorm, research, write, or combine multiple strategies. No manual configuration required.

## When to Use

* Most tasks where the intent is clear from the prompt
* Quick one-off requests across any department
* When you're unsure which workflow fits best
* Tasks that combine multiple activities (e.g., research + write)

## How It Works

<Steps>
  <Step title="Describe your task">
    Provide a clear description of what you want done. Reference specific integrations, data sources, or expected outputs.
  </Step>

  <Step title="Agent analyzes and routes">
    The agent reads your prompt and decides whether to brainstorm, research, write, or combine approaches.
  </Step>

  <Step title="Execution">
    The agent works through the task, pulling from connected integrations and producing the requested output.
  </Step>

  <Step title="Review">
    Check the output in the task view. Iterate with follow-up messages if needed.
  </Step>
</Steps>

## Examples

| Prompt | What the agent does |
| - | - |
| "Summarize last week's Slack activity in #product" | Pulls Slack messages, synthesizes key threads, produces a summary |
| "Draft a follow-up email to the leads from yesterday's demo" | Pulls HubSpot contact data, drafts personalized emails |
| "What are our top 5 competitors doing differently on pricing?" | Researches competitor sites, produces a comparison table |

## Tips

<AccordionGroup>
  <Accordion title="Be specific about outputs">
    Instead of "help with marketing," say "create a one-page brief comparing our Q2 campaign performance to Q1, pulling data from HubSpot."
  </Accordion>

  <Accordion title="Reference integrations explicitly">
    Mention which tools the agent should pull from: "Check Notion for the product roadmap and Slack #engineering for blockers."
  </Accordion>

  <Accordion title="Switch workflows if scope grows">
    If Auto's output is too surface-level, try **Deep Brainstorm** for analysis or **Research** for structured data gathering.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="All Work Workflows" icon="list" href="/zenflow-work">
    Compare all available Work workflows
  </Card>

  <Card title="Brainstorm" icon="lightbulb" href="/zenflow-work/workflows/brainstorm">
    Structured ideation workflow
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
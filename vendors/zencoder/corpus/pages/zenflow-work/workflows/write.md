> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Write

> Drafts, reports, emails, documentation, and other polished written content.

## Overview

**Write** is optimized for content creation. The agent produces polished written output — emails, reports, blog posts, documentation, proposals, and other deliverables — using context from your prompt and connected integrations.

## When to Use

* Drafting emails, follow-ups, or outreach sequences
* Writing reports, briefs, or internal memos
* Creating blog posts, documentation, or marketing copy
* Generating proposals, job descriptions, or process documentation

## How It Works

<Steps>
  <Step title="Describe what to write">
    Specify the content type, audience, tone, length, and any source material the agent should reference.
  </Step>

  <Step title="Agent drafts">
    The agent produces a complete first draft, pulling context from connected integrations when referenced.
  </Step>

  <Step title="Iterate and refine">
    Ask for revisions — adjust tone, expand sections, shorten, or restructure. The agent maintains context across iterations.
  </Step>
</Steps>

## Examples

| Prompt | What the agent produces |
| - | - |
| "Write a follow-up email to prospects who attended yesterday's webinar. Pull attendee list from HubSpot." | Personalized email draft with attendee context |
| "Draft a weekly engineering update for leadership. Check Slack #engineering and Linear for this week's activity." | Executive summary with shipped items, blockers, and next steps |
| "Write a job description for a Senior Backend Engineer. We use Go, PostgreSQL, and Kubernetes." | Complete JD with responsibilities, requirements, and company-specific tech stack |

## Tips

<AccordionGroup>
  <Accordion title="Specify tone and audience">
    "Write in a casual, developer-friendly tone for our engineering blog" produces very different output than "write a formal executive brief for the board."
  </Accordion>

  <Accordion title="Provide examples of what good looks like">
    If you have a past email or report you liked, paste it as context: "Write in a similar style to this example."
  </Accordion>

  <Accordion title="Use Research first for data-heavy content">
    For reports that need facts and figures, run a **Research** task first, then use **Write** to turn the findings into a polished deliverable.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Research" icon="magnifying-glass" href="/zenflow-work/workflows/research">
    Gather data before writing
  </Card>

  <Card title="All Work Workflows" icon="list" href="/zenflow-work">
    Compare all available Work workflows
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
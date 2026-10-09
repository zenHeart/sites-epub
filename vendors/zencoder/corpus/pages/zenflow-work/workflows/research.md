> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Research

> Web research, competitive analysis, and structured data gathering with sourced outputs.

## Overview

**Research** is built for tasks that require gathering, analyzing, and synthesizing information from multiple sources. The agent searches the web, pulls data from connected integrations, and produces structured research reports with citations.

## When to Use

* Competitive analysis and market research
* Gathering data to support a business case or proposal
* Tracking industry trends or technology developments
* Pulling structured data from connected tools for analysis

## How It Works

<Steps>
  <Step title="Define your research question">
    Be specific about what you want to learn, which sources matter, and what format the output should take.
  </Step>

  <Step title="Agent gathers information">
    The agent searches the web, queries connected integrations (HubSpot, Notion, Google Drive, etc.), and collects relevant data.
  </Step>

  <Step title="Analysis and synthesis">
    Raw data is organized into a structured report with key findings, comparisons, and takeaways.
  </Step>

  <Step title="Iterate">
    Ask follow-up questions, request deeper analysis on specific findings, or ask the agent to compare against additional competitors.
  </Step>
</Steps>

## Examples

| Prompt | What the agent produces |
| - | - |
| "Research the top 5 competitors to our product and compare their pricing" | Comparison table with pricing tiers, feature differences, and positioning analysis |
| "What are the latest trends in AI-assisted code review? Focus on enterprise adoption." | Trend report with data points, key players, adoption metrics, and source links |
| "Pull all deals closed this quarter from HubSpot and summarize by region" | Regional breakdown with deal count, revenue, and top accounts |

## Tips

<AccordionGroup>
  <Accordion title="Specify your sources">
    "Research competitor pricing using their public websites and G2 reviews" gives better results than "research competitors."
  </Accordion>

  <Accordion title="Request specific formats">
    Ask for "a comparison table," "a bullet-point summary," or "a one-page brief" to get output in the format you need.
  </Accordion>

  <Accordion title="Combine with Write for polished output">
    Use Research to gather data, then start a new task with the **Write** workflow to turn findings into a polished deliverable.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Write" icon="pen-nib" href="/zenflow-work/workflows/write">
    Turn research findings into polished content
  </Card>

  <Card title="All Work Workflows" icon="list" href="/zenflow-work">
    Compare all available Work workflows
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
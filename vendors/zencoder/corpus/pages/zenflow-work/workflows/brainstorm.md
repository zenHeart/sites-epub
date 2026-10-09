> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Brainstorm

> Generate ideas, explore options, and think through problems with structured ideation.

## Overview

**Brainstorm** is designed for ideation tasks. The agent generates ideas, explores multiple angles, and organizes its thinking into structured outputs — idea lists, pros/cons tables, option matrices, or prioritized recommendations.

## When to Use

* Exploring new feature ideas or product directions
* Generating content topics, campaign concepts, or naming options
* Thinking through trade-offs before making a decision
* Quick idea generation sessions that don't need deep research

## How It Works

<Steps>
  <Step title="Frame the problem">
    Describe what you're brainstorming about. Include constraints, goals, and any context the agent should consider.
  </Step>

  <Step title="Agent generates ideas">
    The agent produces a structured set of ideas, often organized by category, feasibility, or priority.
  </Step>

  <Step title="Iterate">
    Ask the agent to expand on specific ideas, combine options, or filter based on new criteria.
  </Step>
</Steps>

## Examples

| Prompt | What the agent produces |
| - | - |
| "Brainstorm 10 blog post ideas for our developer tools product" | Categorized list with titles, angles, and target audience |
| "What are creative ways to reduce churn for our Pro plan?" | Options matrix with effort vs. impact scoring |
| "Name ideas for our new analytics dashboard feature" | 15+ name options organized by style (descriptive, abstract, playful) |

## Tips

<AccordionGroup>
  <Accordion title="Set constraints to get better ideas">
    "Brainstorm ideas for a launch campaign — budget under \$5K, timeline 2 weeks, target: enterprise CTOs" produces more actionable results than an open-ended ask.
  </Accordion>

  <Accordion title="Use follow-ups to dig deeper">
    After the initial brainstorm, say "expand on ideas 3 and 7" or "combine the best parts of options A and C."
  </Accordion>

  <Accordion title="Use Deep Brainstorm for complex problems">
    If the problem has multiple dimensions or needs research backing, switch to **Deep Brainstorm** for a more thorough exploration.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Deep Brainstorm" icon="brain" href="/zenflow-work/workflows/deep-brainstorm">
    Extended multi-step brainstorming for complex problems
  </Card>

  <Card title="All Work Workflows" icon="list" href="/zenflow-work">
    Compare all available Work workflows
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
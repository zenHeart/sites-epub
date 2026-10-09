> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Brainstorm

> Extended multi-step brainstorming with deeper exploration, analysis, and structured reasoning.

<Note>
  Deep Brainstorm is currently in **beta**. Behavior and output format may evolve.
</Note>

## Overview

**Deep Brainstorm** extends the standard Brainstorm workflow with multi-step exploration. The agent doesn't just list ideas — it researches context, analyzes trade-offs, explores second-order effects, and produces a detailed exploration document with reasoning behind each recommendation.

## When to Use

* Complex strategic decisions with multiple stakeholders
* Problems with non-obvious trade-offs or dependencies
* Planning that needs both creative thinking and analytical depth
* Situations where you need to present options with supporting evidence

## How It Works

<Steps>
  <Step title="Define the problem space">
    Describe the challenge, constraints, and what a good outcome looks like. The more context you provide, the deeper the agent explores.
  </Step>

  <Step title="Agent explores multiple angles">
    The agent breaks the problem into dimensions, researches each one, and identifies patterns, risks, and opportunities.
  </Step>

  <Step title="Structured analysis">
    Results are organized into sections: problem framing, options explored, trade-off analysis, and prioritized recommendations.
  </Step>

  <Step title="Iterate on findings">
    Drill into specific areas, ask for alternative framings, or request the agent to stress-test a particular option.
  </Step>
</Steps>

## Examples

| Prompt | What the agent produces |
| - | - |
| "Should we build or buy a billing system? We're a 50-person SaaS company." | Multi-section analysis covering cost, time-to-market, flexibility, maintenance burden, and vendor comparison |
| "Explore pricing model options for our API product launching in Q3" | Usage-based vs. tiered vs. seat-based comparison with revenue projections, competitive positioning, and migration risks |
| "How should we restructure our engineering org from 20 to 50 people?" | Org design options, reporting structures, communication overhead analysis, and phased rollout plan |

## Output Structure

A typical Deep Brainstorm output includes:

| Section | Content |
| - | - |
| **Problem Framing** | Restated problem with identified constraints and assumptions |
| **Dimensions Explored** | Key angles the agent analyzed (cost, speed, risk, etc.) |
| **Options** | 3-5 distinct approaches with detailed pros/cons |
| **Trade-off Matrix** | Side-by-side comparison across evaluation criteria |
| **Recommendation** | Prioritized suggestion with reasoning and caveats |

## Tips

<AccordionGroup>
  <Accordion title="Provide context generously">
    Share company stage, team size, budget, timeline, and past decisions. The agent uses all of it to produce relevant analysis.
  </Accordion>

  <Accordion title="Ask for counter-arguments">
    After the initial analysis, ask "what's the strongest argument against your top recommendation?" to stress-test the thinking.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Brainstorm" icon="lightbulb" href="/zenflow-work/workflows/brainstorm">
    Quick ideation for simpler problems
  </Card>

  <Card title="Research" icon="magnifying-glass" href="/zenflow-work/workflows/research">
    Data-focused research and analysis
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
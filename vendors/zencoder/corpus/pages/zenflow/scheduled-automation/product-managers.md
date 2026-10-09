> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Managers

> Put product health, revenue impact, and funnel tracking on autopilot with the Product Manager Dashboard automation.

## Overview

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/hveHEDZnPLPC_PCy/images/scheduled-automation/product-manager-dashboard-live.png?fit=max&auto=format&n=hveHEDZnPLPC_PCy&q=85&s=09ad4dfb7899229e9744db5489a94165" alt="Product Manager Dashboard with key metrics and customer context charts" width="3024" height="1734" data-path="images/scheduled-automation/product-manager-dashboard-live.png" />
</Frame>

The **Product Manager Dashboard** automation helps product leaders stay on top of product health, customer feedback, and sentiment trends without manual status compilation. This scheduled automation pulls real-time data from your product and tracking systems (such as Linear, HubSpot, Stripe, Amplitude, and Sentry) to generate a comprehensive daily or weekly report of epic completions, ranked feedback themes, and customer sentiment distribution.

With this automation active, Zenflow automatically spawns a background agent task every morning to query product metrics, compile team-wide progress, and publish a live-rendered HTML dashboard directly in your workspace.

***

## How It Works

This workspace automation executes according to your configured schedule (typically every weekday morning or weekly) and follows a structured execution pipeline:

<Steps>
  <Step title="Spawn Scheduled Task">
    At the configured execution time, Zenflow launches a standalone task titled `Run Product Manager Dashboard` using the **Auto** workflow.
  </Step>

  <Step title="Locate and Verify Skill">
    The agent searches for the globally installed `product-manager` skill across standard agent execution paths on the host machine.
  </Step>

  <Step title="Automatic Installation">
    If the skill is not found, the agent automatically installs it globally using the Zencoder package registry, ensuring zero-configuration execution.
  </Step>

  <Step title="Compile Metrics & Generate Dashboard">
    The agent reads the loaded skill specification, executes the underlying product metrics, roadmap prioritization, and Jira/Linear/HubSpot queries, and compiles the live dashboard report.
  </Step>
</Steps>

***

## How to Install & Configure

Setting up the Product Manager Dashboard is straightforward. You can configure it from scratch or initialize it using the pre-built template in Zenflow.

### Quick Start with Templates

1. Open **Zenflow** and click the **thunderbolt icon** in the left sidebar to navigate to the **Automations** view.
2. Scroll to the **Templates** section at the bottom of the page and click the **Product** tab.

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/hveHEDZnPLPC_PCy/images/scheduled-automation/product-templates-tab.png?fit=max&auto=format&n=hveHEDZnPLPC_PCy&q=85&s=16eeca65df05b41edefc0cd5bc3b2a1b" alt="Product Templates Category Tab" width="1566" height="774" data-path="images/scheduled-automation/product-templates-tab.png" />
</Frame>

3. Locate the **Product Manager Dashboard** card.

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/hveHEDZnPLPC_PCy/images/scheduled-automation/product-manager-template-card.png?fit=max&auto=format&n=hveHEDZnPLPC_PCy&q=85&s=49e7d47b920de106aafa10caee5d5636" alt="Product Manager Dashboard Template Card" width="1564" height="712" data-path="images/scheduled-automation/product-manager-template-card.png" />
</Frame>

4. Click **Use template**.
5. Customize the schedule, target workspace, and execution settings in the modal dialog, and click **Create**.

### Custom Installation Details

When creating or modifying the automation, the underlying execution flow is configured as follows:

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/hveHEDZnPLPC_PCy/images/scheduled-automation/create-product-manager-automation.png?fit=max&auto=format&n=hveHEDZnPLPC_PCy&q=85&s=86a319fd21ec21cadc5ac0b7d95a9fe7" alt="Create Product Manager Automation dialog" width="1240" height="1616" data-path="images/scheduled-automation/create-product-manager-automation.png" />
</Frame>

When the automation executes, the agent follows these explicit technical instructions:

<AccordionGroup>
  <Accordion title="1. Skill Path Verification">
    The agent checks for a globally installed skill by verifying the following local paths in order:

    * `~/.agents/skills/product-manager/SKILL.md`
    * `~/.zencoder/skills/product-manager/SKILL.md`
    * `~/.codex/skills/product-manager/SKILL.md`
    * `~/.claude/skills/product-manager/SKILL.md`
    * `~/.gemini/skills/product-manager/SKILL.md`
  </Accordion>

  <Accordion title="2. Missing Skill Installation">
    If the skill is not present in any of the checked paths, the agent automatically triggers a global installation:

    ```bash theme={"system"}
    npx skills add zencoderai/skill-product-manager -g -y
    ```

    Once the command completes, the agent re-scans the directories to locate the newly installed `SKILL.md` file.
  </Accordion>

  <Accordion title="3. Load Skill Specification">
    The agent reads and parses the `SKILL.md` file from the identified path to initialize the specialized prompts, workflows, and execution context.
  </Accordion>

  <Accordion title="4. Execute Dashboard Flow">
    The agent executes the dashboard generation sequence outlined in the skill, compiling:

    * **Weekly Product Health**: Tracking epic completion rates, active epics aligned with objectives, and shipping velocity trends
    * **Customer Feedback Synthesizer**: Aggregating and prioritizing key customer-tier themes and sentiments (positive, neutral, negative)
    * **Ranked Feedback Themes**: Organizing customer feedback by volume, priority score, and customer segments (Enterprise, Mid-Market, SMB)
    * **Contextual Quotes**: Surfacing specific key customer quotes directly alongside categorized feedback themes for actionable engineering insights
  </Accordion>
</AccordionGroup>

***

## Recommended Configuration

For the best results, we recommend setting up the automation with the following default parameters:

| Configuration Field | Recommended Setting |
| :- | :- |
| **Schedule** | Weekdays (**Mon, Tue, Wed, Thu, Fri**) at `08:00 am` |
| **Task Name** | `Run Product Manager Dashboard` |
| **Repository** | `No repository` (Runs standalone to aggregate multiple external platforms) |
| **Using Workflow** | `Auto` |
| **Agent Model** | `Zencoder Default` |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Engineering Managers

> Put team metrics, PR health, and sprint pulse tracking on autopilot with the Engineering Manager Dashboard automation.

## Overview

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/iGMY_bU51DQRwCjn/images/scheduled-automation/engineering-manager-dashboard-live.png?fit=max&auto=format&n=iGMY_bU51DQRwCjn&q=85&s=7ea7c072ac6bd2053923a933683a1d1d" alt="Engineering Manager Dashboard with PR Cycle Time, Investment Allocation, and Sprint Velocity charts" width="1107" height="760" data-path="images/scheduled-automation/engineering-manager-dashboard-live.png" />
</Frame>

The **Engineering Manager Dashboard** automation helps engineering leaders stay on top of team progress without manual manual status compilation. This scheduled automation pulls real-time data from your development and tracking systems (such as GitHub, Linear, Jira, and Sentry) to generate a comprehensive daily report of sprint health, PR cycles, and production stability.

With this automation active, Zenflow automatically spawns a background agent task every morning to query engineering metrics, compile team-wide progress, and publish a live-rendered HTML dashboard directly in your workspace.

***

## How It Works

This workspace automation executes according to your configured schedule (typically every weekday morning) and follows a structured execution pipeline:

<Steps>
  <Step title="Spawn Scheduled Task">
    At the configured execution time, Zenflow launches a standalone task titled `Run Engineering Manager Dashboard` using the **Auto** workflow.
  </Step>

  <Step title="Locate and Verify Skill">
    The agent searches for the globally installed `engineering-manager` skill across standard agent execution paths on the host machine.
  </Step>

  <Step title="Automatic Installation">
    If the skill is not found, the agent automatically installs it globally using the Zencoder package registry, ensuring zero-configuration execution.
  </Step>

  <Step title="Compile Metrics & Generate Dashboard">
    The agent reads the loaded skill specification, executes the underlying DORA metrics, sprint pulse, and Jira/Linear queries, and compiles the live dashboard report.
  </Step>
</Steps>

***

## How to Install & Configure

Setting up the Engineering Manager Dashboard is straightforward. You can configure it from scratch or initialize it using the pre-built template in Zenflow.

### Quick Start with Templates

1. Open **Zenflow** and click the **thunderbolt icon** in the left sidebar to navigate to the **Automations** view.
2. Scroll to the **Templates** section at the bottom of the page and click the **Engineering** tab.

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/iGMY_bU51DQRwCjn/images/scheduled-automation/engineering-templates-tab.png?fit=max&auto=format&n=iGMY_bU51DQRwCjn&q=85&s=e45687beeaea481c6d6bc82e50301b45" alt="Engineering Templates Category Tab" width="1652" height="844" data-path="images/scheduled-automation/engineering-templates-tab.png" />
</Frame>

3. Locate the **Engineering Manager Dashboard** card.

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/iGMY_bU51DQRwCjn/images/scheduled-automation/engineering-manager-template-card.png?fit=max&auto=format&n=iGMY_bU51DQRwCjn&q=85&s=6c983c9d8c2a5782ed2a107156a8d66f" alt="Engineering Manager Dashboard Template Card" width="1596" height="764" data-path="images/scheduled-automation/engineering-manager-template-card.png" />
</Frame>

4. Click **Use template**.
5. Customize the schedule, target workspace, and execution settings in the modal dialog, and click **Create**.

### Custom Installation Details

When creating or modifying the automation, the underlying execution flow is configured as follows:

<Frame>
  <img src="https://mintcdn.com/forgoodaiinc/iGMY_bU51DQRwCjn/images/scheduled-automation/create-engineering-manager-automation.png?fit=max&auto=format&n=iGMY_bU51DQRwCjn&q=85&s=0149b07579e2963f0212d0013ad5ace2" alt="Create Engineering Manager Automation dialog" width="1234" height="1672" data-path="images/scheduled-automation/create-engineering-manager-automation.png" />
</Frame>

When the automation executes, the agent follows these explicit technical instructions:

<AccordionGroup>
  <Accordion title="1. Skill Path Verification">
    The agent checks for a globally installed skill by verifying the following local paths in order:

    * `~/.agents/skills/engineering-manager/SKILL.md`
    * `~/.zencoder/skills/engineering-manager/SKILL.md`
    * `~/.codex/skills/engineering-manager/SKILL.md`
    * `~/.claude/skills/engineering-manager/SKILL.md`
    * `~/.gemini/skills/engineering-manager/SKILL.md`
  </Accordion>

  <Accordion title="2. Missing Skill Installation">
    If the skill is not present in any of the checked paths, the agent automatically triggers a global installation:

    ```bash theme={"system"}
    npx skills add zencoderai/skill-engineering-manager -g -y
    ```

    Once the command completes, the agent re-scans the directories to locate the newly installed `SKILL.md` file.
  </Accordion>

  <Accordion title="3. Load Skill Specification">
    The agent reads and parses the `SKILL.md` file from the identified path to initialize the specialized prompts, workflows, and execution context.
  </Accordion>

  <Accordion title="4. Execute Dashboard Flow">
    The agent executes the dashboard generation sequence outlined in the skill, compiling:

    * **PR Health**: Analysis of open pull requests, review cycle times, and staleness
    * **Sprint Pulse**: Updates on active sprint progress from Linear or Jira
    * **DORA Metrics**: Investment allocation and deployment frequency
    * **Sentry Alerts**: Unresolved critical production exceptions
  </Accordion>
</AccordionGroup>

***

## Recommended Configuration

For the best results, we recommend setting up the automation with the following default parameters:

| Configuration Field | Recommended Setting |
| :- | :- |
| **Schedule** | Weekdays (**Mon, Tue, Wed, Thu, Fri**) at `08:00 am` |
| **Task Name** | `Run Engineering Manager Dashboard` |
| **Repository** | `No repository` (Runs standalone to aggregate multiple external platforms) |
| **Using Workflow** | `Auto` |
| **Agent Model** | `Zencoder Default` |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Linear Integration

> Connect Zenflow to Linear for issue tracking and task synchronization.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

Zenflow integrates with Linear to sync tasks and issues between both platforms. Create Zenflow tasks from Linear issues, push status updates back, and keep your project management in sync with AI-driven development work.

## Connecting to Linear

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Find Linear">
    Locate **Linear** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the Linear card.
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zenflow to access your Linear workspace via the secure OAuth popup window:
    Click **Authorize**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/linear/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=c1693582cce440877875089f0f8ee8d1" alt="linear authorization screen" width="1273" height="1258" data-path="images/integrations/linear/authorization-screen.png" />

    You should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/linear/open-zenflow-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=57d36532bbd101fb795c48722baa57b6" alt="open zenflow modal" width="1148" height="1054" data-path="images/integrations/linear/open-zenflow-screen.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/linear/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=79504aa1d6fbab9b21d8c0ec69c14ed7" alt="linear integration connected" width="1712" height="192" data-path="images/integrations/linear/connected-integration-zenflow.png" />
  </Step>
</Steps>

## Features

### Create Tasks from Linear Issues

Pull Linear issues directly into Zenflow as tasks:

1. Open the task creation dialog
2. Select **Import from Linear**
3. Choose the issue to work on
4. Zenflow creates a task with the issue context pre-filled

### Status Sync

Zenflow syncs task status back to Linear:

| Zenflow Status | Linear Status |
| - | - |
| Running | In Progress |
| Review | In Review |
| Completed | Done |

### Branch and PR Linking

When a task creates a branch or PR, Zenflow attaches the link to the corresponding Linear issue for traceability.

## Next Steps

<CardGroup cols={2}>
  <Card title="GitHub Integration" icon="github" iconType="brands" href="/zenflow/integrations/github">
    Connect to GitHub for PRs
  </Card>

  <Card title="MCPs" icon="plug" href="/zenflow/mcps">
    Add more tool integrations
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
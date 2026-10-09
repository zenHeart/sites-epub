> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Jira Integration

> Connect Zenflow to Jira for issue tracking and task synchronization.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

Zenflow integrates with Jira to sync tasks and issues between both platforms. Create Zenflow tasks from Jira tickets, push status updates back, and keep your project management in sync with AI-driven development work.

## Connecting to Jira

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Find Jira">
    Locate **Jira** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the Jira card.
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zenflow to access your Jira workspace via the secure OAuth popup window:
    Select the space you want to authorize the app in, click **Accept**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/jira/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=2da8aff0b7ddc5ac4c1c3bf3b0fcb570" alt="jira authorization screen" width="1244" height="1682" data-path="images/integrations/jira/authorization-screen.png" />

    You should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/jira/open-zenflow-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=c902ee7cb61ae3f30cb63293b27d2d3c" alt="open zenflow modal" width="1161" height="1049" data-path="images/integrations/jira/open-zenflow-screen.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/jira/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=36426604c0f5133db1994d9d6811219c" alt="jira integration connected" width="1727" height="208" data-path="images/integrations/jira/connected-integration-zenflow.png" />
  </Step>
</Steps>

## Features

### Create Tasks from Jira Tickets

Pull Jira issues directly into Zenflow as tasks:

1. Open the task creation dialog
2. Select **Import from Jira**
3. Choose the ticket to work on
4. Zenflow creates a task with the ticket context pre-filled

### Status Sync

Zenflow syncs task status back to Jira:

| Zenflow Status | Jira Status |
| - | - |
| Running | In Progress |
| Review | In Review |
| Completed | Done |

### Branch and PR Linking

When a task creates a branch or PR, Zenflow attaches the link to the corresponding Jira ticket for traceability.

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
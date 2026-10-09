> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# HubSpot

> Connect Zenflow to HubSpot for full CRM access — contacts, deals, tickets, campaigns, and workflows.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

The HubSpot integration gives the AI agent full CRM access. Read and update contacts, manage deals and tickets, track email campaigns, query analytics, and trigger workflows — all from within a Zenflow task.

<Note>
  HubSpot integration is based on [HubSpot MCP](https://developers.hubspot.com/mcp)
</Note>

## Connecting to HubSpot

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar (the gear icon at the bottom left).
  </Step>

  <Step title="Find HubSpot">
    Locate **HubSpot** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the HubSpot card.
  </Step>

  <Step title="Authorize the app">
    You'll be redirected first to account selection page (if you have only one account, you might not see this screen)

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/hubspot/choose-an-account-screen-exp-oauth.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=babd82c5c23c183d5b1dbc3c82291cee" alt="hubspot choose an account screen" width="1517" height="1278" data-path="images/integrations/hubspot/choose-an-account-screen-exp-oauth.png" />

    After selecting the account, you'll be redirected to scope selection screen.
    Select scopes according to what you want the agent to have access to. Tick the checkbox agreeing to third party app installation. Click **Connect app**

    <img src="https://mintcdn.com/forgoodaiinc/6hvhGDQTypO9yb1K/images/integrations/hubspot/oauth-scopes.png?fit=max&auto=format&n=6hvhGDQTypO9yb1K&q=85&s=26f519528b22da258debde538dc9ca10" alt="hubspot scopes oauth app" width="2182" height="1548" data-path="images/integrations/hubspot/oauth-scopes.png" />

    You should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/hubspot/open-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=71d6c9a72b23ad86ed7aadaf45232b6c" alt="open zenflow modal" width="1077" height="1001" data-path="images/integrations/hubspot/open-zenflow.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/hubspot/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=7730c50f51bd6872adfe38890cfe8c94" alt="hubspot integration connected" width="1691" height="178" data-path="images/integrations/hubspot/connected-integration-zenflow.png" />
  </Step>
</Steps>

## What the Agent Can Do

* **Contacts** — Read, create, and update contact records and properties
* **Deals** — Manage deal pipelines, stages, and associated data
* **Tickets** — Create and update support tickets
* **Lists** — Manage contact lists and lifecycle stages
* **Campaigns** — Access email campaign performance data and analytics
* **Properties** — Query and update custom properties
* **Workflows** — Trigger and manage HubSpot workflows

## Example Use Cases

* Generate weekly pipeline health reports from deal data
* Enrich contact records with research from web and email
* Track campaign performance and surface trends automatically
* Sync deal updates to Notion dashboards or Google Docs

## Example Automations

### Payment to Customer Lifecycle Sync

Connect HubSpot and Stripe to keep customer statuses in sync automatically:

1. **Check all new customers in Stripe**: The agent monitors Stripe for newly created customer records (requires **Read** permissions in Stripe).
2. **Sync status in HubSpot**: For any customers with an active subscription, the agent automatically searches for the corresponding contact or lead in HubSpot and updates their lifecycle stage to "Paid Customer" (requires **Write** permissions in HubSpot).

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
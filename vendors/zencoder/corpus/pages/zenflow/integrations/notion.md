> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Notion

> Connect Zenflow to Notion to read and update pages, databases, and wikis.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

The Notion integration gives the AI agent access to your Notion workspace. Read pages and databases, create new entries, update records, and build structured dashboards — enabling automated documentation, tracking, and knowledge management.

<Note>
  Notion integration is based on [Notion MCP](https://developers.notion.com/guides/mcp/mcp)
</Note>

## Connecting Notion

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Find Notion">
    Locate **Notion** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the Notion card.
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zenflow to access your Notion workspace via the secure OAuth popup window:
    Check `I recognize and trust this URL` checkbox and click **Continue**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/notion/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=4a16807473005e9173c7f461982093f5" alt="notion allow app access" width="938" height="1382" data-path="images/integrations/notion/authorization-screen.png" />

    You should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/notion/open-zenflow-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=6dea553f19063cdcc8982eb8df1b056f" alt="open zenflow modal" width="1082" height="1501" data-path="images/integrations/notion/open-zenflow-screen.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/notion/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=71e437cd654a4d61837316fae73461aa" alt="notion integration connected" width="1697" height="177" data-path="images/integrations/notion/connected-integration-zenflow.png" />
  </Step>
</Steps>

## What the Agent Can Do

* **Read** — Search and read pages, databases, and wiki entries
* **Create** — Add new pages, database entries, and structured records
* **Update** — Modify existing pages, properties, and database fields
* **Build dashboards** — Create structured trackers, tables, and status boards

## Example Use Cases

* Sync sprint progress from Linear or Jira into a Notion dashboard
* Create onboarding checklists for new hires automatically
* Archive customer quotes and testimonials from email into a Notion database
* Maintain a running competitive intel page updated weekly

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
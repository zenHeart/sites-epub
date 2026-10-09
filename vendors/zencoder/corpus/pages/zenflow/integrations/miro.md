> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Miro

> Connect Zenflow to Miro to create and update boards and visual collaboration spaces.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

The Miro integration lets the AI agent work with your visual collaboration boards. Create new boards, add content like sticky notes and shapes, and update existing workspaces — enabling automated brainstorming, planning, and visual documentation.

<Note>
  Miro integration is based on [Miro MCP](https://developers.miro.com/docs/miro-mcp)
</Note>

## Connecting Miro

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Find Miro">
    Locate **Miro** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the Miro card.
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zenflow to access your Miro workspace via the secure OAuth popup window:
    Click **Allow Access**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/miro/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=d0ebd52a3333b96646a2fe213c592dcd" alt="miro allow app access" width="868" height="774" data-path="images/integrations/miro/authorization-screen.png" />

    Select organization

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/miro/org-select-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=bf8c4513c6e3eba625c19b407b13aa04" alt="miro org selection" width="860" height="1182" data-path="images/integrations/miro/org-select-screen.png" />

    Select team

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/miro/team-select-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=3d8c2fb17070197499bd863d684e1915" alt="miro team selection" width="862" height="1357" data-path="images/integrations/miro/team-select-screen.png" />

    Click **Connect** (or **Add again** if you connected Miro previously), you should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/miro/open-zenflow-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=6dfce3201ed0c827fec077639ef299c5" alt="open zenflow modal" width="1077" height="1132" data-path="images/integrations/miro/open-zenflow-screen.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/miro/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=e6a68cf350798e5f6408e03bd63e2e97" alt="miro integration connected" width="1699" height="179" data-path="images/integrations/miro/connected-integration-zenflow.png" />
  </Step>
</Steps>

## What the Agent Can Do

* **Create boards** — Set up new Miro boards for projects, sprints, or brainstorming sessions
* **Add content** — Place sticky notes, shapes, text, and other elements on boards
* **Update boards** — Modify existing board content and layout
* **Organize** — Structure visual collaboration spaces for team workflows

## Example Use Cases

* Auto-generate sprint retrospective boards with data from Jira or Linear
* Create brainstorming boards from meeting notes
* Build visual project roadmaps from task tracker data
* Organize research findings into structured visual layouts

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sentry

> Connect Zenflow Work to Sentry to access error monitoring, incident tracking, and application health data.

<span className="set-page-badge-native" />

<Note>
  This native integration requires a Zencoder account.
</Note>

## Overview

The Sentry integration gives the AI agent access to your error monitoring and incident data. Track exceptions, monitor application health, surface recurring issues, and generate incident reports — all from within a Zenflow task.

<Note>
  Sentry integration is based on [Sentry MCP](https://docs.sentry.io/ai/mcp/)
</Note>

## Connecting Sentry

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Find Sentry">
    Locate **Sentry** in the Integrations Catalog.
  </Step>

  <Step title="Click Connect">
    Click the **Connect** or **\[+]** button on the Sentry card.
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zenflow to access your Sentry workspace via the secure OAuth popup window:
    Select desired scopes, click **Approve**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/sentry/scope-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=36c683d4c92005985322ad105af80385" alt="sentry scope screen" width="2213" height="1319" data-path="images/integrations/sentry/scope-screen.png" />

    On the next screen, verify the permissions and click **Approve**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/sentry/authorization-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=6f7fb40d1ed9d9737e67cc00427cbe42" alt="sentry scope screen" width="1425" height="998" data-path="images/integrations/sentry/authorization-screen.png" />

    You should get a modal asking if you want to open Zenflow, click **Open Zenflow**

    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/sentry/open-zenflow-screen.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=1cdfe1ad5742ed731829a96a267181ee" alt="open zenflow modal" width="1392" height="985" data-path="images/integrations/sentry/open-zenflow-screen.png" />
  </Step>

  <Step title="Integration enabled">
    <img src="https://mintcdn.com/forgoodaiinc/WZGWyEgQ7UortYL4/images/integrations/sentry/connected-integration-zenflow.png?fit=max&auto=format&n=WZGWyEgQ7UortYL4&q=85&s=be3ab2bab29cd252fd23938d36dae162" alt="sentry integration connected" width="1697" height="189" data-path="images/integrations/sentry/connected-integration-zenflow.png" />
  </Step>
</Steps>

## What the Agent Can Do

* **Monitor errors** — Access exception data, stack traces, and error frequency
* **Track incidents** — View active incidents, their status, and resolution history
* **Surface trends** — Identify recurring issues and regression patterns
* **Generate reports** — Compile error summaries and application health digests

## Example Use Cases

* Generate daily error summaries for the engineering team
* Identify top recurring exceptions for bug prioritization
* Monitor error rates after deployments and flag regressions
* Compile incident reports for post-mortems

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
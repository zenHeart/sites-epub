> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack

> Connect Zenflow to Slack to send messages, monitor channels, and automate workspace communications.

<span className="set-page-badge-extended" />

<Note>
  This extended integration requires a paid Zencoder account.
</Note>

## Overview

Zencoder is an AI teammate for Slack. Mention @zencoder in a channel, thread, or DM to plan work, manage tasks, answer questions about your projects, create automations, or start an AI coding agent on your connected repo.

Zencoder combines chat-based project management with autonomous software engineering. It can update Zenflow tasks, summarize progress, schedule recurring workflows, and when code changes are needed, launch an isolated agent that works on the repo and opens a GitHub pull request for review.

Zencoder supports multi-model workflows, choose the best model for each task, or let Zencoder decide.

## Connecting Slack

Follow these steps to connect Slack to Zenflow:

<Steps>
  <Step title="Open Settings & Integrations">
    Navigate to **Settings → Integrations** in the Zenflow sidebar.
  </Step>

  <Step title="Search for Slack">
    Locate **Slack** in the Integrations Catalog and click the **Connect** or **\[+]** button.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-card.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=e0d68679ba1e8ffa0e54e42782a36495" alt="Slack Integration Card" style={{ width: "100%", maxWidth: "500px", borderRadius: "12px" }} width="560" height="140" data-path="images/integrations/pipedream-card.png" />
    </div>
  </Step>

  <Step title="Consent to Connection">
    A secure popup window will open asking for permission to connect your account. Click **Continue** to proceed.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-consent.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=8bef370f3584515ee91bdb286c558acc" alt="Pipedream Consent Screen" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="388" height="576" data-path="images/integrations/pipedream-consent.png" />
    </div>
  </Step>

  <Step title="Authorize Connection">
    Authenticate and authorize Zencoder via the secure Slack OAuth popup window to add Zencoder to your workspace.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-oauth-provider.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=6f5647dba3c892f94e13cf0a85b6469c" alt="OAuth Authorization Screen Example" style={{ width: "100%", maxWidth: "500px", borderRadius: "12px" }} width="628" height="809" data-path="images/integrations/pipedream-oauth-provider.png" />
    </div>
  </Step>

  <Step title="Complete Setup">
    A progress window will briefly indicate that the account connection is in progress, followed by a confirmation.

    <div className="mt-4 flex justify-center">
      <img src="https://mintcdn.com/forgoodaiinc/eDU9y85HvJm-NpEc/images/integrations/pipedream-connecting.png?fit=max&auto=format&n=eDU9y85HvJm-NpEc&q=85&s=551313855862e9f99e2b409748d16a21" alt="Connection in Progress" style={{ width: "100%", maxWidth: "400px", borderRadius: "12px" }} width="388" height="576" data-path="images/integrations/pipedream-connecting.png" />
    </div>

    Once authorized, close the popup. Zencoder will instantly show as connected and is ready to use.
  </Step>

  <Step title="Start Chatting">
    DM `@zencoder` or invite it to any channel or thread to get started.
  </Step>
</Steps>

## Work with Zencoder in Slack

**Send a direct message**

Start a private conversation with @zencoder for task planning, project questions, or coding requests.

**Mention Zencoder in any thread**

Bring Zencoder into engineering discussions and ask it to summarize, plan, create tasks, or start implementation.

**Continue the conversation**

Reply in the same thread with follow-ups. Zencoder keeps the context and updates the work as it moves forward.

**Collaborate on code**

Ask @zencoder to fix bugs, add tests, refactor code, or implement features. Zencoder runs the work remotely and returns a GitHub pull request for review.

## Built for your daily workflows

<CardGroup cols={2}>
  <Card title="Kick off coding tasks" icon="code">
    Debug issues, implement changes, and open PRs directly from Slack.

    *Example:* `@zencoder fix the login bug in backend-api and open a PR`
  </Card>

  <Card title="Turn threads into tasks" icon="list-check">
    Convert product, support, marketing, content or engineering discussions into structured Zenflow tasks.

    *Example:* `@zencoder create an implementation task from this thread`
  </Card>

  <Card title="Track project progress" icon="chart-line">
    Ask what is pending, blocked, in progress, or ready for review.

    *Example:* `@zencoder summarize what is in progress this week`
  </Card>

  <Card title="Put the routine on autopilot" icon="robot">
    Create recurring workflows without leaving Slack like daily standups, weekly reporting, and checklists.

    *Example:* `@zencoder create a competitor research task for every Monday at 9am`
  </Card>

  <Card title="Work across your tools" icon="plug">
    Pull info and take action across Gmail, HubSpot, Drive, Sheets, Amplitude, LinkedIn, Zoom, and more.

    *Example:* `@zencoder pull this week's top deals from HubSpot and post a summary here`
  </Card>

  <Card title="Choose the right model" icon="brain">
    Use faster models for quick answers and stronger ones for complex work or let Zencoder pick.

    *Example:* `@zencoder use the best model for this and draft the plan`
  </Card>
</CardGroup>

## Secure, and always in your control

* Zencoder works within the Slack permissions your workspace authorizes.
* Coding tasks run in isolated environments.
* SOC 2 Type II, ISO 27001, and ISO 42001 certified. Full audit trails, zero model training on your data.
* Teams stay in control before changes are merged.

## FAQ

<AccordionGroup>
  <Accordion title="What can Zencoder do in Slack?" icon="question">
    Zencoder can manage Zenflow tasks, answer project questions, create automations, and start AI coding agents that open pull requests.
  </Accordion>

  <Accordion title="Can Zencoder write code from Slack?" icon="code">
    Yes. Ask @zencoder to fix bugs, add tests, refactor code, or implement features. Zencoder returns a GitHub PR for review.
  </Accordion>

  <Accordion title="Can I choose which model to use?" icon="microchip">
    Yes. Zencoder supports multi-model workflows. Choose a model in your prompt or let Zencoder pick one.
  </Accordion>

  <Accordion title="Can Zencoder create automations?" icon="robot">
    Yes. Zencoder can create recurring tasks, reminders, summaries, and workflow automations directly from Slack.
  </Accordion>
</AccordionGroup>

Browse ready-to-use templates in the **[Zencoder Marketplace](https://zencoder.ai/marketplace)**.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
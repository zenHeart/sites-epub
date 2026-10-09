> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# April 2026

> Zenflow 2.0 launch, cross-model workflows, integrations overhaul, automations, rich text editing, and Claude Code improvements

# April 2026 — Zenflow Updates

April was a landmark month for Zenflow. We shipped Zenflow 2.0 with a completely new task model, a full integrations overhaul, automations, cross-model workflows, and much more. Here's everything that landed.

## New Features

### Zenflow 2.0 — Code and Work Task Types

<Card title="Simplified Task Model" icon="list-check" color="#F24A07">
  A new dual-mode task system — Code tasks for development work, and Work tasks for research, writing, and general productivity.
</Card>

Zenflow 2.0 introduces a simplified UX with two focused task types:

* **Code tasks** for development workflows with full git integration
* **Work tasks** for research, writing, and non-code productivity
* **Redesigned task creation** with improved layout and UX
* **Inline rename** for tasks via the actions menu
* **Keyboard shortcuts** to start tasks and save drafts

***

### Automations

<Card title="Scheduled and Event-Driven Workflows" icon="robot" color="#10B981">
  Create automations that run on a schedule or in response to events — no manual intervention needed.
</Card>

Automations (formerly Flows) got a major upgrade:

* **In-task automations tab** with redesigned automation cards
* **Automation templates** for common workflows
* **Scheduled execution** with improved reliability
* **Confirmation cards** with auto-run support
* **Real-time UI updates** for automation notifications

***

### Cross-Model Workflows

<Card title="Multi-Model Pipelines" icon="shuffle" color="#9333EA">
  Chain different AI models together in a single task for better results.
</Card>

Run tasks through multiple models in sequence — use one model for planning and another for implementation, or get diverse perspectives on the same problem.

***

### Integrations Overhaul

<Card title="Connect Your Tools" icon="plug" color="#F59E0B">
  Native integrations with Slack, Discord, HubSpot, Google Drive, Gmail, Jira, Linear, Notion, Amplitude, Miro, and more.
</Card>

A completely rebuilt integrations system:

* **Slack integration** with thread reading, channel context, and message sending
* **Discord integration** with emoji reactions and bot support
* **HubSpot integration** now out of beta with full access
* **Google Drive and Gmail** with broader OAuth scopes
* **Pipedream integration** for connecting to hundreds of services
* **Notion integration**
* **Amplitude integration** for analytics
* **Miro integration** for whiteboard collaboration
* **Skill discovery** via `/` command in chat input
* **Integration request feedback form** for missing integrations

***

### Messenger Assistant

<Card title="Chat with Zenflow from Slack and Discord" icon="comments" color="#6366F1">
  Send tasks and get responses from Zenflow through your team's messaging platforms.
</Card>

The new Assistant feature lets you interact with Zenflow from messaging platforms:

* **Unified assistant thread** across all message sources
* **Slack and Discord bots** with configurable bot names
* **Message shortcut context** for quick task creation

***

### Rich Text Editing

<Card title="Formatted Text in Chat and Tasks" icon="text" color="#EC4899">
  Write with formatting — bold, links, lists, and more — in task creation and chat input.
</Card>

Full rich text editing support in task descriptions and chat, including proper link handling and markdown formatting.

***

### Claude Code Improvements

* **Claude Opus 4.7** support
* **Auto permission mode** for hands-free execution
* **Configurable reasoning effort** override
* **Codex support**

***

### Image Generation in UI

Agents can now generate images and see the results rendered directly in the Zenflow Desktop UI.

***

### Clone from GitHub

Start new projects by cloning directly from GitHub in the project creation dialog — no terminal needed.

***

## Improvements

### Agent and Workflow

* **File link parsing** in agent responses — clickable links to files mentioned by the agent
* **Browser console messages** available as a tool for debugging web apps

### UI and UX

* **Onboarding redesign** with animated chip panel and jobs screen
* **Active terminal count badge** in toolbar
* **Files and Browser tab count badges**
* **Task panel width stabilization**
* **Welcome screen refinements** with smaller logo and layout improvements
* **Correct PR status** (Merged/Closed) displayed in Git panel
* **Open HTML files as text** in editor with Open in Browser toolbar action

### Performance and Stability

* Fixed a crash caused by large command output overwhelming the renderer
* Reduced memory usage during long-running sessions
* Faster log streaming and storage
* Improved connection stability for real-time task updates

***

## Bug Fixes

* Fixed crash when viewing tasks with many changes
* Fixed chat input not restored on page reload
* Fixed messages starting with `/` not being sent in follow-up chat
* Fixed browser screenshots not showing in chat
* Fixed text after a pasted link being absorbed into the link
* Fixed bold text rendering when content contains tildes
* Fixed Jira and Linear import issues
* Fixed update loop between stable and beta versions
* Fixed panel resize not working when browser tab is open
* Fixed chat input layout jump when switching between chats
* Fixed resolved issues incorrectly showing in tracker search
* Fixed frozen editor when sending follow-up messages
* Fixed browser state not preserved across panel switches
* Fixed automation list readability in dark theme
* Fixed blank screen when reopening app after task deletion

***

<Accordion title="Version History">
  * **v2.1.0** (April 28, 2026)
  * **v2.0.9** (April 28, 2026)
  * **v2.0.8** (April 21, 2026)
  * **v2.0.7** (April 21, 2026)
  * **v2.0.6** (April 21, 2026)
  * **v2.0.5** (April 14, 2026)
  * **v2.0.4** (April 14, 2026)
  * **v2.0.3** (April 14, 2026)
  * **v2.0.2** (April 14, 2026)
  * **v2.0.1** (April 7, 2026)
  * **v2.0.0** (April 7, 2026)
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
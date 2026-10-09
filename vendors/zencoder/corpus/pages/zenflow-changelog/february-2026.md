> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# February 2026

> Scheduled automations, task intake from GitHub/Jira/Linear, built-in MCP server, Darcula theme, context window indicator, and major UX overhaul

# February 2026 — Zenflow Updates

February brought scheduled automations, deep integrations with GitHub, Jira, and Linear, a built-in MCP server, and a ton of polish. Here's what shipped.

## New Features

### Scheduled Automations

<Card title="Automate Recurring Tasks" icon="clock" color="#F24A07">
  Set up daily or weekly automations to run tasks on a schedule — triage bugs, sync issues, and more.
</Card>

Zenflow now supports **daily and weekly scheduled automations**. Set up recurring workflows like Jira bug triage or codebase maintenance, and Zenflow handles them without manual intervention.

***

### Task Intake: GitHub, Jira, and Linear

<Card title="Import Issues from Your Tools" icon="plug" color="#10B981">
  Browse and import issues directly from GitHub, Jira, or Linear when creating a task.
</Card>

Connect your project management tools and pull issues straight into Zenflow:

* **Search across all connected trackers** with combined results sorted by most recently updated
* **Import title, description, and images** into a new task
* Agents can triage, prioritize, and act on imported work items

***

### Built-in MCP Server

<Card title="Programmatic Access to Zenflow" icon="server" color="#9333EA">
  AI agents can now manage tasks and projects via MCP tools — Claude Code, Codex, Gemini, and Zencoder CLI all supported.
</Card>

Zenflow now includes a built-in MCP server with automation tools. Agents can create tasks, manage projects, and trigger automations programmatically.

***

### Context Window Indicator

<Card title="See How Much Context You're Using" icon="gauge" color="#F59E0B">
  A context window indicator appears after the last agent message so you know when you're running low.
</Card>

Stay informed about context usage with a visual indicator in the chat. Works with both Claude Code and Codex executors.

***

### In-App Changelog

<Card title="Stay Up to Date" icon="newspaper" color="#6366F1">
  Changelogs now appear directly inside Zenflow with a new-version indicator on the version number.
</Card>

Click the version number in the sidebar to see the full changelog. A badge appears when a new version is available.

***

### Darcula Theme

<Card title="Full Dark Theme Support" icon="moon" color="#EC4899">
  A proper dark theme with improved syntax highlighting and softer colors.
</Card>

Darcula theme is here — with full syntax highlighting support and a refined color palette.

***

### Mini-Game While Waiting

Added a **mini-game** you can play while waiting for the agent to finish. Hit the Skip button if you'd rather watch the agent work.

***

## Improvements

### New Model Support

* **Claude Opus 4.6** added as a new default model
* **Sonnet 4.6** available for Claude Code executor
* **GPT 5.3 Codex** set as default for Codex executor
* **GPT 5.2 Codex** added to available Codex models

### Task and Workflow

* **Auto workflow** is now the default — it adapts to task complexity automatically
* **Editable branch names** when creating new tasks
* **Execution mode** for tasks — choose how tasks run
* **Setup scripts run only once** at task creation
* **"Skip" button** during verification script execution
* **New tasks branch from up-to-date remote origin** by default
* **Stale tasks no longer auto-archive** by default

### UI and UX

* **All Projects UX overhaul** — collapsible project folders, pin projects for quick access, drag-to-reorder
* **Improved GitHub integration dialog** with cleaner layout
* **Open and reveal files** directly from the changes summary list
* **Chat changes summary** — see all file changes made during a conversation
* **Formatted text paste** — pasting formatted text auto-converts to markdown
* **Improved file search** with smarter ranking and faster performance
* **Action needed banner** now appears above the chat input
* **"Try again" button** when you hit your usage limit
* **Markdown preview improvements** and improved markdown rendering with syntax highlighting
* **Agent thinking timer** and better tab focus behavior
* **Clickable task title** and various UI polish
* **Increased chat input max height**
* **Improved task archiving** with undo support and async worktree cleanup

### Performance

* **Faster Codex** with WebSocket transport
* **Improved app responsiveness** across the board
* **Improved GitHub integration dialog** with better usability

***

## Bug Fixes

* Fixed **Codex hanging on "Generating"** in some modes
* Fixed **Codex "Always ask"** approval mode
* Fixed **Codex follow-up messages** failing in certain cases
* Fixed **Codex context window usage** display to match Codex CLI
* Fixed **Claude Code (AWS Bedrock)** context window usage calculation
* Fixed **auto-start running multiple steps in parallel** instead of sequentially
* Fixed **version display** showing incorrect or hardcoded values
* Fixed **rollback/reset blocked** by non-agent running processes
* Fixed **chats failing when Windows username contains spaces**
* Fixed **GitHub integration polling** stuck with Brave browser
* Fixed **Linear integration** hotfix
* Fixed **window resizing bugs** on macOS
* Fixed **drag region in settings panel** on macOS
* Fixed **upgrade plan form** dark theme rendering
* Fixed **Darcula theme syntax highlighting** rendering
* Fixed **review button visibility** for failed reviewer and mid-step states
* Fixed **follow-up messages not displayed** when reviewer agent is running
* Fixed **archive dialog layout** preventing task card overflow
* Fixed **agent preset resetting** to default when switching chat tabs
* Fixed **model dropdown extending beyond screen** without scroll
* Fixed **duplicated spinners** when reviewing multiple changes
* Fixed **approval timeout triggering prematurely**
* Fixed **re-inserting deleted images** in task descriptions
* Fixed **commit count not refreshing** automatically
* Fixed **Windows installer setup** issues
* Fixed **failed commits** due to locked git file

***

<Accordion title="Version History">
  * **0.0.92** (March 3, 2026)
  * **0.0.91** (March 3, 2026)
  * **0.0.90** (February 26, 2026)
  * **0.0.89** (February 25, 2026)
  * **0.0.88** (February 24, 2026)
  * **0.0.87** (February 23, 2026)
  * **0.0.86** (February 20, 2026)
  * **0.0.85** (February 20, 2026)
  * **0.0.84** (February 19, 2026)
  * **0.0.83** (February 18, 2026)
  * **0.0.82** (February 17, 2026)
  * **0.0.81** (February 16, 2026)
  * **0.0.80** (February 12, 2026)
  * **0.0.79** (February 12, 2026)
  * **0.0.78** (February 11, 2026)
  * **0.0.77** (February 10, 2026)
  * **0.0.76** (February 10, 2026)
  * **0.0.74** (February 6, 2026)
  * **0.0.73** (February 4, 2026)
  * **0.0.72** (February 3, 2026)
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
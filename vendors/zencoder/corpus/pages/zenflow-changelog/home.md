> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Zenflow Changelog

> Product updates for Zenflow — the desktop app for multi-agent task orchestration

<Note>
  Looking for Zencoder IDE Agent updates? Check out the [IDE Agent Changelog](/changelog/home).
</Note>

<Update label="August 2026" description="Redesigned troubleshooting surface, one-click log export, on-call automation, custom cron, and reliability improvements">
  ## Operability, End-to-End

  ### Redesigned Troubleshooting Surface

  Zenflow Desktop now has a **Troubleshooting** section reachable from Settings and the Help menu, with dedicated pages for common issues, log locations, and how to file a report.

  ### One-Click Log Export

  **Help → Export Logs** produces a zip of the last 24 hours of logs with common secret patterns redacted — ready to attach to a support ticket.

  ### On-Call Automation Template

  A new **On-Call Assistant** automation ships out of the box — connects to PagerDuty and Sentry to triage incoming alerts, summarize stack traces, and draft an initial response.

  ### Task Automations: Custom Cron

  Scheduled automations now accept **custom cron expressions** in addition to the preset intervals, unlocking finer control over when jobs run.

  ### Slack Threaded Replies

  The Slack integration can now **reply in-thread** to the message that triggered an action.

  ### Multi-Model: Reviewer Model Override

  In the **Multi-model workflow**, assign a different model specifically to the review phase without changing planning or implementation models.

  ### Performance and Reliability

  * **Log streaming latency** reduced under sustained agent activity
  * **Faster cold start** on macOS via lazy-loaded panels
  * **Lower memory usage** for long-running orchestrated tasks
  * **Auto-recovery** for stuck task executions after network drops
  * **Safer update installer** with rollback on partial failures

  ### UI and UX

  * **Copy Operation ID** action on every assistant message
  * **Task Logs tab** now supports search and severity filters
  * **Integration health indicators** in Settings show last-successful-call timestamp
  * **Compact chat density** setting for smaller screens
</Update>

<Update label="May 2026" description="Usage-based billing, auto-approve mode, window persistence, Pipedream, performance and stability">
  ## Polish, Stability, and Billing

  ### Usage-Based Billing in Zenflow

  Zenflow now supports **usage-based billing** end-to-end — onboarding skips sign-in when already authenticated, with a robust UBB API key fallback.

  ### Claude Code Auto-Approve Mode

  Run Claude Code without pausing on every action — hands-free agent execution on trusted workflows.

  ### Cross-Model Workflows Refresh

  The cross-model pipeline is now called **Multi-model**, with a new icon and an upgraded review panel for clearer multi-model results.

  ### Window State Persistence

  Zenflow Desktop now remembers **window size and position** across restarts. Keyboard shortcuts to close and re-open tabs added.

  ### Engineering Manager Dashboard Automation

  A new **Engineering Manager Dashboard** automation template ships out of the box.

  ### Pipedream Integration

  Connect to hundreds of third-party services through the new **Pipedream integration**.

  ### Productivity Tweaks

  * **Plain-text paste** (`Cmd/Ctrl+Shift+V`) in the prompt editor
  * **Reveal in Folder** action in the file editor
  * **Operation ID display** for ZenCLI
  * **File links** in agent responses are now clickable
  * **Slack skill**: thread read, channel read, message shortcut context, message send

  ### Performance and Reliability

  * **Eliminated message-sending delay** so chat feels instant
  * Fixed a crash on large command output
  * **Updates apply reliably** — fallback when the installer silently fails
  * **CLI messages like "usage limit reached"** now surface in the UI instead of being hidden
  * **Retry with the agent** on Git hook commit errors
  * **No more duplicate chats** when sending messages quickly
</Update>

<Update label="April 2026" description="Zenflow 2.0, cross-model workflows, integrations overhaul, automations, rich text editing">
  ## Zenflow 2.0

  ### Code and Work Task Types

  A new dual-mode task system — **Code tasks** for development workflows with full git integration, and **Work tasks** for research, writing, and non-code productivity. Redesigned task creation with inline rename, keyboard shortcuts, and improved layout.

  ### Automations

  Automations (formerly Flows) got a major upgrade — in-task automations tab, automation templates, scheduled execution with improved reliability, confirmation cards with auto-run support, and real-time UI updates.

  ### Cross-Model Workflows

  Chain different AI models together in a single task — use one model for planning and another for implementation, or get diverse perspectives on the same problem.

  ### Integrations Overhaul

  Native integrations with **Slack**, **Discord**, **HubSpot**, **Google Drive**, **Gmail**, **Jira**, **Linear**, **Notion**, **Amplitude**, **Miro**, and **Pipedream**. Skill discovery via `/` command. Integration request feedback form.

  ### Messenger Assistant

  Interact with Zenflow from Slack and Discord — unified assistant thread, configurable bot names, and message shortcut context for quick task creation.

  ### Rich Text Editing

  Full rich text editing in task descriptions and chat — bold, links, lists, and proper markdown formatting.

  ### Claude Code Improvements

  **Claude Opus 4.7** support, **auto permission mode**, configurable reasoning effort, and Codex support.

  ### Image Generation

  Agents can generate images and see results rendered directly in the Zenflow UI.

  ### Clone from GitHub

  Start new projects by cloning directly from GitHub in the project creation dialog.

  ### Improvements

  * File link parsing in agent responses — clickable links to files
  * Browser console messages available as a debugging tool
  * Onboarding redesign with animated chip panel
  * Active terminal count badge and tab count badges
  * Correct PR status (Merged/Closed) in Git panel

  ### Bug Fixes

  * Fixed crash when viewing tasks with many changes
  * Fixed chat input not restored on page reload
  * Fixed messages starting with `/` not being sent
  * Fixed browser screenshots not showing in chat
  * Fixed text after pasted link being absorbed into the link
  * Fixed Jira and Linear import issues
  * Fixed panel resize and browser state preservation
</Update>

<Update label="March 2026" description="Built-in browser, task flows, redesigned layout, saved prompts, Mermaid diagrams">
  ### Built-in Browser

  Preview web apps, reference UI elements, and iterate on them directly with the agent. Browser MCP tools for automation. Viewport presets for Responsive, Mobile, Tablet, Desktop, and Wide.

  ### Task Flows

  Autonomous goal-driven agents that keep working toward a goal on a schedule — shepherd a PR through review, watch CI and fix failures, keep a branch rebased.

  ### Redesigned App Layout

  New three-panel architecture — side-by-side chat and content panels with a collapsible tools panel for Steps, Changes, and Files. Improved diff viewer and file attachments with drag & drop.

  ### Saved Prompts

  Create reusable prompt shortcuts and insert them anywhere by typing `/`.

  ### Document Preview

  Preview PDF, DOCX, XLSX, CSV, and PPTX files directly in a tab. HTML files open in the built-in browser.

  ### Mermaid Diagrams

  Agents can generate and render Mermaid diagrams directly in chat — architecture, flow, and sequence diagrams.

  ### AI-Managed Commits

  Hand control of commits to the agent — it commits when it makes sense, not after every turn.

  ### Draft Pull Requests

  Create draft PRs directly from the GitHub dialog.

  ### Additional Features

  * Agents can pause and ask you questions mid-task
  * Spotlight file search with fuzzy-ranked search and file tree explorer
  * Integration discovery — agents detect missing integrations and prompt inline

  ### Improvements

  * "Keep awake" setting to prevent system sleep during tasks
  * Review agent includes code diff in prompt
  * Agents can attach open files as context
  * ZenCLI "Confirm shell commands" toggle
  * Desktop notifications when review agent finishes
  * Inline quote-to-input for agent messages
  * Spell checker in chat and task descriptions
  * GPT 5.4 support for Codex
  * Launch on startup option (macOS and Windows)

  ### Bug Fixes

  * Fixed orphan processes causing high CPU/memory usage
  * Fixed white screen and high CPU usage
  * Fixed slow task loading from redundant git fetches
  * Fixed markdown paste losing formatting
  * Fixed authentication issues related to session refresh
  * Fixed pushing changes to `.github/workflows/` files
  * Fixed mermaid diagrams in dark mode
  * Fixed agent re-running completed verification steps
  * Fixed tool approval failing in Claude Code
</Update>

<Update label="February 2026" description="Scheduled automations, task intake, built-in MCP server, Darcula theme, context window indicator">
  ### Scheduled Automations

  Daily and weekly scheduled automations for recurring workflows like Jira bug triage or codebase maintenance.

  ### Task Intake: GitHub, Jira, and Linear

  Browse and import issues directly from GitHub, Jira, or Linear. Search across all connected trackers with combined results sorted by most recently updated.

  ### Built-in MCP Server

  AI agents can manage tasks and projects via MCP tools — Claude Code, Codex, Gemini, and Zencoder CLI all supported. Extended with Automation MCPs.

  ### Context Window Indicator

  Visual indicator showing context usage after the last agent message. Works with both Claude Code and Codex executors.

  ### Darcula Theme

  Full dark theme with improved syntax highlighting and softer colors.

  ### In-App Changelog

  Changelogs appear directly inside Zenflow with a new-version indicator on the version number.

  ### Mini-Game While Waiting

  Play a mini-game while waiting for the agent to finish.

  ### Improvements

  * **Claude Opus 4.6** and **Sonnet 4.6** added as new model options
  * **GPT 5.3 Codex** set as default for Codex executor
  * Auto workflow is now the default task type
  * Editable branch names, execution mode for tasks
  * Setup scripts run only once, "Skip" button during verification
  * All Projects UX overhaul — collapsible folders, pin projects, drag-to-reorder
  * Formatted text paste auto-converts to markdown
  * Improved file search with smarter ranking
  * Faster Codex with WebSocket transport

  ### Bug Fixes

  * Fixed Codex hanging on "Generating" and "Always ask" mode
  * Fixed auto-start running multiple steps in parallel
  * Fixed rollback/reset blocked by non-agent processes
  * Fixed chats failing when Windows username contains spaces
  * Fixed GitHub integration polling stuck with Brave browser
  * Fixed Darcula theme syntax highlighting
  * Fixed review button visibility issues
  * Fixed failed commits due to locked git file
</Update>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# March 2026

> Built-in browser, task flows, redesigned layout, saved prompts, mermaid diagrams, draft PRs, and document preview

# March 2026 — Zenflow Updates

March was a huge month for Zenflow. We shipped a built-in browser, task flows, a completely redesigned app layout, saved prompts, and a lot more. Here's everything that landed.

## New Features

### Built-in Browser

<Card title="Preview and Iterate on Web Apps" icon="globe" color="#F24A07">
  Preview web apps, reference UI elements, and iterate on them directly with the agent — all without leaving Zenflow.
</Card>

The built-in browser lets you:

* **Preview web apps** running on localhost or any URL
* **Reference elements or regions** and ask the agent to make changes
* **Browser MCP tools** let agents automate interactions, capture screenshots, and control the browser programmatically
* **Viewport presets** — switch between Responsive, Mobile, Tablet, Desktop, and Wide with zoom support
* **Open in external browser** when you need the full experience

***

### Task Flows

<Card title="Autonomous Goal-Driven Agents" icon="arrows-spin" color="#10B981">
  Give the agent a goal — it keeps working toward it on a schedule until the goal is achieved.
</Card>

Task Flows are a new way to let agents work autonomously over time:

* **Shepherd a PR through review** — the agent watches for comments, addresses feedback, and pushes fixes
* **Watch CI and fix failures** — the agent monitors your pipeline and auto-fixes issues
* **Keep a branch rebased** — the agent handles merge conflicts so your branch stays up to date
* Set any **custom interval** for how often the agent checks in

***

### Redesigned App Layout

<Card title="New Three-Panel Architecture" icon="table-columns" color="#9333EA">
  Side-by-side chat and content panels with a collapsible tools panel for Steps, Changes, and Files.
</Card>

The new layout gives you:

* **Top header bar** with quick access to key actions
* **Side-by-side panels** — chat on the left, content on the right
* **Collapsible tools panel** for Steps, Changes, and Files
* **Improved diff viewer** with better colors for readability
* **File attachments** — drag & drop, paste, or pick files with click-to-preview for images

***

### Saved Prompts

<Card title="Reusable Prompt Shortcuts" icon="bookmark" color="#F59E0B">
  Create prompt shortcuts and insert them anywhere by typing `/`.
</Card>

Save your frequently used prompts and insert them in chat or task descriptions with a quick `/` command. No more retyping the same instructions.

***

### Document Preview

<Card title="Open Docs Right in Zenflow" icon="file-lines" color="#6366F1">
  Preview PDF, DOCX, XLSX, CSV, and PPTX files directly in a tab.
</Card>

* Open documents with **zoom controls and multi-sheet support**
* HTML files open automatically in the built-in browser
* Great for reviewing specs, reports, and data files alongside your code

***

### Mermaid Diagrams

<Card title="Diagrams in Chat" icon="diagram-project" color="#EC4899">
  Ask the agent to render architecture, flow, and sequence diagrams inline.
</Card>

Agents can now generate and render **Mermaid diagrams** directly in chat or markdown — perfect for visualizing architecture decisions, data flows, and sequence diagrams.

***

### AI-Managed Commits

Hand control of commits to the agent — it commits when it makes sense, not after every turn. Less noise in your git history.

***

### Draft Pull Requests

Create **draft PRs** directly from the "Create GitHub Pull Request" dialog. Ship when you're ready.

***

### Ask Tool Questions Mid-Task

Agents can now **pause and ask you questions** during a task, then continue once you answer. Questions appear inline in the chat between agent messages.

***

### Spotlight File Search

Find files fast with **fuzzy-ranked search** and a built-in **file tree explorer**. Quickly browse files across your entire project.

***

### Integration Discovery

Agents detect when an integration is missing and **prompt you to connect it inline** — no more hunting through settings.

***

## Improvements

### Agent and Workflow

* **"Keep awake" setting** — prevent system sleep while an agent task is running
* **Review agent** now includes the code diff in its prompt for higher quality reviews
* **Agents can attach open files** as context when sending messages
* **ZenCLI** now supports a "Confirm shell commands" toggle
* **Refresh button** in the file editor toolbar to reload a file from disk
* **Desktop notifications** when a review agent finishes its review
* **Inline quote-to-input** — select text in agent messages and quote it into your follow-up
* **Spell checker** and autocorrect in chat input and task descriptions
* **"Try again" button** when execution stops due to an error

### UI and UX

* **Sticky sidebar tabs** with improved grouping
* **Scroll-to-bottom button** in chat
* **Sidebar collapse chevron**
* **Cmd+, / Ctrl+,** shortcut to open Settings
* **GPT 5.4** support for Codex
* **Launch on startup** option (macOS and Windows)

***

## Bug Fixes

* Fixed **orphan processes** causing high CPU and memory usage
* Fixed **white screen and high CPU usage** in the app window
* Fixed **slow task loading** caused by redundant git fetches
* Fixed **markdown paste** losing formatting when copying agent output
* Fixed plan.md and task files failing to load after **archiving/unarchiving on Windows**
* Fixed sporadic **authentication issues** related to session refresh
* Fixed **pushing changes to `.github/workflows/`** files failing
* Fixed **browser screenshots** not showing in chat
* Fixed **mermaid diagrams in dark mode** showing unreadable text
* Fixed agent MCP tool calls requiring **unnecessary approval prompts**
* Fixed agent occasionally **re-running a completed verification step**
* Fixed app **failing to start on some Windows machines**
* Fixed **Zencoder login** and **Windows desktop builds**
* Fixed **Linear integration** authentication getting stuck
* Fixed deletion of default agent presets leaving **dangling references**
* Fixed agent **removing unpushed commits** when resolving merge conflicts
* Fixed **tool approval failing** in Claude Code

***

<Accordion title="Version History">
  * **0.0.107** (March 28, 2026)
  * **0.0.106** (March 26, 2026)
  * **0.0.105** (March 24, 2026)
  * **0.0.104** (March 19, 2026)
  * **0.0.103** (March 18, 2026)
  * **0.0.102** (March 17, 2026)
  * **0.0.101** (March 13, 2026)
  * **0.0.100** (March 13, 2026)
  * **0.0.99** (March 12, 2026)
  * **0.0.98** (March 12, 2026)
  * **0.0.97** (March 12, 2026)
  * **0.0.96** (March 11, 2026)
  * **0.0.95** (March 11, 2026)
  * **0.0.94** (March 6, 2026)
  * **0.0.93** (March 4, 2026)
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
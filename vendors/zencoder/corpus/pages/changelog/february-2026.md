> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# February 2026

> New model support, built-in skills, research agent, subagent streaming, Zenflow scheduled automation, and major UX overhauls

# February 2026 Product Updates

February 2026 delivers major new capabilities across the IDE Agents and Zenflow desktop app — including support for Gemini 3.1, GPT-5.3 Codex, and Sonnet 4.6 models, a set of built-in skills, a new research agent, real-time subagent streaming, Zenflow scheduled automation, task intake integrations, and significant UX improvements.

## IDE Agent (VS Code & JetBrains)

### New Features

#### New Model Support

<Card title="Gemini 3.1, GPT-5.3 Codex, and Sonnet 4.6" icon="microchip" color="#F24A07">
  Access the latest AI models directly from the model selector for improved code generation and reasoning.
</Card>

Three powerful new models are now available:

* **Gemini 3.1** with improved thinking defaults and adaptive effort support
* **GPT-5.3 Codex** for enhanced code generation capabilities
* **Sonnet 4.6** available in the model selector for Anthropic users

The agent can now also intelligently choose which model to use for subtasks, optimizing quality and speed automatically.

#### Built-in Skills

<Card title="Skills Available Out of the Box" icon="wand-magic-sparkles" color="#10B981">
  Zencoder now ships with pre-installed skills for common development workflows — no setup required.
</Card>

Three skills are included by default:

* **Playwright** for browser automation and web development testing
* **Code Review** for structured, thorough code review workflows
* **Skill Creator** a skill that helps you create new custom skills

Skills can be explicitly mentioned in chat via `/` and are available in the `@`-menu, giving you quick access to specialized agent behaviors.

#### Research Agent

<Card title="Dedicated Research Agent" icon="magnifying-glass" color="#9333EA">
  A new research agent helps you explore codebases, investigate issues, and gather context before making changes.
</Card>

The research agent is designed for exploration and analysis tasks:

* **Codebase investigation** understand unfamiliar code quickly
* **Issue analysis** gather context and identify root causes
* **Pre-implementation research** explore options before committing to an approach

#### Subagent Streaming

<Card title="Real-time Subagent Progress" icon="bars-staggered" color="#F59E0B">
  See subagent work in real time as tasks are broken down and delegated to specialized agents.
</Card>

When the agent delegates work to subagents, you can now see their progress in real time:

* **Live streaming output** from subagent tasks as they execute
* **Clear task delegation visibility** see which subagent is handling what
* **Proper permission handling** subagents respect tool allowlists and permissions

### Improvements

#### Chat Navigation Redesign

* **Redesigned navbar** moved "All Chats" to the left with a chevron for cleaner navigation
* **Clickable chat title** click the current chat title to quickly rename or navigate

#### Skills and Customization

* **Skills menu** shows currently configured skills for easy access and management
* **Claude Code skills symlinks** better compatibility with Claude Code skill definitions
* **AGENTS.md support** agent instructions are now resolved from AGENTS.md files at the CLI level

#### Agent and Model Improvements

* **Review with another model** switch models for a second opinion on code changes
* **Revert to this point** improvements for better change management in conversations
* **Improved model list fetching** faster and more reliable model selection
* **Adaptive thinking support** for Anthropic provider with configurable effort levels
* **MCP caching and lazy loading** faster startup times with deferred MCP server initialization

#### Performance and Stability

* **Improved CLI startup time** reduced initialization overhead
* **Migrated CLI to Bun** from Yarn workspaces for faster builds and execution
* **File path hiding** cleaner agent responses with simplified file links
* **Better Windows support** fixed process manager spawn issues on Windows

#### User Experience

* **Trial quota exhausted notifications** clear messaging when trial limits are reached
* **Allow editing attached files** modify files attached to conversations in Zenflow
* **Removed Code Lenses** cleaned up UI by removing code lens overlays

### Bug Fixes

* **Fixed "Wrapping up" hang** resolved cases where the agent would hang during the wrap-up phase
* **Fixed agent startup hangs** resolved rare cases where the agent would hang on initialization
* **Fixed incomplete tool call handling** properly cancels incomplete tool calls to prevent stuck states
* **Fixed MCP error handling** proper error handling prevents deadlocks in MCP communication
* **Fixed revert button visibility** revert button now properly shows for changed files in JetBrains chat
* **Fixed file mention icon** corrected icon display for file mentions in agent responses
* **Fixed long filename display** file search view no longer gets cropped with very long file names
* **Fixed API key inheritance** resolved unexpected billing issues from inherited API keys
* **Fixed token visibility** tokens are no longer visible in IDE logs
* **Fixed chat error on message regeneration** resolved transient errors when regenerating edited messages in JetBrains
* **Fixed critical Dependabot alerts** addressed high-severity dependency vulnerabilities
* **Fixed MCP OAuth token refresh** resolved authentication token expiration issues

***

## Zenflow Desktop App

### New Features

#### Scheduled Automation

<Card title="Automate Recurring Tasks" icon="clock" color="#F24A07">
  Set up scheduled automations to run tasks on a recurring basis — triage bugs, sync issues, and more.
</Card>

Zenflow now supports scheduled automations that run on a configurable cadence, letting you automate repetitive workflows like Jira bug triage or codebase maintenance without manual intervention.

#### Task Intake: GitHub, Jira, and Linear Integration

<Card title="Import Tasks from Your Tools" icon="plug" color="#10B981">
  Pull issues directly from GitHub, Jira, or Linear into Zenflow and let agents work on them.
</Card>

Connect your project management tools and import issues directly into Zenflow's task queue. Agents can triage, prioritize, and act on imported work items automatically.

#### Auto Workflow

<Card title="Simplified Default Workflow" icon="bolt" color="#9333EA">
  The new Auto workflow replaces Quick Change as the default, streamlining how tasks execute.
</Card>

Auto workflow is now the default task type, providing a more intuitive starting point that automatically handles planning, implementation, and verification.

#### All Projects UX Overhaul

<Card title="Redesigned Projects View" icon="grid" color="#F59E0B">
  Group by status, global archive, global terminals, sorting, and more.
</Card>

The projects view has been completely redesigned with:

* **Group by status** organize tasks by their current state
* **Global archive** access archived tasks across all projects
* **Global terminals** view all running terminals in one place
* **Improved sorting** better options for organizing your task list

#### Built-in MCP Server

Zenflow now includes a built-in MCP server, extended with Automation MCPs, enabling deeper tool integrations and programmatic access to Zenflow's capabilities.

#### In-App Changelog

Stay informed about new features and fixes without leaving the app — Zenflow now displays changelogs directly in the product.

### Improvements

#### New Model Support in Zenflow

* **Sonnet 4.6** available for Claude Code executor
* **Claude Opus 4.6** added as a default model option
* **GPT-5.3 Codex** set as default model for Codex executor
* **Responses API WebSocket transport** for improved Codex performance

#### Task and Workflow Enhancements

* **Editable branch names** customize the Git branch name when creating new tasks
* **Open files from changes summary** click to open any file directly from the changes list
* **Reveal in folder** quickly navigate to files in your system file explorer
* **Auto-load diffs** diffs load automatically when clicking files in the changes tab
* **Execution mode for tasks** choose how tasks are executed
* **Run setup scripts only once** at task creation to avoid redundant runs
* **Skip verification scripts** new "Skip" button during verification script execution
* **Use origin/main as default** for creating worktrees

#### UI and UX

* **Darcula theme support** full dark theme with improved syntax highlighting
* **Markdown preview improvements** better rendering of markdown content in chat
* **Formatted text paste** pasting formatted text into chat or task descriptions auto-converts to markdown
* **Action needed banner redesign** improved visibility when your input is required
* **Chat layout improvements** better alignment, consistency, and increased chat input height
* **Context window indicator** see how much context is being used after the last agent message
* **Improved file search** enhanced ranking and caching for faster results
* **Improved GitHub integration dialog** cleaner connection flow
* **Config preset selector improvements** better UX for managing agent presets
* **Tab restructuring** closed tabs UX improvement and better navigation
* **Chat changes summary** view a summary of all file changes made during a conversation

#### Security and Infrastructure

* **More secure token storage** improved storage mechanism for authentication tokens
* **Offloaded slow Git operations** to a separate threadpool for better responsiveness
* **LoC analytics** track lines of code metrics across tasks

### Bug Fixes

* **Fixed Codex hanging on Generating** in workspace-write mode
* **Fixed Codex "Always ask" mode** using untrusted approval policy
* **Fixed GitHub integration polling** stuck with Brave browser
* **Fixed markdown renderer visual issues** in chat
* **Fixed auto-start parallel execution** prevented multiple steps from starting simultaneously
* **Fixed rollback/reset** no longer blocked by non-agent running processes
* **Fixed Windows spaces in username** chats no longer fail when Windows user profile name contains spaces
* **Fixed context window usage display** for both Codex and Claude Code (AWS Bedrock)
* **Fixed review button visibility** for failed reviewer and mid-step states
* **Fixed Darcula theme syntax highlighting** improved code snippet rendering
* **Fixed archive dialog layout** prevented task card overflow
* **Fixed active terminals overflow** corrected layout in terminals window
* **Fixed Jira ticket search** now case-insensitive when searching by ticket number
* **Fixed usage limits display** resolved cases where limits were not shown
* **Fixed phantom localStorage entries** cleaned up stale zenflow-draft entries
* **Fixed index.lock errors** resolved "Failed to commit changes" after execution

<Accordion title="Version History">
  <Tabs>
    <Tab title="VS Code">
      - **3.36.0** (February 27, 2026)
      - **3.34.0** (February 19, 2026)
      - **3.32.0** (February 12, 2026)
      - **3.30.1** (February 8, 2026)
      - **3.30.0** (February 5, 2026)
    </Tab>

    <Tab title="JetBrains">
      * **3.15.0** (February 27, 2026)
      * **3.14.0** (February 19, 2026)
      * **3.13.0** (February 12, 2026)
      * **3.12.0** (February 5, 2026)
    </Tab>

    <Tab title="Zenflow">
      * **0.0.92** (March 3, 2026)
      * **0.0.91** (February 27, 2026)
      * **0.0.90** (February 24, 2026)
      * **0.0.89** (February 22, 2026)
      * **0.0.88** (February 21, 2026)
      * **0.0.87** (February 20, 2026)
      * **0.0.86** (February 17, 2026)
      * **0.0.85** (February 17, 2026)
      * **0.0.84** (February 17, 2026)
      * **0.0.83** (February 17, 2026)
      * **0.0.82** (February 17, 2026)
      * **0.0.81** (February 17, 2026)
      * **0.0.80** (February 10, 2026)
      * **0.0.79** (February 10, 2026)
      * **0.0.78** (February 10, 2026)
      * **0.0.77** (February 10, 2026)
      * **0.0.76** (February 10, 2026)
    </Tab>
  </Tabs>
</Accordion>

***

*Questions or feedback? Join our [Discord community](https://discord.gg/YjNYBHg8Vb) or visit our [Community Support](/get-started/community-support) page.*


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
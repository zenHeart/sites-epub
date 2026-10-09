> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IDE Agent Changelog

> Product updates for Zencoder IDE Agents (VS Code & JetBrains)

<Note>
  Looking for Zenflow Desktop updates? Check out the [Zenflow Changelog](/zenflow-changelog/home).
</Note>

<Update label="August 2026" description="Structured logs panel, MCP tool audit trail, expanded reasoning-effort support, and stability fixes across VS Code and JetBrains">
  ## Better Debuggability, Broader Model Reach

  ### Structured Logs Panel

  A new **structured logs panel** surfaces agent execution logs — tool calls, model responses, and errors — filtered by task. Copy the whole trace with a single Operation ID so support can reproduce your session end-to-end.

  ### MCP Tool Audit Trail

  Every MCP tool call the agent makes is now logged with **inputs, outputs, and duration**, visible in the new logs panel.

  ### Expanded Reasoning-Effort Support

  Reasoning-effort selection (introduced in July) now works with additional models, including **Claude Sonnet 5 and GPT-5.6**, giving you finer control over depth-vs-speed across more of your workflow.

  ### Zencoder Agent CLI Update

  The bundled `zencli` build now includes the July/August model updates and a faster startup path — cold starts are noticeably quicker on JetBrains.

  ### Improvements

  * **Copy Operation ID** available directly from any assistant message
  * **Debug logging toggle** exposed in plugin settings
  * **JetBrains log viewer** — Zencoder logs stream into the IDE's Log tool window
  * **Faster indexing** for large monorepos on first open
  * **Reduced memory footprint** during long chat sessions

  ### Bug Fixes

  * Fixed **duplicate messages** when sending rapidly on VS Code
  * Fixed **OAuth reconnect** loop behind cookie-stripping proxies
  * Fixed **MCP tool timeouts** not surfacing in the UI
  * Fixed **rare crash** when pasting extremely large files into chat
  * Fixed **JetBrains gutter icon** not clearing after task completion
</Update>

<Update label="July 2026" description="Reasoning effort selection, Claude Fable 5 and Sonnet 5 in Claude Code, GPT-5.6 in OpenAI Codex">
  ## New Models and Finer-Grained Reasoning Control

  ### Choose Reasoning Effort for Supported Models

  Select the **reasoning effort level** for supported models, letting you balance response depth against speed depending on the task at hand.

  ### Claude Fable 5 and Sonnet 5 in Claude Code

  **Claude Fable 5** and **Sonnet 5** are now available in Claude Code, bringing Anthropic's latest models to your CLI workflows.

  ### GPT-5.6 in OpenAI Codex

  **GPT-5.6 is now available in OpenAI Codex**, giving Codex users access to OpenAI's latest frontier model.

  ### Bug Fixes

  * Various bug fixes and stability improvements
</Update>

<Update label="June 2026" description="Provider API keys from .env, global installs for Codex and Claude, updated Claude Opus model, credits visibility, independent memory controls">
  ## More Control Over Providers, Credits, and Memory

  ### Provider API Keys from `.env`

  Provider API keys can now be loaded from an environment file — the plugin picks them up automatically, no manual configuration required.

  ### Global Installation for Codex and Claude

  **Global installation support** for Codex and Claude is now available, making it easier to share runtimes across projects without re-downloading on every run.

  ### Updated Claude Opus Model

  The plugin has been updated to use the **latest Claude Opus model**.

  ### Credits Usage Visibility

  **See the credits used by each request**, along with your remaining monthly credits — giving you clearer visibility into usage as you work.

  ### Independent Memory File Controls

  **Enable or disable your personal and project memory files independently**, giving you finer-grained control over what context the agent retains between sessions.

  ### Bug Fixes

  * Various bug fixes and stability improvements
</Update>

<Update label="May 2026" description="Auto-approve mode, MCP tool permissions, hooks in CLI, AGENTS.md replaces custom rules">
  ## Faster Agents, Tighter Permissions, and a Cleaner Plugin Experience

  ### Auto-Approve Mode for Agent Actions

  A new **Auto-approve mode** is now generally available across VS Code and JetBrains. Ideal for trusted workflows where you want the agent to keep moving without manual confirmation at each step.

  ### Permission Management for MCP Tools

  Agents now request permission before using MCP tools. Grant one-time access or configure **"Always allow"** for trusted tools in settings — full visibility into which external tools run during a task.

  ### Hooks in ZenCLI

  A new **hooks system** in `zencli` lets you run custom commands at key points in an agent's lifecycle — perfect for logging, custom telemetry, or pre/post-task automation.

  ### Global Installation of Codex and Claude Code

  The CLI now supports **global installation of Codex and Claude Code**, making it easier to share runtimes across projects without re-downloading on every run.

  ### Provider API Keys from `.env`

  Configure provider API keys directly in your project's `.env` file — the CLI will pick them up automatically.

  ### Improvements

  * **Custom rules removed** — use `AGENTS.md` instead for a single, standardized way to define project conventions
  * **Built-in system agents removed** from VS Code and JetBrains — all tasks now run through the unified Coding Agent
  * **Usage-based billing support** in plugins
  * More consistent sign-in experience in VS Code across all auth flows
  * Fixed **JetBrains compatibility** issues affecting newer IDE versions
  * Fixed **plugin window constantly stealing focus** during agent runs
  * Fixed **CLI hanging** after task completion
</Update>

<Update label="April 2026" description="GPT 5.5, Opus 4.7, auto permission mode, image generation">
  ## New Models, Smarter Agents, and Better Control

  ### GPT 5.5 Support

  The latest frontier model from OpenAI is now available in Zencoder. Use GPT 5.5 for your most complex tasks — planning, debugging, and research workflows.

  ### Claude Opus 4.7 with Streaming Thinking

  Claude Opus 4.7 is now supported with **streaming thinking** — watch the model's reasoning process in real time as it works through your problem.

  ### Auto Permission Mode

  A new **Auto permission mode** for Claude Code lets agents execute without manual approval at each step. Ideal for trusted workflows where you want the agent to move fast.

  ### Image Generation

  Image generation is now enabled by default. Ask the agent to create visuals — logos, diagrams, mockups — and see results rendered inline in chat.

  ### Agent-Browser Skill

  A new **agent-browser** skill replaces the previous Playwright skill, giving agents improved browser automation capabilities for testing and web interaction tasks.

  ### Frontend Design Skill

  A new **built-in frontend-design skill** helps agents generate production-quality UI designs and HTML mockups directly from your descriptions.

  ### MCP Tool Permissions

  Agents now request permission before using MCP tools, giving you visibility and control over which external tools are invoked during a task. You can also configure **"Always allow"** for trusted tools in settings.

  ### Delete Rules from UI

  You can now **delete skills** directly from the VS Code and JetBrains UI — no need to manually remove files.

  ### Improvements

  * **Improved model selector** — clearer display of the current engine and model
  * **Optimized system prompts** for Claude 4.6 and GPT 5.4 model families
  * **Updated comprehensive review** and **cross-review** skills
  * Fixed agent reporting it edited a file when it didn't actually make changes
  * Fixed Anthropic models stopping prematurely due to output token limits
  * Fixed long-running agent sessions failing with MCP tools
  * Fixed empty `.zencoder/workflows` folders being created in every project
  * Fixed session data corruption in VS Code
</Update>

<Update label="March 2026" description="Multi-model reviews, skills in UI, /init command, Mermaid diagrams">
  ## Smarter IDE Workflows and Collaboration

  ### Multi-Model Code Review

  You can now get a **second opinion on your code** using another model directly inside your IDE. **Review with another model** lets you validate and improve generated code quality. **/comprehensive-review** provides deeper, multi-model feedback for more critical changes.

  ### Skills in the IDE

  **Add and manage skills directly from the UI**. Built-in skills are easier to discover and use, enabling more structured and repeatable workflows.

  ### Project Understanding with /init

  A new **/init command** helps the agent understand your repository faster. Automatically gathers project context and structure, improving response quality from the very first interaction.

  ### Visual Code Understanding (Mermaid Support)

  Agents can now **render Mermaid diagrams directly in your IDE** — useful for understanding architecture, flows, and generated outputs.

  ### IDE Notifications

  **Sound and visual notifications** when responses are ready or approvals are required. Fully configurable in settings.

  ### Improvements

  * More reliable task execution with improved handling of complex workflows
  * Better subagent coordination for more accurate and structured outputs
  * Smoother chat experience with improved auto-scrolling
  * Simplified controls for model and tool selection
  * Improved responsiveness across both VS Code and JetBrains plugins

  ### Bug Fixes

  * Fixed rare cases where the agent could freeze or crash
  * Fixed issues with chat auto-scrolling and output rendering
  * Fixed issues affecting task execution consistency

  ### Important Changes

  * Custom rules are being phased out in favor of a more structured approach
  * Traditional inline code completion is no longer supported — focus is now on agent-driven workflows
</Update>

<Update label="February 2026" description="Gemini 3.1, GPT-5.3 Codex, Sonnet 4.6, built-in skills, research agent, subagent streaming">
  ## IDE Agent

  ### New Model Support

  Three powerful new models: **Gemini 3.1** with improved thinking defaults, **GPT-5.3 Codex** for enhanced code generation, and **Sonnet 4.6** for Anthropic users. The agent can now intelligently choose which model to use for subtasks.

  ### Built-in Skills

  Three skills included by default: **Playwright** for browser automation, **Code Review** for structured review workflows, and **Skill Creator** for creating custom skills. Access via `/` and `@`-menu.

  ### Research Agent

  A dedicated research agent for exploration and analysis — codebase investigation, issue analysis, and pre-implementation research.

  ### Subagent Streaming

  See subagent work in real time with live streaming output, clear task delegation visibility, and proper permission handling.

  ### Improvements

  * Redesigned navbar with "All Chats" moved to the left
  * Clickable chat title for quick rename/navigation
  * Skills menu showing configured skills
  * AGENTS.md support for agent instructions
  * Review with another model for second opinions
  * Adaptive thinking support for Anthropic provider
  * MCP caching and lazy loading for faster startup
  * Improved CLI startup time, migrated CLI to Bun
  * Trial quota exhausted notifications

  ### Bug Fixes

  * Fixed "Wrapping up" hang and agent startup hangs
  * Fixed incomplete tool call handling
  * Fixed MCP error handling preventing deadlocks
  * Fixed revert button visibility in JetBrains
  * Fixed API key inheritance billing issues
  * Fixed token visibility in IDE logs
</Update>

<Update label="January 2026" description="Skills support, terminal mentions, chat navigation, context window indicator">
  ### Skills Support

  Create reusable prompt templates that modify how the agent responds. **Local and global skills** in `.agents/skills` (project) or `~/.agents/skills` (global).

  ### Terminal Mentions

  Reference terminal content directly in chat — share command results, error logs, and build output with the agent.

  ### Chat Navigation Dropdown

  Quick chat switching, search functionality, and pin important chats for easy access.

  ### Context Window Indicator

  Real-time percentage display showing how much of the context window is being used. Helps optimize prompts and avoid context limits.

  ### Improvements

  * Click to open files mentioned in chat responses
  * Streaming indicators and action required indicators
  * Improved small screen UI and better error recovery

  ### Bug Fixes

  * Fixed chat deletion redirect, agent selection on edit
  * Fixed mention popup cleanup, workflow card spacing
  * Fixed table line breaks, chat input focus
  * Windows compatibility fix for some users
</Update>

<Update label="December 2025" description="Spec-driven development, enhanced markdown, per-project MCP, stability improvements">
  ### Spec-Driven Development Workflows

  Custom workflows for spec-driven development — guided development process, spec-first approach, and improved reliability through systematic planning.

  ### Enhanced Markdown Support

  Markdown tables rendering, copy as Markdown button, enhanced code blocks, and line break preservation.

  ### Model Context Protocol Enhancements

  Per-project MCP configuration, better session management, enhanced reliability, and RAG search integration.

  ### Platform Stability Improvements

  Faster agent responses, better edge case handling, improved memory usage, and enhanced long-session reliability.
</Update>

<Update label="November 2025" description="Custom model support, LoC metrics, ZenCLI milestone, dynamic model switching">
  ### Custom Models in Zencoder Plugins

  Use privately deployed models or connect to unsupported providers. Full flexibility to leverage custom LLMs while maintaining Zencoder's development features.

  ### Lines of Code Metrics

  New LoC metrics in the usage analytics dashboard — lines of code generated vs. lines of code accepted. Available in the web admin panel and Analytics API.

  ### Dynamic Model Switching

  Change AI models between messages without losing context or starting a new chat session.

  ### Model Catalog Updates

  New: **GPT-5.1-Codex**, **Gemini Pro 3.0**. Removed: Sonnet 4 PT, GPT-5 (superseded by GPT-5.1-Codex).
</Update>

<Update label="October 2025" description="Clipboard image pasting, chat interface improvements, 20+ stability fixes">
  ### Clipboard Image and Text Pasting

  Paste content directly from clipboard into chat — images, screenshots, long text, and code blocks. Cross-platform support across VS Code, JetBrains, and webview.

  ### Additional Updates

  * Code blocks no longer collapse during streaming
  * Clickable mentions for quick navigation
  * Code hunk language detection for syntax highlighting
  * Removed deprecated docstrings feature
  * MCP tool reliability improvements
  * 20+ bug fixes across API handling, chat, model selection, and platform-specific issues
</Update>

<Update label="September 2025" description="Universal AI Platform, Sonnet 4.5 Parallel Thinking, Grok Code Fast 1">
  ### Universal AI Platform

  Connect your existing ChatGPT, Claude, or Gemini subscriptions to access Zencoder's enterprise features. Native CLI support with Claude Code and OpenAI Codex. Works in VS Code (2.38+) and JetBrains (2.16+).

  ### Sonnet 4.5 Parallel Thinking

  Day-zero support for Anthropic's latest model — parallel execution, persistent state tracking, high verification bias. Available on Starter+ plans at 1.5× multiplier.

  ### Cost-Efficient Model Options

  **Grok Code Fast 1** at 0.25× multiplier — the most cost-efficient model in the lineup. Plus **GPT-5 Codex** at 1× multiplier.

  ### Comprehensive Troubleshooting

  New guides for VS Code Gray Screen (GSOD) and Windows CLI Installation issues.
</Update>

<Update label="August 2025" description="Analytics Dashboard, GPT-5, Skills improvements, MCP OAuth">
  ### Analytics Dashboard

  Organizational insights for Core plans and above — daily active users, IDE and language analytics, member activity tracking.

  ### Enhanced Model Selection

  GPT-5 support added within 24 hours of release. Gemini 2.5 Pro at 0.75× multiplier. Opus 4.1 on Advanced/Max plans. BYOK support for OpenAI and Anthropic.

  ### Skills Enhancements

  Custom skill folders for compatibility with Cursor, Windsurf, Cline, and Continue. Create skills from chat. Currently applied skills badge.

  ### MCP Improvements

  Remote and HTTP-based MCP support with OAuth2 for JetBrains. Max plan with priority support and SLA guarantees.
</Update>

<Update label="July 2025" description="Multi-Repository Search, project-specific instructions, image attachments">
  ### Multi-Repository Search

  Index multiple repositories through the web admin panel. Cross-repository code understanding with automatic context detection.

  ### Project-Specific AI Instructions

  Project-level instructions for team sharing. Conditional application with glob patterns (now evolved into Skills).

  ### Image Attachments for All Users

  Universal access to image attachments across VS Code and JetBrains. Design-to-code workflow with repository image references.

  ### E2E Testing Enhancements

  Multi-framework support — Cypress, Playwright, or Selenium.
</Update>

<Update label="June 2025" description="E2E testing, LLM call pricing, project context, image prompts">
  ### E2E Testing

  Automated E2E test creation in chat. Playwright integration, intelligent test recording, cross-browser testing.

  ### New Pricing Model

  LLM call-based pricing instead of token usage for better transparency and predictability.

  ### Project Context

  Comprehensive project analysis for context. Reduces LLM calls and speeds up agent responses.

  ### Image Prompts in VS Code (Beta)

  Repository image support for visual context — upload Figma screenshots or design mockups and generate matching components.
</Update>

<Update label="May 2025" description="Zen Agents platform, MCP Library, Marketplace, change management">
  ### Zen Agents Platform

  Agent sharing across organizations, custom agent registry synced across devices/IDEs, and tool configuration for custom agents.

  ### MCP Library and Tools Management

  Built-in library with 100+ MCP servers. Project-level MCP installation. Dedicated Agent Tools UI.

  ### Zen Agents Marketplace

  Browse 20+ purpose-built agents. Community contributions via open-source repository. Available in IDEs and on the website.

  ### Change Management

  New ability to revert and rollback agent changes with granular control.
</Update>

<Update label="April 2025" description="Bash/Shell tool, Requirements tool, enhanced chat, search improvements">
  ### Bash/Shell Tool for Coding Agent

  Bash tool now available to the coding agent with safe command UX, "Don't ask again" option, and Coffee Mode support.

  ### Requirements Tool

  Automatically asks for clarifications, delivers higher-quality results, and reduces back-and-forth.

  ### Enhanced Chat Experience

  Slash commands (`/`) and file mentions (`@`) hints in chatbox. Warning system for long chats. Attach files from outside the project.

  ### Bug Fixes

  * Fixed indexing stuck at "Updating index"
  * Fixed cursor positioning above inserted code snippets
  * Jira authentication flow improvements
</Update>

<Update label="March 2025" description="Coding Agent GA, Coffee Mode, Jira integration, MCP support, Chrome extension">
  ### Coding Agent Out of Beta

  Generally available across all supported IDEs with better codebase understanding and more stable code generation.

  ### Coffee Mode

  Work continuously without interrupting your flow — no more constant confirmations.

  ### New Integrations

  **Jira Integration** — mention Jira tickets directly in chat. **MCP Servers Configuration** — connect to community-built tools. **Chrome Extension** — connect with 20+ developer tools from the browser.

  ### Unit Testing Agent Improvements

  Checks for syntax/compile errors, analyzes existing tests to avoid duplication, access to Bash tools.

  ### UX Improvements

  Single-click application for multi-file changes. Persistent coding agent state. New chat button & UI. Automatic saving of accepted changes.
</Update>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
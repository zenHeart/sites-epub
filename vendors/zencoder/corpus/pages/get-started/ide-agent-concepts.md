> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IDE Agent Concepts

> Learn the key concepts that power Zencoder IDE Agent — from the Coding Agent and Skills to context management.

## Coding Agent

The [Coding Agent](/features/coding-agent) is Zencoder's primary development tool. It creates and modifies files across your codebase, runs shell commands, searches the web, and uses MCP tools — all from a single chat prompt.

<Card title="Coding Agent" icon="code" href="/features/coding-agent">
  Multi-file code generation, refactoring, and modification with full tool access
</Card>

## Custom AI Agents

[Custom AI Agents](/features/ai-agents) let you define reusable agents with specific instructions, tools, and commands for recurring tasks like code review, documentation updates, or domain-specific refactoring. They can be shared across your team.

<Card title="AI Agents" icon="microchip-ai" href="/features/ai-agents">
  Create and share custom agents for your team's workflows
</Card>

## Skills

[Skills](/features/skills) are reusable instruction packages that agents load automatically based on task context. They give agents domain expertise, procedural knowledge, and team-specific conventions without manual selection.

* Stored as `SKILL.md` files in `.agents/skills/` in your repo
* The agent decides when to load a skill based on its description and your prompt
* Works in both IDE Agents and Zenflow

<Card title="Skills" icon="wand-magic-sparkles" href="/features/skills">
  Create and manage reusable instruction packages for your agents
</Card>

## Multi-Agent Orchestration (Zenflow)

[Zenflow](/zenflow/quickstart) is Zencoder's standalone desktop app for orchestrating complex, multi-step development workflows. While IDE Agents are best for inline tasks, Zenflow handles larger work:

* **Parallel agents** — Run multiple agents simultaneously on different parts of a task
* **Git worktrees** — Each task runs in an isolated worktree so changes don't interfere
* **Spec-driven development** — Define specifications and let agents implement them step by step
* **Built-in verification** — Agents validate their own output before presenting results

<CardGroup cols={2}>
  <Card title="Zenflow Quickstart" icon="desktop" href="/zenflow/quickstart">
    Get started with multi-agent orchestration
  </Card>

  <Card title="Key Concepts" icon="lightbulb" href="/zenflow/key-concepts">
    Understand tasks, worktrees, and workflows
  </Card>
</CardGroup>

## IDE and Tool Integrations

### IDE Integration

Zencoder installs as an extension from the VS Code or JetBrains marketplace. All features are accessible inside the IDE without switching to external tools.

<Card title="IDE Integration" icon="puzzle-piece" href="/quickstart/ide-plugin">
  Installation steps for VS Code, JetBrains, and Android Studio
</Card>

### Tool Integrations

Zencoder connects to external tools through two paths:

1. **Native Integrations** — Direct integration with Jira for pulling ticket context into the IDE
2. **Model Context Protocol (MCP)** — Open standard for connecting agents to databases, APIs, and custom tools

<Warning>
  **Chrome Extension Discontinued** — The Zencoder Chrome Extension is no longer available. Use `@url` mentions or MCP servers to bring in context from browser-based tools.
</Warning>

<Card title="Tool Integrations" icon="link" href="/features/integrations-and-mcp">
  Setup instructions for native integrations and MCP
</Card>

## How Everything Fits Together

1. **IDE Agent** surfaces agents directly in your editor for inline tasks
2. **Zenflow** orchestrates multi-agent workflows for complex, multi-step projects
3. **Coding Agent** handles code generation, modification, testing, and debugging
4. **Custom Agents** extend functionality with task-specific agents you define
5. **Skills** give agents domain knowledge and project-specific standards
6. **Integrations & MCP** connect agents to your team's external tools

<Callout>
  Start with the Coding Agent for most tasks. Use Custom Agents for recurring team workflows. Use Zenflow when the task spans multiple files, agents, or repositories.
</Callout>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Context Management

> How Zencoder agents gather, prioritize, and use context from your codebase, files, and external tools

## How Context Works

When you send a message, the agent assembles context from multiple sources to understand your task. The more relevant context it has, the better the output.

<Steps>
  <Step title="Workspace analysis">
    The agent reads your project's file structure, dependencies, and language configuration to understand the environment.
  </Step>

  <Step title="Active file context">
    The file currently open in your editor is automatically included. The agent sees the full contents and cursor position.
  </Step>

  <Step title="Skill matching">
    The agent checks available [Skills](/features/skills) and loads any whose description matches the current task.
  </Step>

  <Step title="Explicit context">
    Anything you attach via `@` mentions, file selections, or pasted content is added to the context window.
  </Step>

  <Step title="Tool-gathered context">
    During execution, the agent can search your codebase, read additional files, run shell commands, and query MCP tools to gather more context as needed.
  </Step>
</Steps>

## Providing Context with @ Mentions

Use `@` in the chat input to attach specific context:

| Mention | What it does |
| - | - |
| `@file` | Attaches a specific file from your workspace |
| `@folder` | Attaches all files in a folder |
| `@Jira` | Pulls issue details from a connected Jira ticket |
| `@url` | Fetches content from a URL (docs, API references) |

<Tip>
  Be selective with `@folder` — attaching a large directory can dilute the relevant context. Prefer `@file` for targeted results.
</Tip>

## Multi-Repository Context

With [Multi-Repository Search](/features/multi-repo), agents can search across indexed repositories beyond the current workspace. This is useful for:

* Understanding cross-service dependencies
* Finding shared utility implementations
* Checking how other services handle similar patterns

Multi-repo context is fetched on demand — the agent searches indexed repos when your prompt references other services or projects.

<Note>
  Multi-Repository Search requires Pro Plus or higher. See [Multi-Repository Search](/features/multi-repo) for setup instructions.
</Note>

## Skills as Context

[Skills](/features/skills) inject domain knowledge and team conventions into the agent's context automatically. Unlike `@` mentions, skills are loaded based on task matching — you don't need to attach them manually.

Examples of context that skills provide:

* Coding standards and naming conventions
* Error handling patterns your team uses
* Testing requirements and framework preferences
* API design guidelines

Skills are stored as `SKILL.md` files in `.agents/skills/` and are version-controlled with your repo.

## Image Context

Attach images directly in chat to provide visual context:

* **Screenshots** of UI bugs or desired designs
* **Figma exports** for design-to-code workflows
* **Error screenshots** from browsers or terminals
* **Architecture diagrams** for reference

Image attachments are available across VS Code and JetBrains IDEs.

## Context from External Tools

<Warning>
  **Chrome Extension Discontinued**

  The Zencoder Chrome Extension has been discontinued and is no longer available. Use `@url` mentions to pull in context from browser-based tools, or connect them via [MCP servers](/features/integrations-and-mcp#model-context-protocol-mcp).
</Warning>

### MCP Tools

Connected [MCP servers](/features/integrations-and-mcp) let agents query external systems during execution — databases, APIs, Slack, GitHub, and more. The agent decides when to call these tools based on the task.

## Tips for Better Context

<AccordionGroup>
  <Accordion title="Start with the right file open">
    The active editor file is always included. Open the most relevant file before sending your prompt.
  </Accordion>

  <Accordion title="Use @ mentions for targeted context">
    Instead of describing a file's contents, attach it with `@file`. The agent gets the exact source instead of your paraphrase.
  </Accordion>

  <Accordion title="Keep chats focused on one task">
    Long, multi-topic chats accumulate stale context. Start a new chat for each distinct task so the agent's context stays clean.
  </Accordion>

  <Accordion title="Let the agent search when needed">
    You don't need to attach every relevant file upfront. The agent has codebase search and file read tools — it will find what it needs during execution.
  </Accordion>

  <Accordion title="Use Skills for recurring context">
    If you find yourself repeating the same instructions across chats, create a [Skill](/features/skills) so the agent loads that context automatically.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Coding Agent" icon="code" href="/features/coding-agent">
    The primary agent that uses all context sources
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/features/skills">
    Reusable instruction packages loaded by context matching
  </Card>

  <Card title="Multi-Repository Search" icon="magnifying-glass" href="/features/multi-repo">
    Cross-repository context for multi-service architectures
  </Card>

  <Card title="Integrations & MCP" icon="plug" href="/features/integrations-and-mcp">
    Connect external tools for richer context
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
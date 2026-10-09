> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Coding Agent

> Multi-file, multi-language code generation and modification with deep codebase understanding

## What is the Coding Agent?

The Coding Agent is Zencoder's primary development tool that generates, modifies, and refactors code across multiple files and languages. It has built-in validation and error correction, enabling complex development tasks from a single prompt.

<iframe src="https://www.youtube.com/embed/12xmFOFXKpY?si=drn5658m767NUkI7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style={{ width: '100%', height: '400px', borderRadius: '0.5rem' }} />

## Accessing the Coding Agent

To access the Coding Agent:

1. Open the agent selector with `Cmd+.` (Mac) or `Ctrl+.` (Windows/Linux)
2. Select `Coding` from the dropdown menu
3. The Coding Agent can perform complex tasks like:
   * Creating and modifying multiple files
   * Implementing entire features
   * Searching the web for documentation
   * Running validation and tests

<img src="https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/agents-selector.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=a12e4c38feed42e1eb5e6de6f3e5116a" alt="Agent selector showing Coding Agent option" width="1106" height="430" data-path="images/agents-selector.png" />

<Note>
  Each chat maintains its selected agent type throughout the conversation. You can start new chats with different agents as needed using the agent selector.
</Note>

## How It Works

When you send a message to the Coding Agent, it follows a multi-step process:

<Steps>
  <Step title="Understand context">
    The agent analyzes your project's structure, patterns, and coding standards from the current workspace and any active [Skills](/features/skills).
  </Step>

  <Step title="Plan the changes">
    Based on your prompt, the agent creates a plan — which files to read, edit, or create, and which tools to invoke (shell commands, web search, MCP calls).
  </Step>

  <Step title="Execute and iterate">
    The agent makes edits across multiple files, runs commands, and validates its output. If errors occur (lint failures, type errors, test failures), it self-corrects automatically.
  </Step>

  <Step title="Present results">
    You see a diff of all changes with inline explanations. Accept, reject, or refine with follow-up prompts in the same chat.
  </Step>
</Steps>

<Note>
  There is no limit on the number of tool calls the agent can make in a single turn. Complex tasks may use dozens of tool calls across planning, editing, and validation.
</Note>

## Agent Tools

The Coding Agent has access to a full set of tools that it invokes autonomously:

| Tool | What it does |
| - | - |
| **File Editor** | Read, create, edit, and delete files across your workspace |
| **Shell Commands** | Run terminal commands (build, test, lint, git, package managers) |
| **Codebase Search** | Semantic and full-text search across your project files |
| **Web Search** | Search the web for documentation, APIs, and solutions |
| **Fetch Webpage** | Retrieve content from URLs (docs, API references, stack traces) |
| **Git Operations** | Stage, commit, diff, and manage branches |
| **MCP Tools** | Access any connected [MCP servers](/features/integrations-and-mcp) (databases, Jira, GitHub, Slack, etc.) |
| **File Search** | Find files by name or pattern across the workspace |
| **Gather Requirements** | Ask clarifying questions before proceeding with ambiguous tasks |

<Tip>
  Connect MCP servers to give the agent access to your team's tools — pull Jira tickets, query databases, post to Slack, and more. See [Integrations & MCP](/features/integrations-and-mcp).
</Tip>

## Technical Capabilities

<CardGroup cols={2}>
  <Card title="Multi-file Operations" icon="files">
    Generates and modifies code across multiple files simultaneously while maintaining consistency and proper references
  </Card>

  <Card title="Language Agnostic" icon="code">
    Supports multiple programming languages and frameworks with language-specific optimizations and best practices
  </Card>

  <Card title="Codebase Understanding" icon="brain">
    Analyzes existing code structure, patterns, and conventions to generate contextually appropriate solutions
  </Card>

  <Card title="Automated Validation and Fixes" icon="check-double">
    Validates generated code against syntax rules, project conventions, and integration requirements
  </Card>
</CardGroup>

## Tips for Better Results

<AccordionGroup>
  <Accordion title="Be specific about scope">
    Instead of "refactor the API," try "refactor the user authentication endpoints in `src/api/auth.ts` to use the new session middleware." The agent works better with clear boundaries.
  </Accordion>

  <Accordion title="Use Skills for recurring standards">
    If you always want a certain code style, test pattern, or error handling approach, define it as a [Skill](/features/skills) so every agent response follows it automatically.
  </Accordion>

  <Accordion title="Let the agent run tests">
    Include "run the tests after making changes" in your prompt. The agent will execute your test suite and self-correct if anything fails.
  </Accordion>

  <Accordion title="Keep chats focused">
    Start a new chat for each distinct task. Long, multi-topic chats can cause the agent to lose context on earlier instructions.
  </Accordion>

  <Accordion title="Attach context with @-mentions">
    Use `@file`, `@folder`, or paste URLs to give the agent targeted context.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="AI Agents" icon="microchip-ai" href="/features/ai-agents">
    Create custom agents with specific instructions and tools for recurring tasks
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/features/skills">
    Reusable instruction packages that agents load automatically based on task context
  </Card>

  <Card title="Integrations & MCP" icon="plug" href="/features/integrations-and-mcp">
    Connect external tools via Model Context Protocol
  </Card>

  <Card title="Supported Models" icon="microchip" href="/features/models">
    Choose from 10+ models or bring your own API key
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
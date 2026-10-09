> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Zenflow supports multiple AI coding agents and models from different providers.

## Multi-Agent Support

Zenflow can orchestrate tasks using different AI coding agents. Each agent runs in an isolated Git worktree and has access to Zencoder's context engine, multi-repo search, and skills — regardless of which underlying model or provider powers it.

## Available Agents

<CardGroup cols={3}>
  <Card title="Claude Code" icon="wand-magic-sparkles" href="./claude-code">
    Anthropic's Claude Code agent.
  </Card>

  <Card title="Codex" icon="brain" href="./codex">
    OpenAI's Codex agent.
  </Card>

  <Card title="Gemini" icon="sparkles" href="./gemini">
    Google's Gemini agent.
  </Card>
</CardGroup>

## Custom Models

Connect your own model endpoints — local, VPC, or third-party — to use them alongside or instead of built-in agents.

<Card title="Custom Models" icon="puzzle-piece" href="./custom-agent">
  Bring your own model or private endpoint
</Card>

## Model Flexibility

Zencoder supports models from multiple providers:

| Provider | Models |
| - | - |
| **Anthropic** | Haiku 4.5, Sonnet 4.6, Opus 4.6, Opus 4.7 |
| **OpenAI** | GPT-5.3 Codex, GPT-5.4, GPT-5.4-mini, GPT-5.5 |
| **Google** | Gemini Pro 3.1, Gemini Flash 3.0 |
| **xAI** | Grok Code Fast 1 |
| **Zencoder** | Auto (routed mix), Auto+ |

Select the model per chat session in the model dropdown. Different models have different cost multipliers — see [Models](/features/models) for the full list with plan requirements.

## Custom Hosted Models

You can connect your own model endpoints — local, VPC, or third-party — using `settings.json`. This lets you:

* Run open-source models locally via Ollama or vLLM
* Use Azure OpenAI, Vertex AI, or other cloud-hosted endpoints
* Point to private inference servers inside your network
* Hide the default model catalog and only expose approved models

See [Custom Models Configuration](/features/custom-models-configuration) for the full setup guide.

## Shared Capabilities

All agents running through Zenflow get access to:

| Feature | Description |
| - | - |
| **Multi-Repo Search** | Cross-repository code search |
| **Skills** | Reusable instruction packages |
| **MCP Integrations** | External tool access (databases, APIs, Jira, etc.) |
| **Analytics** | Usage and productivity tracking |

## Selecting an Agent in Zenflow

1. Open **Settings → Default agents** in Zenflow
2. Set the default agent for new tasks


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
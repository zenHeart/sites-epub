> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Codex (OpenAI)

> Use OpenAI's Codex agent through Zenflow.

## Overview

OpenAI Codex is a code-specialized agent from OpenAI. When configured in Zenflow, it runs inside isolated Git worktrees with access to Zencoder's context engine, multi-repo search, and skills.

## Setup

### Prerequisites

You need one of:

* **OpenAI API key**: Get one at [platform.openai.com](https://platform.openai.com)

### Installation

<Steps>
  <Step title="Install Codex CLI">
    Install the OpenAI Codex agent on your machine. See [OpenAI's documentation](https://platform.openai.com/docs) for installation instructions.
  </Step>

  <Step title="Configure API key">
    Set your OpenAI API key during the authentication flow.
  </Step>

  <Step title="Select in Zenflow">
    In Zenflow, go to **Settings → Saved presets** and select **Codex** as the agent for your tasks.
  </Step>
</Steps>

## When to Use Codex

* **Code generation**: Fast, accurate code writing across many languages
* **Test generation**: Comprehensive test suites from existing code
* **Quick iterations**: Fast response times for rapid prototyping
* **API integration**: Strong understanding of APIs and SDKs

## Configurations

* **Sandbox** – Controls what Codex can do without asking: `None`, `Always ask`, `Workspace write`, or `Danger full access`.
* **Model** – Override the Codex model ID.
* **Model reasoning effort** – Controls how much compute Codex spends reasoning: `none`, `low`, `medium`, `high`.

## Pricing

| Option | How It Works |
| - | - |
| **BYOK (API Key)** | Pay OpenAI directly based on token usage |

## Next Steps

<CardGroup cols={2}>
  <Card title="Supported Agents" icon="layer-group" href="./overview">
    Compare all available agents
  </Card>

  <Card title="Claude Code" icon="wand-magic-sparkles" href="./claude-code">
    Try Claude for reasoning tasks
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
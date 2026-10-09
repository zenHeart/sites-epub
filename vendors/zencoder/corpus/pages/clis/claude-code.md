> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code

> Use Anthropic's Claude Code agent through Zenflow.

## Overview

Claude Code is Anthropic's coding agent. When configured in Zenflow, it runs inside isolated Git worktrees and benefits from Zencoder's context engine, multi-repo search, and skills.

## Setup

### Prerequisites

You need one of:

* **Anthropic API key**: Bring your own key (BYOK)
* **Claude Pro/Max subscription**: Use your existing Anthropic account

### Installation

<Steps>
  <Step title="Install Claude Code">
    Install the Claude Code agent on your machine. See [Anthropic's documentation](https://docs.anthropic.com/en/docs/claude-code/overview) for installation instructions.
  </Step>

  <Step title="Authenticate">
    Follow Anthropic's authentication flow to connect your account or API key.
  </Step>

  <Step title="Select in Zenflow">
    In Zenflow, go to **Settings → Saved presets** and select **Claude Code** as the agent for your tasks.
  </Step>
</Steps>

## When to Use Claude Code

* **Complex debugging**: Multi-step problem solving that requires reasoning through code paths
* **Code review**: Thorough, context-aware feedback on diffs
* **Architecture decisions**: System design trade-offs
* **Refactoring**: Safe transformations across large codebases

## Configurations

* **Model** – Override the Claude model ID to use a specific variant.
* **Dangerously Skip Permissions** – When enabled, Claude runs commands without explicit approval. Useful for trusted repos; disable for production workloads.

## Pricing

| Option | How It Works |
| - | - |
| **BYOK (API Key)** | Pay Anthropic directly for usage |
| **Claude Pro/Max** | Use your existing subscription |

## Next Steps

<CardGroup cols={2}>
  <Card title="Supported Agents" icon="layer-group" href="./overview">
    Compare all available agents
  </Card>

  <Card title="Custom Agent" icon="puzzle-piece" href="./custom-agent">
    Connect other models
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini

> Use Google's Gemini agent through Zenflow.

## Overview

Gemini is Google's AI coding agent. When configured in Zenflow, it runs inside isolated Git worktrees with access to Zencoder's context engine, multi-repo search, and skills. Gemini supports multi-modal inputs including images and screenshots.

## Setup

### Prerequisites

You need one of:

* **Google AI API key**: Get one at [ai.google.dev](https://ai.google.dev)
* **Vertex AI access**: For enterprise deployments

### Installation

<Steps>
  <Step title="Install Gemini CLI">
    Install the Gemini agent on your machine. See [Google's documentation](https://ai.google.dev) for installation instructions.
  </Step>

  <Step title="Authenticate">
    Configure your Google AI API key or Vertex AI credentials.
  </Step>

  <Step title="Select in Zenflow">
    In Zenflow, go to **Settings → Saved presets** and select **Gemini** as the agent for your tasks.
  </Step>
</Steps>

## When to Use Gemini

* **Multi-modal tasks**: Implement UIs from screenshots or mockups
* **Large context windows**: Work with very large codebases
* **Design-to-code**: Convert Figma exports into working components
* **Visual debugging**: Debug rendering issues from screenshots

## Configurations

* **Model** – `default` for higher quality, `flash` for faster responses.

## Pricing

| Option | How It Works |
| - | - |
| **Google AI API** | Pay-per-use with a free tier |
| **Vertex AI** | Enterprise pricing with SLAs |

## Next Steps

<CardGroup cols={2}>
  <Card title="Supported Agents" icon="layer-group" href="./overview">
    Compare all available agents
  </Card>

  <Card title="Figma to Code" icon="paintbrush" href="/user-guides/tutorials/figma-to-code-tutorial">
    Design-to-code tutorial
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
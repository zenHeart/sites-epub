> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Models

> Connect your own AI models or agents to Zencoder.

## Overview

Zencoder supports custom agents, allowing you to connect your own models, private deployments, or third-party inference endpoints. Custom models appear in the model selector alongside built-in options.

## Use Cases

* **Local models**: Run open-source models via Ollama or vLLM on your machine
* **Private cloud**: Use Azure OpenAI, Vertex AI, or AWS Bedrock endpoints
* **Air-gapped environments**: Point to inference servers inside your network
* **Fine-tuned models**: Use models you've trained on your own data

## Configuration

Custom models are configured via `settings.json`. This file works at two levels:

* **Machine-wide**: `~/.zencoder/settings.json`
* **Per project**: `.zencoder/settings.json` (overrides machine-wide)

### Example: Ollama (Local)

```json theme={"system"}
{
  "providers": {
    "ollama-local": {
      "mode": "direct",
      "type": "openai-compatible",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "not-needed",
      "models": {
        "llama3-70b": {
          "name": "llama3:70b",
          "displayName": "Llama 3 70B (Local)",
          "capabilities": [],
          "options": {
            "temperature": 0.7,
            "maxOutputTokens": 4096
          }
        }
      }
    }
  }
}
```

### Example: Azure OpenAI

```json theme={"system"}
{
  "providers": {
    "azure-gpt4": {
      "mode": "direct",
      "type": "openai-compatible",
      "baseUrl": "https://your-resource.openai.azure.com/v1",
      "apiKey": "${AZURE_OPENAI_KEY}",
      "models": {
        "gpt4-deployment": {
          "name": "gpt-4",
          "displayName": "Azure GPT-4",
          "capabilities": [],
          "options": {
            "temperature": 0.2,
            "maxOutputTokens": 4096
          }
        }
      }
    }
  }
}
```

### Example: Google Gemini

For Google Gemini, set the `type` to `gemini`. Note that `baseUrl` is not required when using the direct Gemini integration.

```json theme={"system"}
{
  "providers": {
    "gemini": {
      "mode": "direct",
      "type": "gemini",
      "apiKey": "${GEMINI_API_KEY}",
      "models": {
        "gemini-flash-latest": {
          "name": "gemini-flash-latest",
          "displayName": "Gemini Flash Latest BYOC"
        },
        "gemini-pro-latest": {
          "name": "gemini-pro-latest",
          "displayName": "Gemini Pro Latest BYOC"
        }
      }
    }
  }
}
```

### Example: xAI (Grok)

To use xAI's Grok models, use the `openai-compatible` type and specify the xAI API base URL.

```json theme={"system"}
{
  "providers": {
    "xai": {
      "mode": "direct",
      "type": "openai-compatible",
      "baseUrl": "https://api.x.ai/v1",
      "apiKey": "${XAI_API_KEY}",
      "models": {
        "grok-build-0.1": {
          "name": "grok-build-0.1",
          "displayName": "Grok Code Fast 1 BYOC"
        },
        "grok-4.20-0309-reasoning": {
          "name": "grok-4.20-0309-reasoning",
          "displayName": "Grok 4.20 Reasoning BYOC"
        }
      }
    }
  }
}
```

### Hiding Default Models

Set `useDefaultProviders` to `false` to only show your custom models in the selector:

```json theme={"system"}
{
  "useDefaultProviders": false,
  "providers": {
    "my-provider": { ... }
  }
}
```

## Requirements

Custom endpoints must support:

| Requirement | Description |
| - | - |
| **OpenAI-compatible API** | `/chat/completions` endpoint |
| **Streaming** | Server-sent events for real-time responses |
| **Tool use** (optional) | Function calling for enhanced capabilities |

## Full Reference

See [Custom Models Configuration](/features/custom-models-configuration) for the complete settings reference, and [Private Deployments](/features/private-deployments) for air-gapped setup.

## Selecting a Custom Model in Chat

In the chat composer, click the preset dropdown (the gear icon) and select **Custom**. Then use the model dropdown next to Zencoder to choose your model.

<div className="mt-3 flex flex-wrap gap-4 justify-center">
  <img src="https://mintcdn.com/forgoodaiinc/C44A_MKv6B04y7aH/images/zenflow/custom-v2.png?fit=max&auto=format&n=C44A_MKv6B04y7aH&q=85&s=a455e47cb9afbafc2e238746d056c0be" alt="Preset dropdown showing Custom option selected" style={{ height:"420px", width:"auto", maxWidth:"100%", borderRadius:"12px" }} width="976" height="572" data-path="images/zenflow/custom-v2.png" />

  <img src="https://mintcdn.com/forgoodaiinc/C44A_MKv6B04y7aH/images/zenflow/custom-model-v2.png?fit=max&auto=format&n=C44A_MKv6B04y7aH&q=85&s=675e706eba7553f4d021e2ff3fd978a6" alt="Model dropdown showing available models including Auto+, Claude, Gemini, GPT, and Grok options" style={{ height:"420px", width:"auto", maxWidth:"100%", borderRadius:"12px" }} width="976" height="572" data-path="images/zenflow/custom-model-v2.png" />
</div>

## Next Steps

<CardGroup cols={2}>
  <Card title="Custom Models Config" icon="gear" href="/features/custom-models-configuration">
    Full configuration reference
  </Card>

  <Card title="Private Deployments" icon="server" href="/features/private-deployments">
    Air-gapped and on-premise setup
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
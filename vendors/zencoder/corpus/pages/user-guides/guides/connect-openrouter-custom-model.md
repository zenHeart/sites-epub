> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zencoder.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect OpenRouter as a Custom Model

> Use OpenRouter to access 200+ models through Zencoder's BYOM (Bring Your Own Model) configuration.

## Overview

[OpenRouter](https://openrouter.ai) is a unified API gateway that provides access to 200+ models from providers like Anthropic, Google, Meta, Mistral, and more — all through a single API key and OpenAI-compatible endpoint.

By connecting OpenRouter as a custom model provider in Zencoder, you can:

* Access models not natively available in the Zencoder model selector
* Use a single API key for multiple providers
* Take advantage of OpenRouter's automatic fallback and routing
* Use open-source models (Llama, Mistral, Qwen, DeepSeek) alongside commercial ones

## Prerequisites

* A Zencoder account (any plan, including Free)
* An [OpenRouter API key](https://openrouter.ai/keys)

## Step-by-Step Setup

<Steps>
  <Step title="Get your OpenRouter API key">
    Go to [openrouter.ai/keys](https://openrouter.ai/keys) and create a new API key. Copy it — you'll need it in the next step.
  </Step>

  <Step title="Open your Zencoder settings file">
    Open the settings file at one of these locations:

    * **Machine-wide**: `~/.zencoder/settings.json`
    * **Per project**: `.zencoder/settings.json` (in your repo root)

    Create the file if it doesn't exist.
  </Step>

  <Step title="Add the OpenRouter provider">
    Paste the following configuration, replacing `your-openrouter-api-key` with your actual key:

    ```json theme={"system"}
    {
      "providers": {
        "openrouter": {
          "mode": "direct",
          "type": "openai-compatible",
          "baseUrl": "https://openrouter.ai/api/v1",
          "apiKey": "your-openrouter-api-key",
          "models": {
            "deepseek-r1": {
              "name": "deepseek/deepseek-r1",
              "displayName": "DeepSeek R1 (OpenRouter)",
              "capabilities": [],
              "options": {
                "temperature": 0.7,
                "maxOutputTokens": 8192
              }
            },
            "llama-4-maverick": {
              "name": "meta-llama/llama-4-maverick",
              "displayName": "Llama 4 Maverick (OpenRouter)",
              "capabilities": [],
              "options": {
                "temperature": 0.7,
                "maxOutputTokens": 8192
              }
            },
            "mistral-large": {
              "name": "mistralai/mistral-large",
              "displayName": "Mistral Large (OpenRouter)",
              "capabilities": [],
              "options": {
                "temperature": 0.7,
                "maxOutputTokens": 4096
              }
            },
            "qwen-3-235b": {
              "name": "qwen/qwen3-235b",
              "displayName": "Qwen 3 235B (OpenRouter)",
              "capabilities": [],
              "options": {
                "temperature": 0.7,
                "maxOutputTokens": 8192
              }
            }
          }
        }
      }
    }
    ```
  </Step>

  <Step title="Reload settings">
    Restart the Zencoder extension or Zenflow app to pick up the new provider. Your OpenRouter models will appear in the model selector.
  </Step>
</Steps>

## Adding More Models

To add any model from the [OpenRouter model list](https://openrouter.ai/models), add a new entry under the `"models"` object. The `"name"` field must match OpenRouter's model identifier (e.g., `anthropic/claude-sonnet-4`, `google/gemini-2.5-pro`).

```json theme={"system"}
"claude-sonnet-4-or": {
  "name": "anthropic/claude-sonnet-4",
  "displayName": "Claude Sonnet 4 (OpenRouter)",
  "capabilities": [],
  "options": {
    "temperature": 0.7,
    "maxOutputTokens": 8192
  }
}
```

<Tip>
  Use descriptive `displayName` values that include "(OpenRouter)" so you can distinguish these from Zencoder's built-in models in the selector.
</Tip>

## Keeping Zencoder Default Models

By default, OpenRouter models appear **alongside** Zencoder's built-in models. If you want to hide the built-in catalog and only show your OpenRouter models, add `"useDefaultProviders": false` at the top level:

```json theme={"system"}
{
  "useDefaultProviders": false,
  "providers": {
    "openrouter": { ... }
  }
}
```

## Securing Your API Key

Instead of storing your API key directly in the JSON file, you can use an environment variable:

1. Remove the `"apiKey"` field from the provider config
2. Export the key in your shell profile:

```bash theme={"system"}
export ZENCODER_OPENROUTER_API_KEY="your-openrouter-api-key"
```

Zencoder will automatically look for `ZENCODER_<PROVIDER>_API_KEY` if no inline key is found.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Models don't appear in the selector">
    Restart Zencoder or Zenflow after editing `settings.json`. Verify the JSON is valid — a missing comma or bracket will silently fail.
  </Accordion>

  <Accordion title="'Something went wrong' error">
    Check that your OpenRouter API key is valid and has sufficient credits. Verify the model `name` matches the exact identifier on [openrouter.ai/models](https://openrouter.ai/models).
  </Accordion>

  <Accordion title="Slow responses">
    Some OpenRouter models queue during peak hours. Try a different model or check [openrouter.ai/activity](https://openrouter.ai/activity) for current status.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Custom Models (BYOM)" icon="sliders" href="/features/custom-models-configuration">
    Full reference for configuring custom model providers
  </Card>

  <Card title="Model Selection & BYOK" icon="robot" href="/features/models">
    Built-in models and Bring Your Own Key setup
  </Card>
</CardGroup>


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.